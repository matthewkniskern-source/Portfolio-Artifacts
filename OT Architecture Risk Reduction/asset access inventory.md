# Asset and Access Inventory

## Purpose

This inventory identifies the main cyber-relevant assets, user groups, and access relationships in the reference central utility plant.

It is not intended to be a complete engineering asset register. Field devices are grouped where additional detail would not add much to the cybersecurity analysis.

The goal is to establish a common baseline for the legacy topology, risk findings, and target-state design.

---

# Supervisory and Control Assets

| Asset                     | Function                                                                        | Typical Users                                  | Relative Criticality |
| ------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------- |
| SCADA/BAS Server          | Central supervisory control, alarming, coordination, and plant data acquisition | Operators, engineering personnel               | High                 |
| Operator HMI Station 1    | Operator visualization and supervisory control                                  | Plant operators                                | High                 |
| Operator HMI Station 2    | Operator visualization and supervisory control                                  | Plant operators                                | High                 |
| Engineering Workstation   | PLC programming, configuration, diagnostics, and control-system maintenance     | Authorized controls/maintenance personnel      | Very High            |
| OT Historian              | Stores trends, alarms, equipment states, and performance data                   | Operators, maintenance, engineering            | Moderate             |
| PLC-1                     | Chiller process control                                                         | Control system / authorized engineering access | Critical             |
| PLC-2                     | Pump and chilled-water distribution control                                     | Control system / authorized engineering access | Critical             |
| PLC-3                     | Cooling-tower and condenser-water control                                       | Control system / authorized engineering access | Critical             |
| OT Network Infrastructure | Connectivity between supervisory and control assets                             | Authorized technical personnel                 | Critical             |

Both HMI stations are active operator workstations with access to the plant supervisory environment. They are not modeled as a formal primary/backup pair.

---

# Field and Process Assets

For this case study, field devices are grouped by function rather than listed individually.

| Asset Group                    | Examples                                                             | Primary Interface                  | Operational Importance |
| ------------------------------ | -------------------------------------------------------------------- | ---------------------------------- | ---------------------- |
| Chillers                       | Central chilled-water production equipment                           | PLC and/or manufacturer controller | Critical               |
| Pumps                          | Chilled-water and condenser-water pumps                              | PLC/VFD                            | Critical               |
| Cooling Towers                 | Tower fans and associated equipment                                  | PLC/VFD                            | Critical               |
| Variable-Frequency Drives      | Pump and fan motor control                                           | PLC / local interface              | High                   |
| Controlled Valves              | Automated process-flow control                                       | PLC                                | High                   |
| Instrumentation                | Temperature, pressure, flow, status                                  | PLC                                | High                   |
| Local Equipment Controls       | Equipment boards, local panels, selectors, manufacturer interfaces   | Operator/technician                | Resilience-critical    |
| Central Physical Control Board | Coordinated local plant control during supervisory-system impairment | Plant operator                     | Resilience-critical    |

Individual sensors, actuators, and similar devices are only broken out separately when they matter to a specific communication path or risk finding.

---

# Engineering and Maintenance Assets

## Permanent Engineering Workstation

A dedicated engineering workstation is installed in the plant control room, which is treated as a controlled-access area.

The workstation supports:

* PLC programming and configuration
* Control-logic troubleshooting
* Commissioning
* Controller diagnostics
* Authorized configuration changes
* Recovery and restoration

Physical access control helps, but this is still one of the highest-value cyber assets in the plant. If it is compromised or misused, it can directly affect controller behavior.

---

## Company Maintenance Laptop

Plant maintenance personnel use a company-issued laptop for direct service work on equipment where required.

Typical uses include:

* Manufacturer service-port access
* Equipment diagnostics
* Fault-history review
* Parameter inspection
* Troubleshooting
* Authorized maintenance changes

Unlike the fixed engineering workstation, this laptop moves between normal company use and direct interaction with industrial equipment.

That makes it a different trust problem.

---

## Vendor Service Laptop

Vendor technicians may use their own laptops to connect directly to manufacturer-supported service interfaces.

The plant does not administer those devices, so it cannot automatically assume:

* Current patch status
* Endpoint-security posture
* Software inventory
* Prior network exposure
* Removable-media history
* Credential hygiene

That does not mean vendor laptops can simply be banned. In some cases, the vendor's tools are what get the equipment diagnosed or returned to service.

