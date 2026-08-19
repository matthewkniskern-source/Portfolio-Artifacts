# OT Architecture Risk Reduction

### Comparative Industrial Network Security Case Study

This project looks at a problem that is common in operational technology environments: a plant can be running reliably while the network around it has accumulated years of access, trust, vendor support, legacy equipment, and business convenience that no longer make sense from a cybersecurity standpoint.

The reference environment is a fictionalized central utility plant built around a predominantly BACnet/IP control network with legacy BACnet MS/TP field devices, SCADA/BAS supervisory systems, operator workstations, engineering access, historian services, vendor support, and physical/manual plant controls.

The goal is not to design a perfect greenfield OT network.

It is to take a plant that already works and answer a harder question:

> **How do you materially reduce cybersecurity risk without creating a larger operational problem?**

---

## Quick Navigation

If you only have a few minutes, start here:

* [Executive Summary](executive%20summary.md)
* [Legacy Topology](legacy%20topo.mmd)
* [Legacy Risk Findings](legacy%20risk%20findings.md)
* [Target Topology](target%20topo.mmd)
* [Risk Reduction Mapping](risk%20reduction%20mapping.md)

The remaining documents provide the operating assumptions, communication requirements, NIST alignment, architecture rationale, and validation detail behind those conclusions.

---

# What This Case Study Found

The main problem in the legacy environment is not simply old equipment.

It is **accumulated trust**.

Over time, reasonable operating and maintenance decisions created a network where systems and users could reach farther than their actual jobs required.

The legacy environment includes:

* A largely flat BACnet/IP OT network
* Limited separation between operator, engineering, historian, and controller functions
* Management access that accumulated supervisory control capability beyond the actual business need
* A historical vendor VPN that remains technically available outside the current recognized access model
* A highly privileged engineering workstation with broad controller reachability
* Company and vendor laptops used for direct equipment troubleshooting
* Operational dependence on legacy BACnet MS/TP process inputs
* Shared responsibility across plant operations, controls personnel, enterprise IT, and vendors

None of those conditions is especially hard to imagine in a plant that has evolved over time.

The problem is what happens when they all exist together.

A compromise of one workstation, credential, vendor path, or maintenance endpoint may be able to affect systems well beyond the function that originally justified the access.

---

# Legacy Architecture

The legacy plant uses BACnet/IP as the primary supervisory and control backbone.

Operationally important legacy BACnet MS/TP field networks continue feeding process information such as differential pressure, temperature, flow, status, and permissive data into the plant's automatic control logic.

The network is functional, maintainable, and familiar to the people operating it.

It is also broadly trusted internally.

The effective legacy model is:

> **Connected to OT → Broadly trusted**

That creates unnecessary reachability between systems with very different purposes and privilege levels.

[Read the Legacy Architecture](legacy%20architecture.md)

[View the Legacy Topology](legacy%20topo.mmd)

---

# Key Risk Findings

Eight primary risk conditions were identified.

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

The detailed findings, evidence, risk statements, and target-state directions are documented in:

[Legacy Risk Findings](legacy%20risk%20findings.md)

---

# Target Architecture

The redesign does not replace the plant.

It changes how trust is granted around it.

The target model becomes:

> **Operational requirement → Explicitly permitted access**

The redesigned architecture introduces:

* Enterprise / OT separation
* An OT DMZ
* Separate supervisory, engineering, and control zones
* Explicitly allowed communication paths
* Governed vendor remote access through a controlled gateway and jump host
* Read-oriented management visibility without unnecessary process-control authority
* Controlled historian replication for enterprise reporting
* Restricted access to legacy MS/TP gateways
* Passive and anomaly-oriented OT monitoring
* Clearer administrative ownership
* Continued local and manual plant-control capability

High privilege is still available where it is operationally required.

It just no longer comes with unnecessary universal reachability.

[Read the Target Architecture](target%20architecture.md)

[View the Target Topology](target%20topo.mmd)

---

# Before and After

| Legacy Condition                     | Target-State Response                                 |
| ------------------------------------ | ----------------------------------------------------- |
| Broad OT reachability                | Segmented supervisory, engineering, and control zones |
| Direct enterprise-to-OT exposure     | OT DMZ and controlled intermediary services           |
| Excess management command capability | Read-oriented management visibility                   |
| Persistent legacy vendor VPN         | Governed remote-access gateway and jump host          |
| Broad engineering reachability       | Explicitly permitted controller paths                 |
| Enterprise demand for historian data | Controlled replication to a DMZ reporting service     |
| Legacy MS/TP exposure                | Gateway containment and compensating controls         |
| Limited internal visibility          | Passive OT and anomaly-oriented monitoring            |
| Informal administrative ownership    | Defined technical and governance responsibilities     |

The full comparison, including residual risk, is documented in:

[Risk Reduction Mapping](risk%20reduction%20mapping.md)

---

# Legacy Does Not Mean Disposable

The BACnet MS/TP devices in this case study remain operationally important.

They provide process values used by automatic plant logic, including:

* Chilled-water differential pressure
* Supply and return water temperature
* Condenser-water temperature
* Flow and status information
* Equipment permissives

Removing them simply because they are old would solve the cybersecurity problem by creating an operational problem.

That is not an improvement.

The target architecture instead protects the environment around them through:

**Containment → Restricted Reachability → Gateway Protection → Passive Visibility → Compensating Controls**

