# SLA and Escalation Model

## Purpose

This diagram shows how priority, service-level timing, waiting states, warning thresholds, exceptions, and escalation interact in the target Enterprise Service Management model.

The intent is to make service commitments visible without reducing SLA management to a simple breach percentage.

The operating principle is:

> **An SLA should drive attention and action before a service commitment is missed.**

---

## Priority Model

Priority is derived from business impact and urgency.

```mermaid
flowchart TD

    A["Incident"]

    B["Impact"]

    C["Urgency"]

    D["Priority Matrix"]

    E["P1"]
    F["P2"]
    G["P3"]
    H["P4"]

    A --> B
    A --> C

    B --> D
    C --> D

    D --> E
    D --> F
    D --> G
    D --> H
```

Representative priority matrix:

| Impact | Urgency | Priority |
| ------ | ------- | -------- |
| High   | High    | P1       |
| High   | Medium  | P2       |
| High   | Low     | P3       |
| Medium | High    | P2       |
| Medium | Medium  | P3       |
| Medium | Low     | P4       |
| Low    | High    | P3       |
| Low    | Medium  | P4       |
| Low    | Low     | P4       |

Priority should reflect business effect rather than requester pressure.

---

## Representative SLA Targets

The following values are illustrative design assumptions for the case study.

| Priority |  Response Target | Resolution Target |
| -------- | ---------------: | ----------------: |
| P1       |       15 minutes |           4 hours |
| P2       |       30 minutes |  8 business hours |
| P3       | 4 business hours |   2 business days |
| P4       |   1 business day |   5 business days |

Actual targets would be finalized with service owners during implementation.

---

## SLA Lifecycle

```mermaid
flowchart LR

    A["Ticket Created"]

    B["SLA Starts"]

    C["Active Work"]

    D{"Approved Waiting State?"}

    E["Pause / Policy Treatment"]

    F["Resume"]

    G["Resolved"]

    H["SLA Stops"]

    A --> B
    B --> C

    C --> D

    D -->|"No"| C
    D -->|"Yes"| E

    E --> F
    F --> C

    C --> G
    G --> H
```

SLA behavior should be explicitly defined for each workflow state.

---

## SLA State Behavior

| State             | Typical SLA Behavior      |
| ----------------- | ------------------------- |
| New               | Running                   |
| Assigned          | Running                   |
| In Progress       | Running                   |
| Waiting on User   | Paused if policy permits  |
| Waiting on Vendor | Defined by service policy |
| Scheduled         | Defined by service policy |
| Resolved          | Stopped                   |
| Closed            | Stopped                   |

The platform should not allow arbitrary pause behavior simply to protect performance numbers.

---

## Escalation Thresholds

```mermaid
flowchart LR

    A["SLA Active"]

    B["50%"]

    C["Normal Monitoring"]

    D["75%"]

    E["Support Group Warning"]

    F["90%"]

    G["Lead Escalation"]

    H["100%"]

    I["Breach"]

    J["Service Owner / Management Review"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> J
```

Representative thresholds:

* **50%** — normal monitoring
* **75%** — support group warning
* **90%** — lead or supervisor escalation
* **100%** — breach and service-owner visibility

P1 incidents may use more aggressive escalation.

---

## Functional vs Hierarchical Escalation

```mermaid
flowchart TD

    A["Escalation Needed"]

    B{"What is missing?"}

    C["Technical Capability"]

    D["Management Attention / Authority"]

    E["Functional Escalation"]

    F["Hierarchical Escalation"]

    A --> B

    B -->|"Expertise"| C
    B -->|"Priority / Resources / Risk"| D

    C --> E
    D --> F
```

### Functional Escalation

Used when deeper or different technical capability is required.

### Hierarchical Escalation

Used when management attention, authority, prioritization, or resource decision is required.

These are different problems and should not be treated as the same escalation.

---

## Ownership During Escalation

```mermaid
flowchart LR

    A["Current Owner"]

    B["Escalation"]

    C["Additional Expertise / Authority"]

    D["Owner Retained Unless Explicitly Reassigned"]

    A --> B
    B --> C
    C --> D
```

Escalation increases attention.

It does not automatically transfer responsibility.

---

## P1 Escalation

```mermaid
flowchart TD

    A["P1 Created"]

    B["Immediate Assignment"]

    C["Major Incident Coordination"]

    D["Technical Lead"]

    E["Service Owner"]

    F["Management / Communications"]

    G["Vendor if Required"]

    H["Recovery"]

    A --> B
    B --> C

    C --> D
    C --> E
    C --> F
    C --> G

    D --> H
    E --> H
    F --> H
    G --> H
```

