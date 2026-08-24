# Business Requirements

## Purpose

The business requirements define what the organization needs the Enterprise Service Management transformation to accomplish.

They are intentionally written at the outcome level.

They do not prescribe a specific vendor, product feature, configuration method, or technical implementation. Those decisions belong in the functional requirements and later solution design.

The requirements are derived from the current-state findings documented in:

* [Current State Assessment](../01%20Current%20State/current%20state%20assessment.md)
* [Stakeholder Map](../01%20Current%20State/stakeholder%20map.md)
* [Pain Points and Failure Modes](../01%20Current%20State/pain%20points%20and%20failure%20modes.md)
* [Baseline Metrics](../01%20Current%20State/baseline%20metrics.md)

The core rule is simple:

> **Every business requirement should solve a real operating problem or establish a necessary control.**

If it cannot be traced back to a business need, it probably does not belong in the initial implementation.

---

# 1. Requirement Priority

Business requirements are assigned one of three priorities.

| Priority | Meaning                                                                                           |
| -------- | ------------------------------------------------------------------------------------------------- |
| Must     | Required for the initial operating model, governance, or credible go-live                         |
| Should   | Important capability that should be delivered when practical but does not block initial operation |
| Could    | Useful enhancement that may be introduced after the core model is stable                          |

Priority reflects business dependency and implementation value, not stakeholder preference alone.

---

# 2. Business Requirements Summary

| ID    | Business Requirement                                                 | Priority | Primary Owner                  | Source                          |
| ----- | -------------------------------------------------------------------- | -------- | ------------------------------ | ------------------------------- |
| BR-01 | Maintain an authoritative record for managed service activity        | Must     | IT Management                  | FM-01, FM-15                    |
| BR-02 | Provide consistent service intake across approved channels           | Must     | Service Management Owner       | FM-01, FM-02                    |
| BR-03 | Apply consistent business-based prioritization                       | Must     | IT Management                  | FM-03                           |
| BR-04 | Maintain clear ownership throughout the service lifecycle            | Must     | Service Management Owner       | FM-04                           |
| BR-05 | Define measurable service levels and escalation expectations         | Must     | IT Management / Service Owners | FM-05                           |
| BR-06 | Maintain auditable approval records                                  | Must     | Process Owners                 | FM-06                           |
| BR-07 | Separate request, approval, and fulfillment where required           | Must     | Security / Process Owners      | FM-07                           |
| BR-08 | Relate service activity to relevant users, services, assets, and CIs | Should   | Service / CI Owners            | FM-08                           |
| BR-09 | Capture and reuse operational knowledge                              | Should   | Service Management Owner       | FM-09                           |
| BR-10 | Maintain traceability between changes, services, CIs, and incidents  | Must     | Change Process Owner           | FM-10                           |
| BR-11 | Maintain internal accountability for vendor-supported work           | Must     | Service Owners                 | FM-11                           |
| BR-12 | Govern temporary and vendor access throughout its lifecycle          | Must     | Security / Access Owners       | FM-12                           |
| BR-13 | Maintain useful and complete closure records                         | Must     | Process Owners                 | FM-13                           |
| BR-14 | Identify recurring service issues and operational trends             | Should   | IT Management                  | FM-14                           |
| BR-15 | Produce management reporting from consistent service data            | Must     | IT Management                  | FM-15                           |
| BR-16 | Use automation to enforce approved and repeatable business rules     | Should   | Platform / Process Owners      | FM-16                           |
| BR-17 | Govern AI-assisted service-management capabilities                   | Should   | IT Management / Security       | FM-16                           |
| BR-18 | Support adoption, training, feedback, and continuous improvement     | Must     | Implementation Sponsor         | Stakeholder / Baseline Findings |

---

# 3. Detailed Business Requirements

## BR-01 — Authoritative Service Record

**Requirement**

The organization shall maintain an authoritative record for managed service activity.

**Business Rationale**

The current environment allows work to remain in email, chat, phone conversations, spreadsheets, and individual technician workflows.

That makes workload, service history, accountability, and reporting incomplete.

The target model does not need to eliminate every informal interaction. It does need to ensure that work requiring tracking, ownership, authorization, escalation, historical context, or measurement becomes part of the managed service record.

**Priority:** Must

**Primary Owner:** IT Management

**Source:** FM-01, FM-15

**Acceptance Direction**

The organization can identify active managed work, current ownership, status, and historical activity from a common service-management record.

---

## BR-02 — Consistent Service Intake

**Requirement**

