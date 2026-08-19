# Communication Requirements

## Purpose

This document defines the logical communication requirements of the reference central utility plant before evaluating how those communications should be secured.

The objective is to identify which systems must exchange information for normal operation, maintenance, troubleshooting, administration, monitoring, and business support.

These requirements are intentionally architecture-neutral. A legitimate communication requirement does not imply that the participating systems should reside on the same network or communicate directly.

Later stages of the case study will compare how these functional requirements are implemented in the legacy environment and how they can be preserved through a more defensible target-state architecture.

---

## Communication Principles

Each communication relationship should have an identifiable operational or business purpose.

The analysis considers:

* Source and destination
* Operational purpose
* Direction of communication
* Frequency or operating condition
* Relative privilege
* Availability importance
* Trust-boundary implications
* Whether the path is operationally necessary or primarily a matter of convenience

Communications that cannot be tied to a legitimate current requirement should not automatically be preserved in the target architecture.

---

# Core Process Communications

## 1. PLCs to Field Devices

**Source / Destination:** PLCs ↔ VFDs, controlled valves, instrumentation, and other connected process equipment

**Purpose:**
Provide direct automated process control and acquire the field measurements necessary for plant operation.

Typical functions include:

* Start and stop commands
* Speed references
* Valve-position commands
* Equipment status
* Temperature measurements
* Pressure measurements
* Flow measurements
* Equipment alarms and fault conditions

**Operational Frequency:** Continuous or near-continuous during plant operation.

**Privilege:** High.

**Availability Importance:** Critical.

Disruption of these communications may directly affect automated process operation.

---

## 2. SCADA/BAS Server to PLCs

**Source / Destination:** SCADA/BAS Server ↔ PLC-1, PLC-2, PLC-3

**Purpose:**
Provide centralized supervisory monitoring and authorized control of plant systems.

Expected functions include:

* Reading controller process values
* Receiving alarms and equipment status
* Writing authorized operator commands
* Adjusting supervisory setpoints
* Coordinating plant-level operating sequences

**Operational Frequency:** Continuous.

**Privilege:** High.

**Availability Importance:** High.

Loss of supervisory communication may remove centralized visibility and remote operator control but should not inherently cause immediate loss of local process control.

---

## 3. Operator HMI to Supervisory System

**Source / Destination:** Operator HMI ↔ SCADA/BAS Server

**Purpose:**
Provide the operating staff with centralized process visualization and authorized supervisory control.

Expected functions include:

* Viewing plant conditions
* Reviewing alarms
* Issuing authorized commands
* Changing permitted setpoints
* Reviewing equipment status
* Acknowledging alarms

**Operational Frequency:** Continuous during staffed operation.

**Privilege:** Moderate to high depending on operator authorization.

**Availability Importance:** High.

---

# Local and Manual Control

## 4. Local and Central Manual Control

**Source / Destination:** Authorized operator or technician → Local equipment controls and central/local physical control board

**Purpose:**  
Allow continued operation, shutdown, startup, or troubleshooting when centralized supervisory systems are unavailable or when direct local intervention is operationally necessary.

Depending on the equipment and operating condition, local control may include:

- Physical control boards
- Local control panels
- Equipment-mounted interfaces
- Local selector switches
- Manufacturer-provided control interfaces

An experienced operator may also use the central/local physical board to maintain a reduced but coordinated plant operating state when SCADA/BAS supervisory control is unavailable.

**Operational Frequency:** Exceptional or maintenance-driven.

**Privilege:** High.

**Availability Importance:** Critical as a resilience capability.

Loss of supervisory control should therefore be distinguished from total loss of process control. Manual operation may reduce automation, efficiency, and centralized visibility while still allowing essential plant functions to be maintained.

---

# Engineering and Maintenance Communications

## 5. Permanent Engineering Workstation to Controllers

**Source / Destination:** Dedicated Engineering Workstation → PLCs and supported control equipment

**Purpose:**
Support controller configuration, programming, diagnostics, commissioning, and maintenance.

Potential activities include:

* Uploading and downloading controller programs
* Reviewing controller configuration
* Troubleshooting control logic
* Changing authorized configurations
* Performing supported firmware or software maintenance

**Operational Frequency:** Intermittent and maintenance-driven.

**Privilege:** Very high.

**Availability Importance:** Low during routine plant operation but potentially high during maintenance and recovery.

Because the engineering workstation can modify controller behavior, it represents one of the highest-value and highest-privilege assets in the OT environment.

---

## 6. Company Maintenance Laptop to Equipment Service Ports

**Source / Destination:** Company-issued maintenance laptop ↔ Individual chillers or other equipped machinery

**Purpose:**
Allow plant maintenance personnel to perform diagnostics and troubleshooting using manufacturer-provided local service interfaces.

Potential activities include:

* Accessing onboard diagnostics
* Reviewing fault histories
* Reading operating parameters
* Conducting equipment-specific troubleshooting
* Making authorized maintenance changes

**Operational Frequency:** Maintenance-driven.

**Privilege:** Potentially high.

