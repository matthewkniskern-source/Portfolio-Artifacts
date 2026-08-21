# Containment

## Purpose

This document defines the immediate containment actions for SOC-2026-0817-0042.

The incident has already moved beyond alert validation. The sarnold account is confirmed compromised, IT-LT-017 is the affected endpoint, and attempted lateral movement toward IT-WS-031 has been identified.

Containment should stop further activity without destroying evidence or expanding the scope of the response beyond what the investigation supports.

The priority is straightforward:

1. stop account misuse
2. stop endpoint activity
3. protect the secondary target
4. preserve evidence
5. determine whether the incident extends further

---

## Containment Priorities

| Priority | Action                          | Objective                                               |
| -------- | ------------------------------- | ------------------------------------------------------- |
| 1        | Isolate IT-LT-017               | Stop additional network activity from the affected host |
| 2        | Disable or secure sarnold       | Prevent continued use of compromised credentials        |
| 3        | Terminate active sessions       | Remove existing authenticated access                    |
| 4        | Review and protect IT-WS-031    | Verify attempted lateral movement did not succeed       |
| 5        | Preserve investigation evidence | Maintain data required for scope and follow-on analysis |
| 6        | Expand targeted searches        | Identify related account, endpoint, or network activity |

---

## 1. Isolate IT-LT-017

IT-LT-017 should be isolated through Microsoft Defender for Endpoint or equivalent endpoint response tooling.

The preferred action is logical network isolation rather than immediately powering the system off.

This allows the response team to:

* stop further communication
* prevent additional internal access attempts
* preserve the current endpoint state
* retain access through approved response tooling where available
* continue evidence collection if required

The analyst should record:

* isolation time
* analyst or responder initiating the action
* response platform used
* endpoint status after isolation

### Expected Result

IT-LT-017 can no longer initiate normal internal or external network connections.

If endpoint tooling provides an approved management channel during isolation, that channel may remain available for response activity.

---

## 2. Secure the sarnold Account

The sarnold account should be disabled or have its credentials reset according to organizational incident-response policy.

Because the credentials have been used without authorization, the current password should be treated as compromised.

Recommended actions include:

* disable the account during initial containment
* revoke or terminate active sessions
* reset the password through a trusted administrative workflow
* require reauthentication after the account is restored
* review authentication methods associated with the account
* verify MFA registration where applicable

The user should not reset the password from IT-LT-017.

Any credential recovery or account restoration should occur from a known-good administrative system.

---

## 3. Terminate Active Sessions

Credential reset alone may not invalidate every active session immediately.

Where supported, terminate active sessions associated with sarnold across:

* Active Directory-connected resources
* VPN
* Microsoft 365
* Entra ID
* remote support platforms
* administrative sessions
* other applications using centralized identity

The purpose is to prevent an existing token or authenticated session from surviving the password reset.

The response record should document which session types were reviewed and which were revoked.

---

## 4. Protect IT-WS-031

IT-WS-031 was targeted but is not confirmed compromised.

The response should therefore validate the system before taking more disruptive action.

Review should include:

* successful Event 4624 activity during and after the incident window
* failed Event 4625 activity
* Event 4688 process creation
* new services
* scheduled tasks
* unusual PowerShell activity
* SMB and administrative-share activity
* unexpected outbound connections
* endpoint alerts
* new or modified local accounts

If evidence of successful access is identified, IT-WS-031 should be isolated and added to the confirmed incident scope.

If no evidence of successful compromise is found, the system can remain classified as a targeted asset rather than an affected asset.

That distinction should be maintained in the incident record.

---

## 5. Preserve Evidence

Containment should not erase the evidence needed to understand the incident.

Preserve the available telemetry before routine retention or administrative activity alters it.

Priority evidence includes:

* authentication-events.csv
* process-events.csv
* network-connections.csv
* endpoint telemetry from IT-LT-017
* relevant logs from IT-WS-031
* SIEM alert details
* firewall records
* Entra ID authentication history
* VPN activity
* account activity for sarnold
* available asset and device custody records

The automation in this case can be used to package the normalized investigation evidence and generate SHA-256 hashes.

That integrity record supports basic evidence handling but is not treated as a formal forensic chain-of-custody process.

---

## 6. Expand the Account Search

Once sarnold is confirmed compromised, the investigation window should expand beyond the original 20-minute triage period.

Search for:

* earlier failed authentication attempts
* earlier successful logons from unusual hosts
* authentication from other shared IT devices
* VPN access
* cloud authentication
* access to file servers
* access to administrative systems
* authentication attempts against additional endpoints

The objective is to determine whether the observed incident represents the beginning of the compromise or simply the first activity that triggered an alert.

---

## 7. Expand the Endpoint Search

Review IT-LT-017 for activity outside the initial timeline.

Search for:

* earlier PowerShell execution
* command shell activity
* downloads
* unusual file creation
* persistence mechanisms
* scheduled tasks
* service creation
* new user accounts
* browser activity
* unusual processes
* outbound connections
* additional SMB activity

The investigation should remain evidence driven.

The responder should not assume persistence or malware exists simply because the account was compromised.

---

## 8. Search for the External Destination

Search the environment for additional connections to 198.51.100.42 within the synthetic case data.

In a production incident, the equivalent search would include:

* firewall logs
* proxy logs
* endpoint network telemetry
* DNS history
* SIEM network events
* other EDR detections

The objective is to determine whether the destination appears only on IT-LT-017 or is associated with broader activity.

If additional hosts are identified, they should be reviewed separately before being added to the confirmed incident scope.

---

## 9. Search for Additional Lateral Movement

Review activity originating from IT-LT-017 and sarnold for signs of access attempts against other internal systems.

Relevant indicators include:

* TCP 445 activity
* ADMIN$ or C$ access
* remote authentication
* RDP
* WinRM
* remote service creation
* PowerShell remoting
* repeated failed logons across multiple hosts

No additional system should be labeled compromised solely because it received traffic from IT-LT-017.

Each target should be validated using its own authentication, process, and endpoint telemetry.

---

## 10. Physical and Custody Review

The cyber investigation establishes that unauthorized activity occurred from IT-LT-017.

It does not establish who physically operated the device.

Because the laptop was located in the help desk area and was not formally checked out, a limited physical and custody review is appropriate.

Review should determine:

* when IT-LT-017 was last legitimately used
* whether the laptop was left unlocked
* whether it was normally left powered on
* who had access to the help desk area before day shift
* whether badge or access-control records exist
* whether camera coverage is available
* whether another employee reported using the device
* whether device checkout procedures were followed

This review should not delay cyber containment.

It is a parallel effort intended to answer an attribution and control question raised by the incident.

---

## Containment Decision Matrix

| Condition                                        | Action                                            |
| ------------------------------------------------ | ------------------------------------------------- |
| Confirmed compromise on IT-LT-017                | Isolate                                           |
| Confirmed compromised account                    | Disable/reset and revoke sessions                 |
| IT-WS-031 targeted but no successful access      | Investigate and monitor                           |
| Successful access identified on IT-WS-031        | Isolate and expand incident scope                 |
| Additional host contacts external destination    | Review before scope expansion                     |
| Additional successful unauthorized sarnold logon | Add system to investigation                       |
| Physical access uncertainty only                 | Review separately; do not infer attacker identity |

---

## Actions to Avoid

The response should avoid unnecessary actions that could either destroy evidence or create avoidable business impact.

Do not:

* immediately wipe or reimage IT-LT-017 before evidence preservation
* assume IT-WS-031 is compromised solely because access was attempted
* disable unrelated accounts without supporting evidence
* block all PowerShell use across the environment as an incident reaction
* treat all SMB or ADMIN$ activity as malicious
* label the external destination as confirmed command-and-control without evidence
* assume a physical intruder operated the laptop
* expand the incident to the entire domain without supporting telemetry

Containment should be decisive where the evidence is strong and restrained where it is not.

---

## Containment Success Criteria

Initial containment is successful when:

* IT-LT-017 is isolated
* sarnold can no longer authenticate using the compromised credentials
* existing sessions are revoked where supported
* IT-WS-031 has been reviewed for successful compromise
* relevant evidence has been preserved
* no additional unauthorized authentication is observed
* no additional lateral movement is identified during the immediate review window

Successful containment does not mean the incident is closed.

It means the actor's known ability to continue the observed activity has been interrupted.

---

## Containment Status

Primary Endpoint: Contained

Compromised Account: Secured

Secondary Target: Under validation

Known Lateral Movement: Attempted, not confirmed successful

Known Data Loss: None confirmed

Incident Status: Contained pending remediation and recovery

The incident can move into remediation once the response team is satisfied that the known access path has been interrupted and the immediate scope has been reasonably established.

