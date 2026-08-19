# Legacy Architecture

## Purpose

This document defines the effective legacy architecture of the reference central utility plant.

The environment represents an operationally functional industrial network that developed over time around availability, maintainability, equipment compatibility, and business convenience rather than around a modern cybersecurity architecture.

The legacy state is not intentionally insecure. Many of its weaknesses result from accumulated trust relationships, inherited technology, changing business requirements, and incomplete retirement of older access methods.

---

# Architecture Overview

The plant uses a predominantly BACnet-based supervisory and control environment.

BACnet/IP provides the primary communications backbone between supervisory systems, operator workstations, engineering resources, controllers, and supporting systems.

A number of operationally important legacy devices remain connected through BACnet MS/TP networks.

The result is a hybrid architecture containing modern Ethernet/IP communications alongside legacy serial field networks that continue to support automatic plant operation.

From a cybersecurity perspective, the OT environment remains largely flat and broadly trusted.

---

# Primary OT Network

The principal OT network supports:

* SCADA/BAS server
* Operator HMI Station 1
* Operator HMI Station 2
* Permanent engineering workstation
* OT historian
* BACnet/IP controllers
* BACnet routers and supervisory controllers
* Supporting OT network infrastructure

These assets share a broadly trusted plant control environment with limited internal security separation.

Access decisions historically rely heavily on an assumption that systems already connected to the OT network are authorized to communicate with other plant systems.

---

# BACnet/IP Control Backbone

BACnet/IP is the primary protocol used for plant supervisory and controller communications.

The BACnet/IP environment supports:

* Process values
* Equipment status
* Alarms
* Operator commands
* Supervisory setpoints
* Plant sequencing
* Trend data
* Controller-to-controller information exchange

The network allows the SCADA/BAS platform and authorized workstations to interact with plant controllers and supporting systems.

Because the environment developed primarily around operational interoperability, communications between OT assets are more permissive than would be expected in a purpose-built segmented cybersecurity architecture.

---

# Legacy BACnet MS/TP Networks

Multiple BACnet MS/TP trunks remain in active service within the plant.

These serial networks primarily support legacy field-level sensing and interface devices that provide process information to the main BACnet/IP control environment.

Representative MS/TP-connected devices may include:

* Differential-pressure sensing interfaces
* RTD temperature sensing interfaces
* Legacy temperature and pressure input modules
* Flow or status interfaces
* Field I/O devices
* Other low-bandwidth process-sensing components

MS/TP communications traverse RS-485 serial networks and enter the broader BACnet/IP environment through BACnet routers, supervisory controllers, or similar gateway functions.

## Operational Dependency

The MS/TP-connected devices provide process values that are consumed by the primary plant control logic during automatic operation.

Representative inputs may include:

* Chilled-water differential pressure
* Supply-water temperature
* Return-water temperature
* Condenser-water temperature
* Pressure values
* Flow-related measurements
* Equipment status or permissive indications

These values may be used for:

* Automatic pump-speed control
* Chiller staging
* Cooling-tower operation
* Setpoint regulation
* Equipment sequencing
* Alarm generation
* Operational permissives

As a result, loss or degradation of an MS/TP segment may not immediately cause complete loss of plant operation, but it can impair automatic control by removing required process inputs.

Depending on the affected measurement and control strategy, the plant may enter a degraded operating condition, generate alarms, fall back to predetermined control behavior, or require increased manual operator intervention.

The continued operational dependence on legacy MS/TP-connected field devices therefore represents both a reliability consideration and a cybersecurity modernization constraint.

---

# Supervisory Access

Two operator workstations provide access to the HMI/SCADA environment.

Both stations can:

* Monitor plant conditions
* Review alarms
* View equipment states
* Issue authorized operator commands
* Modify permitted supervisory setpoints

The stations function as normal operational interfaces rather than as a formal primary/standby pair.

---

# Engineering Access

A permanent engineering workstation is located within the controlled-access plant control room.

It provides high-privilege access for:

* PLC programming
* BACnet controller configuration
* Control-logic troubleshooting
* Commissioning
* Diagnostics
* Configuration changes
* Recovery activities

