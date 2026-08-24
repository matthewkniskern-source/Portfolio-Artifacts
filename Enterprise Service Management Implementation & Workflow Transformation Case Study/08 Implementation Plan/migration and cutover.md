# Migration and Cutover

## Purpose

This artifact defines how the organization transitions from the fragmented current-state service model into the target Enterprise Service Management environment.

The migration effort should preserve what is operationally useful while avoiding the mistake of rebuilding the old environment inside the new platform.

The cutover plan should make the transition understandable to:

* support teams
* approvers
* service owners
* administrators
* end users

The operating principle is:

> **Move the service operation forward without dragging every legacy problem with it.**

This artifact builds on:

* [Implementation Plan](./implementation%20plan.md)
* [Phase Exit Criteria](./phase%20exit%20criteria.md)
* [Data Governance](../05%20Data%20and%20Configuration%20Model/data%20governance.md)
* [Service Management Data Model](../05%20Data%20and%20Configuration%20Model/service%20management%20data%20model.md)

---

# 1. Migration Objectives

The migration should:

* establish clean production data
* preserve required operational history
* minimize service interruption
* retire uncontrolled intake paths where practical
* maintain active work ownership
* preserve approval and audit evidence
* validate critical relationships
* provide rollback or recovery options
* avoid unnecessary migration volume

The migration is successful when users and support teams can continue working without losing the context required to manage active service activity.

---

# 2. Migration Scope

Initial migration may include:

* active users
* support groups
* service records
* service ownership
* catalog items
* SLA definitions
* approval mappings
* active vendors
* selected assets and CIs
* current knowledge articles
* active service records where required
* limited historical records where justified

Migration scope should be based on business use.

Not data availability.

---

# 3. Migration Decision Model

Each legacy data set should be evaluated through the following decision:

```text id="th9teb"
Legacy Data
    ↓
Required for Active Operations?
   ↙                     ↘
 Yes                      No
 ↓                         ↓
Migrate              Retention Required?
                      ↙          ↘
                    Yes           No
                     ↓             ↓
                  Archive        Retire
```

This prevents the assumption that every record belongs in the new environment.

---

# 4. Migration Categories

Legacy data should be classified as:

| Category               | Treatment                    |
| ---------------------- | ---------------------------- |
| Active Operational     | Migrate                      |
| Required Historical    | Migrate or archive           |
| Regulatory / Retention | Preserve according to policy |
| Reference Only         | Archive where useful         |
| Duplicate              | Exclude                      |
| Obsolete               | Retire                       |
| Unreliable             | Correct or exclude           |

The implementation team should be able to explain why each major data set is being moved.

---

# 5. Active Ticket Strategy

Open incidents and requests require special handling because they represent work in progress.

Possible approaches include:

## Migrate Active Records

Appropriate where:

* record volume is manageable
* required data can be mapped
* continuity matters
* relationships can be preserved

## Close and Recreate Selected Records

Appropriate where:

* legacy structure cannot be mapped reliably
* only a small number of records remain active

The original legacy reference should remain available.

## Complete in Legacy Platform

Appropriate where:

* ticket is near completion
* migration adds more risk than value

The chosen strategy should be consistent rather than decided technician by technician during cutover.

---

# 6. Active Ticket Migration Requirements

Migrated active records should retain, where applicable:

* legacy record ID
* requester
* affected user
* current owner
* service
* category
* priority
* status
* created date
* current SLA context
* relevant notes
* related asset / CI
* vendor dependency
* approval state
* related change

The target record should identify that it originated in the legacy environment.

---

# 7. Historical Ticket Strategy

Historical ticket migration should be limited.

Reasons to retain history may include:

* audit requirement
* incident trend analysis
* contractual need
* known problem history
* regulatory retention

Reasons not to migrate include:

* low data quality
* incompatible fields
* duplicate records
* high migration complexity
* little expected future use

Historical records may remain in:

* read-only legacy environment
* controlled archive
* reporting repository

Migration is not the only form of retention.

---

# 8. Knowledge Migration

Knowledge should be reviewed before migration.

