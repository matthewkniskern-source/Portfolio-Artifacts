# Environment

## Organization Profile

Northstar Project Services is a mid-sized commercial construction and project services company with approximately 325 employees.

The workforce is split between a primary office, project management staff, estimators, administrative users, and employees who routinely work from jobsites or other remote locations. Because of that mix, remote access, mobile workstations, VPN use, and temporary equipment assignments are normal parts of the environment.

The company maintains an internal IT team of approximately eight to ten employees. Security responsibilities are handled by two dedicated analysts with support from systems, network, and help desk personnel when incidents require escalation.

The security program is reasonably established but not highly mature. The organization has centralized logging, endpoint protection, identity controls, and a SIEM, but some investigation and response activities still depend on manual analyst correlation.

## Identity and Access

Northstar uses an on-premises Active Directory environment synchronized with Microsoft Entra ID.

Microsoft 365 is used for email, collaboration, and cloud productivity services.

Multi-factor authentication is required for remote VPN access and cloud services where supported. Normal authentication to internal domain-joined workstations still relies primarily on Active Directory credentials.

Access is role based, but IT personnel have broader permissions than normal business users due to troubleshooting and support responsibilities.

The affected user, sarnold, is a help desk technician with legitimate access to common administrative utilities, remote support tools, PowerShell, and multiple internal systems.

This makes some of the activity involved in the incident difficult to classify based on process execution alone.

## Endpoint Environment

Most corporate endpoints run Windows 11 Enterprise and are joined to the company domain.

Microsoft Defender for Endpoint is deployed across managed workstations and provides endpoint detection, process telemetry, and response capability.

The IT department also maintains a small pool of shared loaner and troubleshooting laptops. These systems may be used when an employee workstation is being repaired, when IT needs a temporary test system, or when support personnel need a clean managed device.

The initial source device in this incident is:

IT-LT-017

IT-LT-017 is a managed Windows 11 laptop owned by the IT department. It is not permanently assigned to a single user.

The system has Defender for Endpoint installed and forwards security telemetry, but its shared use makes normal user attribution less straightforward than on a permanently assigned workstation.

## Network Environment

The corporate network is segmented at a basic functional level.

Typical network areas include:

* corporate user workstations
* IT and administrative systems
* server infrastructure
* wireless access
* VPN-connected users
* limited guest access

Internal addressing uses private RFC 1918 address space.

IT-LT-017 is connected to an internal network used by IT support systems and temporary managed devices.

Outbound internet traffic is filtered through the company firewall and is logged at a level sufficient to review source and destination addresses, ports, and connection timing.

TCP 443 traffic is common throughout the environment and is not treated as suspicious without additional context.

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

Important event types for this investigation include successful and failed authentication events as well as process creation activity.

Logging is sufficient to reconstruct the major sequence of the incident, but coverage is not assumed to be perfect. Some endpoint activity requires correlation between multiple sources, and asset ownership information for shared devices may require manual verification.

## SOC Operations

The SOC operates with moderate maturity.

Analysts receive alerts through the SIEM and use endpoint, identity, network, and Windows event telemetry to validate and investigate suspicious activity.

Basic detection rules are in place for behaviors such as:

* repeated authentication failures
* suspicious PowerShell execution
* unusual endpoint behavior
* potentially malicious network activity
* identity anomalies

Some alerts generate independently and must be correlated manually.

The environment does not currently rely on full SOAR-based investigation or automatic containment for routine alerts. Analysts are expected to validate activity before taking disruptive actions such as isolating a workstation or disabling an account.

This creates a deliberate balance between detection and operational impact. A help desk technician using PowerShell from an IT-owned laptop is not automatically treated as malicious.

## Incident-Relevant Assets

| Asset                           | Function                               | Notes                                                 |
| ------------------------------- | -------------------------------------- | ----------------------------------------------------- |
| IT-LT-017                       | IT loaner and troubleshooting laptop   | Initial source of suspicious activity                 |
| sarnold                         | Help desk technician account           | Valid account with legitimate administrative activity |
| SIEM                            | Central security monitoring            | Generates initial authentication alert                |
| Microsoft Defender for Endpoint | Endpoint monitoring and response       | Provides process and endpoint telemetry               |
| Active Directory                | Internal identity service              | Source of domain authentication activity              |
| Entra ID                        | Cloud identity platform                | Synchronized with on-premises identity                |
| Corporate firewall              | Network security and egress monitoring | Provides outbound connection telemetry                |

## Security Limitations

The environment has several realistic limitations that become relevant during the investigation.

Shared IT equipment does not always have a single clearly documented user at a given point in time.

Administrative tools such as PowerShell are commonly used by IT personnel and cannot be treated as suspicious solely because they execute.

Some detection rules operate independently, requiring the analyst to correlate authentication, process, endpoint, and network activity before determining whether a larger pattern exists.

The organization also has limited automated response capability. Account disablement, endpoint isolation, and broader incident escalation normally require analyst validation.

These limitations do not prevent investigation, but they increase the importance of context and event correlation.

## Environment Assumptions

This case assumes that the affected systems were online and reporting normally during the incident.

Security telemetry used in the case is synthetic but is designed to reflect data that could reasonably be available from a moderately mature Windows enterprise environment.

The environment is intentionally not designed as either a poorly secured organization or a highly optimized SOC. The objective is to represent a company with reasonable security controls where a valid account and legitimate administrative tooling can still create an investigation that is not immediately obvious.

