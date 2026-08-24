# Requirements Traceability Flow

## Purpose

This diagram shows how the case study maintains traceability from an observed operational problem through requirement definition, solution design, control implementation, validation, and measurement.

The intent is to make sure the implementation can answer a simple question:

> **Why does this requirement exist, how was it addressed, and how will we prove it worked?**

```mermaid
flowchart LR

    FM["Current-State Failure Mode"]

    BR["Business Requirement"]

    FR["Functional Requirement"]
    NFR["Nonfunctional Requirement"]

    DESIGN["Target Design / Workflow"]

    CONTROL["Control / Governance"]

    TEST["Test Case / UAT"]

    METRIC["Operational Metric"]

    OUTCOME["Business Outcome"]

    FM --> BR

    BR --> FR
    BR --> NFR

    FR --> DESIGN
    NFR --> DESIGN

    DESIGN --> CONTROL

    CONTROL --> TEST

    TEST --> METRIC

    METRIC --> OUTCOME
```

---

## Traceability Logic

The traceability chain follows:

```text
Failure Mode
    ↓
Business Requirement
    ↓
Functional / Nonfunctional Requirement
    ↓
Target Design
    ↓
Control
    ↓
Test
    ↓
Metric
    ↓
Business Outcome
```

Each stage serves a different purpose.

| Stage                                  | Question                                              |
| -------------------------------------- | ----------------------------------------------------- |
| Failure Mode                           | What is wrong today?                                  |
| Business Requirement                   | What must the organization achieve?                   |
| Functional / Nonfunctional Requirement | What must the solution do, and under what conditions? |
| Target Design                          | How will the process operate?                         |
| Control                                | How will risk and decision authority be managed?      |
| Test                                   | How will expected behavior be validated?              |
| Metric                                 | How will production performance be measured?          |
| Outcome                                | Did the change improve the operation?                 |

---

## Example 1 — Inconsistent Priority

```mermaid
flowchart LR

    A["FM-03<br/>Subjective Priority"]

    B["BR-03<br/>Consistent Prioritization"]

    C["FR-05<br/>Impact & Urgency"]
    D["FR-06<br/>Calculated Priority"]
    E["FR-07<br/>Controlled Override"]

    F["Priority & SLA Model"]

    G["AC-07<br/>Priority Override Control"]

    H["TC-INC-03<br/>P1 Calculation"]
    I["TC-GOV-05<br/>Override Audit"]

    J["Priority Override Rate"]
    K["SLA / Resolution Performance"]

    A --> B

    B --> C
    B --> D
    B --> E

    C --> F
    D --> F
    E --> F

    F --> G

    G --> H
    G --> I

    H --> J
    I --> J

    J --> K
```

### Intended Outcome

Priority becomes based on business impact and urgency rather than requester pressure or technician interpretation.

---

## Example 2 — Temporary Vendor Access

```mermaid
flowchart LR

    A["FM-12<br/>Vendor Access Persists"]

    B["BR-12<br/>Temporary / Vendor Access Governance"]

    C["FR-25<br/>Required Access Attributes"]
    D["FR-26<br/>Expiration Required"]

    E["Vendor Access Workflow"]

    F["VND-03<br/>Expiration Control"]
    G["AC-03<br/>Approval Authority"]

    H["TC-VND-01<br/>Vendor Access Approval"]
    I["TC-VND-02<br/>Access Expiration"]

    J["Vendor Access Expiration Compliance"]

    K["Reduced Persistent Access Risk"]

    A --> B

    B --> C
    B --> D

    C --> E
    D --> E

    E --> F
    E --> G

    F --> H
    G --> H
    F --> I

    H --> J
    I --> J

    J --> K
```

### Intended Outcome

Temporary access remains:

* sponsored
* approved
* time-bound
* auditable
* accountable to an internal owner

---

## Example 3 — Failed Change Traceability

