"""Advisory roadmap workspace. No authenticated decisions or network resolution."""
import hashlib
import io
import zipfile
import json
import re
from datetime import datetime, timezone
from uuid import uuid4
from pathlib import Path
from provision_oscal import ASSET_SHA256

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

def schema_status(document, model, version=VERSION):
    version=version.removeprefix("v")
    if version not in ASSET_SHA256 or model not in ASSET_SHA256[version]:
        return "VERSION_NOT_SUPPORTED_FOR_SCHEMA_VALIDATION"
    path=ROOT/"interoperability"/"oscal"/"schemas"/version/("oscal_"+model+"_schema.json")
    if not path.is_file():
        return "OFFICIAL_SCHEMA_NOT_PROVISIONED"
    try:
        import jsonschema
        from referencing import Registry
    except ImportError:
        return "VALIDATOR_NOT_INSTALLED"
    if path.stat().st_size>4_000_000:
        raise ValueError("Schema file exceeds limit")
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=ASSET_SHA256[version][model]:
        raise ValueError("Local schema fingerprint mismatch")
    schema=json.loads(raw)
    validator=jsonschema.validators.validator_for(schema)
    validator.check_schema(schema)
    try:
        validator(schema,registry=Registry(),format_checker=jsonschema.FormatChecker()).validate(document)
    except Exception as exc:
        raise ValueError("Official schema validation failed or reference unresolved") from exc
    return "SCHEMA_VALID_LOCAL_UNATTESTED"

TEMPLATES={
    "nist-800-171-r3":{"title":"NIST SP 800-171 Rev. 3","file":"NIST_SP800-171_rev3_catalog.json","source_path":"nist.gov/SP800-171/rev3/json/NIST_SP800-171_rev3_catalog.json","upstream_git_blob":"1bc9d5ab5f57329c1ab5553b4d2b27ea54d9d13f"},
    "nist-csf-2":{"title":"NIST Cybersecurity Framework 2.0","file":"NIST_CSF_v2.0_catalog.json","source_path":"nist.gov/CSF/v2.0/json/NIST_CSF_v2.0_catalog.json","upstream_git_blob":"7b8b2d8b45cbf6fca093fcc5ae9f17ca9938b425"},
    "nist-ssdf":{"title":"NIST SP 800-218 SSDF","file":"NIST_SP800-218_ver1_catalog.json","source_path":"nist.gov/SP800-218/ver1/json/NIST_SP800-218_ver1_catalog.json","upstream_git_blob":"94f85f214557d4f52faddbf0b2e83de55d11db5d"},
}

def load_template(key):
    entry=TEMPLATES[key]
    path=ROOT/"interoperability"/"oscal"/"catalogs"/entry["file"]
    raw=path.read_bytes()
    if len(raw)>MAX_BYTES:
        raise ValueError("Catalog exceeds limit")
    result=catalog(json.loads(raw))
    result["template"]={**entry,"key":key,"content_release":"v1.5.0","source_file_sha256":hashlib.sha256(raw).hexdigest(),
                        "review_status":"PROPOSED_UNREVIEWED"}
    return result

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
            "schema_status":schema_status(document,"catalog",version),
            "projection":"PARTIAL_READ_ONLY_ORIGINAL_REQUIRED","original":document,**FLAGS}

