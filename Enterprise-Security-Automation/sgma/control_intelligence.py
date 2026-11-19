"""Source-identified, local, read-only control intelligence. No compliance inference."""
import hashlib
import json
from roadmap import ROOT, TEMPLATES, bounded, fingerprint, FLAGS, load_template

EXTRACT = "NIST_800-53_r5.2.0_OT_reference_extract.json"
EXTRACT_BLOB = "0fe2c3cfc2717472f1c97bfadd603a223dbfbdd0"
UPSTREAM_BLOB = "8ebe3c91181cc078d40e39bcf34ea233e652d025"
# Git IDs above are provenance metadata only; these independent raw-byte pins enforce integrity.
EXTRACT_SHA256 = "694aa7df1678905eae725e6c73087775a8b54d5a7ecc488e9572e865e7713483"
UPSTREAM_SHA256 = "01f37cf90ea99d92242c936cbfbdebcc338eef1f71454e2acac36cc56e9bc062"
CATALOG_SHA256 = {
    "nist-800-171-r3": "21b6f3b118b6e5b305aaed3a0e4b70fa5d1d9aa388a0b92e7d6ddfed69e93ac3",
    "nist-csf-2": "4836943f21d393f2821df85ada4e6f3c0617243b4ddf44263fe68205400210b4",
    "nist-ssdf": "b01634a5fdb382e7a12660c379a4d0bc3a2b8e29abccf2861834880005137117",
}
NIST53 = "nist-800-53-r5.2.0-extract"
OT = "sgma-ot-800-82-r3"
CSF = "nist-csf-2"
CUI = "nist-800-171-r3"
CATALOG_PATH = ROOT / "interoperability" / "oscal" / "catalogs"
SOURCE_CLASSES = {"UPSTREAM_CATALOG", "UPSTREAM_CONTROL_EXTRACT", "SGMA_DERIVED_UNREVIEWED"}
# Candidate relationships are explicitly scoped and directional, never equivalences.
CROSSWALKS = [
    ("OT-01", CSF, "ID.AM-01", "Hardware inventory overlap; software and OT criticality still require review."),
    ("OT-01", CSF, "ID.AM-02", "Software and system inventory overlap; reconcile hardware scope separately."),
    ("OT-03", CUI, "SP_800_171_03.04.01", "Baseline configuration overlap; industrial controller logic and CUI scope need separate review."),
    ("OT-04", CUI, "SP_800_171_03.04.03", "Configuration change control overlap; operational safety and maintenance restrictions need review."),
    ("OT-05", CSF, "PR.IR-01", "Network protection and boundary segregation overlap; validate industrial communications."),
    ("OT-05", CUI, "SP_800_171_03.13.01", "Boundary protection overlap; CUI applicability and zones/conduits remain distinct."),
    ("OT-06", CUI, "SP_800_171_03.01.12", "Remote access overlap; vendor maintenance and operational coordination remain distinct."),
    ("OT-07", CSF, "PR.AA-05", "Least-privilege authorization overlap; engineering and operator roles need review."),
    ("OT-07", CUI, "SP_800_171_03.01.05", "Least-privilege overlap; CUI and OT asset scopes need review."),
    ("OT-08", CSF, "PR.AA-06", "Physical access overlap; specific plant equipment protection must be assessed."),
    ("OT-10", CSF, "ID.RA-01", "Vulnerability identification overlap; SGMA OT guidance restricts active testing."),
    ("OT-11", CUI, "SP_800_171_03.14.01", "Flaw remediation overlap; operational safety, compatibility and maintenance constraints need review."),
    ("OT-12", CSF, "PR.DS-11", "Backup and testing overlap; logic/configuration and recovery requirements need review."),
    ("OT-13", CSF, "RC.RP-01", "Recovery overlap; local operation and safe process state are distinct considerations."),
    ("OT-18", CSF, "GV.SC-07", "Supplier risk overlap; component support and firmware provenance need review."),
    ("OT-18", CUI, "SP_800_171_03.17.01", "Supply chain risk overlap; CUI and industrial lifecycle scope need review."),
    ("OT-20", CUI, "SP_800_171_03.12.01", "Assessment overlap; commissioning and operator acceptance need separate evidence."),
]
REFERENCES = [
    {"id":"nist-82-r3","title":"NIST SP 800-82 Rev. 3, Appendix F","url":"https://csrc.nist.gov/projects/risk-management/sp800-53-controls/scor-overview/current-overlays","status":"REFERENCE_ONLY_NOT_INGESTED","scope":"Final OT low/moderate/high overlay; not represented by the SGMA candidate catalog"},
    {"id":"nist-82-r4-ipd","title":"NIST SP 800-82 Rev. 4 initial public draft","url":"https://csrc.nist.gov/pubs/sp/800/82/r4/ipd","status":"DRAFT_REFERENCE_ONLY","scope":"Never substituted for a final publication"},
    {"id":"iec-62443","title":"ISA/IEC 62443 series","url":"https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards","status":"LICENSED_REFERENCE_ONLY","scope":"Part, edition and licensing review required; no standard text bundled"},
]

