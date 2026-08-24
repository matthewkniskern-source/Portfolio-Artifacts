# Functional Requirements

## Purpose

The functional requirements define how the target Enterprise Service Management environment must behave in order to satisfy the approved business requirements.

These requirements translate business outcomes into system behavior.

They remain vendor-neutral. A specific platform may implement the requirement through workflow rules, configuration, forms, business logic, integrations, automation, or another supported mechanism.

The requirement is the behavior.

The platform feature used to achieve it comes later.

Source requirements:

* [Business Requirements](./business%20requirements.md)
* [Requirements Discovery](./requirements%20discovery.md)
* [Pain Points and Failure Modes](../01%20Current%20State/pain%20points%20and%20failure%20modes.md)

---

# 1. Requirement Standard

Each functional requirement is written to be:

* specific
* testable
* traceable
* implementation-neutral where practical
* limited to one primary behavior

The word **shall** identifies required system behavior.

Where a function depends on organizational policy or technical integration, that dependency is identified rather than quietly assumed.

---

# 2. Functional Requirements Summary

| ID    | Functional Requirement                               | Priority           | Related BR   |
| ----- | ---------------------------------------------------- | ------------------ | ------------ |
| FR-01 | Create a unique managed service record               | Must               | BR-01        |
| FR-02 | Support approved intake channels                     | Must               | BR-02        |
| FR-03 | Enforce minimum intake data                          | Must               | BR-02        |
| FR-04 | Identify duplicate or related incidents              | Should             | BR-02, BR-14 |
| FR-05 | Apply impact and urgency values                      | Must               | BR-03        |
| FR-06 | Calculate priority using approved rules              | Must               | BR-03        |
| FR-07 | Control and document priority override               | Must               | BR-03        |
| FR-08 | Assign an owning support group                       | Must               | BR-04        |
| FR-09 | Preserve reassignment history                        | Must               | BR-04        |
| FR-10 | Require reassignment reason                          | Must               | BR-04        |
| FR-11 | Apply SLA timing rules                               | Must               | BR-05        |
| FR-12 | Generate SLA warnings and escalations                | Must               | BR-05        |
| FR-13 | Record SLA exceptions                                | Must               | BR-05        |
| FR-14 | Route approval-required records                      | Must               | BR-06        |
| FR-15 | Preserve structured approval history                 | Must               | BR-06        |
| FR-16 | Prevent prohibited self-approval                     | Must               | BR-07        |
| FR-17 | Associate users, services, assets, and CIs           | Should             | BR-08        |
| FR-18 | Link knowledge to service records                    | Should             | BR-09        |
| FR-19 | Support knowledge lifecycle states                   | Should             | BR-09        |
| FR-20 | Link changes to affected services and CIs            | Must               | BR-10        |
| FR-21 | Link incidents to relevant changes                   | Must               | BR-10        |
| FR-22 | Record change outcome and validation                 | Must               | BR-10        |
| FR-23 | Maintain internal ownership during vendor dependency | Must               | BR-11        |
| FR-24 | Record vendor support activity                       | Must               | BR-11        |
| FR-25 | Capture temporary/vendor access attributes           | Must               | BR-12        |
| FR-26 | Enforce or initiate access expiration                | Must               | BR-12        |
| FR-27 | Require record-type-specific closure data            | Must               | BR-13        |
| FR-28 | Support reopen handling                              | Must               | BR-13        |
| FR-29 | Support trend analysis using service data            | Should             | BR-14        |
| FR-30 | Provide standardized operational reporting           | Must               | BR-15        |
| FR-31 | Distinguish SLA-active and excluded time             | Must               | BR-15        |
| FR-32 | Execute approved workflow automation                 | Should             | BR-16        |
| FR-33 | Log automated actions and failures                   | Must               | BR-16        |
| FR-34 | Route failed automation to manual handling           | Must               | BR-16        |
| FR-35 | Support AI-assisted ticket summarization             | Could              | BR-17        |
| FR-36 | Support AI-assisted categorization                   | Could              | BR-17        |
| FR-37 | Support AI-assisted knowledge suggestion             | Could              | BR-17        |
| FR-38 | Support AI-assisted duplicate detection              | Could              | BR-17        |
| FR-39 | Distinguish AI recommendations from human decisions  | Must if AI enabled | BR-17        |
| FR-40 | Prevent autonomous restricted AI actions             | Must if AI enabled | BR-17        |
| FR-41 | Capture user feedback / satisfaction                 | Should             | BR-18        |
| FR-42 | Support configurable notifications                   | Should             | BR-18        |
| FR-43 | Maintain configuration and workflow change history   | Must               | BR-16, BR-18 |

