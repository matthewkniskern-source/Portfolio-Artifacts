# Environment

## Organization Profile

Northstar Project Services is a mid-sized commercial construction and project services company with approximately 325 employees.

The workforce is divided across a primary office, project management, estimating, administrative functions, and field personnel who routinely work from jobsites or other remote locations. Because of that mix, mobile systems, VPN access, temporary device assignments, and remote support are normal parts of day-to-day operations.

The company maintains an internal IT department of approximately eight to ten employees. Security responsibilities are handled by two dedicated analysts, with systems, network, and help desk staff providing escalation support when needed.

The security program is reasonably established but not highly mature. Northstar has centralized logging, endpoint protection, identity controls, and SIEM capability, but some investigation and response activities still depend on manual correlation and analyst judgment.

## Identity and Access

Northstar uses an on-premises Active Directory environment synchronized with Microsoft Entra ID.

Microsoft 365 supports email, collaboration, and cloud productivity services. Multi-factor authentication is required for remote VPN access and cloud services where supported.

Normal authentication to internal domain-joined workstations relies primarily on Active Directory credentials.

Access is role based, but IT personnel have broader permissions than standard business users because of their troubleshooting and support responsibilities.

The affected account, sarnold, belongs to an IT help desk technician. The role includes legitimate use of PowerShell, command-line tools, remote support utilities, and access to multiple internal systems. Because of that, administrative activity associated with the account cannot be treated as malicious based on tool use alone.

## Endpoint Environment

Most corporate endpoints run Windows 11 Enterprise and are joined to the company domain.

Microsoft Defender for Endpoint is deployed across managed workstations and provides endpoint detection, process telemetry, and response capability.

The IT department maintains a small pool of shared loaner and troubleshooting laptops. These systems are used when employee devices are being repaired, when support staff need a temporary managed workstation, or when a clean system is required for troubleshooting or testing.

The initial source device in this incident is IT-LT-017.

IT-LT-017 is a managed Windows 11 laptop owned by the IT department. It is not permanently assigned to a single employee.

At the time of the incident, IT-LT-017 was physically located in the help desk work area and was not formally checked out to any individual employee. The laptop was powered on, connected to the internal network, and available for legitimate support use.

Because the device was shared equipment and no active custody record identified a specific user at the time of the event, asset assignment alone could not establish who was operating the system.

That fact becomes relevant later in the investigation. Legitimate access to the laptop was plausible, but the lack of individual custody reduced the value of the asset record as an attribution control.

## Network Environment

The corporate network is segmented at a basic functional level.

Typical network areas include:

* corporate user workstations
* IT and administrative systems
* server infrastructure
* wireless access
* VPN-connected users
* guest access

Internal addressing uses private RFC 1918 address space.

IT-LT-017 is connected to an internal network used by IT support systems and temporary managed devices.

Outbound internet traffic passes through the corporate firewall and is logged at a level sufficient to review source and destination addresses, destination ports, and connection timing.

TCP 443 traffic is common throughout the environment and is not considered suspicious without additional context.

## Logging and Monitoring

Northstar collects several sources of security telemetry.

Available data includes:

* Windows Security event logs
* Microsoft Defender for Endpoint telemetry
* authentication activity
* process execution data
* firewall connection logs
* VPN authentication logs
* selected Entra ID activity
* asset inventory information

Windows Security events are centrally collected and available to the SOC through the SIEM.

Important event types for this investigation include successful and failed authentication events, process creation activity, and endpoint network telemetry.

Logging is sufficient to reconstruct the major sequence of the incident, but visibility is not assumed to be complete. Some endpoint activity requires correlation between multiple sources, and shared device attribution may require additional review outside of normal asset records.

## SOC Operations

The SOC operates at a moderate level of maturity.

Analysts receive alerts through the SIEM and use endpoint, identity, Windows event, and network telemetry to validate and investigate suspicious activity.

Basic detection rules exist for behaviors such as:

* repeated authentication failures
* suspicious PowerShell execution
* unusual endpoint behavior
* potentially malicious network activity
* identity anomalies

Some detections operate independently and must be correlated manually.

The environment does not rely on full SOAR-based investigation or automatic containment for routine alerts. Analysts are expected to validate activity before taking disruptive actions such as disabling an account or isolating a workstation.

This creates a deliberate balance between detection and operational impact. A help desk technician using PowerShell from an IT-owned system is not automatically treated as malicious.

## Physical and Asset Control Context

The help desk work area is used by IT staff throughout the business day and contains shared equipment, temporary devices, and systems awaiting deployment or troubleshooting.

IT-LT-017 was physically present in this area when the suspicious activity occurred.

The incident does not initially establish how the system was accessed or who physically operated it. The SOC investigation begins with digital evidence and does not assume a physical security failure at intake.

However, the location and custody status of the laptop create a secondary review path once the incident is confirmed.

Potential follow-up areas include:

* shared device custody practices
* workstation locking requirements
* handling of powered-on but unassigned equipment
* physical access to the help desk area
* badge or access-control records
* availability of camera coverage where applicable
* whether shared IT systems should remain connected while not actively assigned

These issues are treated as post-incident control questions rather than assumptions built into the initial alert.

## Incident-Relevant Assets

| Asset                           | Function                               | Notes                                                                                           |
| ------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------- |
| IT-LT-017                       | IT loaner and troubleshooting laptop   | Initial source of suspicious activity; physically located in help desk area and not checked out |
| sarnold                         | Help desk technician account           | Valid account with legitimate administrative responsibilities                                   |
| SIEM                            | Central security monitoring            | Generates the initial authentication alert                                                      |
| Microsoft Defender for Endpoint | Endpoint monitoring and response       | Provides process and endpoint telemetry                                                         |
| Active Directory                | Internal identity service              | Source of domain authentication activity                                                        |
| Entra ID                        | Cloud identity platform                | Synchronized with on-premises identity                                                          |
| Corporate firewall              | Network security and egress monitoring | Provides outbound connection telemetry                                                          |

## Security Limitations

The environment has several realistic limitations that affect the investigation.

Shared IT equipment does not always have a clearly documented individual user at a given point in time.

Administrative tools such as PowerShell are routinely used by IT personnel and cannot be treated as suspicious solely because they execute.

Some detection rules operate independently, requiring the analyst to correlate authentication, process, endpoint, and network activity before determining whether a broader pattern exists.

The organization also has limited automated response capability. Account disablement, endpoint isolation, and broader incident escalation normally require analyst validation.

Physical access and device custody information are not automatically correlated into SOC alerts.

These limitations do not prevent investigation, but they increase the importance of context, event correlation, and evidence outside of a single monitoring platform.

## Environment Assumptions

This case assumes that the affected systems were online and reporting normally during the incident.

Security telemetry used in the case is synthetic but is designed to reflect data that could reasonably be available from a moderately mature Windows enterprise environment.

The environment is intentionally not designed as either a poorly secured organization or a highly optimized SOC. The objective is to represent a company with reasonable controls where a valid account, legitimate administrative tooling, and a shared internal device can still create an investigation that is not immediately obvious.

The physical location of IT-LT-017 is included as part of the case context, but the initial investigation does not assume whether access to the device resulted from a process failure, a physical security weakness, or legitimate presence within the help desk area.
