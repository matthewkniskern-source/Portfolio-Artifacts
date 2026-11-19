"""SGMA local-only application. No deployment or risk acceptance authority."""
import argparse
import getpass
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

from flask import Flask, abort, jsonify, request, send_file
from sqlalchemy import (Column, ForeignKey, Integer, MetaData, String, Table,
                        Text, UniqueConstraint, create_engine, insert, select, text)
from sqlalchemy.engine import URL
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "governance"))
from requirements_engine import assess
sys.path.insert(0, str(ROOT / "security"))
from evidence_import import verify_package, LIMIT as ARCHIVE_LIMIT

metadata = MetaData()
projects = Table("projects", metadata, Column("id", String(100), primary_key=True),
                 Column("created_at", String(40), nullable=False))
revisions = Table("profile_revisions", metadata, Column("id", Integer, primary_key=True),
                  Column("project_id", String(100), ForeignKey("projects.id"), nullable=False),
                  Column("revision", String(40), nullable=False),
                  Column("proposal_json", Text(length=16777215), nullable=False),
                  Column("proposal_sha256", String(64), nullable=False),
                  Column("created_at", String(40), nullable=False),
                  UniqueConstraint("project_id", "revision"))
assessments = Table("assessments", metadata, Column("id", Integer, primary_key=True),
                    Column("revision_id", Integer, ForeignKey("profile_revisions.id"), nullable=False),
                    Column("evidence_json", Text(length=16777215)),
                    Column("evidence_sha256", String(64)),
                    Column("scanned_json", Text, nullable=False),
                    Column("assessment_json", Text(length=16777215), nullable=False),
                    Column("assessment_sha256", String(64), nullable=False),
                    Column("created_at", String(40), nullable=False))
audit = Table("audit_events", metadata, Column("id", Integer, primary_key=True),
              Column("assessment_id", Integer, ForeignKey("assessments.id"), nullable=False),
              Column("event_type", String(60), nullable=False),
              Column("actor", String(80), nullable=False),
              Column("created_at", String(40), nullable=False))

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)

def digest(value):
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()

def now():
    return datetime.now(timezone.utc).isoformat()

def example():
    return json.loads((ROOT / "governance/profiles/synthetic-project-a.json").read_text(encoding="utf-8"))

def config_engine(prompt=False):
    if os.getenv("SGMA_MODE", "local") != "local":
        raise RuntimeError("Remote deployment is disabled until authentication and RBAC are implemented")
    password = os.getenv("SGMA_DB_PASSWORD")
    if password is None and prompt:
        password = getpass.getpass("MySQL database password: ")
    if not password:
        raise RuntimeError("Set SGMA_DB_PASSWORD or use an interactive password prompt")
    user = os.getenv("SGMA_DB_USER", "sgma_app")
    host = os.getenv("SGMA_DB_HOST", "127.0.0.1")
    ca = os.getenv("SGMA_DB_TLS_CA")
    if host not in {"127.0.0.1", "localhost", "::1"} and not ca:
        raise RuntimeError("Remote MySQL requires a trusted TLS CA")
    options = {"connect_timeout": 5}
    if ca:
        options["ssl"] = {"ca": ca, "check_hostname": True}
    url = URL.create("mysql+pymysql", username=user, password=password, host=host,
                     port=int(os.getenv("SGMA_DB_PORT", "3306")), database=os.getenv("SGMA_DB_NAME", "sgma"),
                     query={"charset":"utf8mb4"})
    return create_engine(url, pool_pre_ping=True, pool_recycle=1800, connect_args=options)

def evaluate(payload):
    if not isinstance(payload, dict):
        raise ValueError("JSON object required")
    profile = payload["profile"]
    if profile["baseline"] != example()["baseline"]:
        raise ValueError("Organizational baseline must match the repository-controlled baseline")
    required = next(r for r in example()["manual"] if r["id"] == "MAN-002")
    if required not in profile["manual"]:
        raise ValueError("Organizational manual requirement MAN-002 cannot be changed or removed")
    for key, limit in (("profile_id",100),("revision",40)):
        if not isinstance(profile.get(key),str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,"+str(limit-1)+"}",profile[key]):
            raise ValueError("Invalid "+key)
    evidence = payload.get("evidence")
    scanned = payload.get("scanned", [])
    if not isinstance(scanned,list) or any(not isinstance(s,str) for s in scanned):
        raise ValueError("Invalid scanner completion declaration")
    result = assess(profile, evidence, scanned)
    result["evidence_trust"] = "USER_DECLARED_UNVERIFIED" if evidence is not None else "NOT_SUPPLIED"
    return result

