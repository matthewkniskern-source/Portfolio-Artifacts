# Data Governance

## Purpose

The Data Governance model defines how core service-management data is owned, maintained, reviewed, retained, and corrected over time.

The target ESM environment depends on more than workflow logic.

It also depends on the quality of the data feeding that logic.

If ownership, services, support groups, configuration items, vendors, or approval relationships are stale or incomplete, the platform can still function while producing bad routing, weak reporting, and unreliable automation.

The operating principle is:

> **Data only stays trustworthy when someone is accountable for keeping it that way.**

This artifact builds on:

* [Service Management Data Model](./service%20management%20data%20model.md)
* [Entity Relationships](./entity%20relationships.md)
* [Functional Requirements](../02%20Requirements%20Discovery/functional%20requirements.md)
* [Nonfunctional Requirements](../02%20Requirements%20Discovery/nonfunctional%20requirements.md)

---

# 1. Governance Scope

This model applies to core service-management data domains including:

* users
* support groups
* services
* assets
* configuration items
* vendors
* knowledge
* categories
* SLA definitions
* approval rules
* service records

Not every data element requires the same governance model.

The strongest controls should be applied where poor data creates material operational or security impact.

---

# 2. Governance Principles

The target model follows six principles.

## 2.1 Define an Owner

Every important data domain needs a business or operational owner.

Technical administrators may maintain the platform.

That does not automatically make them responsible for deciding what the data means.

---

## 2.2 Use Authoritative Sources

Where another system already owns a data domain, the ESM platform should consume or reference that source where practical.

Examples include:

* employee status from HR
* identity from identity management
* asset records from asset management
* vendor master data from procurement

The ESM platform should not quietly become a second source of truth.

---

## 2.3 Control Reference Data

Values used for routing, reporting, access, or workflow should use controlled lists where consistency matters.

Examples:

* service
* support group
* category
* priority
* change type
* approval type
* vendor status

Free text is useful for context.

It is a poor replacement for structured reference data.

---

## 2.4 Review Data That Can Go Stale

Some data changes slowly.

Some changes constantly.

Review frequency should reflect the risk and volatility of the data.

---

## 2.5 Preserve Material History

Data corrections should not erase the history needed to understand:

* ownership
* approvals
* access
* workflow transitions
* major configuration changes

Current-state accuracy and historical traceability both matter.

---

## 2.6 Measure Data Quality

Data governance should produce measurable quality signals.

If data quality is only discussed when something breaks, governance is already late.

---

# 3. Data Ownership Matrix

| Data Domain         | Primary Owner                 | Technical Steward         | Review Need |
| ------------------- | ----------------------------- | ------------------------- | ----------- |
| Users               | HR / Identity                 | Identity Administration   | High        |
| Support Groups      | IT Management                 | Platform Administrator    | Medium      |
| Services            | Service Owners                | Service Management Team   | High        |
| Assets              | Asset Management              | Asset Team                | High        |
| Configuration Items | Technical / CI Owners         | Platform / Discovery Team | High        |
| Vendors             | Procurement / Vendor Owner    | Platform Administrator    | Medium      |
| Knowledge           | Knowledge / Service Owner     | Support Teams             | High        |
| Categories          | Service Management Owner      | Platform Administrator    | Medium      |
| SLA Definitions     | Service Owner / IT Management | Platform Administrator    | High        |
| Approval Rules      | Process Owner                 | Platform Administrator    | High        |
| Ticket Data         | Process Owner                 | Support Teams             | High        |

This separates ownership from stewardship.

The person maintaining the field is not necessarily the person authorized to redefine it.

---

# 4. Authoritative Data Sources

| Data Domain              | Authoritative Source               |
| ------------------------ | ---------------------------------- |
| Employee Identity        | Identity / HR                      |
| Manager Relationship     | HR / Identity                      |
| Department               | HR                                 |
| Support Group Membership | Identity / ESM Administration      |
| Service Catalog          | ESM                                |
| Service Ownership        | ESM / Service Governance           |
| Ticket History           | ESM                                |
| Asset Data               | Asset Management                   |
| CI Data                  | ESM / Discovery / Technical Owners |
| Vendor Master            | Procurement / Vendor Management    |
| Approval History         | ESM                                |
| Change History           | ESM                                |
| Knowledge Content        | ESM                                |

