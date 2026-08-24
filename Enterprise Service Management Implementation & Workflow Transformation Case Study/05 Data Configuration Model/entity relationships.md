# Entity Relationships

## Purpose

This artifact defines the key relationships among service-management entities and explains why each relationship exists.

The [Service Management Data Model](./service%20management%20data%20model.md) establishes the major entities.

This document focuses on how those entities connect.

The goal is not to maximize relationship count.

It is to make the relationships that matter:

* understandable
* maintainable
* testable
* reportable
* useful to workflow

The basic design rule is:

> **A relationship should exist because it improves an operational decision, control, or measurement.**

---

# 1. Relationship Summary

| Source Entity     | Relationship          | Target Entity        | Cardinality | Requirement                 | Primary Use                   |
| ----------------- | --------------------- | -------------------- | ----------- | --------------------------- | ----------------------------- |
| User              | creates               | Ticket               | 1:M         | Required                    | Requester traceability        |
| User              | belongs to            | Support Group        | M:1         | Conditional                 | Technician ownership          |
| User              | performs              | Approval             | 1:M         | Conditional                 | Authorization traceability    |
| Ticket            | relates to            | Service              | M:1         | Required where identifiable | Routing, SLA, reporting       |
| Ticket            | owned by              | Support Group        | M:1         | Required while active       | Accountability                |
| Ticket            | affects               | Asset                | M:M         | Conditional                 | User/device context           |
| Ticket            | affects               | Configuration Item   | M:M         | Conditional                 | Technical context             |
| Ticket            | related to            | Change               | M:M         | Conditional                 | Change correlation            |
| Ticket            | uses                  | Knowledge Article    | M:M         | Optional                    | Resolution reuse              |
| Ticket            | depends on            | Vendor               | M:M         | Conditional                 | External support tracking     |
| Ticket            | requires              | Approval             | 1:M         | Conditional                 | Controlled fulfillment        |
| Service           | supported by          | Support Group        | M:M         | Required                    | Ownership and routing         |
| Service           | contains / depends on | Configuration Item   | 1:M or M:M  | Conditional                 | Impact analysis               |
| Service           | documented by         | Knowledge Article    | 1:M         | Optional                    | Support knowledge             |
| Service           | affected by           | Change               | M:M         | Conditional                 | Change visibility             |
| Change            | modifies              | Configuration Item   | M:M         | Required where applicable   | Impact and validation         |
| Change            | requires              | Approval             | 1:M         | Conditional                 | Authorization                 |
| Change            | implemented with      | Vendor               | M:M         | Conditional                 | External change support       |
| Vendor            | supports              | Configuration Item   | 1:M or M:M  | Conditional                 | Support dependency            |
| Asset             | represented by        | Configuration Item   | 1:1 or 1:M  | Conditional                 | Lifecycle / technical context |
| Knowledge Article | owned by              | Support Group / User | M:1         | Required                    | Content accountability        |

---

# 2. Relationship Classification

Relationships are classified as:

| Classification            | Meaning                                                            |
| ------------------------- | ------------------------------------------------------------------ |
| Required                  | Workflow cannot operate correctly without it                       |
| Required Where Applicable | Required when the business condition exists                        |
| Optional                  | Useful but not necessary for every record                          |
| Derived                   | Created through another authoritative relationship where supported |

This prevents the data model from becoming overly rigid.

For example:

**Ticket → Requester**

is required.

**Ticket → Vendor**

only matters when a vendor is actually involved.

---

# 3. User Relationships

## User → Ticket

**Relationship:** User creates or is affected by Ticket
**Cardinality:** One-to-Many
**Requirement:** Required

A user may create many tickets.

Each ticket must identify a requester.

Where appropriate, the requester and affected user may be different.

Example:

```text id="itw4qi"
Manager
  ↓ creates
Service Request
  ↓ affects
Employee
```

This supports:

* request history
* communication
* approval routing
* reporting
* user context

---

## User → Support Group

**Relationship:** User belongs to Support Group
**Cardinality:** Many-to-One / Many-to-Many where needed
**Requirement:** Conditional

This relationship applies primarily to support personnel.

It supports:

* assignment
* RBAC
* queue visibility
* escalation

Membership should come from a controlled administrative source rather than manual ticket-level selection.

