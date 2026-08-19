# Reference Environment Overview

## Purpose

This case study uses a fictionalized central utility plant as the reference OT environment.

The plant is intentionally vendor-neutral. It is not meant to recreate any specific facility, but it is built around realistic control, maintenance, and operating conditions that commonly exist in chilled-water and central plant environments.

The point is to keep the physical process and asset population largely constant while comparing two very different cybersecurity postures.

That gives the project a clean baseline:

> **Same plant. Same operational requirements. Different trust model.**

---

# Operational Function

The plant provides centralized chilled-water production and distribution for a multi-building facility.

Automated control systems monitor and operate:

* Chillers
* Chilled-water pumps
* Condenser-water pumps
* Cooling towers
* Variable-frequency drives
* Motor-operated valves
* Temperature instrumentation
* Pressure instrumentation
* Flow instrumentation

Operators supervise the process through HMI/SCADA functions, while plant controllers maintain the automatic process logic.

The environment is built around the assumption that the plant has to keep running even when parts of the supervisory layer are unavailable.

That matters later, because cybersecurity controls that improve isolation but make the plant harder to operate are not automatically better controls.

---

# Logical OT Assets

The reference environment includes the following logical systems.

| Asset                       | Primary Function                                                        |
| --------------------------- | ----------------------------------------------------------------------- |
| Operator HMI Station 1      | Process monitoring and supervisory control                              |
| Operator HMI Station 2      | Process monitoring and supervisory control                              |
| Engineering Workstation     | Controller programming, diagnostics, maintenance, and recovery          |
| SCADA/BAS Server            | Supervisory control, alarming, coordination, and plant data acquisition |
| OT Historian                | Operational trend and historical data storage                           |
| PLC-1                       | Chiller process control                                                 |
| PLC-2                       | Pump and chilled-water distribution control                             |
| PLC-3                       | Cooling-tower and condenser-water control                               |
| BACnet/IP Infrastructure    | Primary supervisory and control-network communications                  |
| BACnet MS/TP Field Networks | Legacy field-level sensing and interface communications                 |
| Local / Physical Controls   | Equipment-level and degraded-operation control capability               |

Supporting systems such as firewalls, jump hosts, monitoring tools, and reporting services are introduced later where the architecture actually requires them.

They are not assumed at the beginning just to make the topology look secure.

---

# Field and Process Environment

The field layer includes a mix of directly controlled equipment and legacy field devices that still matter to automatic plant operation.

Representative systems include:

* Chillers
* Pumps
* Cooling towers
* VFDs
* Control valves
* Differential-pressure inputs
* RTD temperature inputs
* Flow and status interfaces
* Legacy I/O devices
* Local equipment panels
* Central physical control board

Some of the older field devices remain on BACnet MS/TP networks.

They are not there as decorative legacy equipment.

They provide process values used by the main plant logic during automatic operation.

That means any cybersecurity redesign has to work around the reality that old does not necessarily mean optional.

---

# Enterprise Interaction

The OT environment is not completely isolated from the rest of the organization.

There are legitimate reasons for information and support to cross the IT/OT boundary, including:

* Energy reporting
* Performance analysis
* Maintenance planning
* Management visibility
* Remote vendor troubleshooting
* System backups
* Time synchronization
* Security monitoring

The problem is not that these interactions exist.

The problem is when a legitimate requirement for information or support turns into broader network access than the job actually requires.

That distinction drives much of the later risk analysis.

---

# Maintenance Model

Plant personnel use a mix of fixed and mobile maintenance tools.

A permanent engineering workstation supports high-privilege controller work from the controlled plant environment.

Company maintenance personnel may also use an organization-managed laptop for direct service-port access to chillers, VFDs, or other supported machinery.

Vendors may arrive with their own laptops and manufacturer-specific tools.

That is a realistic operating condition, not something the case study tries to wish away.

The target state therefore has to preserve specialized maintenance capability while avoiding the assumption that every maintenance endpoint deserves broad OT trust.

---

# Local and Degraded Operation

The plant retains local operating capability independent of centralized supervisory control.

Depending on the affected system, operators can use:

* Local equipment panels
* Physical selector switches
* Manufacturer interfaces
* Equipment-mounted controls
* The central physical control board

An experienced operator should be able to maintain a reduced but coordinated plant operating condition if SCADA/BAS is unavailable.

That means the case study treats **loss of supervisory visibility** and **loss of physical process control** as two different things.

They are both serious, but they are not the same failure mode.

---

# Operational Priorities

The cybersecurity design has to account for the priorities of an operating plant.

Those include:

1. **Availability**
   The plant has to remain capable of performing its core function.

2. **Reliability**
   Controls should behave predictably and consistently.

3. **Safety**
   Security changes cannot introduce unsafe process behavior.

4. **Process continuity**
   Required control communications must remain available.

5. **Maintainability**
   Operators, technicians, and vendors still need practical ways to troubleshoot and repair equipment.

6. **Recoverability**
   The plant should retain a path to degraded or manual operation when higher-level systems are unavailable.

The target architecture is judged against all of these, not just whether it blocks more traffic.

---

# Case Study Constraint

The legacy and target architectures use substantially the same operational plant and asset population.

The major variable being changed is the cybersecurity architecture around those assets.

That includes:

* Network segmentation
* Trust boundaries
* Enterprise / OT communication
* Remote access
* Engineering access
* Historian placement and data flow
* Legacy field-network containment
* Monitoring
* Administrative ownership

This keeps the comparison honest.

If the target state simply replaced every old device and rebuilt the plant from scratch, it would not be much of a legacy OT risk-reduction case study.

---

# Scope Boundary

This is a conceptual cybersecurity architecture case study.

It is not a production controls design or a complete plant engineering package.

The project does not attempt to define:

* Detailed PLC logic
* Complete BACnet configuration
* Electrical design
* Safety-system engineering
* Vendor-specific control sequences
* Production IP addressing
* Final firewall rule sets
* Complete hardware specifications

Those details matter in a real implementation, but they are outside the question being answered here.

The focus is narrower:

> **What access, trust, and architecture changes materially reduce cyber risk while keeping the plant operable?**
