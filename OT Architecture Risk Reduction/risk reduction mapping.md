# Risk Reduction Mapping

## Purpose

This page maps each major legacy risk to the target-state control intended to reduce it.

The goal is not to claim that the redesign eliminates cyber risk.

The goal is to show that each architecture change has a reason, addresses a specific problem, and produces a measurable reduction in exposure while keeping the plant operable.

Supporting detail is available in:

* [Legacy Risk Findings](legacy%20risk%20findings.md)
* [NIST Alignment](nist%20alignment.md)
* [Target Architecture](target%20architecture.md)
* [Validation and Residual Risk](validation%20and%20residual%20risk.md)

---

# Risk Reduction Summary

| Finding                                                  | Legacy Condition                                                                                             | Target-State Change                                                                                          | Expected Risk Reduction                                                                     | Residual Risk                                                                                    |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **LR-01 — Broadly Trusted OT Network**                   | Supervisory, engineering, historian, controller, and gateway systems share broad internal reachability       | Separate enterprise, DMZ, supervisory, engineering, and control zones with explicitly permitted paths        | Reduces lateral movement and limits blast radius after endpoint compromise                  | Required cross-zone traffic still creates attack paths and depends on correct rule configuration |
| **LR-02 — Excess Management Supervisory Privilege**      | Enterprise-connected management workstation can issue commands beyond its actual business need               | Replace direct supervisory control with read-oriented plant visibility                                       | Removes unnecessary command authority and reduces enterprise-originating control exposure   | Management accounts and reporting systems still expose operational information                   |
| **LR-03 — Persistent Legacy Vendor VPN**                 | Historical vendor VPN remains technically available outside the current recognized access model              | Retire the legacy VPN and require approved remote access through the OT DMZ and jump host                    | Removes an unmanaged remote path and centralizes authentication, logging, and access review | Approved vendor access remains privileged and must still be governed                             |
| **LR-04 — Broad Engineering Workstation Reachability**   | Engineering workstation has high privilege and broad controller access                                       | Place engineering in a separate zone and allow only approved controller and infrastructure paths             | Reduces the number of systems reachable from a compromised engineering workstation          | The workstation still retains legitimate high-impact capability on approved systems              |
| **LR-05 — Mobile and Third-Party Maintenance Endpoints** | Company and vendor laptops connect directly to equipment with different security postures                    | Limit mobile devices to approved local service interfaces and approved maintenance tasks                     | Reduces the chance that temporary maintenance access becomes broad OT access                | Direct equipment connection still creates temporary exposure                                     |
| **LR-06 — Historian Within Broad OT Trust Zone**         | Enterprise reporting demand pushes access toward an OT historian located inside the control environment      | Keep an OT-side historian or collector and replicate approved data to a DMZ reporting service                | Separates business data use from direct OT access                                           | Replication remains a controlled cross-boundary dependency                                       |
| **LR-07 — Legacy MS/TP Process Dependencies**            | Operationally required MS/TP devices feed process inputs into automatic plant logic                          | Contain gateways, restrict reachability, block unrelated access, and add passive/anomaly-oriented monitoring | Reduces exposure without forcing premature replacement of working field devices             | Legacy devices still have limited native security and require compensating controls              |
| **LR-08 — Ambiguous IT/OT/Vendor Ownership**             | Responsibility is shared across operations, controls, IT, and vendors without consistently defined ownership | Define ownership for access, boundaries, monitoring, configuration, inventory, and incident coordination     | Reduces gaps caused by unclear responsibility and institutional knowledge                   | Governance can drift if ownership and documentation are not maintained                           |

---

# Architecture-Level Change

The legacy environment mostly works on this assumption:

> **Connected to OT → Broadly trusted**

The target state replaces that with:

> **Operational requirement → Explicitly permitted access**

That one change drives most of the risk reduction in the project.

It means:

* Enterprise users do not reach control assets directly
* Managers get visibility without inheriting operator authority
* Vendors enter through one governed remote-access path
* Engineering retains high privilege without universal reachability
* Historian data can leave OT without dragging enterprise users into OT
* Legacy gateways remain useful without being broadly exposed
* Maintenance access stays practical without becoming permanent trust

---

# Attack-Path Reduction

The target architecture is not designed around the assumption that compromise can always be prevented.

It is designed so that compromise of one system does not automatically expose everything around it.

## Enterprise Workstation

**Legacy:**

Enterprise workstation
→ Existing OT access
→ Broad OT environment
→ Supervisory or control assets

**Target:**

Enterprise workstation
→ Enterprise / DMZ boundary
→ Approved intermediary service
→ No direct controller path

The enterprise endpoint can still be compromised.

What changes is how far that compromise can travel.

---

## Vendor Credential

**Legacy:**

Vendor credential
→ Recognized or legacy remote path
→ OT environment

**Target:**

Vendor credential
→ Approved remote-access gateway
→ Jump host
→ Explicitly authorized destination

The credential still has value.

The path is narrower, more visible, and easier to revoke.

---

## Engineering Workstation

**Legacy:**

Engineering workstation
→ Broad OT network
→ Multiple controller and supporting systems

**Target:**

Engineering workstation
→ Engineering zone
→ Explicitly allowed controller paths

The workstation remains powerful because it has to be.

The architecture simply stops treating that power as a reason for unrestricted reachability.

---

# Legacy Technology

The target state does not solve legacy OT risk by pretending old devices can disappear overnight.

BACnet MS/TP field devices still provide process values used by automatic plant logic.

The risk-reduction strategy around them is:

* Restrict who can reach the gateways
* Prevent direct enterprise and vendor access
* Keep the field networks inside defined trust boundaries
* Monitor BACnet/IP-side behavior where practical
* Use process context to help identify abnormal conditions
* Preserve local/manual operating capability

The design reduces exposure around the devices even when the devices themselves cannot support modern endpoint controls.

---

# Operational Tradeoff

A control is only useful if the plant can still run.

The target state therefore preserves:

* Required BACnet communications
* Operator HMI access
* Engineering functions
* Historian availability
* Vendor maintenance
* Equipment-level service access
* Local controller logic
* Central physical-board operation
* Degraded/manual operation

The objective is not maximum isolation.

It is **enough isolation to reduce unnecessary risk without breaking required operations**.

---

# Residual Risk

The redesign still leaves real risk.

That includes:

* High-value engineering systems
* Approved vendor credentials
* Firewall and segmentation misconfiguration
* DMZ intermediary compromise
* Maintenance activity
* Legacy device limitations
* Monitoring false positives and false negatives
* Outdated inventories
* Governance drift

Those risks are not architecture failures.

They are the remaining risks that still have to be managed after the architecture has done what it can.

For a deeper treatment, see [Validation and Residual Risk](validation%20and%20residual%20risk.md).

---

# Bottom Line

The target state does not make the plant invulnerable.

It makes compromise harder to spread.

It removes access that is no longer justified, narrows high-privilege paths, separates business requirements from control authority, and gives legacy systems protection they cannot provide for themselves.

That is the core risk-reduction outcome:

> **Less unnecessary trust. Smaller blast radius. Better visibility. Same plant.**