def profile_export(document, selected):
    inspected=catalog(document)
    if not isinstance(selected,list) or not selected or any(not isinstance(x,str) for x in selected):
        raise ValueError("Select controls")
    if len(set(selected))!=len(selected) or not set(selected)<={x["id"] for x in inspected["controls"]}:
        raise ValueError("Unknown or duplicate selection")
    if inspected["oscal_version"].removeprefix("v") not in ASSET_SHA256:
        raise ValueError("Profile generation requires supported source OSCAL version")
    output={"profile":{"uuid":str(uuid4()),"metadata":{"title":"SGMA proposed selection",
        "last-modified":datetime.now(timezone.utc).isoformat(),"version":"1.0","oscal-version":VERSION},
        "imports":[{"href":"catalog.json","include-controls":[{"with-ids":selected}]}]}}
    return {"document":output,"catalog_filename":"catalog.json","catalog_sha256":inspected["catalog_sha256"],"source_oscal_version":inspected["oscal_version"],
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
        rule=item.get("rule")
        if rule is not None:
            from requirements_engine import SCANNERS, RANK
            if method=="manual" or not isinstance(rule,dict) or rule.get("scanner") not in SCANNERS or rule.get("threshold") not in RANK:
                raise ValueError("Invalid proposed automated rule")
            rule={"scanner":rule["scanner"],"threshold":rule["threshold"],"allow_exceptions":False}
        result["requirements"].append({"id":rid,"title":string(item["title"]),
            "clause":string(item["clause"]),"statement":string(item["statement"],10000),
            "method":method,"applicability":applicability,"rationale":rationale,
            "evidence":string(item["evidence"],4000),"deadline":item.get("deadline",""),"rule":rule})
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

def attach_occurrences(assessment,evidence):
    """Occurrence IDs are scoped to the exact normalized evidence document, never across runs."""
    from requirements_engine import rank, RANK
    if evidence is None:
        return assessment
    evidence_hash=fingerprint(evidence)
    occurrences=[]
    for index,finding in enumerate(evidence["findings"]):
        occurrence_id=fingerprint({"evidence_sha256":evidence_hash,"index":index})
        fields={k:finding[k] for k in ("scanner","id","target","resource","package","line","severity","disposition","exception_id") if k in finding}
        occurrences.append({"occurrence_id":occurrence_id,"source_index":index,**fields})
    for row in assessment["requirements"]:
        if row["status"] in {"GAP","RESIDUAL RISK"} and "scanner" in row:
            row["finding_occurrence_ids"]=[occ["occurrence_id"] for occ,finding in zip(occurrences,evidence["findings"])
                if finding["scanner"]==row["scanner"] and rank(finding)>=RANK[row["threshold"]]]
        else:
            row["finding_occurrence_ids"]=[]
    assessment["finding_occurrences"]=occurrences
    assessment["normalized_evidence_sha256"]=evidence_hash
    return assessment

def decision_queue(assessment):
    bounded(assessment)
    occurrences=assessment.get("finding_occurrences")
    by_occurrence={}
    if occurrences is not None:
        if not isinstance(occurrences,list):
            raise ValueError("Invalid occurrence inventory")
        for item in occurrences:
            key=item["occurrence_id"]
            if not isinstance(key,str) or not re.fullmatch(r"[0-9a-f]{64}",key) or key in by_occurrence:
                raise ValueError("Invalid occurrence identifier")
            by_occurrence[key]=item
    rows=[]
    groups={}
    seen=set()
    for row in assessment["requirements"]:
        rid=ident(row["id"])
        status=row["status"]
        if rid in seen:
            raise ValueError("Duplicate requirement identifier")
        seen.add(rid)
        if status not in {"GAP","RESIDUAL RISK","EVIDENCE MISSING","REVIEW REQUIRED","NO MATCHING FINDING"}:
            raise ValueError("Invalid assessment status")
        if status=="NO MATCHING FINDING":
            continue
        refs=row.get("finding_occurrence_ids",[])
        if not isinstance(refs,list) or len(set(refs))!=len(refs) or any(key not in by_occurrence for key in refs):
            raise ValueError("Unknown or duplicate occurrence references")
        if refs and status in {"GAP","RESIDUAL RISK"}:
            for key in refs:
                groups.setdefault(key,[]).append({"requirement_id":rid,"status":status})
        else:
            rows.append({"record_id":"requirement:"+rid,"requirement_id":rid,"status":status,
                         "finding_ids":row.get("finding_ids",[]),"owner":None,
                         "disposition":"PENDING_HUMAN_REVIEW"})
    for key,requirements in groups.items():
        rows.append({"record_id":key,"occurrence":by_occurrence[key],"requirements":requirements,
                     "status":"GAP" if any(x["status"]=="GAP" for x in requirements) else "RESIDUAL RISK",
                     "owner":None,"disposition":"PENDING_HUMAN_REVIEW"})
    return {"assessment_sha256":fingerprint(assessment),"source_trust":"USER_DECLARED_UNVERIFIED",
            "consolidation":"WITHIN_EVIDENCE_DOCUMENT" if occurrences is not None else "NOT_PERFORMED_WITHOUT_OCCURRENCE_IDENTITY",
            "records":rows,**FLAGS}

def dashboard(queue):
    records=queue["records"]
    counts={}
    for row in records:
        counts[row["status"]]=counts.get(row["status"],0)+1
    return {"record_count":len(records),"counts":counts,"scope":"SINGLE_UNVERIFIED_ASSESSMENT",**FLAGS}

def compose_overlay(base, document, selected, draft, revision, selections=None):
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
    def add(row, group="manual"):
        if row["id"] in existing:
            raise ValueError("Duplicate proposed requirement")
        existing.add(row["id"])
        result[group].append(row)
    inputs=[] if selections is None else selections
    if not isinstance(inputs,list) or len(inputs)>10:
        raise ValueError("Invalid catalog selections")
    inputs=list(inputs)
    if document is not None:
        inputs.append({"catalog":document,"selected":selected})
    elif selected:
        raise ValueError("Selected controls require a catalog")
    source_hashes=set()
    for item in inputs:
        if not isinstance(item,dict):
            raise ValueError("Invalid catalog selection")
        inspected=load_template(item["template"]) if "template" in item else catalog(item["catalog"])
        selected=item["selected"]
        if inspected["catalog_sha256"] in source_hashes:
            raise ValueError("Duplicate catalog selection")
        source_hashes.add(inspected["catalog_sha256"])
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
            if row["method"] in {"automated","hybrid"} and row["rule"] is not None:
                add({**item,**row["rule"]},"overlays")
                if row["method"]=="hybrid":
                    add({**item,"id":item["id"]+"-manual","title":item["title"]+" (manual evidence review)"})
            else:
                add(item)
    validate(result)
    verify_profile(result)
    return {"proposal":result,"proposal_sha256":fingerprint(result),
            "assessment_mapping":"EXPLICIT_RULES_OR_MANUAL_REVIEW",**FLAGS}

def contract_catalog(draft):
    """Represent the authored obligations; SGMA evaluation rules remain explicit extensions."""
    item=contract_draft(draft)
    return requirements_catalog(item["contract_id"]+" — proposed revision "+item["revision"],
                                item["revision"],item["requirements"])

def requirements_catalog(title, revision, rows):
    namespace="https://github.com/matthewkniskern-source/Portfolio-Artifacts/sgma"
    controls=[]
    used=set()
    for row in rows:
        rid=ident(row["id"])
        if rid in used:
            raise ValueError("Duplicate catalog identifier")
        used.add(rid)
        props=[]
        for k in ("source","clause","applicability","method","requested_method","evidence","deadline","rationale"):
            if row.get(k):
                props.append({"name":k.replace("_","-"),"ns":namespace,"value":str(row[k])})
        rule=row.get("rule") or row
        for k in ("scanner","threshold","allow_exceptions"):
            if k in rule:
                props.append({"name":k.replace("_","-"),"ns":namespace,"value":str(rule[k]).lower() if isinstance(rule[k],bool) else str(rule[k])})
        control={"id":rid,"title":string(row["title"],4000),
                 "parts":[{"name":"statement","prose":row.get("statement") or row["title"]}]}
        if props:
            control["props"]=props
        controls.append(control)
    if not controls:
        raise ValueError("Empty catalog")
    return {"catalog":{"uuid":str(uuid4()),"metadata":{"title":title,"version":revision,
        "last-modified":datetime.now(timezone.utc).isoformat(),"oscal-version":VERSION},
        "controls":controls}}

def exchange_bundle(payload):
    """Package local-reference OSCAL candidates and the matching native proposal."""
    base=payload["base"]
    inputs=payload.get("selections",[])
    draft=payload.get("contract")
    composed=compose_overlay(base,None,[],draft,payload["revision"],inputs)
    native=composed["proposal"]
    # Existing project requirements (including the mandatory baseline) are one SGMA catalog.
    base_rows=[row for group in ("baseline","overlays","manual") for row in base[group]]
    sources=[(requirements_catalog("SGMA project obligations (proposed)",base["revision"],base_rows),
              [row["id"] for row in base_rows])]
    for selection in inputs:
        doc=load_template(selection["template"])["original"] if "template" in selection else selection["catalog"]
        sources.append((doc,selection["selected"]))
    if draft is not None:
        doc=contract_catalog(draft)
        sources.append((doc,[row["id"] for row in contract_draft(draft)["requirements"]]))
    files={}
    seen=set()
    imports=[]
    statuses={}
    for index,(doc,selected) in enumerate(sources):
        inspected=catalog(doc)
        if set(selected)&seen:
            raise ValueError("Cross-catalog identifier conflict; reconcile before profile exchange")
        seen.update(selected)
        name="catalog-"+str(index+1)+".json"
        files[name]=doc
        statuses[name]=inspected["schema_status"]
        imports.append({"href":name,"include-controls":[{"with-ids":selected}]})
    profile={"profile":{"uuid":str(uuid4()),"metadata":{"title":"SGMA project profile — proposed",
             "last-modified":datetime.now(timezone.utc).isoformat(),"version":native["revision"],"oscal-version":VERSION},
             "imports":imports}}
    files["profile.json"]=profile
    statuses["profile.json"]=schema_status(profile,"profile")
    files["sgma-proposal.json"]=native
    output=io.BytesIO()
    encoded={name:(json.dumps(doc,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+"\n").encode("utf-8")
             for name,doc in files.items()}
    manifest={"schema_version":1,"files":{name:{"sha256":hashlib.sha256(raw).hexdigest(),"bytes":len(raw)}
                  for name,raw in encoded.items()},"schema_status":statuses,"resolution":"NOT_EXECUTED",
              "source_preservation":"JSON_CONTENT_NOT_ORIGINAL_BYTE_STREAM","native_proposal_sha256":composed["proposal_sha256"],**FLAGS}
    encoded["exchange-manifest.json"]=(json.dumps(manifest,indent=2,sort_keys=True)+"\n").encode("utf-8")
    if sum(len(raw) for raw in encoded.values())>MAX_BYTES:
        raise ValueError("Exchange package exceeds limit")
    with zipfile.ZipFile(output,"w",compression=zipfile.ZIP_DEFLATED) as archive:
        for name,raw in encoded.items():
            archive.writestr(name,raw)
    output.seek(0)
    return output

def decision_draft(payload):
    bounded(payload)
    queue_sha=string(payload["assessment_sha256"],64)
    if not re.fullmatch(r"[0-9a-f]{64}",queue_sha):
        raise ValueError("Invalid assessment fingerprint")
    action=payload["proposed_action"]
    if action not in {"investigate","remediate","collect_evidence","review_exception","review_applicability"}:
        raise ValueError("Invalid proposed action")
    due=payload.get("due_date","")
    if due:
        from datetime import date
        date.fromisoformat(due)
    return {"assessment_sha256":queue_sha,"record_id":string(payload["record_id"],200),
            "proposed_owner":ident(payload["proposed_owner"]),"proposed_action":action,
            "due_date":due,"rationale":string(payload["rationale"],4000),
            "decision_state":"PENDING_HUMAN_REVIEW",**FLAGS}

LIFECYCLE_MODELS={"component-definition","system-security-plan","assessment-plan",
                  "assessment-results","plan-of-action-and-milestones","mapping-collection"}

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
    schema_model={"component-definition":"component","system-security-plan":"ssp",
                  "plan-of-action-and-milestones":"poam","mapping-collection":"mapping"}.get(model,model)
    return {"model":model,"title":string(meta["title"],4000),"oscal_version":version,
            "document_sha256":fingerprint(document),"schema_status":schema_status(document,schema_model,version),
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
    @app.get("/roadmap/templates")
    def roadmap_templates():
        return jsonify(templates=[{"key":key,**entry} for key,entry in TEMPLATES.items()],**FLAGS)
    @app.get("/roadmap/templates/<key>")
    def roadmap_template(key):
        return jsonify(load_template(key))
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
        return jsonify(compose_overlay(p["base"],p.get("catalog"),p.get("selected",[]),p.get("contract"),p["revision"],p.get("selections")))
    @app.post("/roadmap/lifecycle")
    def roadmap_lifecycle():
        return jsonify(inspect_lifecycle(request.get_json()))
    @app.post("/roadmap/contract-catalog")
    def roadmap_contract_catalog():
        document=contract_catalog(request.get_json())
        return jsonify(document=document,schema_status=schema_status(document,"catalog"),**FLAGS)
    @app.post("/roadmap/exchange")
    def roadmap_exchange():
        return send_file(exchange_bundle(request.get_json()),mimetype="application/zip",as_attachment=True,download_name="sgma-oscal-exchange.zip")
    @app.post("/roadmap/decision-draft")
    def roadmap_decision_draft():
        return jsonify(decision_draft(request.get_json()))
    @app.post("/roadmap/decisions")
    def roadmap_decisions():
        queue=decision_queue(request.get_json())
        return jsonify(queue=queue,dashboard=dashboard(queue))