---

## User → Approval

**Relationship:** User performs Approval
**Cardinality:** One-to-Many
**Requirement:** Required where approval exists

The relationship preserves:

* approver identity
* authority
* decision history

This is critical to separation-of-duty controls.

---

# 4. Ticket Relationships

## Ticket → Service

**Relationship:** Ticket relates to Service
**Cardinality:** Many-to-One
**Requirement:** Required where identifiable

This is one of the most important relationships in the model.

It supports:

* ownership
* priority
* SLA
* reporting
* service-level trend analysis

A service record without service context may still be valid during initial triage, but the relationship should be established where reasonably possible.

---

## Ticket → Support Group

**Relationship:** Ticket owned by Support Group
**Cardinality:** Many-to-One
**Requirement:** Required while active

This relationship establishes operational accountability.

The active record should never lose group ownership during:

* waiting
* approval
* vendor dependency
* escalation

Ownership history remains traceable when the relationship changes.

---

## Ticket → Asset

**Relationship:** Ticket affects or references Asset
**Cardinality:** Many-to-Many
**Requirement:** Conditional

This supports cases such as:

```text id="yrvgyv"
User
 ↓
Incident
 ↓
Laptop Asset
```

or:

```text id="nbmgl5"
Service Request
 ↓
Replacement Asset
```

Asset relationships primarily support:

* lifecycle
* ownership
* warranty
* assignment history

---

## Ticket → Configuration Item

**Relationship:** Ticket affects Configuration Item
**Cardinality:** Many-to-Many
**Requirement:** Conditional

This supports:

* technical troubleshooting
* repeat-incident analysis
* impact analysis
* change correlation

Example:

```text id="49mghr"
Incident
   ↓
Application CI
   ↓
Business Service
```

---

## Ticket → Change

**Relationship:** Ticket related to Change
**Cardinality:** Many-to-Many
**Requirement:** Conditional

This relationship may indicate:

* incident caused by change
* request requiring change
* incident requiring permanent corrective change

The relationship should indicate context where the platform supports relationship type.

---

## Ticket → Knowledge Article

**Relationship:** Ticket uses or produces Knowledge Article
**Cardinality:** Many-to-Many
**Requirement:** Optional

This supports:

* resolution reuse
* knowledge effectiveness
* knowledge candidate creation

Example:

```text id="r8y55a"
Incident
  ↓
Knowledge Used
  ↓
Resolution
```

---

## Ticket → Vendor

**Relationship:** Ticket depends on Vendor
**Cardinality:** Many-to-Many
**Requirement:** Required where vendor dependency exists

This relationship supports:

* vendor case tracking
* dependency time
* escalation
* reporting

A vendor relationship never removes the requirement for internal ownership.

---

## Ticket → Approval

**Relationship:** Ticket requires Approval
**Cardinality:** One-to-Many
**Requirement:** Conditional

This supports:

* manager approval
* service-owner approval
* security approval
* access approval

Multiple approvals may apply to one request.

---

# 5. Service Relationships

## Service → Support Group

**Relationship:** Service supported by Support Group
**Cardinality:** Many-to-Many
**Requirement:** Required

A service may have several technical support groups.

Example:

```text id="c20jfv"
Business Email
├── Service Desk
├── Messaging Support
├── Identity and Access
└── Network Support
```

One group may still be designated as the primary owner for routing purposes.

---

## Service → Configuration Item

**Relationship:** Service depends on Configuration Item
**Cardinality:** One-to-Many or Many-to-Many
**Requirement:** Conditional

This relationship creates service context around technical components.

Example:

```text id="k6j02j"
Remote Access Service
├── VPN Gateway
├── Identity Service
├── MFA Service
└── Network Connectivity
```

This supports incident and change impact analysis.

---

## Service → Knowledge Article

**Relationship:** Service documented by Knowledge Article
**Cardinality:** One-to-Many
**Requirement:** Optional

This supports:

* service-specific guidance
* troubleshooting
* user self-service

---

## Service → Change

**Relationship:** Service affected by Change
**Cardinality:** Many-to-Many
**Requirement:** Required where applicable

This provides the business-service view of planned technical activity.

---

# 6. Change Relationships

## Change → Configuration Item