def verify_sha256(raw, expected):
    actual=hashlib.sha256(raw).hexdigest()
    if actual!=expected:
        raise ValueError("Pinned SHA-256 content integrity mismatch")
    return actual

def reference_extract():
    path=CATALOG_PATH/EXTRACT
    if path.stat().st_size>4_000_000:
        raise ValueError("Reference extract exceeds limit")
    raw=path.read_bytes()
    digest=verify_sha256(raw,EXTRACT_SHA256)
    data=json.loads(raw)
    if data["source"]["git_blob"]!=UPSTREAM_BLOB or len(data["controls"])!=20:
        raise ValueError("Unexpected reference extract")
    return data,digest

def node_id(source,cid):
    return source+":"+cid

def walk_controls(control,parents):
    yield control,parents
    for child in control.get("controls",[]):
        yield from walk_controls(child,parents+[control["id"]])

def build_library():
    sources={}
    nodes={}
    details={}
    def add(source,cid,title,parents,parts,params,props,raw=None):
        key=node_id(source,cid)
        if key in nodes:
            raise ValueError("Duplicate source-scoped control")
        record={"node_id":key,"source":source,"control_id":cid,"title":title,"parents":parents,
                "source_sha256":sources[source]["content_sha256"],"source_class":sources[source]["source_class"]}
        nodes[key]=record
        details[key]={**record,"parts":parts,"params":params,"props":props}
        if raw is not None:
            details[key]["source_control"]=raw
    for key,entry in TEMPLATES.items():
        path=CATALOG_PATH/entry["file"]
        if path.stat().st_size>8_000_000:
            raise ValueError("Catalog exceeds size limit")
        raw=path.read_bytes()
        expected=entry.get("upstream_git_blob")
        if expected:
            if key not in CATALOG_SHA256:
                raise ValueError("Missing pinned upstream catalog SHA-256")
            verify_sha256(raw,CATALOG_SHA256[key])
        template=load_template(key)
        metadata=template["original"]["catalog"]["metadata"]
        actual_sha256=hashlib.sha256(raw).hexdigest()
        if actual_sha256!=template["template"]["source_file_sha256"]:
            raise ValueError("Catalog changed during load")
        sources[key]={"id":key,"title":template["title"],"revision":metadata["version"],
            "release":template["template"]["content_release"],"oscal_version":template["oscal_version"],
            "source_class":"UPSTREAM_CATALOG" if expected else "SGMA_DERIVED_UNREVIEWED",
            "raw_sha256":actual_sha256,"content_sha256":template["catalog_sha256"],
            "git_blob":expected,"source_path":entry["source_path"],
            "status":"SOURCE_IDENTITY_MATCH" if expected else "DERIVED_UNREVIEWED",
            "schema_status":template["schema_status"]}
        for item in template["controls"]:
            add(key,item["id"],item["title"],item["parents"],item["parts"],item["params"],item["props"])
    extract,raw_hash=reference_extract()
    metadata=extract["source"]["metadata"]
    sources[NIST53]={"id":NIST53,"title":metadata["title"],"revision":metadata["version"],
        "release":extract["source"]["release"],"oscal_version":metadata["oscal-version"],
        "source_class":"UPSTREAM_CONTROL_EXTRACT","status":"PINNED_PARTIAL_EXTRACT",
        "raw_sha256":raw_hash,"content_sha256":fingerprint(extract),
        "git_blob":UPSTREAM_BLOB,"extract_git_blob":EXTRACT_BLOB,
        "upstream_raw_sha256":UPSTREAM_SHA256,
        "source_path":extract["source"]["path"],"schema_status":"NOT_STANDALONE_OSCAL_CATALOG"}
    for entry in extract["controls"]:
        for control,parents in walk_controls(entry["control"],[entry["family"]]):
            add(NIST53,control["id"],control["title"],parents,control.get("parts",[]),
                control.get("params",[]),control.get("props",[]),control)
    edges=[]
    def edge(a,b,rationale):
        if a not in nodes or b not in nodes:
            raise ValueError("Mapping references absent source control")
        record={"source_node":a,"target_node":b,"relationship":"related",
                "review_status":"PROPOSED_UNREVIEWED","rationale":rationale,
                "source_sha256":nodes[a]["source_sha256"],"target_sha256":nodes[b]["source_sha256"],
                "evidence_transfer":"NOT_AUTHORIZED","transitive_inference":False}
        edges.append({"edge_id":fingerprint(record),**record})
    for key,record in details.items():
        if record["source"]==OT:
            props={p["name"]:p["value"] for p in record["props"]}
            edge(key,node_id(NIST53,props["candidate-control-reference"].lower()),
                 "SGMA engineering objective references this NIST control; related only, not a reviewed equivalence or Appendix F tailoring.")
    for a,source,b,rationale in CROSSWALKS:
        edge(node_id(OT,a),node_id(source,b),rationale)
    return sources,nodes,details,edges