---

# 3. Intake and Record Creation

## FR-01 — Unique Service Record

**Requirement**

The platform shall create a unique record identifier for each managed incident, service request, change, or other configured service-management record.

**Priority:** Must
**Related Business Requirement:** BR-01

**Acceptance Direction**

A newly created record receives a unique identifier and can be retrieved throughout its lifecycle.

---

## FR-02 — Approved Intake Channels

**Requirement**

The platform shall support creation of incident and service-request records through approved intake channels.

Approved channels may include:

* self-service portal
* service desk entry
* email integration
* approved automated integration
* authorized technician entry

**Priority:** Must
**Related Business Requirement:** BR-02

**Design Note**

A phone call or chat conversation does not need to disappear.

If the interaction becomes managed work, it needs a record.

---

## FR-03 — Minimum Intake Data

**Requirement**

The platform shall require defined minimum information before an incident or service request enters active fulfillment.

Minimum information may vary by record type and shall include, where applicable:

* requester
* request or incident description
* service or category
* affected user
* location
* impact
* relevant asset or CI

**Priority:** Must
**Related Business Requirement:** BR-02

**Acceptance Direction**

Incomplete submissions cannot enter a workflow state requiring information that has not been provided.

---

## FR-04 — Duplicate and Related Incident Association

**Requirement**

The platform shall support identification and association of duplicate or related incident records.

**Priority:** Should
**Related Business Requirements:** BR-02, BR-14

The solution shall support:

* duplicate designation
* related-record linkage
* parent/child incident relationships where required
* common incident association during broader service disruption

Detailed design:

[Incident Management](../04%20Workflow%20Design/incident%20management.md)

---

# 4. Priority Management

## FR-05 — Impact and Urgency

**Requirement**

The platform shall support defined impact and urgency values for applicable incident records.

**Priority:** Must
**Related Business Requirement:** BR-03

Values shall use business-readable definitions rather than relying solely on technical severity terminology.

---

## FR-06 — Calculated Priority

**Requirement**

The platform shall determine incident priority using the approved relationship between impact and urgency.

**Priority:** Must
**Related Business Requirement:** BR-03

The calculation model will be defined in:

[Priority and SLA Model](../03%20Target%20Service%20Model/priority%20and%20sla%20model.md)

---

## FR-07 — Priority Override

**Requirement**

Authorized personnel shall be able to override calculated priority only when an approved exception condition exists.

The platform shall record:

* original priority
* revised priority
* actor
* timestamp
* override reason

**Priority:** Must
**Related Business Requirement:** BR-03

This provides flexibility without making the priority model optional.

---

# 5. Assignment and Ownership

## FR-08 — Owning Support Group

**Requirement**

Each active service record shall have a defined owning support group where group ownership applies.

**Priority:** Must
**Related Business Requirement:** BR-04

Individual assignment may exist beneath group ownership, but the record shall not become ownerless during normal workflow transitions.

---

## FR-09 — Assignment History

**Requirement**

The platform shall maintain historical assignment information for each service record.

The history shall identify:

* previous owner or group
* new owner or group
* timestamp
* initiating actor or automated rule