The real requirement is to allow the maintenance function without treating the vendor device as broadly trusted OT infrastructure.

---

# Human Access Roles

| Role                              | Normal Access Requirement                                           | Expected Privilege                           |
| --------------------------------- | ------------------------------------------------------------------- | -------------------------------------------- |
| Plant Operator                    | HMI/SCADA operation, alarms, trends, local/manual control           | Moderate to High                             |
| Controls / Maintenance Technician | Diagnostics, engineering functions, equipment service interfaces    | High to Very High                            |
| Plant Manager                     | Plant status and performance visibility                             | Read-oriented                                |
| Enterprise Business User          | Approved operational reporting and metrics                          | Read-only                                    |
| IT Administrator                  | Supporting infrastructure where specifically authorized             | Administrative but scoped                    |
| Vendor Technician                 | Specific supported equipment or systems during approved maintenance | Temporary / scoped high privilege            |
| Senior Legacy Vendor Personnel    | Historically retained remote-support capability                     | Potentially high and insufficiently governed |

The important distinction is between **what a role needs** and **what access it may have accumulated over time**.

---

# Enterprise IT Support

Corporate IT supports selected infrastructure that overlaps with the OT environment, including servers, workstations, networking, and enterprise connectivity.

OT-specific knowledge is limited and may depend heavily on a small number of people who have enough familiarity with plant systems to work effectively across the boundary.

That creates a practical problem.

Responsibility may be spread across:

* Plant operations
* Controls and maintenance
* Corporate IT
* Vendors

Shared responsibility is not automatically a weakness. Unclear responsibility is.

If nobody is sure who owns an account, firewall rule, remote-access path, backup, or retirement decision, those things tend to persist long after the original reason for them is gone.

The target state should make those boundaries explicit.

---

# Enterprise-Side Assets

## Management Workstation

An enterprise-connected management workstation is used for plant visibility.

In the legacy environment, the installed supervisory client and accumulated permissions also allow some control actions.

That is more capability than the role requires.

**Required capability:** Plant visibility and performance awareness.

**Legacy capability:** Visibility plus unnecessary supervisory command authority.

This is both an access-control problem and a governance problem.

---

## Enterprise Reporting Users

Business and facilities personnel may need selected plant data for:

* Energy reporting
* Cost analysis
* Performance review
* Maintenance planning
* Management dashboards

They need information.

They do not need direct access to controllers or process-control functions.

---

# Third-Party and Remote Access

## Recognized Vendor Access

Approved vendors may be given remote access to specific systems when remote troubleshooting is justified.

That access is not required for routine plant operation and should be treated as an exceptional privileged path.

---

## Legacy Vendor VPN Access

A historical vendor VPN remains technically available for selected chiller-related support.

It was originally installed for legitimate troubleshooting and maintenance. The problem is that it outlived the governance around it.

A small number of long-tenured vendor personnel still know about the path and may still be able to use it.

That raises several questions:

* Who owns it now?
* Which credentials still work?
* What can it actually reach?
* Is anyone monitoring it?
* Is it still needed?
* Is it even represented accurately in current network documentation?

The VPN is part of the **effective architecture** whether or not it appears on the current approved diagram.

If there is no current business requirement for it, it should not survive into the target state.

---

# Access Classification

For this case study, access is grouped into four practical categories.

### Operational Access

Access required to run the plant.

Examples include operator HMI access and controller communication with field devices.

### Maintenance Access

Privileged access used for diagnostics, repair, commissioning, or configuration.

This is often intermittent but can be very high impact.

### Business Access

Access to plant information for reporting, management, planning, or analysis.

These users may need visibility into OT data without needing control authority.

### Legacy or Inherited Access

Access that still exists because it was once useful, convenient, or approved.

It may no longer reflect a current operational requirement.

That distinction becomes important later because the target architecture should preserve required capability without automatically preserving every old access path that came with it.

---

# Inventory Boundary

This inventory focuses on assets and access relationships that matter to the cybersecurity architecture.

It does not attempt to list:

* Every sensor or actuator
* Individual electrical components
* Complete safety circuitry
* Every enterprise workstation
* Detailed PLC I/O
* Vendor-specific controller internals
* A complete network-device inventory

More detail is only added when it changes the architecture, communication requirements, or risk analysis.
