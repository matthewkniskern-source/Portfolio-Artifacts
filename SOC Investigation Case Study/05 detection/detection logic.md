# Detection Logic

## Purpose

The initial alert in this case correctly identified an authentication anomaly, but the investigation showed that the more meaningful signal came from activity that occurred after the successful logon.

The detection opportunity is therefore broader than:

Five failed logons followed by one successful logon.

A stronger detection approach should correlate authentication, process, and network behavior over a short period of time and raise confidence as additional indicators appear.

The goal is not to turn every use of PowerShell, SMB, or administrative tooling into an alert.

The goal is to identify when otherwise explainable activity begins to form a sequence that no longer fits normal administrative behavior.

---

## Initial Authentication Detection

The original alert is based on repeated failed authentication attempts followed by a successful logon from the same account and source asset.

### Detection Conditions

Flag for analyst review when:

- the same account records multiple Event 4625 failures
- failures originate from the same source asset
- the configured failure threshold is reached
- Event 4624 follows within a defined time window
- the successful authentication originates from the same source

For this case:

| Detection Parameter | Value |
|---|---|
| Failure Event | 4625 |
| Success Event | 4624 |
| Failure Threshold | 5 |
| Correlation Window | 5 minutes |
| Account | sarnold |
| Source Asset | IT-LT-017 |

The authentication pattern is sufficient for a medium-severity alert.

It is not sufficient by itself to establish credential compromise.

---

## Authentication Detection Concept

```text
IF
    failed_logons >= 5
AND
    same_account = true
AND
    same_source_asset = true
AND
    successful_logon_follows = true
AND
    elapsed_time <= 5 minutes
THEN
    create medium-severity authentication alert
```

The purpose of this rule is to surface the pattern for investigation.

It should not automatically label the account compromised.

---

## Behavioral Correlation

The investigation identified several additional behaviors after the successful authentication.

Within approximately twelve minutes of the successful logon, IT-LT-017 generated:

- PowerShell execution
- user and host discovery
- network configuration discovery
- domain account queries
- domain trust discovery
- network resource discovery
- an unusual PowerShell-initiated external HTTPS connection
- internal host probing
- SMB activity against a second endpoint
- an attempted ADMIN$ connection
- failed authentication against that endpoint

That sequence presents a stronger detection opportunity than any individual event.

---

## Correlation Model

A practical model can assign increasing confidence as related behaviors appear within a defined time window.

### Stage 1 - Authentication Anomaly

Observed:

- repeated Event 4625 failures
- Event 4624 success
- same account
- same source

Suggested severity:

Medium

### Stage 2 - Administrative Discovery

Observed shortly after authentication:

- powershell.exe
- whoami.exe
- hostname.exe
- ipconfig.exe
- net.exe
- nltest.exe

Suggested action:

Increase investigative priority but do not automatically escalate severity.

For an IT account, these processes may be legitimate.

### Stage 3 - Unusual External Process Connection

Observed:

- PowerShell initiates outbound TCP 443
- destination is not part of normal observed host activity
- activity follows authentication anomaly and discovery

Suggested severity:

Medium to High depending on destination context and environment baseline.

### Stage 4 - Internal Targeting

Observed:

- reachability testing against another endpoint
- SMB connection
- remote resource enumeration
- ADMIN$ access attempt

Suggested severity:

High when correlated with the earlier authentication and PowerShell activity.

### Stage 5 - Remote Authentication Attempt

Observed:

- Event 4625 against a second endpoint
- same account
- same source device
- timing matches the preceding ADMIN$ attempt

Suggested disposition:

Escalate for suspected credential compromise and attempted lateral movement.

---

## Detection Chain

```text
Repeated Authentication Failures
        |
        v
Successful Authentication
        |
        v
PowerShell / Administrative Discovery
        |
        v
Unusual External Connection
        |
        v
Internal Host Targeting
        |
        v
SMB / ADMIN$ Attempt
        |
        v
Remote Authentication Failure
        |
        v
High-Confidence Incident Candidate
```

The strength of the detection comes from progression rather than any single tool or event.

---

## Example Authentication Query

The following KQL-style example demonstrates the basic failed-logon followed by successful-logon concept.

It is provided as representative detection logic rather than as a production-ready rule for a specific SIEM deployment.

```kusto
let FailureThreshold = 5;
let Window = 5m;

let FailedLogons =
    SecurityEvent
    | where EventID == 4625
    | summarize
        FailureCount = count(),
        FirstFailure = min(TimeGenerated),
        LastFailure = max(TimeGenerated)
        by Account, Computer
    | where FailureCount >= FailureThreshold;

let SuccessfulLogons =
    SecurityEvent
    | where EventID == 4624
    | project
        SuccessTime = TimeGenerated,
        Account,
        Computer;

FailedLogons
| join kind=inner SuccessfulLogons on Account, Computer
| where SuccessTime > LastFailure
| where SuccessTime <= FirstFailure + Window
| project
    Account,
    Computer,
    FailureCount,
    FirstFailure,
    LastFailure,
    SuccessTime
```

The query identifies candidate authentication patterns.

It does not determine whether those patterns are malicious.

---

## Example PowerShell Discovery Logic

