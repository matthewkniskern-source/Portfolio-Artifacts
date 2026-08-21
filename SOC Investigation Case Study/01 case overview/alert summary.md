# Alert Summary

## Alert Metadata

| Field              | Value                       |
| ------------------ | --------------------------- |
| Alert ID           | SOC-2026-0817-0042          |
| Date               | 17 August 2026              |
| Initial Time       | 06:31                       |
| Initial Severity   | Medium                      |
| Alert Source       | SIEM correlation rule       |
| Detection Category | Authentication anomaly      |
| Affected Account   | sarnold                     |
| Source Asset       | IT-LT-017                   |
| Source Network     | Internal IT support segment |
| Status at Intake   | Open / Unvalidated          |
| Assigned Queue     | SOC Analyst Review          |

## Alert Description

The SIEM generated a medium-severity authentication alert after detecting multiple failed logon attempts for the account sarnold from IT-LT-017, followed by a successful authentication from the same source system within a short time window.

The source asset is an internal IT-owned loaner and troubleshooting laptop. The affected account belongs to a help desk technician with legitimate administrative responsibilities.

At intake, the activity could represent a routine password-entry issue, use of stale credentials, normal support activity, or unauthorized use of a valid account.

The alert requires analyst review because the successful authentication occurred after a concentrated series of failures and originated from a shared IT device that was not formally assigned to an individual user at the time of the event.

## Initial Event Pattern

The SIEM presents the following authentication pattern:

| Time | Event | Account | Source Asset | Result |
|---|---|---|---|---|
| 06:47:09 | 4625 | sarnold | IT-LT-017 | Failed logon |
| 06:47:26 | 4625 | sarnold | IT-LT-017 | Failed logon |
| 06:47:44 | 4625 | sarnold | IT-LT-017 | Failed logon |
| 06:48:03 | 4625 | sarnold | IT-LT-017 | Failed logon |
| 06:48:21 | 4625 | sarnold | IT-LT-017 | Failed logon |
| 06:50:54 | 4624 | sarnold | IT-LT-017 | Successful logon |

The alert logic is based primarily on the concentration of failed authentication attempts followed by a successful authentication from the same source.

At this stage, the SIEM has not established that the activity is malicious.

## Initial Context

The following information is available to the analyst at intake:

* sarnold is a valid Active Directory account.
* The account belongs to an IT help desk technician.
* IT-LT-017 is a managed corporate asset.
* IT-LT-017 is used as a shared loaner and troubleshooting laptop.
* The device is connected to the internal IT support network.
* The laptop was not formally checked out to an individual user at the time of the alert.
* PowerShell and command-line activity may be normal for the affected user's role.
* No confirmed account lockout occurred.
* No external source IP is involved in the initial authentication alert.
* No confirmed secondary host compromise is known at intake.

## Why the Alert Is Not Immediately Clear

The initial pattern contains both suspicious and potentially benign characteristics.

### Factors Supporting Benign Activity

* The account is valid.
* The source asset is company owned.
* The source asset is associated with IT support activity.
* The user normally has reason to access administrative tools.
* Repeated password failures can occur during normal troubleshooting.
* A successful logon following several failures may simply indicate that the correct password was eventually entered.

### Factors Supporting Further Review

* Five authentication failures occur in a short period.
* The same account successfully authenticates shortly afterward.
* The source device is shared and not assigned to a specific person.
* The analyst cannot establish the operator of the laptop from asset records alone.
* The account has broader access than a standard business user.
* Successful misuse of an IT account could provide a useful starting point for additional internal activity.

The alert therefore remains medium severity pending correlation with additional telemetry.

## Detection Logic

The synthetic SIEM rule is intended to identify a common authentication pattern:

Multiple failed logon events for the same account and source device, followed by a successful authentication within a defined time period.

The rule is designed to identify activity that may be associated with:

* repeated password guessing
* credential misuse
* use of stale or cached credentials
* account troubleshooting
* unauthorized use of a valid account

The rule does not classify the authentication itself as a confirmed compromise.

Its purpose is to generate an analyst review when the sequence warrants additional context.

## Initial Analyst Objectives

The assigned analyst should determine:

1. Whether sarnold was expected to be using IT-LT-017 at the time of the alert.
2. Whether the failed and successful authentication events represent normal user behavior.
3. What type of logon produced the successful Event 4624.
4. Whether additional process activity occurred immediately after authentication.
5. Whether PowerShell or other administrative utilities were executed.
6. Whether IT-LT-017 initiated unusual internal or external network connections.
7. Whether the same account was used against additional internal systems.
8. Whether the activity should remain an authentication anomaly or be escalated into an incident.

## Immediate Triage Actions

At intake, the analyst should avoid disruptive containment until additional evidence supports escalation.

Initial triage includes:

* review the 4625 and 4624 event details
* verify the source asset and account in inventory
* establish whether sarnold was expected to use the device
* review recent authentication history for the account
* pivot into endpoint process telemetry for IT-LT-017
* review network activity surrounding the successful authentication
* check for related alerts involving the same account or device

Endpoint isolation or account disablement is not initiated solely on the basis of the initial alert.

## Unknowns at Intake

The analyst does not yet know:

* who physically operated IT-LT-017
* whether sarnold intentionally authenticated from the device
* whether the password failures were user generated
* whether the successful authentication was legitimate
* whether PowerShell activity followed the logon
* whether an unusual outbound connection occurred
* whether internal discovery was performed
* whether lateral movement was attempted
* whether the account credentials were compromised
* whether the incident extends beyond IT-LT-017

These questions form the starting point for the investigation.

## Initial Disposition

Initial Severity: Medium

Confidence: Low to Moderate

Disposition: Suspicious authentication activity requiring validation

Escalation Status: Not yet confirmed

The alert remains open for investigation until endpoint, authentication, and network telemetry can be correlated.