**Priority:** Must
**Related Business Requirement:** BR-04

---

## FR-10 — Reassignment Reason

**Requirement**

Manual reassignment between support groups shall require a defined reassignment reason.

**Priority:** Must
**Related Business Requirement:** BR-04

Example reasons may include:

* incorrect initial assignment
* specialized support required
* service ownership transfer
* escalation
* vendor coordination

This data will later support reassignment analysis rather than treating every transfer as identical.

---

# 6. SLA and Escalation

## FR-11 — SLA Timer Behavior

**Requirement**

The platform shall start, pause, resume, and stop applicable SLA timers according to defined workflow conditions.

**Priority:** Must
**Related Business Requirement:** BR-05

Timer behavior shall distinguish between:

* active support time
* requester dependency
* approved scheduling
* vendor dependency where policy permits
* completed work
* documented exception

---

## FR-12 — SLA Warning and Escalation

**Requirement**

The platform shall generate defined actions as applicable SLA thresholds approach or are exceeded.

Actions may include:

* technician notification
* group notification
* manager escalation
* service-owner escalation
* dashboard indication

**Priority:** Must
**Related Business Requirement:** BR-05

---

## FR-13 — SLA Exception Documentation

**Requirement**

An SLA record excluded from standard performance treatment shall require an approved exception reason.

**Priority:** Must
**Related Business Requirement:** BR-05

The platform shall retain sufficient information to distinguish a legitimate exception from an unexplained missed target.

---

# 7. Approval Workflow

## FR-14 — Approval Routing

**Requirement**

The platform shall route records requiring approval to the appropriate approver or approval group based on defined business rules.

**Priority:** Must
**Related Business Requirement:** BR-06

Approval logic may consider:

* request type
* requester
* cost
* service
* privilege level
* change risk
* organizational relationship

---

## FR-15 — Approval History

**Requirement**

The platform shall retain structured approval history.

Approval history shall include:

* approver
* decision
* date and time
* associated record
* comments where required

**Priority:** Must
**Related Business Requirement:** BR-06

Email alone shall not serve as the authoritative approval record for controlled workflows.

---

## FR-16 — Self-Approval Prevention

**Requirement**

The platform shall prevent a requester from approving their own request where separation of duties is required.

**Priority:** Must
**Related Business Requirement:** BR-07

This requirement applies only to designated controlled workflows.

Routine work should not inherit approval controls simply because the platform can support them.

Detailed control design:

[RBAC and Approval Controls](../06%20Governance%20and%20Controls/rbac%20and%20approval%20controls.md)

---

# 8. Service, Asset, and Configuration Relationships

## FR-17 — Operational Relationship Data

**Requirement**

The platform shall support association of service records with relevant:

* users
* services
* assets
* configuration items
* support groups
* locations

**Priority:** Should
**Related Business Requirement:** BR-08

Not every field must be populated for every record.

Relationships should be required where they materially support service delivery, impact analysis, change management, or reporting.

Detailed model:

[Service Management Data Model](../05%20Data%20and%20Configuration%20Model/service%20management%20data%20model.md)

---

# 9. Knowledge Management

## FR-18 — Knowledge Association

**Requirement**

The platform shall support association of knowledge articles with incidents, service requests, services, and other applicable records.

**Priority:** Should
**Related Business Requirement:** BR-09

---

## FR-19 — Knowledge Lifecycle

**Requirement**

The platform shall support defined knowledge lifecycle states.

At minimum:

```text id="u8kxn2"
Draft
  ↓
Review
  ↓
Approved
  ↓
Published
  ↓
Review / Update
  ↓
Retired
```

The model shall support:

* article owner
* reviewer
* publication status
* review date
* expiration or retirement
* usage history where available

Detailed workflow:

[Knowledge Management](../04%20Workflow%20Design/knowledge%20management.md)

---

# 10. Change Management

