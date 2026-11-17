"""Requirements assessment prototype. Never authorizes deployment or changes CI policy."""
import argparse
import json
from pathlib import Path

RANK = {"LOW":1,"MEDIUM":2,"HIGH":3,"CRITICAL":4}
SCANNERS = {"trivy-iac","trivy-sca","semgrep","gitleaks"}
APPLICABILITY = {"applicable","undetermined","not_applicable"}

def validate(profile):
    if not isinstance(profile,dict) or profile.get("schema_version") != 1:
        raise ValueError("Unsupported profile schema")
    for k in ("profile_id","revision"):
        if not isinstance(profile.get(k),str) or not profile[k].strip():
            raise ValueError("Missing "+k)
    seen=set()
    for group in ("baseline","overlays","manual"):
        rows=profile.get(group)
        if not isinstance(rows,list):
            raise ValueError("Missing "+group)
        for row in rows:
            for k in ("id","title","source"):
                if not isinstance(row.get(k),str) or not row[k].strip():
                    raise ValueError("Missing requirement "+k)
            if row["id"] in seen:
                raise ValueError("Duplicate requirement ID")
            seen.add(row["id"])
            if row.get("applicability") not in APPLICABILITY:
                raise ValueError("Invalid applicability")
            if row["applicability"]=="not_applicable" and not str(row.get("rationale","")).strip():
                raise ValueError("Non-applicability requires rationale")
            if group!="manual" and (row.get("scanner") not in SCANNERS or row.get("threshold") not in RANK or type(row.get("allow_exceptions")) is not bool):
                raise ValueError("Invalid automated requirement")
    if not profile["baseline"]:
        raise ValueError("Baseline cannot be empty")
    if any(r["applicability"]!="applicable" for r in profile["baseline"]):
        raise ValueError("Baseline requirements cannot be disabled in this prototype")

def rank(f):
    s=f.get("severity","UNKNOWN")
    return RANK.get(s,5) if s!="ERROR" else 4

def assess(profile, evidence=None, scanned=None):
    validate(profile)
    scanned=set(scanned or [])
    if not scanned <= SCANNERS:
        raise ValueError("Unknown evidence scanner")
    if evidence is not None and (not isinstance(evidence,dict) or evidence.get("schema_version")!=1 or evidence.get("decision") not in {"PASS","BLOCK","EXCEPTION APPROVED","EXCEPTION PENDING"} or not isinstance(evidence.get("findings"),list)):
        raise ValueError("Invalid unified decision evidence")
    findings=evidence["findings"] if evidence else []
    if any(not isinstance(f,dict) or f.get("scanner") not in SCANNERS or f.get("disposition") not in {"blocking","advisory","exception_approved","exception_pending"} or not f.get("id") for f in findings):
        raise ValueError("Invalid normalized finding")
    rows=[]
    effective={}
    for group in ("baseline","overlays","manual"):
        for req in profile[group]:
            result={k:req[k] for k in ("id","title","source","applicability")}
            result["layer"]=group
            result["finding_ids"]=[]
            if req["applicability"]=="not_applicable":
                result.update(status="REVIEW REQUIRED",reason="Proposed non-applicability: "+req["rationale"])
            elif req["applicability"]=="undetermined" or group=="manual":
                result.update(status="REVIEW REQUIRED",reason="Human applicability or manual evidence decision required")
            else:
                s=req["scanner"]
                result["scanner"]=s
                result["threshold"]=req["threshold"]
                rule=effective.setdefault(s,{"threshold":req["threshold"],"allow_exceptions":req["allow_exceptions"],"requirement_ids":[]})
                if RANK[req["threshold"]]<RANK[rule["threshold"]]:
                    rule["threshold"]=req["threshold"]
                rule["allow_exceptions"]=rule["allow_exceptions"] and req["allow_exceptions"]
                rule["requirement_ids"].append(req["id"])
                if evidence is None or s not in scanned:
                    result.update(status="EVIDENCE MISSING",reason="No completed scanner evidence supplied")
                else:
                    matches=[f for f in findings if f["scanner"]==s and rank(f)>=RANK[req["threshold"]]]
                    result["finding_ids"]=[f["id"] for f in matches]
                    blocked=[f for f in matches if not(req["allow_exceptions"] and f["disposition"]=="exception_approved")]
                    if blocked:
                        result.update(status="GAP",reason="Finding meets requirement threshold")
                    elif matches:
                        result.update(status="RESIDUAL RISK",reason="Existing exception referenced; applicability still requires review")
                    else:
                        result.update(status="NO MATCHING FINDING",reason="Limited automated evidence; not a compliance determination")
            rows.append(result)
    return {"schema_version":1,"profile_id":profile["profile_id"],"revision":profile["revision"],"status":"REVIEW REQUIRED","requirements":rows,"effective_rules":effective,"ci_decision":evidence.get("decision") if evidence else None,"deployment_authorized":False,"policy_changed":False,"compliance_certified":False}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("profile",type=Path)
    parser.add_argument("output",type=Path)
    parser.add_argument("--evidence",type=Path)
    parser.add_argument("--scanned",nargs="*",default=[])
    args=parser.parse_args()
    result=assess(json.loads(args.profile.read_text()),json.loads(args.evidence.read_text()) if args.evidence else None,args.scanned)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print("Requirements assessment:",result["status"])

if __name__=="__main__":
    main()
