# Target Architecture

## Purpose

This document defines the target-state cybersecurity architecture for the reference central utility plant.

The target state preserves the plant's existing operational functions while reducing the excessive trust, reachability, privilege, and unmanaged access identified in the legacy environment.

The design is informed by the findings documented in [Legacy Risk Findings](legacy%20risk%20findings.md) and by the NIST guidance summarized in [NIST Alignment](nist%20alignment.md).

The objective is not to replace every legacy device or eliminate every operational risk. The objective is to introduce defensible security boundaries and compensating controls while preserving plant availability, maintainability, and degraded operating capability.

---

# Target-State Design Principles

The target architecture applies the following principles:

* Separate enterprise and OT trust domains
* Require enterprise-to-OT communication to traverse controlled intermediary services
* Segment supervisory, engineering, and control functions according to operational need
* Permit only explicitly required communication paths between security zones
* Remove unnecessary supervisory privilege from business users
* Consolidate third-party remote access through a governed pathway
* Treat engineering functions as highly privileged
* Differentiate company-managed and vendor-managed maintenance devices
* Contain rather than unnecessarily replace operationally required legacy MS/TP devices
* Introduce passive monitoring and behavioral visibility where direct endpoint controls are impractical
* Preserve physical and local control capability during supervisory-system impairment

---

# 1. Enterprise / OT Separation

**Addresses:** LR-01, LR-02, LR-03, LR-06

The enterprise network and OT environment are separated by an industrial security boundary rather than relying on direct enterprise-to-control connectivity.

An OT demilitarized zone (DMZ) is introduced between the two environments.

The intended communication model becomes:

**Enterprise → OT DMZ → OT Supervisory Environment → Control Environment**

Direct enterprise communication with PLCs, field-network gateways, engineering systems, or other control assets is not permitted.

Services that legitimately bridge enterprise and OT functions terminate or exchange information through systems located in the DMZ.

---

# 2. OT DMZ

The OT DMZ serves as the controlled intermediary between enterprise and plant systems.

Representative services may include:

* Remote-access gateway
* Privileged jump host
* Replicated operational reporting data
* Security monitoring services
* Approved file-transfer or maintenance staging functions where required

The DMZ does not itself become a trusted extension of the OT network.

Communication between:

* Enterprise and DMZ
* DMZ and OT

is separately controlled.

Only required source, destination, service, and direction combinations are permitted.

---

# 3. Supervisory Zone

The two operator HMI stations and the SCADA/BAS supervisory functions reside within a dedicated supervisory security zone.

The supervisory zone supports:

* Operator visualization
* Alarm management
* Permitted operator commands
* Supervisory setpoints
* Plant sequencing
* Operational status

The operator HMIs remain logically separated from engineering and administrative functions.

This reduces the likelihood that compromise or misuse of a privileged engineering resource automatically exposes normal operator workstations, or vice versa.

---

# 4. Engineering / Administrative Zone

The permanent engineering workstation is separated from routine operator workstations.

Its high-privilege capabilities are preserved, including:

* PLC programming
* Controller configuration
* Diagnostics
* Commissioning
* Recovery
* Authorized control-logic modification

However, network access is no longer based on unrestricted membership within a broadly trusted OT network.

Engineering communication is limited to explicitly authorized controller and infrastructure destinations.

The design principle is:

**High privilege does not require universal reachability.**

Where an engineering function does not require a communication path, that path should not exist by default.

---

# 5. Control Zone

BACnet/IP plant controllers reside within a control-oriented security zone separated from supervisory and engineering systems by controlled network boundaries.

The control zone retains the communications necessary for:

* Plant sequencing
* Chiller control
* Pump and distribution control
* Cooling-tower and condenser-water control
* Equipment status
* Process values
* Approved operator commands

Traffic crossing into the control zone is restricted to explicitly required operational communications.

Routine enterprise traffic and general-purpose remote access do not terminate within this zone.

---

# 6. Historian and Operational Data Architecture

The target state separates the operational historian function from enterprise data consumption.

An OT-side historian or data-collection function remains available to plant operators and engineering personnel for:

* Process trending
* Alarm investigation
* Troubleshooting
* Operational analysis
* Historical comparison

Selected historical and performance data is replicated outward to a DMZ-based reporting or historian service.

The intended data path is:

**Control / Supervisory Environment → OT Historian → DMZ Reporting or Historian Service → Authorized Enterprise Consumers**

Enterprise users therefore consume approved operational information without querying the primary OT historian or entering the control environment.

Replication is restricted to defined datasets and communication paths.

The target architecture does not assume that historian replication is inherently safe merely because it is read-oriented; the replication mechanism remains a controlled cross-boundary service.

---

# 7. Management Visibility

Plant management retains legitimate visibility into current plant performance.

However, management access no longer requires an enterprise workstation to run a control-capable supervisory client directly against the OT environment.

