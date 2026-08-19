# OT Architecture Risk Reduction

### Comparative Industrial Network Security Case Study

This case study evaluates cybersecurity risk within a fictionalized central utility plant and develops a target-state OT architecture that reduces unnecessary trust, privilege, and attack-path reachability while preserving operational requirements.

The reference environment combines a predominantly **BACnet/IP control network** with operationally necessary **BACnet MS/TP field devices**, supervisory control systems, engineering access, historian services, vendor support, and local/manual plant controls.

Rather than replacing the industrial process or assuming that all legacy technology can be modernized immediately, the project holds the underlying plant function largely constant and asks a narrower question:

> **How can architectural cybersecurity controls materially reduce OT risk without creating unacceptable operational risk?**

---

## Executive Snapshot

The legacy environment is operationally functional but relies heavily on perimeter protection and broad internal trust.

Key risk conditions include:

* A largely flat BACnet/IP OT network
* Limited separation between supervisory, engineering, historian, and controller functions
* Excess supervisory privilege from an enterprise-connected management workstation
* A persistent legacy vendor VPN outside the currently recognized access model
* Broad reachability from a highly privileged engineering workstation
* Direct maintenance access from company and vendor laptops
* Operational dependence on legacy BACnet MS/TP process inputs
* Shared IT, OT, maintenance, and vendor responsibilities with incomplete ownership boundaries

The target architecture reduces these exposures through:

* Enterprise / OT separation
* An OT demilitarized zone
* Segmented supervisory, engineering, and control zones
* Explicitly permitted communication paths
* Governed vendor remote access through a privileged jump host
* Separation of business visibility from process-control authority
* Controlled historian replication for enterprise consumption
* Containment and monitoring of legacy field-network gateways
* Passive and anomaly-oriented OT monitoring
* Defined administrative ownership
* Preservation of local and degraded plant operation

---

# Architecture Comparison

## Legacy State

The legacy architecture represents a common evolutionary condition in OT: equipment and access paths were added over time to satisfy legitimate operating, maintenance, and business needs, but the resulting trust model was never comprehensively redesigned around modern cybersecurity principles.

**Primary trust model:**

> **Connected to OT → Broadly trusted**

[View the Legacy Architecture](legacy%20architecture.md)
[View the Legacy Topology](legacy%20topo.mmd)

---

## Target State

The target architecture preserves the existing industrial process while introducing controlled trust boundaries around the systems that support it.

Enterprise users, operators, engineers, vendors, and legacy devices retain the functions they legitimately require without inheriting unnecessary access to the rest of the control environment.

**Target trust model:**

> **Operational requirement → Explicitly permitted access**

[View the Target Architecture](target%20architecture.md)
[View the Target Topology](target%20topo.mmd)

---

# Key Risk Findings

| ID        | Finding                                         | Priority      |
| --------- | ----------------------------------------------- | ------------- |
| **LR-01** | Broadly Trusted OT Network                      | High          |
| **LR-02** | Excess Management Supervisory Privilege         | High          |
| **LR-03** | Persistent Legacy Vendor VPN                    | High          |
| **LR-04** | Broad Engineering Workstation Reachability      | High          |
| **LR-05** | Mobile and Third-Party Maintenance Endpoints    | Moderate-High |
| **LR-06** | Historian Within Broad OT Trust Zone            | Moderate      |
| **LR-07** | Dependency on Legacy MS/TP Process Inputs       | Moderate-High |
| **LR-08** | Ambiguous IT/OT/Vendor Administrative Ownership | Moderate-High |

The findings are evaluated in detail in the [Legacy Risk Findings](legacy%20risk%20findings.md).

---

# Risk-Reduction Strategy

The target design does not depend on a wholesale replacement of plant equipment.

Instead, the architecture focuses on reducing the consequences of compromise by constraining trust and reachability.

| Legacy Condition                     | Target-State Response                                 |
| ------------------------------------ | ----------------------------------------------------- |
| Broad OT reachability                | Segmented supervisory, engineering, and control zones |
| Direct enterprise-to-OT exposure     | OT DMZ and controlled intermediary services           |
| Excess management command capability | Read-oriented management visibility                   |
| Persistent legacy VPN                | Governed remote-access gateway and jump host          |
| Broad engineering access             | Explicit controller communication paths               |
| Enterprise demand for historian data | Controlled replication to a DMZ reporting service     |
| Legacy MS/TP dependencies            | Gateway containment and compensating controls         |
| Limited internal visibility          | Passive OT and anomaly-oriented monitoring            |
| Informal ownership                   | Defined administrative and vendor responsibilities    |

The full before-and-after analysis is available in the [Risk Reduction Mapping](risk%20reduction%20mapping.md).

---

# Legacy Technology as an Operational Constraint

The case study deliberately retains legacy BACnet MS/TP devices that provide process values used during automatic plant operation.

Representative inputs include:

