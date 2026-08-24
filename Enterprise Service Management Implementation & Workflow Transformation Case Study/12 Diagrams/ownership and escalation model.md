# Ownership and Escalation Model

## Purpose

This diagram shows how ownership, assignment, consultation, escalation, and vendor dependency interact in the target Enterprise Service Management operating model.

The intent is to prevent a common service-management failure:

> Work moves between people or teams, but accountability becomes unclear.

The target model separates:

* who owns the record
* who is assigned the work
* who is being consulted
* who is being escalated to
* whether an external vendor is involved

Ownership should remain visible through each of those conditions.

---

## Core Ownership Model

```mermaid id="6q8y9m"
flowchart TD

    A["Service Record Created"]

    B["Owning Support Group"]

    C["Assigned Technician / Resolver"]

    D["Work Performed"]

    E{"Need Another Team?"}

    F["Consult Another Team"]

    G["Reassign Ownership"]

    H{"Need Escalation?"}

    I["Functional Escalation"]

    J["Hierarchical Escalation"]

    K{"Vendor Required?"}

    L["Vendor Dependency"]

    M["Internal Owner Retained"]

    N["Resolution / Completion"]

    O["Closure Validation"]

    A --> B
    B --> C
    C --> D

    D --> E

    E -->|"No"| H
    E -->|"Consultation"| F
    E -->|"Ownership Transfer"| G

    F --> C
    G --> B

    H -->|"No"| K
    H -->|"Technical Expertise"| I
    H -->|"Management Attention"| J

    I --> C
    J --> B

    K -->|"No"| N
    K -->|"Yes"| L

    L --> M
    M --> C

    N --> O
```

---

## Ownership Layers

```mermaid id="2t4q4b"
flowchart LR

    S["Service Owner"]

    G["Support Group Owner"]

    A["Assigned Resolver"]

    V["Vendor / External Party"]

    S -->|"Defines service accountability"| G
    G -->|"Owns active work"| A
    A -->|"Performs / coordinates work"| V
```

The roles are related but not interchangeable.

### Service Owner

Accountable for the service itself.

Typical responsibilities include:

* service expectations
* SLA
* escalation policy
* service performance
* major exceptions
* improvement priorities

### Support Group Owner

Operationally accountable for active work assigned to the group.

Responsibilities include:

* queue ownership
* workload
* reassignment
* escalation
* aging work
* operational completion

### Assigned Resolver

Responsible for the current technical or fulfillment action.

The assigned resolver may change without changing overall service accountability.

### Vendor

May perform technical work or provide information.

Vendor involvement should not eliminate the internal owner.

---

## Assignment vs Ownership

```mermaid id="77gtei"
flowchart LR

    A["Owning Support Group"]
    B["Assigned Technician A"]
    C["Assigned Technician B"]

    A --> B
    A --> C
```

A technician assignment answers:

> Who is currently working this?

Group ownership answers:

> Which internal team remains accountable for making sure this work moves forward?

These should not be confused.

---

## Consultation vs Reassignment

```mermaid id="7z9xgg"
flowchart TD

    A["Current Owner"]

    B{"Does another team need to help?"}

    C["Consult"]

    D["Reassign"]

    E["Current Owner Remains"]

    F["New Group Becomes Owner"]

    A --> B

    B -->|"Expertise only"| C
    B -->|"Work responsibility changes"| D

    C --> E
    D --> F
```

Consultation is appropriate when another team provides:

* expertise
* diagnostic assistance
* information
* a supporting task

Reassignment is appropriate when the other team becomes responsible for driving the work to the next meaningful outcome.

This distinction reduces unnecessary ticket bouncing.

---

## Functional Escalation

Functional escalation occurs when the ticket requires:

* deeper technical expertise
* specialized support
* different capability
* another operational function

```mermaid id="yy4oew"
flowchart LR

    A["Frontline Support"]
    B["Specialist Team"]
    C["Engineering / Advanced Support"]

    A -->|"Functional Escalation"| B
    B -->|"Additional Expertise Required"| C
```

Functional escalation does not automatically require management involvement.

---

## Hierarchical Escalation

Hierarchical escalation occurs when the issue requires management attention rather than deeper technical capability.

Typical triggers include:

* SLA risk
* repeated reassignment
* priority dispute
* stalled vendor response
* resource conflict
* high business impact
* unresolved ownership conflict

```mermaid id="jf9uru"
flowchart TD

    A["Assigned Work"]

    B["SLA / Operational Risk"]

    C["Support Lead"]

    D["Service Owner / Management"]

    E["Executive / Major Incident Authority"]

    A --> B
    B --> C
    C --> D
    D -->|"Critical Impact if Required"| E
```

Escalation increases visibility or authority.

It should not automatically cause the original team to stop owning the work.