The organization shall provide consistent intake for incidents and service requests across approved service channels.

**Business Rationale**

Multiple intake channels are acceptable as long as they feed a common process.

The current problem is not that users can email, call, or submit a form. The problem is that those channels can produce different levels of documentation, ownership, and visibility.

The target model should allow practical user access without creating parallel service processes.

**Priority:** Must

**Primary Owner:** Service Management Owner

**Source:** FM-01, FM-02

**Acceptance Direction**

Approved intake channels create or update a managed service record using defined minimum information.

---

## BR-03 — Consistent Prioritization

**Requirement**

The organization shall prioritize managed service work using defined business impact and urgency criteria.

**Business Rationale**

Priority should reflect the effect on the business, not which requester contacts support most aggressively.

A consistent model improves:

* resource allocation
* escalation
* SLA performance
* management confidence
* fairness across service consumers

**Priority:** Must

**Primary Owner:** IT Management

**Source:** FM-03

**Acceptance Direction**

Equivalent impact and urgency conditions produce equivalent priority unless an authorized and documented exception is applied.

Related design:

[Priority and SLA Model](../03%20Target%20Service%20Model/priority%20and%20sla%20model.md)

---

## BR-04 — Clear Service Ownership

**Requirement**

The organization shall maintain clear ownership of active service work throughout the ticket lifecycle.

**Business Rationale**

A ticket moving between groups should never create ambiguity about who is currently responsible for moving it forward.

The target operating model should distinguish between:

* current ownership
* technical participation
* escalation
* reassignment
* approval responsibility

A handoff should transfer responsibility deliberately rather than leave the ticket floating between teams.

**Priority:** Must

**Primary Owner:** Service Management Owner

**Source:** FM-04

**Acceptance Direction**

Every active service record has a defined owning group and historical ownership remains traceable.

---

## BR-05 — Service Levels and Escalation

**Requirement**

The organization shall define measurable service-level expectations and escalation behavior for supported services and request types.

**Business Rationale**

Service expectations cannot be governed consistently if timers, pause conditions, and escalation paths are informal.

The future model should clearly define:

* response expectations
* resolution or fulfillment expectations
* warning thresholds
* pause conditions
* exception conditions
* escalation responsibility

The point is not to create an SLA for every possible interaction.

The point is to make the service commitments that do exist measurable and defensible.

**Priority:** Must

**Primary Owner:** IT Management / Service Owners

**Source:** FM-05

**Acceptance Direction**

Applicable service records can be measured against documented service targets using consistent start, pause, resume, and completion logic.

---

## BR-06 — Auditable Approvals

**Requirement**

The organization shall maintain auditable approval records for service activities requiring authorization.

**Business Rationale**

An approval buried in email or chat may be enough to keep work moving, but it is a poor control record.

Where approval is required, the organization should be able to determine:

* what was approved
* who approved it
* when it was approved
* what state the request was in
* whether it was approved, rejected, or returned

**Priority:** Must

**Primary Owner:** Process Owners

**Source:** FM-06

**Acceptance Direction**

Controlled requests contain a structured and retained approval history.

---

## BR-07 — Separation of Duties

**Requirement**

The organization shall maintain appropriate separation between request, approval, and fulfillment for designated controlled activities.

**Business Rationale**

Having permission to approve a type of request should not automatically mean a user can approve their own transaction.

This requirement is especially relevant to:

* privileged access
* sensitive access
* higher-cost purchases
* selected infrastructure changes
* high-risk changes

Controls should be proportional to risk.

Routine work should not be burdened with unnecessary approval layers.

**Priority:** Must

**Primary Owner:** Security / Process Owners

**Source:** FM-07

**Acceptance Direction**

Defined controlled activities cannot bypass required separation-of-duty rules.

---

## BR-08 — Service and Configuration Context

**Requirement**

Service records shall provide relevant relationships to users, services, assets, and configuration items where those relationships support operational decisions.

**Business Rationale**

The objective is not to build the largest possible configuration database.

The organization needs enough context to answer useful questions:

* What does this incident affect?
* Who uses it?
* What service depends on it?
* Was it recently changed?
* Who owns it?
* Is a vendor involved?

Data relationships should exist because they support troubleshooting, impact analysis, change management, or reporting.

**Priority:** Should

**Primary Owner:** Service / CI Owners

**Source:** FM-08

**Acceptance Direction**

Applicable service records can be associated with relevant service and configuration context without requiring unnecessary data population.

---

## BR-09 — Operational Knowledge Reuse