* Differential pressure
* Supply and return water temperature
* Condenser-water temperature
* Flow and status information
* Equipment permissives

These devices cannot be treated as disposable simply because they use older communications technology.

The target architecture therefore emphasizes:

**Containment → Restricted Reachability → Gateway Protection → Passive Visibility → Compensating Controls**

rather than immediate replacement.

This distinction is central to the case study: **OT cybersecurity decisions must account for the physical process being protected.**

---

# Operational Resilience

The reference plant is designed so that loss of centralized supervisory capability does not automatically equal loss of physical plant control.

The environment retains:

* Local controller logic
* Equipment-mounted controls
* Local control panels
* Physical selectors
* Manufacturer service interfaces
* A central physical control board

An experienced operator can therefore maintain a reduced or manual plant configuration during supervisory-system impairment.

The target cybersecurity architecture is required to preserve this capability.

---

# NIST-Informed Methodology

The project uses NIST guidance as a design and traceability framework rather than as a compliance checklist.

Primary references include:

* **NIST SP 800-82 Rev. 3** — Operational Technology security guidance
* **NIST Cybersecurity Framework 2.0**
* **NIST SP 800-53 Rev. 5** — Selected control traceability

The project follows the analytical relationship:

> **Observed Condition → Risk Finding → NIST Guidance → Architecture Decision → Expected Risk Reduction**

Detailed mappings are available in [NIST Alignment](nist%20alignment.md).

---

# Validation Philosophy

The target architecture is not considered successful merely because it blocks traffic.

Controls must demonstrate both:

> **Reduced Cybersecurity Exposure**

and

> **Preserved Operational Capability**

Validation therefore considers:

* Network segmentation
* Access enforcement
* Vendor remote access
* Engineering reachability
* Historian data flow
* Legacy MS/TP containment
* Passive monitoring
* Maintenance access
* Local and degraded plant operation
* Governance ownership

See [Validation and Residual Risk](validation%20and%20residual%20risk.md) for the proposed validation methodology and remaining risks.

---

# Case Study Method

The project develops the architecture through the following sequence:

**Reference Environment**
↓
**Communication Requirements**
↓
**Asset and Access Inventory**
↓
**Legacy Architecture**
↓
**Risk Identification**
↓
**NIST Alignment**
↓
**Target Architecture**
↓
**Risk Reduction**
↓
**Validation and Residual Risk**

This structure provides traceability from operational requirement through cybersecurity decision.

---

# Repository Navigation

| Document                                                              | Purpose                                                                                |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [Environment Overview](environment%20overview.md)                     | Defines the fictionalized central utility plant and project boundaries                 |
| [Communication Requirements](communication%20requirements.md)         | Identifies legitimate OT, maintenance, business, and remote communication needs        |
| [Asset and Access Inventory](asset%20access%20inventory.md)           | Defines major cyber-relevant assets, user roles, and access relationships              |
| [Legacy Architecture](legacy%20architecture.md)                       | Documents the effective current-state architecture                                     |
| [Legacy Topology](legacy%20topo.mmd)                                  | Visual representation of the largely flat legacy environment                           |
| [Legacy Risk Findings](legacy%20risk%20findings.md)                   | Identifies and analyzes eight principal legacy risk conditions                         |
| [NIST Alignment](nist%20alignment.md)                                 | Maps findings to relevant NIST OT guidance, CSF outcomes, and selected controls        |
| [Target Architecture](target%20architecture.md)                       | Defines the segmented target-state security architecture                               |
| [Target Topology](target%20topo.mmd)                                  | Visual representation of the proposed target state                                     |
| [Risk Reduction Mapping](risk%20reduction%20mapping.md)               | Compares legacy conditions, architectural changes, expected effects, and residual risk |
| [Validation and Residual Risk](validation%20and%20residual%20risk.md) | Defines validation activities and identifies risks remaining after redesign            |

---

# Scope and Limitations

This project is a conceptual cybersecurity architecture case study rather than a production engineering design.

It does not attempt to provide:

* Vendor-specific firewall configurations
* Production IP addressing
* Detailed PLC logic
* Complete BACnet configuration
* Safety-system engineering
* Complete NIST or IEC 62443 compliance certification
* Detailed incident-response procedures
* Capital replacement planning
* A complete legacy-device modernization roadmap

Those topics may require separate engineering, governance, or modernization efforts.

---

# Conclusion

The central finding of this case study is that the greatest weakness in the legacy environment is not simply the presence of old technology.

It is **accumulated trust**.

Operational requirements, maintenance practices, business convenience, vendor relationships, and legacy systems gradually produced connectivity and privilege beyond what many individual functions actually required.

The target architecture reduces that exposure without attempting to turn an industrial plant into an enterprise IT network.

The result is the same underlying physical process operating within a more defensible trust model:

> **Preserve the process. Reduce unnecessary trust. Constrain access. Improve visibility. Maintain operational resilience.**
