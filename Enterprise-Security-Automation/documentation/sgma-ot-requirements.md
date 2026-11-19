# OT/ICS requirements extension — initial increment

This feature adds a selectable, SGMA-authored OT catalog of 20 original assessment objectives, informed by [NIST SP 800-82 Rev. 3](https://doi.org/10.6028/NIST.SP.800-82r3). It is explicitly not the official Appendix F overlay, not a complete baseline, not a normative reproduction and not independently reviewed. Candidate SP 800-53 control references are advisory pointers, not asserted equivalence. The [official OT overlay](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/overlay-repository/nist-developed-overlay-submissions/operational-technology) remains the authoritative source. Source text not reproduced. The official 800-53 OSCAL v1.5.0 catalog byte retrieval was unavailable through the connector; full catalog onboarding remains open.

## Implemented
- Four categories: asset/configuration; access/segmentation; resilience/safety; monitoring/supply chain.
- 20 individually selectable controls with original statements, candidate 800-53 identifiers and suggested evidence. Select alongside existing IT catalogs, retain within an unapproved project proposal and OSCAL candidate bundle.
- All OT rows default to undetermined applicability and manual review; no additional scanner, active network operation, policy change, approval or automatic closure.
- Search matches control prose as well as title/ID. Composition preserves built-in template identity for staged and current selections.
- Three additional regression tests for metadata, preservation of stricter rules, manual assessment, exchange and invalid selection.

## Acceptance procedure
1. Start local preview, open /roadmap, select OT / ICS — NIST SP 800-82 Rev. 3 informed (SGMA candidate). Verify 20 controls and derived/unreviewed source status.
2. Select OT-06 (vendor access), OT-10 (safe vulnerability assessment), OT-13 (recovery/local operation) and compose using an unchanged registry-bound proposal with new revision. Verify all three manual rows, evidence and candidate references; existing LOW SCA rule remains unchanged.
3. Export native proposal and OSCAL exchange; validate manifest hashes and local selection references. Assess with historical CI evidence: OT rows remain REVIEW REQUIRED, no inferred OT scanner coverage.
4. Test unknown selection, duplicate stages, invalid project revision and attempts to weaken baseline. Confirm no governance authority, deployment or policy change.

## Remaining OT work
- Official SP 800-53 catalog and complete independently reviewed 800-82 Rev. 3 Appendix F low/moderate/high tailoring; SP 800-82 Rev. 4 draft in separate revision track, never substituted for final guidance.
- Authorized ISA/IEC 62443 imports with licensing and exact edition controls; facility controls (UFC/UFGS), CISA CPG, C2M2 maturity and applicable NERC CIP revisions.
- Asset context (IT/OT/converged, zones/conduits, owner, safety, operational criticality, availability, patch feasibility, maintenance window, compensating controls and rollback). Current increment does not implement an asset registry or operational action fields.
- OT-specific evidence adapters, manual review and scoped vendor exports; no live probing. Stable cross-run asset identity, approved mappings and role-based action lifecycle.
- Official OSCAL schemas, independent profile resolution, browser UAT and security closeout. CI results to be verified, no claim of production readiness.

Related #22 and #23. Existing pipeline and protected integration policy unchanged.
