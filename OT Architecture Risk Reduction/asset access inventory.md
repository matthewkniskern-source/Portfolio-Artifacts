# Asset and Access Inventory

## Purpose

This inventory defines the principal cyber-relevant assets, user groups, and access relationships within the reference central utility plant.

It is not intended to represent a complete engineering asset register. Field instruments and individual equipment components are grouped where additional detail would not materially improve the cybersecurity analysis.

The inventory provides a common baseline for development of the legacy-state topology, risk assessment, and target-state architecture.

---

# Supervisory and Control Assets

| Asset                     | Function                                                                        | Typical Users                                  | Relative Criticality |
| ------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------- |
| SCADA/BAS Server          | Central supervisory control, alarming, coordination, and plant data acquisition | Operators, engineering personnel               | High                 |
| Operator HMI Station 1    | Operator visualization and supervisory control interface                        | Plant operators                                | High                 |
| Operator HMI Station 2    | Operator visualization and supervisory control interface                        | Plant operators                                | High                 |
| Engineering Workstation   | PLC programming, configuration, diagnostics, and control-system maintenance     | Authorized controls/maintenance personnel      | Very High            |
| OT Historian              | Storage of operational trends, alarms, equipment states, and performance data   | Operators, maintenance, engineering            | Moderate             |
| PLC-1                     | Chiller process control                                                         | Control system / authorized engineering access | Critical             |
| PLC-2                     | Pump and chilled-water distribution control                                     | Control system / authorized engineering access | Critical             |
| PLC-3                     | Cooling-tower and condenser-water control                                       | Control system / authorized engineering access | Critical             |
| OT Network Infrastructure | Connectivity between supervisory and control assets                             | Authorized technical personnel                 | Critical             |

Both operator HMI stations are capable of accessing the plant supervisory control environment. They are treated as active operator workstations rather than as a formal primary/backup pair.

---

# Field and Process Assets

For cybersecurity architecture purposes, individual field devices are grouped according to their operational function.

| Asset Group                    | Examples                                                             | Primary Interface                  | Operational Importance |
| ------------------------------ | -------------------------------------------------------------------- | ---------------------------------- | ---------------------- |
| Chillers                       | Central chilled-water production equipment                           | PLC and/or manufacturer controller | Critical               |
| Pumps                          | Chilled-water and condenser-water pumps                              | PLC/VFD                            | Critical               |
| Cooling Towers                 | Tower fans and associated equipment                                  | PLC/VFD                            | Critical               |
| Variable-Frequency Drives      | Pump and fan motor control                                           | PLC / local interface              | High                   |
| Controlled Valves              | Automated water-flow control                                         | PLC                                | High                   |
| Instrumentation                | Temperature, pressure, flow, status                                  | PLC                                | High                   |
| Local Equipment Controls       | Equipment boards, local panels, selectors, manufacturer interfaces   | Operator/technician                | Resilience-critical    |
| Central Physical Control Board | Coordinated local plant control during supervisory-system impairment | Plant operator                     | Resilience-critical    |

Individual sensors, actuators, and similar field components are not modeled as separate network assets unless their connectivity becomes relevant to a specific cybersecurity finding.

---

# Engineering and Maintenance Assets

## Permanent Engineering Workstation

A dedicated engineering workstation is permanently installed within the plant control room.

The control room is a controlled-access operational area, limiting casual physical access to high-privilege control-system assets.

The engineering workstation supports:

* PLC programming and configuration
* Control-logic troubleshooting
* Commissioning support
* Controller diagnostics
* Authorized configuration changes
* Recovery and restoration activities

Although physical placement provides an additional layer of protection, the workstation remains one of the most privileged cyber assets in the OT environment because compromise or misuse may directly affect controller behavior.

---

## Company Maintenance Laptop

A company-issued mobile maintenance workstation is available to authorized plant technical personnel.

The laptop may be used for:

* Direct connection to manufacturer service ports
* Equipment diagnostics
* Fault-history review
* Parameter inspection
* Troubleshooting
* Authorized maintenance changes

The device may interact with both ordinary organizational resources and industrial equipment during its lifecycle.

Because it is mobile, its security characteristics differ from those of the permanently installed engineering workstation.

---

