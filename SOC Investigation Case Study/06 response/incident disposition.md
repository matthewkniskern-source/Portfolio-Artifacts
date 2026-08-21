# Incident Disposition

## Purpose

This document records the formal disposition of the incident involving the sarnold account and IT-LT-017.

The investigation began as a medium-severity authentication anomaly. Based on correlated authentication, process, endpoint, and network evidence, the activity is now classified as a confirmed security incident.

The purpose of this disposition is to establish what is known, what is not known, why escalation is justified, and what response actions are required.

---

## Final Disposition

| Field | Disposition |
|---|---|
| Incident ID | SOC-2026-0817-0042 |
| Alert Disposition | True Positive |
| Final Severity | High |
| Confidence | High |
| Primary Account | sarnold |
| Primary Asset | IT-LT-017 |
| Secondary Target | IT-WS-031 |
| Confirmed Secondary Compromise | No |
| Attempted Lateral Movement | Yes |
| Confirmed Data Exfiltration | No |
| Containment Required | Yes |
| Response Status | Escalated to Incident Response |

---

## Incident Classification

The incident is classified as a credential compromise involving unauthorized use of a valid domain account and attempted lateral movement.

The available evidence supports the following sequence:

- repeated failed authentication attempts for sarnold
- successful interactive authentication to IT-LT-017
- PowerShell execution
- host and domain discovery
- unusual outbound HTTPS activity initiated by PowerShell
- internal targeting of IT-WS-031
- SMB and ADMIN$ access attempts
- failed network authentication against IT-WS-031

The activity exceeded the threshold for routine alert handling once the account was used to target a second internal system.

---

## Why Escalation Is Justified

The original authentication alert was not enough by itself to justify a high-severity incident.

Several individual events had plausible benign explanations.

A help desk technician may legitimately:

- use PowerShell
- run network troubleshooting commands
- query domain information
- access remote systems
- use SMB
- work from shared IT equipment

The benign explanation breaks down when the events are placed in sequence and correlated across telemetry sources.

The combination of suspicious authentication, discovery activity, unexplained external communication, and attempted access to another internal endpoint is no longer consistent with routine support activity.

That progression is the basis for escalation.

---

## Confirmed Scope

### Confirmed Affected Account

sarnold

The account was successfully used from IT-LT-017 during the suspicious session.

### Confirmed Affected Asset

IT-LT-017

The device hosted the unauthorized session and generated the process and network activity associated with the incident.

### Secondary Target

IT-WS-031

The system was probed and targeted through SMB and ADMIN$ activity.

Authentication attempts against IT-WS-031 failed.

No successful secondary authentication is present in the available evidence.

---

## Confirmed Activity

The following activity is supported by the evidence:

- unauthorized use of valid credentials
- successful interactive logon
- PowerShell execution
- local system discovery
- network configuration discovery
- domain account discovery
- domain trust discovery
- network resource discovery
- unusual PowerShell-initiated outbound HTTPS connection
- remote host probing
- SMB access attempt
- ADMIN$ access attempt
- failed network authentication against a second endpoint

---

## Activity Not Confirmed

The investigation does not currently confirm:

- successful compromise of IT-WS-031
- successful lateral movement
- privilege escalation
- credential dumping
- persistence
- malware deployment
- data staging
- data exfiltration
- compromise of additional accounts
- compromise of additional endpoints

These items should remain outside the incident scope unless later evidence supports them.

---

## Severity Determination

Final Severity: High

The severity is based on:

- confirmed unauthorized use of a valid IT account
- activity from an internal managed asset
- administrative discovery
- unusual external communication
- attempted lateral movement
- targeting of a second endpoint

The incident is not classified as Critical because there is no evidence of:

- successful secondary compromise
- widespread account compromise
- production outage
- destructive activity
- material data loss
- enterprise-wide lateral movement

The severity can be reassessed if follow-on investigation identifies broader impact.

---

## Response Objectives

The immediate response should focus on four objectives:

1. Stop further use of the compromised account.
2. Prevent additional activity from IT-LT-017.
3. Verify whether IT-WS-031 or any other endpoint was successfully accessed.
4. Preserve enough evidence to support follow-on investigation and control review.

Response actions should be proportionate to the known scope.

There is enough evidence to contain the affected account and endpoint.

There is not enough evidence to treat the entire environment as compromised.

---

## Required Response Actions

The following actions should be initiated:

- isolate IT-LT-017 from the network
- disable or reset sarnold credentials
- terminate active sessions associated with sarnold
- preserve relevant authentication, endpoint, and network evidence
- review IT-WS-031 for successful access or process execution
- search for additional sarnold authentication activity
- search for additional connections to the external destination
- review other ADMIN$ or SMB activity originating from IT-LT-017
- validate the physical and custody status of IT-LT-017

---

## Escalation Path

The incident should move from SOC analyst review to incident response handling.

Recommended participants include:

- SOC analyst
- incident response lead or senior analyst
- endpoint / systems administrator
- identity administrator
- help desk management
- network administrator if broader traffic review is required

Physical security or facilities support may become relevant if follow-on review indicates unauthorized access to the help desk area.

That should remain a secondary escalation path unless evidence supports it.

---

## Open Questions

Several questions remain unresolved:

- how were the sarnold credentials obtained?
- who physically operated IT-LT-017?
- was IT-LT-017 left unlocked?
- was the device accessed by someone with legitimate physical access to the help desk area?
- what content was retrieved during the external PowerShell request?
- did the actor attempt access to any other endpoints?
- did related activity occur before the current investigation window?

These questions should drive follow-on investigation.

They do not prevent immediate containment.

---

## Disposition Statement

The incident is classified as a true-positive credential compromise involving unauthorized use of the sarnold account from IT-LT-017.

The activity included administrative discovery, unusual external PowerShell communication, and attempted lateral movement to IT-WS-031.

No successful secondary compromise or confirmed data loss has been identified.

Immediate containment is justified based on the known evidence, with additional scope review required before the incident can be considered fully resolved.
