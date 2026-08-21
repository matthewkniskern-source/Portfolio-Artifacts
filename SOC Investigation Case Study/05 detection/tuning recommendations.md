# Detection Tuning Recommendations

## Purpose

The initial authentication rule did what it was supposed to do.

It identified a repeated failed-logon pattern followed by a successful authentication and generated a medium-severity alert for review.

The bigger opportunity is not necessarily to make that first rule more aggressive. It is to improve the way the environment correlates what happens immediately after the authentication event.

The incident shows that several individually explainable behaviors can become meaningful when they occur in sequence.

The recommendations below focus on reducing that gap.

---

## 1. Preserve the Authentication Rule, Improve Context

The existing failed-to-successful authentication rule should remain in place.

Recommended tuning inputs include:

- account role
- source asset
- source subnet
- assigned workstation
- normal work hours
- shared-device status
- recent successful authentication history

The rule should continue to generate a medium-severity alert rather than automatically escalating every repeated failure pattern.

The objective is to give the analyst better context at intake.

### Recommended Improvement

Include asset and identity enrichment directly in the alert:

- user department or role
- whether the account is privileged or administrative
- expected workstation
- whether the source device is shared
- whether the source device is currently assigned
- normal login window for the account

This would have immediately shown that sarnold was a help desk technician using a shared IT asset before normal day-shift activity.

---

## 2. Add Post-Authentication Correlation

The main gap in the existing workflow is that the authentication alert and subsequent endpoint behavior are treated separately.

Create a correlation window after a suspicious successful authentication.

Recommended initial window:

10-15 minutes

Within that window, look for:

- PowerShell execution
- command shell execution
- multiple discovery utilities
- unusual outbound connections
- SMB activity
- administrative share access
- authentication attempts against additional hosts

The goal is not to alert on each behavior independently.

The goal is to increase confidence when several appear together.

---

## 3. Tune PowerShell Detection by Context

PowerShell is expected in the IT environment and should not be treated as inherently malicious.

Generic PowerShell execution alerts would generate unnecessary noise.

Recommended tuning factors:

- account role
- parent process
- command-line content
- destination
- execution timing
- source host
- whether the host normally runs PowerShell
- whether the activity follows an authentication anomaly

Higher-confidence conditions include:

- PowerShell launched shortly after suspicious authentication
- external network access initiated by PowerShell
- file writes to unusual locations
- multiple discovery commands in the same session
- follow-on access to remote systems

This preserves legitimate administrative use while improving detection of suspicious sequences.

---

## 4. Correlate Process and Network Telemetry

The external HTTPS connection became useful only after endpoint telemetry showed that PowerShell initiated it.

That process attribution should be retained wherever possible.

Recommended fields include:

- source host
- user
- process name
- process ID
- parent process
- destination IP
- destination port
- timestamp
- connection direction

Without process attribution, the event looks like ordinary TCP 443 traffic.

With process attribution, it becomes part of the larger incident sequence.

---

## 5. Improve Baseline Awareness for External Destinations

An unfamiliar external destination should not automatically be considered malicious.

However, the SOC should be able to determine whether the destination is normal for the host or user.

Recommended baselines:

- destinations previously contacted by the host
- destinations commonly used by IT systems
- approved administrative services
- known update infrastructure
- sanctioned remote support platforms
- frequently observed cloud services

A destination that is both new to the host and associated with PowerShell activity should receive more scrutiny than normal browser traffic.

---

## 6. Correlate Cross-Host Authentication

The attempted lateral movement becomes clear only when activity from IT-LT-017 is linked to authentication failures on IT-WS-031.

The SIEM should correlate:

- source asset
- user account
- destination asset
- event type
- authentication result
- related SMB or remote-service activity

Recommended rule logic:

```text
IF
    source host has active security alert
AND
    same account attempts authentication to second host
AND
    SMB or administrative-share activity is present
THEN
    increase incident confidence
```

A failed remote authentication is still useful evidence.

It can indicate intent even when lateral movement does not succeed.

---

## 7. Increase Visibility Around Administrative Shares

ADMIN$ and other administrative shares are legitimate Windows features, especially in IT environments.

They should not be blocked or alerted on blindly.