Each article should be classified:

| Status                    | Action                  |
| ------------------------- | ----------------------- |
| Current and Useful        | Migrate                 |
| Current but Needs Cleanup | Update then migrate     |
| Duplicate                 | Consolidate             |
| Obsolete                  | Retire                  |
| Unknown Owner             | Assign owner or exclude |
| Temporary Workaround      | Validate continued need |

Migrating stale knowledge creates a problem immediately.

AI-assisted search or recommendation would only make that stale content easier to find.

---

# 9. Service Catalog Migration

Legacy service or request definitions should not automatically become target catalog items.

Each candidate should be evaluated for:

* current business need
* owner
* fulfillment group
* required data
* approval model
* SLA target
* closure criteria

Only validated catalog items should be published.

---

# 10. User and Identity Migration

User data should preferably come from an authoritative source rather than one-time manual migration.

Required validation includes:

* active status
* identity
* department
* manager where used for approval
* location where used for routing
* support role membership

Inactive users should not receive active platform roles.

---

# 11. Support Group Migration

Existing groups should be reviewed against the target ownership model.

Potential outcomes include:

* retain
* rename
* merge
* split
* retire

A legacy queue should not be preserved simply because users recognize its name.

The question is whether it represents a valid target ownership boundary.

---

# 12. Service Migration

Active target services require:

* service name
* service owner
* support group
* criticality
* support window
* status
* applicable SLA

Services without a clear owner should not silently move into production as governed target services.

They should enter a remediation list.

---

# 13. Asset and CI Migration

Asset and CI migration should follow the minimal model established earlier.

Priority should be given to records that support:

* active incidents
* change impact
* vendor support
* service dependency
* asset fulfillment

The project should avoid turning cutover into a large CMDB cleanup program.

---

# 14. Vendor Migration

Active vendor records should be validated for:

* active relationship
* internal owner
* supported service
* supported asset / CI where useful
* support contact
* access status

Inactive vendors should not become selectable in the new environment.

---

# 15. Approval Mapping

Approval relationships must be validated before go-live.

Examples include:

* manager approval
* service owner
* system owner
* change authority
* security approval

Validation should identify:

* inactive approvers
* missing approvers
* conflicting roles
* self-approval risk

Approval mapping deserves direct testing before production cutover.

---

# 16. Data Mapping

Migration should define explicit source-to-target mappings.

Example:

| Legacy Field    | Target Field                | Treatment                |
| --------------- | --------------------------- | ------------------------ |
| Ticket Number   | Legacy Reference            | Preserve                 |
| Assigned Team   | Owning Group                | Transform / validate     |
| Severity        | Impact / Urgency / Priority | Map through target logic |
| Application     | Service / CI                | Normalize                |
| Vendor Notes    | Vendor Relationship / Notes | Transform                |
| Resolution Text | Resolution Summary          | Preserve where useful    |
| Status          | Workflow State              | Map                      |

Not every legacy field requires a target equivalent.

---

# 17. Data Transformation

Migration may require transformation such as:

* category consolidation
* support-group normalization
* service-name cleanup
* status mapping
* user-identity matching
* vendor deduplication
* date normalization

Transformations should be documented and repeatable.

Manual cleanup without a defined rule is difficult to validate.

---

# 18. Data Validation

Migration validation should include:

## Record Count

Confirm expected volume.

## Required Fields

Confirm mandatory target values exist.

## Relationship Validation

Confirm:

* users
* services
* groups
* CIs
* vendors
* approvals

resolve correctly.

## Sampling

Manually inspect representative migrated records.

## Exception Review

Identify migration failures rather than silently dropping them.

---

# 19. Migration Reconciliation

Example reconciliation:

| Data Set           | Source | Expected | Loaded |             Exceptions |
| ------------------ | -----: | -------: | -----: | ---------------------: |
| Active Users       |    750 |      742 |    742 |    8 inactive excluded |
| Support Groups     |     18 |       14 |     14 |         4 consolidated |
| Active Services    |     31 |       26 |     26 |    5 pending ownership |
| Knowledge Articles |    210 |       94 |     94 | 116 retired / excluded |

