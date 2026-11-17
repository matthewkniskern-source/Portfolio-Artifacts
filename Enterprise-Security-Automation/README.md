# Enterprise Security Governance and Automation

**Status (2026-11-17):** working static DevSecOps and sole-owner governance prototype. Hardened clean regression passed; combined negative regression passed (expected BLOCK). Hardening is proposed in [PR #9](https://github.com/matthewkniskern-source/Portfolio-Artifacts/pull/9), not yet integrated. No production or live AWS deployment, and no compliance certification.

## Purpose
Turn technical security findings into traceable organizational decisions using reproducible infrastructure, automated security checks, explicit human risk acceptance and protected change management. The intended end state adds configurable contractual requirements, control mapping, decision queues, RBAC and an operational GRC dashboard.

## Implementation status
| Capability | Status / evidence |
|---|---|
| AWS Terraform | Static validation of private, encrypted evidence and log storage configurations |
| CI and branch protection | Active ruleset 27481934 requires pull requests, current passing validate check, resolved conversations; blocks deletion and force pushes |
| IaC, SAST, SCA, secrets | Trivy, Semgrep and Gitleaks integrated; current project scope only |
| Exception governance | Two exact-scoped owner-approved S3 exceptions, verified against PR #3; expire 2027-02-15 |
| Security effectiveness | SCV-001–004 completed; PRs #5–7 closed without merging, issue #8 accepted and closed |
| Hardened decision / evidence | PR #9: unified decision, mandatory component outcomes, per-report SHA-256 manifest, pinned actions, Trivy 0.76.2, requested 90-day artifact retention |
| Hardened clean regression | 42/42 unit tests, all scanners and both existing approvals passed in run 44152446196 |
| Hardened negative regression | REG-001: all three intended findings blocked, both existing exceptions verified, 42 tests passed; run 44153268306; remediation revalidation pending |
| Requirements engine, RBAC, dashboard | Planned; illustrative control map and initial templates only |
| Runtime cloud / hybrid IT/OT | Planned; zero AWS resources deployed |

## Evidence and review
- [Passing integrated baseline](https://github.com/matthewkniskern-source/Portfolio-Artifacts/actions/runs/44147329527)
- [Owner exception decision and closeout](https://github.com/matthewkniskern-source/Portfolio-Artifacts/issues/2)
- [Security control validation register](https://github.com/matthewkniskern-source/Portfolio-Artifacts/issues/8) — detection, severity-based enforcement, remediation and human acceptance; initial unexpected results preserved.
- [Clean hardened regression](https://github.com/matthewkniskern-source/Portfolio-Artifacts/actions/runs/44152446196)
- [Combined negative regression](https://github.com/matthewkniskern-source/Portfolio-Artifacts/pull/10) — [run 44153268306](https://github.com/matthewkniskern-source/Portfolio-Artifacts/actions/runs/44153268306), artifact 14360341529, SHA-256 `20e0c46a0c2b027b2b542c3ca875c9a0de47b0a6a72f40bdb398194e4fc442d0`. Unified decision BLOCK; Semgrep dynamic evaluation, PyYAML CVE-2020-14343, Gitleaks generic-api-key. Both previously approved IaC exceptions retained. Eight report hashes independently matched evidence manifest. Artifact expires 2027-02-15. No fixture merged; exact hardened tree restored on test branch, revalidation pending.
- [Historical validation register](evidence/historical-validation-register.json) — ten archived evidence references and digests. Raw archives exported for offline retention; not committed publicly.
- [Hardening design](documentation/hardening.md) · [Expanded scanning scope](documentation/expanded-scanning.md) · [Owner approval procedure](governance/approval-workflow.md)

## Architecture
Change request → protected pull request → Terraform and four security disciplines → component gates and human authorization verification → unified decision and evidence manifest → owner integration decision → future authorized deployment and runtime assurance.

## Reproduce
From repository root: `python -m unittest discover -s Enterprise-Security-Automation/tests -v`. For Terraform static validation, run `terraform -chdir=Enterprise-Security-Automation/infrastructure/aws init -backend=false`, then `terraform -chdir=Enterprise-Security-Automation/infrastructure/aws validate`. CI workflow: [.github/workflows/enterprise-security-baseline.yml](../.github/workflows/enterprise-security-baseline.yml). No AWS credentials required for static checks; no apply workflow exists.

## Boundaries and next milestones
Synthetic data only; never commit real credentials, state, contract data or raw sensitive findings. A passing check does not establish compliance or deployment authorization. Owner attestations do not establish independent separation of duties. Required check alone does not protect its own workflow against authorized edits; persistent private evidence, stronger independent validation, hash-free authorization and broader coverage remain outstanding. One Node runtime warning remains. Test PR draft state and failing required checks were observed; no insecure merge was attempted.

Next: complete REG-001 remediation revalidation, review and merge hardening, then build the configurable requirements engine, control evidence mapping, decision matrix, dashboard and RBAC before live AWS and hybrid integration. See [roadmap](documentation/roadmap.md) and [legacy integration](governance/legacy-integration.md).