**Relationship:** Change modifies Configuration Item
**Cardinality:** Many-to-Many
**Requirement:** Required where applicable

This relationship supports:

* impact assessment
* collision identification
* incident correlation
* validation

A high-risk production change should not simply say "infrastructure."

The affected technical scope should be identifiable.

---

## Change → Approval

**Relationship:** Change requires Approval
**Cardinality:** One-to-Many
**Requirement:** Conditional

Approval requirements depend on:

* change type
* risk
* affected service
* organizational policy

The relationship preserves authorization history.

---

## Change → Vendor

**Relationship:** Change implemented with Vendor
**Cardinality:** Many-to-Many
**Requirement:** Conditional

This applies where an external party:

* performs implementation
* provides technical support
* validates vendor-specific activity

Internal Change Owner accountability remains unchanged.

---

# 7. Asset and CI Relationship

## Asset → Configuration Item

**Relationship:** Asset represented by Configuration Item
**Cardinality:** One-to-One or One-to-Many
**Requirement:** Conditional

This relationship exists where the same physical or logical object matters from both:

* asset-lifecycle perspective
* service-configuration perspective

Example:

```text id="xqjskz"
Laptop Asset
   ↓
Endpoint CI
```

The implementation should avoid duplicate maintenance where the platform can reasonably represent both contexts through one managed record.

---

# 8. Vendor Relationships

## Vendor → Service

**Relationship:** Vendor supports Service
**Requirement:** Conditional

This supports questions such as:

* Which services depend on this vendor?
* Which service owners should be notified of vendor issues?

---

## Vendor → CI

**Relationship:** Vendor supports Configuration Item
**Requirement:** Conditional

This helps identify:

* vendor escalation path
* warranty/support responsibility
* technical dependency

---

## Vendor → Ticket

**Relationship:** Vendor supports active Ticket
**Requirement:** Conditional

This provides transaction-level dependency tracking.

---

# 9. Knowledge Relationships

## Knowledge Article → Owner

**Relationship:** Article owned by User or Support Group
**Requirement:** Required

An article without ownership is unlikely to remain accurate.

---

## Knowledge Article → Service

**Relationship:** Article supports Service
**Requirement:** Optional but preferred where meaningful

This improves:

* search
* recommendation
* content ownership
* lifecycle review

---

## Knowledge Article → Ticket

**Relationship:** Article used by or derived from Ticket
**Requirement:** Optional

This creates the feedback loop between operational work and reusable knowledge.

---

# 10. Approval Relationships

Approval should always retain a parent relationship.

Valid parent records include:

* Service Request
* Change
* Temporary Access Request
* other controlled workflow where defined

Example:

```text id="ovvukp"
Privileged Access Request
      ↓
Manager Approval
      ↓
System Owner Approval
      ↓
Security Approval
```

Each approval remains independently traceable.

---

# 11. Relationship Purpose Matrix

| Relationship           | Routing | Troubleshooting | Governance | Reporting | Audit |
| ---------------------- | ------: | --------------: | ---------: | --------: | ----: |
| Ticket → User          |       ✓ |               ✓ |            |         ✓ |     ✓ |
| Ticket → Service       |       ✓ |               ✓ |          ✓ |         ✓ |       |
| Ticket → Support Group |       ✓ |                 |          ✓ |         ✓ |     ✓ |
| Ticket → Asset         |         |               ✓ |            |         ✓ |       |
| Ticket → CI            |         |               ✓ |          ✓ |         ✓ |       |
| Ticket → Change        |         |               ✓ |          ✓ |         ✓ |     ✓ |
| Ticket → Vendor        |         |               ✓ |          ✓ |         ✓ |     ✓ |
| Ticket → Approval      |         |                 |          ✓ |         ✓ |     ✓ |
| Ticket → Knowledge     |         |               ✓ |            |         ✓ |       |
| Service → CI           |       ✓ |               ✓ |          ✓ |         ✓ |       |
| Vendor → CI            |         |               ✓ |          ✓ |         ✓ |       |

This helps distinguish operational relationships from data that would merely be nice to have.

---

# 12. Relationship Creation

Relationships may be created through:

* user selection
* technician selection
* workflow rule
* integration
* automated discovery
* approved AI suggestion

