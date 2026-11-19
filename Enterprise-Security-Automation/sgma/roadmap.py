"""Advisory roadmap workspace. No authenticated decisions or network resolution."""
import hashlib
import json
import re
from datetime import datetime, timezone
from uuid import uuid4
from pathlib import Path

VERSION = "1.2.3"
MAX_BYTES = 8_000_000
MAX_NODES = 100_000
ROOT = Path(__file__).resolve().parents[1]
FLAGS = {"approval":"NOT_APPROVED","deployment_authorized":False,
         "compliance_certified":False,"policy_changed":False}

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",",":"), ensure_ascii=False, allow_nan=False)

def fingerprint(value):
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()

def bounded(value):
    nodes = [(value, 0)]
    count = 0
    while nodes:
        node, depth = nodes.pop()
        count += 1
        if count > MAX_NODES or depth > 60:
            raise ValueError("Document exceeds structural limits")
        if isinstance(node, dict):
            nodes.extend((v, depth+1) for v in node.values())
        elif isinstance(node,list):
            nodes.extend((v,depth+1) for v in node)
    if len(canonical(value).encode("utf-8")) > MAX_BYTES:
        raise ValueError("Document exceeds size limit")
    return value

def string(value, limit=1000):
    if not isinstance(value,str) or not value.strip() or len(value)>limit:
        raise ValueError("Invalid text field")
    return value.strip()

def ident(value):
    value=string(value,100)
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*",value):
        raise ValueError("Invalid identifier")
    return value

def schema_status(document, model):
    # Only locally provisioned, pinned official schemas may be used. No network retrieval.
    path=ROOT/"interoperability"/"oscal"/"schemas"/VERSION/("oscal_"+model+"_schema.json")
    if not path.is_file():
        return "OFFICIAL_SCHEMA_NOT_PROVISIONED"
    try:
        import jsonschema
        from referencing import Registry
    except ImportError:
        return "VALIDATOR_NOT_INSTALLED"
    manifest=path.parent/"schema-manifest.json"
    if not manifest.is_file():
        return "SCHEMA_MANIFEST_MISSING"
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=json.loads(manifest.read_text(encoding="utf-8")).get(path.name):
        raise ValueError("Local schema fingerprint mismatch")
    schema=json.loads(raw)
    validator=jsonschema.validators.validator_for(schema)
    validator.check_schema(schema)
    try:
        validator(schema,registry=Registry(),format_checker=jsonschema.FormatChecker()).validate(document)
    except Exception as exc:
        raise ValueError("Official schema validation failed or reference unresolved") from exc
    return "SCHEMA_VALID_LOCAL_UNATTESTED"

def catalog(document):
    bounded(document)
    if not isinstance(document,dict) or set(document)!={"catalog"}:
        raise ValueError("Expected OSCAL catalog")
    source=document["catalog"]
    meta=source["metadata"]
    string(source["uuid"],100)
    version=string(meta["oscal-version"],40)
    rows=[]
    seen=set()
    def walk(node, parents):
        for control in node.get("controls",[]):
            cid=ident(control["id"])
            if cid in seen:
                raise ValueError("Duplicate control identifier")
            seen.add(cid)
            rows.append({"id":cid,"title":string(control["title"],4000),
                         "parents":parents,"parts":control.get("parts",[]),
                         "params":control.get("params",[])})
            walk(control,parents+[cid])
        for group in node.get("groups",[]):
            walk(group,parents+[ident(group["id"])])
    walk(source,[])
    if not rows:
        raise ValueError("No controls")
    return {"title":string(meta["title"],4000),"oscal_version":version,
            "catalog_sha256":fingerprint(document),"controls":rows,
            "schema_status":schema_status(document,"catalog") if version==VERSION else "VERSION_NOT_SUPPORTED_FOR_SCHEMA_VALIDATION",
            "projection":"PARTIAL_READ_ONLY_ORIGINAL_REQUIRED","original":document,**FLAGS}

def profile_export(document, selected):
    inspected=catalog(document)
    if not isinstance(selected,list) or not selected or any(not isinstance(x,str) for x in selected):
        raise ValueError("Select controls")
    if len(set(selected))!=len(selected) or not set(selected)<={x["id"] for x in inspected["controls"]}:
        raise ValueError("Unknown or duplicate selection")
    if inspected["oscal_version"]!=VERSION:
        raise ValueError("Profile generation requires matching OSCAL version")
    output={"profile":{"uuid":str(uuid4()),"metadata":{"title":"SGMA proposed selection",
        "last-modified":datetime.now(timezone.utc).isoformat(),"version":"1.0","oscal-version":VERSION},
        "imports":[{"href":"catalog.json","include-controls":[{"with-ids":selected}]}]}}
    return {"document":output,"catalog_filename":"catalog.json","catalog_sha256":inspected["catalog_sha256"],
            "schema_status":schema_status(output,"profile"),"resolution":"NOT_EXECUTED",**FLAGS}