PowerShell should not be treated as inherently suspicious.

A better approach is to look for PowerShell activity followed by multiple discovery utilities within a short period.

```kusto
SecurityEvent
| where EventID == 4688
| where NewProcessName has_any (
    "powershell.exe",
    "whoami.exe",
    "hostname.exe",
    "ipconfig.exe",
    "net.exe",
    "nltest.exe"
)
| summarize
    ProcessCount = count(),
    Processes = make_set(NewProcessName)
    by Account, Computer, bin(TimeGenerated, 5m)
| where ProcessCount >= 4
```

In an environment with active administrative users, this result should normally be correlated with account role and surrounding telemetry before escalation.

---

## Example PowerShell Network Correlation

Where endpoint telemetry includes process-to-network attribution, the detection can look for PowerShell initiating outbound connections to destinations not already established as expected.

Conceptually:

```text
IF
    process = powershell.exe
AND
    direction = outbound
AND
    destination = external
AND
    destination_not_baselined = true
AND
    recent_authentication_anomaly = true
THEN
    increase alert confidence
```

The destination itself should not be labeled malicious simply because it is unfamiliar.

Process, timing, user context, and previous host behavior matter.

---

## Lateral Movement Detection

The strongest correlation in this case occurs when activity begins targeting IT-WS-031.

Relevant indicators include:

- ping or other reachability testing
- TCP 445 connection attempts
- net view against the remote host
- ADMIN$ access
- authentication attempts using the same account

Conceptually:

```text
IF
    source_host = previously alerted host
AND
    target_host != source_host
AND
    SMB_activity = true
AND
    administrative_share_attempt = true
AND
    remote_authentication_event = true
THEN
    escalate for suspected lateral movement
```

A failed authentication still matters.

It establishes that the account was used against another endpoint even though access was not successful.

---

## Recommended Multi-Signal Detection

The most useful improvement is a correlation rule that combines several moderate-confidence signals.

Example scoring model:

| Behavior | Score |
|---|---:|
| 5+ failed logons followed by success | 25 |
| PowerShell shortly after authentication | 10 |
| Multiple discovery commands | 15 |
| Unusual PowerShell external connection | 25 |
| SMB activity toward second endpoint | 15 |
| ADMIN$ attempt | 20 |
| Authentication attempt against second endpoint | 25 |

Example thresholds:

| Score | Action |
|---|---|
| 0-24 | Retain telemetry / no escalation |
| 25-49 | Medium alert |
| 50-74 | High-priority analyst review |
| 75+ | High-confidence incident candidate |

This model is illustrative.

A production implementation would require tuning against actual environment behavior before these thresholds should be trusted.

The value is in combining evidence rather than assigning absolute meaning to any one event.

---

## False Positive Considerations

The same behaviors observed in this case can occur legitimately.

Potential benign explanations include:

- help desk troubleshooting
- account lockout resolution
- scripted administration
- software deployment
- network troubleshooting
- domain diagnostics
- remote support
- administrative share access

That is especially relevant because the affected account belongs to IT.

Useful tuning inputs include:

- account role
- approved administrative systems
- assigned workstation
- source subnet
- normal work hours
- known scripts
- approved external destinations
- change and support tickets
- frequency of similar behavior

A detection that ignores this context will generate noise quickly.

---

## Detection Gaps Identified

The incident exposes several areas where additional context would improve detection quality.

### Shared Asset Attribution

IT-LT-017 was not assigned to a specific individual.

Asset ownership data therefore provided limited help during triage.

Improvement:

Correlate shared-device checkout or custody information where practical.

### Administrative Account Baseline

sarnold legitimately uses administrative tools.

Improvement:

Develop account and device baselines that distinguish expected IT administration from unusual location, timing, or sequence.

### Process-to-Network Correlation

The external connection became significant only after endpoint telemetry associated it with PowerShell.

Improvement:

Ensure EDR or equivalent telemetry retains process-to-network attribution.

### Cross-Host Authentication Correlation

The lateral movement attempt became clear when authentication activity from IT-LT-017 was linked to IT-WS-031.

Improvement:

Correlate source host, account, destination host, and process activity across endpoints.

### Physical Context

The SOC telemetry cannot establish who physically operated IT-LT-017.

Improvement:

Treat physical access and shared-device custody as follow-up context where the incident involves an unattended internal asset.

This should remain a supporting control rather than a requirement for initial cyber detection.

---

## Detection Outcome for This Incident

The original authentication rule performed its intended function.

It generated a medium-severity alert worth investigating.

The main opportunity for improvement is not necessarily to make that first alert more severe.

It is to recognize the activity that followed it.

A mature correlation rule should be able to move from:

Authentication anomaly

to:

Authentication anomaly plus suspicious post-authentication behavior

and finally to:

Probable credential compromise with attempted lateral movement.

That progression preserves analyst context while reducing the chance that a meaningful sequence remains scattered across several independent alerts.

## Detection Principle

The case reinforces a simple detection principle:

A common administrative tool is not a finding.

A common network port is not a finding.

A failed password is not a finding.

The value comes from understanding what happened next and whether the combined activity still makes sense.

That is the logic this detection model is intended to preserve.