**Availability Importance:** Low during normal operation.

This communication commonly occurs through direct local connection rather than through the plant supervisory network.

The maintenance laptop therefore represents a mobile asset that may interact with both ordinary corporate resources and sensitive industrial equipment during its lifecycle.

---

## 7. Vendor Laptop to Equipment Service Ports

**Source / Destination:** Vendor-owned laptop ↔ Supported plant equipment

**Purpose:**
Allow authorized third-party personnel to perform specialized diagnostics, configuration, commissioning, or repair.

**Operational Frequency:** Exceptional and service-driven.

**Privilege:** Potentially very high.

**Availability Importance:** Low during normal operation.

Unlike company-issued maintenance laptops, vendor-owned devices are not administered under the plant organization's endpoint-management program.

The environment therefore cannot inherently assume the security posture, patch state, software inventory, or prior network exposure of the device.

This relationship will require specific consideration in the target-state architecture and supporting access procedures.

---

# Operational Data Communications

## 8. Supervisory System to OT Historian

**Source / Destination:** SCADA/BAS Server → OT Historian

**Purpose:**
Provide historical storage of operational process information.

Expected information may include:

* Equipment status
* Temperature
* Pressure
* Flow
* Runtime
* Energy consumption
* Alarm events
* Operating states
* Process trends

**Operational Frequency:** Continuous or periodic.

**Privilege:** Primarily data transfer rather than process control.

**Availability Importance:** Moderate.

The historian resides within the OT environment in the initial architecture.

Temporary historian failure should not interrupt plant operation, although extended loss may affect troubleshooting, reporting, optimization, performance analysis, and historical records.

The appropriate security-zone placement and enterprise-consumption model for historical data will be reconsidered during development of the target-state architecture.

---

## 9. OT Workstations to Historian

**Source / Destination:** Authorized OT workstations → OT Historian

**Purpose:**
Support process analysis, troubleshooting, maintenance, and operational optimization.

Expected activities include:

* Reviewing historical trends
* Comparing operating periods
* Investigating equipment faults
* Evaluating system performance
* Reviewing prior alarms and operating states

**Operational Frequency:** On demand.

**Privilege:** Primarily read-oriented.

**Availability Importance:** Moderate.

---

# Enterprise and Management Communications

## 10. Enterprise Consumption of Plant Information

**Source / Destination:** Enterprise users or applications → Approved plant information source

**Purpose:**
Allow authorized business functions to consume selected operational information for legitimate non-control purposes.

Potential uses include:

* Energy reporting
* Management dashboards
* Cost analysis
* Maintenance planning
* Performance analysis
* Operational reporting

**Operational Frequency:** Periodic or on demand.

**Privilege:** Read-only wherever practicable.

**Availability Importance:** Low to moderate.

Direct enterprise access to PLCs or other process controllers is not considered a legitimate business requirement.

---

## 11. Management Supervisory Access

**Source / Destination:** Authorized management workstation → Plant supervisory environment

**Purpose:**
Provide designated management personnel with remote visibility into current plant conditions.

In the legacy environment, this capability has grown beyond simple reporting and may provide supervisory functionality directly from an enterprise-connected workstation.

Potential functions may include:

* Viewing live plant status
* Viewing alarms
* Reviewing equipment states
* Accessing supervisory interfaces
* Issuing commands where existing permissions allow

The manager's existing control capability is not considered an operational requirement. It reflects accumulated legacy permissions that exceed the legitimate business need for plant visibility. The target-state architecture should therefore preserve appropriate supervisory visibility while removing unnecessary command authority.

**Operational Frequency:** On demand.

**Privilege:** Potentially high.

**Availability Importance:** Low from the perspective of actual plant operation.

This pathway exists primarily for management convenience rather than because plant operation depends upon it.

Because supervisory actions can affect physical plant operation, the combination of enterprise connectivity and unnecessary command capability represents a significant architecture and governance concern.

The target-state design should preserve legitimate management visibility without assuming that remote management personnel require unrestricted process-control authority.

---

# Vendor Remote Support

## 12. Recognized Vendor Remote Access

**Source / Destination:** Authorized vendor remote connection → Approved maintenance resource

**Purpose:**
Allow selected third-party specialists to provide remote support where on-site service is impractical or unnecessarily delays restoration.

Potential activities include:

* Diagnostic review
* Software support
* Specialized controller troubleshooting
* Vendor-specific configuration assistance

**Operational Frequency:** Exceptional or maintenance-driven.

**Privilege:** Potentially high.

**Availability Importance:** Normally low.

Remote vendor connectivity is not required for autonomous plant operation.

---

## 13. Legacy Vendor Remote-Access Paths

**Source / Destination:** Selected long-established vendor personnel → Legacy OT access mechanism

**Purpose:**
Historically provided remote troubleshooting or support for specific plant equipment.

**Current Condition:**
Certain legacy access methods may remain technically functional even though they are no longer part of the organization's formally recognized access model.

These pathways may be known primarily to long-tenured technical or vendor personnel and may have persisted through system upgrades, staffing changes, or incomplete documentation.