Where multiple systems contribute data, ownership should be explicit.

---

# 5. Data Lifecycle

Key data should follow a defined lifecycle.

```text id="x75knf"
Create
  ↓
Validate
  ↓
Use
  ↓
Review
  ↓
Update
  ↓
Retire / Archive
```

The specific lifecycle differs by entity.

For example:

```text id="nq8a1u"
Service
 ↓
Proposed
 ↓
Approved
 ↓
Active
 ↓
Review
 ↓
Retired
```

or:

```text id="d53wde"
Vendor
 ↓
Active
 ↓
Support Relationship
 ↓
Review
 ↓
Inactive
```

---

# 6. Data Quality Dimensions

The target model evaluates data quality across five dimensions.

| Dimension    | Question                                      |
| ------------ | --------------------------------------------- |
| Completeness | Is required information present?              |
| Accuracy     | Does the data represent reality?              |
| Consistency  | Is the same concept represented the same way? |
| Timeliness   | Is the information current enough to use?     |
| Ownership    | Is someone accountable for correcting it?     |

A field can be complete and still be wrong.

Completion alone is not a sufficient data-quality measure.

---

# 7. Required Data Controls

The platform should enforce required values where their absence would prevent reliable workflow behavior.

Examples include:

* active ticket owner
* requester
* service where required
* approval parent
* temporary-access expiration
* knowledge owner
* change owner
* vendor sponsor where applicable

Mandatory fields should be limited to information that actually supports process integrity.

Too many required fields create low-quality filler rather than better data.

---

# 8. Reference Data Governance

Controlled reference values should include:

* service names
* support groups
* request categories
* incident categories
* priority values
* change types
* change risk
* approval types
* vendor status
* knowledge status

Changes to these values should follow controlled configuration procedures.

A category change can affect:

* routing
* reporting
* automation
* historical comparison

It should not be treated as a cosmetic edit.

---

# 9. Service Data Governance

Every active service should have:

* service owner
* support group
* criticality
* support window
* status
* applicable SLA model

A service record should be reviewed when:

* ownership changes
* service is materially redesigned
* support responsibility changes
* service is retired
* SLA expectations change

Services without owners should be treated as governance exceptions.

---

# 10. Support Group Governance

Support groups should have:

* defined scope
* group lead
* active membership
* supported services
* escalation path
* active / inactive status

Inactive groups should not remain valid assignment targets.

Membership should be reviewed as staffing changes.

---

# 11. CI Governance

The initial CI model should stay deliberately limited.

Each managed CI should have, where applicable:

* CI type
* owner
* support group
* service relationship
* operational status
* vendor
* lifecycle status

The organization should not add CI classes faster than it can maintain them.

A smaller reliable model is more useful than a larger stale one.

---

# 12. Asset Governance

Asset data should support:

* ownership
* assignment
* location
* lifecycle
* warranty
* support context

Asset retirement should prevent the asset from being treated as active for new fulfillment or assignment while preserving historical ticket relationships.

---

# 13. Vendor Data Governance

Vendor records should include:

* vendor owner
* active status
* supported services
* supported assets / CIs where applicable
* escalation contact
* relevant contractual support reference

Inactive vendors should not remain selectable for new access or support activity without exception.

---

# 14. Knowledge Data Governance

Published knowledge requires:

* owner
* audience
* status
* review date
* service context where applicable

Articles reaching review date should enter:

* review
* update
* retirement

rather than remaining indefinitely published.

---

# 15. Approval Data Governance

Approval records are transactional evidence and should not be rewritten casually.

Required approval data includes:

* parent record
* approver
* approval role or type
* decision
* timestamp
* comments where required

Changes to approval rules should affect future workflow logic without destroying historical approval evidence.

---

# 16. Ticket Data Quality

