# Executive Summary

## OT Architecture Risk Reduction Case Study

### Executive Objective

This case study evaluates cybersecurity risk within a representative central utility plant and develops a target-state architecture that reduces unnecessary trust, excessive privilege, unmanaged access, and lateral movement opportunities without disrupting the operational capabilities required to run the plant.

The reference environment reflects a realistic hybrid OT architecture consisting of:

* BACnet/IP supervisory and control communications
* Operationally necessary BACnet MS/TP field networks
* SCADA/BAS supervisory systems
* Operator HMI workstations
* Engineering and maintenance access
* Historian services
* Vendor support pathways
* Local and physical plant-control capability

The analysis focuses on one central question:

> **How can OT cybersecurity risk be materially reduced while preserving plant availability, maintainability, and operational resilience?**

---

# Executive Finding

The principal weakness of the legacy environment is not any single obsolete device or vulnerable protocol.

It is **accumulated trust**.

Over time, legitimate operational, maintenance, management, and vendor requirements created an environment in which systems and users possessed more reachability or privilege than their current functions required.

The legacy architecture therefore exposes the plant to elevated risk from:

* Broad internal OT connectivity
* Excess supervisory privilege
* Persistent third-party access
* Highly privileged engineering systems
* Mobile and externally managed maintenance devices
* Enterprise demand for operational data
* Legacy field-device dependencies
* Unclear administrative ownership

The plant remains operationally functional, but compromise of a relatively limited endpoint, credential, or access pathway may have consequences beyond that asset's intended role.

---

# Legacy-State Risk Profile

The legacy environment relies primarily on a perimeter boundary surrounding a largely flat BACnet/IP control network.

Within that environment, supervisory, engineering, historian, controller, and gateway systems have relatively broad internal reachability.

Several additional conditions increase exposure:

| Risk Condition                                 | Executive Impact                                                                  |
| ---------------------------------------------- | --------------------------------------------------------------------------------- |
| Flat OT trust model                            | A compromised OT endpoint may reach systems outside its intended function         |
| Management workstation with control capability | Business-facing access can directly affect plant operation                        |
| Persistent legacy vendor VPN                   | Third-party access exists outside the current governance model                    |
| Broad engineering workstation reachability     | Compromise of a privileged system may affect multiple controllers                 |
| Vendor and maintenance laptops                 | Temporary endpoints may interact directly with critical equipment                 |
| Historian inside broad OT trust zone           | Business data requirements encourage deeper enterprise-to-OT access               |
| Legacy MS/TP dependencies                      | Modernization cannot simply remove older devices without operational consequences |
| Shared IT/OT/vendor responsibility             | Security tasks may fall between organizational boundaries                         |

Detailed findings are available in the [Legacy Risk Findings](legacy%20risk%20findings.md).

---

# Target-State Response

The proposed architecture changes the plant's trust model without materially changing the underlying industrial process.

The legacy assumption:

> **Connected to OT → Broadly trusted**

is replaced with:

> **Operational requirement → Explicitly permitted access**

The target state introduces:

### OT DMZ

Enterprise and external users no longer communicate directly with the control environment.

Approved services terminate or exchange information through an OT demilitarized zone.

### Segmented OT Security Zones

Operator, engineering, administrative, and control functions are logically separated according to their operational roles and privilege levels.

### Explicit Communication Paths

High-privilege systems retain the access required to perform their functions but do not receive unrestricted reachability simply because they reside within OT.

### Governed Vendor Access

Remote vendor connectivity is consolidated through an approved remote-access gateway and privileged jump host.

The inherited legacy VPN is removed.

### Reduced Management Privilege

Management retains plant visibility without unnecessary process-control authority.

### Controlled Historian Architecture

Operational historian functionality remains available to plant personnel while approved data is replicated outward for enterprise reporting.

### Legacy-System Containment

Operationally necessary BACnet MS/TP devices remain in service but are protected through gateway isolation, restricted reachability, compensating controls, and passive monitoring.

### Preserved Manual Operation

Physical plant controls and degraded operating procedures remain available if centralized supervisory systems are unavailable.

---

# Expected Risk Reduction

The proposed architecture is designed primarily to reduce the consequences of compromise.

| Legacy Exposure                        | Target-State Effect                                   |
| -------------------------------------- | ----------------------------------------------------- |
| Broad OT lateral movement              | Security zones reduce reachable assets                |
| Direct enterprise-to-control exposure  | DMZ intermediates IT/OT communications                |
| Excess management privilege            | Read-oriented visibility replaces unnecessary control |
| Unmanaged vendor pathway               | Remote access becomes centralized and governed        |
| Engineering workstation exposure       | Explicit access limits high-privilege reachability    |
| Direct business access to OT historian | Replicated data supports enterprise consumption       |
| Legacy-device exposure                 | Gateways and compensating controls contain risk       |
| Limited visibility                     | Passive OT monitoring improves anomaly detection      |
| Informal responsibility                | Administrative ownership becomes explicit             |

The complete comparison is documented in the [Risk Reduction Mapping](risk%20reduction%20mapping.md).

---

# Operational Constraint

The target architecture is intentionally designed around OT realities rather than conventional enterprise assumptions.

Cybersecurity controls must not introduce a larger operational risk than the threat they are intended to mitigate.

The redesign therefore preserves:

* Automatic control functions
* Required BACnet communications
* Operator HMI capability
* Authorized engineering access
* Vendor maintenance capability
* Equipment-level service access
* Local controller logic
* Central physical-board operation
* Degraded/manual plant operation

The project does not assume that legacy technology can simply be patched, replaced, or disconnected.

Where modern endpoint protections cannot be applied directly, the architecture relies on containment, controlled communications, monitoring, and compensating controls.

---

# NIST Alignment

The architecture is informed by:

* **NIST SP 800-82 Rev. 3** for operational technology security guidance
* **NIST Cybersecurity Framework 2.0** for cybersecurity outcomes and governance alignment
* **NIST SP 800-53 Rev. 5** for selected control-level traceability

NIST guidance is used as a decision framework rather than as a compliance checklist.

The analytical model is:

> **Observed Condition → Risk Finding → NIST Guidance → Architecture Decision → Expected Risk Reduction**

Detailed framework mappings are available in [NIST Alignment](nist%20alignment.md).

---

# Residual Risk

The target state materially reduces exposure but does not eliminate cyber risk.

Significant residual risks remain around:

* Privileged engineering systems
* Authorized vendor credentials
* Firewall and segmentation misconfiguration
* DMZ intermediary systems
* Temporary maintenance activity
* Legacy field devices
* Monitoring accuracy
* Asset inventory accuracy
* Governance drift over time

These risks require continued technical controls, periodic review, and operational governance.

The objective is not zero risk.

The objective is to ensure that remaining risks are:

> **Visible, constrained, governed, and operationally understood.**

---

# Executive Conclusion

The case study demonstrates that meaningful OT cybersecurity improvement does not require replacing the entire industrial environment.

The most significant risk reduction comes from changing how trust is granted.

By separating enterprise and OT functions, controlling remote access, reducing unnecessary privilege, isolating high-consequence engineering functions, containing legacy field networks, and preserving operational resilience, the target architecture reduces the number of pathways through which a cyber event can affect physical operations.

The resulting design preserves the plant's operational purpose while creating a more defensible cybersecurity posture.

> **Preserve the process. Reduce unnecessary trust. Constrain access. Improve visibility. Maintain operational resilience.**
