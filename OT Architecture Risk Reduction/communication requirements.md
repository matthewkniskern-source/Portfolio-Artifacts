# Communication Requirements

## Purpose

This document defines what actually has to communicate for the plant to operate, be maintained, and support the business around it.

The point is to separate **real requirements** from **access that simply exists because it was convenient or inherited**.

A system needing information does not automatically mean it needs direct network access to the system that produces it. Likewise, a maintenance requirement does not automatically justify broad OT reachability.

This page is the baseline for that distinction.

---

# Core Process Communications

## PLCs and Field Devices

The controllers exchange data with VFDs, valves, instrumentation, and other connected process equipment.

This is the control loop. These communications are not optional.

Typical traffic includes:

* Start and stop commands
* Speed references
* Valve-position commands
* Equipment status
* Temperature
* Pressure
* Flow
* Fault and alarm conditions

These exchanges occur continuously or near-continuously while the plant is running.

**Privilege:** High
**Operational importance:** Critical

If this communication is disrupted, the plant may lose automated control of the affected process.

---

## SCADA/BAS Server and PLCs

The SCADA/BAS server communicates with the plant controllers for centralized monitoring and supervisory control.

That includes:

* Reading process values
* Receiving equipment status
* Receiving alarms
* Writing approved operator commands
* Adjusting supervisory setpoints
* Coordinating plant-level sequences

**Frequency:** Continuous
**Privilege:** High
**Operational importance:** High

Loss of this path is serious, but it should not automatically mean loss of the plant.

The PLCs should continue executing appropriate local logic, and operators should retain a path to local or manual control.

---

## Operator HMIs and Supervisory Control

Two operator stations provide access to the HMI/SCADA environment.

Both can:

* View plant conditions
* Review alarms
* See equipment states
* Issue authorized commands
* Change permitted setpoints
* Acknowledge alarms

These are active operating stations, not a formal primary/backup pair.

**Frequency:** Continuous during staffed operation
**Privilege:** Moderate to High
**Operational importance:** High

---

# Local and Central Manual Control

The plant must remain operable if centralized supervisory control is impaired.

Authorized operators and technicians therefore retain access to:

* Equipment-mounted controls
* Local control panels
* Physical selector switches
* Manufacturer interfaces
* The central physical control board

An experienced operator should be able to hold the plant in a reduced but coordinated operating condition without relying entirely on SCADA/BAS.

That may mean losing automation, trending, centralized visibility, or efficiency.

It should not automatically mean losing the physical process.

**Frequency:** Exceptional
**Privilege:** High
**Operational importance:** Resilience-critical

---

# Engineering and Maintenance

## Permanent Engineering Workstation

The permanent engineering workstation is used for work that can directly change controller behavior.

Typical functions include:

* PLC programming
* Controller configuration
* Diagnostics
* Commissioning
* Control-logic troubleshooting
* Authorized software or firmware maintenance
* Recovery activities

This access is intermittent, but when it is used, it is highly privileged.

**Frequency:** Maintenance-driven
**Privilege:** Very High
**Operational importance:** Conditional

The workstation needs powerful access.

It does not need unrestricted access to everything simply because it is an engineering workstation.

That distinction matters in the target state.

---

## Company Maintenance Laptop

Plant maintenance personnel use a company-issued laptop for direct equipment-level troubleshooting when the machinery supports it.

Typical examples include:

* Chiller service interfaces
* VFD diagnostics
* Fault-history review
* Parameter inspection
* Equipment-specific troubleshooting
* Authorized maintenance changes

This device is mobile and may spend part of its life outside the control environment.

**Frequency:** Maintenance-driven
**Privilege:** High
**Operational importance:** Conditional

The maintenance function is legitimate.

Broad OT trust is not part of that requirement.

---

## Vendor Service Laptop

Vendors may need to connect their own laptops directly to manufacturer service interfaces.

