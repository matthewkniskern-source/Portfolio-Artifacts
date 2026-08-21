# Incident Scenario

## Overview

This case study follows a synthetic security incident at a mid-sized construction and project services company with a mixed office and field workforce. The company has roughly 325 employees, a small internal IT team, and a moderate security program built around Microsoft-based endpoint, identity, and logging tools.

The incident begins with what looks like a fairly routine authentication problem. An IT help desk account records several failed logon attempts from a shared loaner laptop, followed by a successful authentication. By itself, that would not be enough to establish compromise. The account belongs to a help desk technician, the source device is part of the IT inventory, and both PowerShell and remote administrative activity are normal enough in that role to create some initial ambiguity.

That ambiguity does not last.

As the SOC reviews the activity, additional events begin to line up: PowerShell execution, host and network discovery, an unusual outbound connection, and an attempted connection to another internal system. None of the individual events is especially dramatic. Taken together, they establish a pattern consistent with credential compromise and early lateral movement.

The goal of the investigation is to determine whether the alert represents normal IT activity, misuse of a valid account, or an active compromise, and to contain the activity before it develops into a broader incident.

## Organization Context

The fictional organization, Northstar Project Services, supports commercial construction and project delivery across a mix of office and field locations. Most users work from Windows 11 endpoints and rely on Microsoft 365, Active Directory, Entra ID, VPN access, and shared project resources.

The IT department maintains a small pool of loaner and troubleshooting laptops that can be issued temporarily or used for support work. These systems are legitimate administrative assets, but their shared nature also makes ownership and activity attribution less straightforward than on a permanently assigned workstation.

The organization has centralized Windows event logging, Microsoft Defender for Endpoint, firewall and VPN telemetry, and a basic SIEM. The environment has enough visibility to support a meaningful investigation, but it is not assumed to have perfect logging or mature automation across every endpoint.

## Affected Account and Asset

The account involved in the incident is:

sarnold

sarnold belongs to an IT help desk technician. The user routinely performs workstation troubleshooting, account support, remote assistance, and basic administrative tasks. PowerShell, command-line utilities, remote access, and elevated actions may therefore be legitimate depending on context.

The initial source of suspicious activity is:

IT-LT-017

IT-LT-017 is a shared IT loaner and troubleshooting laptop. The device is not permanently assigned to one employee, which initially limits the analyst's ability to determine whether the activity is expected.

## Initial Activity

At approximately 08:12 on a normal business day, the SIEM generates a medium-severity alert after detecting several failed authentication attempts for sarnold, followed shortly afterward by a successful authentication from IT-LT-017.

The successful authentication alone does not establish compromise. A technician could have entered an incorrect password several times, reconnected to a system using stale credentials, or performed normal troubleshooting from the shared laptop.

The source system is internal. The account is valid. The role has legitimate administrative responsibilities.

At this point, the alert remains suspicious but unresolved.

## Escalating Indicators

Several minutes after the successful authentication, process telemetry shows activity that includes PowerShell and common Windows administrative utilities.

Observed activity includes commands consistent with:

* identifying the logged-in user
* identifying the local system
* reviewing network configuration
* examining domain or trust information
* checking available network resources

These actions can be legitimate for IT support, but the sequence begins to look less like routine troubleshooting when combined with the authentication pattern.

The investigation then identifies a PowerShell action that results in an outbound HTTPS connection to an external address not previously associated with normal activity from IT-LT-017.

The connection uses TCP 443, which is common and not suspicious on its own. The concern comes from the timing, the originating process, and the fact that it follows a successful authentication and a series of discovery-related commands.

Shortly afterward, the same account is used in an attempted connection to another internal endpoint.

The attempt does not result in confirmed access to the second system.

## Ground Truth

For purposes of the case study, the final determination is that the sarnold account was compromised and used from IT-LT-017 without authorization.

The attacker successfully authenticated with valid credentials, executed PowerShell and native Windows utilities, performed limited host and network discovery, and attempted to extend access to another internal system.

The activity was identified and contained before a second endpoint was successfully compromised and before evidence of significant data staging or exfiltration was observed.

This was not a large-scale breach. It was a limited but legitimate security incident involving a valid account, an internal administrative asset, and early-stage lateral movement.

## Containment Outcome

The SOC escalated the event from a medium-severity authentication alert to a confirmed security incident after correlating authentication, process, network, and endpoint activity.

The affected account was disabled or reset, IT-LT-017 was isolated for investigation, active sessions were terminated, and the attempted lateral movement target was reviewed for signs of compromise.

No confirmed secondary host compromise was identified.

The incident therefore ended with:

* confirmed credential compromise
* limited internal reconnaissance
* suspicious PowerShell activity
* one attempted lateral movement action
* no confirmed secondary compromise
* no confirmed material data loss
* successful containment before further progression

## Case Study Scope

This case study focuses on the SOC investigation and response process rather than on reproducing offensive activity.

The supporting telemetry, logs, IP addresses, usernames, hostnames, and event data are synthetic and are designed to resemble normal Windows enterprise security data. The scenario is modeled around common authentication, endpoint, process, and network behaviors documented in public Microsoft and MITRE ATT&CK resources.

The investigation will be used to demonstrate:

* alert triage
* Windows event analysis
* PowerShell and CLI-based investigation
* evidence correlation
* incident timeline development
* security automation
* MITRE ATT&CK mapping
* containment and remediation decisions
* post-incident detection and control improvements
