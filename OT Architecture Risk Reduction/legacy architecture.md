# Legacy Architecture

## Purpose

This document describes the effective legacy architecture of the reference central utility plant.

The plant works. That matters.

The legacy environment is not presented as a deliberately weak network or a collection of obviously bad decisions. It developed over time around uptime, maintainability, vendor support, equipment compatibility, and day-to-day convenience.

The cybersecurity problem is what accumulated around those requirements.

---

# Architecture Overview

The plant uses a predominantly BACnet-based control environment.

BACnet/IP provides the main supervisory and control backbone between operator workstations, the SCADA/BAS server, engineering resources, controllers, and supporting systems.

Several operationally important field devices remain on BACnet MS/TP networks.

That gives the plant a hybrid architecture:

* Modern IP-based supervisory communications
* Legacy serial field networks
* High-privilege engineering access
* Local maintenance connections
* Business-facing access requirements
* Remote vendor support

From an operating standpoint, this is workable.

From a cybersecurity standpoint, too much of it lives inside one broad trust model.

---

# Primary OT Network

The main OT network includes:

* SCADA/BAS server
* Operator HMI Station 1
* Operator HMI Station 2
* Permanent engineering workstation
* OT historian
* BACnet/IP plant controllers
* BACnet routers and supervisory controllers
* Supporting OT switching and network infrastructure

These systems have different jobs and different privilege levels, but the legacy architecture does not strongly separate them.

Once a system is inside the OT environment, it can generally reach more of the plant than its specific function requires.

That is the core architectural weakness.

---

# BACnet/IP Control Backbone

BACnet/IP carries most of the plant's supervisory and control traffic.

That includes:

* Process values
* Equipment status
* Alarms
* Operator commands
* Supervisory setpoints
* Plant sequencing
* Trend data
* Controller-to-controller information

The network was built for interoperability and operations first.

That is not inherently wrong.

The problem is that the same openness that makes systems easy to integrate also creates broader reachability than a modern OT security design would normally accept.

---

# Legacy BACnet MS/TP Networks

Multiple BACnet MS/TP trunks remain in active service.

These networks are used primarily for field-level sensing and interface devices that feed information into the main BACnet/IP control environment.

Representative devices include:

* Differential-pressure interfaces
* RTD temperature inputs
* Legacy pressure and temperature modules
* Flow and status interfaces
* Field I/O
* Other low-bandwidth sensing components

The MS/TP networks use RS-485 serial communications and connect into the BACnet/IP environment through BACnet routers or supervisory controllers.

The devices are old.

They are also still useful.

That distinction is important.

---

## Operational Dependency

The MS/TP devices provide process values used by the plant's automatic control logic.

Examples include:

* Chilled-water differential pressure
* Supply-water temperature
* Return-water temperature
* Condenser-water temperature
* Flow information
* Equipment status
* Permissive signals

Those values may drive:

* Pump-speed control
* Chiller staging
* Cooling-tower operation
* Setpoint regulation
* Equipment sequencing
* Alarm generation

If an MS/TP trunk fails, the plant may not immediately stop.

It may instead lose automatic inputs, fall back to defaults, generate alarms, or force the operator to take more direct control.

That is a more realistic failure mode and a more useful cybersecurity constraint.

The serial devices cannot simply be removed from the design because they do not support modern security features.

---

# Supervisory Access

Two operator workstations provide normal HMI/SCADA access.

Both can:

* Monitor plant conditions
* Review alarms
* View equipment states
* Issue authorized commands
* Adjust permitted supervisory setpoints

They are active operating stations, not a formal primary/standby pair.

Their job is to run the plant.

They do not need to share the same trust assumptions as engineering systems simply because they sit in the same control room.

---

# Engineering Access

The permanent engineering workstation is located in the controlled-access plant control room.

It supports:

* PLC programming
* BACnet controller configuration
* Control-logic troubleshooting
* Commissioning
* Diagnostics
* Configuration changes
* Recovery activities

This is one of the most powerful systems in the environment.

That is necessary.

What is not necessary is giving that power broader network reachability than the engineering function requires.