def contract_draft(payload):
    bounded(payload)
    result={"contract_id":ident(payload["contract_id"]),"revision":ident(payload["revision"]),
            "customer":string(payload["customer"]),"requirements":[]}
    seen=set()
    for item in payload["requirements"]:
        rid=ident(item["id"])
        if rid in seen:
            raise ValueError("Duplicate requirement")
        seen.add(rid)
        method=item["method"]
        if method not in {"manual","automated","hybrid"}:
            raise ValueError("Invalid method")
        applicability=item.get("applicability","undetermined")
        if applicability not in {"applicable","undetermined","not_applicable"}:
            raise ValueError("Invalid applicability")
        rationale=item.get("rationale","")
        if applicability=="not_applicable":
            string(rationale)
        result["requirements"].append({"id":rid,"title":string(item["title"]),
            "clause":string(item["clause"]),"statement":string(item["statement"],10000),
            "method":method,"applicability":applicability,"rationale":rationale,
            "evidence":string(item["evidence"],4000),"deadline":item.get("deadline","")})
    if not result["requirements"]:
        raise ValueError("At least one contractual requirement is required")
    result.update(FLAGS)
    return result

def compare_contract(before, after):
    a,b=contract_draft(before),contract_draft(after)
    if a["contract_id"]!=b["contract_id"] or a["revision"]==b["revision"]:
        raise ValueError("Compare distinct revisions of the same contract")
    old={x["id"]:x for x in a["requirements"]}; new={x["id"]:x for x in b["requirements"]}
    return {"before_sha256":fingerprint(a),"after_sha256":fingerprint(b),
            "added":sorted(new.keys()-old.keys()),"removed":sorted(old.keys()-new.keys()),
            "changed":sorted(k for k in old.keys() & new.keys() if old[k]!=new[k]),
            "impact":"HUMAN_REVIEW_REQUIRED",**FLAGS}

def mapping_draft(payload):
    relation=payload["relationship"]
    if relation not in {"equivalent","partial","broader","narrower","related"}:
        raise ValueError("Invalid relation")
    return {"source":string(payload["source"]),"target":string(payload["target"]),
            "relationship":relation,"rationale":string(payload["rationale"],4000),
            "status":"PROPOSED_UNVERIFIED",**FLAGS}

def decision_queue(assessment):
    bounded(assessment)
    # Assessment exports do not contain occurrence identity. Do not conflate equal CVEs.
    rows=[]
    for row in assessment["requirements"]:
        if row["status"] not in {"GAP","RESIDUAL RISK","EVIDENCE MISSING","REVIEW REQUIRED","NO MATCHING FINDING"}:
            raise ValueError("Invalid assessment status")
        if row["status"]=="NO MATCHING FINDING":
            continue
        rows.append({"requirement_id":ident(row["id"]),"status":row["status"],
                     "finding_ids":row.get("finding_ids",[]),"owner":None,
                     "disposition":"PENDING_HUMAN_REVIEW"})
    return {"assessment_sha256":fingerprint(assessment),"source_trust":"USER_DECLARED_UNVERIFIED",
            "consolidation":"NOT_PERFORMED_WITHOUT_OCCURRENCE_IDENTITY","records":rows,**FLAGS}

def dashboard(queue):
    records=queue["records"]
    counts={}
    for row in records:
        counts[row["status"]]=counts.get(row["status"],0)+1
    return {"record_count":len(records),"counts":counts,"scope":"SINGLE_UNVERIFIED_ASSESSMENT",**FLAGS}

