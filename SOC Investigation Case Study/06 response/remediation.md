# Remediation

## Purpose

This document defines the remediation and recovery actions for SOC-2026-0817-0042 after initial containment is complete.

Containment stops the known activity.

Remediation addresses the affected account, endpoint, related systems, and the control gaps exposed by the incident so the environment can return to normal operations without simply recreating the same conditions.

The priorities are:

1. restore the affected account securely
2. return IT-LT-017 to a trusted state
3. validate IT-WS-031
4. close the known access path
5. address the shared-device and monitoring gaps exposed by the incident
6. verify that normal operations can resume without evidence of continued compromise

---

## 1. Remediate the sarnold Account

The sarnold account should remain disabled until the response team completes account review.

Required actions include:

- reset the password using a trusted administrative system
- invalidate existing sessions and tokens where supported
- review MFA registration and recovery methods
- verify group memberships
- verify delegated permissions
- review recent authentication history
- review recent cloud and VPN activity
- confirm no unauthorized account changes occurred
- confirm no new application registrations or access methods were added

If account configuration remains consistent with the expected help desk role and no additional compromise is identified, the account may be restored after credential reset and validation.

### Return-to-Service Conditions

The sarnold account should not be returned to normal use until:

- the old credentials are invalid
- active sessions have been revoked
- MFA methods are validated
- recent authentication activity has been reviewed
- no unauthorized privilege or account changes are identified
- the user has been interviewed or otherwise validated as part of the incident review

---

## 2. Rebuild or Reimage IT-LT-017

IT-LT-017 hosted the confirmed unauthorized session.

Because the endpoint was used for discovery, external communication, and attempted lateral movement, simply reconnecting it after account remediation would not provide sufficient confidence in the system state.

The preferred recovery action is to reimage or rebuild the laptop from an approved corporate baseline.

Before reimaging:

- preserve required forensic and investigation data
- collect endpoint telemetry
- record relevant file hashes
- preserve logs
- preserve any suspicious files
- document installed applications
- preserve the investigation timeline
- confirm that any additional forensic review is complete

After preservation, the system should be rebuilt using the standard managed endpoint deployment process.

### Rebuild Requirements

The rebuilt device should include:

- current Windows security updates
- Microsoft Defender for Endpoint
- current endpoint policy
- approved applications only
- current inventory agent
- current configuration baseline
- domain or Entra registration as required
- validated logging
- validated endpoint telemetry

The system should not return to the shared device pool until those controls are verified.

---

## 3. Review the Retrieved File

The PowerShell activity wrote content to:

C:\Users\Public\Documents\status.txt

The file should be preserved before the endpoint is rebuilt.

Review should include:

- SHA-256 hash
- file size
- file type
- creation and modification timestamps
- content review
- antivirus or EDR verdict
- whether the same hash appears elsewhere in the environment

The investigation should avoid assuming the file is malware solely because it was retrieved during suspicious activity.

If the file is determined to be benign or inert, that should be documented.

If it contains executable content, commands, encoded material, or other suspicious data, the incident scope and ATT&CK mapping should be reassessed.

---

## 4. Validate IT-WS-031

IT-WS-031 was targeted but not confirmed compromised.

Before considering the secondary system cleared, review:

- successful authentication activity
- failed authentication activity
- process creation
- PowerShell execution
- remote service activity
- scheduled tasks
- new services
- local account changes
- administrative share access
- unusual outbound connections
- endpoint detections

The available case evidence currently supports attempted access only.

If no evidence of successful access or execution is identified, IT-WS-031 may remain in service.

If evidence of successful compromise appears, the endpoint should be isolated and remediated as a confirmed affected system.

---

## 5. Review Other Use of sarnold

The account should be searched across the environment for activity outside the original investigation window.

Review should include:

- successful logons
- failed logons
- VPN activity
- cloud authentication
- SMB activity
- remote support systems
- file server access
- administrative systems
- other shared IT devices

The purpose is to determine whether IT-LT-017 was the only unauthorized use of the account.

If other suspicious successful authentications are found, the incident scope should expand before closure.

---

## 6. Review Other Activity from IT-LT-017

The endpoint should be searched historically for related behavior.

Review:

- earlier PowerShell sessions
- previous external connections
- SMB activity
- remote authentication attempts
- ADMIN$ or C$ access
- unusual file creation
- script execution
- task creation
- service creation
- account changes

The existing twenty-minute window was sufficient for triage.

Remediation requires a broader review to determine whether the observed activity was the beginning of the compromise or only the point where it became visible.

---

## 7. Address Shared Device Custody

IT-LT-017 was physically located in the help desk area and was not formally assigned when the incident occurred.

That condition should be corrected.

Recommended changes include:

- require checkout or custody assignment for shared laptops
- record current custodian
- record checkout and return times
- avoid leaving shared devices signed in
- require workstation locking when unattended
- power down or disconnect unused shared devices where practical
- clearly identify device status in asset management

The goal is not to create an administrative burden for every troubleshooting laptop.

The goal is to eliminate situations where a managed device is available for use but nobody can reliably establish who had custody of it.

---

## 8. Review Help Desk Physical Access

The physical location of IT-LT-017 creates a legitimate follow-up question.

Review should determine:

- who had access to the help desk area before day shift
- whether the area was secured
- whether badge records exist
- whether camera coverage exists
- whether non-IT personnel could reasonably enter the area
- whether early-shift or overnight personnel were present

The outcome should be documented separately from the cyber findings.

The digital evidence does not establish a physical intruder.

Physical access review is intended to close an attribution and control gap, not to force a conclusion the telemetry cannot support.

---

## 9. Improve Workstation Locking Controls

Shared IT devices should follow the same basic session security expectations as permanently assigned endpoints.

Recommended controls include:

- automatic screen lock after an approved inactivity period
- password or approved authentication required to unlock
- prohibit shared generic user sessions
- prevent help desk staff from leaving privileged sessions unattended
- enforce session timeout where appropriate

If investigation determines IT-LT-017 was left unlocked, that should be recorded as a confirmed control failure.

If that cannot be established, the recommendation can still be carried forward as a preventive improvement.

---

## 10. Improve Asset Context

The SIEM investigation had to manually establish that IT-LT-017 was:

- a shared IT device
- physically located in the help desk area
- not checked out
- available before normal day-shift staffing

That context should be easier to obtain.

Where practical, asset records should expose:

- device owner
- device type
- shared-device status
- current custodian
- physical location
- business function
- expected user population

This information can improve alert enrichment without turning asset management into a detection system.

---

## 11. Implement Detection Improvements

The detection tuning recommendations identified several opportunities that should be carried into remediation.

Priority improvements include:

- correlate failed-successful authentication patterns with post-login activity
- retain process-to-network attribution
- correlate cross-host authentication
- improve SMB and ADMIN$ context
- baseline help desk and administrative accounts separately
- enrich alerts with asset and user context

The objective is not to make every administrative action generate a high-severity alert.

The objective is to identify when several normal-looking actions form an abnormal sequence.

---

## 12. Review Logging Coverage

The case depends on the availability of:

- Event 4624
- Event 4625
- Event 4688
- endpoint telemetry
- network telemetry
- process-to-network attribution

The organization should verify that these sources are consistently available across managed endpoints.

Review should include:

- process creation auditing
- command-line visibility
- endpoint telemetry health
- log forwarding
- retention periods
- clock synchronization
- asset coverage

Any gaps discovered during the incident should be documented and corrected.

---

## 13. Review Least Privilege

Because sarnold is a help desk technician, the account legitimately has broader access than a standard user.

Remediation should include review of whether the account has more privilege than required.

Questions include:

- Is local administrator access required everywhere?
- Are remote administrative shares required from shared laptops?
- Can help desk administration be limited to approved management systems?
- Are privileged tasks performed with separate administrative credentials?
- Can support access be restricted by source device or management subnet?

The incident does not automatically prove the account was overprivileged.

It does justify reviewing the current privilege model.

---

## 14. Consider Separate Administrative Accounts

If sarnold uses the same account for normal workstation activity and elevated support functions, the organization should consider separating those roles.

Example:

- standard user account for normal activity
- separate administrative account for elevated support tasks

This can reduce the impact of a compromised day-to-day credential and make administrative activity easier to baseline.

Implementation should be based on operational need and existing identity policy.

---

## 15. Recovery Validation

Before declaring the incident recovered, validate that:

- IT-LT-017 has been rebuilt or otherwise returned to a trusted state
- sarnold credentials have been replaced
- active sessions have been revoked
- IT-WS-031 shows no evidence of compromise
- no additional systems show related activity
- no additional unauthorized sarnold authentications are occurring
- logging and endpoint telemetry are operating normally
- required detection changes are tracked for implementation
- device custody actions have been assigned

Recovery should be based on evidence, not simply on the passage of time after containment.

---

## Return-to-Service Criteria

### sarnold

May return to normal use when:

- credentials are replaced
- MFA is validated
- sessions are revoked
- account permissions are reviewed
- expanded authentication review is complete

### IT-LT-017

May return to service when:

- evidence preservation is complete
- endpoint has been rebuilt or validated as trusted
- security tooling is operational
- logging is confirmed
- patching is current
- the device has a documented custody status

### IT-WS-031

May remain in service if:

- no successful unauthorized authentication is found
- no suspicious process execution is found
- no persistence is identified
- endpoint telemetry shows no related compromise

---

## Remediation Ownership

| Action | Suggested Owner |
|---|---|
| sarnold credential remediation | Identity / Systems Administration |
| Session revocation | Identity / Cloud Administration |
| IT-LT-017 rebuild | Endpoint / Help Desk |
| IT-WS-031 validation | SOC / Endpoint Administration |
| Expanded log review | SOC |
| Detection tuning | Security Engineering / SOC |
| Shared device custody changes | Help Desk Management |
| Physical access review | IT Management / Physical Security |
| Logging validation | Security / Systems Administration |

Ownership should be clear enough that remediation actions do not remain open simply because they cross team boundaries.

---

## Remediation Status

Credential Compromise: Remediation required

Primary Endpoint: Rebuild required

Secondary Endpoint: Validation required

Detection Improvements: Identified

Shared Device Controls: Review required

Physical Access Controls: Review required

Incident Status: Contained, remediation in progress

The incident can move to closure after technical recovery is validated, the affected account and endpoint are returned to a trusted state, and follow-on actions have either been completed or formally assigned.
