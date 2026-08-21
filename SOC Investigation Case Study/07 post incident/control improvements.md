# Control Improvements

## Purpose

The incident exposed a small number of specific control gaps across identity, endpoint management, detection, asset custody, and physical access.

The objective of this review is not to respond to one compromised account by creating a wall of new controls.

Each recommendation should trace back to something the incident actually exposed.

The priority is to improve visibility, reduce unnecessary ambiguity, and make the same sequence easier to detect and contain if it occurs again.

---

## Control Improvement Summary

| Area | Improvement | Priority |
|---|---|---|
| Detection | Correlate authentication with post-logon activity | High |
| Identity | Separate standard and administrative account use where practical | High |
| Endpoint | Preserve process-to-network attribution | High |
| Asset Management | Track custody of shared IT devices | High |
| Endpoint Security | Enforce unattended workstation locking | High |
| Detection | Correlate cross-host authentication and SMB activity | High |
| Logging | Validate 4624, 4625, 4688 and endpoint coverage | High |
| SIEM Enrichment | Add user, asset, and shared-device context | Medium |
| Administrative Access | Review ADMIN$ and remote support paths | Medium |
| Physical Security | Review access to help desk work area | Medium |
| Automation | Automate repetitive triage and evidence packaging | Medium |
| Governance | Assign ownership and validation dates to improvements | Medium |

---

## 1. Correlate Authentication With Post-Logon Behavior

### Observed Gap

The authentication alert correctly identified the initial anomaly, but subsequent process and network behavior required manual correlation.

### Improvement

Create a short post-authentication correlation window for suspicious successful logons.

Relevant activity should include:

- PowerShell execution
- multiple discovery commands
- unusual external connections
- SMB activity
- administrative share access
- authentication attempts against additional hosts

### Expected Benefit

The SIEM can raise confidence as the incident develops rather than presenting each event as an unrelated alert.

### Priority

High

---

## 2. Improve Administrative Account Separation

### Observed Gap

sarnold is a help desk technician whose account legitimately performs administrative activity.

That makes abnormal administrative behavior harder to distinguish from normal use.

### Improvement

Where operationally practical, separate:

- standard user activity
- privileged administrative activity

A technician could use a normal account for everyday workstation activity and a separate administrative identity for elevated support functions.

### Expected Benefit

Separate administrative identities improve:

- privilege control
- logging clarity
- behavioral baselining
- investigation context
- blast-radius reduction if a normal credential is compromised

### Priority

High

---

## 3. Review Administrative Privilege Scope

### Observed Gap

The compromised account was able to attempt remote administrative access against another internal endpoint.

### Improvement

Review whether help desk accounts require the current level of remote administrative capability from all managed devices.

Consider:

- limiting privileged access to approved management systems
- restricting administrative shares where not required
- limiting remote administration by source subnet or device
- applying least privilege to support roles
- reviewing local administrator assignments

### Expected Benefit

A compromised support credential has fewer paths available for lateral movement.

### Priority

High

---

## 4. Preserve Process-to-Network Attribution

### Observed Gap

The outbound TCP 443 connection became meaningful only when endpoint telemetry associated it with PowerShell.

Without that context, it looked like routine encrypted web traffic.

### Improvement

Ensure endpoint telemetry consistently records:

- process
- process ID
- parent process
- user
- destination
- destination port
- timestamp

### Expected Benefit

Analysts can distinguish ordinary browser or application traffic from network activity initiated by administrative or scripting tools.

### Priority

High

---

## 5. Correlate Cross-Host Authentication

### Observed Gap

The attempted lateral movement became clear only after authentication events against IT-WS-031 were tied back to IT-LT-017.

### Improvement

Correlate:

- source host
- account
- destination host
- authentication result
- SMB activity
- administrative share activity

Where an already-alerted endpoint begins authenticating against additional systems, incident confidence should increase.

### Expected Benefit

Early lateral movement becomes easier to identify before successful access spreads the incident.

### Priority

High

---

## 6. Validate Windows Security Logging

### Observed Gap

The investigation depended heavily on Event IDs 4624, 4625, and 4688.

Inconsistent collection of those events would significantly reduce visibility.

### Improvement

Verify across managed Windows systems that:

- successful logons are collected
- failed logons are collected
- process creation auditing is enabled
- command-line visibility is available where policy allows
- timestamps are synchronized
- forwarding is functioning
- retention supports incident review

### Expected Benefit

The SOC maintains a consistent minimum evidence set for authentication and endpoint investigations.

### Priority

High

---

## 7. Formalize Shared Device Custody

### Observed Gap

IT-LT-017 was a managed corporate endpoint but had no identified custodian during the incident window.

### Improvement

Shared IT devices should have a lightweight custody process that records:

- current user or custodian
- checkout time
- return time
- device status
- physical location

This does not need to become a heavy administrative workflow.

It needs to answer one basic question:

Who was supposed to have the device?

### Expected Benefit

Asset information becomes useful during attribution and incident validation instead of simply confirming that the organization owns the laptop.

### Priority

High

---

## 8. Enforce Unattended Workstation Locking

### Observed Gap

The investigation could not establish whether IT-LT-017 had been left unlocked.

