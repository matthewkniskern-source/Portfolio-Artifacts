# Security automation hardening — increment 1
Preserves existing owner authority and scoped risk acceptances. No deployment authorization.
- Historical register records ten verified archive digests and normalized outcomes; raw archives exported separately to owner for offline retention. No secret values or raw scanner reports committed. Register is version controlled, not immutable.
- Unified decision consumes existing component outputs and verified exception IDs. Both component exits remain mandatory; missing evidence fails closed. Existing scanners and test contracts retained.
- Evidence manifests include CI identity and report-level hashes; artifact retention requested at 90 days (repository limits apply).
- Pin checkout, upload and Terraform setup to resolved release commits; upgrade Trivy engine to 0.76.2. Signature status of Terraform setup commit not verified; pip transitive dependencies not locked. Regression test required.
- Remaining: protected workflow/policy enforcement independent of proposed code, scheduled exception renewal, hash-free owner commands, broader scan coverage, durable private evidence backend and independent verification. A same-repository author can modify workflow or evaluator in a PR, so required check alone is not a tamper-resistant trust boundary.
