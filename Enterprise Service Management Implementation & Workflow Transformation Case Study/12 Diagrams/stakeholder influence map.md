# Stakeholder Influence Map

## Purpose

This diagram shows the major stakeholder groups involved in the Enterprise Service Management transformation and how their influence changes across design, implementation, governance, and ongoing operation.

The case study assumes that the primary implementation challenge is not simply identifying who participates.

It is defining:

* who requests
* who performs
* who owns
* who approves
* who governs
* who decides

The operating principle is:

> **Responsibility may already exist informally. The target model makes it explicit.**

---

## Stakeholder Landscape

```mermaid
flowchart TD

    E["Executive Sponsor"]

    M["IT Management"]

    PO["Process / Service Owners"]

    SD["Service Desk"]

    ST["Specialist Support Teams"]

    EU["End Users"]

    AP["Approvers"]

    SEC["Security / Risk / Compliance"]

    AC["Asset / CI Owners"]

    V["External Vendors"]

    HR["HR / Identity"]

    PA["Platform Administrators"]

    CH["Champions / Super-Users"]

    E --> M

    M --> PO

    PO --> SD
    PO --> ST
    PO --> AP

    SD --> EU
    ST --> EU

    SEC --> PO
    SEC --> AP

    AC --> PO

    V --> ST

    HR --> AP
    HR --> PA

    PA --> SD
    PA --> ST

    CH --> EU
    CH --> SD
```

This is not intended to represent a strict reporting hierarchy.

It represents influence and operational dependency.

---

## Stakeholder Groups

| Stakeholder                  | Primary Interest                              |
| ---------------------------- | --------------------------------------------- |
| Executive Sponsor            | Business outcome and implementation support   |
| IT Management                | Service performance and operational control   |
| Process / Service Owners     | Process quality and service accountability    |
| Service Desk                 | Intake, triage, ownership, escalation         |
| Specialist Teams             | Technical resolution and fulfillment          |
| End Users                    | Simple access to service and visible status   |
| Approvers                    | Clear, timely decision authority              |
| Security / Risk / Compliance | Control, evidence, access, exceptions         |
| Asset / CI Owners            | Accurate technical relationships              |
| Vendors                      | Defined external responsibilities             |
| HR / Identity                | Joiner, mover, leaver and access context      |
| Platform Administrators      | Configured implementation of approved process |
| Champions                    | Adoption and peer support                     |

---

## Influence and Impact View

```mermaid
quadrantChart
    title Stakeholder Influence and Change Impact
    x-axis Low Influence --> High Influence
    y-axis Low Change Impact --> High Change Impact

    quadrant-1 Manage Closely
    quadrant-2 Engage and Support
    quadrant-3 Monitor
    quadrant-4 Keep Informed

    "Executive Sponsor": [0.90, 0.45]
    "IT Management": [0.85, 0.75]
    "Service Owners": [0.82, 0.88]
    "Service Desk": [0.70, 0.95]
    "Specialist Teams": [0.60, 0.85]
    "Approvers": [0.65, 0.70]
    "Security / Risk": [0.75, 0.55]
    "Platform Admins": [0.72, 0.90]
    "End Users": [0.35, 0.72]
    "Vendors": [0.35, 0.45]
    "Champions": [0.45, 0.78]
```

The exact placement is illustrative.

The purpose is to show that influence and operational impact are not the same thing.

For example:

* end users may have limited design authority but experience meaningful workflow change
* Service Desk personnel have both high operational impact and significant implementation influence
* executives have high decision authority but may interact with the platform very little

---

## Decision Authority

```mermaid
flowchart LR

    A["Executive Sponsor"]

    B["IT Management"]

    C["Process / Service Owner"]

    D["Operational Lead"]

    E["Technician / Resolver"]

    A -->|"Strategic Direction"| B

    B -->|"Policy / Priority"| C

    C -->|"Process Decisions"| D

    D -->|"Operational Coordination"| E
```

Decision authority should be placed at the level where the decision can be made responsibly.

Not every operational question should escalate to management.

Not every governance decision should be left to technicians.

---

## Service Request Stakeholders

```mermaid
flowchart LR

    U["Requester"]

    O["Service Owner"]

    A["Approver"]

    F["Fulfillment Team"]

    P["Platform"]

    U -->|"Submits"| P

    P -->|"Routes"| A

    A -->|"Authorizes"| P

    P -->|"Assigns"| F

    O -->|"Defines Service Rules"| P
```

This model separates:

* requester need
* approval authority
* fulfillment responsibility
* service ownership

