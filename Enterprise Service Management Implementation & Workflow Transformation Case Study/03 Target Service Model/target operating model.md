# Target Operating Model

## Purpose

The target operating model defines how the organization will manage service work once the fragmented current-state process is replaced by a consistent Enterprise Service Management model.

This is not a platform screen design.

It is the operating structure the platform must support.

The target state establishes clear intake, ownership, prioritization, escalation, approval, data relationships, and accountability without forcing every service interaction into unnecessary process.

The operating principle is:

> **Use enough structure to make service work visible, accountable, measurable, and repeatable without slowing down routine support.**

The target model is derived from:

* [Current State Assessment](../01%20Current%20State/current%20state%20assessment.md)
* [Stakeholder Map](../01%20Current%20State/stakeholder%20map.md)
* [Pain Points and Failure Modes](../01%20Current%20State/pain%20points%20and%20failure%20modes.md)
* [Business Requirements](../02%20Requirements%20Discovery/business%20requirements.md)
* [Functional Requirements](../02%20Requirements%20Discovery/functional%20requirements.md)
* [Requirements Traceability Matrix](../02%20Requirements%20Discovery/requirements%20traceability%20matrix.md)

---

# 1. Target-State Objective

The current environment relies heavily on individual technicians to decide:

* whether work should be recorded
* what kind of record to create
* how important the work is
* who should own it
* whether approval is required
* when escalation is appropriate
* what must be documented before closure

The target operating model moves those decisions into defined service processes where standardization adds value.

The result should be an organization where service work can be answered consistently through six questions:

1. **What is being requested or disrupted?**
2. **Who currently owns the work?**
3. **How important is it?**
4. **What service, user, asset, or CI is affected?**
5. **What approvals or controls apply?**
6. **What must happen before the record is complete?**

Those answers should remain visible throughout the service lifecycle.

---

# 2. Target Operating Model Overview

The future environment is organized around a common service-management layer.

```text
                         ┌──────────────────────┐
                         │      End Users       │
                         └──────────┬───────────┘
                                    │
                  Approved Intake Channels
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Enterprise Service   │
                         │ Management Platform  │
                         └──────────┬───────────┘
                                    │
                     Classification / Routing
                                    │
               ┌────────────────────┼────────────────────┐
               │                    │                    │
               ▼                    ▼                    ▼
        Service Desk        Specialist Groups       Process Owners
               │                    │                    │
               └──────────────┬─────┴──────────────┬────┘
                              │                    │
                              ▼                    ▼
                        Resolution /          Approval /
                         Fulfillment          Governance
                              │                    │
                              └──────────┬─────────┘
                                         ▼
                                   Closure
                                         │
                                         ▼
                              Reporting / Knowledge
                                         │
                                         ▼
                               Continuous Improvement
```

A more polished representation will be maintained in:

[Target Operating Model Diagram](../diagrams/target%20operating%20model.md)

---

# 3. Core Operating Principles

The target model is built around eight operating principles.

## 3.1 One Managed Record

Managed service work should ultimately be represented in the ESM platform.

Users may still initiate contact through approved channels such as:

* portal
* email
* phone
* technician-assisted entry
* approved integrations

Those channels feed the same service-management process.

They do not create separate operating models.

---

## 3.2 Clear Ownership

Every active record should have a defined owner.

Ownership may move during the lifecycle, but it should never become ambiguous.

The organization should always be able to identify:

* owning support group
* assigned technician where applicable
* service owner
* pending approver
* vendor dependency
* escalation owner

Detailed ownership design is maintained in:

[Ownership and Escalation](./ownership%20and%20escalation.md)

---

## 3.3 Business-Based Priority

Priority should reflect operational impact and urgency rather than requester influence.

The target model uses defined impact and urgency criteria to drive:

* priority
* response expectation
* escalation behavior

Authorized exceptions remain possible, but they must be documented.

Detailed model:

[Priority and SLA Model](./priority%20and%20sla%20model.md)

---

## 3.4 Workflow by Work Type

Different work requires different controls.

The platform therefore distinguishes among:

* Incident
* Service Request
* Change
* Knowledge

Each process has its own lifecycle, ownership, data requirements, approval conditions, and closure rules.

Detailed workflows are maintained in:

* [Incident Management](../04%20Workflow%20Design/incident%20management.md)
* [Service Request Management](../04%20Workflow%20Design/service%20request%20management.md)
* [Change Management](../04%20Workflow%20Design/change%20management.md)
* [Knowledge Management](../04%20Workflow%20Design/knowledge%20management.md)

