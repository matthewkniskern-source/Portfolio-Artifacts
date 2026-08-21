# Evidence Correlation

This diagram shows how separate telemetry sources contribute to the incident finding.

No single evidence source establishes the entire case.

```mermaid
flowchart LR
    subgraph AUTH["Authentication Telemetry"]
        A1["4625<br/>Repeated failed logons"]
        A2["4624<br/>Successful logon"]
        A3["4625<br/>Failed remote logons<br/>against IT-WS-031"]

        A1 --> A2
    end

    subgraph PROC["Process Telemetry"]
        P1["PowerShell execution"]
        P2["whoami / hostname / ipconfig"]
        P3["net / nltest discovery"]
        P4["Invoke-WebRequest"]
        P5["net use ADMIN$"]

        P1 --> P2
        P2 --> P3
        P3 --> P4
        P4 --> P5
    end

    subgraph NET["Network Telemetry"]
        N1["External TCP 443 connection"]
        N2["PowerShell identified<br/>as initiating process"]
        N3["ICMP to IT-WS-031"]
        N4["SMB TCP 445"]
        N5["ADMIN$ connection attempt"]

        N1 --> N2
        N2 --> N3
        N3 --> N4
        N4 --> N5
    end

    A2 --> C["Analyst Correlation"]
    A3 --> C
    P3 --> C
    P4 --> C
    P5 --> C
    N2 --> C
    N5 --> C

    C --> F["True Positive<br/>Credential Compromise<br/>Attempted Lateral Movement"]
```

## Correlation Principle

Authentication telemetry establishes that the account was used.

Process telemetry establishes what occurred during the session.

Network telemetry establishes where that activity communicated and which processes initiated the connections.

The finding becomes defensible when those sources independently support the same progression.
