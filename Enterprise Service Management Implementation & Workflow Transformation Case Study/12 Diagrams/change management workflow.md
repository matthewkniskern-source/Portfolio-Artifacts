# Change Management Workflow

## Purpose

This diagram shows how the target Enterprise Service Management model handles Standard, Normal, and Emergency Change.

The objective is to scale control to risk while preserving:

* authorization
* readiness
* implementation evidence
* validation
* recovery
* service traceability

The operating principle is:

> **Change control should reduce avoidable risk without making routine work unnecessarily difficult.**

---

## Change Type Decision

```mermaid id="d7c3qe"
flowchart TD

    A["Change Needed"]

    B{"Does an approved<br/>Standard Change template apply?"}

    C["Standard Change"]

    D{"Is immediate action required<br/>to address critical risk or outage?"}

    E["Emergency Change"]

    F["Normal Change"]

    A --> B

    B -->|"Yes"| C
    B -->|"No"| D

    D -->|"Yes"| E
    D -->|"No"| F
```

The change type determines the level of assessment and approval required.

It should not be chosen simply because one path is faster.

---

## Core Change Lifecycle

```mermaid id="87k9yt"
flowchart LR

    A["Draft"]

    B["Assessment"]

    C["Pending Approval"]

    D["Scheduled"]

    E["Implementation"]

    F["Validation"]

    G["Completed"]

    H["Failed"]

    I["Backout / Recovery"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F

    F -->|"Successful"| G
    F -->|"Unsuccessful"| H

    H --> I
    I --> F
```

A change should not close as successful simply because implementation activity ended.

Validation determines the outcome.

---

## Standard Change Workflow

Standard Changes are repeatable, documented, and pre-authorized within an approved scope.

```mermaid id="5rcvng"
flowchart TD

    A["Standard Change Requested"]

    B["Approved Template Selected"]

    C{"Within Template Scope?"}

    D["Validate Required Data"]

    E["Schedule"]

    F["Implement"]

    G["Validate"]

    H["Complete"]

    I["Route to Normal Change"]

    A --> B
    B --> C

    C -->|"Yes"| D
    C -->|"No"| I

    D --> E
    E --> F
    F --> G
    G --> H
```

A Standard Change remains standard only while it stays inside the approved template.

If scope, risk, implementation method, or affected service materially changes, the work should move to the appropriate Normal Change path.

---

## Normal Change Workflow

```mermaid id="ok5ip4"
flowchart TD

    A["Normal Change Drafted"]

    B["Define Scope / Service / CI"]

    C["Assess Risk & Impact"]

    D["Confirm Implementation Plan"]

    E["Confirm Validation & Backout"]

    F{"Readiness Complete?"}

    G["Required Approval"]

    H{"Approved?"}

    I["Schedule"]

    J["Implement"]

    K["Validate"]

    L{"Outcome?"}

    M["Successful"]

    N["Successful with Issue"]

    O["Failed"]

    P["Backout / Recovery"]

    Q["Rejected / Rework"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F

    F -->|"No"| Q
    F -->|"Yes"| G

    G --> H

    H -->|"No"| Q
    H -->|"Yes"| I

    I --> J
    J --> K
    K --> L

    L -->|"Successful"| M
    L -->|"Issue Remaining"| N
    L -->|"Unsuccessful"| O

    O --> P
```

---

## Risk-Based Approval

Approval should scale with risk.

```mermaid id="7c5m8d"
flowchart LR

    A["Low Risk"]
    B["Defined / Simplified Approval"]

    C["Medium Risk"]
    D["Service / Change Authority Approval"]

    E["High Risk"]
    F["Enhanced Review / Authorization"]

    A --> B
    C --> D
    E --> F
```

Risk assessment may consider:

* business impact
* service criticality
* number of affected users
* technical complexity
* rollback capability
* security impact
* vendor involvement
* implementation window
* previous change history

The model should remain practical.

Not every field needs a scoring formula if experienced reviewers can make the decision consistently from defined criteria.

---

## Readiness Gate

Before implementation, a Normal or high-risk change should confirm:

```mermaid id="5feclh"
flowchart TD

    A["Change Ready?"]

    B["Scope Defined"]
    C["Affected Service / CI Known"]
    D["Risk Assessed"]
    E["Implementation Plan"]
    F["Validation Plan"]
    G["Backout Plan"]
    H["Approval Complete"]
    I["Schedule Confirmed"]

    J["Ready for Implementation"]

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F
    A --> G
    A --> H
    A --> I

    B --> J
    C --> J
    D --> J
    E --> J
    F --> J
    G --> J
    H --> J
    I --> J
```

If a critical readiness requirement is missing, the change should not proceed simply because the scheduled window has arrived.

---

## Failed Change Path