**Operational Frequency:** Rare or unknown.

**Privilege:** Potentially high.

**Availability Importance:** Not operationally required.

This condition represents a combination of:

* Technical debt
* Incomplete asset and access-path inventory
* Third-party governance risk
* Institutional knowledge dependency
* Potential unauthorized persistence

The continued existence of an undocumented or unofficial access pathway does not constitute a legitimate communication requirement.

Such pathways should be identified during current-state assessment rather than silently carried into the target architecture.

---

# Supporting Infrastructure Communications

## 14. Time Synchronization

**Source / Destination:** OT systems → Approved time source

**Purpose:**
Maintain consistent timestamps across operational systems.

Accurate time supports alarm correlation, historical trending, troubleshooting, event analysis, and security monitoring.

**Operational Frequency:** Periodic.

**Privilege:** Low.

**Availability Importance:** Low in the short term.

---

## 15. Backup and Configuration Preservation

**Source / Destination:** Selected OT systems → Approved backup repository

**Purpose:**
Preserve critical configurations and data required for restoration.

Potential content includes:

* PLC programs
* SCADA/BAS configuration
* HMI configuration
* Historian configuration
* Engineering files
* Network-device configuration

**Operational Frequency:** Scheduled and following significant configuration changes.

**Privilege:** Moderate to high.

**Availability Importance:** Low during routine operation but recovery-critical.

---

## 16. Cybersecurity Monitoring

**Source / Destination:** OT systems and network infrastructure → Security-monitoring capability

**Purpose:**
Provide visibility into abnormal, unauthorized, or security-relevant activity.

Potential information sources include:

* Network traffic metadata
* Firewall events
* Authentication activity
* System logs
* Remote-access events
* Administrative actions

**Operational Frequency:** Continuous where technically appropriate.

**Privilege:** Primarily monitoring and collection.

**Availability Importance:** Moderate.

Monitoring mechanisms should avoid introducing unacceptable interference with operational control communications.

---

# Preliminary Communication Matrix

| Source                     | Destination                    | Purpose                            | Frequency           | Privilege        | Operational Criticality |
| -------------------------- | ------------------------------ | ---------------------------------- | ------------------- | ---------------- | ----------------------- |
| PLCs                       | Field devices                  | Process control and telemetry      | Continuous          | High             | Critical                |
| SCADA/BAS Server           | PLCs                           | Supervisory control and monitoring | Continuous          | High             | High                    |
| Operator HMI               | SCADA/BAS Server               | Operator control and visualization | Continuous          | Moderate/High    | High                    |
| Operator/Technician        | Local controls                 | Local/manual process control       | Exceptional         | High             | Resilience-critical     |
| Engineering Workstation    | Controllers                    | Programming and maintenance        | Maintenance         | Very High        | Conditional             |
| Company Maintenance Laptop | Equipment service ports        | Local diagnostics                  | Maintenance         | High             | Conditional             |
| Vendor Laptop              | Equipment service ports        | Vendor diagnostics and service     | Exceptional         | High             | Conditional             |
| SCADA/BAS Server           | OT Historian                   | Historical process data            | Continuous/Periodic | Low/Moderate     | Moderate                |
| OT Workstations            | OT Historian                   | Trend analysis                     | On demand           | Read-oriented    | Moderate                |
| Enterprise Systems         | Plant information source       | Reporting and analytics            | Periodic            | Read-only        | Low                     |
| Management Workstation     | Supervisory environment        | Remote plant visibility/control    | On demand           | Potentially High | Low                     |
| Authorized Vendor          | Recognized remote-support path | Technical support                  | Exceptional         | High             | Low                     |
| Legacy Vendor              | Legacy access mechanism        | Historical remote support          | Rare/Unknown        | Potentially High | None                    |
| OT Systems                 | Time Source                    | Time synchronization               | Periodic            | Low              | Low                     |
| OT Systems                 | Backup Repository              | Configuration/data preservation    | Scheduled           | Moderate/High    | Recovery-critical       |
| OT Environment             | Security Monitoring            | Event and network visibility       | Continuous          | Read-oriented    | Moderate                |

---

# Functional vs. Architectural Requirement

A required operational capability does not automatically justify the communication path through which that capability currently occurs.

For example:

**Functional requirement:** Management requires visibility into current plant performance.

**Legacy implementation:** An enterprise-connected management workstation can directly access the supervisory control environment and may retain command privileges.

**Target-state question:** How can legitimate management visibility be preserved without maintaining unnecessary control authority or broad enterprise-to-OT reachability?

The same distinction applies to remote vendor support, maintenance access, historian data, and engineering functions.

---

# Design Constraint

The target-state architecture must preserve legitimate operational capabilities while reducing unnecessary:

* Reachability
* Privilege
* Trust
* Bidirectional communication
* Persistence
* Third-party exposure
* Dependence on undocumented access paths

Security improvements should not unnecessarily eliminate useful operational capabilities when those capabilities can instead be delivered through a safer architecture.
