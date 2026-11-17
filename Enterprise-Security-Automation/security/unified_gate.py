"""Unified decision and evidence manifest; no deployment authorization."""
import hashlib
import json
import os
from pathlib import Path

def combine(iac, expanded, reviews):
    if not isinstance(reviews,list):
        raise ValueError("Invalid review evidence")
    if iac["decision"] not in ("PASS","BLOCK","EXCEPTION PENDING","EXCEPTION APPROVED"):
        raise ValueError("Invalid IaC decision")
    if expanded["decision"] not in ("PASS","BLOCK"):
        raise ValueError("Invalid expanded decision")
    findings = []
    verified = {r["exception_id"] for r in reviews}
    for item in iac["findings"]:
        disposition = item["disposition"]
        if disposition == "exception_approved" and item["exception_id"] not in verified:
            disposition = "blocking"
        findings.append({"scanner":"trivy-iac","id":item["check_id"],"target":item["target"],
                         "resource":item.get("resource"),"severity":item["severity"],"disposition":disposition,
                         "exception_id":item.get("exception_id")})
    for item in expanded["findings"]:
        findings.append({**item,"disposition":"blocking" if item["blocking"] else "advisory"})
    states = {f["disposition"] for f in findings}
    decision = ("BLOCK" if "blocking" in states or "BLOCK" in (iac["decision"],expanded["decision"])
                else "EXCEPTION PENDING" if "exception_pending" in states or iac["decision"]=="EXCEPTION PENDING"
                else "EXCEPTION APPROVED" if "exception_approved" in states else "PASS")
    return {"schema_version":1,"decision":decision,"findings":findings,
            "human_approval_required":True,"deployment_authorized":False}

def main():
    paths = ["trivy.json","semgrep.json","sca.json","gitleaks.json","gate.json","expanded-gate.json","review-evidence.json"]
    manifest = {"schema_version":1,"repository":os.getenv("GITHUB_REPOSITORY"),"run_id":os.getenv("GITHUB_RUN_ID"),
                "attempt":os.getenv("GITHUB_RUN_ATTEMPT"),"commit":os.getenv("GITHUB_SHA"),"files":{}}
    for name in paths:
        path=Path(name)
        if path.is_file():
            manifest["files"][name]={"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),"bytes":path.stat().st_size}
    try:
        if len(manifest["files"]) != len(paths):
            raise ValueError("Required reports or review evidence missing")
        data=[json.loads(Path(n).read_text()) for n in paths[-3:]]
        result=combine(*data)
    except (OSError,ValueError,TypeError,KeyError) as exc:
        result={"schema_version":1,"decision":"SCAN ERROR","error":str(exc),"deployment_authorized":False}
    Path("unified-decision.json").write_text(json.dumps(result,indent=2)+"\n")
    manifest["files"]["unified-decision.json"]={"sha256":hashlib.sha256(Path("unified-decision.json").read_bytes()).hexdigest(),"bytes":Path("unified-decision.json").stat().st_size}
    Path("evidence-manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    print("Unified decision:",result["decision"])
    return 0 if result["decision"] in ("PASS","EXCEPTION APPROVED") else 1

if __name__=="__main__":
    raise SystemExit(main())