The target capability should provide:

* Plant status
* Performance information
* Selected alarms
* Equipment states
* Historical and trend information where appropriate

Process-control commands are removed from the management role unless a separately justified operational requirement is established.

This preserves the business requirement while eliminating inherited supervisory privilege.

---

# 8. Governed Vendor Remote Access

All recognized external remote support terminates in the OT DMZ.

External users do not connect directly to the control environment.

The remote-access sequence becomes conceptually:

**Vendor → Approved Remote-Access Service → OT DMZ → Privileged Jump Host → Explicitly Authorized OT Destination**

The jump host acts as the controlled transition point for remote maintenance activity.

Access should be:

* Explicitly authorized
* Limited to approved systems
* Limited to appropriate time periods where practical
* Authenticated using the organization's approved mechanism
* Logged and monitored
* Reviewed as part of vendor-access governance

The historical vendor VPN identified in the legacy architecture is retired rather than reproduced in the target state.

---

# 9. Maintenance and Vendor Service Devices

The architecture distinguishes between:

**Company-managed maintenance devices**
and
**Externally managed vendor devices**

The company maintenance laptop may continue to connect to approved equipment service interfaces when required.

Vendor-owned laptops may also be necessary for manufacturer-specific troubleshooting.

Neither circumstance automatically grants the mobile device access to the broader OT network.

Direct local service connectivity should be constrained to the equipment and interface required for the approved maintenance task.

The target state therefore preserves specialized maintenance capability without treating temporary mobile endpoints as equivalent to permanently trusted OT workstations.

---

# 10. Legacy BACnet MS/TP Containment

The target architecture retains operationally necessary BACnet MS/TP field devices.

These devices continue providing process values required by automatic plant operation, including:

* Differential pressure
* Supply and return temperatures
* Condenser-water temperature
* Flow information
* Equipment status
* Permissive indications

Immediate replacement is not required solely because the devices use legacy serial communications.

Instead, protection is concentrated around the transition between the MS/TP field networks and the BACnet/IP control environment.

Controls include:

* Dedicated BACnet/IP-to-MS/TP gateways
* Restricted network reachability to those gateways
* Explicitly permitted BACnet communication paths
* No direct enterprise access
* No direct vendor remote access
* Separation from general supervisory and administrative traffic
* Passive network visibility on the IP side of the field-network boundary
* Process-data monitoring where meaningful baselines can be established

The MS/TP devices themselves remain operationally functional while the accessible attack surface surrounding them is reduced.

---

# 11. Process and Communications Anomaly Monitoring

Because legacy field devices may not support contemporary endpoint-security capabilities, the target architecture introduces monitoring around their communications and process behavior.

Monitoring should emphasize non-disruptive collection.

Potential observations include:

* Unexpected BACnet devices
* New communication relationships
* Unexpected protocol use
* Abnormal communication volume
* Unexpected controller-to-gateway activity
* Process values outside plausible or historically expected ranges
* Sudden changes in normally stable measurements
* Communications occurring outside expected operating conditions

Process data from SCADA/BAS and historian sources can provide additional context when evaluating suspicious behavior.

The objective is not to assume that every unusual process value represents a cyber event.

Operational conditions, instrument failure, calibration issues, maintenance activity, and legitimate process transitions must also be considered.

Cybersecurity monitoring therefore supplements rather than replaces operator and controls expertise.

---

# 12. Local and Degraded Operation

The target architecture preserves the plant's existing resilience advantage: physical operation is not entirely dependent on centralized supervisory infrastructure.

Controllers retain appropriate local automation, and operators retain access to:

* Central physical control board
* Local equipment panels
* Equipment-mounted controls
* Selector switches
* Manufacturer interfaces

An experienced operator can continue operating the plant in a reduced or manual condition if supervisory systems are unavailable.

Cybersecurity controls must not compromise this capability.

---

# 13. Administrative Ownership

Target-state governance explicitly assigns responsibility for major OT cybersecurity functions.

Responsibilities should be defined for:

* OT network ownership
* Firewall and boundary management
* Controller administration
* Engineering workstation administration
* Remote-access approval
* Vendor-account lifecycle
* Maintenance-device requirements
* Monitoring and logging
* Backup and recovery
* Asset inventory
* Configuration management
* Incident coordination

Plant operations, controls personnel, enterprise IT, cybersecurity personnel, and vendors may continue sharing responsibilities.

The improvement is that ownership and authorization are explicit rather than dependent on informal institutional knowledge.

---

# Resulting Trust Model

The legacy environment largely followed the model:

**Inside OT = broadly trusted**

The target state replaces that assumption with:

**Operational requirement = explicitly permitted access**

The same plant continues to operate, but systems no longer receive broad network reachability merely because they reside within the OT environment.

This change provides the architectural basis for reducing the risks identified in the legacy-state assessment.
