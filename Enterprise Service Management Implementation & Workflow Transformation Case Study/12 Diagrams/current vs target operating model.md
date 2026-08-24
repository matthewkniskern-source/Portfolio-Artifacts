# Current State vs Target Operating Model

## Purpose

This diagram summarizes the primary transformation modeled in the case study.

The current environment depends on fragmented intake, individual coordination, and inconsistent service-management practices.

The target environment establishes controlled intake, visible ownership, defined workflow, governance, and measurable service performance.

```mermaid
flowchart LR

    subgraph CURRENT["CURRENT STATE — PERSON-DEPENDENT SERVICE DELIVERY"]
        direction TB

        C1["Email"]
        C2["Phone"]
        C3["Chat"]
        C4["Spreadsheet"]
        C5["Direct Technician Contact"]

        C6["Fragmented Intake"]

        C7["Individual Technician Judgment"]

        C8["Subjective Priority"]
        C9["Informal Ownership"]
        C10["Manual Handoffs"]
        C11["Off-Record Approvals"]

        C12["Limited Service / Asset Context"]
        C13["Tribal Knowledge"]
        C14["Weak SLA Visibility"]
        C15["Incomplete Reporting"]

        C1 --> C6
        C2 --> C6
        C3 --> C6
        C4 --> C6
        C5 --> C6

        C6 --> C7

        C7 --> C8
        C7 --> C9
        C7 --> C10
        C7 --> C11

        C8 --> C14
        C9 --> C15
        C10 --> C15
        C11 --> C15

        C12 --> C15
        C13 --> C15
    end


    TRANSFORM["SERVICE MANAGEMENT TRANSFORMATION"]


    subgraph TARGET["TARGET STATE — PROCESS-DRIVEN SERVICE DELIVERY"]
        direction TB

        T1["Approved Intake Channels"]

        T2["Authoritative Service Record"]

        T3["Defined Service & Support Ownership"]

        T4["Impact / Urgency Priority"]
        T5["SLA & Escalation"]
        T6["Controlled Approvals"]
        T7["RBAC & Decision Authority"]

        T8["Service / Asset / CI Relationships"]
        T9["Managed Knowledge"]
        T10["Vendor Accountability"]

        T11["Controlled Automation"]
        T12["Governed AI Assistance"]

        T13["Reliable Operational Data"]

        T14["Performance Measurement"]
        T15["Continuous Improvement"]

        T1 --> T2
        T2 --> T3

        T3 --> T4
        T3 --> T5
        T3 --> T6
        T3 --> T7

        T2 --> T8
        T2 --> T9
        T2 --> T10

        T4 --> T11
        T5 --> T11
        T6 --> T11

        T8 --> T12
        T9 --> T12

        T2 --> T13
        T3 --> T13
        T4 --> T13
        T5 --> T13
        T6 --> T13
        T8 --> T13
        T9 --> T13
        T10 --> T13
        T11 --> T13
        T12 --> T13

        T13 --> T14
        T14 --> T15
    end


    CURRENT --> TRANSFORM
    TRANSFORM --> TARGET
```

---

## Transformation Summary

| Current State                  | Target State                           |
| ------------------------------ | -------------------------------------- |
| Fragmented intake              | Controlled intake                      |
| Technician-dependent decisions | Defined process rules                  |
| Subjective prioritization      | Impact / urgency priority              |
| Informal ownership             | Explicit service and support ownership |
| Manual escalation              | SLA-driven escalation                  |
| Off-record approvals           | Auditable workflow approvals           |
| Limited technical context      | Service / asset / CI relationships     |
| Tribal knowledge               | Managed knowledge lifecycle            |
| Weak vendor visibility         | Internal vendor accountability         |
| Manual repetitive work         | Controlled automation                  |
| Unstructured AI use            | Governed AI assistance                 |
| Weak reporting                 | Reliable operational measurement       |

---

## Design Intent

The target model does not attempt to remove human judgment from service delivery.

It moves that judgment to the places where it is useful.

Technicians still determine how to troubleshoot an issue.

Service owners still make service decisions.

Approvers still decide whether controlled activity should proceed.

What changes is the process surrounding those decisions.

Intake, ownership, priority, approval, escalation, evidence, and measurement become consistent enough that the organization no longer depends on an individual technician remembering how the process is supposed to work.

The transformation can be summarized as:

> **Person-dependent service delivery → Process-driven service delivery**
