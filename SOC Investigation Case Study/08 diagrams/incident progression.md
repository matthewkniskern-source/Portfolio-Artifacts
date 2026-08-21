# Incident Progression

This diagram summarizes the progression of activity from the initial authentication anomaly through attempted lateral movement and containment.

```mermaid
flowchart TD
    A["06:47<br/>Five failed logons<br/>sarnold / IT-LT-017"]
    B["06:50<br/>Successful interactive logon"]
    C["06:53<br/>PowerShell session begins"]
    D["06:54–06:56<br/>Host, account, domain,<br/>and network discovery"]
    E["06:58<br/>PowerShell initiates<br/>external HTTPS connection"]
    F["06:59<br/>IT-WS-031 identified<br/>and tested for reachability"]
    G["07:00<br/>SMB resource query<br/>against IT-WS-031"]
    H["07:01<br/>ADMIN$ access attempted"]
    I["07:02<br/>Remote authentication fails<br/>against IT-WS-031"]
    J["SOC correlation<br/>confidence increases"]
    K["Containment<br/>IT-LT-017 isolated<br/>sarnold secured"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> J
    J --> K
```

## Interpretation

The investigation does not depend on a single malicious event.

The early activity remains reasonably explainable as normal IT behavior. Confidence changes as the same session progresses from authentication into discovery, unusual external communication, and attempted access to another internal endpoint.

The attempted access to IT-WS-031 is the clearest point where the activity stops fitting a routine help desk explanation.