def create_app(engine):
    app = Flask(__name__)
    app.config.update(MAX_CONTENT_LENGTH=1_000_000, TRUSTED_HOSTS=["127.0.0.1","localhost"])
    @app.before_request
    def guard():
        if request.method == "POST":
            if request.headers.get("Origin") not in (None, request.host_url.rstrip("/")):
                abort(403)
            if request.path == "/assess-package":
                request.max_content_length = ARCHIVE_LIMIT + 1_000_000
                if request.mimetype != "multipart/form-data":
                    abort(415)
            elif not request.is_json:
                abort(415)
    @app.after_request
    def headers(response):
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Content-Security-Policy"] = "default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'"
        return response
    @app.errorhandler(ValueError)
    @app.errorhandler(KeyError)
    @app.errorhandler(TypeError)
    @app.errorhandler(AttributeError)
    def invalid(_exc):
        return jsonify(error="Invalid proposal or evidence; verify schema, baseline, identifiers and required fields."), 400
    @app.errorhandler(IntegrityError)
    def conflict(_exc):
        return jsonify(error="Concurrent save or revision conflict; retry or create a new revision."), 409
    @app.errorhandler(SQLAlchemyError)
    def database_error(_exc):
        return jsonify(error="Database unavailable; check server and application permissions."), 503
    @app.get("/")
    def home():
        return send_file(ROOT / "sgma/workbench.html")
    @app.get("/profile")
    def profile():
        return jsonify(example())
    @app.get("/health")
    def health():
        if engine is None:
            return jsonify(status="ready", mode="preview", authenticated=False, persistent=False)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            conn.execute(select(projects.c.id).limit(1))
        return jsonify(status="ready", mode="local", authenticated=False)
    @app.post("/assess")
    def assessment():
        return jsonify(evaluate(request.get_json()))
    @app.post("/assess-package")
    def assess_package():
        profile = json.loads(request.form["profile"])
        package = verify_package(request.files["archive"].stream.read(ARCHIVE_LIMIT + 1))
        result = evaluate({"profile": profile, "evidence": package["evidence"], "scanned": package["scanned"]})
        result["evidence_trust"] = "MANIFEST_MATCH_UNAUTHENTICATED"
        result["evidence_package"] = {key: value for key, value in package.items() if key != "evidence"}
        result["project_association"] = "PROPOSED_UNVERIFIED"
        return jsonify(result)
    @app.post("/save")
    def save():
        if engine is None:
            return jsonify(error="Persistent storage is disabled in preview mode."), 503
        payload = request.get_json()
        result = evaluate(payload)
        profile = payload["profile"]
        evidence = payload.get("evidence")
        project_id, revision = profile["profile_id"], profile["revision"]
        fingerprint = digest(profile)
        stamp = now()
        with engine.begin() as conn:
            existing = conn.execute(select(projects.c.id).where(projects.c.id == project_id)).first()
            if existing is None:
                conn.execute(insert(projects).values(id=project_id, created_at=stamp))
            old = conn.execute(select(revisions).where(revisions.c.project_id == project_id, revisions.c.revision == revision)).mappings().first()
            if old:
                if old["proposal_sha256"] != fingerprint:
                    return jsonify(error="This revision already exists with different content. Increment revision before saving."), 409
                revision_id = old["id"]
            else:
                revision_id = conn.execute(insert(revisions).values(project_id=project_id, revision=revision, proposal_json=canonical(profile), proposal_sha256=fingerprint, created_at=stamp)).inserted_primary_key[0]
            assessment_id = conn.execute(insert(assessments).values(revision_id=revision_id, evidence_json=canonical(evidence) if evidence is not None else None, evidence_sha256=digest(evidence) if evidence is not None else None, scanned_json=canonical(payload.get("scanned",[])), assessment_json=canonical(result), assessment_sha256=digest(result), created_at=stamp)).inserted_primary_key[0]
            conn.execute(insert(audit).values(assessment_id=assessment_id,event_type="ASSESSMENT_SAVED",actor="local-operator-unverified",created_at=stamp))
        return jsonify(assessment_id=assessment_id, revision_id=revision_id, assessment_sha256=digest(result), result=result), 201
    @app.get("/history")
    def history():
        if engine is None:
            return jsonify(error="Persistent storage is disabled in preview mode."), 503
        with engine.connect() as conn:
            rows=conn.execute(select(assessments.c.id, revisions.c.project_id, revisions.c.revision, assessments.c.created_at, assessments.c.assessment_sha256).join_from(assessments,revisions).order_by(assessments.c.id.desc()).limit(100)).mappings()
            return jsonify([dict(row) for row in rows])
    @app.get("/history/<int:assessment_id>")
    def load(assessment_id):
        if engine is None:
            return jsonify(error="Persistent storage is disabled in preview mode."), 503
        with engine.connect() as conn:
            row=conn.execute(select(assessments, revisions.c.proposal_json, revisions.c.proposal_sha256).join_from(assessments,revisions).where(assessments.c.id==assessment_id)).mappings().first()
        if row is None:
            abort(404)
        proposal=json.loads(row["proposal_json"])
        outcome=json.loads(row["assessment_json"])
        evidence=json.loads(row["evidence_json"]) if row["evidence_json"] else None
        if digest(proposal)!=row["proposal_sha256"] or digest(outcome)!=row["assessment_sha256"] or (evidence is not None and digest(evidence)!=row["evidence_sha256"]):
            return jsonify(error="Stored record integrity check failed"), 409
        return jsonify(profile=proposal, result=outcome, evidence=evidence, scanned=json.loads(row["scanned_json"]), created_at=row["created_at"])
    return app

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("command", choices=["init-db","serve","preview"])
    args=parser.parse_args()
    if args.command == "preview":
        from waitress import serve
        print("SGMA nonpersistent preview: http://127.0.0.1:8765")
        serve(create_app(None), host="127.0.0.1", port=8765)
        return
    engine=config_engine(prompt=True)
    if args.command=="init-db":
        metadata.create_all(engine)
        print("Initial SGMA schema created or already present; no existing tables modified.")
        return
    if os.getenv("SGMA_DB_USER","sgma_app") in {"root","admin"}:
        raise RuntimeError("Use a dedicated restricted application account")
    from waitress import serve
    host="0.0.0.0" if os.getenv("SGMA_CONTAINER_LOCAL")=="1" else "127.0.0.1"
    print("SGMA local prototype: http://127.0.0.1:8765")
    serve(create_app(engine),host=host,port=8765)

if __name__=="__main__":
    main()
