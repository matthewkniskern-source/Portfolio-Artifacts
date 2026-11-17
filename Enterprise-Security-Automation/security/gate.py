"""Evaluate a Trivy JSON configuration/vulnerability report against a severity policy."""
import argparse
import json
from pathlib import Path

def evaluate(report, policy):
    blocked = set(policy["blocked_severities"])
    results = report.get("Results")
    if not isinstance(results, list) or not results:
        raise ValueError("Missing scan results")
    findings = []
    for result in results:
        for key in ("Misconfigurations", "Vulnerabilities", "Secrets"):
            for item in result.get(key) or []:
                severity = item.get("Severity", "UNKNOWN").upper()
                if severity in blocked or severity == "UNKNOWN":
                    findings.append({"target": result.get("Target"), "id": item.get("ID") or item.get("VulnerabilityID") or item.get("RuleID"), "severity": severity})
    return {"decision": "BLOCK" if findings else "PASS", "findings": findings, "human_approval_required": policy["human_approval_required"]}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("policy", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    decision = evaluate(json.loads(args.report.read_text()), json.loads(args.policy.read_text()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(decision, indent=2) + "\n")
    return int(decision["decision"] == "BLOCK")

if __name__ == "__main__":
    raise SystemExit(main())