The source should match the reliability needed.

Example:

```text id="y3x92u"
Ticket Service
      ↓
Service Ownership Rule
      ↓
Support Group
```

This is preferable to manually reselecting the same group for every record.

---

# 13. Relationship Validation

The platform should validate relationships where practical.

Examples:

| Condition                                     | Expected Behavior            |
| --------------------------------------------- | ---------------------------- |
| Inactive support group selected               | Prevent or warn              |
| Retired service selected for new request      | Prevent                      |
| Inactive approver routed                      | Exception / reroute          |
| Temporary vendor access without active vendor | Prevent                      |
| Change references retired CI                  | Warn / require justification |
| Published article has no owner                | Prevent publication          |

Validation prevents data-quality problems earlier than reporting can detect them.

---

# 14. Relationship History

Material relationship changes should be retained where they affect accountability or auditability.

Examples include:

* Ticket → Support Group
* Ticket → Priority
* Ticket → Vendor
* Change → CI
* Approval → Approver

Not every relationship modification requires a formal audit event.

The focus is on relationships that materially change process meaning.

---

# 15. Relationship Ownership

The entity owner and the relationship owner may not always be the same.

Example:

```text id="l5nww1"
Service Owner
   ↓ owns Service

Technical Team
   ↓ maintains Service → CI relationship
```

Similarly:

```text id="v3x9ph"
Vendor Management
   ↓ owns Vendor Record

Service Owner
   ↓ validates Vendor → Service relationship
```

This distinction becomes important during data governance.

---

# 16. Relationship Quality Measures

Useful data-quality measures include:

| Metric                             | Purpose                                |
| ---------------------------------- | -------------------------------------- |
| Tickets with Service               | Measure service-context completeness   |
| Incidents with CI                  | Measure technical-context completeness |
| Changes with CI                    | Measure change-impact coverage         |
| Vendor Tickets with Internal Owner | Validate accountability                |
| Active Services with Owner         | Validate service governance            |
| Published Articles with Owner      | Validate knowledge accountability      |
| Temporary Access with Expiration   | Validate access lifecycle              |
| Invalid / Inactive References      | Identify stale relationship data       |

These should be used to improve the data model rather than simply report field completion.

---

# 17. Relationship Design Guardrails

## Do Not Require Everything

A low-impact user incident may not need full CI mapping.

The relationship should add value.

---

## Do Not Hide Ownership in Free Text

If ownership matters operationally, it should be represented structurally.

---

## Do Not Duplicate Authoritative Data Without Reason

If another system owns user or asset information, integrate or reference it where practical.

---

## Do Not Confuse Relationship Count With Maturity

A highly connected CMDB with unreliable relationships is less useful than a smaller model people trust.

---

# 18. Testing Mapping

Representative tests include:

| Test ID   | Scenario                                       |
| --------- | ---------------------------------------------- |
| TC-REL-01 | Ticket requires valid requester                |
| TC-REL-02 | Active ticket retains owning group             |
| TC-REL-03 | Incident linked to affected service and CI     |
| TC-REL-04 | Change linked to multiple affected CIs         |
| TC-REL-05 | Incident linked to failed change               |
| TC-REL-06 | Vendor-supported ticket retains internal owner |
| TC-REL-07 | Approval retains parent record                 |
| TC-REL-08 | Published knowledge requires owner             |
| TC-REL-09 | Inactive reference rejected or flagged         |

These will be formalized in:

[Testing and UAT](../09%20Testing%20and%20UAT/test%20cases.md)

---

# 19. Relationship Success Criteria

The relationship model is design-ready when:

* core relationships are defined
* required versus optional relationships are clear
* ownership is identified
* relationship validation is defined
* authoritative data sources are known
* audit-sensitive relationships are identified
* reporting dependencies are understood
* test scenarios exist

---

# 20. Entity Relationships Conclusion

The value of the service-management data model comes from the connections between records.

A ticket by itself tells us that work happened.

A connected ticket can tell us:

* who was affected
* what service was involved
* who owned the response
* what technical component was involved
* whether a change contributed
* whether a vendor was required
* who approved the action
* whether useful knowledge already existed

That is the difference between storing tickets and building operational context.

**Next:** [Data Governance](./data%20governance.md)
