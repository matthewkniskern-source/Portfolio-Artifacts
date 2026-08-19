# NIST Alignment

## Purpose

This case study uses NIST guidance to provide a defensible basis for evaluating the legacy OT architecture and developing the target-state design.

The project does not represent a formal NIST compliance assessment.

Instead, NIST guidance is used to connect identified risk conditions with recognized cybersecurity outcomes and control concepts appropriate to operational technology.

The primary references are:

* **NIST SP 800-82 Rev. 3 — Guide to Operational Technology (OT) Security**
* **NIST Cybersecurity Framework (CSF) 2.0**
* **NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations**

NIST SP 800-82 Rev. 3 serves as the primary OT-specific reference because it addresses cybersecurity while accounting for the performance, reliability, and safety requirements of operational environments.

CSF 2.0 provides the higher-level cybersecurity outcomes used to organize the risk-reduction objectives.

Selected SP 800-53 controls provide additional traceability where a specific control concept is useful.

---

# Alignment Approach

The case study uses the following relationship:

**Observed Condition → Risk Finding → NIST Guidance → Architecture Decision → Expected Risk Reduction**

This approach prevents the standards mapping from becoming a checklist exercise.

Controls are selected because they address identified risks within the reference environment rather than because every available NIST control must be represented.

---

# Legacy Risk Alignment

| Finding                                                  | NIST SP 800-82 Theme                                                         | CSF 2.0 Alignment                                               | Selected SP 800-53 Traceability                                            |
| -------------------------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **LR-01 — Broadly Trusted OT Network**                   | Network segmentation, boundary protection, controlled communications         | PR.IR — Technology Infrastructure Resilience                    | SC-7 — Boundary Protection; CA-9 — Internal System Connections             |
| **LR-02 — Excess Management Supervisory Privilege**      | Access restriction and separation of operational responsibilities            | PR.AA — Identity Management, Authentication, and Access Control | AC-6 — Least Privilege; AC-3 — Access Enforcement                          |
| **LR-03 — Persistent Legacy Vendor VPN**                 | Remote-access control and third-party connectivity                           | PR.AA; GV.SC — Cybersecurity Supply Chain Risk Management       | AC-17 — Remote Access; AC-20 — Use of External Systems                     |
| **LR-04 — Broad Engineering Workstation Reachability**   | Protection of high-privilege OT engineering functions                        | PR.AA; PR.IR                                                    | AC-6 — Least Privilege; SC-7 — Boundary Protection                         |
| **LR-05 — Mobile and Third-Party Maintenance Endpoints** | Maintenance access, portable systems, and external-device risk               | PR.AA; GV.SC                                                    | AC-19 — Access Control for Mobile Devices; AC-20 — Use of External Systems |
| **LR-06 — Historian Within Broad OT Trust Zone**         | Separation of control functions from information-consumption pathways        | PR.IR; PR.DS — Data Security                                    | SC-7 — Boundary Protection; CA-9 — Internal System Connections             |
| **LR-07 — Legacy MS/TP Process Dependencies**            | Legacy-system constraints, compensating controls, and operational resilience | ID.AM — Asset Management; PR.IR                                 | CM-8 — System Component Inventory; CP-family resilience concepts           |
| **LR-08 — Ambiguous IT/OT/Vendor Ownership**             | Governance, responsibility, asset ownership, and third-party coordination    | GV.RR — Roles, Responsibilities, and Authorities; GV.SC         | PM and SR control-family concepts                                          |

---

# LR-01 — Segmentation and Boundary Protection

The legacy network places supervisory, engineering, historian, and controller systems within a broadly trusted BACnet/IP environment.

NIST OT guidance supports using network architecture and segmentation to limit communications between systems and security domains while accounting for operational requirements.

The relevant CSF 2.0 outcome area is primarily **Technology Infrastructure Resilience (PR.IR)**, which includes protecting networks and environments from unauthorized logical access and usage.

Selected control traceability includes:

* **SC-7 — Boundary Protection**
* **CA-9 — Internal System Connections**

These references support the target-state objective of replacing broad implicit reachability with explicitly controlled communication paths.

---

# LR-02 — Least Privilege for Management Access

The plant manager requires operational visibility but does not require process-control authority.

This distinction aligns directly with the principle that access permissions should reflect actual responsibilities and assessed risk.

The primary CSF 2.0 category is:

* **PR.AA — Identity Management, Authentication, and Access Control**

Selected SP 800-53 traceability includes:

* **AC-6 — Least Privilege**
* **AC-3 — Access Enforcement**

The target state should therefore preserve the legitimate information requirement while removing unnecessary command authority.

---

# LR-03 — Governed Remote Vendor Access

The legacy vendor VPN demonstrates the difference between technically functional access and governed access.