---

## Reassignment Model

A reassignment should require:

* valid destination
* reason
* current context
* preserved history

```mermaid id="5qq68a"
flowchart LR

    A["Current Group"]

    B["Reassignment Decision"]

    C["Reason Recorded"]

    D["New Group"]

    E["Ownership History Preserved"]

    A --> B
    B --> C
    C --> D
    D --> E
```

The target state should avoid:

```text id="pwi6je"
Send Ticket
   ↓
Remove From My Queue
   ↓
Hope Someone Else Handles It
```

---

## Reassignment Loop Detection

Repeated reassignment is an operational signal.

```mermaid id="pk7nws"
flowchart TD

    A["Ticket Reassigned"]

    B["Reassignment Count Increases"]

    C{"Threshold Reached?"}

    D["Continue Normal Workflow"]

    E["Escalate Ownership Review"]

    F["Correct Routing / Ownership"]

    A --> B
    B --> C

    C -->|"No"| D
    C -->|"Yes"| E

    E --> F
```

A reassignment loop may indicate:

* poor categorization
* bad service mapping
* unclear support boundaries
* weak ownership
* missing technical context

The goal should be to fix the routing problem rather than simply move the ticket faster.

---

## SLA Escalation

SLA escalation should add urgency and visibility while preserving ownership.

```mermaid id="sj7ps2"
flowchart LR

    A["Active Ticket"]

    B["75% SLA"]

    C["Support Group Warning"]

    D["90% SLA"]

    E["Group Lead Escalation"]

    F["100% SLA"]

    G["Service Owner / Management Escalation"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
```

The specific thresholds may vary by service, but the principle remains the same:

> Escalation should cause action, not simply another notification.

---

## Vendor Dependency Model

External involvement is one of the places where ownership most often becomes unclear.

The target model prevents that.

```mermaid id="4ss7ap"
flowchart TD

    A["Internal Service Record"]

    B["Internal Owning Group"]

    C["Vendor Engagement"]

    D["Vendor Action / Response"]

    E["Internal Validation"]

    F["Resolution"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F

    B -. "Ownership Retained" .-> E
```

The vendor may own a contractual action.

The organization still owns the service outcome.

---

## Waiting on Vendor

```mermaid id="rzybr3"
flowchart LR

    A["Active Work"]

    B["Waiting on Vendor"]

    C["Internal Owner Remains"]

    D["Vendor Follow-Up / Escalation"]

    E["Response Received"]

    F["Work Resumes"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
```

A waiting state should describe why work is delayed.

It should not remove accountability.

---

## Approval Ownership

Approval is another decision point where ownership needs to remain clear.

```mermaid id="pjrg1v"
flowchart TD

    A["Request"]

    B["Operational Owner"]

    C["Approver"]

    D{"Decision"}

    E["Approved"]

    F["Rejected"]

    G["Fulfillment"]

    H["Request Closed"]

    A --> B
    B --> C
    C --> D

    D -->|"Approve"| E
    D -->|"Reject"| F

    E --> G
    G --> H
    F --> H
```

The approver owns the decision.

The operational owner retains responsibility for the request workflow.

---

## Major Incident Ownership

High-severity incidents may introduce multiple participants.

```mermaid id="2lwgkk"
flowchart TD

    A["P1 / Major Incident"]

    B["Incident Owner"]

    C["Technical Teams"]

    D["Service Owner"]

    E["Management / Communications"]

    F["Vendor if Required"]

    G["Recovery"]

    A --> B

    B --> C
    B --> D
    B --> E
    B --> F

    C --> G
    D --> G
    E --> G
    F --> G
```

More participants should not mean less accountability.

Major Incident handling should make coordination clearer, not blur who is driving recovery.

---

## Ownership Decision Model

```mermaid id="2fu6x5"
flowchart TD

    A["Work Requires Action"]

    B{"Who owns the next meaningful outcome?"}

    C["Current Group"]

    D["Another Internal Group"]

    E["External Vendor"]

    F["Current Group Retains Ownership"]

    G["Transfer Ownership"]

    H["Retain Internal Owner + Track Vendor"]

    A --> B

    B -->|"Current team"| C
    B -->|"Different internal team"| D
    B -->|"External dependency"| E

    C --> F
    D --> G
    E --> H
```

This is the central decision behind the target ownership model.

---

## Target Operating Principle

The target service model does not require the same person or team to perform every action.

It requires accountability to remain visible as work moves.

That means:

* consultation does not automatically transfer ownership
* escalation does not automatically transfer ownership
* vendor dependency does not eliminate internal ownership
* waiting states do not eliminate ownership
* reassignment requires an explicit decision
* approval responsibility is distinct from fulfillment responsibility

The model can be reduced to one operational rule:

> **Someone always owns the next move.**
