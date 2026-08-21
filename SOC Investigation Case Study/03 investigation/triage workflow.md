# Triage Workflow

## Purpose

This workflow defines the initial investigation path for the authentication alert involving sarnold and IT-LT-017.

The point is not to assume compromise because several events look suspicious when placed next to each other. The analyst has to establish whether the activity fits normal help desk behavior, whether it can be explained by routine support work, and whether the evidence is strong enough to justify escalation.

The investigation starts with the alert as presented and builds outward from there.

## Step 1 - Validate the Alert

The first step is to confirm that the alert is based on real authentication activity and not a parsing issue, duplicate event, or obvious false positive.

Review:

- Event 4625 failures for sarnold
- Event 4624 success following the failures
- source asset
- source IP
- logon type
- authentication package
- time between failures and successful authentication

The initial sequence is:

| Time | Event | Result |
|---|---|---|
| 06:47:09 | 4625 | Failed logon |
| 06:47:26 | 4625 | Failed logon |
| 06:47:44 | 4625 | Failed logon |
| 06:48:03 | 4625 | Failed logon |
| 06:48:21 | 4625 | Failed logon |
| 06:50:54 | 4624 | Successful logon |

This is enough to justify review, but not enough to call the account compromised.

## Step 2 - Validate the Account and Source Asset

Confirm that sarnold is a valid account and determine whether the account normally performs administrative activity.

Asset and identity review establishes that:

- sarnold is an IT help desk technician
- IT-LT-017 is a legitimate company-owned device
- IT-LT-017 is a shared loaner and troubleshooting laptop
- the laptop was physically located in the help desk area
- the device was not formally assigned to an individual at the time of the event
- PowerShell and command-line tools are reasonable for sarnold's role

That context matters.

A suspicious PowerShell session involving a standard accounting user would carry a different weight than the same activity involving a help desk account. The tool is not the finding. The sequence and context are.

## Step 3 - Review Recent Authentication History

The analyst should determine whether the alert represents an isolated event or a change from normal account behavior.

Review:

- recent successful sarnold logons
- recent failed sarnold logons
- usual source devices
- normal work hours
- authentication from shared IT systems
- VPN or remote access activity
- whether the same account appears on more than one endpoint during the same period

The goal is to answer a simple question:

Is this something sarnold normally does?

The later 07:34:08 successful logon to IT-WS-023 is relevant because that workstation is normally assigned to sarnold.

It does not prove the earlier activity was unauthorized, but it creates a useful point for validation.

## Step 4 - Pivot to Endpoint Activity

Once the successful authentication at 06:50:54 is established, the analyst should review process activity on IT-LT-017 immediately before and after the logon.

Focus first on the period from approximately 06:50 through 07:05.

Normal session initialization should be separated from user-driven activity.

The investigation identifies PowerShell starting at 06:53:42, followed by:

- whoami
- hostname
- ipconfig
- net
- nltest
- network resource discovery
- active connection review

At this point, the activity remains explainable as help desk troubleshooting.

The question is no longer whether administrative tools were used.

The question becomes whether the sequence makes sense for legitimate support activity.

## Step 5 - Identify the Behavioral Pivot

The analyst should look for activity that changes the context of the session.

At 06:58:03, PowerShell initiates an outbound HTTPS connection to 198.51.100.42 and writes returned content to a local public directory.

This event deserves additional scrutiny because:

- the connection originates from PowerShell
- the destination is not part of the normal observed activity for the host
- it follows several minutes of system and domain discovery
- the action is not immediately explained by the user's normal role

The event still should not be viewed in isolation.

The analyst should confirm it against network telemetry.

## Step 6 - Correlate Network Evidence

Review network telemetry for IT-LT-017 during the same window.

The investigation should confirm:

- source process
- destination
- destination port
- timing
- whether the connection was allowed
- whether the destination appears elsewhere in normal host activity

Firewall and endpoint telemetry both identify the outbound connection to 198.51.100.42:443.

Endpoint telemetry associates the session with powershell.exe.

That correlation is stronger than the network event by itself.

## Step 7 - Check for Internal Follow-On Activity

Once unusual outbound activity is confirmed, the analyst should determine whether the session remained local to IT-LT-017.

Review for:

- internal host discovery
- SMB activity
- remote service access
- authentication attempts against other systems
- administrative share access
- RDP or remote management activity

The evidence shows activity directed at IT-WS-031.

The sequence includes:

- reachability testing
- SMB resource queries
- an attempted ADMIN$ connection
- failed network authentication using sarnold credentials

This is the point where the investigation changes materially.

The activity is no longer limited to a questionable login and unusual PowerShell use on one machine.

There is now evidence of attempted access to another internal endpoint.

## Step 8 - Correlate Across Telemetry Sources

The analyst should build a single timeline rather than treating authentication, process, and network telemetry as separate problems.

The core sequence is:

Authentication failures  
→ successful interactive logon  
→ PowerShell execution  
→ host and domain discovery  
→ unusual external HTTPS connection  
→ internal host probe  
→ SMB and ADMIN$ activity  
→ failed network authentication to second endpoint

No individual event carries the full case.

The value comes from the progression.

## Step 9 - Validate User Context

At this point, the analyst should attempt to establish whether sarnold was expected to be using IT-LT-017 before the help desk day shift began.

Relevant checks include:

- work schedule
- assigned workstation
- whether sarnold had checked out IT-LT-017
- whether another technician was using the laptop
- help desk staffing at the time
- physical access to the work area
- whether the user can account for the observed activity

The later login to IT-WS-023 becomes useful here.

If sarnold reports arriving for normal shift and logging into the assigned workstation around 07:34, that materially weakens the benign explanation for the earlier activity on IT-LT-017.

It still needs to be treated as corroborating context rather than proof by itself.

## Step 10 - Reassess Severity

The alert began as a medium-severity authentication anomaly.

By this point, the analyst has identified:

- repeated failed authentication
- successful use of the same credentials
- activity from a shared and unassigned IT asset
- PowerShell execution
- system and domain discovery
- unusual PowerShell-initiated external traffic
- attempted access to another internal system
- failed authentication against that second endpoint

That combination is no longer reasonably explained as a simple password-entry issue.

The event should be escalated from an authentication anomaly to a suspected credential compromise with attempted lateral movement.

## Step 11 - Escalate and Recommend Containment

Once the activity is assessed as likely malicious, the analyst should recommend containment.

Initial actions include:

- isolate IT-LT-017
- disable or reset sarnold credentials
- terminate active sessions
- review IT-WS-031 for evidence of successful access
- preserve relevant endpoint and authentication telemetry
- expand the search for additional use of the account
- review the external connection for related activity elsewhere in the environment

The analyst should document the reason for escalation and the evidence supporting each containment action.

## Decision Point

The investigation moves from alert triage to incident response when the combined evidence is no longer reasonably consistent with routine help desk activity.

The strongest indicator is not PowerShell by itself, the failed logons by themselves, or the external connection by itself.

It is the full sequence.

That distinction matters because this environment contains real administrative users doing real administrative work. A useful SOC process has to separate unusual activity from malicious activity without treating every powerful tool as an incident.

## Workflow Summary

Alert validation  
→ account and asset context  
→ authentication review  
→ endpoint process review  
→ network correlation  
→ lateral movement check  
→ user validation  
→ severity reassessment  
→ escalation and containment

The workflow is intentionally manual at this stage.

Later automation will be used to reduce the repetitive parts of this process, particularly log filtering, time-window correlation, and identification of repeated failed-successful authentication patterns. Analyst judgment remains necessary for the final disposition.
