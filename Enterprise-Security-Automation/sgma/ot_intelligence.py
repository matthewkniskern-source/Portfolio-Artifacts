"""Local advisory OT requirements intelligence. No network, approval or live assessment."""
from roadmap import load_template, bounded, ident, string, fingerprint, FLAGS, contract_draft

TEMPLATE = "sgma-ot-800-82-r3"
SECTORS = ("district-energy","buildings","water","electric","manufacturing","healthcare","transport","oil-gas","defense")
SYSTEMS = ("bas-ddc","scada","plc","dcs","sis","electrical","converged")
CUSTOMERS = ("private","municipal","federal","dod")
PHASES = ("procurement","design","construction","commissioning","turnover","operations","modernization")
FEATURES = ("vendor-access","legacy","safety","critical-availability","portable-media")
SOURCES = [
    {"id":"nist-82-r3","title":"NIST SP 800-82 Rev. 3","url":"https://doi.org/10.6028/NIST.SP.800-82r3","kind":"guidance","availability":"DERIVED_CANDIDATE_ONLY"},
    {"id":"nist-53-r5","title":"NIST SP 800-53 Rev. 5","url":"https://doi.org/10.6028/NIST.SP.800-53r5","kind":"control catalog","availability":"REFERENCE_ONLY"},
    {"id":"iec-62443","title":"ISA/IEC 62443 series","url":"https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards","kind":"licensed series; verify part and edition","availability":"REFERENCE_ONLY_LICENSE_REQUIRED"},
    {"id":"ufc","title":"UFC 4-010-06","url":"https://www.wbdg.org/dod/ufc/ufc-4-010-06","kind":"facility design criteria; verify contract adoption and edition","availability":"REFERENCE_ONLY"},
    {"id":"ufgs","title":"UFGS 25 05 11","url":"https://www.wbdg.org/dod/ufgs","kind":"facility construction specifications; verify section and edition","availability":"REFERENCE_ONLY"},
    {"id":"nerc","title":"NERC CIP","url":"https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx","kind":"sector requirements; determine regulated scope","availability":"REFERENCE_ONLY"},
    {"id":"cisa","title":"CISA Cross-Sector Cybersecurity Performance Goals","url":"https://www.cisa.gov/cross-sector-cybersecurity-performance-goals","kind":"voluntary guidance","availability":"REFERENCE_ONLY"},
]
# Original SGMA engineering recommendations, not source text or normative mappings.
# Phase-specific suggestions never exclude other requirements from the explorer.
PHASE_IDS = {
    "procurement": (6,9,11,18,19), "design": (2,5,7,14,16),
    "construction": (3,4,5,8,9), "commissioning": (5,10,12,13,14,20),
    "turnover": (1,3,12,13,17,20), "operations": (4,6,7,10,11,15,16,17),
    "modernization": (3,4,11,12,13,19,20),
}
SYSTEM_IDS = {
    "bas-ddc":(5,6,13,16,19), "scada":(5,13,15,16,17),
    "plc":(3,4,9,12,14), "dcs":(3,4,12,13,14), "sis":(4,13,14,20),
    "electrical":(2,4,13,14,17), "converged":(5,6,7,16,18),
}
FEATURE_IDS = {"vendor-access":(6,7,16), "legacy":(11,19), "safety":(4,14,20),
               "critical-availability":(2,11,12,13,15), "portable-media":(9,)}
TECH_TAGS = {
    1:"PLC DDC HMI SCADA historian VFD",3:"PLC DDC HMI firmware logic",5:"BACnet Modbus OPC UA DNP3 PROFINET EtherNet/IP",
    6:"VPN gateway vendor remote access",9:"USB engineering workstation",10:"passive discovery PLC DDC",
    12:"PLC DDC HMI backup",13:"HMI local operation SCADA",14:"SIS interlock safety",
    16:"historian BACnet Modbus monitoring",17:"NTP historian",19:"legacy firmware HMI",
}
ACCEPTANCE = {
    1:"Reconcile a representative inventory against approved drawings and records.",
    2:"Review process dependencies and consequence analysis with operations.",
    3:"Compare approved configuration versions and integrity records.",
    4:"Review an authorized change package and rollback plan.",
    5:"Inspect approved network design and permitted-flow records.",
    6:"Review access approvals, architecture and session records.",
    7:"Review role assignments and approved privilege exceptions.",
    8:"Inspect physical access records and approved walkthrough findings.",
    9:"Review approved media-transfer procedure and usage records.",
    10:"Review passive assessment scope and engineering authorization; no active test initiated.",
    11:"Review compatibility, maintenance and rollback evidence with engineering.",
    12:"Verify backup inventory and integrity evidence.",
    13:"Review authorized recovery exercise and operator sign-off.",
    14:"Review hazard analysis and independent safety authorization where applicable.",
    15:"Review tabletop exercise and operational escalation records.",
    16:"Review monitoring coverage and loss-of-visibility procedures.",
    17:"Inspect approved time configuration and log samples.",
    18:"Review supplier support and provenance evidence.",
    19:"Review lifecycle register and approved compensating-control plan.",
    20:"Review authorized commissioning results and operator acceptance.",
}
def choice(payload, key, choices):
    value = payload[key]
    if not isinstance(value,str) or value not in choices:
        raise ValueError("Invalid "+key)
    return value

