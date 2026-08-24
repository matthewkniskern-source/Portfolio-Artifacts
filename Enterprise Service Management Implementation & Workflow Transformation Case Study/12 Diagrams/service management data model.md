# Service Management Data Model

## Purpose

This diagram shows the core data relationships that support the target Enterprise Service Management operating model.

The goal is not to model every possible platform object.

The goal is to capture the relationships needed to support:

* service ownership
* ticket context
* approvals
* change traceability
* vendor accountability
* knowledge reuse
* reporting
* automation

The design principle is:

> **Capture relationships that support real decisions. Do not collect data just because the platform has a field for it.**

---

## Core Data Model

```mermaid id="h8vszw"
erDiagram

    USER ||--o{ TICKET : submits
    SERVICE ||--o{ TICKET : supports
    SUPPORT_GROUP ||--o{ TICKET : owns

    TICKET }o--o{ ASSET : references
    TICKET }o--o{ CONFIGURATION_ITEM : affects

    SERVICE ||--o{ CONFIGURATION_ITEM : includes

    TICKET }o--o{ CHANGE : related_to
    CHANGE }o--o{ CONFIGURATION_ITEM : affects
    CHANGE }o--o{ SERVICE : impacts

    TICKET }o--o{ KNOWLEDGE_ARTICLE : uses

    TICKET ||--o{ APPROVAL : requires
    CHANGE ||--o{ APPROVAL : requires

    VENDOR ||--o{ TICKET : supports
    VENDOR ||--o{ CHANGE : performs

    SERVICE ||--o{ SUPPORT_GROUP : supported_by

    USER {
        string user_id
        string name
        string department
        string role
        string status
    }

    TICKET {
        string ticket_id
        string type
        string priority
        string status
        string owner
        datetime created
        datetime resolved
    }

    SERVICE {
        string service_id
        string service_name
        string owner
        string criticality
        string status
    }

    SUPPORT_GROUP {
        string group_id
        string group_name
        string group_owner
        string status
    }

    ASSET {
        string asset_id
        string asset_type
        string assigned_user
        string status
    }

    CONFIGURATION_ITEM {
        string ci_id
        string ci_type
        string ci_name
        string owner
        string status
    }

    CHANGE {
        string change_id
        string change_type
        string risk
        string status
        string outcome
    }

    KNOWLEDGE_ARTICLE {
        string article_id
        string title
        string owner
        string status
        datetime review_date
    }

    APPROVAL {
        string approval_id
        string approver
        string decision
        datetime decision_time
    }

    VENDOR {
        string vendor_id
        string vendor_name
        string sponsor
        string status
    }
```

---

## Relationship View

```mermaid id="l7nmi6"
flowchart LR

    U["User"]

    T["Ticket"]

    S["Service"]

    SG["Support Group"]

    A["Asset"]

    CI["Configuration Item"]

    CH["Change"]

    K["Knowledge"]

    AP["Approval"]

    V["Vendor"]

    U -->|"submits"| T
    S -->|"provides context"| T
    SG -->|"owns"| T

    T -->|"references"| A
    T -->|"affects"| CI

    S -->|"contains / depends on"| CI

    T -->|"related to"| CH
    CH -->|"affects"| CI
    CH -->|"impacts"| S

    T -->|"uses"| K

    T -->|"requires"| AP
    CH -->|"requires"| AP

    V -->|"supports"| T
    V -->|"performs work on"| CH
```

---

## Core Entity Roles

| Entity             | Purpose                                                    |
| ------------------ | ---------------------------------------------------------- |
| User               | Identifies requester, affected user, approver, or operator |
| Ticket             | Authoritative service record                               |
| Service            | Connects work to a business or technical service           |
| Support Group      | Establishes operational ownership                          |
| Asset              | Represents owned physical or logical asset                 |
| Configuration Item | Represents managed service-supporting component            |
| Change             | Tracks authorized production modification                  |
| Knowledge Article  | Supports repeatable troubleshooting and fulfillment        |
| Approval           | Captures decision authority and evidence                   |
| Vendor             | Represents external dependency or service provider         |

---

## Ticket-Centered View

The ticket is the operational center of the service-management model.

```mermaid id="pn19k7"
flowchart TD

    T["Ticket"]

    U["Requester / Affected User"]
    S["Service"]
    SG["Owning Support Group"]
    A["Asset"]
    CI["Configuration Item"]
    CH["Related Change"]
    K["Knowledge Article"]
    AP["Approval"]
    V["Vendor"]

    U --> T
    S --> T
    SG --> T

    T --> A
    T --> CI
    T --> CH
    T --> K
    T --> AP
    T --> V
```

The ticket should contain enough context to answer:

* who is affected
* what service is affected
* who owns the work
* what asset or CI is involved
* whether a change is related
* whether approval is required
* whether a vendor is involved
* whether knowledge was used

---

## Service-Centered View

```mermaid id="9xgozd"
flowchart TD

    S["Service"]

    O["Service Owner"]
    SG["Support Groups"]
    CI["Configuration Items"]
    T["Tickets"]
    CH["Changes"]
    SLA["SLA / Performance"]

    O --> S

    S --> SG
    S --> CI
    S --> T
    S --> CH
    S --> SLA
```

