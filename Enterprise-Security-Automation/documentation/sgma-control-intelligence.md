# SGMA common control intelligence — authoritative content and candidate graph

## Business and educational intent
This increment supports a capstone-grade engineering demonstration, evidence of understanding contract requirements and change workflow, and a bridge between IT and OT architecture. It is an original, vendor-neutral portfolio project, not an implementation for a named employer or a claim of customer endorsement. Design decisions and residual gaps are deliberate opportunities to exercise business analysis, requirements engineering, software assurance and technical communication.

## Local content inventory
- Three complete pinned NIST OSCAL catalogs already onboarded (800-171 Rev. 3, CSF 2.0, SSDF), totaling 410 projected entries.
- NIST SP 800-53/53A Rev. 5.2.0: exact 20 selected top-level control subtrees including 201 enhancements, 221 total entries. Full source has 1,196 entries and exceeds the current 8 MB catalog-processing limit. The extracted JSON is explicitly NOT a standalone OSCAL catalog, profile, approved baseline or Appendix F overlay. It retains upstream metadata, control objects, links, parts and parameters; references to unselected material are not independently resolved.
- 20 original SGMA-derived OT candidates, separately identified. Expected graph inventory: 651 source-scoped nodes across five local sources.
- 37 proposed direct related edges: 20 candidate 800-53 references and 17 manually authored overlap relationships to CSF or 800-171. No equivalence, transitivity, automatic evidence transfer, compliance or deployment authority.
- The official 800-82 Rev. 3 Appendix F low/moderate/high overlay, Rev. 4 initial public draft and licensed ISA/IEC 62443 source material remain reference-only. No fabricated control text or inferred applicability.

## Reproducibility
Upstream: https://github.com/usnistgov/oscal-content/blob/v1.5.0/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json
Upstream Git blob: 8ebe3c91181cc078d40e39bcf34ea233e652d025
Local extract Git blob: 0fe2c3cfc2717472f1c97bfadd603a223dbfbdd0
Connector retrieval of the upstream blob and the stored extract confirmed all 20 parsed control subtrees and the full upstream metadata exactly matched; recursive counts were 1,196 and 221 respectively. This establishes content comparison, not authenticated publisher signatures or schema conformance. Runtime verifies pinned Git identity for the extract and three complete NIST catalogs, and reports SHA-256 raw/content fingerprints. Git SHA-1 identifies objects; it is not used as an authorization or signature mechanism.

To repeat the comparison, independently obtain the complete JSON at the pinned release, retain it outside the repository, then run:
```
python Enterprise-Security-Automation/sgma/verify_nist53_extract.py PATH_TO_PINNED_JSON
```
This offline verifier reads at most 16 MB, checks the exact upstream Git blob, verifies metadata and selected subtrees. No network retrieval or automatic import occurs in the running application.

## Graph and workflow
Open /controls in local preview. Browse publisher and derivative records, filter by source or identifier/title, inspect control details and associated one-hop relationships, mark hypothetical changed nodes and export human-review candidates. Source-scoped IDs and content hashes preserve distinctions; edges carry rationale, source/target fingerprints, unreviewed state and no authority. This is not actual project revision impact analysis; project associations, approved mappings and decision lifecycle remain future work. The 800-53 extract is a read-only reference library, not selectable through the existing OSCAL composition API. Existing three full catalogs and derived OT template retain their original composition behavior.

## Acceptance and portfolio demonstration
1. Verify all six new regression tests and prior baseline. Check the five local sources, 651 projected records, 37 related edges and reference-only labeling.
2. Browse OT-06 and inspect 800-53 AC-17 and 800-171 03.01.12 as distinct nodes. Verify the unreviewed rationale and no automatic evidence transfer.
3. Mark AC-17 for hypothetical review. The direct candidate is OT-06, not an inferred transitive change to 800-171 or an affected project.
4. Review OT-05 against CSF PR.IR-01 and its 800-53 and 800-171 references; consider how industrial availability, scope and acceptance criteria differ.
5. Separately use /ot to produce contract and acceptance drafts for a synthetic facility modernization. Compose and assess under the original strict baseline; no new approval or scanner authorization.
6. Explain which objectives came from publisher material, which are engineering interpretations, how sources are versioned and what requires human review.

## Remaining engineering gates
Full 800-53 catalog ingestion with separately bounded storage/index architecture; actual 800-82 Appendix F tailoring with reviewed impact levels and control-parameter semantics; licensed content workflow; formal mapping review, persisted source revisions, approved relationship lifecycle and direct/indirect project impact with separate confidence and human decisions; OSCAL schema provisioning and independent resolution; evidence reuse validation and IT/OT asset context; browser acceptance and CI/security review. No live scanning or deployment.