The engineering workstation resides within the broadly trusted OT environment and can communicate with multiple controller systems.

Its legitimate capabilities also make it one of the most consequential assets if compromised or misused.

---

# Historian Placement

The OT historian resides within the plant OT network.

It receives operational information from the supervisory environment and supports:

* Trend analysis
* Troubleshooting
* Performance review
* Alarm investigation
* Historical reporting

Its location simplifies access to process information but also places a data-consumption system within the same broadly trusted environment as higher-criticality control functions.

The appropriate location and data-transfer model for historical information will be reconsidered during target-state design.

---

# Enterprise Interaction

The OT environment is connected to the enterprise environment through an existing network boundary.

The boundary provides some perimeter protection but does not create comprehensive internal separation between supervisory, engineering, historian, and controller functions.

Selected enterprise users have historically been provided access to plant information and supervisory services.

---

# Management Access

An enterprise-connected management workstation has access to the plant supervisory environment.

The legitimate business requirement is visibility into current plant conditions.

Over time, however, the associated account and client configuration accumulated permissions that also allow some supervisory control actions.

This creates a distinction between:

**Required capability:** operational visibility.

**Inherited capability:** visibility plus unnecessary process-control authority.

The access path therefore represents both an architecture issue and a privilege-governance issue.

---

# Maintenance and Local Service Access

Plant maintenance personnel use a company-issued laptop for direct connection to equipment service interfaces when required.

Typical targets may include:

* Chillers
* Equipment controllers
* VFDs
* Manufacturer-specific diagnostic interfaces

Vendor technicians may similarly connect vendor-owned laptops directly to supported machinery.

These direct service connections may be necessary for effective troubleshooting but introduce endpoints with different levels of organizational control into close proximity with critical equipment.

---

# Vendor Remote Access

Approved remote vendor support is available for selected systems when remote troubleshooting is required.

In addition to the currently recognized support mechanism, a historical vendor VPN pathway remains technically functional.

The legacy VPN was originally established for legitimate chiller-related support and remains known to a small number of long-tenured vendor personnel.

It is no longer fully represented within the current recognized remote-access model.

This creates uncertainty regarding:

* Current ownership
* Credential lifecycle
* Reachable assets
* Authentication controls
* Continuing necessity
* Documentation
* Monitoring

The legacy VPN therefore represents part of the effective architecture even if it is absent from the formal architecture.

---

# Local and Degraded Operation

The plant is not entirely dependent on SCADA/BAS availability for physical operation.

Controllers retain local process logic where appropriate, and operators have access to:

* Equipment-mounted controls
* Local control panels
* Physical selector controls
* Manufacturer interfaces
* A central/local physical control board

An experienced operator can maintain a reduced but coordinated plant operating condition if centralized supervisory control is unavailable.

The loss of SCADA/BAS therefore represents a serious reduction in visibility and supervisory capability but does not inherently equal immediate loss of the physical plant.

---

# Legacy Architecture Characteristics

The legacy environment can be summarized by the following characteristics:

* Predominantly BACnet/IP supervisory and control backbone
* Operationally important BACnet MS/TP field-sensing networks supporting automatic plant control
* Broadly trusted internal OT communications
* Limited segmentation between supervisory and control functions
* Historian located within the OT environment
* Permanent high-privilege engineering workstation
* Two full supervisory operator stations
* Enterprise-connected management supervisory access
* Company and vendor maintenance laptops
* Recognized vendor remote support
* Persistent legacy vendor VPN
* Shared IT, OT, maintenance, and vendor responsibilities
* Local/manual operating capability during supervisory-system impairment

These conditions establish the baseline for subsequent cybersecurity risk analysis.

---

# Assessment Principle

The objective of the target-state architecture will not be to eliminate legacy technology solely because it is old.

The assessment will instead determine:

* Which communications are operationally required
* Which access paths are unnecessary
* Where trust can be reduced
* Where segmentation can limit exposure
* Where legacy devices require compensating controls
* How business and maintenance functionality can be preserved safely
* How the plant can maintain availability while improving cybersecurity

The legacy architecture therefore serves as the operational baseline rather than as a deliberately weak straw-man design.
