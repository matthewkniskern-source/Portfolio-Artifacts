# Applied Technology, Cybersecurity & Systems Portfolio

This repository contains selected technical and systems-analysis work covering security operations, operational technology (OT), business systems, service management, databases, and digital commerce.

The common thread is **turning operational requirements and risk into documented designs, controls, workflows, and testable implementations**. Some artifacts are working demonstrations; others are explicitly conceptual case studies. Those distinctions are noted below rather than implying production deployments.

## Featured active project — SGMA

**Security Governance Management Application (SGMA)** is my active development project connecting automated security engineering with requirements management and human governance. The working local requirements interface has completed four user acceptance tests; the integrated DevSecOps and SGMA application foundation has passed 57 automated tests. MySQL execution, identity/RBAC and cloud deployment remain future validation work.

[Open SGMA project overview](https://github.com/matthewkniskern-source/Portfolio-Artifacts/tree/develop/enterprise-security-automation/Enterprise-Security-Automation) · [Latest verified CI](https://github.com/matthewkniskern-source/Portfolio-Artifacts/actions/runs/44163139855) · [User acceptance testing](https://github.com/matthewkniskern-source/Portfolio-Artifacts/issues/12)

## Start here — selected work

| Project | What to review first | Evidence and scope |
| --- | --- | --- |
| **Enterprise security governance and automation — SGMA (active development)** | [Project overview](https://github.com/matthewkniskern-source/Portfolio-Artifacts/tree/develop/enterprise-security-automation/Enterprise-Security-Automation) · [Security validation](https://github.com/matthewkniskern-source/Portfolio-Artifacts/issues/8) · [Browser UAT](https://github.com/matthewkniskern-source/Portfolio-Artifacts/issues/12) | Working static DevSecOps and advisory GRC prototype; four scanner disciplines, protected changes, scoped exceptions, configurable requirements, local browser UAT and a database-oriented application foundation. MySQL and container runtime not yet validated; no live AWS deployment. |
| **OT architecture and risk reduction** | [Architecture case study](OT%20Architecture%20Risk%20Reduction/README.md) · [Legacy findings](OT%20Architecture%20Risk%20Reduction/legacy%20risk%20findings.md) · [Target topology](OT%20Architecture%20Risk%20Reduction/target%20topo.mmd) | Fictionalized utility-plant case: BACnet/IP, legacy MS/TP dependencies, trust boundaries, vendor access, risk reduction, and operational continuity. **Conceptual design.** |
| **SOC investigation and PowerShell** | [Incident overview](SOC%20Investigation%20Case%20Study/README.md) · [Evidence](SOC%20Investigation%20Case%20Study/02%20evidence/) · [Automation](SOC%20Investigation%20Case%20Study/04%20automation/README.md) | Synthetic event evidence, investigation chronology, containment reasoning, ATT&CK mapping, and defensive PowerShell utilities. **Case simulation and source code.** |
| **Enterprise service-management transformation** | [Client solution brief](Enterprise%20Service%20Management%20Implementation%20%26%20Workflow%20Transformation%20Case%20Study/Client%20Solution%20Brief.md) · [Full case](Enterprise%20Service%20Management%20Implementation%20%26%20Workflow%20Transformation%20Case%20Study/README.md) | Vendor-neutral workflows, RBAC/approvals, traceability, migration, UAT, metrics and governance for a fictional organization. **Proposed operating model.** |
| **Project-management DBMS** | [DBMS overview](Database-DBMS/Remediation-Project-Management-DBMS/README.md) · [SQL reports](Database-DBMS/Remediation-Project-Management-DBMS/queries/) | MySQL relational model, ERD, sample data views, operational queries, and role concepts. Historical beta integration; authoritative original DDL not included. |
| **SAP workflow governance** | [Case overview](SAP%20Workflow%20Governance/README.md) · [Decision and edge cases](SAP%20Workflow%20Governance/core/04%20decision%20and%20edge%20case%20matrix.md) | Anonymized eligibility and exception workflow analysis with auditable decision rules and testable requirements. **Conceptual governance design.** |
| **Digital retail prototype** | [Project guide](Secure-E-Commerce-Digital-Retail-Transformation/README.md) · [Browser demo source](Secure-E-Commerce-Digital-Retail-Transformation/Implementation/Academic%20Website/) | Fictional multi-location storefront with catalog, cart, checkout demonstration and accompanying business/security design documents. **Browser-only academic demonstration.** |
| **Digital commerce and inventory integration** | [Architecture and scope](New-Source-Digital-Commerce-Inventory-Integration/README.md) · [Integration pattern](New-Source-Digital-Commerce-Inventory-Integration/docs/04-architecture/integration-architecture.md) | Proposed Zoho Inventory / Lightspeed middleware design, reservations, sync, exception handling and governance. **Specification, not deployed integration.** |

## Pick a path based on the role

**OT / ICS security:** OT architecture → communication requirements → legacy risks → target topology → residual-risk validation.

**SOC / security analyst:** Synthetic evidence → investigation timeline → detection logic → PowerShell automation → containment and lessons learned.

**DevSecOps / cybersecurity engineering:** Enterprise security automation → protected CI → security findings and risk acceptance → validation evidence.

**GRC / systems analysis:** Enterprise security governance prototype → ESM solution brief → requirements traceability → governance controls → UAT; then SAP decision modeling.

**Business systems / implementation:** DBMS relational model → digital commerce integration architecture → retail prototype.

## Evidence standards

- **Working demonstration** means executable code or an interactive browser prototype is present; it does not imply production authentication, connected payment processors, or live infrastructure.
- **Conceptual or proposed** means a documented future-state design, control model, workflow, or migration plan—not an installed enterprise solution.
- **Synthetic/anonymized data** are used in the security incident, fictional business scenarios, and demonstrations.
- Where source exports or test execution records are not available, the limitation is explicitly disclosed rather than invented.

## Navigating the repository

Each project directory contains or links to a project guide. Technical details remain alongside supporting diagrams, queries, CSV evidence, scripts, and design documents. For a short evaluation, start with the project description and one representative implementation or evidence artifact before exploring the full document tree.

**Repository:** [Portfolio-Artifacts](https://github.com/matthewkniskern-source/Portfolio-Artifacts) · [Project index](#start-here--selected-work)
