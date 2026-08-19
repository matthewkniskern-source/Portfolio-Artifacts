# Target Architecture

## Purpose

This document defines the target-state cybersecurity architecture for the reference central utility plant.

The plant itself is not being redesigned from scratch.

The same basic process, operators, engineering functions, maintenance requirements, vendor support needs, historian functions, and legacy field networks still exist.

What changes is how trust is granted around them.

The target state addresses the risks identified in [Legacy Risk Findings](legacy%20risk%20findings.md) using the design principles documented in [NIST Alignment](nist%20alignment.md).

The goal is straightforward:

> **Reduce unnecessary reachability and privilege without making the plant harder to run.**

---

# Target-State Design Principles

The target architecture is built around a few practical rules:

* Separate enterprise and OT trust domains
* Put a controlled intermediary layer between business systems and control systems
* Separate operator, engineering, and control functions where their access requirements differ
* Allow only communication paths that have a defined operational reason
* Remove command authority where visibility is enough
* Force external remote access through one governed path
* Treat engineering systems as highly privileged without treating them as universally trusted
* Treat company and vendor maintenance devices differently
* Keep necessary legacy MS/TP devices in service, but reduce what can reach them
* Use passive monitoring where direct endpoint protection is not realistic
* Preserve local and degraded plant operation

This is not maximum isolation for its own sake.

It is controlled access based on what the plant actually needs.

---

# 1. Enterprise / OT Separation

**Addresses:** LR-01, LR-02, LR-03, LR-06

The enterprise network and OT environment are separated by a dedicated industrial security boundary.

An OT DMZ sits between them.

The normal communication model becomes:

> **Enterprise → OT DMZ → OT Supervisory Environment → Control Environment**

Enterprise systems do not communicate directly with PLCs, field-network gateways, engineering systems, or other control assets.

If a business or support function needs something from OT, that requirement is handled through an approved intermediary service.

That keeps legitimate IT/OT interaction without treating the enterprise network as an extension of the plant network.

---

# 2. OT DMZ

The OT DMZ is the controlled transition point between enterprise and plant systems.

Representative services include:

* Remote-access gateway
* Privileged jump host
* Replicated historian or reporting service
* Security monitoring and log collection
* Approved maintenance or file-transfer staging where required

The DMZ is not a trusted shortcut into OT.

Traffic between:

* Enterprise and DMZ
* DMZ and OT

is controlled separately.

Only approved source, destination, service, and direction combinations are allowed.

If a communication path cannot be tied to a real requirement, it does not get added simply because it is convenient.

---

# 3. Supervisory Zone

The SCADA/BAS server and the two operator HMI stations reside in a dedicated supervisory zone.

This zone supports:

* Operator visualization
* Alarm management
* Approved operator commands
* Supervisory setpoints
* Plant sequencing
* Operational status

The operator workstations remain fully capable of running the plant.

What they no longer do is share the same broad trust relationship as engineering and administrative systems.

Operators need control.

They do not need engineering privilege.

Keeping those functions separate reduces the number of ways a compromise can move between routine plant operation and high-privilege configuration activity.

---

# 4. Engineering / Administrative Zone

The permanent engineering workstation is moved into its own logical security zone.

Its capabilities remain intact.

It still supports:

* PLC programming
* BACnet controller configuration
* Diagnostics
* Commissioning
* Control-logic troubleshooting
* Recovery
* Authorized configuration changes

The difference is reachability.

The engineering workstation can only communicate with controller and infrastructure destinations that have an approved engineering requirement.

High privilege is necessary.

Universal access is not.

This is one of the most important changes in the target architecture because the engineering workstation remains one of the highest-impact assets in the environment.

---

# 5. Control Zone

The BACnet/IP plant controllers reside in a dedicated control zone.

This zone supports the communications required for:

* Chiller control
* Pump and distribution control
* Condenser-water control
* Cooling-tower operation
* Plant sequencing
* Equipment status
* Process values
* Operator commands
* Required controller-to-controller communication

Traffic into the control zone is restricted to systems that have a reason to be there.

Routine enterprise traffic does not enter this zone.

Remote vendor sessions do not terminate directly in this zone.

Management workstations do not reach it.

That is the point of the boundary.

---

# 6. Historian and Operational Data

The legacy historian model is split into two functions.

An OT-side historian or data collector remains available to operations and engineering for:

* Trend review
* Alarm investigation
* Troubleshooting
* Performance analysis
* Historical comparison

Selected data is then replicated outward to a reporting or historian service in the OT DMZ.

The intended flow is:

> **Control / Supervisory Environment → OT Historian → DMZ Reporting Service → Enterprise Consumers**

This solves two different problems separately.

Operations still gets a local historian.

The business still gets the information it needs.

Enterprise users no longer need to reach into the primary OT environment to get it.

The replication path is still treated as a controlled boundary crossing. Read-oriented data does not automatically mean risk-free data movement.

