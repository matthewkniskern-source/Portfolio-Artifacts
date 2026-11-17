"""Evaluate Trivy findings, preserving raw evidence and scoped exception decisions."""
import argparse
import json
from datetime import date, timedelta
from pathlib import Path

EXIT_CODES = {"PASS": 0, "EXCEPTION APPROVED": 0, "BLOCK": 1, "EXCEPTION PENDING": 2}

def exception_state(record, today):
    if record.get("status") != "approved":
        return "pending"
    try:
        approved = date.fromisoformat(record["approved_on"])
        expires = date.fromisoformat(record["expires_on"])
        reviewer = record["approved_by"]
        interval = record["review_interval_days"]
        if (not isinstance(reviewer, str) or not reviewer.strip()
                or type(interval) is not int or not 1 <= interval <= 90
                or not approved <= today < expires
                or not approved < expires <= approved + timedelta(days=interval)
                or not record.get("reason") or not record.get("compensating_controls")):
            return "invalid"
    except (KeyError, TypeError, ValueError, OverflowError):
        return "invalid"
    return "approved"

def evaluate(report, policy, today=None):
    today = today or date.today()
    blocked = set(policy["blocked_severities"])
    results = report.get("Results")
    if not isinstance(results, list) or not results:
        raise ValueError("Missing scan results")
    exceptions = policy.get("exceptions", [])
    findings = []
    for result in results:
        for kind in ("Misconfigurations", "Vulnerabilities", "Secrets"):
            for item in result.get(kind) or []:
                severity = item.get("Severity", "UNKNOWN").upper()
                resource = (item.get("CauseMetadata") or {}).get("Resource")
                finding = {"kind": kind, "target": result.get("Target"),
                           "check_id": item.get("ID") or item.get("VulnerabilityID") or item.get("RuleID"),
                           "resource": resource, "severity": severity}
                is_blocking = severity in blocked or severity not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
                matches = [e for e in exceptions if all(finding.values()) and e.get("scope") == finding]
                state = "blocking" if is_blocking else "advisory"
                exception_id = None
                if len(matches) == 1 and severity in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
                    exception_id = matches[0]["id"]
                    status = exception_state(matches[0], today)
                    if status == "approved":
                        state = "exception_approved"
                    elif status == "pending":
                        state = "exception_pending"
                findings.append({**finding, "disposition": state, "exception_id": exception_id})
    dispositions = {f["disposition"] for f in findings}
    decision = ("BLOCK" if "blocking" in dispositions else
                "EXCEPTION PENDING" if "exception_pending" in dispositions else
                "EXCEPTION APPROVED" if "exception_approved" in dispositions else "PASS")
    return {"decision": decision, "findings": findings,
            "human_approval_required": policy["human_approval_required"],
            "deployment_authorized": False, "evaluated_on": today.isoformat()}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("policy", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    decision = evaluate(json.loads(args.report.read_text()), json.loads(args.policy.read_text()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(decision, indent=2) + "\n")
    print("Policy decision:", decision["decision"])
    return EXIT_CODES[decision["decision"]]

if __name__ == "__main__":
    raise SystemExit(main())