Ticket quality is heavily influenced by frontline behavior.

Important structured fields include:

* requester
* service
* category
* priority
* owner
* status
* resolution
* related CI where applicable

Ticket quality should be improved through:

* form design
* defaults
* routing logic
* validation
* training
* targeted reporting

not simply by adding more mandatory fields.

---

# 17. Stale Data Detection

The organization should be able to identify data that may no longer be reliable.

Examples:

* service with inactive owner
* CI not reviewed within defined period
* vendor with no active relationship
* knowledge article past review date
* support group with no active members
* temporary access past expiration
* inactive approver still assigned to workflow

These should feed exception reporting.

---

# 18. Periodic Review

Representative review frequencies may include:

| Data Domain              | Suggested Review          |
| ------------------------ | ------------------------- |
| Support Group Membership | Quarterly                 |
| Service Ownership        | Semiannual                |
| Critical Service Data    | Quarterly                 |
| CI Ownership / Status    | Quarterly or event-driven |
| Vendor Relationships     | Semiannual                |
| Knowledge                | By article review date    |
| SLA Definitions          | Annual or service change  |
| Approval Rules           | Annual or control change  |

These are starting assumptions and should be adjusted based on business need.

---

# 19. Event-Driven Review

Some data should be reviewed immediately when triggering events occur.

Examples:

| Event                       | Data Review                       |
| --------------------------- | --------------------------------- |
| Employee termination        | User / group / approval roles     |
| Team reorganization         | Support groups / ownership        |
| Service retirement          | Service / CI / knowledge          |
| Vendor termination          | Vendor / access / CI relationship |
| Major infrastructure change | CI / service relationships        |
| Policy change               | Approval / SLA / RBAC rules       |

Event-driven review is more useful than waiting for the next scheduled audit when the underlying condition has already changed.

---

# 20. Data Retention

Service-management data should follow organizational retention policy.

Retention may vary by:

* incident
* request
* approval
* change
* knowledge
* access record
* audit record

The platform should support retention requirements without assuming every record needs to be stored forever.

---

# 21. Archival and Retirement

Retirement should preserve historical relationships where required.

For example:

```text id="w4yax4"
Retired CI
  ↑
Historical Incident
```

The CI should no longer be available for normal new selection.

The historical incident should still show what was affected at the time.

---

# 22. Data Correction

When incorrect data is identified, the process should distinguish between:

* correcting reference data
* correcting active transactional data
* preserving historical audit evidence

Example:

A support-group name may be corrected.

A historical approval decision should not simply be overwritten.

Material corrections should remain traceable where governance requires it.

---

# 23. Data Quality Exceptions

Representative exceptions include:

| ID    | Exception                                    |
| ----- | -------------------------------------------- |
| DQ-01 | Active service has no owner                  |
| DQ-02 | Ticket assigned to inactive group            |
| DQ-03 | CI has no support group                      |
| DQ-04 | Published article has expired review date    |
| DQ-05 | Temporary access is past expiration          |
| DQ-06 | Vendor dependency references inactive vendor |
| DQ-07 | Change lacks affected service                |
| DQ-08 | Approval references inactive approver        |

Exceptions should be assigned to accountable data owners.

---

# 24. Data Quality Metrics

| Metric                           | Purpose                        |
| -------------------------------- | ------------------------------ |
| Active Services with Owner       | Measure service governance     |
| Tickets with Valid Owning Group  | Measure ownership integrity    |
| Tickets with Service Association | Measure service context        |
| Changes with CI Association      | Measure impact visibility      |
| CIs with Active Owner            | Measure CI governance          |
| Knowledge Past Review Date       | Measure content staleness      |
| Invalid Reference Count          | Measure reference-data quality |
| Temporary Access Past Expiration | Measure lifecycle control      |
| Inactive Approver Exceptions     | Measure approval integrity     |

The purpose of these metrics is correction.

Not field-completion theater.

---

# 25. Data Governance Roles