---

## 3.5 Controls Where Risk Justifies Them

Not every request needs approval.

Not every change needs the same authorization.

Not every record needs restricted access.

The target model applies additional control where business or security risk justifies it.

Examples include:

* privileged access
* sensitive system access
* high-risk change
* selected purchases
* vendor access

The design should avoid turning control into bureaucracy for low-risk routine work.

---

## 3.6 Useful Data Relationships

Service-management records should connect to operational context where that relationship supports a real decision.

Useful relationships include:

```text
User
  ↓
Ticket
  ↓
Service
  ↓
Asset / CI
  ↓
Change
```

Additional relationships may include:

* support group
* vendor
* knowledge
* approval
* location

The goal is operational context, not maximum data collection.

Detailed design:

[Service Management Data Model](../05%20Data%20and%20Configuration%20Model/service%20management%20data%20model.md)

---

## 3.7 Automation After Process Definition

Automation should reduce repetitive administrative work after business rules are defined.

Candidate automation includes:

* routing
* SLA timers
* escalation
* reminders
* approval notifications
* expiration
* change notifications

Automation should not make unresolved process decisions on behalf of the organization.

Detailed design:

[Automation Opportunities](../07%20Automation%20and%20AI/automation%20opportunities.md)

---

## 3.8 Measurement as Feedback

Metrics are part of the operating model, not just reporting output.

Service data should help identify:

* process bottlenecks
* routing problems
* recurring incidents
* weak knowledge coverage
* unsuccessful change patterns
* adoption problems
* service-level misses

Measurement should drive process adjustment rather than simply produce monthly dashboards.

Detailed design:

[Performance Framework](../11%20Metrics%20and%20Optimization/performance%20framework.md)

---

# 4. Target Service Entry Model

The target environment supports multiple approved intake methods while maintaining one service process.

```text
Portal ───────────┐
Email ────────────┤
Phone ────────────┤
Technician Entry ─┼──► Managed Service Record
Integration ──────┘
```

The important change from the current state is not fewer communication methods.

It is consistent record creation.

## Approved Channel Principles

Approved channels should:

* capture or create a managed record
* identify the requester where possible
* collect minimum required information
* route into a defined workflow
* provide confirmation
* preserve communication history where practical

Informal conversations may still occur.

If they result in managed service work, the record should follow.

---

# 5. Service Catalog Model

The service catalog becomes the user-facing representation of repeatable services and requests.

The catalog should be organized around what users need rather than internal IT department structure.

Representative catalog areas may include:

* Accounts and Access
* End-User Technology
* Business Applications
* Collaboration and Communication
* Network and Connectivity
* Facilities Technology Support

Each catalog item may define:

* service owner
* request form
* required information
* fulfillment group
* approval requirements
* target fulfillment time
* related knowledge
* cost information where applicable

Detailed design:

[Service Catalog](./service%20catalog.md)

---

# 6. Service Ownership

Each supported service should have an accountable owner.

The service owner is responsible for the service as a business or technical capability.

That does not mean the service owner personally resolves every ticket.

The role includes accountability for:

* service definition
* service expectations
* escalation
* approval policy where applicable
* reporting
* improvement priorities

A service may be supported by several technical groups while still having one accountable service owner.

Example:

```text
Business Email Service
        │
        ├── Service Owner
        │
        ├── Service Desk
        │
        ├── Messaging Support
        │
        ├── Identity Team
        │
        └── External Vendor
```

This prevents shared technical responsibility from becoming shared ambiguity.

---

# 7. Support Group Model

Support groups are organized around service capability rather than individual technician preference.

Representative groups may include:

* Service Desk
* Endpoint Support
* Network Support
* Infrastructure / Server Support
* Application Support
* Identity and Access
* Platform Administration

Each support group should have:

* defined scope
* queue ownership
* escalation path
* group lead
* supported categories or services
* reassignment rules

Individual assignment may occur after group assignment.

Group ownership remains the operational anchor.

---

# 8. Priority Model

Incident priority is based on:

**Impact + Urgency → Priority**

The model should avoid excessive complexity.

A practical structure may use:

* High / Medium / Low Impact
* High / Medium / Low Urgency
* P1–P4 Priority

Example:

| Impact | Urgency | Priority |
| ------ | ------- | -------- |
| High   | High    | P1       |
| High   | Medium  | P2       |
| Medium | High    | P2       |
| Medium | Medium  | P3       |
| Low    | High    | P3       |
| High   | Low     | P3       |
| Medium | Low     | P4       |
| Low    | Medium  | P4       |
| Low    | Low     | P4       |

Detailed definitions, overrides, and associated service targets are maintained in:

[Priority and SLA Model](./priority%20and%20sla%20model.md)

---

# 9. SLA Model

The target SLA model separates response expectations from resolution or fulfillment expectations.

Applicable records may therefore include:

* first-response target
* resolution target
* fulfillment target
* warning threshold
* breach threshold

SLA timing also requires defined pause conditions.

Example states may include:

```text
Active Support
     │
     ├── SLA Running
     │
Waiting on User
     │
     ├── SLA Paused if policy permits
     │
Waiting on Vendor
     │
     ├── Policy dependent
     │
Scheduled
     │
     ├── Policy dependent
     │
Resolved
     │
     └── SLA Stopped
```

A pause state should not become a convenient way to protect SLA numbers.

Every pause condition must have a defined business reason.

---

# 10. Escalation Model

Escalation exists in two forms.

## Functional Escalation

Work moves to a team with additional expertise.

Example:

```text
Service Desk
     ↓
Application Support
     ↓
Database Support
```

This changes who performs the work.

---

## Hierarchical Escalation

Management or service ownership is notified because service risk or delay has increased.

Example:

```text
Ticket
  ↓
SLA Warning
  ↓
Group Lead
  ↓
SLA Breach
  ↓
Service Owner / IT Management
```

A ticket may use both forms.

Escalation should not automatically remove ownership unless the workflow explicitly transfers it.

Detailed design:

[Ownership and Escalation](./ownership%20and%20escalation.md)

---

# 11. Approval Model

Approval is applied to predefined conditions.

Representative approval scenarios include:

* hardware purchase
* privileged access
* selected application access
* high-risk change
* emergency exception
* vendor remote access

An approval workflow should capture:

```text
Request
   ↓
Validation
   ↓
Approval Required?
  ↙              ↘
No                Yes
↓                  ↓
Fulfillment       Approver
                   ↓
              Approve / Reject
                   ↓
                Fulfillment
```

The model should define:

* approver authority
* approval order
* rejection behavior
* escalation
* prohibited self-approval
* expiration where appropriate

Approval is a business decision.

The platform records and enforces it.

---

# 12. Vendor Operating Model

Vendor involvement remains part of the internal service process.

A vendor may perform technical work without becoming the owner of the internal service outcome.

Target model:

```text
Internal Ticket
      ↓
Internal Owner
      ↓
Vendor Support Required
      ↓
Vendor Case / Access
      ↓
Vendor Activity
      ↓
Internal Validation
      ↓
Resolution
```

The service record should retain:

* internal owner
* vendor identity
* vendor case reference
* current vendor dependency
* material activity
* access status where applicable

If temporary access is granted, it must have defined expiration and internal sponsorship.

---

# 13. Knowledge Operating Model

Knowledge should be produced from service experience rather than treated as a separate documentation exercise.

Candidate knowledge sources include:

* recurring incidents
* high-value resolutions
* known workarounds
* support procedures
* service-request guidance

Target lifecycle:

```text
Operational Knowledge
        ↓
Draft
        ↓
Review
        ↓
Publish
        ↓
Use
        ↓
Feedback / Update
        ↓
Retire
```

Article volume is not the objective.

Reuse is.

---

# 14. Reporting Operating Model

Reporting is organized around three audiences.

## Operational

Used by support teams for day-to-day management.

Examples:

* queue volume
* aging tickets
* SLA warnings
* pending approvals
* vendor dependencies

---

## Management

Used to understand service performance.

Examples:

* SLA compliance
* backlog age
* reassignment rate
* reopen rate
* change success
* workload distribution

---

## Improvement

Used to identify where the process should change.

Examples:

* recurring incidents
* repeated priority overrides
* high reassignment categories
* knowledge gaps
* slow approval types
* repeated automation failures

The target reporting model therefore moves beyond counting tickets.

It should help explain where the service process is losing time or producing avoidable work.

---

# 15. Target-State Role Model