**Requirement**

The organization shall capture and reuse operational knowledge where doing so improves service delivery.

**Business Rationale**

Technical knowledge should not repeatedly disappear into closed tickets, inboxes, or individual memory.

The target knowledge process should make it easier to reuse:

* proven resolutions
* support procedures
* known workarounds
* recurring troubleshooting patterns

Not every ticket needs to become a knowledge article.

The goal is useful knowledge, not documentation volume.

**Priority:** Should

**Primary Owner:** Service Management Owner

**Source:** FM-09

**Acceptance Direction**

Support teams can create, find, reuse, and maintain validated knowledge relevant to service work.

---

## BR-10 — Change Traceability

**Requirement**

The organization shall maintain traceability between changes, affected services and configuration items, implementation outcomes, and resulting incidents where applicable.

**Business Rationale**

A recently implemented change is often one of the first things an incident responder should know.

Change and incident processes should therefore support each other rather than operate as isolated records.

**Priority:** Must

**Primary Owner:** Change Process Owner

**Source:** FM-10

**Acceptance Direction**

Relevant incidents can identify related changes and relevant changes can identify affected services, CIs, and post-implementation outcomes.

---

## BR-11 — Vendor Accountability

**Requirement**

Vendor-supported work shall remain visible and accountable within the organization's internal service-management process.

**Business Rationale**

Opening a vendor case should not cause internal ownership to disappear.

The organization still needs to know:

* who owns the internal issue
* which vendor is involved
* what action is pending
* when follow-up is expected
* what outcome was received

The internal service record remains authoritative even if part of the technical work occurs in an external vendor system.

**Priority:** Must

**Primary Owner:** Service Owners

**Source:** FM-11

**Acceptance Direction**

Vendor-dependent work retains a defined internal owner and sufficient vendor activity history to support operational follow-up.

---

## BR-12 — Temporary and Vendor Access Governance

**Requirement**

Temporary, vendor, and designated privileged access shall be governed throughout the access lifecycle.

**Business Rationale**

Temporary access should actually be temporary.

Where access is granted for a specific support or implementation need, the organization should retain:

* sponsor
* purpose
* scope
* start
* expiration
* approval
* extension history where applicable

Access should not remain active simply because no one remembered to remove it.

**Priority:** Must

**Primary Owner:** Security / Access Owners

**Source:** FM-12

**Acceptance Direction**

Applicable temporary access has defined authorization, scope, ownership, and expiration.

---

## BR-13 — Closure Record Quality

**Requirement**

Closed service records shall contain sufficient information to support historical review, troubleshooting, reporting, and auditability.

**Business Rationale**

A status of `Closed` is not the same thing as a useful resolution record.

Closure information should be proportional to the work performed but should leave enough context to understand:

* what happened
* what action was taken
* what resolved the issue
* what was affected
* whether follow-up is required

**Priority:** Must

**Primary Owner:** Process Owners

**Source:** FM-13

**Acceptance Direction**

Records cannot complete the defined closure workflow without required closure information.

---

## BR-14 — Recurring Issue Identification

**Requirement**

The organization shall be capable of identifying recurring service issues and operational patterns.

**Business Rationale**

Resolving the same issue five times is not the same thing as solving the underlying problem.

The target service model should support pattern identification using available service data such as:

* category
* service
* configuration item
* location
* time
* resolution
* related change

**Priority:** Should

**Primary Owner:** IT Management

**Source:** FM-14

**Acceptance Direction**

Management and service owners can identify repeated or clustered service conditions for further investigation.

---

## BR-15 — Reliable Management Reporting

**Requirement**

Management reporting shall be based on consistently captured and defined service-management data.

**Business Rationale**

More dashboards do not fix incomplete data.

Before service metrics can support management decisions, the organization must improve:

* transaction capture
* status consistency
* priority consistency
* ownership
* closure data
* exception handling

The reporting layer should reflect the process rather than compensate for it.

**Priority:** Must

**Primary Owner:** IT Management

**Source:** FM-15

**Acceptance Direction**

Published service metrics use documented definitions and identifiable source data.

---

## BR-16 — Controlled Automation

**Requirement**

Automation shall support approved, repeatable business rules and provide defined handling for exceptions or failures.

**Business Rationale**

Automation should remove unnecessary manual effort from stable processes.

It should not be used to hide unresolved process decisions.

Appropriate examples include:

* routing
* SLA warnings
* reminders
* approval notifications
* expiration
* change notifications

The operating principle remains:

> **Automate repeatable decisions. Do not use automation to avoid making the decision in the first place.**

**Priority:** Should

**Primary Owner:** Platform / Process Owners

**Source:** FM-16

**Acceptance Direction**

Automated actions are based on documented rules, produce traceable outcomes, and provide a manual exception path when they fail.

---

## BR-17 — Responsible AI Assistance

**Requirement**

AI-assisted service-management capabilities shall support human decision-making while maintaining defined restrictions for sensitive, privileged, or governance-related actions.

**Business Rationale**

AI may add value in areas such as:

* summarization
* categorization
* knowledge recommendation
* duplicate detection
* response drafting
* trend identification

Those uses are materially different from allowing AI to independently:

* approve privileged access
* authorize a high-risk change
* alter access rights
* close sensitive exceptions
* override governance controls

AI should reduce administrative work without becoming an unaccountable decision authority.

**Priority:** Should

**Primary Owner:** IT Management / Security

**Source:** FM-16

**Acceptance Direction**

AI-assisted activity is identifiable, reviewable, correctable, and restricted from designated autonomous actions.

Related design:

[Automation and AI](../07%20Automation%20and%20AI/automation%20opportunities.md)

---

## BR-18 — Adoption and Continuous Improvement

**Requirement**

The organization shall support user adoption, role-based training, feedback, and continuous improvement throughout and after implementation.

**Business Rationale**

The implementation fails operationally if users and technicians immediately recreate the old process around the new platform.

Adoption therefore directly affects:

* service capture
* data quality
* reporting
* SLA accuracy
* knowledge reuse
* workflow consistency

Training and adoption are not separate from implementation quality.

They are part of it.

**Priority:** Must

**Primary Owner:** Implementation Sponsor

**Source:** Stakeholder and baseline findings

**Acceptance Direction**

Affected stakeholder groups receive appropriate training, support, communication, and post-go-live feedback mechanisms.

---

# 4. Requirement Ownership

Business ownership should remain separate from technical configuration ownership.

| Responsibility                 | Role                                      |
| ------------------------------ | ----------------------------------------- |
| Define business outcome        | Business / Process Owner                  |
| Validate operational need      | Stakeholders                              |
| Approve requirement            | Authorized Process or Management Owner    |
| Translate into system behavior | Business Analyst / Implementation Team    |
| Configure solution             | Platform Administrator                    |
| Validate configuration         | Process Owner / UAT Participants          |
| Approve production release     | Defined Change / Implementation Authority |

This prevents an implementation team from quietly turning configuration choices into business policy.

---

# 5. Business Requirement Relationships

Several requirements intentionally work together.

### Service Record Integrity

```text
BR-01 Authoritative Record
        ↓
BR-02 Consistent Intake
        ↓
BR-04 Clear Ownership
        ↓
BR-13 Closure Quality
        ↓
BR-15 Reliable Reporting
```

### Controlled Service Decisions

```text
BR-03 Priority
        ↓
BR-05 SLA / Escalation
        ↓
BR-06 Approval
        ↓
BR-07 Separation of Duties
```

### Operational Context

```text
BR-08 Assets / CIs
        ↓
BR-10 Change Traceability
        ↓
BR-14 Trend Identification
```

### External and Automated Activity

```text
BR-11 Vendor Accountability
        ↓
BR-12 Access Governance

BR-16 Automation
        ↓
BR-17 AI Governance
```

A consolidated view will later be incorporated into the:

[Requirements Traceability Matrix](./requirements%20traceability%20matrix.md)

---

# 6. Requirement Validation Checklist

Before a business requirement is considered approved for design, it should answer:

* Is there a documented business or operational need?
* Is the expected outcome clear?
* Is an accountable owner identified?
* Can the requirement be validated?
* Does it unnecessarily prescribe a specific platform solution?
* Does it conflict with another requirement?
* Does it create avoidable operational burden?
* Does it depend on an assumption that has not been validated?
* Is it required for initial go-live, or can it reasonably wait?

A requirement that fails these checks should be revised before it drives configuration.

---

# 7. Business Requirements Conclusion

These requirements establish the outcomes the target service model must deliver.

They are intentionally broader than platform behavior.

The next step is to translate them into functional requirements that define how the future ESM environment must behave.

The chain remains:

**Current-State Failure → Business Requirement → Functional Behavior → Workflow / Control → Test → Metric**

That traceability is what keeps the implementation centered on the original business problem instead of drifting into feature configuration.

**Next:** [Functional Requirements](./functional%20requirements.md)