That may be the only practical way to diagnose or restore specialized equipment.

The plant does not manage those laptops and cannot automatically know:

* Their patch level
* Their endpoint-security posture
* What software is installed
* Where the device was connected before arriving
* Whether removable media has been used
* How credentials are being handled

This is not an argument for banning vendor laptops.

It is an argument for treating them differently from organization-managed endpoints.

**Frequency:** Exceptional / Service-driven
**Privilege:** Potentially Very High
**Operational importance:** Conditional

---

# Operational Data

## SCADA/BAS to OT Historian

The historian collects operational data from the supervisory environment.

Typical data includes:

* Equipment status
* Temperatures
* Pressures
* Flow
* Runtime
* Energy use
* Alarms
* Process states
* Trend data

**Frequency:** Continuous or Periodic
**Privilege:** Primarily data collection
**Operational importance:** Moderate

The historian belongs inside the OT environment in the legacy state because it supports day-to-day troubleshooting and operations.

Later, the architecture will separate the plant's need for a local historian from the enterprise's need to consume selected data.

---

## OT Users and Historical Data

Operators, maintenance personnel, and engineering staff need access to historical information for:

* Trend review
* Fault investigation
* Performance comparison
* Troubleshooting
* Optimization

This is mostly read-oriented access.

**Frequency:** On demand
**Privilege:** Low to Moderate
**Operational importance:** Moderate

---

# Enterprise and Management Access

## Enterprise Consumption of Plant Data

Business users may need selected plant information for:

* Energy reporting
* Cost analysis
* Maintenance planning
* Performance review
* Dashboards
* Management reporting

That is a legitimate business requirement.

Direct controller access is not.

The requirement is:

> **Give the business the information it needs without making the control network part of the business network.**

**Frequency:** Periodic / On demand
**Privilege:** Read-only wherever practical
**Operational importance:** Low

---

## Management Supervisory Access

Management has a legitimate reason to see what the plant is doing.

In the legacy environment, that requirement drifted into something broader: an enterprise-connected management workstation has access to the supervisory environment and inherited some ability to issue commands.

The manager may be able to:

* View live plant status
* Review alarms
* See equipment states
* Open supervisory screens
* Issue commands where existing permissions allow

The visibility requirement is valid.

The command authority is not.

That is privilege drift.

**Frequency:** On demand
**Privilege:** Higher than required
**Operational importance:** Low

The target state should keep the visibility and remove the unnecessary control capability.

---

# Vendor Remote Access

## Recognized Vendor Remote Support

Some vendors need remote access for specialized troubleshooting.

That can include:

* Diagnostic review
* Software support
* Controller troubleshooting
* Vendor-specific configuration work

This access is exceptional, not part of routine plant operation.

**Frequency:** Exceptional
**Privilege:** High
**Operational importance:** Low

The plant should be able to run without a remote vendor being connected.

---

## Legacy Vendor VPN

A historical vendor VPN remains technically functional for selected chiller-related support.

It was originally installed for a legitimate reason.

The issue is that the reason, ownership, and governance around the access path did not age as cleanly as the technology itself.

The pathway is still known to a small number of long-tenured vendor personnel.

That raises practical questions:

* Who owns the access today?
* Which credentials still work?
* What can the connection reach?
* Who reviews it?
* Who monitors it?
* Is it still needed?
* Does the current network documentation even show it?

This is not a current communication requirement.

It is an inherited condition that needs to be dealt with during redesign.

---

# Supporting Infrastructure

## Time Synchronization

OT systems need consistent time for:

* Alarm correlation
* Trend data
* Event investigation
* Troubleshooting
* Security monitoring

**Frequency:** Periodic
**Privilege:** Low
**Operational importance:** Low in the short term, important over time

---

## Backup and Configuration Preservation

Selected OT systems need their configurations and critical data backed up.

That may include:

* PLC programs
* SCADA/BAS configuration
* HMI configuration
* Historian configuration
* Engineering files
* Network-device configuration

**Frequency:** Scheduled and after significant changes
**Privilege:** Moderate to High
**Operational importance:** Recovery-critical

Backups do not keep the plant running minute to minute.

They become very important when something goes wrong.

---

## Cybersecurity Monitoring

The OT environment needs visibility into activity that may be abnormal, unauthorized, or simply worth investigating.

Useful sources include:

* Network traffic metadata
* Firewall events
* Authentication events
* Remote-access activity
* Administrative actions
* System logs
* Controller and gateway communications

Monitoring should be as non-disruptive as possible.

In this environment, visibility is valuable only if the monitoring itself does not create a new operational problem.

**Frequency:** Continuous where appropriate
**Privilege:** Primarily observational
**Operational importance:** Moderate

---

# Communication Summary

| Source                     | Destination                | Purpose                               | Frequency           | Privilege        | Operational Importance |
| -------------------------- | -------------------------- | ------------------------------------- | ------------------- | ---------------- | ---------------------- |
| PLCs                       | Field devices              | Process control and telemetry         | Continuous          | High             | Critical               |
| SCADA/BAS Server           | PLCs                       | Supervisory control and monitoring    | Continuous          | High             | High                   |
| Operator HMIs              | SCADA/BAS Server           | Operator control and visualization    | Continuous          | Moderate/High    | High                   |
| Operator / Technician      | Local and central controls | Manual or degraded operation          | Exceptional         | High             | Resilience-critical    |
| Engineering Workstation    | Controllers                | Programming and maintenance           | Maintenance-driven  | Very High        | Conditional            |
| Company Maintenance Laptop | Equipment service ports    | Local diagnostics and troubleshooting | Maintenance-driven  | High             | Conditional            |
| Vendor Laptop              | Equipment service ports    | Vendor diagnostics and service        | Exceptional         | Very High        | Conditional            |
| SCADA/BAS Server           | OT Historian               | Historical process data               | Continuous/Periodic | Low/Moderate     | Moderate               |
| OT Users                   | OT Historian               | Trend and fault analysis              | On demand           | Read-oriented    | Moderate               |
| Enterprise Systems         | Approved plant data source | Reporting and analytics               | Periodic            | Read-only        | Low                    |
| Management Workstation     | Supervisory environment    | Visibility / inherited control        | On demand           | Excessive        | Low                    |
| Authorized Vendor          | Recognized remote path     | Technical support                     | Exceptional         | High             | Low                    |
| Legacy Vendor              | Historical VPN             | Historical support access             | Rare / Unknown      | Potentially High | None                   |
| OT Systems                 | Time Source                | Time synchronization                  | Periodic            | Low              | Low                    |
| OT Systems                 | Backup Repository          | Configuration preservation            | Scheduled           | Moderate/High    | Recovery-critical      |
| OT Environment             | Security Monitoring        | Visibility and anomaly detection      | Continuous          | Observational    | Moderate               |

---

# What Is Actually Required

This distinction drives the rest of the case study:

**A required capability is not the same thing as the legacy path used to deliver it.**

For example:

**Requirement:** Management needs plant visibility.

**Legacy implementation:** An enterprise-connected workstation can access the supervisory environment and retains some command capability.

**Target-state question:** How do we preserve visibility without preserving unnecessary control authority?

The same logic applies to:

* Vendor support
* Engineering access
* Historian data
* Maintenance laptops
* Legacy field networks

The redesign should preserve the function and challenge the access path.

---

# Design Constraint

The target state should reduce unnecessary:

* Reachability
* Privilege
* Trust
* Bidirectional communication
* Persistent access
* Third-party exposure
* Dependence on undocumented pathways

It should not make the plant harder to operate simply for the sake of producing a cleaner security diagram.

If a control removes legitimate capability without providing a practical replacement, it is not a complete design.