This is one of the central assumptions of the project: **the physical process has to remain part of the cybersecurity decision.**

---

# Maintenance Still Has to Work

The plant also cannot be designed around the assumption that nobody ever needs to plug into anything.

Company maintenance technicians may need direct service-port access to troubleshoot equipment.

Vendors may arrive with manufacturer-specific laptops and software that the plant does not own or administer.

Those are real maintenance requirements.

The target state therefore does not try to eliminate them. It limits those devices to the equipment and access required for the maintenance task rather than treating temporary service access as broad OT trust.

The same principle applies to remote vendors.

Remote support remains available, but outside users land in the OT DMZ and move through a controlled jump host before reaching an explicitly authorized destination.

The old vendor VPN does not come with them.

---

# Operational Resilience

SCADA availability and plant availability are not treated as the same thing.

The reference plant retains:

* Local controller logic
* Equipment-mounted controls
* Local control panels
* Physical selectors
* Manufacturer service interfaces
* A central physical control board

If centralized supervisory control is unavailable, an experienced operator can maintain a reduced or manual plant configuration.

That capability is deliberately preserved in the target architecture.

Cybersecurity controls that make the plant more secure on paper while making it less recoverable or less operable in practice are not treated as successful controls.

---

# NIST Basis

The architecture is informed primarily by:

* **NIST SP 800-82 Rev. 3**
* **NIST Cybersecurity Framework 2.0**
* **NIST SP 800-53 Rev. 5**

NIST is used here as a design and traceability framework, not as a checklist pasted over the project after the fact.

The working model is:

> **Observed Condition → Risk Finding → NIST Guidance → Architecture Decision → Expected Risk Reduction**

Detailed mappings are available in:

[NIST Alignment](nist%20alignment.md)

---

# Validation

A firewall rule is not successful simply because it blocks traffic.

The target architecture has to prove two things:

> **Cybersecurity exposure went down.**

and

> **The plant still works.**

The validation approach therefore checks:

* Network segmentation
* Management access
* Vendor remote access
* Engineering reachability
* Historian replication
* Legacy MS/TP containment
* Passive monitoring
* Maintenance access
* Local and degraded operation
* Administrative ownership

The project also identifies the risk that remains after redesign rather than treating the target architecture as a zero-risk state.

[Validation and Residual Risk](validation%20and%20residual%20risk.md)

---

# How the Analysis Was Built

The project follows a deliberate sequence:

**Reference Environment**
↓
**Communication Requirements**
↓
**Asset and Access Inventory**
↓
**Legacy Architecture**
↓
**Risk Findings**
↓
**NIST Alignment**
↓
**Target Architecture**
↓
**Risk Reduction**
↓
**Validation and Residual Risk**

That sequence matters.

The target network was not designed first and justified afterward.

The architecture grew out of what the plant actually needed to do, which systems required access, where the legacy exposure existed, and which controls could reduce that exposure without compromising operations.

---

# Repository Navigation

| Document                                                              | What It Covers                                                                                         |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| [Executive Summary](executive%20summary.md)                           | Management-facing summary of the problem, proposed architecture, expected reduction, and residual risk |
| [Environment Overview](environment%20overview.md)                     | Defines the reference plant and project boundaries                                                     |
| [Communication Requirements](communication%20requirements.md)         | Defines legitimate control, maintenance, business, and remote communication needs                      |
| [Asset and Access Inventory](asset%20access%20inventory.md)           | Defines cyber-relevant assets, users, privilege, and access relationships                              |
| [Legacy Architecture](legacy%20architecture.md)                       | Documents how the effective legacy environment operates                                                |
| [Legacy Topology](legacy%20topo.mmd)                                  | Visual model of the broadly trusted legacy network                                                     |
| [Legacy Risk Findings](legacy%20risk%20findings.md)                   | Detailed analysis of the eight primary risk conditions                                                 |
| [NIST Alignment](nist%20alignment.md)                                 | Connects findings to NIST OT guidance, CSF outcomes, and selected controls                             |
| [Target Architecture](target%20architecture.md)                       | Defines the redesigned OT security architecture                                                        |
| [Target Topology](target%20topo.mmd)                                  | Visual model of the segmented target state                                                             |
| [Risk Reduction Mapping](risk%20reduction%20mapping.md)               | Maps each legacy condition to the target control and remaining risk                                    |
| [Validation and Residual Risk](validation%20and%20residual%20risk.md) | Defines how the design would be tested and what risk remains                                           |

---

# Scope

This is a conceptual OT cybersecurity architecture case study, not a production engineering package.

It does not attempt to provide:

* Production firewall rule sets
* IP addressing
* Detailed PLC programming
* Complete BACnet configuration
* Vendor-specific deployment instructions
* Safety-system engineering
* Full NIST or IEC 62443 certification
* A complete incident-response program
* Capital replacement planning
* A full legacy-device modernization roadmap

Those would be separate engineering or governance efforts.

---

# Bottom Line

This case study does not argue that every old OT device needs to disappear.

It argues that old architectures should not be allowed to keep every trust relationship they accumulated along the way.

The plant still needs to run. Operators still need control. Technicians still need diagnostic access. Vendors still need to service specialized equipment. Management still needs visibility.

Those requirements can be preserved without giving every system or user more access than the job requires.

> **Preserve the process. Reduce unnecessary trust. Constrain access. Improve visibility. Maintain operational resilience.**
