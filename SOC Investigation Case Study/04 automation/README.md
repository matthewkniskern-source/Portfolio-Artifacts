# Security Automation

## Purpose

The automation in this section takes the repetitive parts of the manual SOC investigation and turns them into reusable PowerShell utilities.

The goal is not to automate the incident decision.

Each script handles a specific part of the workflow:

1. collect host evidence
2. identify authentication patterns worth reviewing
3. package investigation evidence with integrity hashes

The analyst still decides what the activity means.

That separation is intentional. Automation should reduce the time spent gathering and filtering data without hiding the evidence or replacing analyst judgment.

---

## Scripts

### Collect-HostTriage.ps1

Collect-HostTriage.ps1 gathers a focused first-pass evidence package from a Windows endpoint.

Collected data includes:

- host identity
- logged-on users
- network configuration
- running processes
- active TCP connections
- Event 4624 successful logons
- Event 4625 failed logons
- Event 4688 process creation
- combined security event timeline
- network neighbor information

The script accepts a defined investigation window so the analyst can collect data relevant to the incident without exporting an unnecessarily large volume of unrelated events.

### Case Study Example

```powershell
.\Collect-HostTriage.ps1 `
    -StartTime "2026-08-17 06:45:00" `
    -EndTime "2026-08-17 07:05:00" `
    -OutputPath ".\SOC-2026-0817-0042"
```

### Output

The script creates structured CSV files and a collection manifest inside the specified output directory.

Example:

```text
SOC-2026-0817-0042/
├── authentication-events.csv
├── host-information.csv
├── logged-on-users.csv
├── network-configuration.csv
├── network-neighbors.csv
├── process-events.csv
├── running-processes.csv
├── security-timeline.csv
├── tcp-connections.csv
└── collection-manifest.txt
```

---

## Find-SuspiciousLogons.ps1

Find-SuspiciousLogons.ps1 reviews normalized authentication data for repeated failed logons followed by a successful authentication from the same account and source asset.

The threshold and time window are configurable.

The script does not determine whether the activity is malicious.

It identifies patterns that deserve analyst review.

### Case Study Example

```powershell
.\Find-SuspiciousLogons.ps1 `
    -Path "..\02 evidence\authentication-events.csv" `
    -FailureThreshold 5 `
    -WindowMinutes 5 `
    -OutputPath ".\output\suspicious-logons.csv"
```

For the synthetic incident, the script identifies the sarnold activity from IT-LT-017 because five failed authentication events are followed by a successful logon within the configured window.

Other failed-successful authentication pairs exist in the dataset.

Those routine events are included deliberately. A useful authentication rule should identify patterns for investigation rather than treating every mistyped password as an incident.

### Output

Example fields include:

```text
Account
SourceAsset
SourceIP
FailureCount
FirstFailure
LastFailure
SuccessfulLogon
ElapsedSeconds
LogonType
TargetAsset
Pattern
```

---

## Export-InvestigationEvidence.ps1

Export-InvestigationEvidence.ps1 creates a case-specific evidence package from selected investigation files.

The script:

- validates source evidence
- creates a case directory
- copies selected evidence files
- calculates SHA-256 hashes
- creates an evidence manifest
- writes an export summary

### Case Study Example

```powershell
.\Export-InvestigationEvidence.ps1 `
    -CaseId "SOC-2026-0817-0042" `
    -EvidencePath "..\02 evidence" `
    -OutputRoot ".\exports"
```

### Output

Example:

```text
exports/
└── SOC-2026-0817-0042/
    ├── authentication-events.csv
    ├── process-events.csv
    ├── network-connections.csv
    ├── evidence-notes.md
    ├── evidence-manifest.csv
    └── evidence-package-summary.txt
```

The manifest includes the file name, size, timestamp, and SHA-256 hash for each exported evidence file.

This provides a basic integrity record for the case package.

It is not presented as a forensic acquisition or formal legal chain-of-custody process.

---

## Workflow

The three scripts support a simple investigation sequence:

```text
Alert
  |
  v
Collect-HostTriage.ps1
  |
  v
Focused endpoint evidence
  |
  v
Find-SuspiciousLogons.ps1
  |
  v
Authentication candidates
  |
  v
Analyst correlation and investigation
  |
  v
Export-InvestigationEvidence.ps1
  |
  v
Case evidence package + SHA-256 manifest
```

The scripts intentionally stop short of automated incident disposition.

For example, Find-SuspiciousLogons.ps1 may identify five failures followed by a successful authentication, but it does not label that sequence a credential compromise.

That decision still depends on context such as:

- account role
- source asset
- normal user behavior
- process execution
- network activity
- activity against other systems

In this case, the authentication pattern becomes significant only after it is correlated with PowerShell activity, external network traffic, internal discovery, and attempted access to IT-WS-031.

---

## Design Approach

The scripts are intentionally small and readable.

They use standard PowerShell and Windows interfaces rather than adding unnecessary dependencies.

Common techniques include:

- parameterized investigation windows
- FilterHashtable queries for Windows events
- structured PSCustomObject output
- CSV export
- process-to-network PID correlation
- input validation
- basic exception handling
- configurable detection thresholds
- SHA-256 file hashing

The scripts are written so the investigation logic remains visible.

There is little value in making a short SOC utility look complex simply to make the code appear more advanced.

The better outcome is a tool another analyst can read quickly, understand, modify, and verify.

---

## Automation Boundaries

These utilities are designed for defensive investigation and case organization.

They do not:

- automatically isolate endpoints
- disable user accounts
- terminate sessions
- classify an alert as malicious
- make containment decisions
- perform malware execution or offensive testing
- replace EDR or SIEM functionality
- provide formal forensic acquisition

Those actions either require analyst approval or belong to tooling outside the scope of this case study.

---

## Requirements

The scripts are intended for Windows environments with PowerShell and standard Windows management interfaces available.

Depending on the data being collected, elevated privileges may be required to access the Windows Security event log or certain endpoint information.

Relevant PowerShell cmdlets include:

```text
Get-WinEvent
Get-CimInstance
Get-Process
Get-NetTCPConnection
Get-NetIPConfiguration
Get-NetNeighbor
Get-FileHash
Import-Csv
Export-Csv
```

No third-party PowerShell modules are required.

---

## Case Study Use

Within this incident, the automation supports the same investigation already documented manually.

The progression is deliberate:

Manual investigation establishes what matters.

Automation identifies which parts of that work are repetitive.

The scripts then reduce those repetitive steps without changing the underlying investigative logic.

That makes the automation a supporting part of the SOC workflow rather than a separate scripting exercise.
