# Analyst Findings

## Finding Summary

The investigation supports a true-positive security incident involving compromise of the sarnold account and unauthorized activity from IT-LT-017.

The activity began with repeated failed authentication attempts, followed by a successful interactive logon from a shared IT laptop that was not assigned to a specific user at the time.

After authentication, the session progressed through PowerShell execution, local and domain discovery, an unusual outbound HTTPS connection, and attempted access to a second internal endpoint.

The evidence supports credential compromise and attempted lateral movement.

No successful secondary compromise was identified in the available telemetry.

## Final Disposition

| Field | Finding |
|---|---|
| Alert Disposition | True Positive |
| Final Severity | High |
| Confidence | High |
| Primary Account | sarnold |
| Primary Asset | IT-LT-017 |
| Secondary Target | IT-WS-031 |
| Secondary Compromise | Not confirmed |
| Data Exfiltration | Not confirmed |
| Lateral Movement | Attempted |
| Containment Required | Yes |

## Evidence Supporting the Finding

### Authentication Pattern

The initial alert was based on five failed interactive logons for sarnold from IT-LT-017 between 06:47:09 and 06:48:21.

A successful interactive logon followed at 06:50:54.

That sequence was enough to justify review, but not enough by itself to establish compromise.

Failed logons followed by a successful authentication happen in normal environments. The account was valid, the laptop belonged to IT, and sarnold had a role where administrative activity could reasonably occur.

The case became stronger only after the activity following the successful logon was reviewed.

### Post-Authentication Activity

PowerShell launched at 06:53:42, approximately three minutes after the successful authentication.

The session then used native Windows tools to identify:

- the current user
- the local hostname
- network configuration
- domain account information
- domain trust relationships
- available network resources
- active network connections

None of these actions is enough to establish malicious activity on its own.

For a help desk technician, most of them are defensible administrative actions.

The issue is the sequence.

The activity moves quickly from authentication into system and domain discovery without an identified support task or documented reason for use of the shared laptop.

### Unusual External Connection

At 06:58:03, PowerShell initiated an outbound HTTPS connection to 198.51.100.42 and wrote returned content to a public local directory.

Firewall telemetry identified the outbound connection.

Endpoint telemetry independently identified powershell.exe as the initiating process.

That correlation materially changed the investigation.

TCP 443 is normal. PowerShell is also normal in this environment.

What is not normal is an unexplained PowerShell-initiated external request appearing immediately after credential anomalies and a concentrated discovery sequence.

The destination is synthetic in this case and is not treated as malicious based on reputation. The concern comes from the behavior around the connection, not from the address itself.

### Internal Targeting

After the external connection, activity shifted toward IT-WS-031.

Observed actions included:

- ICMP reachability testing
- remote SMB resource discovery
- an attempted ADMIN$ connection
- network authentication attempts using sarnold

Authentication telemetry from the same window shows failed network logons against IT-WS-031.

The process, network, and authentication evidence all point to the same sequence.

This is the point where the activity is no longer reasonably explained as a simple password issue or routine PowerShell use.

## Why the Benign Explanation Breaks Down

Several parts of the case initially had reasonable benign explanations.

The failed logons could have been user error.

The successful logon could have been the same user correcting the password.

PowerShell could have been legitimate help desk work.

Domain discovery could have been troubleshooting.

TCP 443 could have been routine web traffic.

SMB activity could have been normal support access.

Taken one at a time, those explanations are all plausible.

They do not hold together well once the events are placed in order.

The sequence is:

Authentication failures  
→ successful logon  
→ PowerShell execution  
→ host and domain discovery  
→ unusual external PowerShell connection  
→ internal host targeting  
→ ADMIN$ access attempt  
→ failed authentication against a second endpoint

At that point, the case is no longer built around one suspicious event.

It is built around progression.

That progression is what supports the true-positive disposition.

## User Context

The sarnold account belongs to a help desk technician and therefore has legitimate reasons to use PowerShell, command-line tools, and remote administrative resources.

That context lowered the value of individual process events as indicators.

It also made correlation more important.

The later 07:34:08 authentication to IT-WS-023, sarnold's normally assigned workstation, is useful supporting context.

It does not prove that sarnold was not responsible for the earlier activity on IT-LT-017.

It does, however, create a reasonable point for user validation and supports review of whether the account owner was present or expected to be using the shared laptop before normal help desk staffing began.

## Asset and Physical Context

IT-LT-017 was physically located in the help desk area and was not formally checked out to an individual at the time of the activity.

That limits attribution.

The digital evidence establishes what occurred on the endpoint, but it does not establish who physically operated the laptop.

The investigation should not fill that gap with assumptions.

The device custody issue should be carried forward into post-incident review, including:

- shared device handling
- workstation locking
- access to the help desk area
- custody records
- powered-on but unassigned equipment
- available physical access records

Those are control questions raised by the incident, not conclusions established by the SOC telemetry.

## Confirmed Scope

The available evidence confirms involvement of:

- sarnold
- IT-LT-017
- attempted access to IT-WS-031

The available evidence supports:

- use of valid credentials
- successful interactive access to IT-LT-017
- PowerShell execution
- local host discovery
- domain discovery
- network discovery
- unusual outbound HTTPS activity
- SMB-based targeting of IT-WS-031
- attempted ADMIN$ access
- failed network authentication against IT-WS-031

## What Was Not Confirmed

The investigation did not identify evidence of:

- successful authentication to IT-WS-031
- confirmed compromise of a second endpoint
- confirmed persistence
- confirmed privilege escalation
- confirmed data staging
- confirmed data exfiltration
- successful deployment of malware to another host
- additional compromised user accounts

Those items should remain unconfirmed unless later evidence establishes otherwise.

The incident should not be expanded beyond what the telemetry supports.

## Immediate Response Recommendation

Based on the combined evidence, the incident warrants containment.

Recommended actions:

1. Isolate IT-LT-017 through endpoint response tooling.
2. Disable or reset the sarnold account.
3. Terminate active sessions associated with sarnold.
4. Review IT-WS-031 for successful authentication, process creation, persistence, and unusual network activity.
5. Search for additional use of sarnold across the environment.
6. Search for connections to the external destination from other endpoints.
7. Preserve endpoint, authentication, and network evidence from the investigation window.
8. Review the physical and custody status of IT-LT-017.

These actions are proportionate to the evidence.

The investigation supports a real compromise, but it does not support treating the event as a confirmed enterprise-wide breach.

## Residual Investigative Gaps

Several questions remain open at the end of the initial investigation:

- How were the sarnold credentials obtained?
- Who physically operated IT-LT-017?
- Was the laptop left unlocked or was authentication performed directly?
- Was the external request part of a larger tool or script?
- Did related activity occur before the current evidence window?
- Was the same account tested against additional hosts?
- Did the actor have physical access to the help desk area?
- Were shared-device handling practices followed?

These gaps should drive follow-on investigation and control review.

They should not be converted into findings without supporting evidence.

## Analyst Conclusion

The initial SIEM alert was correctly generated as a medium-severity authentication anomaly.

The investigation established that the authentication activity was part of a broader sequence involving unauthorized account use, administrative discovery, external PowerShell activity, and attempted access to a second internal endpoint.

The evidence supports classification as a true-positive credential compromise with attempted lateral movement.

The activity was contained before successful secondary compromise or confirmed data loss was identified.

The strongest part of the case is not any single command or alert.

It is that multiple telemetry sources independently support the same progression and leave the benign explanation increasingly difficult to defend.