## FR-20 — Change Relationship to Services and CIs

**Requirement**

Each applicable change record shall support association with affected services and configuration items.

**Priority:** Must
**Related Business Requirement:** BR-10

This relationship supports both pre-change impact assessment and post-change troubleshooting.

---

## FR-21 — Incident and Change Relationship

**Requirement**

The platform shall support association between incident records and relevant change records.

**Priority:** Must
**Related Business Requirement:** BR-10

The relationship shall be visible from both records where practical.

---

## FR-22 — Change Outcome and Validation

**Requirement**

A change record shall capture its implementation outcome before final closure.

Supported outcomes shall distinguish at minimum:

* successful
* successful with issue
* unsuccessful / backed out

The workflow shall capture:

* implementation result
* validation result
* backout status where applicable
* resulting incident where applicable

**Priority:** Must
**Related Business Requirement:** BR-10

Detailed workflow:

[Change Management](../04%20Workflow%20Design/change%20management.md)

---

# 11. Vendor-Supported Work

## FR-23 — Internal Ownership During Vendor Dependency

**Requirement**

A service record awaiting vendor action shall retain a defined internal owner.

**Priority:** Must
**Related Business Requirement:** BR-11

`Waiting on Vendor` may describe status.

It shall not replace accountability.

---

## FR-24 — Vendor Activity Record

**Requirement**

The platform shall support recording vendor involvement in applicable service activity.

The record shall support:

* vendor identity
* vendor case or reference number
* internal owner
* current vendor status
* latest material interaction
* associated service or CI where applicable

**Priority:** Must
**Related Business Requirement:** BR-11

The internal ESM record remains the authoritative internal history even when the vendor uses a separate support portal.

---

# 12. Temporary and Vendor Access

## FR-25 — Temporary Access Attributes

**Requirement**

Temporary or vendor access requests shall capture, where applicable:

* requester
* internal sponsor
* user or vendor
* business purpose
* target service or system
* requested privilege
* start date/time
* expiration date/time
* approving authority

**Priority:** Must
**Related Business Requirement:** BR-12

---

## FR-26 — Access Expiration

**Requirement**

The solution shall initiate or enforce expiration of approved temporary access at the defined expiration point where technical integration permits.

**Priority:** Must
**Related Business Requirement:** BR-12

Where automatic disablement is not technically available, the platform shall generate a tracked expiration action for an accountable internal owner.

This avoids pretending that workflow automation can perform a control the connected system does not actually support.

---

# 13. Resolution and Closure

## FR-27 — Required Closure Data

**Requirement**

The platform shall require defined closure information before applicable records reach final closed status.

Required information may include:

* resolution category
* resolution summary
* action performed
* affected service or CI
* change relationship
* knowledge relationship
* closure code

**Priority:** Must
**Related Business Requirement:** BR-13

The exact requirement shall vary by record type.

A password reset does not need the same closure record as a P1 infrastructure incident.

---

## FR-28 — Reopen Handling

**Requirement**

The platform shall support reopening a recently resolved record where defined criteria are met.

**Priority:** Must
**Related Business Requirement:** BR-13

Reopening shall retain previous resolution history and record the reopen reason.

---

# 14. Trend and Pattern Analysis

## FR-29 — Service Trend Analysis

**Requirement**

The platform shall support analysis of service activity using available structured data.

Analysis shall support filtering or grouping by applicable fields including:

* category
* service
* CI
* asset
* location
* support group
* priority
* resolution
* related change
* time period

**Priority:** Should
**Related Business Requirement:** BR-14

This creates the data foundation for recurring-issue identification without assuming that every statistical cluster is automatically a root cause.

---

# 15. Reporting

## FR-30 — Operational Reporting

**Requirement**

The platform shall provide standardized reporting for approved service-management metrics.

At minimum, reporting shall support:

* ticket volume
* first response
* resolution time
* SLA compliance
* backlog
* backlog age
* reassignment
* reopen activity
* change outcomes
* knowledge usage
* vendor dependency
* customer feedback

**Priority:** Must
**Related Business Requirement:** BR-15

Detailed definitions:

[Performance Framework](../11%20Metrics%20and%20Optimization/performance%20framework.md)

---

## FR-31 — SLA Time Classification

**Requirement**

Reporting shall distinguish time counted toward SLA performance from time excluded under approved pause or exception conditions.

**Priority:** Must
**Related Business Requirement:** BR-15

Without this distinction, an SLA percentage may be mathematically correct but operationally meaningless.

---

# 16. Workflow Automation

## FR-32 — Approved Automation

**Requirement**

The platform shall support automated workflow actions based on documented business rules.

**Priority:** Should
**Related Business Requirement:** BR-16

Candidate automation includes:

* ticket routing
* SLA warnings
* escalation
* approval routing
* reminders
* expiration actions
* change notifications
* status transitions where appropriate

Detailed design:

[Automation Opportunities](../07%20Automation%20and%20AI/automation%20opportunities.md)

---

## FR-33 — Automation Logging

**Requirement**

The platform shall record material automated workflow actions.

Records shall include, where applicable:

* automation rule
* affected record
* action
* timestamp
* success or failure status

**Priority:** Must
**Related Business Requirement:** BR-16

Automation should not become invisible system behavior that nobody can reconstruct later.

---

## FR-34 — Automation Exception Handling

**Requirement**

Failed automated actions that prevent required workflow completion shall create a defined manual exception path.

**Priority:** Must
**Related Business Requirement:** BR-16

The exception shall identify:

* failed action
* affected record
* time of failure
* required follow-up
* responsible group where applicable

The system should fail visibly rather than silently pretending the workflow completed.

---

# 17. AI-Assisted Service Management

AI-assisted functions are treated as optional capabilities layered onto a stable service process.

They are not dependencies for initial service-management operation.

## FR-35 — Ticket Summarization

**Requirement**

Where AI functionality is enabled, the platform may generate a concise summary of ticket history for human review.

**Priority:** Could
**Related Business Requirement:** BR-17

---

## FR-36 — Suggested Categorization

**Requirement**

Where AI functionality is enabled, the platform may recommend ticket category, subcategory, service, or assignment based on available record data.

**Priority:** Could
**Related Business Requirement:** BR-17

Authorized users shall be able to correct the recommendation.

---

## FR-37 — Knowledge Recommendation

**Requirement**

Where AI functionality is enabled, the platform may recommend relevant approved knowledge articles based on ticket context.

**Priority:** Could
**Related Business Requirement:** BR-17

---

## FR-38 — Duplicate Detection

**Requirement**

Where AI functionality is enabled, the platform may identify records that appear to represent duplicate or related service conditions.

**Priority:** Could
**Related Business Requirement:** BR-17

Human confirmation shall remain available before material record consolidation.

---

## FR-39 — AI Attribution

**Requirement**

AI-generated recommendations, summaries, or drafted content shall be distinguishable from human-authored decisions where the distinction is material to workflow or auditability.

**Priority:** Must if AI enabled
**Related Business Requirement:** BR-17

---

## FR-40 — Restricted AI Actions

**Requirement**

AI-assisted capabilities shall not independently perform designated restricted actions.

Restricted actions shall include at minimum:

* privileged-access approval
* high-risk change authorization
* approval-rule bypass
* access-control modification
* audit-record deletion or alteration

**Priority:** Must if AI enabled
**Related Business Requirement:** BR-17

Detailed governance:

[AI Governance](../07%20Automation%20and%20AI/ai%20governance.md)

---

# 18. User Feedback and Communication

## FR-41 — Service Feedback

**Requirement**

The platform shall support structured end-user feedback following applicable service interactions.

**Priority:** Should
**Related Business Requirement:** BR-18