For a P1, escalation begins immediately rather than waiting for a late-stage SLA threshold.

---

## Waiting on User

```mermaid
flowchart TD

    A["Information Required"]

    B["Waiting on User"]

    C["Owner Retained"]

    D["Reminder"]

    E{"Response?"}

    F["Resume Work"]

    G["Follow Closure / Cancellation Policy"]

    A --> B
    B --> C
    C --> D
    D --> E

    E -->|"Yes"| F
    E -->|"No"| G
```

An approved pause should still remain visible in reporting.

---

## Waiting on Vendor

```mermaid
flowchart TD

    A["Vendor Dependency"]

    B["Waiting on Vendor"]

    C["Internal Owner Retained"]

    D["Vendor Follow-Up"]

    E["Vendor Escalation"]

    F["Response"]

    G["Resume Work"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
```

Vendor wait should not become a place where tickets disappear from operational attention.

---

## SLA Exception

```mermaid
flowchart TD

    A["SLA Exception Requested"]

    B["Business Reason Required"]

    C["Authorized Reviewer"]

    D{"Approved?"}

    E["Exception Recorded"]

    F["Normal SLA Treatment"]

    G["Reporting Retains Exception"]

    A --> B
    B --> C
    C --> D

    D -->|"Yes"| E
    D -->|"No"| F

    E --> G
```

An SLA exception should include:

* authorized decision
* documented reason
* affected record or service
* timing
* audit history

It should remain reportable.

---

## Priority Override

```mermaid
flowchart TD

    A["Calculated Priority"]

    B{"Override Needed?"}

    C["Continue Calculated Priority"]

    D["Authorized Override"]

    E["Reason Required"]

    F["Old / New Priority Logged"]

    G["Continue Workflow"]

    A --> B

    B -->|"No"| C
    B -->|"Yes"| D

    D --> E
    E --> F
    F --> G
```

Repeated priority overrides should trigger review of either:

* the priority model
* service context
* training
* requester-pressure behavior

---

## SLA and Approval Time

Approval delay should be visible rather than automatically hidden.

```mermaid
flowchart LR

    A["Request Submitted"]

    B["Approval Required"]

    C["Approval Time"]

    D["Fulfillment Time"]

    E["Total Service Experience"]

    A --> B
    B --> C
    C --> D
    D --> E
```

Approval and fulfillment may have different service expectations.

Separating them allows the organization to understand where delay is actually occurring.

---

## Escalation Decision Model

```mermaid
flowchart TD

    A["Ticket at Risk"]

    B{"Why?"}

    C["Technical Blocker"]

    D["Owner / Routing Problem"]

    E["SLA Risk"]

    F["Vendor Delay"]

    G["Priority / Resource Conflict"]

    H["Functional Escalation"]

    I["Ownership Review"]

    J["Hierarchical Escalation"]

    K["Vendor Escalation"]

    A --> B

    B --> C
    B --> D
    B --> E
    B --> F
    B --> G

    C --> H
    D --> I
    E --> J
    F --> K
    G --> J
```

Escalation should match the actual cause of the delay.

---

## SLA Performance Interpretation

SLA metrics should be interpreted with related measures.

Example:

```mermaid
flowchart LR

    A["SLA Compliance Improves"]

    B["SLA Exceptions Increase"]

    C["Review Required"]

    A --> C
    B --> C
```

Another example:

```mermaid
flowchart LR

    A["Resolution Time Improves"]

    B["Reopen Rate Increases"]

    C["Review Resolution Quality"]

    A --> C
    B --> C
```

A green dashboard does not automatically mean the service improved.

---

## SLA Performance Feedback

```mermaid
flowchart TD

    A["SLA Data"]

    B["Compliance"]
    C["Breach"]
    D["Exceptions"]
    E["Pause Time"]
    F["Vendor Wait"]

    G["Trend Analysis"]

    H["Root Cause"]

    I["Service Improvement"]

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F

    B --> G
    C --> G
    D --> G
    E --> G
    F --> G

    G --> H
    H --> I
```

The purpose of SLA measurement is to improve service performance.

It is not to make the dashboard look better.

---

## SLA and Escalation Principle

The model can be reduced to three rules:

1. **Priority should reflect business impact and urgency.**
2. **Escalation should happen before failure where possible.**
3. **Exceptions should remain visible rather than improve the metric by hiding the problem.**

The SLA is useful when it helps the organization act.

> **Measure the commitment, expose the risk, and escalate while there is still time to do something about it.**
