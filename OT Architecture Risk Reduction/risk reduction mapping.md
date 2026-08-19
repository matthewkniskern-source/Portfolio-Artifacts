# Risk Reduction Mapping

## Purpose

This document maps the principal legacy cybersecurity findings to the target-state architecture and identifies the expected reduction in risk.

The purpose is not to claim that the redesigned environment eliminates cyber risk.

Instead, the analysis demonstrates how specific architecture and governance decisions reduce unnecessary trust, privilege, exposure, and attack-path reachability while preserving required plant functionality.

Supporting analysis is available in:

* [Legacy Risk Findings](legacy%20risk%20findings.md)
* [NIST Alignment](nist%20alignment.md)
* [Target Architecture](target%20architecture.md)

---

# Risk Reduction Summary

| Finding                                                     | Legacy Condition                                                                                                         | Target-State Change                                                                                                                          | Expected Risk Reduction                                                                                                     | Residual Risk                                                                                                            |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **LR-01 — Broadly Trusted OT Network**                      | Supervisory, engineering, historian, controller, and gateway systems share broad internal reachability                   | Separate enterprise, DMZ, supervisory, engineering, and control security zones with explicitly permitted communication paths                 | Reduces lateral movement opportunities and limits the blast radius of endpoint compromise                                   | Required cross-zone communications remain potential attack paths and depend on correct rule configuration and monitoring |
| **LR-02 — Excess Management Supervisory Privilege**         | Enterprise-connected management workstation can issue supervisory commands beyond its legitimate business need           | Replace direct control-capable access with read-oriented reporting and plant visibility                                                      | Removes unnecessary command authority and reduces enterprise-originating control exposure                                   | Compromised management or reporting accounts may still expose operational information                                    |
| **LR-03 — Persistent Legacy Vendor VPN**                    | Historical vendor VPN remains functional outside the current recognized access model                                     | Retire legacy VPN and require external support to terminate in the OT DMZ through approved remote access and a privileged jump host          | Eliminates an unmanaged remote pathway and centralizes vendor access for authentication, authorization, logging, and review | Approved third-party access remains high privilege and continues to require strong lifecycle governance                  |
| **LR-04 — Broad Engineering Workstation Reachability**      | Engineering workstation has high privilege and broad controller reachability within the flat OT environment              | Place engineering functions in a separate zone and permit only explicitly authorized paths to required controllers and infrastructure        | Limits the number of assets reachable from a highly privileged workstation and reduces consequences of compromise           | The engineering workstation remains capable of making consequential controller changes to authorized systems             |
| **LR-05 — Mobile and Third-Party Maintenance Endpoints**    | Company and vendor laptops may connect directly to equipment despite materially different security postures              | Restrict mobile devices to approved local service interfaces and distinguish company-managed from externally managed endpoints               | Reduces the chance that temporary maintenance access becomes broad OT network access                                        | Direct connection to critical equipment still creates exposure during authorized maintenance activities                  |
| **LR-06 — Historian Within Broad OT Trust Zone**            | Enterprise data demand places pressure on a historian located within the same broad trust environment as control systems | Retain an OT-side historian/collector while replicating approved data to a DMZ reporting or historian service                                | Separates business data consumption from direct OT access and reduces pressure to expose the control environment            | Replication services create a controlled but still significant cross-boundary dependency                                 |
| **LR-07 — Legacy MS/TP Process Dependencies**               | Operationally required legacy MS/TP devices provide process inputs used by automatic plant logic                         | Contain MS/TP gateways, restrict gateway reachability, prohibit direct enterprise/vendor access, and add passive/anomaly-oriented monitoring | Reduces exposure without disrupting legacy process instrumentation or forcing premature replacement                         | Legacy serial devices remain limited in native security capability and continue to require compensating controls         |
| **LR-08 — Ambiguous IT/OT/Vendor Administrative Ownership** | Responsibility is shared across operations, controls, IT, and vendors without consistently defined ownership             | Define ownership for network boundaries, accounts, remote access, monitoring, configuration, inventory, and incident coordination            | Reduces gaps caused by unclear responsibility and dependence on informal institutional knowledge                            | Governance effectiveness still depends on documentation, review, staffing, and sustained organizational discipline       |

---

