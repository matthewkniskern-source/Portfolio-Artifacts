# Reference Environment Overview

## Purpose

This case study uses a fictionalized central utility plant as a representative operational technology environment for comparing legacy and security-segmented network architectures.

The environment is intentionally vendor-neutral and is designed to reflect common industrial control and building automation functions without reproducing the configuration of any specific real-world facility.

The same operational process, logical assets, and functional requirements will be retained across both architectures. This allows the case study to evaluate the effect of cybersecurity architecture changes without changing the underlying industrial process.

## Operational Function

The reference environment provides centralized chilled-water production and distribution for a multi-building facility.

The plant uses automated control systems to monitor and operate:

* Chillers
* Chilled-water pumps
* Condenser-water pumps
* Cooling towers
* Variable-frequency drives
* Motor-operated valves
* Temperature instrumentation
* Pressure instrumentation
* Flow instrumentation

Operators supervise the process through HMI and SCADA functions, while programmable controllers provide automated process control.

## Logical OT Assets

The initial reference environment contains the following logical systems.

| Asset                   | Primary Function                                           |
| ----------------------- | ---------------------------------------------------------- |
| Operator HMI            | Process monitoring and operator control                    |
| Engineering Workstation | Controller configuration, maintenance, and troubleshooting |
| SCADA/BAS Server        | Supervisory control, alarming, and system coordination     |
| Historian               | Collection and retention of operational trend data         |
| PLC-1                   | Chiller process control                                    |
| PLC-2                   | Pump and distribution control                              |
| PLC-3                   | Cooling tower and condenser-water control                  |
| VFDs                    | Motor speed control for pumps and fans                     |
| Instrumentation         | Temperature, pressure, and flow measurement                |
| Controlled Valves       | Automated process-flow control                             |

Additional supporting infrastructure may be introduced later where required by the architecture, including network switches, firewalls, monitoring systems, remote-access services, or intermediary systems.

## Enterprise Interaction

The OT environment is not completely isolated from enterprise information systems.

Legitimate business and operational requirements may include:

* Access to selected historical or performance data
* Administrative support
* Vendor maintenance
* Remote troubleshooting
* System backups
* Time synchronization
* Security monitoring

The architecture must therefore support necessary IT/OT interaction while limiting unnecessary or uncontrolled connectivity.

## Operational Priorities

Cybersecurity controls within the environment must account for operational requirements that differ from those of a conventional enterprise network.

Primary considerations include:

1. **Availability** — Loss of control or visibility may disrupt plant operation.
2. **Reliability** — Control systems must continue to perform predictably.
3. **Safety** — Cybersecurity changes must not introduce unsafe process behavior.
4. **Process continuity** — Security controls should not unnecessarily interfere with legitimate industrial communications.
5. **Maintainability** — Operators, technicians, and authorized vendors must retain practical methods for maintaining the system.

## Case Study Constraint

The legacy and target-state architectures will use substantially the same operational asset population.

The primary variable being changed is the cybersecurity architecture surrounding those assets, including:

* Network segmentation
* Trust boundaries
* IT/OT communication paths
* Remote-access pathways
* Administrative access
* Monitoring
* Boundary protection

This constraint allows the case study to focus on architectural risk reduction rather than equipment replacement or process redesign.

## Scope Boundary

This environment is a conceptual cybersecurity reference architecture rather than a production engineering design.

Detailed process-control logic, vendor-specific configuration, safety-system engineering, electrical design, and complete industrial protocol implementation are outside the scope of the case study.
