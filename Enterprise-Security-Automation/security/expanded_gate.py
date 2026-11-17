"""Fail closed on malformed/missing scanner reports and block unapproved findings.
Existing IaC exceptions are deliberately not applicable to these scanners.
"""
import json
import sys
from pathlib import Path

def require_list(obj, key):
    if not isinstance(obj, dict) or not isinstance(obj.get(key), list):
        raise ValueError("Missing or invalid " + key)
    return obj[key]

def evaluate(sast, sca, secrets):
    findings = []
    errors = require_list(sast, "errors")
    if errors:
        raise ValueError("Semgrep reported scan errors")
    for item in require_list(sast, "results"):
        findings.append({"scanner":"semgrep","id":item["check_id"],"target":item["path"],
                         "severity":item.get("extra",{}).get("severity","UNKNOWN"),"blocking":True})
    if not isinstance(sca, dict) or sca.get("SchemaVersion") != 2:
        raise ValueError("Invalid Trivy SCA report")
    results = require_list(sca, "Results")
    inventory = set()
    for result in results:
        for pkg in result.get("Packages") or []:
            inventory.add(str(pkg.get("Name","")).lower())
        for item in result.get("Vulnerabilities") or []:
            severity = str(item.get("Severity","UNKNOWN")).upper()
            findings.append({"scanner":"trivy-sca","id":item["VulnerabilityID"],"target":result["Target"],
                             "package":item.get("PkgName"),"severity":severity,
                             "blocking":severity not in {"LOW","MEDIUM"}})
    if not {"jinja2","markupsafe"} <= inventory:
        raise ValueError("Expected sample workload dependency inventory missing")
    if not isinstance(secrets, list):
        raise ValueError("Invalid Gitleaks report")
    for item in secrets:
        findings.append({"scanner":"gitleaks","id":item["RuleID"],"target":item["File"],
                         "line":item.get("StartLine"),"severity":"HIGH","blocking":True})
    return {"decision":"BLOCK" if any(f["blocking"] for f in findings) else "PASS",
            "findings":findings,"packages_detected":sorted(inventory),"deployment_authorized":False}

def main():
    if len(sys.argv) != 5:
        raise SystemExit("usage: expanded_gate.py SEMGREP SCA GITLEAKS OUTPUT")
    try:
        reports = [json.loads(Path(p).read_text()) for p in sys.argv[1:4]]
        decision = evaluate(*reports)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        decision = {"decision":"SCAN ERROR","error":str(exc),"deployment_authorized":False}
    Path(sys.argv[4]).write_text(json.dumps(decision,indent=2)+"\n")
    print("Expanded security decision:",decision["decision"])
    return 0 if decision["decision"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
