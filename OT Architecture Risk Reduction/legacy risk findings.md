# Legacy Risk Findings

## Purpose

This document identifies the main cybersecurity risks in the reference plant's legacy OT architecture.

The findings come directly from the operating environment, communication requirements, asset inventory, and effective legacy topology.

The plant is not presented as broken.

It runs.

The problem is that years of legitimate operating, maintenance, vendor, and management decisions have left behind more trust and reachability than the plant actually needs.

Supporting detail is available in:

* [Environment Overview](environment%20overview.md)
* [Communication Requirements](communication%20requirements.md)
* [Asset and Access Inventory](asset%20access%20inventory.md)
* [Legacy Architecture](legacy%20architecture.md)

---

# Risk Summary

| ID        | Finding                                         | Primary Risk Theme              | Relative Priority |
| --------- | ----------------------------------------------- | ------------------------------- | ----------------- |
| **LR-01** | Broadly Trusted OT Network                      | Segmentation / Lateral Movement | High              |
| **LR-02** | Excess Management Supervisory Privilege         | Access Control / Governance     | High              |
| **LR-03** | Persistent Legacy Vendor VPN                    | Third-Party / Remote Access     | High              |
| **LR-04** | Broad Engineering Workstation Reachability      | Privileged Access               | High              |
| **LR-05** | Mobile and Third-Party Maintenance Endpoints    | Endpoint / Maintenance Access   | Moderate-High     |
| **LR-06** | Historian Located Within Broad OT Trust Zone    | Architecture / Data Access      | Moderate          |
| **LR-07** | Dependency on Legacy MS/TP Process Inputs       | Legacy Technology / Resilience  | Moderate-High     |
| **LR-08** | Ambiguous IT/OT/Vendor Administrative Ownership | Governance                      | Moderate-High     |

These ratings are qualitative. They are meant to show relative priority inside this case study, not pretend that a simple table can replace a formal site-specific risk assessment.

---

# LR-01 — Broadly Trusted OT Network

## Condition

The main OT environment is a largely flat BACnet/IP network.

Supervisory systems, engineering resources, historian services, controllers, and field-network gateways have broad internal reachability with limited segmentation between them.

Once a system is inside OT, it can generally see and reach more than its actual job requires.

## Why It Matters

This architecture puts too much faith in the perimeter.

If an endpoint inside OT is compromised, the attacker does not necessarily have to fight through another meaningful security boundary before reaching higher-value systems.

That increases the potential for:

* Lateral movement
* Unauthorized discovery
* Controller access
* Exposure of privileged systems
* A larger blast radius from a single compromised endpoint

The issue is not that every OT system talks to every other system constantly.

The issue is that the architecture allows more of that communication than the plant actually needs.

## Evidence

The legacy environment places the following systems inside the same broadly trusted OT domain:

* SCADA/BAS server
* Two operator HMI stations
* Engineering workstation
* OT historian
* BACnet/IP plant controllers
* Field-network gateways

See:

