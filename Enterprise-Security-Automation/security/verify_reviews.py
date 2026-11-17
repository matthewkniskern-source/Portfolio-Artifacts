"""Verify approved exception metadata against authenticated GitHub PR reviews.
Read-only API access. No approval is issued by this script.
"""
import base64
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import quote

POLICY = "Enterprise-Security-Automation/governance/requirements.example.json"
REVIEWERS = "Enterprise-Security-Automation/governance/authorized-reviewers.json"
BASE = "develop/enterprise-security-automation"

def verify_record(record, pr, reviews, reviewed_record, authorized, active_pr=None):
    reviewer = record.get("approved_by")
    if not reviewer or reviewer not in authorized:
        raise ValueError("Reviewer not authorized")
    if pr["user"]["login"].casefold() == reviewer.casefold():
        raise ValueError("PR author cannot approve own request")
    if pr["base"]["ref"] != BASE or (not pr.get("merged") and pr["number"] != active_pr):
        raise ValueError("Approval PR not merged into expected branch or current review PR")
    if reviewed_record != record:
        raise ValueError("Current exception differs from reviewed record")
    decisive = [r for r in reviews if r["user"]["login"].casefold() == reviewer.casefold()
                and r["state"] in ("APPROVED", "CHANGES_REQUESTED", "DISMISSED")]
    latest = max(decisive, key=lambda r: (r.get("submitted_at") or "", r["id"]), default=None)
    if not latest or latest["state"] != "APPROVED" or latest["commit_id"] != pr["head"]["sha"]:
        raise ValueError("Missing approval of exact PR head")
    if latest["submitted_at"][:10] != record.get("approved_on"):
        raise ValueError("Approval date does not match GitHub review")
    return {"exception_id": record["id"], "pr": pr["number"], "review_id": latest["id"],
            "reviewer": reviewer, "reviewed_sha": latest["commit_id"], "review_url": latest.get("html_url")}

def main():
    repo = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GH_TOKEN"]
    event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    active = event.get("pull_request", {}).get("number")
    def get(path):
        req = Request("https://api.github.com/repos/" + repo + "/" + path,
                      headers={"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json",
                               "X-GitHub-Api-Version": "2022-11-28"})
        with urlopen(req, timeout=30) as response:
            return json.load(response)
    def read_at(path, ref):
        data = get("contents/" + path + "?ref=" + quote(ref, safe=""))
        return json.loads(base64.b64decode(data["content"]))
    def all_reviews(number):
        out = []
        for page in range(1, 101):
            batch = get(f"pulls/{number}/reviews?per_page=100&page={page}")
            out.extend(batch)
            if len(batch) < 100:
                return out
        raise ValueError("Review pagination limit exceeded")
    policy = json.loads(Path(POLICY).read_text())
    authority = read_at(REVIEWERS, event["pull_request"]["base"]["sha"]) if active else json.loads(Path(REVIEWERS).read_text())
    authorized = set(authority["github_logins"])
    evidence = []
    for record in policy.get("exceptions", []):
        if record.get("status") != "approved":
            continue
        number = record.get("approval_pr")
        if type(number) is not int or number < 1:
            raise ValueError("Missing approval PR number")
        pr = get(f"pulls/{number}")
        if pr["head"]["repo"]["full_name"] != repo:
            raise ValueError("Approval PR must originate in this repository")
        reviewed = read_at(POLICY, pr["head"]["sha"])
        matches = [r for r in reviewed.get("exceptions", []) if r["id"] == record["id"]]
        if len(matches) != 1:
            raise ValueError("Missing or duplicate reviewed exception")
        evidence.append(verify_record(record, pr, all_reviews(number), matches[0], authorized, active))
    Path("review-evidence.json").write_text(json.dumps(evidence, indent=2) + "\n")
    print(f"Verified {len(evidence)} approved exceptions against GitHub reviews")

if __name__ == "__main__":
    main()