| Role                   | Primary Responsibility              |
| ---------------------- | ----------------------------------- |
| Requester              | Submit and provide information      |
| Service Desk           | Intake, triage, initial resolution  |
| Resolver Group         | Technical resolution or fulfillment |
| Service Owner          | Accountable for service outcome     |
| Approver               | Authorize controlled activity       |
| Change Authority       | Authorize applicable changes        |
| Platform Administrator | Configure approved workflow         |
| Security / Risk        | Define applicable controls          |
| Vendor                 | Provide bounded external support    |
| IT Management          | Govern performance and priorities   |
| Champion / Super-User  | Support adoption and feedback       |

These roles will later be translated into:

* RBAC
* workflow permissions
* approval rights
* reporting access
* control ownership

Detailed governance:

[Governance and Controls](../06%20Governance%20and%20Controls/governance%20model.md)

---

# 16. Target-State Decision Model

The target process follows a consistent decision sequence.

```text
Work Enters
    ↓
What type of work is this?
    ↓
Who owns it?
    ↓
How important is it?
    ↓
What does it affect?
    ↓
Does it require approval or control?
    ↓
What work must be completed?
    ↓
Has closure criteria been met?
    ↓
What should be measured or learned?
```

This sequence becomes the backbone for later workflow configuration.

---

# 17. Current-to-Target Comparison

| Current State                          | Target State                                   |
| -------------------------------------- | ---------------------------------------------- |
| Multiple informal service paths        | Multiple approved channels feeding one process |
| Technician-dependent record creation   | Defined managed-record criteria                |
| Subjective priority                    | Impact / urgency model                         |
| Unclear ownership                      | Explicit group ownership                       |
| Manual SLA follow-up                   | Defined timers and escalation                  |
| Email / verbal approval                | Structured approval history                    |
| Weak CI relationships                  | Relevant service / asset / CI context          |
| Vendor activity outside service record | Managed internal vendor dependency             |
| Informal knowledge reuse               | Controlled knowledge lifecycle                 |
| Incomplete reporting                   | Standardized service data and metrics          |
| Automation added opportunistically     | Automation based on approved rules             |
| AI treated as generic capability       | AI bounded by defined use and control          |

A visual comparison will be maintained in:

[Current vs Target Operating Model](../diagrams/current%20vs%20target%20operating%20model.md)

---

# 18. Target-State Control Points

The operating model introduces several deliberate control points.

```text
Intake
  ↓
Minimum Data Gate
  ↓
Priority / Ownership
  ↓
Approval Gate if Required
  ↓
Fulfillment / Resolution
  ↓
Closure Data Gate
  ↓
Reporting / Audit
```

Additional control points apply to:

* change authorization
* privileged requests
* vendor access
* SLA exceptions
* priority overrides
* automation failure
* AI-assisted decisions

Controls will be fully defined in:

[Governance and Controls](../06%20Governance%20and%20Controls/governance%20model.md)

---

# 19. Target-State Implementation Boundaries

The operating model intentionally does not attempt to solve everything at once.

Initial implementation should focus on:

* core intake
* Incident Management
* Service Request Management
* Change Management
* Knowledge Management
* ownership
* priority
* SLA
* approvals
* core data relationships
* RBAC
* reporting

Later maturity may expand:

* service catalog depth
* automation
* advanced asset / CI relationships
* additional integrations
* AI-assisted capabilities
* expanded ESM use outside IT

This keeps the initial implementation grounded.

A platform can be expanded later.

A bad operating model is much harder to unwind after people start depending on it.

---

# 20. Target Operating Model Success Criteria

The model is considered design-ready when the organization can answer the following:

* Which service activities require a managed record?
* Which channels create those records?
* Who owns each supported service?
* Which group owns each active ticket?
* How is priority determined?
* Which service levels apply?
* What triggers escalation?
* Which activities require approval?
* Who may approve them?
* Which records require asset or CI association?
* How are vendors represented?
* What information is required before closure?
* Which actions are automated?
* Which activities require human review?
* What metrics determine whether the process is improving?

If those answers remain unclear, the workflow is not ready to be configured.

---

# 21. Target Operating Model Conclusion

The target state replaces a service environment built around individual coordination with one built around visible ownership and repeatable workflow.

That does not mean removing technician judgment.

Technical judgment still matters in troubleshooting, diagnosis, resolution, risk evaluation, and exception handling.

What changes is where individual judgment is useful.

Technicians should spend judgment on the problem.

They should not have to reinvent the service process every time work arrives.

The target operating model establishes that process.

The next artifacts define its major components in more detail.

**Next:** [Service Catalog](./service%20catalog.md)