* [Legacy Architecture](legacy%20architecture.md#primary-ot-network)
* [Legacy Topology](legacy%20topo.mmd)

## Risk Statement

Compromise of a system already inside the OT network can create a path toward higher-consequence control assets because the network does not strongly separate systems by function, privilege, or operational need.

## Target-State Direction

Break the broad trust domain into security zones and allow only the communications the plant actually requires.

---

# LR-02 — Excess Management Supervisory Privilege

## Condition

An enterprise-connected management workstation is used for legitimate plant visibility but also retains some supervisory command capability.

That control authority is not part of the actual management requirement.

It is access that accumulated over time.

## Why It Matters

A manager may need to know:

* What equipment is running
* What is in alarm
* What the plant is producing
* Whether performance is within expectations

That does not mean the same account needs to start equipment, stop equipment, or change process settings.

Giving a business-facing endpoint unnecessary command authority creates avoidable exposure and increases the chance that an enterprise-side problem becomes an OT problem.

It also creates a very ordinary human-factors risk: somebody with incomplete operating context can still affect the plant.

## Evidence

The communication requirements identify management visibility as legitimate and command capability as unnecessary.

See:

* [Management Supervisory Access](communication%20requirements.md#management-supervisory-access)
* [Management Workstation](asset%20access%20inventory.md#management-workstation)

## Risk Statement

The management workstation can affect plant operation beyond what the role requires, creating unnecessary exposure to user error, credential compromise, conflicting operator actions, and enterprise-originating security events.

## Target-State Direction

Keep the visibility.

Remove the control authority.

Management should consume approved plant information without becoming another control station.

---

# LR-03 — Persistent Legacy Vendor VPN

## Condition

A historical vendor VPN remains technically functional for selected chiller-related support.

It was originally installed for legitimate troubleshooting.

The problem is that the connection outlived the governance around it.

A small number of long-tenured vendor personnel still know about the path, while its current ownership, monitoring, and necessity are less clear.

## Why It Matters

A remote-access path does not become safe just because everyone forgot about it.

An old VPN can still carry:

* Valid credentials
* Persistent reachability
* Privileged access
* Old assumptions about who is authorized
* Little or no current monitoring

The biggest concern is the gap between the network on paper and the network that actually exists.

## Evidence

The legacy VPN appears in the effective architecture but is no longer fully represented in the recognized remote-access model.

See [Legacy Vendor VPN Access](asset%20access%20inventory.md#legacy-vendor-vpn-access).

## Risk Statement

The plant retains a third-party access path that may bypass current authorization, monitoring, account review, and ownership controls.

That gives an inherited technical connection more trust than its present business justification supports.

## Target-State Direction

Retire the legacy VPN unless somebody can establish a current, documented requirement for it.

If vendor remote access is still needed, move it into the same governed path used for all other approved external support.

---

# LR-04 — Broad Engineering Workstation Reachability

## Condition

The engineering workstation has legitimate high-privilege access to multiple controller systems.

It can program, configure, diagnose, commission, and recover control assets.

In the legacy network, that power comes with broad reachability.

## Why It Matters

The engineering workstation is supposed to be powerful.

That is the job.

The risk comes from treating “needs high privilege” as if it also means “needs access to everything.”

If this system is compromised, misused, or exposed through removable media or an unsafe maintenance action, the attacker inherits a workstation that already knows how to talk to critical control assets.

## Evidence

The engineering workstation sits inside the broadly trusted OT environment and can reach multiple controller systems.

See:

* [Permanent Engineering Workstation](asset%20access%20inventory.md#permanent-engineering-workstation)
* [Engineering Access](legacy%20architecture.md#engineering-access)

## Risk Statement

A compromised engineering workstation can become a high-impact path into multiple control systems because the architecture does not sufficiently limit its reach to the systems and functions actually required.

## Target-State Direction

Keep the engineering capability.

Constrain the path.

The workstation should reach approved controller and administrative destinations, not the entire OT environment by default.

---

# LR-05 — Mobile and Third-Party Maintenance Endpoints

## Condition

Plant maintenance personnel use a company-issued laptop for direct equipment troubleshooting.

Vendors may use their own laptops for the same kind of service work.

Those two devices may perform similar maintenance tasks, but they do not carry the same level of organizational trust.

## Why It Matters

The company laptop can be managed.

The vendor laptop may not be.

The plant may have no direct control over the vendor device's:

* Patch level
* Endpoint protection
* Software inventory
* Prior network exposure
* Removable-media history
* Credential hygiene

That does not make the vendor laptop illegitimate.

Sometimes the manufacturer's software on that laptop is exactly what is needed to get a machine back online.

The real problem is allowing a temporary maintenance device to become more trusted than the maintenance task requires.

## Evidence

The asset inventory identifies both company-managed and vendor-managed mobile maintenance endpoints.

See:

* [Company Maintenance Laptop](asset%20access%20inventory.md#company-maintenance-laptop)
* [Vendor Service Laptop](asset%20access%20inventory.md#vendor-service-laptop)

## Risk Statement

A temporary maintenance endpoint with an uncertain security posture can be connected directly to critical equipment and may introduce malware, unsafe configuration changes, or an unintended path into the wider OT environment.

## Target-State Direction

Allow the maintenance function, but constrain the connection to the equipment and service interface required for the task.

Company and vendor devices should not receive the same trust simply because both can plug into the same machine.

---

# LR-06 — Historian Located Within Broad OT Trust Zone

## Condition

The historian sits inside the same broad OT trust environment as supervisory and control systems.

That works well for plant operations, but the historian also contains exactly the kind of information enterprise users want.

## Why It Matters

The historian becomes a natural point of pressure between OT and the business.

Operations need fast, reliable access to plant history.

Management, facilities, analysts, and other business users may also want:

* Energy data
* Performance trends
* Runtime information
* Alarm history
* Maintenance data

If everyone reaches the same historian directly, a legitimate reporting requirement starts pulling enterprise access deeper into the control environment.

## Evidence

The historian is located within the broad BACnet/IP OT environment alongside SCADA/BAS, engineering resources, and control systems.

See [Historian Placement](legacy%20architecture.md#historian-placement).

## Risk Statement

The historian's dual role as an OT operational resource and a source of business information can create unnecessary enterprise-to-OT exposure when both audiences depend on the same broadly trusted service.

## Target-State Direction

Keep operational history available to the plant, but give enterprise users a separate approved path to the data they actually need.

---

# LR-07 — Dependency on Legacy MS/TP Process Inputs

## Condition

The plant still depends on BACnet MS/TP field networks for process values used during automatic control.

Those values include:

* Differential pressure
* Supply and return temperatures
* Condenser-water temperature
* Flow information
* Equipment status
* Permissive signals

The technology is old.

The information is still important.

## Why It Matters

These devices cannot be treated like obsolete office hardware.

If an MS/TP segment disappears, the plant may lose process inputs required for:

* Pump control
* Chiller staging
* Cooling-tower operation
* Sequence decisions
* Alarm generation
* Equipment permissives

The result may be degraded automatic control rather than an immediate hard shutdown, but that still matters operationally.

This creates a modernization constraint.

The security design has to protect devices that may have little or no native cybersecurity capability without breaking the logic that depends on them.

## Evidence

The legacy architecture identifies the MS/TP field networks as active process-input sources for automatic plant operation.

See [Legacy BACnet MS/TP Networks](legacy%20architecture.md#legacy-bacnet-mstp-networks).

## Risk Statement

The plant depends on legacy field communications that cannot easily support modern endpoint security controls, which limits direct remediation options and increases reliance on architecture-level protections.

## Target-State Direction

Do not force a replacement project into a segmentation project.

Contain the gateways, restrict reachability, block unrelated access, monitor where practical, and use compensating controls until replacement makes operational and financial sense.

---

# LR-08 — Ambiguous IT/OT/Vendor Administrative Ownership

## Condition

Responsibility for the environment is spread across plant operations, controls personnel, corporate IT, and vendors.

Some systems are clearly plant-owned.

Some are clearly IT-owned.

Others sit directly in the middle.

OT knowledge inside the IT organization may also depend heavily on one or two people who happen to understand the plant.

## Why It Matters

Shared responsibility is normal.

Unclear responsibility is where things get ugly.

If nobody has clear ownership, questions such as these become harder than they should be:

* Who disables an old vendor account?
* Who owns the firewall rule?
* Who approves remote access?
* Who patches the server?
* Who verifies the backup?
* Who inventories the gateway?
* Who removes equipment from the network when it is retired?
* Who responds when OT and IT both think the other group owns the problem?

That is how temporary access becomes permanent and undocumented systems become institutional knowledge.

## Evidence

The asset inventory identifies overlapping responsibility across operations, controls, IT, and third parties.

See [Enterprise IT Support](asset%20access%20inventory.md#enterprise-it-support).

## Risk Statement

Unclear ownership can leave important security tasks, accounts, access paths, and lifecycle decisions sitting between organizational boundaries with nobody clearly responsible for closing the loop.

## Target-State Direction

Assign ownership.

Not every task has to belong to one department, but every important decision should have somebody accountable for it.

---

# Cross-Cutting Observation

The biggest weakness in the legacy environment is not any one device.

It is the amount of trust that accumulated around a plant that still had to run while technology, vendors, personnel, and business requirements changed around it.

The result is:

* Broad reachability
* Excess privilege
* Persistent remote access
* Mixed-trust maintenance devices
* Legacy technology dependencies
* Unclear ownership

Most of those conditions probably made sense at some point.

That does not mean they still make sense now.

The target architecture focuses on taking away the trust the plant no longer needs while preserving the functions it still does.

---

# Next Step

The findings on this page drive the target-state design.

The next question is not:

> **How do we make the network look more secure?**

It is:

> **Which architecture and governance changes reduce these risks without breaking the plant?**

That means the target state still has to preserve:

* Required control communications
* Operator access
* Engineering capability
* Vendor maintenance where necessary
* Historical data
* Legacy field-device inputs
* Local and degraded plant operation

The redesign only counts as an improvement if both sides of that equation work.