---

# 7. Management Visibility

Management keeps visibility into the plant.

The unnecessary control capability goes away.

The target management view can provide:

* Plant status
* Equipment states
* Selected alarms
* Performance information
* Historical data
* Trend information

It does not provide routine process-control commands.

That is a better match to the actual business requirement.

The manager can still see what the plant is doing without becoming another operator station from the enterprise network.

---

# 8. Governed Vendor Remote Access

All approved external remote access terminates in the OT DMZ.

The normal vendor path becomes:

> **Vendor → Approved Remote Access → OT DMZ → Jump Host → Explicitly Authorized OT Destination**

External users do not connect directly to the control network.

The jump host becomes the controlled transition point for remote maintenance.

Vendor access should be:

* Explicitly approved
* Limited to required systems
* Time-bounded where practical
* Authenticated through the approved mechanism
* Logged
* Monitored
* Revocable

The legacy vendor VPN identified in the current-state architecture is retired.

It does not get grandfathered into the target state just because it still works.

---

# 9. Maintenance and Vendor Service Devices

The target architecture distinguishes between:

* Company-managed maintenance laptops
* Vendor-managed service laptops

Both may still need direct equipment access.

That requirement does not disappear.

What changes is the amount of trust attached to it.

Company maintenance devices may connect to approved service interfaces where required.

Vendor devices may do the same during authorized maintenance.

Neither device automatically receives broad access to the OT network.

The connection should be limited to:

* The equipment being serviced
* The approved service interface
* The duration of the maintenance task

This keeps the troubleshooting capability without turning every service event into a new network trust path.

---

# 10. Legacy BACnet MS/TP Containment

The BACnet MS/TP field networks remain in service.

They still provide process inputs that the plant depends on during automatic operation.

Those include:

* Differential pressure
* Supply and return water temperature
* Condenser-water temperature
* Flow information
* Equipment status
* Permissive signals

The target state does not force replacement simply because the devices are old.

Instead, protection is concentrated around the BACnet/IP-to-MS/TP boundary.

Controls include:

* Dedicated gateways
* Restricted reachability to those gateways
* Explicitly allowed BACnet communication paths
* No direct enterprise access
* No direct vendor remote access
* Separation from routine administrative traffic
* Passive monitoring on the IP side of the gateway
* Process-data review where useful baselines can be established

This is the practical tradeoff.

The field devices keep doing the job they were installed to do.

The architecture around them stops giving them more exposure than they need.

---

# 11. Passive Monitoring and Anomaly Detection

Legacy field devices may not support modern endpoint security.

That does not mean the environment has to remain blind.

The target architecture adds passive monitoring around key OT communication paths.

Useful observations may include:

* New BACnet devices
* Unexpected communication relationships
* Unexpected protocol use
* Abnormal traffic volume
* Unexpected controller-to-gateway activity
* Remote-access events
* Administrative changes
* Process values that move outside expected operating patterns

The monitoring should remain non-disruptive.

That matters in OT.

The goal is to observe the control environment without creating a new reliability problem.

Process anomalies also need operational context.

A strange temperature or pressure value might be:

* A cyber event
* A failed sensor
* Instrument drift
* A calibration issue
* A maintenance condition
* A legitimate process transition

Security tooling can flag the condition.

Operators and controls personnel still have to help interpret what it means.

---

# 12. Local and Degraded Operation

The target architecture preserves the plant's ability to operate when supervisory systems are unavailable.

Controllers retain appropriate local logic.

Operators retain access to:

* Central physical control board
* Local equipment panels
* Equipment-mounted controls
* Selector switches
* Manufacturer interfaces

An experienced operator can maintain a reduced or manual plant configuration when required.

This is deliberately preserved as part of the cybersecurity design.

A more secure network that removes a proven fallback operating mode would not be an improvement.

---

# 13. Administrative Ownership

The target state also tightens the organizational side of the architecture.

Responsibility is explicitly assigned for:

* OT network ownership
* Firewall and boundary management
* Controller administration
* Engineering workstation administration
* Remote-access approval
* Vendor account lifecycle
* Maintenance-device requirements
* Monitoring and logging
* Backup and recovery
* Asset inventory
* Configuration management
* Incident coordination
* System retirement

Operations, controls, IT, cybersecurity personnel, and vendors can still share work.

The difference is that important decisions have an identifiable owner.

The environment should not depend on somebody remembering that "the one guy in IT" knows how a particular connection works.

---

# Resulting Trust Model

The legacy environment mostly operated on:

> **Inside OT = Trusted**

The target architecture replaces that with:

> **Operational requirement = Explicitly permitted access**

That is the core design change.

The plant still has:

* Operators
* Engineers
* Vendors
* Legacy devices
* Historians
* Maintenance laptops
* Business reporting
* Manual fallback capability

The difference is that those functions no longer inherit more access than their jobs require.

That is where most of the risk reduction comes from.