| Role                   | Responsibility                               |
| ---------------------- | -------------------------------------------- |
| Data Owner             | Defines acceptable data and business meaning |
| Data Steward           | Maintains operational quality                |
| Platform Administrator | Configures data structures and controls      |
| Process Owner          | Defines workflow data requirements           |
| Security / Risk        | Defines sensitive-data controls              |
| Auditor / Reviewer     | Validates governance evidence                |

One person may hold multiple roles in a midsize organization.

The responsibilities should still remain clear.

---

# 26. Configuration Change Control

Changes to data structures that affect production workflow should be governed.

Examples include:

* new required field
* new category
* new service
* support-group restructuring
* CI class changes
* approval-rule changes
* reference-value retirement

These changes may affect:

* routing
* reporting
* integration
* automation
* UAT
* training

The data model should therefore be part of configuration change control.

---

# 27. Automation and Data Quality

Automation should validate the quality of the data it depends on.

Example:

```text id="lcf0b4"
Service
  ↓
Owning Group
  ↓
Routing Rule
```

If the service has no valid owning group, automation should fail visibly into an exception path.

It should not guess.

---

# 28. AI and Data Governance

AI-assisted functions may help identify:

* missing categories
* likely duplicates
* stale knowledge
* unusual ticket patterns
* probable service relationships

AI should not silently correct authoritative service-management data.

Where an AI recommendation materially changes structured data, the recommendation should be:

* reviewable
* attributable
* correctable

Detailed governance:

[AI Governance](../07%20Automation%20and%20AI/ai%20governance.md)

---

# 29. Data Governance Controls

| Control                          | Type                   | Purpose                   |
| -------------------------------- | ---------------------- | ------------------------- |
| Required data owner              | Preventive             | Maintain accountability   |
| Controlled reference values      | Preventive             | Improve consistency       |
| Required relationship validation | Preventive             | Reduce invalid records    |
| Periodic review                  | Detective              | Identify stale data       |
| Exception reporting              | Detective              | Identify quality failures |
| Correction workflow              | Corrective             | Restore accuracy          |
| Inactive-reference restriction   | Preventive             | Prevent invalid use       |
| Retention policy                 | Preventive             | Govern lifecycle          |
| Historical audit preservation    | Detective / Corrective | Preserve traceability     |

These controls will roll into:

[Governance and Controls](../06%20Governance%20and%20Controls/governance%20model.md)

---

# 30. Testing Mapping

Representative tests include:

| Test ID  | Scenario                                                              |
| -------- | --------------------------------------------------------------------- |
| TC-DG-01 | Active service cannot remain without required owner                   |
| TC-DG-02 | Inactive support group cannot receive new assignment                  |
| TC-DG-03 | Published knowledge requires review date                              |
| TC-DG-04 | Expired vendor cannot receive new access request                      |
| TC-DG-05 | Retired CI remains visible historically but blocked for new selection |
| TC-DG-06 | Data-quality exception appears in reporting                           |
| TC-DG-07 | Approval history remains unchanged after approval-rule update         |

These will be formalized in:

[Testing and UAT](../09%20Testing%20and%20UAT/test%20cases.md)

---

# 31. Data Governance Success Criteria

The data governance model is design-ready when:

* data owners are identified
* authoritative sources are defined
* controlled reference data is identified
* lifecycle states are defined
* review triggers are defined
* stale-data conditions are defined
* retention expectations are understood
* material historical data is preserved
* quality metrics are defined
* exception ownership is defined
* representative tests exist

---

# 32. Data Governance Conclusion

The target ESM platform can only be as reliable as the data the organization is willing to maintain.

Good workflow design can compensate for some missing information.

It cannot compensate indefinitely for:

* stale ownership
* invalid support groups
* obsolete configuration records
* outdated knowledge
* expired vendor relationships
* broken approval data

The goal is not perfect data.

The goal is data reliable enough that people, workflows, automation, and reporting can make decisions from it without constantly working around it.

That is the point where the data model becomes part of the operating model instead of another database to clean up later.

**Next:** [Governance Model](../06%20Governance%20and%20Controls/governance%20model.md)
