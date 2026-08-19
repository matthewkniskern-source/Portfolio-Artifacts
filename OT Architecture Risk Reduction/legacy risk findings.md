# NIST Alignment

## Purpose

This case study uses NIST guidance to support the risk analysis and target-state architecture.

It is not a formal NIST compliance assessment, and it is not intended to demonstrate complete implementation of every applicable control.

The standards are used for three things:

* Validate that the identified risks are consistent with recognized OT cybersecurity concerns
* Provide a defensible basis for the proposed architecture changes
* Create traceability between findings, control objectives, and expected risk reduction

The primary references are:

- [**NIST SP 800-82 Rev. 3 — Guide to Operational Technology (OT) Security**](references.md#nist-sp-800-82-rev-3)
- [**NIST Cybersecurity Framework (CSF) 2.0**](references.md#nist-cybersecurity-framework-csf-20)
- [**NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations**](references.md#nist-sp-800-53-rev-5)

NIST SP 800-82 Rev. 3 is the primary technical reference because it addresses cybersecurity in operational environments while accounting for availability, reliability, safety, legacy technology, and process constraints.

CSF 2.0 provides the higher-level cybersecurity outcomes.

Selected SP 800-53 controls provide more specific control traceability where it adds value.

---

# Alignment Method

The project uses the following relationship:

> **Observed Condition → Risk Finding → NIST Guidance → Architecture Decision → Expected Risk Reduction**

The intent is to use the standards to support the architecture, not to work backward from a control catalog and force the plant into it.

Controls are selected because they address an identified condition in this environment.

That distinction matters in OT, where a technically correct control can still be a poor control if it creates unacceptable operational consequences.

---

# Legacy Risk Alignment

| Finding                                                  | NIST SP 800-82 Theme                                                         | CSF 2.0 Alignment                                               | Selected SP 800-53 Traceability                                            |
| -------------------------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **LR-01 — Broadly Trusted OT Network**                   | Network segmentation, boundary protection, controlled communications         | PR.IR — Technology Infrastructure Resilience                    | SC-7 — Boundary Protection; CA-9 — Internal System Connections             |
| **LR-02 — Excess Management Supervisory Privilege**      | Access restriction and separation of responsibilities                        | PR.AA — Identity Management, Authentication, and Access Control | AC-3 — Access Enforcement; AC-6 — Least Privilege                          |
| **LR-03 — Persistent Legacy Vendor VPN**                 | Remote-access control and third-party connectivity                           | PR.AA; GV.SC — Cybersecurity Supply Chain Risk Management       | AC-17 — Remote Access; AC-20 — Use of External Systems                     |
| **LR-04 — Broad Engineering Workstation Reachability**   | Protection of high-privilege engineering functions                           | PR.AA; PR.IR                                                    | AC-6 — Least Privilege; SC-7 — Boundary Protection                         |
| **LR-05 — Mobile and Third-Party Maintenance Endpoints** | Maintenance access, mobile systems, and external-device risk                 | PR.AA; GV.SC                                                    | AC-19 — Access Control for Mobile Devices; AC-20 — Use of External Systems |
| **LR-06 — Historian Within Broad OT Trust Zone**         | Separation of control functions from information-consumption paths           | PR.IR; PR.DS — Data Security                                    | SC-7 — Boundary Protection; CA-9 — Internal System Connections             |
| **LR-07 — Legacy MS/TP Process Dependencies**            | Legacy-system constraints, compensating controls, and operational resilience | ID.AM — Asset Management; PR.IR                                 | CM-8 — System Component Inventory; selected CP-family resilience controls  |
| **LR-08 — Ambiguous IT/OT/Vendor Ownership**             | Governance, responsibility, asset ownership, and third-party coordination    | GV.RR — Roles, Responsibilities, and Authorities; GV.SC         | Relevant PM- and SR-family controls                                        |

The mapping is intentionally selective.

The goal is enough traceability to explain the architecture decisions without turning the case study into a control-by-control certification exercise.

---

# LR-01 — Segmentation and Boundary Protection

The legacy architecture places supervisory, engineering, historian, controller, and gateway systems inside a broadly trusted BACnet/IP environment.

That creates more reachability than the plant's operating requirements justify.

NIST OT guidance supports segmentation and controlled communication between security domains so that access follows function rather than simple network presence.

Relevant CSF 2.0 alignment includes:

* **PR.IR — Technology Infrastructure Resilience**

Selected SP 800-53 traceability includes:

* **SC-7 — Boundary Protection**
* **CA-9 — Internal System Connections**

These references support the target-state decision to separate supervisory, engineering, and control functions and permit only required communication between them.

---

# LR-02 — Management Access and Least Privilege

The management role needs plant visibility.

It does not need routine process-control authority.

The legacy state allows both.

This is a straightforward least-privilege issue.

Relevant CSF 2.0 alignment includes:

* **PR.AA — Identity Management, Authentication, and Access Control**

Selected SP 800-53 traceability includes:

* **AC-3 — Access Enforcement**
* **AC-6 — Least Privilege**

The target state preserves the legitimate requirement for visibility while removing supervisory control that is not required by the role.

---

# LR-03 — Vendor Remote Access

The legacy vendor VPN demonstrates a common governance problem: a technically functional access path can remain in place long after the process around it has become unclear.

The concern is not merely that remote access exists.

The concern is whether that access remains:

* Authorized
* Necessary
* Monitored
* Reviewed
* Limited to approved destinations
* Owned by a clearly identified party

Relevant CSF 2.0 alignment includes:

* **PR.AA — Identity Management, Authentication, and Access Control**
* **GV.SC — Cybersecurity Supply Chain Risk Management**

Selected SP 800-53 traceability includes:

* **AC-17 — Remote Access**
* **AC-20 — Use of External Systems**

The target state removes the inherited VPN and consolidates approved vendor support into one controlled remote-access pathway.

---

# LR-04 — Engineering Workstation Privilege

The engineering workstation requires high privilege.

That is not the finding.

The finding is that high privilege is paired with broad network reachability.

Relevant CSF 2.0 alignment includes:

* **PR.AA — Identity Management, Authentication, and Access Control**
* **PR.IR — Technology Infrastructure Resilience**

Selected SP 800-53 traceability includes:

* **AC-6 — Least Privilege**
* **SC-7 — Boundary Protection**

The target-state design keeps the workstation's engineering capability while limiting access to approved controller and infrastructure destinations.

The control objective is not to weaken engineering.

It is to prevent engineering privilege from becoming unnecessary universal reachability.

---

# LR-05 — Maintenance and External Devices

Company maintenance laptops and vendor-owned service laptops may perform similar work, but they should not automatically receive the same level of trust.

A company-managed endpoint can be governed through organizational policy.

A vendor device may be necessary for specialized troubleshooting while remaining outside direct organizational control.

Relevant CSF 2.0 alignment includes:

* **PR.AA — Identity Management, Authentication, and Access Control**
* **GV.SC — Cybersecurity Supply Chain Risk Management**

Selected SP 800-53 traceability includes:

* **AC-19 — Access Control for Mobile Devices**
* **AC-20 — Use of External Systems**

The target state allows the maintenance function while constraining temporary devices to approved service interfaces and authorized tasks.

---

# LR-06 — Historian and Enterprise Data Access

The historian is an operational resource, but it also contains information that enterprise users want.

That creates a natural pressure point between OT and the business.

The legacy approach places both needs against the same historian inside the broad OT trust zone.

Relevant CSF 2.0 alignment includes:

* **PR.IR — Technology Infrastructure Resilience**
* **PR.DS — Data Security**

Selected SP 800-53 traceability includes:

* **SC-7 — Boundary Protection**
* **CA-9 — Internal System Connections**

The target state retains an OT-side historian or collector for operations while exposing approved data through a controlled DMZ-based reporting service.

That preserves plant access to operational history without requiring enterprise users to reach into the control environment.

---

# LR-07 — Legacy MS/TP Dependencies

The BACnet MS/TP field networks provide process values used by automatic plant logic.

They have limited native cybersecurity capability, but they are not operationally disposable.

That makes this less of a patching problem and more of an architecture and compensating-control problem.

Relevant CSF 2.0 alignment includes:

* **ID.AM — Asset Management**
* **PR.IR — Technology Infrastructure Resilience**

Selected SP 800-53 traceability includes:

* **CM-8 — System Component Inventory**
* Selected contingency and resilience controls within the **CP family**

The target approach is to contain the gateways, restrict reachability, monitor behavior where practical, and preserve the process inputs the plant still depends on.

Replacement may eventually be appropriate.

It is not assumed as the immediate cybersecurity answer.

---

# LR-08 — Roles, Responsibilities, and Ownership

The plant environment crosses organizational boundaries.

Operations, controls, IT, cybersecurity personnel, and vendors may all own part of the problem.

That is normal.

The risk appears when nobody clearly owns a specific decision.

Relevant CSF 2.0 alignment includes:

* **GV.RR — Roles, Responsibilities, and Authorities**
* **GV.SC — Cybersecurity Supply Chain Risk Management**

Relevant SP 800-53 traceability includes selected controls from:

* **PM — Program Management**
* **SR — Supply Chain Risk Management**

The target state should clearly assign responsibility for items such as:

* Access approval
* Account lifecycle
* Firewall and boundary management
* Vendor connectivity
* Asset inventory
* Logging and monitoring
* Configuration ownership
* Backup and recovery
* Incident coordination
* System retirement

Shared work is acceptable.

Undefined accountability is not.

---

# OT Control Constraint

NIST guidance is useful here because it does not treat OT as ordinary enterprise IT.

Any proposed safeguard has to be evaluated against the plant's operating requirements.

For this case study, that means controls must:

* Preserve required process communications
* Avoid unacceptable latency or disruption
* Maintain operator access
* Preserve necessary engineering and maintenance capability
* Account for legacy technology
* Support local and degraded operation
* Avoid creating a larger availability or safety problem than the risk being addressed

A control is not considered effective simply because it is technically stronger.

It also has to work in the plant.

---

# Use in the Target State

The NIST alignment provides a defensible basis for the architecture decisions documented in the target state.

It is not being used to claim certification or full compliance.

The expected traceability is:

> **Finding → Control Objective → Architecture Change → Expected Risk Reduction → Validation**

That is enough to show why the proposed controls exist, what they are intended to accomplish, and how they would be tested.

For this case study, that is more useful than a long checklist of controls that may or may not materially affect the plant's actual risk.