Feedback may include:

* satisfaction rating
* optional comment
* service or interaction context

The organization should avoid survey fatigue by applying feedback requests selectively.

---

## FR-42 — Configurable Notifications

**Requirement**

The platform shall support configurable stakeholder notifications triggered by defined workflow events.

**Priority:** Should
**Related Business Requirement:** BR-18

Potential events include:

* ticket creation
* assignment
* approval required
* approval decision
* SLA warning
* material status change
* resolution
* closure
* change implementation
* vendor follow-up

Notification design should avoid turning every workflow transition into another email.

---

# 19. Platform Configuration Governance

## FR-43 — Configuration Change History

**Requirement**

Material production configuration changes shall be traceable through an approved change record or equivalent controlled configuration process.

**Priority:** Must
**Related Business Requirements:** BR-16, BR-18

Applicable configuration includes:

* workflow logic
* SLA rules
* routing
* permissions
* approval logic
* automation
* production forms
* integrations

The platform used to manage change should not itself become an uncontrolled source of change.

---

# 20. Functional Requirement Dependencies

Several requirements rely on foundational capabilities.

```text id="jd3kk8"
Reliable Intake
FR-01 → FR-02 → FR-03
                  ↓
            Classification
                  ↓
Priority → Ownership → SLA
FR-05/06   FR-08     FR-11
    ↓         ↓         ↓
   Routing / Escalation
             ↓
      Resolution / Closure
             ↓
          Reporting
```

A second dependency chain applies to governance:

```text id="d49d8o"
Identity / Role
      ↓
Approval Routing
      ↓
Separation of Duties
      ↓
Controlled Fulfillment
      ↓
Audit History
```

And the data model supports several workflows simultaneously:

```text id="h85jlr"
User
 ↓
Ticket → Service → CI / Asset
  ↓        ↓          ↓
Knowledge  Change ← Vendor
```

These relationships will be represented visually in later design artifacts rather than treated as isolated platform features.

---

# 21. Functional Requirement Validation

A functional requirement is considered design-ready when:

* its related business requirement is identified
* expected system behavior is clear
* required inputs are understood
* expected outputs are understood
* exception behavior is identified where necessary
* dependencies are known
* the requirement can be tested
* the requirement does not unnecessarily depend on a named vendor feature

If the implementation team cannot explain how a requirement will be tested, it should not be treated as complete.

---

# 22. Functional Requirements to Testing

The functional requirements will directly inform UAT.

Representative future mappings include:

| Functional Requirement | Planned Test                             |
| ---------------------- | ---------------------------------------- |
| FR-06                  | P1 incident priority calculation         |
| FR-10                  | Ticket reassignment with required reason |
| FR-11                  | SLA pause and resume behavior            |
| FR-12                  | SLA breach escalation                    |
| FR-14                  | Hardware request approval routing        |
| FR-16                  | Prohibited self-approval                 |
| FR-21                  | Failed change linked to incident         |
| FR-26                  | Vendor access expiration                 |
| FR-27                  | Required closure information             |
| FR-34                  | Failed automation exception handling     |
| FR-40                  | Restricted AI action blocked             |

Full mappings will be maintained in:

[Requirements Traceability Matrix](./requirements%20traceability%20matrix.md)

and

[Requirements-to-Test Traceability](../09%20Testing%20and%20UAT/requirements%20test%20traceability.md)

---

# 23. Functional Requirements Conclusion

The business requirements define what the organization needs.

These functional requirements define the behavior required to support those outcomes.

They deliberately stop short of deciding exactly how a specific platform should be configured.

That separation gives the implementation team room to use standard platform capability where it fits without allowing the tool to dictate the process.

The next step is to define the nonfunctional conditions the solution must satisfy around security, availability, usability, maintainability, data handling, and auditability.

**Next:** [Nonfunctional Requirements](./nonfunctional%20requirements.md)