Recommended monitoring should focus on:

- source account
- source host
- destination host
- whether the source normally performs remote administration
- whether the activity follows another suspicious event
- whether the target is normally administered by that source

An ADMIN$ attempt from a shared loaner laptop shortly after suspicious authentication deserves more attention than the same activity from an approved management server.

---

## 8. Add Shared-Device Context to SIEM Enrichment

IT-LT-017 was a shared asset with no active individual assignment.

That limited the value of normal asset ownership data during triage.

Recommended asset fields include:

- shared device indicator
- current custodian
- checkout status
- last assigned user
- physical location
- device purpose
- support ownership

The objective is not to turn asset management into a security control by itself.

The objective is to make shared-device ambiguity visible to the analyst instead of discovering it manually halfway through the case.

---

## 9. Baseline Administrative Accounts Separately

Administrative and help desk accounts behave differently from standard users.

The detection model should account for that.

Recommended baselines include:

- normal source workstations
- typical administrative tools
- normal working hours
- common remote targets
- expected subnets
- normal PowerShell frequency
- expected use of SMB and administrative shares

This should reduce false positives while making unusual combinations easier to identify.

For example:

PowerShell from sarnold is normal.

PowerShell from sarnold on an unassigned shared laptop before normal shift, followed by unusual egress and ADMIN$ activity, is not the same thing.

---

## 10. Improve Alert Enrichment Before Analyst Review

The original alert could be made more useful without changing the detection threshold.

Recommended enrichment fields:

- user role
- privileged status
- usual workstation
- source device assignment
- source device location
- recent login history
- recent PowerShell activity
- recent external destinations
- related alerts on the same host
- related authentication attempts to other systems

That would allow the analyst to make a better first-pass decision without manually searching several tools.

---

## 11. Avoid Automatic Containment on the Initial Signal

The first authentication alert should not automatically isolate IT-LT-017 or disable sarnold.

The initial evidence is too ambiguous.

Automatic containment becomes more reasonable only after multiple signals are present.

Potential containment threshold:

- authentication anomaly
- suspicious post-authentication process activity
- unusual external connection
- attempted access to second endpoint

Even then, organizational policy should determine whether the response is automatic or requires analyst approval.

For this environment, analyst validation remains the better choice.

---

## 12. Expand Search Windows After Confirmation

Initial triage should stay narrow to reduce noise.

Once compromise is confirmed, the search window should expand.

Recommended follow-up searches:

- earlier sarnold authentication activity
- other hosts accessed by sarnold
- other systems contacting the same external destination
- earlier PowerShell activity on IT-LT-017
- other ADMIN$ attempts from IT-LT-017
- additional failed authentication against internal systems

This keeps the first pass efficient while allowing scope to expand when the evidence justifies it.

---

## 13. Preserve Detection Explainability

Correlation rules should remain understandable to the analyst.

A detection should be able to explain why the score or severity increased.

For example:

```text
+25  repeated authentication failures followed by success
+10  PowerShell within five minutes
+15  multiple discovery commands
+25  unusual external PowerShell connection
+20  ADMIN$ attempt
+25  authentication attempt against second host
```

The exact values require production tuning.

The important part is that the analyst can see what drove the result.

A black-box score that cannot be explained adds less value during incident review.

---

## Recommended Priority

### High Priority

- correlate suspicious authentication with post-login process activity
- retain process-to-network attribution
- correlate cross-host authentication with SMB activity
- enrich alerts with user and asset context

### Medium Priority

- baseline administrative accounts separately
- baseline expected external destinations
- improve administrative-share monitoring
- include shared-device status in asset enrichment

### Longer-Term Improvement

- integrate device custody data where practical
- automate related-host and related-account searches
- develop confidence-based correlation scoring
- evaluate limited SOAR-assisted containment after rule maturity improves

---

## Expected Outcome

The objective of these recommendations is not to generate more alerts.

It is to make the existing alerts more useful.

A tuned environment should recognize the difference between:

a help desk technician using PowerShell

and:

a help desk account authenticating from an unassigned shared laptop, performing rapid discovery, making an unusual external PowerShell connection, and then attempting ADMIN$ access to another host.

That difference is where the useful signal exists.
