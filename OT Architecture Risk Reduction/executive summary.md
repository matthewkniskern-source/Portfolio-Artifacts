# Executive Summary

## OT Architecture Risk Reduction Case Study

This case study evaluates cybersecurity risk in a representative central utility plant and develops a target-state architecture that reduces unnecessary trust, privilege, and attack-path reachability without disrupting the plant’s ability to operate.

The reference environment combines BACnet/IP supervisory control, legacy BACnet MS/TP field devices, SCADA/BAS systems, engineering access, historian services, vendor support, and local/manual plant controls.

The central question is straightforward:

> **How do you materially reduce OT cybersecurity risk without creating a larger operational problem?**

---

## Executive Finding

The primary weakness in the legacy environment is not simply old equipment.

It is **accumulated trust**.

Over time, legitimate operating, maintenance, management, and vendor requirements created access that extended beyond what many users and systems actually needed.

The result is an operationally functional plant with several avoidable risk conditions:

* A largely flat BACnet/IP OT network
* Limited separation between operator, engineering, historian, and controller functions
* Management access with unnecessary supervisory control capability
* A legacy vendor VPN that remains technically available outside the current access model
* Broad reachability from a highly privileged engineering workstation
* Direct maintenance access from both company and vendor laptops
* Operational dependence on legacy MS/TP process inputs
* Shared responsibility across operations, controls, IT, and vendors without consistently defined ownership

Any one of these conditions is understandable in an operating plant.

Taken together, they create an environment where compromise of a relatively limited endpoint, credential, or access path can reach farther than its intended function requires.

---

## Target-State Response

The target architecture changes the trust model while keeping the underlying plant process intact.

The legacy model is effectively:

> **Connected to OT → Broadly trusted**

The target model becomes:

> **Operational requirement → Explicitly permitted access**

The redesign introduces:

* An OT DMZ between enterprise and control environments
* Separate supervisory, engineering, and control security zones
* Explicitly allowed communication paths between zones
* Governed vendor remote access through a controlled gateway and jump host
* Read-oriented management visibility without unnecessary process-control authority
* Controlled historian replication for enterprise reporting
* Restricted reachability around legacy MS/TP gateways
* Passive and anomaly-oriented OT monitoring
* Clearer administrative ownership
* Continued local and manual plant-control capability

The intent is not to make the plant harder to operate.

The intent is to make it harder for one compromised system, user, or vendor pathway to affect systems outside its legitimate role.

---

## Expected Risk Reduction

| Legacy Exposure                  | Target-State Effect                                              |
| -------------------------------- | ---------------------------------------------------------------- |
| Broad internal OT reachability   | Segmentation reduces lateral movement and blast radius           |
| Direct enterprise-to-OT exposure | DMZ services control boundary crossings                          |
| Excess management privilege      | Visibility is preserved while command authority is removed       |
| Legacy vendor VPN                | Remote access is consolidated into a governed pathway            |
| Broad engineering reachability   | High-privilege access is limited to required destinations        |
| Enterprise demand for OT data    | Replicated services separate reporting from control access       |
| Legacy MS/TP dependencies        | Gateway containment and monitoring provide compensating controls |
| Informal responsibility          | Ownership and access authority become explicit                   |

Detailed analysis is available in the [Risk Reduction Mapping](risk%20reduction%20mapping.md).

---

## Operational Constraint

The plant still has to run.

That requirement governs every cybersecurity decision in the target state.

The redesign preserves:

* Automatic controller operation
* Required BACnet communications
* Operator HMI functionality
* Engineering and troubleshooting capability
* Vendor maintenance where necessary
* Equipment-level service access
* Local control panels
* Central physical-board operation
* Degraded/manual plant operation

Legacy field devices are not removed simply because they are old.

Where those devices cannot support modern endpoint controls, the design reduces risk around them through segmentation, restricted gateway access, passive monitoring, and other compensating controls.

This keeps cybersecurity aligned with the physical process rather than treating OT as another enterprise network.

---

## NIST Basis

The design is informed primarily by:

* **NIST SP 800-82 Rev. 3**
* **NIST Cybersecurity Framework 2.0**
* **NIST SP 800-53 Rev. 5**

NIST guidance is used to support design decisions and control traceability rather than to turn the project into a compliance checklist.

The working method is:

> **Observed Condition → Risk Finding → Guidance → Architecture Decision → Expected Risk Reduction**

Detailed mappings are available in [NIST Alignment](nist%20alignment.md).

---

## Residual Risk

The target state reduces exposure but does not eliminate risk.

High-value engineering systems remain high-value targets. Approved vendor access still carries third-party risk. Legacy field devices still have limited native security capability. Firewalls and segmentation still depend on correct configuration. Maintenance activity still creates temporary exposure.

Those risks are not hidden by the redesign.

They are made more visible, more constrained, and easier to govern.

---

## Executive Conclusion

The legacy environment does not need to be rebuilt from the ground up to achieve meaningful cybersecurity improvement.

The largest gains come from reducing unnecessary trust.

By separating enterprise and OT functions, controlling remote access, limiting privilege, isolating engineering functions, containing legacy field networks, and improving visibility, the target architecture reduces the number of paths through which a cyber event can reach physical operations.

The plant remains operationally recognizable.

The difference is that access now has to justify itself.

> **Preserve the process. Reduce unnecessary trust. Constrain access. Improve visibility. Maintain operational resilience.**
