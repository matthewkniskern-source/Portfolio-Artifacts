# Legacy Risk Findings

## Purpose

This document identifies the principal cybersecurity risk conditions present in the reference plant's legacy OT architecture.

The findings are derived from the documented operating environment, communication requirements, asset and access inventory, and effective legacy architecture.

The objective is not to characterize the legacy environment as operationally defective. The plant remains functional and includes important resilience capabilities. The findings instead identify conditions where accumulated trust, access, legacy technology, or governance practices create cybersecurity exposure beyond what is required for plant operation.

Supporting context is available in:

* [Environment Overview](environment%20overview.md)
* [Communication Requirements](communication%20requirements.md)
* [Asset and Access Inventory](asset%20access%20inventory.md)
* [Legacy Architecture](legacy%20architecture.md)

---

# Risk Summary

| ID    | Finding                                         | Primary Risk Theme              | Relative Priority |
| ----- | ----------------------------------------------- | ------------------------------- | ----------------- |
| LR-01 | Broadly Trusted OT Network                      | Segmentation / Lateral Movement | High              |
| LR-02 | Excess Management Supervisory Privilege         | Access Control / Governance     | High              |
| LR-03 | Persistent Legacy Vendor VPN                    | Third-Party / Remote Access     | High              |
| LR-04 | Broad Engineering Workstation Reachability      | Privileged Access               | High              |
| LR-05 | Mobile and Third-Party Maintenance Endpoints    | Endpoint / Maintenance Access   | Moderate-High     |
| LR-06 | Historian Located Within Broad OT Trust Zone    | Architecture / Data Access      | Moderate          |
| LR-07 | Dependency on Legacy MS/TP Process Inputs       | Legacy Technology / Resilience  | Moderate-High     |
| LR-08 | Ambiguous IT/OT/Vendor Administrative Ownership | Governance                      | Moderate-High     |

Priority ratings are qualitative and represent relative cybersecurity significance within this reference environment. They are not intended to represent a formal quantitative risk score.

---

# LR-01 — Broadly Trusted OT Network

## Condition

The primary OT environment operates as a largely flat BACnet/IP network with limited internal segmentation between supervisory systems, engineering resources, historian services, controllers, and supporting infrastructure.

Systems connected to the OT network therefore inherit a relatively broad level of network reachability.

## Why It Matters

The architecture places substantial reliance on perimeter protection.

If an authorized OT endpoint is compromised, misused, or unintentionally exposes malicious traffic, limited internal segmentation may allow the event to affect systems beyond the endpoint's legitimate operational function.

This increases potential:

* Lateral movement
* Unauthorized discovery
* Controller reachability
* Exposure of privileged systems
* Blast radius following endpoint compromise

## Evidence

The legacy topology places the following systems within the same broadly trusted OT environment:

* SCADA/BAS server
* Two operator HMI stations
* Engineering workstation
* OT historian
* BACnet/IP plant controllers
* Field-network gateways

