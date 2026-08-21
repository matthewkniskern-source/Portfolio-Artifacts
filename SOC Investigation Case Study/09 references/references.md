# References

## Purpose

This page identifies the primary public references used to build the synthetic SOC investigation, Windows telemetry, PowerShell workflow, ATT&CK mapping, and incident-response methodology represented in this case study.

The incident data itself is fictional.

The technical behaviors, event semantics, investigation methods, and framework mappings are based on publicly documented security resources.

---

## Microsoft Windows Security Events

### Event ID 4624 - Successful Logon

Microsoft Windows Security Auditing

Event ID 4624 records the creation of a successful logon session on the system being accessed.

The event is used in this case to represent successful authentication involving sarnold and later authentication activity during scope review.

Relevant fields include:

- account
- logon type
- source system or network address
- authentication package
- logon ID
- process information where available

Microsoft Learn  
4624(S): An account was successfully logged on

---

### Event ID 4625 - Failed Logon

Microsoft Windows Security Auditing

Event ID 4625 records a failed logon attempt.

The event is used throughout the case for:

- the initial repeated failed authentication sequence
- failed authentication against IT-WS-031
- authentication correlation and detection logic

Relevant fields include:

- account
- source address
- source workstation
- logon type
- failure reason
- status and substatus
- authentication package

Microsoft Learn  
4625(F): An account failed to log on

---

### Event ID 4688 - Process Creation

Microsoft Windows Security Auditing

Event ID 4688 records creation of a new process when process creation auditing is enabled.

The case uses Event 4688-style telemetry to represent execution of:

- powershell.exe
- whoami.exe
- hostname.exe
- ipconfig.exe
- net.exe
- nltest.exe
- cmd.exe
- ping.exe
- arp.exe

Microsoft Learn  
Advanced Audit Policy Configuration - Audit Process Creation

---

## Microsoft PowerShell

### Get-WinEvent

Get-WinEvent is used throughout the manual investigation and automation examples to query Windows event logs.

The case uses FilterHashtable queries to restrict results by:

- Security log
- Event ID
- start time
- end time

Microsoft Learn  
Get-WinEvent - Microsoft.PowerShell.Diagnostics

---

### Get-NetTCPConnection

Get-NetTCPConnection is used to review active TCP sessions and identify:

- local address
- local port
- remote address
- remote port
- connection state
- owning process

The owning process identifier is correlated with process information during endpoint triage.

Microsoft Learn  
Get-NetTCPConnection - NetTCPIP

---

### Get-FileHash

Get-FileHash is used by the evidence-export workflow to calculate SHA-256 hashes for exported case files.

The hashes provide a basic integrity record for the synthetic evidence package.

They are not presented as a replacement for formal forensic chain-of-custody procedures.

Microsoft Learn  
Get-FileHash - Microsoft.PowerShell.Utility

---

## MITRE ATT&CK

The MITRE ATT&CK Enterprise framework is used to classify observed behaviors in the case.

Only techniques directly supported by the available evidence are mapped.

### T1078.002 - Valid Accounts: Domain Accounts

Used to classify unauthorized use of the legitimate sarnold domain account.

MITRE ATT&CK  
Valid Accounts: Domain Accounts

---

### T1059.001 - Command and Scripting Interpreter: PowerShell

Used to classify PowerShell execution associated with discovery and the external HTTPS request.

MITRE ATT&CK  
Command and Scripting Interpreter: PowerShell

---

### T1033 - System Owner/User Discovery

Used to classify execution of whoami during the discovery sequence.

MITRE ATT&CK  
System Owner/User Discovery

---

### T1016 - System Network Configuration Discovery

Used to classify network configuration and neighbor discovery activity such as:

- ipconfig /all
- arp -a

MITRE ATT&CK  
System Network Configuration Discovery

---

### T1087.002 - Account Discovery: Domain Account

Used to classify:

net user sarnold /domain

MITRE ATT&CK  
Account Discovery: Domain Account

---

### T1482 - Domain Trust Discovery

Used to classify:

nltest /domain_trusts

MITRE ATT&CK  
Domain Trust Discovery

---

### T1135 - Network Share Discovery

Used to classify network resource discovery using net view.

MITRE ATT&CK  
Network Share Discovery

---

### T1018 - Remote System Discovery

Used to classify activity used to identify and validate IT-WS-031 as a reachable internal endpoint.

MITRE ATT&CK  
Remote System Discovery

---

### T1021.002 - Remote Services: SMB/Windows Admin Shares

Used to classify the attempted ADMIN$ connection to IT-WS-031.

The case maps this as attempted lateral movement because no successful secondary authentication or execution was confirmed.

MITRE ATT&CK  
Remote Services: SMB/Windows Admin Shares

---

## NIST Incident Response Guidance

### NIST SP 800-61 Rev. 3

Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile

National Institute of Standards and Technology  
Published April 2025

NIST SP 800-61 Rev. 3 is used as the primary incident-response reference for the case.

Relevant areas include:

- incident detection
- analysis
- response
- containment
- recovery
- lessons learned
- integration of incident response with broader cybersecurity risk management

The case does not attempt to reproduce the publication as a formal incident-response procedure. The guidance is used as a reference point for the response and post-incident structure.

NIST SP 800-61 Rev. 3 supersedes SP 800-61 Rev. 2.

---

## Documentation Address Space

### RFC 5737 - IPv4 Address Blocks Reserved for Documentation

The external address used in the synthetic incident is:

198.51.100.42

This address is drawn from the 198.51.100.0/24 TEST-NET-2 range reserved for documentation and example use.

The address does not represent a live malicious system.

RFC Editor  
RFC 5737 - IPv4 Address Blocks Reserved for Documentation

---

## Reference Use

These references are used to keep the synthetic case technically grounded without presenting the generated datasets as literal exports from any specific security platform.

The case intentionally distinguishes between:

- documented event behavior
- documented ATT&CK techniques
- documented PowerShell functionality
- synthetic organization and incident data
- analyst interpretation of that synthetic evidence

Where the available evidence does not support a conclusion, the case does not expand the finding simply because an additional framework technique or attack path would be plausible.
