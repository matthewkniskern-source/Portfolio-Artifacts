"""Opt-in local draft persistence and scoped bearer authorization.
No approval or risk acceptance operations; legacy workbench remains local advisory.
"""
import hashlib
import hmac
import json
import os
import re
from datetime import datetime, timezone

from flask import jsonify, request
from sqlalchemy import Column, Integer, String, Table, Text, UniqueConstraint, insert, select
from sqlalchemy.exc import IntegrityError

ROLE_ACTIONS = {
    "analyst": {"read", "write"},
    "contract_coordinator": {"read", "write"},
    "requirements_custodian": {"read", "write"},
    "auditor": {"read"},
    "administrator": set(),
}

def define(metadata):
    records=Table("roadmap_draft_records",metadata,
        Column("id",Integer,primary_key=True),
        Column("project_id",String(100),nullable=False),
        Column("kind",String(40),nullable=False),
        Column("record_key",String(100),nullable=False),
        Column("revision",String(40),nullable=False),
        Column("payload_json",Text(length=16777215),nullable=False),
        Column("payload_sha256",String(64),nullable=False),
        Column("created_by",String(100),nullable=False),
        Column("created_at",String(40),nullable=False),
        UniqueConstraint("project_id","kind","record_key","revision"))
    events=Table("roadmap_draft_events",metadata,
        Column("id",Integer,primary_key=True),
        Column("project_id",String(100),nullable=False),
        Column("record_id",Integer,nullable=False),
        Column("actor",String(100),nullable=False),
        Column("action",String(40),nullable=False),
        Column("created_at",String(40),nullable=False))
    return records,events

def principal(config, token, project, action):
    if not isinstance(config,list) or not isinstance(token,str) or len(token)<32 or len(token)>512:
        return None
    digest=hashlib.sha256(token.encode("utf-8")).hexdigest()
    matched=[]
    for row in config:
        if not isinstance(row,dict) or not isinstance(row.get("token_sha256"),str):
            return None
        if hmac.compare_digest(row["token_sha256"],digest):
            matched.append(row)
    if len(matched)!=1:
        return None
    row=matched[0]
    actor=row.get("id")
    if not isinstance(actor,str) or not re.fullmatch(r"[A-Za-z0-9_.-]{1,100}",actor):
        return None
    if not isinstance(row.get("projects"),list) or project not in row["projects"]:
        return None
    if action not in ROLE_ACTIONS.get(row.get("role"),set()):
        return None
    return actor

def register(app,engine,tables):
    from roadmap import contract_draft, mapping_draft, canonical, fingerprint, ident, FLAGS
    records,events=tables
    def authorized(project,action):
        if engine is None:
            return None
        try:
            config=json.loads(os.getenv("SGMA_ROADMAP_PRINCIPALS","[]"))
        except ValueError:
            return None
        header=request.headers.get("Authorization","")
        return principal(config,header[7:] if header.startswith("Bearer ") else "",project,action)

    @app.post("/roadmap/projects/<project>/drafts")
    def save_draft(project):
        project=ident(project)
        actor=authorized(project,"write")
        if not actor:
            return jsonify(error="Draft persistence unavailable or access denied"),403
        body=request.get_json()
        kind=body["kind"]
        key=ident(body["record_key"])
        rev=ident(body["revision"])
        if len(rev)>40:
            raise ValueError("Revision too long")
        if kind=="contract":
            payload=contract_draft(body["payload"])
            if payload["contract_id"]!=key or payload["revision"]!=rev:
                raise ValueError("Draft identity mismatch")
        elif kind=="mapping":
            payload=mapping_draft(body["payload"])
        else:
            raise ValueError("Unsupported draft kind")
        stamp=datetime.now(timezone.utc).isoformat()
        sha=fingerprint(payload)
        try:
            with engine.begin() as conn:
                record_id=conn.execute(insert(records).values(project_id=project,kind=kind,
                    record_key=key,revision=rev,payload_json=canonical(payload),payload_sha256=sha,
                    created_by=actor,created_at=stamp)).inserted_primary_key[0]
                conn.execute(insert(events).values(project_id=project,record_id=record_id,
                    actor=actor,action="DRAFT_CREATED",created_at=stamp))
        except IntegrityError:
            return jsonify(error="Draft revision already exists"),409
        return jsonify(id=record_id,payload_sha256=sha,**FLAGS),201

    @app.get("/roadmap/projects/<project>/drafts")
    def list_drafts(project):
        project=ident(project)
        if not authorized(project,"read"):
            return jsonify(error="Draft persistence unavailable or access denied"),403
        with engine.connect() as conn:
            rows=conn.execute(select(records).where(records.c.project_id==project)
                .order_by(records.c.id.desc()).limit(100)).mappings()
            output=[]
            for row in rows:
                data=dict(row)
                payload=json.loads(data.pop("payload_json"))
                if fingerprint(payload)!=data["payload_sha256"]:
                    return jsonify(error="Draft integrity check failed"),409
                data["payload"]=payload
                output.append(data)
        return jsonify(records=output,**FLAGS)