```mermaid
flowchart LR

    A["FM-10<br/>Failed Change Not Linked to Incident"]

    B["BR-10<br/>Change Traceability"]

    C["FR-20<br/>Change / CI Relationship"]
    D["FR-21<br/>Incident / Change Relationship"]
    E["FR-22<br/>Change Outcome & Validation"]

    F["Change Management Workflow"]

    G["CHG-03<br/>Backout / Recovery"]
    H["CHG-05<br/>Incident Relationship"]

    I["TC-CHG-05<br/>Failed Change"]
    J["TC-CHG-06<br/>Change-Caused Incident"]

    K["Change Failure Rate"]
    L["Incidents Caused by Change"]

    M["Better Change Reliability"]

    A --> B

    B --> C
    B --> D
    B --> E

    C --> F
    D --> F
    E --> F

    F --> G
    F --> H

    G --> I
    H --> J

    I --> K
    J --> L

    K --> M
    L --> M
```

### Intended Outcome

A failed change should not disappear into isolated troubleshooting.

The organization should be able to see:

* what changed
* what failed
* what service was affected
* whether an incident resulted
* what recovery occurred
* whether the same pattern is recurring

---

## Example 4 — Automation Failure

```mermaid
flowchart LR

    A["FM-16<br/>Automation of Weak / Incomplete Decisions"]

    B["BR-16<br/>Controlled Automation"]

    C["FR-32<br/>Approved Automation"]
    D["FR-33<br/>Automation Logging"]
    E["FR-34<br/>Exception Handling"]

    F["Automation Design"]

    G["AUT-01<br/>Validated Rule"]
    H["AUT-02<br/>Execution Evidence"]
    I["AUT-03<br/>Visible Failure Path"]

    J["TC-AUT-01<br/>Successful Routing"]
    K["TC-AUT-02<br/>Routing Failure"]
    L["TC-AUT-09<br/>Execution Logging"]

    M["Automation Success Rate"]
    N["Manual Exception Rate"]

    O["Reliable Automation"]

    A --> B

    B --> C
    B --> D
    B --> E

    C --> F
    D --> F
    E --> F

    F --> G
    F --> H
    F --> I

    G --> J
    I --> K
    H --> L

    J --> M
    K --> N
    L --> M

    M --> O
    N --> O
```

### Intended Outcome

Automation should reduce repetitive work without creating invisible failure.

If automation cannot complete safely, the work should return to a visible, owned process.

---

## Example 5 — AI-Assisted Categorization

```mermaid
flowchart LR

    A["Operational Need<br/>Reduce Manual Categorization Effort"]

    B["BR-17<br/>Responsible AI Assistance"]

    C["FR-36<br/>Suggested Categorization"]
    D["FR-39<br/>AI Attribution"]
    E["FR-40<br/>Restricted AI Actions"]

    F["AI-Assisted Service Management"]

    G["AI-01<br/>Human Review"]
    H["AI-02<br/>Attribution"]
    I["AI-03<br/>Restricted Autonomous Action"]

    J["TC-AI-01<br/>Category Suggestion"]
    K["TC-AI-02<br/>Attribution"]
    L["TC-AI-03<br/>Restricted Action"]

    M["Suggestion Acceptance"]
    N["Correction / Rejection Rate"]

    O["Reduced Manual Effort<br/>Without Loss of Authority"]

    A --> B

    B --> C
    B --> D
    B --> E

    C --> F
    D --> F
    E --> F

    F --> G
    F --> H
    F --> I

    G --> J
    H --> K
    I --> L

    J --> M
    K --> M
    L --> N

    M --> O
    N --> O
```

---

## Design Principle

Traceability should not exist only because a project template asks for it.

It should make design decisions easier to defend.

If someone asks:

> Why is this control here?

the answer should trace back to a real requirement or operational risk.

If someone asks:

> How do we know the requirement was implemented?

the answer should trace forward to a test.

If someone asks:

> Did the implementation actually improve anything?

the answer should trace forward again to an operational metric.

That creates a complete implementation chain:

> **Problem → Requirement → Design → Control → Test → Measure**