See [Legacy Architecture](legacy%20architecture.md#primary-ot-network).

## Risk Statement

A compromise of a system already admitted to the OT network may provide access pathways to higher-criticality control assets because internal trust boundaries do not sufficiently reflect differing system functions or privilege levels.

## Target-State Direction

Introduce security zones and explicitly controlled conduits between systems with materially different functions, privileges, and risk profiles.

---

# LR-02 — Excess Management Supervisory Privilege

## Condition

An enterprise-connected management workstation is used for legitimate operational visibility but retains supervisory command capability beyond the manager's actual business requirement.

The access represents accumulated privilege rather than an intentional requirement for process control.

## Why It Matters

Management personnel may have legitimate reasons to view:

* Plant status
* Alarms
* Equipment conditions
* Performance information

Those requirements do not inherently justify command capability.

Providing unnecessary control authority from an enterprise-connected workstation creates both an access-control weakness and an IT/OT exposure path.

## Evidence

The documented communication requirement identifies management visibility as legitimate while explicitly identifying command capability as unnecessary.

See:

* [Management Supervisory Access](communication%20requirements.md#11-management-supervisory-access)
* [Management Workstation](asset%20access%20inventory.md#management-workstation)

## Risk Statement

Excess privilege allows a business-facing endpoint or user to perform actions capable of affecting physical plant operation without a corresponding operational need.

The risk includes intentional misuse, operator conflict, user error, credential compromise, and propagation of an enterprise-originating security event into the control environment.

## Target-State Direction

Preserve legitimate management visibility through an appropriately separated read-oriented service while removing unnecessary supervisory command authority.

---

# LR-03 — Persistent Legacy Vendor VPN

## Condition

A historical vendor VPN remains technically functional for selected chiller-related support.

The pathway was originally created for legitimate troubleshooting but is no longer fully represented within the current recognized remote-access model.

Access remains known to a limited number of long-tenured vendor personnel.

## Why It Matters

A remote-access path may remain technically valid even when it is no longer effectively governed.

This creates uncertainty concerning:

* Active credentials
* Authentication requirements
* Reachable assets
* Current ownership
* Logging and monitoring
* Continued business necessity
* Access review
* Retirement responsibility

## Evidence

The legacy VPN is documented as part of the effective architecture despite being incompletely represented in the formally recognized access model.

See [Legacy Vendor VPN Access](asset%20access%20inventory.md#legacy-vendor-vpn-access).

## Risk Statement

An inherited third-party pathway may provide persistent privileged access to OT resources without the same authorization, monitoring, review, and lifecycle controls applied to currently recognized remote-access mechanisms.

## Target-State Direction

Inventory and retire the legacy pathway unless a current business requirement is established. Any required vendor remote access should transition to a single governed and monitored access model.

---

# LR-04 — Broad Engineering Workstation Reachability

## Condition

The permanent engineering workstation is a trusted OT asset with high-privilege access to multiple controller systems.

Its functions include programming, configuration, diagnostics, commissioning, and recovery.

## Why It Matters

The engineering workstation is legitimately powerful.

That legitimate capability also makes it one of the most consequential systems in the OT environment if:

* Compromised
* Misconfigured
* Used with inappropriate credentials
* Exposed to malicious removable media
* Used outside an approved maintenance activity

In the flat architecture, its network reachability is broader than its routine use necessarily requires.

## Evidence

The engineering workstation is located within the broadly trusted OT network and can communicate with multiple control assets.

See:

* [Permanent Engineering Workstation](asset%20access%20inventory.md#permanent-engineering-workstation)
* [Engineering Access](legacy%20architecture.md#engineering-access)

## Risk Statement

Compromise or misuse of the engineering workstation may provide a high-privilege pathway for modification of multiple controller systems because architectural controls do not strongly constrain its reachability.

## Target-State Direction

Retain necessary engineering functionality while restricting the workstation to explicitly authorized controller and administrative pathways.

---

# LR-05 — Mobile and Third-Party Maintenance Endpoints

## Condition

Plant maintenance personnel use a company-issued laptop for direct equipment service access.

Vendor technicians may also connect vendor-owned laptops directly to manufacturer-supported service interfaces.

These endpoints have materially different security characteristics.

## Why It Matters

The company maintenance laptop can be managed under organizational policy.

Vendor-owned endpoints cannot automatically be assumed to share the same:

* Patch level
* Endpoint protection
* Software inventory
* Removable-media controls
* Credential practices
* Prior exposure history

Direct equipment access may nevertheless be operationally necessary.

## Evidence

The maintenance model explicitly includes both company-controlled and vendor-controlled mobile endpoints.

See:

* [Company Maintenance Laptop](asset%20access%20inventory.md#company-maintenance-laptop)
* [Vendor Service Laptop](asset%20access%20inventory.md#vendor-service-laptop)

## Risk Statement

Maintenance activity may introduce a mobile endpoint with uncertain security posture into direct proximity with critical industrial equipment.

The risk cannot be resolved solely by prohibiting vendor access because specialized vendor maintenance may be operationally required.

## Target-State Direction

Differentiate trust and access requirements for company and vendor devices, limit connections to approved service interfaces, and apply procedural and technical controls appropriate to temporary high-privilege maintenance activity.

---

# LR-06 — Historian Located Within Broad OT Trust Zone

## Condition

The historian resides inside the primary OT network and shares the broadly trusted environment with supervisory and control systems.

It is used for trend analysis, historical reporting, troubleshooting, and operational review.

## Why It Matters

The historian serves a fundamentally different function from process controllers.

Its purpose includes data consumption and reporting, which may attract access requirements from users or systems outside the control environment.

Keeping the historian in the same broad trust zone can create pressure to extend enterprise or business access deeper into OT than is operationally necessary.

## Evidence

The legacy architecture places the historian within the same broad BACnet/IP OT environment as SCADA/BAS, engineering, and control systems.

See [Historian Placement](legacy%20architecture.md#historian-placement).

## Risk Statement

A system intended partly for information consumption may become an unnecessary bridge between business information requirements and higher-criticality control assets when it resides within the same broad trust environment.

## Target-State Direction

Reconsider historian placement and the method by which operational data is exposed to enterprise consumers. Preserve plant data availability without requiring enterprise users to reach directly into the primary control environment.

---

# LR-07 — Dependency on Legacy MS/TP Process Inputs

## Condition

Multiple BACnet MS/TP field networks provide process values used by the main plant control logic during automatic operation.

Representative inputs include:

* Differential pressure
* Supply and return temperatures
* Condenser-water temperature
* Flow information
* Equipment status
* Permissive indications

## Why It Matters

These devices are legacy from a communications perspective but remain operationally relevant.

Their age or protocol alone does not make immediate replacement an acceptable cybersecurity strategy.

Loss or degradation of an MS/TP segment may:

* Remove required automatic-control inputs
* Generate alarms
* Impair sequencing
* Force fallback behavior
* Increase manual operator workload
* Move the plant into a degraded operating state

## Evidence

The legacy architecture explicitly identifies MS/TP field networks as supporting process inputs consumed during automatic plant operation.

See [Legacy BACnet MS/TP Networks](legacy%20architecture.md#legacy-bacnet-mstp-networks).

## Risk Statement

Operational dependence on legacy field networks constrains modernization because security improvements must account for devices that cannot necessarily support contemporary cybersecurity capabilities.

## Target-State Direction

Preserve required field functionality while reducing exposure through segmentation, gateway placement, restricted reachability, monitoring where practical, and other compensating controls.

---

# LR-08 — Ambiguous IT/OT/Vendor Administrative Ownership

## Condition

Responsibility for OT-connected infrastructure is distributed across plant operations, controls and maintenance personnel, corporate IT, and third-party vendors.

Corporate IT possesses limited OT-specific expertise, while plant and vendor personnel may retain specialized system knowledge unavailable elsewhere in the organization.

## Why It Matters

Shared responsibility is not inherently a weakness.

Risk emerges when ownership is unclear.

Ambiguity may affect:

* Account management
* Patch responsibility
* Network changes
* Remote-access approval
* Logging
* Asset inventory
* Vendor access reviews
* Incident response
* System retirement
* Configuration ownership

This may also create dependence on individual personnel rather than documented organizational processes.

## Evidence

The asset and access inventory identifies overlapping administrative roles and limited concentration of OT-specific knowledge within the enterprise IT function.

See [Enterprise IT Support](asset%20access%20inventory.md#enterprise-it-support).

## Risk Statement

Unclear responsibility for cyber-relevant OT infrastructure may allow important security tasks or access paths to fall between organizational boundaries.

## Target-State Direction

Define administrative ownership, authorization authority, technical responsibility, and vendor accountability for each major OT security domain.

---

# Cross-Cutting Observation

The legacy environment's principal cybersecurity weakness is not any single obsolete device or misconfigured system.

The larger issue is accumulated trust.

Over time, legitimate operational, maintenance, management, and vendor requirements have produced:

* Broad internal reachability
* Excess privilege
* Persistent access paths
* Mixed-trust endpoints
* Legacy protocol dependencies
* Ambiguous ownership

Each condition is individually understandable in an operating plant.

Together, they create an architecture in which compromise of a relatively limited asset or account may produce consequences outside its intended operational role.

The target-state design will therefore focus primarily on reducing unnecessary trust while preserving required plant functionality.

---

# Next Assessment Stage

The findings in this document establish the basis for the target-state architecture.

The next stage will determine which architectural and governance controls can reduce these risks without:

* Disrupting required plant communications
* Eliminating necessary maintenance capability
* Creating unacceptable availability risk
* Assuming immediate replacement of legacy devices
* Removing legitimate business visibility

The resulting design decisions will be mapped back to these findings to demonstrate explicit risk reduction.