# Architecture-Level Risk Reduction

The target state changes the trust model of the environment.

The legacy architecture largely assumes:

**Connected to OT → Broadly trusted**

The target architecture instead assumes:

**Operational requirement → Explicitly permitted communication**

This change reduces the number of systems and users that can reach high-consequence OT assets simply because they are connected to an adjacent network.

The primary architectural improvements are:

* Reduced enterprise-to-OT reachability
* Controlled IT/OT boundary crossings
* Separation of operator and engineering functions
* Explicitly authorized engineering access
* Consolidated vendor remote access
* Removal of inherited management command authority
* Separation of enterprise reporting from primary OT data services
* Containment of legacy field-network gateways
* Increased visibility into abnormal communications
* Preservation of manual and degraded operating capability

---

# Attack-Path Reduction

The target architecture does not assume that initial compromise can always be prevented.

Instead, several design decisions reduce what an attacker or compromised account can reach after gaining access to one part of the environment.

## Example: Enterprise Workstation Compromise

**Legacy condition:**

Enterprise workstation
→ Existing OT access
→ Broad OT network
→ Supervisory or control assets

**Target state:**

Enterprise workstation
→ Enterprise / DMZ boundary
→ Approved DMZ service
→ No direct controller path

The target state therefore reduces the ability of an ordinary enterprise compromise to become a direct control-system compromise.

---

## Example: Vendor Credential Compromise

**Legacy condition:**

Compromised vendor credential
→ Legacy or recognized remote pathway
→ OT environment

**Target state:**

Compromised vendor credential
→ Approved remote-access gateway
→ Privileged jump host
→ Explicitly authorized destination

The credential remains valuable, but its usable path is narrower and more observable.

---

## Example: Engineering Workstation Compromise

**Legacy condition:**

Engineering workstation
→ Broadly trusted OT network
→ Multiple controller and supporting systems

**Target state:**

Engineering workstation
→ Engineering security zone
→ Explicitly allowed controller paths

The workstation remains a high-value target, but the architecture reduces unnecessary reachability beyond its approved engineering function.

---

# Legacy Technology Treatment

The target state does not equate legacy technology with unacceptable technology.

The BACnet MS/TP devices remain operationally necessary because they supply process information used during automatic plant operation.

Risk is therefore reduced around them through:

* Gateway isolation
* Restricted IP-side reachability
* Controlled communication paths
* Removal of enterprise and remote-vendor exposure
* Passive network monitoring
* Behavioral and process-data review
* Preservation of local/manual operating alternatives

This approach acknowledges that cybersecurity improvements in OT often require compensating controls rather than immediate replacement.

---

# Availability and Operational Risk

Cybersecurity risk reduction is not considered successful if the control itself creates unacceptable operational risk.

The target-state architecture therefore preserves:

* Required BACnet communications
* Automatic controller operation
* Operator HMI functionality
* Authorized engineering access
* Equipment service capability
* Vendor maintenance where necessary
* Local equipment controls
* Central physical-board operation
* Degraded/manual plant operation

The design intentionally avoids treating isolation as the same thing as security.

---

# Residual Risk

The target architecture materially reduces several legacy risk conditions but does not eliminate them.

Principal residual risks include:

* Compromise of authorized high-privilege engineering systems
* Misuse or compromise of approved vendor credentials
* Configuration errors in firewall or segmentation rules
* Vulnerabilities in DMZ intermediary systems
* Exposure introduced during authorized maintenance activity
* Limited native security capabilities of legacy field devices
* Failure to maintain accurate asset and access inventories
* Governance controls becoming outdated as personnel and vendors change
* Monitoring systems failing to distinguish cyber anomalies from legitimate process behavior

These risks require continued technical and governance controls rather than further architectural segmentation alone.

---

# Risk Reduction Conclusion

The target-state architecture reduces risk primarily by limiting unnecessary trust.

The redesigned environment does not depend on wholesale equipment replacement or elimination of legitimate operational capabilities.

Instead, it introduces:

**Segmentation → Explicit Access → Controlled Intermediation → Reduced Privilege → Improved Visibility → Defined Ownership**

The resulting architecture remains operationally recognizable as the same central utility plant while materially reducing the number of pathways through which a compromise can affect higher-consequence control functions.