The numbers above are illustrative.

Actual implementation values should come from validated source data.

---

# 20. Migration Exception Handling

Migration errors should enter a controlled exception process.

```text id="8faycy"
Migration Record
      ↓
Validation Failure
      ↓
Exception
      ↓
Correct / Exclude / Defer
      ↓
Revalidate
```

Examples include:

* unknown user
* invalid owner
* missing service
* duplicate asset
* unsupported status
* invalid approver

Every material exception should have a disposition.

---

# 21. Migration Testing

Migration should be rehearsed before production cutover.

A recommended sequence is:

```text id="25zglq"
Extract
  ↓
Transform
  ↓
Test Load
  ↓
Validate
  ↓
Correct Mapping
  ↓
Repeat
```

The first production migration should not be the first time the migration logic has run.

---

# 22. Cutover Strategy

The target implementation uses a controlled cutover rather than an indefinite dual-running model.

The general sequence is:

```text id="fs48z3"
Prepare
  ↓
Freeze Selected Legacy Changes
  ↓
Final Extract
  ↓
Transform
  ↓
Load
  ↓
Validate
  ↓
Enable Production
  ↓
Redirect Intake
  ↓
Hypercare
```

---

# 23. Cutover Window

The cutover window should be selected based on:

* service demand
* support availability
* business calendar
* integration requirements
* migration duration
* validation duration

A low-volume period is preferred.

The organization should avoid cutover immediately before:

* major business events
* known peak periods
* major infrastructure changes

where possible.

---

# 24. Pre-Cutover Activities

Before the cutover window:

* production configuration frozen
* production data validated
* migration scripts / procedures tested
* user roles verified
* support groups confirmed
* approvers confirmed
* integrations tested
* communications prepared
* support roster confirmed
* legacy data backup completed
* rollback criteria agreed
* cutover checklist approved

The cutover should not begin with major readiness questions still open.

---

# 25. Configuration Freeze

A temporary configuration freeze should apply before production cutover.

The freeze may include:

* workflow changes
* categories
* SLA logic
* RBAC
* service catalog
* approval rules
* automation

Only emergency corrections should occur during this period.

The goal is to keep the tested production baseline stable.

---

# 26. Legacy Transaction Freeze

Depending on the migration design, selected legacy transactions may require a temporary freeze.

Possible treatment:

* stop new requests at defined time
* continue critical incident handling
* manually reconcile emergency transactions
* perform final extract

Business continuity takes priority over a perfect database freeze.

A clear exception procedure should exist.

---

# 27. Final Data Extract

The final extraction should capture the approved migration scope after the cutover freeze.

The team should record:

* extraction timestamp
* source system
* record count
* migration version
* responsible owner

This creates a defensible migration baseline.

---

# 28. Production Load

Data should be loaded in dependency order.

Recommended sequence:

```text id="y6h24u"
Users
  ↓
Support Groups
  ↓
Services
  ↓
Reference Data
  ↓
Assets / CIs
  ↓
Vendors
  ↓
Knowledge
  ↓
Active Tickets
```

This reduces broken relationships during migration.

---

# 29. Production Validation

Before opening the platform broadly, validate:

* login
* roles
* support queues
* service catalog
* incident submission
* request submission
* routing
* approval
* SLA
* CI relationships
* vendor relationships
* notifications
* reporting
* audit logging

Critical validation should use production-like transactions rather than only viewing configuration screens.

---

# 30. Smoke Test

A production smoke test should include representative end-to-end scenarios.

Example:

```text id="98ucou"
Submit Incident
     ↓
Route
     ↓
Assign
     ↓
Update
     ↓
Resolve
```

and:

```text id="s8cyf6"
Submit Controlled Request
       ↓
Approval
       ↓
Fulfillment
       ↓
Complete
```

and:

```text id="jru81u"
Normal Change
     ↓
Approval
     ↓
Implementation
     ↓
Validation
```

---

# 31. Intake Transition

Legacy service channels should be handled intentionally.

Potential actions include:

* retire old portal
* redirect legacy portal
* update support email
* forward selected mail to managed intake
* update phone scripts
* update intranet links
* communicate new self-service URL
* stop spreadsheet intake

The organization should not launch a new platform while leaving every old intake method unchanged indefinitely.

---

# 32. Email Intake

Where email remains an approved channel, it should create or update managed records.

Example:

```text id="7thm7i"
Support Email
     ↓
ESM Ticket
     ↓
Managed Workflow
```

Email itself should not remain a parallel unmanaged ticket system.

---

# 33. Direct Technician Requests

Users will continue to approach technicians directly.

The target operating response should be:

```text id="n8c9p6"
Direct User Contact
      ↓
Urgent?
   ↙         ↘
 Yes          No
 ↓             ↓
Respond      Create / Direct to
and Record   Managed Request
```

The implementation should not pretend informal contact disappears on go-live day.

The objective is to bring the resulting work into the managed process.

---

# 34. Cutover Communication

Communications should explain:

* when the new system becomes active
* how users request service
* what legacy channels are changing
* what happens to existing requests
* where users can get help
* what to expect during transition

Different messages should be prepared for:

* end users
* technicians
* approvers
* service owners
* management

---

# 35. Cutover Roles

| Role                | Responsibility                |
| ------------------- | ----------------------------- |
| Cutover Lead        | Coordinates cutover           |
| Platform Lead       | Production configuration      |
| Migration Lead      | Data movement                 |
| Data Owners         | Validate data                 |
| Process Owners      | Validate workflows            |
| Security / Risk     | Validate critical controls    |
| Service Desk Lead   | Validate intake and support   |
| Integration Owners  | Validate external connections |
| Communications Lead | Release transition messaging  |
| Project Sponsor     | Go / No-Go authority          |

---

# 36. Cutover Command Model

During the cutover window, decision authority should be clear.

```text id="h75la4"
Cutover Lead
    │
    ├── Platform
    ├── Migration
    ├── Data
    ├── Integration
    ├── Process
    └── Support
```

Issues that may force rollback or delay should escalate immediately.

---

# 37. Go / No-Go Check

Before production opening:

| Area             | Required Condition                               |
| ---------------- | ------------------------------------------------ |
| Platform         | Available and stable                             |
| Data             | Critical data validated                          |
| RBAC             | Correct                                          |
| Intake           | Operational                                      |
| Routing          | Operational                                      |
| Approval         | Operational                                      |
| SLA              | Operational                                      |
| Integrations     | Required paths operational or fallback available |
| Audit            | Active                                           |
| Support          | Staffed                                          |
| Critical Defects | None open                                        |

A critical failure should result in No-Go or rollback rather than acceptance by momentum.

---

# 38. Rollback Criteria

Potential rollback triggers include:

* platform unavailable
* critical data corruption
* broad authentication failure
* major RBAC failure
* critical routing failure
* required approval unavailable
* severe integration failure with no fallback
* material audit/control failure

Rollback should be based on defined conditions.

Not improvised during the outage.

---

# 39. Rollback Strategy

Rollback may include:

* disable new production intake
* restore legacy intake
* preserve transactions created during cutover
* restore prior configuration
* reverse failed migration
* communicate status
* reschedule cutover

The rollback procedure should identify how transactions created after the migration extract will be reconciled.

---

# 40. Forward-Fix Decision

Not every defect requires rollback.

Example:

```text id="1zgiji"
Issue Found
   ↓
Critical to Operation?
 ↙              ↘
Yes              No
 ↓                ↓
Rollback /       Forward Fix
Major Recovery
```

Forward fix may be appropriate where:

* core service continues
* data is intact
* controls remain effective
* workaround exists
* remediation is quick

---

# 41. Dual-Run Limitation

A short overlap may be necessary.

A long dual-run period should generally be avoided.

Extended parallel operation creates:

* duplicate tickets
* ownership confusion
* inconsistent reporting
* user uncertainty
* split knowledge
* reconciliation effort

If dual-run is required, the system of record must remain clear.

---

# 42. Cutover Issue Log