```mermaid id="0dh7if"
flowchart TD

    A["Implementation Completed"]

    B["Validation"]

    C{"Validation Successful?"}

    D["Complete Change"]

    E["Change Failed"]

    F{"Backout Possible?"}

    G["Execute Backout"]

    H["Corrective Action"]

    I["Validate Service Recovery"]

    J{"Service Impact?"}

    K["Create / Link Incident"]

    L["Record Final Change Outcome"]

    A --> B
    B --> C

    C -->|"Yes"| D
    C -->|"No"| E

    E --> F

    F -->|"Yes"| G
    F -->|"No"| H

    G --> I
    H --> I

    I --> J

    J -->|"Yes"| K
    J -->|"No"| L

    K --> L
```

The goal is not to hide failure.

It is to make failure recoverable and traceable.

---

## Change-to-Incident Relationship

```mermaid id="7pcj8u"
flowchart LR

    CH["Change"]

    CI["Affected CI"]

    S["Affected Service"]

    I["Incident"]

    R["Recovery / Backout"]

    CH --> CI
    CH --> S

    CH -->|"causes / contributes to"| I

    I --> R
    CH --> R
```

This relationship supports questions such as:

* Which change affected the service?
* Which CI was modified?
* Did the change create an incident?
* Was a backout performed?
* Is the same change pattern failing repeatedly?

---

## Emergency Change Workflow

Emergency Change allows speed while preserving minimum accountability.

```mermaid id="9t4jrf"
flowchart TD

    A["Critical Condition"]

    B["Emergency Change Raised"]

    C["Minimum Risk / Impact Assessment"]

    D["Expedited Authorized Approval"]

    E["Implement"]

    F["Validate"]

    G{"Successful?"}

    H["Restore / Stabilize"]

    I["Backout / Corrective Action"]

    J["Post-Implementation Review"]

    K["Complete Record"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F

    F --> G

    G -->|"Yes"| H
    G -->|"No"| I

    H --> J
    I --> J

    J --> K
```

Emergency should mean:

> the normal timing of the process is inappropriate for the operational condition.

It should not mean:

> documentation and accountability are optional.

---

## Emergency Change Retrospective

The retrospective review should confirm:

* why emergency handling was required
* who authorized the change
* what was implemented
* whether service was restored
* whether an incident occurred
* whether a standard or normal change should follow
* whether the emergency could have been prevented

Repeated emergency changes for the same condition should become an improvement signal.

---

## Vendor-Implemented Change

```mermaid id="zmdwwr"
flowchart TD

    A["Internal Change Owner"]

    B["Vendor Implementation"]

    C["Internal Coordination"]

    D["Vendor Executes Work"]

    E["Internal Validation"]

    F["Change Outcome"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F

    A -. "Accountability Retained" .-> E
```

Vendor execution does not remove internal accountability.

The internal Change Owner should still ensure:

* authorization
* schedule
* affected service visibility
* implementation evidence
* validation
* final outcome

---

## Approval and Separation of Duties

```mermaid id="j6q3wj"
flowchart TD

    A["Change Requester / Implementer"]

    B["Approval Required"]

    C{"Authorized Independent Approver?"}

    D["Approval Recorded"]

    E["Implementation Allowed"]

    F["Approval Blocked"]

    A --> B
    B --> C

    C -->|"Yes"| D
    C -->|"No"| F

    D --> E
```

For controlled changes, the person requesting or implementing the activity should not automatically receive authority to approve it.

The level of separation should scale with risk.

---

## Change Closure

A change should close only after:

* implementation result is documented
* validation is complete
* service status is known
* failure or backout is recorded where applicable
* related incidents are linked
* final outcome is accurate

```mermaid id="tyyspa"
flowchart LR

    A["Implementation"]

    B["Validation"]

    C["Outcome Recorded"]

    D["Relationships Updated"]

    E["Closure"]

    A --> B
    B --> C
    C --> D
    D --> E
```

"Work completed" and "change successfully completed" are not necessarily the same thing.

---

## Change Performance Feedback

Change data should feed continuous improvement.

```mermaid id="lwhx0p"
flowchart TD

    A["Change Outcomes"]

    B["Success Rate"]
    C["Failure Rate"]
    D["Emergency Rate"]
    E["Backout Rate"]
    F["Incidents Caused by Change"]

    G["Trend Analysis"]

    H["Process Improvement"]

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
```

The objective is to improve how reliably the organization changes production.

---

## Change Management Principle

The target change model is designed around three ideas:

1. **Routine work should remain routine.**
2. **Higher risk should receive stronger control.**
3. **Failure should remain visible and recoverable.**

A mature change process should not make every production action difficult.

It should make it difficult to introduce material risk without understanding, authorization, and a recovery path.

> **Control should scale with risk, while accountability remains constant.**