def library():
    sources,nodes,_,edges=build_library()
    counts={key:sum(n["source"]==key for n in nodes.values()) for key in sources}
    return {"sources":[{**value,"control_count":counts[key]} for key,value in sources.items()],
            "references":REFERENCES,"nodes":list(nodes.values()),"edges":edges,
            "counts":{"nodes":len(nodes),"edges":len(edges),"sources":len(sources)},
            "mapping_status":"ADVISORY_ONLY",**FLAGS}

def control_detail(key):
    _,nodes,details,edges=build_library()
    if key not in nodes:
        raise ValueError("Unknown source-scoped control")
    adjacent=[{**e,"other_node":nodes[e["target_node"] if e["source_node"]==key else e["source_node"]]}
              for e in edges if key in (e["source_node"],e["target_node"])]
    return {"control":details[key],"relationships":adjacent,**FLAGS}

def impact(payload):
    bounded(payload)
    _,nodes,_,edges=build_library()
    changed=payload["changed_nodes"]
    if not isinstance(changed,list) or not changed or any(not isinstance(x,str) or x not in nodes for x in changed) or len(set(changed))!=len(changed):
        raise ValueError("Invalid changed source nodes")
    rows=[]
    for key in changed:
        related=sorted({e["target_node"] if e["source_node"]==key else e["source_node"]
                        for e in edges if key in (e["source_node"],e["target_node"])})
        rows.append({"changed_node":key,"direct_review_candidates":related})
    return {"review_candidates":rows,"scope":"ONE_HOP_ONLY_HYPOTHETICAL_CHANGE",
            "affected_projects":"NOT_EVALUATED","review_state":"PENDING_HUMAN_REVIEW",**FLAGS}

def register(app):
    from flask import jsonify, request, send_file
    @app.get("/controls")
    def controls_home():
        return send_file(ROOT/"sgma"/"control_intelligence.html")
    @app.get("/controls/library")
    def controls_library():
        return jsonify(library())
    @app.get("/controls/detail")
    def controls_detail():
        return jsonify(control_detail(request.args.get("id","")))
    @app.post("/controls/impact")
    def controls_impact():
        return jsonify(impact(request.get_json()))