In the legacy design, those two things are largely bundled together.

---

# Historian Placement

The OT historian resides inside the plant network.

It supports:

* Trend analysis
* Troubleshooting
* Performance review
* Alarm investigation
* Historical reporting

That makes sense from an operations standpoint.

The problem appears when enterprise users also want that data.

Instead of treating historian access as a separate information-sharing requirement, the legacy architecture makes it easier to extend access deeper into OT.

The target state will separate those two needs.

---

# Enterprise Interaction

The OT environment has a connection to the enterprise network through an existing perimeter boundary.

That boundary provides some protection, but it does not solve the internal trust problem.

Once traffic is allowed into OT, there is limited separation between supervisory, engineering, historian, and controller functions.

Selected enterprise users have also been given access to plant services over time.

Again, the individual reasons are understandable.

The accumulated result is the problem.

---

# Management Access

An enterprise-connected management workstation can access the plant supervisory environment.

The legitimate requirement is straightforward:

Management wants to know what the plant is doing.

Over time, the associated account and client configuration accumulated enough privilege to issue some supervisory commands.

That is not a management requirement.

It is privilege drift.

The distinction is:

**Required:** visibility.

**Inherited:** visibility plus unnecessary control authority.

That becomes both a network-security issue and a governance issue.

---

# Maintenance and Local Service Access

Plant maintenance personnel use a company-issued laptop for direct connection to supported equipment when needed.

That may include:

* Chillers
* VFDs
* Equipment controllers
* Manufacturer diagnostic interfaces

Vendors may arrive with their own laptops and use the same type of local service connection.

Those connections are sometimes the fastest or only practical way to troubleshoot specialized machinery.

The problem is not the existence of the service port.

The problem is what level of trust is granted to the device using it.

A company-managed laptop and a vendor-owned laptop should not automatically be treated the same way.

---

# Vendor Remote Access

Approved remote vendor support exists for selected systems.

That is useful when a specialist can diagnose a problem without waiting for someone to travel to the site.

The legacy environment also contains an older vendor VPN used for chiller-related support.

It was originally installed for a valid reason and still works.

What is less clear is:

* Who owns it now
* Which accounts remain valid
* What it can reach
* Whether it is monitored
* Whether it is still necessary
* Whether current documentation accurately shows it

A small number of long-tenured vendor personnel still know about the path.

That makes it part of the real network whether or not it appears on the official drawing.

---

# Local and Degraded Operation

The plant is not completely dependent on SCADA/BAS for physical control.

Controllers retain local logic, and operators can use:

* Equipment-mounted controls
* Local control panels
* Physical selector controls
* Manufacturer interfaces
* The central physical control board

An experienced operator can keep the plant in a reduced but coordinated operating condition if centralized supervisory control is unavailable.

That may be uglier, slower, and more labor-intensive than normal operation.

It is still operation.

The distinction matters because cybersecurity controls should not accidentally remove the plant's ability to function when the network does not.

---

# Legacy Architecture Characteristics

The legacy environment can be summarized as:

* Predominantly BACnet/IP supervisory and control communications
* Operationally important BACnet MS/TP field networks
* Broad internal OT trust
* Limited separation between supervisory and control functions
* Historian inside the OT trust zone
* Permanent high-privilege engineering access
* Two active operator HMI stations
* Enterprise-connected management access
* Company and vendor maintenance laptops
* Recognized vendor remote support
* A persistent legacy vendor VPN
* Shared responsibility across IT, OT, maintenance, and vendors
* Local/manual plant operation during supervisory impairment

None of those points by itself defines the problem.

The risk comes from how they interact.

---

# Assessment Principle

The target state is not going to solve the legacy architecture by deleting everything old.

The real questions are:

* Which communications are actually required?
* Which access paths are still justified?
* Where can trust be reduced?
* Where does segmentation buy real risk reduction?
* Which legacy devices need compensating controls instead of replacement?
* How do we keep maintenance practical?
* How do we preserve plant availability while tightening access?

That is the standard the target architecture has to meet.

The legacy environment is the operating baseline, not a straw man.