## Vendor Service Laptop

Third-party technicians may use vendor-owned laptops to connect directly to manufacturer-supported service interfaces on plant equipment.

These systems are not administered by the plant organization.

The organization therefore cannot automatically assume:

* Current patch status
* Endpoint-security configuration
* Software inventory
* Prior network exposure
* Removable-media history
* Credential hygiene

Direct vendor service access may nevertheless be operationally necessary for specialized troubleshooting and repair.

The cybersecurity problem is therefore not solved simply by prohibiting vendor equipment. Appropriate controls must account for a legitimate maintenance requirement involving an endpoint outside organizational administration.

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

The required privilege of a role is distinguished from privilege that may have accumulated in the legacy environment.

---

# Enterprise IT Support

Corporate IT provides limited support for selected infrastructure that intersects with the OT environment, including server, workstation, network, and enterprise-connectivity functions.

OT-specific knowledge within the IT organization is limited and may depend heavily on a small number of personnel with prior familiarity with industrial control systems.

As a result, responsibility for OT-connected infrastructure may be shared across:

* Plant operations
* Controls and maintenance personnel
* Corporate IT
* Vendors

This creates a potential governance risk when technical ownership, cybersecurity responsibility, and operational authority are not clearly aligned.

The target-state architecture should therefore define administrative boundaries and ownership rather than assuming that either IT or plant personnel have complete responsibility for all OT-connected systems.

---

# Enterprise-Side Assets

## Management Workstation

An enterprise-connected management workstation is used by plant management for operational visibility.

In the legacy environment, the installed supervisory client and accumulated account permissions allow the manager to perform some control actions in addition to viewing plant conditions.

This capability exceeds the legitimate management requirement.

**Required capability:** Plant visibility and performance awareness.

**Legacy capability:** Visibility plus unnecessary supervisory command authority.

This distinction will be evaluated as both an access-control and governance issue.

---

## Enterprise Reporting Users

Business and facilities personnel may require selected plant information for:

* Energy reporting
* Cost analysis
* Performance review
* Maintenance planning
* Management dashboards

These users require plant information but do not require direct access to controllers or process-control functions.

---

# Third-Party and Remote Access

## Recognized Vendor Access

Approved vendors may be provided remote support capability for specific systems when remote troubleshooting is justified.

Remote access is not necessary for routine autonomous plant operation and should therefore be treated as an exceptional privileged pathway.

---

## Legacy Vendor VPN Access

A historical vendor VPN pathway remains technically available for remote support of selected chiller-related systems.

The connection was originally established to support legitimate vendor troubleshooting and maintenance but has persisted beyond the period in which it was actively governed as part of the current remote-access model.

Access remains known to a small number of long-tenured vendor personnel.

The pathway may therefore represent:

* Persistent third-party access
* Incomplete credential and access review
* Unclear current ownership
* Incomplete network documentation
* Dependence on institutional knowledge
* Potential inconsistency between approved and effective remote-access architecture

The existence of this VPN path does not establish a continuing business requirement.

Its purpose, ownership, authentication method, reachable assets, and continuing necessity should be reassessed during the legacy-state review.

---

# Access Classification

For this case study, access relationships are classified into four broad categories.

### Operational Access

Access necessary for normal plant operation, such as operator use of the HMI and controller communication with field devices.

### Maintenance Access

Privileged access required intermittently for diagnostics, configuration, repair, or commissioning.

### Business Access

Access to operational information needed for reporting, management, planning, or analysis without a legitimate need to control the physical process.

### Legacy or Inherited Access

Connectivity or permissions that remain available because of historical implementation, convenience, privilege accumulation, or incomplete retirement rather than a current operational requirement.

This classification will be used during the legacy-state assessment to distinguish necessary functionality from avoidable exposure.

---

# Inventory Boundary

This inventory intentionally emphasizes assets and access relationships that materially affect cybersecurity architecture.

It does not attempt to enumerate:

* Every field sensor or actuator
* Individual electrical components
* Complete safety circuitry
* Every workstation in the enterprise environment
* Detailed PLC I/O
* Vendor-specific controller internals
* Complete network-device inventories

Additional assets will be introduced only when they are necessary to explain an architecture decision, communication requirement, or risk condition.