def context(payload):
    bounded(payload)
    if not isinstance(payload,dict):
        raise ValueError("Expected context object")
    features=payload.get("features",[])
    if not isinstance(features,list) or any(not isinstance(x,str) or x not in FEATURES for x in features) or len(set(features))!=len(features):
        raise ValueError("Invalid context features")
    return {"sector":choice(payload,"sector",SECTORS),"system":choice(payload,"system",SYSTEMS),
            "customer":choice(payload,"customer",CUSTOMERS),"phase":choice(payload,"phase",PHASES),
            "features":sorted(features)}

def explorer():
    source=load_template(TEMPLATE)
    rows=[]
    for control in source["controls"]:
        n=int(control["id"].split("-")[1])
        props={x["name"]:x["value"] for x in control["props"]}
        rows.append({"id":control["id"],"title":control["title"],"category":control["parents"][0],
            "statement":control["parts"][0]["prose"],"evidence":props["evidence"],
            "candidate_reference":props["candidate-control-reference"],"relationship":"RELATED_UNREVIEWED",
            "acceptance_candidate":ACCEPTANCE[n],"technology_tags":TECH_TAGS.get(n,"").split(),
            "source_sha256":source["catalog_sha256"],"source_revision":source["template"]["content_release"],
            "source_class":"SGMA_DERIVED_UNREVIEWED","applicability":"undetermined"})
    return {"controls":rows,"sources":SOURCES,"template":TEMPLATE,"catalog_sha256":source["catalog_sha256"],**FLAGS}

def discover(payload):
    ctx=context(payload)
    reasons={n:["Core discovery objective"] for n in (1,2,5,7,12,15)}
    def include(ids, rationale):
        for n in ids:
            reasons.setdefault(n,[]).append(rationale)
    include(PHASE_IDS[ctx["phase"]],"Lifecycle phase: "+ctx["phase"])
    include(SYSTEM_IDS[ctx["system"]],"System type: "+ctx["system"])
    for feature in ctx["features"]:
        include(FEATURE_IDS[feature],"Declared feature: "+feature)
    library=explorer()
    rows=[{**row,"recommendation_reasons":reasons[int(row["id"].split("-")[1])]}
          for row in library["controls"] if int(row["id"].split("-")[1]) in reasons]
    source_ids=["nist-82-r3","nist-53-r5","iec-62443","cisa"]
    if ctx["customer"]=="dod":
        source_ids+=["ufc","ufgs"]
    if ctx["sector"]=="electric":
        source_ids+=["nerc"]
    return {"context":ctx,"context_sha256":fingerprint(ctx),"catalog_sha256":library["catalog_sha256"],
            "recommendations":rows,"sources_to_review":[x for x in SOURCES if x["id"] in source_ids],
            "applicability":"HUMAN_DETERMINATION_REQUIRED",**FLAGS}

def deliverables(payload):
    bounded(payload)
    ctx=context(payload["context"])
    library=explorer()
    indexed={x["id"]:x for x in library["controls"]}
    selected=payload["selected"]
    if not isinstance(selected,list) or not selected or any(not isinstance(x,str) or x not in indexed for x in selected) or len(set(selected))!=len(selected):
        raise ValueError("Invalid OT selection")
    contract_id=ident(payload["contract_id"])
    revision=ident(payload["revision"])
    customer=string(payload["customer"])
    records=[]
    for cid in selected:
        row=indexed[cid]
        records.append({**row,"draft_requirement_id":"DRAFT-"+cid,
            "proposed_clause":"SGMA candidate / "+cid,
            "proposed_statement":"The contractor shall: "+row["statement"][0].lower()+row["statement"][1:],
            "responsibility":"TO_BE_ASSIGNED","acceptance_state":"NOT_ASSESSED"})
    contract=contract_draft({"contract_id":contract_id,"revision":revision,"customer":customer,
        "requirements":[{"id":x["draft_requirement_id"],"title":x["title"],"clause":x["proposed_clause"],
            "statement":x["proposed_statement"],"method":"manual","applicability":"undetermined",
            "evidence":x["evidence"]+"; "+x["acceptance_candidate"],
            "rationale":"Derived OT candidate "+x["id"]+" catalog "+x["source_sha256"]} for x in records]})
    return {"context":ctx,"context_sha256":fingerprint(ctx),"catalog_sha256":library["catalog_sha256"],
            "contract_draft":contract,"contract_sha256":fingerprint(contract),"traceability_matrix":records,
            "selection":{"template":TEMPLATE,"selected":selected},
            "acceptance_checklist":[{"requirement_id":x["draft_requirement_id"],"method":x["acceptance_candidate"],
            "state":"NOT_ASSESSED","owner":None} for x in records],
            "review_state":"PENDING_HUMAN_REVIEW",**FLAGS}

def register(app):
    from flask import jsonify, request, send_file
    from roadmap import ROOT
    @app.get("/ot")
    def ot_home():
        return send_file(ROOT/"sgma"/"ot_intelligence.html")
    @app.get("/ot/library")
    def ot_library():
        return jsonify(explorer())
    @app.post("/ot/discover")
    def ot_discover():
        return jsonify(discover(request.get_json()))
    @app.post("/ot/deliverables")
    def ot_deliverables():
        return jsonify(deliverables(request.get_json()))
