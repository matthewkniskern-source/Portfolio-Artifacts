# SGMA roadmap 02–10 integration — proposed baseline

Date: 2026-11-19. Integration branch only. No merge, MySQL initialization, external deployment or approval authority authorized. The maintained security workflow and prior gate logic are unchanged. This is a development build, not acceptance.

## Architecture decision

Adopt OSCAL as an exchange format through adapters, while retaining the native SGMA requirements, evaluation, and workflow model. Official NIST documents are retained as JSON; imported files are not executed. Catalog projection is deliberately partial and no external URI is resolved. JSON canonical fingerprints are distinct from byte hashes; re-encoded exports preserve the parsed content, not original file bytes. Imported and authored obligations remain proposed. The active baseline and selected repository-controlled rows remain protected by the existing library verifier. External control selections are manual-review obligations unless a separately configured scanner rule is supplied; no framework compliance inference.

## Roadmap implementation and residual scope

| Phase | Landed in this branch | Required closure |
|---|---|---|
| 02 | Bounded catalog inspection, exact-version schema adapters, schema asset hashes, candidate profile generation and ZIP exchange with manifest and local imports | Provision official schemas, validate actual content, independently resolve, round-trip and cross-tool tests |
| 03 | Three upstream catalogs and selectable staged overlays | 800-53 and other templates, revision lifecycle, reviewed mappings and applicability, content licensing for non-NIST sources |
| 04 | Contract authoring UI, optional scanner rule, hybrid review row, source/evidence/deadline, revision comparison and native project proposal composition | Persistent authoring/approval UI, clause-level change impact across projects, comprehensive revision rules; compare uses uploaded independent drafts |
| 05 | Proposed source-target mappings with relation and rationale; lifecycle mapping inspection | Verified reference identity, OSCAL mapping exchange, approved mapping graph, overlap/conflict reconciliation |
| 06 | Evidence-document occurrence IDs, many-requirement associations, legacy fallback, advisory action drafts | Stable cross-run asset/occurrence identities; durable decision state, verified scope and ownership, action lifecycle and deadlines |
| 07 | Catalog/profile/contract catalog generation, inspection adapter for six other OSCAL model roots | Full SSP/AP/AR/POA&M generation and semantic exchange, reference resolution, component and mapping interoperability |
| 08 | Browser decision table, per-assessment metrics, draft export | Organization-wide aggregate reporting, role-specific dashboards |
| 09 | Opt-in scoped bearer authorization and append-only draft records/events with per-project record retrieval | Real identity provider/user sessions, server-enforced action-specific RBAC for entire application, secure migration/runtime validation, full persistence |
| 10 | Bounded requests, no external resolution, SHA-pinned schema assets, no authorization operations, added regression tests | Comprehensive QA/QC, preliminary red-team findings, independent security enforcement, operational readiness; no deployment |

The new /roadmap workbench can be opened via the main preview. Keep using the same local preview command: `python Enterprise-Security-Automation/sgma/app.py preview`. Update dependencies first with `python -m pip install -r Enterprise-Security-Automation/sgma/requirements.txt`. No actual data, credentials or real contract obligations in preview.

## Official content / source

NIST OSCAL Content v1.5.0 (https://github.com/usnistgov/oscal-content/releases/tag/v1.5.0). Git blob verified against upstream on integration. Retained public-domain/CC0 notice in catalogs/LICENSE-NIST.md. No endorsement implied.

| File | Upstream Git blob |
|---|---|
| NIST_SP800-171_rev3_catalog.json | 1bc9d5ab5f57329c1ab5553b4d2b27ea54d9d13f |
| NIST_CSF_v2.0_catalog.json | 7b8b2d8b45cbf6fca093fcc5ae9f17ca9938b425 |
| NIST_SP800-218_ver1_catalog.json | 94f85f214557d4f52faddbf0b2e83de55d11db5d |

The files declare v1.2.2; generated candidates target 1.2.3. The bundle is not a claim of successful OSCAL interoperability. Source docs, manifest hashes and approval flags remain explicit. Never treat a schema check as evidence of implementation or authorization.

## Offline schema provisioning

Official asset hashes pinned in sgma/provision_oscal.py from:
- https://github.com/usnistgov/OSCAL/releases/expanded_assets/v1.2.2
- https://github.com/usnistgov/OSCAL/releases/expanded_assets/v1.2.3

Obtain individual JSON schema release assets in separate local directories for each version (or the release ZIP if it includes the desired schemas). No automatic download occurs at runtime:
`python Enterprise-Security-Automation/sgma/provision_oscal.py PATH_TO_ASSETS --version 1.2.2`
`python Enterprise-Security-Automation/sgma/provision_oscal.py PATH_TO_ASSETS --version 1.2.3`

Missing official assets are reported as OFFICIAL_SCHEMA_NOT_PROVISIONED. Local schema verification is not semantic validation or independent profile resolution. With provisioned schemas the adapter must reject mismatches, invalid documents, and unresolved schema references without outbound retrieval. The independent OSCAL CLI resolver is a required QA integration; run only in isolated no-network workspace on approved local-reference inputs, verify manifests and check resolved control selection. No resolver is executed by this branch.

## Persistence boundary

Preview denies persistent draft API requests. In database mode new draft endpoints require explicitly configured `SGMA_ROADMAP_PRINCIPALS`: JSON list of principal IDs, roles, project scopes, and SHA-256 fingerprints of high entropy bearer tokens. Do not commit or log tokens or real principal configuration. New app database tables are defined; no schema initialization has been performed. Existing legacy workbench routes are still local unauthenticated; this is not application-wide RBAC. No approval routes exist. No production use.

## Consolidated QA/QC campaign

Preserve issue #18/#20 and 77-test baseline. This branch adds tests; exact pass count must be recorded from actual CI. Do not merge or label accepted before evidence review. Consolidated test objectives:
1. Existing regression CI, scanner evidence, negative gate, scoped exceptions.
2. Official schema provisioning for both versions; asset hash mutation, missing and unsupported schemas, nested malformed/oversized and duplicate-key JSON, invalid references.
3. Official catalog count, hierarchical controls, statements, parameters, source raw/canonical hash distinctions and reproducibility. Multi-framework profile resolve against expected IDs with independent tooling, no network, duplicate-control conflict.
4. Contract draft UI required fields, rule mapping, hybrid review, duplicate IDs, revisions, and attempts to weaken mandatory baseline or alter selected library entries.
5. Common control mapping identity and scope, partial/equivalent distinction, approval disabled, conflict review and traceability.
6. Real positive and negative CI archive assessment exports; same CVE across distinct targets must remain distinct; one occurrence across multiple requirements produces one record; no secret values; legacy export fallback; forged assessment trust flags.
7. OSCAL lifecycle artifacts and local reference chain: actual component/SSP/AP/AR/POA&M fixtures; reject invalid/unresolved references; round-trip independent app. Complete missing semantic adapters before signoff.
8. Dashboard and action draft UI, stale-state/revision/race handling; cross-project reporting not yet implemented.
9. Scoped persistence: unauthorized/cross-project/read-only/administrator denial, immutable revision conflict, transaction and audit integrity, role semantics, actual MySQL migrations and full auth/RBAC before real use.
10. Reopen preliminary 12 red-team findings; threat model updates, SAST/SCA/secret history, source attestation, dynamic tests, resilience and operator acceptance. No deployment until all blocking gaps closed.

The phase numbers identify the workstreams advanced, not proof that all requirements have been implemented. QA record remains open pending the owner session.
