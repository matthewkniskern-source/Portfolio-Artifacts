# Incident Timeline

## Purpose

This timeline reconstructs the incident involving the sarnold account and IT-LT-017 using authentication, process, and network evidence.

The intent is to show the sequence in the order it occurred and identify where the activity changes from explainable help desk behavior into something that no longer fits normal use.

## Reconstructed Timeline

| Time | Source | Event | Analyst Significance |
|---|---|---|---|
| 06:47:09 | Authentication | First failed logon for sarnold from IT-LT-017 | Beginning of suspicious authentication sequence |
| 06:47:26 | Authentication | Second failed logon | Repeated failure |
| 06:47:44 | Authentication | Third failed logon | Pattern continues |
| 06:48:03 | Authentication | Fourth failed logon | Concentrated failures from same host |
| 06:48:21 | Authentication | Fifth failed logon | Threshold sufficient for SIEM review |
| 06:50:54 | Authentication | Successful interactive logon for sarnold on IT-LT-017 | Same account and host successfully authenticate after repeated failures |
| 06:50:57 | Process | userinit.exe launches | Normal interactive session initialization |
| 06:51:00 | Process | explorer.exe launches | Normal Windows desktop session begins |
| 06:51:19 | Process | OneDrive.exe launches | Normal user-session activity |
| 06:51:48 | Process | Microsoft Edge launches | Normal browser activity |
| 06:53:42 | Process | powershell.exe launches | Administrative activity begins approximately three minutes after logon |
| 06:54:07 | Process | whoami.exe | Current user identification |
| 06:54:19 | Process | hostname.exe | Local host identification |
| 06:54:36 | Process | ipconfig.exe /all | Network configuration discovery |
| 06:54:58 | Process | net user sarnold /domain | Domain account information queried |
| 06:55:21 | Process | nltest.exe /domain_trusts | Domain trust discovery |
| 06:55:47 | Process | net view /domain | Network and domain resource discovery |
| 06:56:13 | Process | Get-NetTCPConnection | Active network connection review |
| 06:58:03 | Process / Network | PowerShell initiates HTTPS request to 198.51.100.42:443 | First event not readily explained by routine local troubleshooting |
| 06:58:04 | Endpoint Telemetry | Defender telemetry confirms powershell.exe as initiating process | Independent process attribution strengthens network finding |
| 06:58:41 | Process | Downloaded file opened from public documents directory | Confirms content returned by external request was accessed locally |
| 06:59:12 | Process | arp -a | Local network neighbor discovery |
| 06:59:46 | Process / Network | IT-WS-031 pinged | Activity begins shifting toward a second internal endpoint |
| 07:00:09 | Process | net view \\IT-WS-031 | Remote resource query |
| 07:00:10 | Network | SMB connection to IT-WS-031:445 | Network telemetry confirms remote resource access attempt |
| 07:01:51 | Process | net use \\IT-WS-031\ADMIN$ /user:NPS\sarnold | Administrative share connection attempted |
| 07:01:52 | Network | SMB connection associated with ADMIN$ attempt | Network telemetry confirms second-host access attempt |
| 07:02:17 | Authentication | Failed network logon for sarnold against IT-WS-031 | Authentication evidence independently supports lateral movement attempt |
| 07:02:34 | Authentication | Second failed network logon against IT-WS-031 | Repeated attempt against second endpoint |
| 07:05-07:10 | SOC Review | Authentication, process, and network events correlated | Alert confidence increases and investigation expands |
| 07:27:53 | Authentication | rlopez logs into assigned help desk workstation | Normal day-shift staffing begins |
| 07:29:16 | Authentication | knguyen logs into assigned help desk workstation | Additional help desk staff arrive |
| 07:31:42 | Authentication | dmiller logs into assigned help desk workstation | Day-shift activity becomes established |
| 07:34:08 | Authentication | sarnold logs into IT-WS-023 | Account owner appears on normal assigned workstation after earlier suspicious activity |

## Key Transition Points

### Authentication Anomaly

The first transition occurs between 06:47 and 06:50.

Five failed interactive logons are followed by a successful logon using the same account and source device.

At this point, the activity is suspicious but still reasonably explainable as a normal password-entry issue.

### Administrative Discovery

Between 06:53 and 06:56, the session begins using PowerShell and native Windows administrative utilities.

The commands identify the user, host, network configuration, domain information, and available resources.

Because sarnold is a help desk technician, this activity remains ambiguous.

The commands themselves do not establish compromise.

### External Connection

At 06:58:03, PowerShell initiates an HTTPS request to 198.51.100.42 and writes returned content to a local public directory.

This is the first event that significantly weakens the routine-support explanation.

The external connection is independently visible in firewall and endpoint telemetry, and the initiating process is identified as PowerShell.

### Internal Targeting

Beginning at 06:59:46, the activity shifts toward IT-WS-031.

The sequence progresses from a reachability test to SMB resource discovery and then to an attempted ADMIN$ connection.

This movement toward a second endpoint changes the scope of the investigation.

### Attempted Lateral Movement

At 07:02, failed network authentication events appear against IT-WS-031 using sarnold credentials from IT-LT-017.

At this point, the process, network, and authentication datasets independently support the same conclusion: the session attempted to use valid credentials to access another internal system.

No successful secondary authentication is observed.

## Timeline Interpretation

The incident is not established by any one event.

Repeated authentication failures could be user error.

PowerShell could be legitimate administrative work.

Domain discovery could be troubleshooting.

TCP 443 could be normal web traffic.

An SMB connection could be routine support activity.

The concern comes from the order in which the events occur and the way multiple telemetry sources confirm the same progression.

The sequence moves from:

Authentication anomaly  
→ successful access  
→ administrative discovery  
→ unusual external connection  
→ internal host targeting  
→ administrative share attempt  
→ failed authentication against a second endpoint

Taken together, the activity is no longer reasonably consistent with routine help desk troubleshooting.

## Scope at End of Timeline

Confirmed affected asset:

IT-LT-017

Affected account:

sarnold

Secondary system targeted:

IT-WS-031

Confirmed secondary compromise:

None identified

Observed activity:

- credential use
- host discovery
- domain discovery
- network discovery
- PowerShell execution
- unusual outbound HTTPS activity
- internal SMB access attempt
- attempted administrative share connection
- failed lateral authentication

The timeline supports escalation from a medium-severity authentication anomaly to a confirmed security incident involving credential compromise and attempted lateral movement.