All material cutover issues should capture:

* issue
* timestamp
* severity
* owner
* business impact
* decision
* workaround
* resolution

The issue log becomes an input to Hypercare and post-implementation review.

---

# 43. Hypercare Transition

After cutover:

```text id="ofpguk"
Cutover
  ↓
Production Stable Enough
  ↓
Hypercare
  ↓
Normal Operations
```

Open cutover issues should transfer directly into the Hypercare backlog.

They should not disappear because the formal cutover window ended.

---

# 44. Migration and Cutover Metrics

Useful measures include:

| Metric                      | Purpose                          |
| --------------------------- | -------------------------------- |
| Migration Success Rate      | Measure data-load quality        |
| Migration Exception Count   | Identify data problems           |
| Record Reconciliation Rate  | Validate completeness            |
| Cutover Duration            | Validate planning                |
| Critical Cutover Defects    | Measure transition risk          |
| Rollback Required           | Identify severe failure          |
| Intake Transition Success   | Measure channel adoption         |
| Post-Cutover Routing Errors | Measure ownership quality        |
| Data Correction Volume      | Measure migration quality        |
| Legacy Channel Usage        | Measure transition effectiveness |

---

# 45. Post-Cutover Validation

During early production, confirm:

* migrated ownership remains valid
* active tickets continue progressing
* service catalog requests route correctly
* SLA operates as designed
* approval queues are active
* vendor access workflows function
* integrations remain stable
* reporting reflects production data
* legacy channels are declining

Some migration problems only become visible once real work begins.

---

# 46. Legacy Platform Retirement

The legacy environment should be retired only after:

* required active records are resolved or migrated
* retention needs are satisfied
* audit access is addressed
* required exports are complete
* new environment is stable
* operational ownership approves retirement

Legacy retirement may mean:

* shutdown
* read-only mode
* archived export

depending on retention needs.

---

# 47. Legacy Access After Cutover

If legacy access remains available for historical research, it should be:

* read-only where practical
* limited to authorized users
* clearly labeled as historical
* removed from normal intake processes

Users should not be able to accidentally create new operational work in the retired system.

---

# 48. Migration Documentation

The implementation should retain:

* migration scope
* source-to-target mapping
* transformation rules
* exception disposition
* load results
* reconciliation results
* final extract reference
* cutover checklist
* go/no-go decision
* rollback decision if applicable

This provides enough evidence to understand how the target environment was populated.

---

# 49. Migration and Cutover Guardrails

## Do Not Migrate Everything Because Storage Is Cheap

Migration effort and data quality matter more than storage cost.

## Do Not Preserve Obsolete Structure

Legacy categories and queues should earn their place in the target model.

## Do Not Change Production Design During Cutover

Cutover is the wrong time for feature redesign.

## Do Not Hide Migration Exceptions

Failed records should be visible and dispositioned.

## Do Not Leave Legacy Intake Open Forever

That recreates the fragmented environment the project was designed to remove.

## Do Not Roll Back for Every Small Defect

Use defined criticality and business impact.

## Do Not Assume Cutover Ends at Go-Live

The transition is not complete until normal operations can own the environment.

---

# 50. Migration and Cutover Success Criteria

Migration and cutover are successful when:

* production data is validated
* active work remains owned
* required historical information remains accessible
* users can access the new environment
* intake routes into managed workflows
* approvals function
* critical controls operate
* required integrations operate or have tested fallback
* migration exceptions are owned
* legacy channels are controlled
* Hypercare receives remaining issues
* rollback is no longer required

---

# 51. Migration and Cutover Conclusion

A successful cutover is not the moment the new platform turns on.

It is the point where the organization can move its service operation into the new environment without losing ownership, context, control, or the ability to recover.

The migration should preserve what still has value.

The cutover should make the new operating model clear.

The legacy environment should stop being the place where work continues by habit.

And once production opens, every remaining issue should have an owner and a path forward.

That is what turns platform deployment into an operational transition.

**Next:** [Test Strategy](../09%20Testing%20and%20UAT/test%20strategy.md)
