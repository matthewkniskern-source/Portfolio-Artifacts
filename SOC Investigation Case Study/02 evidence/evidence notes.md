# Evidence Notes

## Purpose

The evidence package is built to support the investigation, not to hand the reader the answer.

Each dataset contains a mix of routine enterprise activity and incident-relevant events. The intent is to recreate the basic problem an analyst would face in a normal SOC queue: most of what the environment produces is expected, individual events can be misleading, and the useful information starts to appear when multiple sources are put together.

The evidence should therefore be read as a connected set rather than as three independent lists of suspicious activity.

## Evidence Files

The case uses three primary datasets:

- authentication-events.csv
- process-events.csv
- network-connections.csv

Together they represent the core telemetry available to the analyst during the initial investigation.

### Authentication Events

authentication-events.csv contains successful and failed Windows authentication activity from the investigation window.

The dataset includes routine employee logons, service account activity, isolated password failures, normal failed-then-successful user authentication, and the activity involving sarnold.

This matters because Event 4625 by itself is not unusual enough to establish compromise. Users mistype passwords, services retry old credentials, and authentication failures occur regularly in a working environment.

The incident-relevant pattern begins with five failed interactive logons for sarnold from IT-LT-017 between 06:47:09 and 06:48:21.

A successful interactive logon follows at 06:50:54.

Later, failed network authentication attempts involving the same account and source device appear against IT-WS-031.

Those later events become substantially more important once they are correlated with process and network telemetry.

### Process Events

process-events.csv represents process creation telemetry from IT-LT-017 during the same investigation window.

Normal operating system, Microsoft Defender, browser, inventory, update, and user-session processes are included alongside the activity being investigated.

Following the successful sarnold authentication, PowerShell starts at 06:53:42.

The subsequent command sequence includes:

- current user identification
- hostname identification
- network configuration review
- domain account queries
- domain trust discovery
- network resource discovery
- active connection review

None of those commands automatically establishes malicious behavior.

That distinction matters in this case because sarnold is a help desk technician. PowerShell, command-line utilities, domain queries, and network troubleshooting are all reasonable tools for the role.

The concern comes from sequence and context rather than from the existence of PowerShell itself.

At 06:58:03, a new PowerShell process initiates an HTTPS request to an external destination and writes the returned content to a public user directory.

Activity then shifts toward IT-WS-031 through network discovery, reachability testing, remote resource queries, and an attempted connection to the system's administrative share.

## Network Connections

network-connections.csv represents normalized firewall and endpoint network telemetry associated with IT-LT-017.

The dataset includes normal DNS, Microsoft cloud, Windows Update, Defender, browser, inventory, Kerberos, LDAP, and internal management traffic.

This background traffic is intentional. An outbound connection on TCP 443 is normal enough that the port alone provides very little value to an analyst.

The relevant connection occurs at 06:58:03 when IT-LT-017 establishes an outbound HTTPS session to 198.51.100.42.

Firewall telemetry identifies the network connection, while endpoint telemetry independently associates that connection with powershell.exe.

That process attribution is what materially changes the value of the event.

The network evidence also documents the progression toward IT-WS-031:

- ICMP reachability testing
- SMB resource access
- an ADMIN$ connection attempt
- authentication-related traffic associated with the failed logons

When combined with the authentication and process datasets, those events support the conclusion that the activity progressed beyond local system discovery into attempted lateral movement.

## Evidence Format Note

The evidence files in this case study are normalized synthetic datasets designed to represent the types of authentication, process, endpoint, and network telemetry that could reasonably be available in a moderately mature Windows enterprise environment.

The CSV files are not intended to reproduce the exact native schema, field order, or export format of a specific SIEM, EDR, firewall, or Microsoft security product.

Fields have been normalized to keep the investigation readable while preserving realistic relationships between timestamps, accounts, hosts, processes, authentication activity, and network behavior.

Where applicable, Windows event IDs and process behaviors are based on documented Windows and Microsoft security telemetry. All users, systems, addresses, and incident activity in the case are fictional.

The external address 198.51.100.42 is drawn from address space reserved for documentation and is used only as a synthetic destination within the case.

## Evidence Boundaries

The available evidence is intentionally useful without being perfect.

The analyst has enough information to reconstruct the primary sequence of events, but several questions are not answered directly by the datasets.

The evidence does not initially establish:

- who was physically operating IT-LT-017
- how the sarnold credentials were obtained
- whether the account owner was present when the first authentication occurred
- why the shared laptop was powered on and available before the normal help desk shift
- what existed at the external destination beyond the observed request
- whether additional activity occurred outside the available logging window

Those questions should not be filled in with assumptions simply because the final incident disposition is known.

Where the evidence supports a conclusion, the investigation should state it. Where it does not, the issue should remain an investigative gap or become part of the later control review.

## Correlation Points

Several timestamps provide the core anchors for the investigation.

| Time | Evidence | Significance |
|---|---|---|
| 06:47:09-06:48:21 | Authentication | Five failed sarnold logons from IT-LT-017 |
| 06:50:54 | Authentication | Successful interactive sarnold logon |
| 06:53:42 | Process | PowerShell session begins |
| 06:54:07-06:56:13 | Process | Host, domain, and network discovery |
| 06:58:03 | Process / Network | PowerShell initiates unusual external HTTPS connection |
| 06:59:47 | Process / Network | IT-WS-031 reachability test |
| 07:00:09-07:00:12 | Process / Network | Remote SMB resource query |
| 07:01:51-07:01:54 | Process / Network | Administrative share connection attempt |
| 07:02:17-07:02:35 | Authentication / Network | Failed network authentication against IT-WS-031 |
| 07:34:08 | Authentication | sarnold later logs into assigned workstation |

The 07:34:08 event deserves some restraint. It is useful context, but it does not prove that sarnold was not responsible for the earlier activity. It gives the analyst a reason to validate the user's location and normal work pattern rather than treating the later logon as automatic exoneration.

## Analyst Use

The evidence package is intended to support both manual investigation and later automation.

The first pass should be performed as an analyst would reasonably approach the case: isolate the authentication anomaly, identify the affected host and account, establish a timeline, pivot into process activity, review network behavior, and look for evidence that the activity spread beyond the original endpoint.

The automation developed later in the case should reduce repetitive work in that process. It should not replace the judgment required to determine whether the resulting pattern is benign or malicious.

That distinction is central to the case. The useful finding is not that one suspicious command existed somewhere in a CSV. It is that several individually explainable events formed a sequence that became progressively harder to explain as normal IT activity.