The uncertainty itself is enough to justify reviewing the control.

### Improvement

Confirm enforcement of:

- automatic screen locking
- authentication on unlock
- appropriate inactivity timeout
- no unattended privileged sessions
- no shared generic desktop sessions

### Expected Benefit

Physical access to a managed endpoint does not automatically become access to an authenticated session.

### Priority

High

---

## 9. Improve SIEM Asset and Identity Enrichment

### Observed Gap

The analyst had to manually determine that:

- sarnold was a help desk technician
- IT-LT-017 was a shared device
- the laptop was unassigned
- the device was located in the help desk area
- the activity occurred before normal day-shift staffing

### Improvement

Where data is available, enrich alerts with:

- user role
- privileged status
- assigned workstation
- source device type
- shared-device status
- device owner
- current custodian
- physical location
- normal login hours

### Expected Benefit

Analysts receive useful context at the beginning of triage rather than discovering it manually several pivots into the investigation.

### Priority

Medium

---

## 10. Baseline IT Activity Separately

### Observed Gap

Administrative tools generate different behavior for IT personnel than they do for standard users.

### Improvement

Develop separate behavioral expectations for technical accounts and systems.

Useful baseline elements include:

- normal PowerShell frequency
- normal administrative tools
- common remote targets
- expected workstations
- normal support hours
- approved external services
- expected SMB activity

### Expected Benefit

The SOC can reduce noise without ignoring suspicious administrative behavior.

### Priority

Medium

---

## 11. Review Help Desk Physical Access

### Observed Gap

The affected laptop was physically located in the help desk area before normal day-shift staffing.

Digital evidence cannot determine who operated it.

### Improvement

Review:

- badge access
- door controls
- early-shift access
- contractor or non-IT access
- visitor practices
- camera coverage where appropriate
- placement of shared equipment

### Expected Benefit

The organization can determine whether the help desk area provides an appropriate level of physical protection for systems capable of administrative access.

### Priority

Medium

---

## 12. Improve Shared Device Idle State

### Observed Gap

IT-LT-017 was powered on, connected, and available while not actively assigned.

### Improvement

Establish an expected state for unused shared IT systems.

Depending on operational need, that may include:

- powered off
- disconnected
- locked
- stored securely
- checked into a known device pool state

### Expected Benefit

Unassigned equipment presents less opportunity for unauthorized use while remaining available when legitimately needed.

### Priority

Medium

---

## 13. Automate Repetitive Triage

### Observed Gap

Several investigation steps required repetitive filtering and data preparation.

### Improvement

Continue developing defensive PowerShell tooling for:

- host triage collection
- authentication pattern detection
- investigation timelines
- process and network correlation
- evidence export
- integrity hashing

Automation should return structured evidence for review rather than automatically assigning incident disposition.

### Expected Benefit

Analysts spend less time gathering the same data repeatedly and more time evaluating what the data means.

### Priority

Medium

---

## 14. Review Alert Escalation Logic

### Observed Gap

The initial authentication alert remained medium severity even as additional related behaviors appeared.

### Improvement

Introduce explainable correlation scoring or staged escalation.

For example:

```text
Authentication anomaly
        |
        + discovery behavior
        |
        + unusual process-driven egress
        |
        + remote host targeting
        |
        + remote authentication
        |
        v
Escalated incident confidence
```

The exact thresholds should be tuned against production data.

### Expected Benefit

Severity follows the development of the incident instead of remaining tied to the first event that happened to trigger.

### Priority

Medium

---

## 15. Establish Improvement Ownership

Control improvements are only useful if someone owns them.

Recommended ownership:

| Improvement | Suggested Owner |
|---|---|
| Authentication correlation | SOC / Security Engineering |
| Administrative account separation | Identity / Systems Administration |
| Privilege review | Identity / IT Management |
| Process-network telemetry | Endpoint / Security Engineering |
| Cross-host authentication detection | SOC / Security Engineering |
| Windows logging validation | Systems / Security |
| Shared device custody | Help Desk Management |
| Workstation locking | Endpoint Management |
| SIEM enrichment | SOC / Security Engineering |
| IT behavior baselines | SOC |
| Physical access review | IT Management / Physical Security |
| Triage automation | SOC / Security Engineering |

Each action should have:

- an owner
- a target date
- a validation method
- a documented closure status

---

## Validation

Control improvements should be tested rather than considered complete because a configuration change was made.

Examples include:

- verify the SIEM correlates a simulated failed-successful authentication sequence
- confirm process-to-network telemetry identifies the initiating process
- test that an unattended shared laptop locks according to policy
- verify shared device checkout records identify the current custodian
- confirm Event 4624, 4625, and 4688 reach the SIEM
- verify remote administrative access follows the intended privilege model
- confirm alert enrichment displays expected asset and identity context

A control is not complete until the organization can demonstrate that it behaves as intended.

---

## Improvement Principle

The incident does not justify locking down every administrative tool or generating an alert every time an IT technician touches PowerShell.

That would solve the wrong problem.

The better control set improves context, attribution, correlation, and least privilege.

The environment should still allow help desk staff to do their jobs.

It should simply become harder for unauthorized use of a valid account and a legitimate IT asset to blend into that normal activity.
