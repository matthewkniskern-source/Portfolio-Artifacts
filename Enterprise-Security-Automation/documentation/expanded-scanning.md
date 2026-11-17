# Expanded static security scanning
Scope: Enterprise-Security-Automation project tree only. Existing portfolio projects, full Git history, infrastructure runtime and deployed dependencies are not scanned by these new checks.
- SAST: Semgrep 1.185.0, local curated Python rules, no registry dependency; all matches block. Limited ruleset, not exhaustive.
- SCA: existing Trivy binary and vulnerability database, filesystem dependency manifests; sample Jinja2/MarkupSafe workload provides a concrete inventory. HIGH, CRITICAL and unknown/unrecognized severity block; LOW/MEDIUM remain advisory. Inventory presence is required to prevent an empty scan from silently passing.
- Secrets: Gitleaks 8.30.1 current-project directory scan, fully redacted report; any finding blocks. No historical Git scan.
- Existing infrastructure scanner and owner exception verification remain in the mandatory validate job. No AWS exception is inherited by new scanners.
- CI retains scanner reports and normalized decision for 14 days. Do not commit real secrets; rotate any actual leaked credentials immediately. No deployment authorization. Tool errors fail the job; downstream stages can be skipped. Scanner outputs are not proof of compliance.
- Versions pinned where practical; pip transitive dependencies and Gitleaks release checksum provenance are not independently supply-chain attested. Existing Trivy version warning and Node maintenance remain outstanding.
Acceptance criteria: all checks run, raw/redacted evidence retained, unit tests pass; separately demonstrate controlled negative cases and remediation before claiming detection coverage.