The Service entity provides the business context that isolated tickets often lack.

It supports questions such as:

* Which service is being affected?
* Who owns that service?
* Which support teams are responsible?
* Which CIs support it?
* Which changes affected it?
* How is the service performing?

---

## Asset vs Configuration Item

Asset and Configuration Item are related concepts but serve different purposes.

```mermaid id="1snt70"
flowchart LR

    A["Asset"]

    B["Ownership / Cost / Assignment"]

    C["Configuration Item"]

    D["Service Relationship / Dependency / Operational Context"]

    A --> B
    C --> D

    A -. "May also be" .-> C
```

### Asset

Primarily answers:

* What do we own?
* Who is it assigned to?
* What is its lifecycle status?

### Configuration Item

Primarily answers:

* What supports the service?
* What is affected?
* What changed?
* What operational dependency exists?

Not every asset needs to become a fully managed CI.

Not every CI is necessarily a traditional physical asset.

---

## Change Relationship Model

```mermaid id="st5hcc"
flowchart LR

    CH["Change"]

    S["Service"]
    CI["Configuration Item"]
    I["Incident"]
    AP["Approval"]
    V["Vendor"]

    CH -->|"impacts"| S
    CH -->|"modifies"| CI
    CH -->|"may cause / resolve"| I
    CH -->|"requires"| AP
    CH -->|"may involve"| V
```

This structure supports:

* change-impact analysis
* failed-change investigation
* incident correlation
* vendor accountability
* approval history

A failed change should be traceable to the service and technical components it affected.

---

## Approval Relationship Model

Approvals should exist as structured decision records.

```mermaid id="v3w54h"
flowchart TD

    R["Request / Change"]

    A["Approval Record"]

    P["Approver"]

    D["Decision"]

    E["Evidence"]

    R --> A
    P --> A
    A --> D
    A --> E
```

An approval record should retain:

* parent record
* approver
* authority context
* decision
* timestamp
* comments where required

The approval should not survive as an isolated email with no connection to the transaction it authorized.

---

## Vendor Relationship Model

```mermaid id="tnwjsy"
flowchart TD

    V["Vendor"]

    S["Internal Sponsor / Owner"]

    T["Ticket"]

    CH["Change"]

    VA["Temporary Access"]

    V --> S
    V --> T
    V --> CH
    V --> VA

    S --> T
    S --> CH
    S --> VA
```

External activity should remain linked to internal accountability.

The vendor may perform the work.

The organization still owns the service outcome.

---

## Knowledge Relationship Model

```mermaid id="3c1ql2"
flowchart LR

    K["Knowledge Article"]

    I["Incident"]

    R["Service Request"]

    S["Service"]

    U["User / Technician"]

    K --> I
    K --> R
    K --> S
    U --> K
```

Knowledge relationships support:

* troubleshooting
* repeatable fulfillment
* self-service
* knowledge-gap analysis
* article usefulness reporting

---

## Data Relationship Principles

The target model follows several rules.

### Relationships Should Support Decisions

A relationship should help answer a useful operational question.

### Ownership Must Be Visible

Active services, support groups, and managed records should have a valid accountable owner.

### History Must Be Preserved

Changes in:

* ownership
* approval
* status
* configuration
* relationship

should not rewrite the historical record.

### Inactive Data Should Not Drive New Work

Inactive:

* support groups
* vendors
* services
* approvers
* configuration items

should normally be unavailable for new transactions.

Historical relationships should remain visible.

---

## Data Quality Dependencies

```mermaid id="wkr82h"
flowchart TD

    D["Reliable Data"]

    R["Accurate Routing"]
    A["Useful Automation"]
    REP["Reliable Reporting"]
    AI["Useful AI Assistance"]
    GOV["Effective Governance"]

    D --> R
    D --> A
    D --> REP
    D --> AI
    D --> GOV
```

Weak source data creates downstream problems.

For example:

```text id="v0ixzl"
Missing Service Ownership
        ↓
Routing Failure
        ↓
Manual Reassignment
        ↓
Higher Resolution Time
        ↓
Unreliable Reporting
```

Data governance is therefore part of service management, not simply an administrative cleanup function.

---

## Reporting Relationship

The data model enables reporting across:

```text id="cv1yvh"
User
  ↓
Ticket
  ↓
Service
  ↓
Support Group
  ↓
Asset / CI
  ↓
Change
  ↓
Vendor / Approval / Knowledge
```

That supports questions such as:

* Which services generate the most incidents?
* Which groups receive the most reassignment?
* Which CIs are linked to repeated failures?
* Which changes create incidents?
* Which vendors are associated with service delay?
* Which knowledge articles are actually used?
* Which approvals are aging?
* Which services have weak ownership?

---

## Model Boundary

This is intentionally a **service-management data model**, not a full enterprise CMDB.

The case study does not attempt to model:

* every technical dependency
* every network relationship
* every software component
* every contract attribute
* every financial asset field

Those may become appropriate in a mature implementation.

The initial design captures enough structure to support the workflows and decisions defined in this case study.

---

## Target Data Principle

The service-management data model can be summarized as:

> **People → Work → Services → Technology → Decisions → Outcomes**

The value does not come from how many entities the platform can store.

It comes from whether the relationships between those entities help the organization understand and manage the service.