Remote connectivity that persists outside the recognized access model creates uncertainty about authorization, credentials, monitoring, reachable assets, and ownership.

Relevant CSF 2.0 categories include:

* **PR.AA — Identity Management, Authentication, and Access Control**
* **GV.SC — Cybersecurity Supply Chain Risk Management**

Selected SP 800-53 traceability includes:

* **AC-17 — Remote Access**
* **AC-20 — Use of External Systems**

The target architecture should consolidate legitimate vendor connectivity into an explicitly authorized and monitored remote-access pathway.

---

# LR-04 — Engineering Workstation Privilege

The engineering workstation requires high privilege because it performs legitimate controller programming, configuration, diagnostics, and recovery functions.

The security objective is therefore not to remove its capability but to limit that capability to appropriate systems and authorized activities.

Relevant CSF 2.0 categories include:

* **PR.AA — Identity Management, Authentication, and Access Control**
* **PR.IR — Technology Infrastructure Resilience**

Selected SP 800-53 traceability includes:

* **AC-6 — Least Privilege**
* **SC-7 — Boundary Protection**

The target-state architecture should retain required engineering functionality while reducing unrestricted controller reachability.

---

# LR-05 — Maintenance and External Endpoints

Company maintenance laptops and vendor-owned service laptops should not automatically receive equivalent levels of trust.

A company device can be managed under organizational endpoint policy, while a third-party device may have a security posture that the plant cannot independently verify.

Relevant CSF 2.0 categories include:

* **PR.AA — Identity Management, Authentication, and Access Control**
* **GV.SC — Cybersecurity Supply Chain Risk Management**

Selected SP 800-53 traceability includes:

* **AC-19 — Access Control for Mobile Devices**
* **AC-20 — Use of External Systems**

The target state should preserve necessary equipment service capability while limiting where, when, and how mobile or externally managed systems can connect.

---

# LR-06 — Historian and Data-Access Separation

The historian supports operational analysis but also creates demand for data access by users who do not require process-control privileges.

This makes the historian placement question an architecture issue rather than simply a server-location decision.

Relevant CSF 2.0 categories include:

* **PR.IR — Technology Infrastructure Resilience**
* **PR.DS — Data Security**

Selected SP 800-53 traceability includes:

* **SC-7 — Boundary Protection**
* **CA-9 — Internal System Connections**

The target-state design should separate enterprise data consumption from direct access to higher-criticality OT resources.

---

# LR-07 — Legacy Technology and Operational Resilience

The BACnet MS/TP field networks support process values required by automatic plant logic.

Their continued use represents a modernization constraint rather than an automatic justification for replacement.

Relevant CSF 2.0 categories include:

* **ID.AM — Asset Management**
* **PR.IR — Technology Infrastructure Resilience**

Selected SP 800-53 traceability includes:

* **CM-8 — System Component Inventory**
* Relevant contingency and resilience controls from the **CP family**

The target design should account for the operational dependency and apply compensating protections where legacy devices cannot directly support modern cybersecurity mechanisms.

---

# LR-08 — Roles and Administrative Ownership

The legacy environment distributes responsibility across plant operations, controls personnel, corporate IT, and vendors.

The issue is not shared responsibility itself but uncertainty about who owns specific security decisions and lifecycle activities.

Relevant CSF 2.0 categories include:

* **GV.RR — Roles, Responsibilities, and Authorities**
* **GV.SC — Cybersecurity Supply Chain Risk Management**

Relevant SP 800-53 concepts include organizational program-management and supply-chain controls.

The target operating model should define ownership for:

* Access authorization
* Account lifecycle management
* Remote vendor connectivity
* Network changes
* Asset inventory
* Logging and monitoring
* Configuration management
* System retirement
* Incident coordination

---

# OT Constraint

NIST guidance for OT emphasizes that cybersecurity safeguards must account for operational performance, reliability, and safety requirements.

Accordingly, this case study does not assume that conventional enterprise controls can be applied to industrial systems without evaluating operational consequences.

Target-state controls must therefore:

* Preserve required process communications
* Avoid unacceptable control latency or disruption
* Maintain appropriate local and degraded-operation capability
* Account for legacy equipment limitations
* Preserve necessary maintenance access
* Reduce risk without creating a larger availability or safety problem

---

# Use in Target-State Design

The NIST alignment in this document establishes design guidance rather than a compliance score.

Each major target-state architecture decision will trace back to one or more legacy findings.

The target architecture should therefore be able to demonstrate:

**Finding → Control Objective → Architecture Change → Expected Risk Reduction**

This traceability will provide the basis for evaluating whether the redesigned architecture materially improves cybersecurity while preserving the plant's operational requirements.