def compose_overlay(base, document, selected, draft, revision):
    """Create a new advisory project revision; imported obligations remain manual."""
    from copy import deepcopy
    from requirements_library import verify_profile
    from requirements_engine import validate
    bounded(base)
    validate(base)
    if verify_profile(base)["status"]!="REGISTRY_MATCH":
        raise ValueError("A registry-bound proposal is required")
    revision=ident(revision)
    if revision==base["revision"]:
        raise ValueError("Use a new project revision")
    result=deepcopy(base)
    result["revision"]=revision
    existing={row["id"] for group in ("baseline","overlays","manual") for row in result[group]}
    def add(row):
        if row["id"] in existing:
            raise ValueError("Duplicate proposed requirement")
        existing.add(row["id"])
        result["manual"].append(row)
    if document is not None:
        inspected=catalog(document)
        if not isinstance(selected,list) or not selected or any(not isinstance(x,str) for x in selected):
            raise ValueError("Select catalog controls")
        indexed={x["id"]:x for x in inspected["controls"]}
        if len(set(selected))!=len(selected) or not set(selected)<=indexed.keys():
            raise ValueError("Invalid selected controls")
        for cid in selected:
            control=indexed[cid]
            add({"id":"OSCAL-"+inspected["catalog_sha256"][:12]+"-"+cid,
                 "title":control["title"],"source":inspected["title"]+" / "+cid,
                 "applicability":"undetermined","source_sha256":inspected["catalog_sha256"],
                 "source_control_id":cid,"source_schema_status":inspected["schema_status"]})
    elif selected:
        raise ValueError("Selected controls require a catalog")
    if draft is not None:
        contract=contract_draft(draft)
        for row in contract["requirements"]:
            item={"id":row["id"],"title":row["title"],
                  "source":contract["contract_id"]+"@"+contract["revision"]+" / "+row["clause"],
                  "applicability":row["applicability"],"contract_sha256":fingerprint(contract),
                  "statement":row["statement"],"evidence":row["evidence"],
                  "requested_method":row["method"],"deadline":row["deadline"]}
            if row["rationale"]:
                item["rationale"]=row["rationale"]
            add(item)
    validate(result)
    verify_profile(result)
    return {"proposal":result,"proposal_sha256":fingerprint(result),
            "assessment_mapping":"MANUAL_REVIEW_ONLY",**FLAGS}

LIFECYCLE_MODELS={"component-definition","system-security-plan","assessment-plan",
                  "assessment-results","plan-of-action-and-milestones","control-mapping"}

def inspect_lifecycle(document):
    bounded(document)
    if not isinstance(document,dict) or len(document)!=1:
        raise ValueError("Expected one OSCAL document")
    model=next(iter(document))
    if model not in LIFECYCLE_MODELS:
        raise ValueError("Unsupported lifecycle model")
    body=document[model]
    meta=body["metadata"]
    version=string(meta["oscal-version"],40)
    schema_model=model
    return {"model":model,"title":string(meta["title"],4000),"oscal_version":version,
            "document_sha256":fingerprint(document),"schema_status":schema_status(document,schema_model) if version==VERSION else "VERSION_NOT_SUPPORTED_FOR_SCHEMA_VALIDATION",
            "reference_resolution":"NOT_EXECUTED","semantic_validation":"NOT_EXECUTED",
            "original":document,**FLAGS}

def register(app):
    from flask import jsonify, request, send_file
    @app.get("/roadmap")
    def roadmap_home():
        return send_file(ROOT/"sgma"/"roadmap.html")
    @app.get("/roadmap/capabilities")
    def roadmap_capabilities():
        return jsonify(mode="LOCAL_ADVISORY",authenticated=False,persistent=False,
                       lifecycle_exchange="NOT_IMPLEMENTED",**FLAGS)
    @app.post("/roadmap/catalog")
    def roadmap_catalog():
        return jsonify(catalog(request.get_json()))
    @app.post("/roadmap/profile")
    def roadmap_profile():
        p=request.get_json()
        return jsonify(profile_export(p["catalog"],p["selected"]))
    @app.post("/roadmap/contract")
    def roadmap_contract():
        return jsonify(contract_draft(request.get_json()))
    @app.post("/roadmap/compare")
    def roadmap_compare():
        p=request.get_json()
        return jsonify(compare_contract(p["before"],p["after"]))
    @app.post("/roadmap/mapping")
    def roadmap_mapping():
        return jsonify(mapping_draft(request.get_json()))
    @app.post("/roadmap/compose")
    def roadmap_compose():
        p=request.get_json()
        return jsonify(compose_overlay(p["base"],p.get("catalog"),p.get("selected",[]),p.get("contract"),p["revision"]))
    @app.post("/roadmap/lifecycle")
    def roadmap_lifecycle():
        return jsonify(inspect_lifecycle(request.get_json()))
    @app.post("/roadmap/decisions")
    def roadmap_decisions():
        queue=decision_queue(request.get_json())
        return jsonify(queue=queue,dashboard=dashboard(queue))