---

## Incident Stakeholders

```mermaid
flowchart TD

    U["Affected User"]

    SD["Service Desk"]

    ST["Specialist Team"]

    SO["Service Owner"]

    M["Management"]

    V["Vendor"]

    U --> SD
    SD --> ST

    ST --> V

    SD --> SO
    ST --> SO

    SO --> M
```

The Service Desk coordinates the record.

Specialist teams resolve technical issues.

Service ownership and management become increasingly involved as impact or escalation grows.

---

## Change Stakeholders

```mermaid
flowchart TD

    R["Change Requester"]

    O["Change Owner"]

    S["Service Owner"]

    CA["Change Authority"]

    SEC["Security / Risk"]

    I["Implementer"]

    V["Vendor"]

    R --> O

    O --> S
    O --> CA

    CA --> SEC

    O --> I
    I --> V
```

Higher-risk changes may require broader stakeholder participation.

Routine changes should not require the same decision chain as high-risk production activity.

---

## Governance Stakeholders

```mermaid
flowchart LR

    P["Process Owner"]

    C["Control Owner"]

    S["Security / Risk"]

    A["Auditor / Reviewer"]

    PA["Platform Administrator"]

    P --> C
    C --> S
    S --> A

    C --> PA
```

A useful separation exists between:

* defining the process
* owning the control
* configuring the platform
* reviewing the evidence

One person may fill multiple roles in a smaller organization, but the responsibilities should still remain distinct.

---

## Platform Administration Boundary

```mermaid
flowchart TD

    A["Business / Process Decision"]

    B["Approved Requirement"]

    C["Platform Configuration"]

    D["Testing"]

    E["Production"]

    A --> B
    B --> C
    C --> D
    D --> E
```

Platform administrators should implement approved process decisions.

They should not become the default authority for:

* service ownership
* approval policy
* SLA policy
* access authority
* control exceptions

Configuration capability does not automatically create business authority.

---

## Stakeholder Discovery

Stakeholder discovery should identify:

```mermaid
flowchart TD

    A["Stakeholder"]

    B["What Work Do They Perform?"]

    C["What Decisions Do They Make?"]

    D["What Information Do They Need?"]

    E["What Friction Exists Today?"]

    F["What Changes for Them?"]

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F
```

This helps keep discovery focused on operating behavior rather than feature wish lists.

---

## Adoption Influence

```mermaid
flowchart TD

    A["Leadership"]

    B["Process Owners"]

    C["Service Desk / Support Leads"]

    D["Champions"]

    E["End Users"]

    A --> B
    B --> C
    C --> D
    D --> E
```

Adoption is strongly influenced by visible behavior.

If leaders and support teams continue to bypass the target process, users will learn that the new operating model is optional.

---

## Stakeholder Conflict Example

Different stakeholders may have valid but competing priorities.

```mermaid
flowchart TD

    A["Service Request"]

    B["Requester:<br/>Fast Access"]

    C["Approver:<br/>Business Justification"]

    D["Security:<br/>Least Privilege"]

    E["Support Team:<br/>Efficient Fulfillment"]

    F["Target Workflow"]

    A --> B
    A --> C
    A --> D
    A --> E

    B --> F
    C --> F
    D --> F
    E --> F
```

The target workflow should reconcile those needs rather than simply optimize for the loudest stakeholder.

---

## Stakeholder Engagement by Phase

| Phase          | Primary Stakeholders                                   |
| -------------- | ------------------------------------------------------ |
| Current State  | End Users, Service Desk, Support Teams                 |
| Discovery      | All affected operational and decision roles            |
| Requirements   | Process Owners, Business Analyst, Security, Operations |
| Design         | Process Owners, Platform Team, Support Leads           |
| Governance     | Control Owners, Security, Approvers                    |
| Testing        | Operational Users, UAT Participants                    |
| Implementation | Project Team, Platform Team, Operations                |
| Adoption       | End Users, Managers, Champions                         |
| Optimization   | Process Owners, Service Owners, Management             |

Stakeholder involvement should change as the implementation moves through the lifecycle.

---

## Stakeholder Principle

The target operating model should make responsibility visible enough that the organization can answer:

* Who needs the service?
* Who performs the work?
* Who owns the outcome?
* Who approves the decision?
* Who governs the risk?
* Who can change the platform?
* Who reviews whether the process is working?

The goal is not to create more roles.

It is to remove ambiguity from the roles that already exist.

> **Clear ownership makes escalation easier, governance stronger, and implementation decisions easier to defend.**
