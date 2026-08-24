# Incident Management

## Purpose

The Incident Management workflow defines how the organization records, prioritizes, owns, escalates, resolves, and closes unplanned service interruptions or degradations.

The objective is straightforward:

> **Restore service quickly, preserve enough context to understand what happened, and keep ownership visible throughout the incident lifecycle.**

This workflow builds on:

* [Target Operating Model](../03%20Target%20Service%20Model/target%20operating%20model.md)
* [Priority and SLA Model](../03%20Target%20Service%20Model/priority%20and%20sla%20model.md)
* [Ownership and Escalation](../03%20Target%20Service%20Model/ownership%20and%20escalation.md)
* [Functional Requirements](../02%20Requirements%20Discovery/functional%20requirements.md)

---

# 1. Scope

Incident Management applies when a supported service is:

* unavailable
* degraded
* behaving unexpectedly
* preventing normal user activity

It does not apply to:

* standard service requests
* planned changes
* general questions better handled through knowledge
* enhancement requests

Where classification is unclear, the service desk may reclassify the record during triage.

---

# 2. Incident States

The target workflow uses the following core states:

```text
New
 ↓
Triage
 ↓
Assigned
 ↓
In Progress
 ↓
Waiting
 ↓
Resolved
 ↓
Closed
```

Additional exception states may include:

* Cancelled
* Major Incident
* Reopened

The workflow should remain simple enough that technicians can use states consistently.

---

# 3. State Definitions

| State       | Purpose                                                | Owner                       |
| ----------- | ------------------------------------------------------ | --------------------------- |
| New         | Record created and awaiting initial review             | Service Desk / Intake Queue |
| Triage      | Validate, classify, prioritize, and route              | Service Desk                |
| Assigned    | Correct support group identified                       | Owning Support Group        |
| In Progress | Active technical work underway                         | Owning Support Group        |
| Waiting     | Work blocked by defined dependency                     | Owning Support Group        |
| Resolved    | Service restored; awaiting final validation or closure | Owning Support Group        |
| Closed      | Workflow complete                                      | Final Owning Group          |
| Reopened    | Issue returned after resolution                        | Owning Support Group        |
| Cancelled   | Record invalid, duplicate, or no longer required       | Authorized Support Role     |

---

# 4. Core Workflow

```text
Incident Created
      ↓
Validate Minimum Data
      ↓
Classify Service / Category
      ↓
Determine Impact + Urgency
      ↓
Calculate Priority
      ↓
Assign Owning Group
      ↓
Investigate / Diagnose
      ↓
Resolution Found?
   ↙            ↘
 No              Yes
 ↓                ↓
Escalate /       Restore Service
Consult /            ↓
Vendor              Validate
 ↓                   ↓
Continue          Resolve
                     ↓
                   Close
```

A polished version will be maintained in:

[Incident Management Workflow](../diagrams/incident%20management%20workflow.md)

---

# 5. Intake Requirements

Before an incident enters active fulfillment, the record should contain enough information to support triage.

Minimum fields include:

* requester
* incident description
* affected service or category
* location where relevant
* impact
* urgency
* affected user or group
* related asset or CI where available

The platform should not force users to understand internal technical structure.

The service desk may complete or correct classification during triage.

---

# 6. Priority

Incident priority follows the approved:

**Impact + Urgency → Priority**

model.

Priority levels:

* P1 — Critical
* P2 — High
* P3 — Normal
* P4 — Low

Detailed definitions and SLA targets are maintained in:

[Priority and SLA Model](../03%20Target%20Service%20Model/priority%20and%20sla%20model.md)

Priority override is restricted and requires documented reason.

---

# 7. Assignment

Each active incident must have a defined owning support group.

Assignment may occur through:

* category rule
* service relationship
* location
* approved automation
* service desk triage

If routing confidence is low, the record should enter triage rather than be automatically sent through several incorrect queues.

---

# 8. Handoffs

Reassignment requires:

* destination group
* reassignment reason
* current troubleshooting summary
* relevant findings
* expected next action

The receiving group should not have to reconstruct the incident from the beginning.

For complex cases, consultation should be used where another team’s expertise is required but ownership does not need to change.

---

# 9. Waiting States

Waiting states represent genuine external dependency.

Approved conditions may include:

* Waiting on User
* Waiting on Vendor
* Waiting on Scheduled Activity

The owning support group remains accountable.

A waiting state does not mean the ticket no longer has an owner.

SLA pause behavior follows the applicable service policy.

---

# 10. Escalation

Incident escalation may be:

## Functional

Additional technical expertise is required.

Example:

```text
Service Desk
   ↓
Application Support
   ↓
Database Support
```

## Hierarchical

Management visibility is required due to:

* business impact
* SLA risk
* repeated reassignment
* unresolved ownership
* extended vendor dependency

Example:

```text
Technician
   ↓
Group Lead
   ↓
Service Owner
   ↓
IT Management
```

Escalation does not automatically transfer ownership.

---

# 11. P1 Incident Handling

P1 incidents use an accelerated path.

```text
P1 Identified
    ↓
Immediate Assignment
    ↓
Technical Lead Engaged
    ↓
Service Owner / Management Notified
    ↓
Active Coordinated Response
    ↓
Periodic Status Updates
    ↓
Service Restored
    ↓
Validation
    ↓
Review
```

P1 incidents should be rare enough that the designation still means something.

---

# 12. Major Incident Path

A P1 may be designated as a Major Incident when broader coordination is required.

Potential triggers include:

* enterprise-critical service outage
* multiple facilities affected
* broad operational impact
* severe external impact
* major security or safety consequence

A Major Incident may add:

* incident coordinator
* communications lead
* technical workstream leads
* executive visibility

This case study does not attempt to build a full Major Incident Management framework.

---

# 13. Duplicate Incidents

When multiple users report the same underlying condition, the workflow should support:

* duplicate designation
* parent/child relationship
* common status communication
* affected-user tracking

Example:

```text
Primary Incident
   ├── Duplicate 1
   ├── Duplicate 2
   └── Duplicate 3
```

The goal is to avoid several teams troubleshooting the same problem independently.

AI-assisted duplicate suggestion may be introduced later but should remain reviewable.

---

# 14. Asset and CI Relationships

Where relevant, an incident should be associated with:

* affected service
* asset
* configuration item
* location
* recent change

These relationships support:

* troubleshooting
* impact analysis
* recurrence analysis
* change correlation

Detailed structure:

[Service Management Data Model](../05%20Data%20and%20Configuration%20Model/service%20management%20data%20model.md)

---

# 15. Change Correlation

During investigation, technicians should be able to identify relevant recent changes.

If a change appears to have caused the incident:

* associate the incident with the change
* retain both records
* document service impact
* follow change backout or review process where applicable

A failed change should not become an unrelated incident simply because the workflows use different record types.

---

# 16. Vendor Dependency

If vendor support is required:

```text
Incident
   ↓
Internal Owner
   ↓
Vendor Case Opened
   ↓
Vendor Activity
   ↓
Internal Validation
   ↓
Resolution
```

The internal incident should retain:

* internal owner
* vendor
* vendor case number
* current dependency
* latest material update
* next action

`Waiting on Vendor` describes status.

It does not replace internal ownership.

---

# 17. Resolution Criteria

An incident may move to `Resolved` when:

* service is restored
* workaround is accepted where appropriate
* required technical action is complete
* related change or vendor activity is documented
* resolution summary is entered

Required resolution fields should include:

* resolution category
* resolution summary
* action taken
* affected service / CI where applicable
* related knowledge where useful

---

# 18. Closure Criteria

An incident may move to `Closed` when:

* resolution criteria are complete
* required user validation has occurred or defined closure period has passed
* mandatory record fields are complete
* related records are linked where applicable

A closure note of only:

> "Fixed"

does not meet the target record-quality standard.

The goal is enough information to make the record useful later without turning every incident into a technical report.

---

# 19. Reopen Handling

A recently resolved incident may be reopened when:

* the same issue returns
* the resolution did not restore expected service
* user validation fails

Reopening must preserve:

* prior resolution
* previous owner
* reopen reason
* previous timestamps

Repeated reopen activity may indicate:

* weak resolution
* poor closure validation
* recurring defect

---

# 20. Cancellation

An incident may be cancelled when:

* created in error
* duplicate and formally associated
* requester confirms no issue exists
* record belongs to another process type

Cancellation requires a reason.

Cancelled records remain auditable.

---

# 21. Exception Handling

| Condition                | Workflow Response                                |
| ------------------------ | ------------------------------------------------ |
| Insufficient intake data | Return to triage                                 |
| Ownership unclear        | Service desk / process-owner review              |
| Reassignment loop        | Escalate for ownership decision                  |
| User nonresponse         | Reminder → final notice → controlled closure     |
| Vendor delay             | Vendor escalation while retaining internal owner |
| SLA breach               | Hierarchical escalation                          |
| Failed automation        | Manual exception queue                           |
| Priority dispute         | Authorized review / documented override          |
| Failed change suspected  | Link change and incident                         |

---

# 22. Incident Decision Table

| Condition                     | Action                   | Ownership               |
| ----------------------------- | ------------------------ | ----------------------- |
| Service desk can resolve      | Resolve incident         | Service Desk            |
| Specialist advice required    | Consult specialist       | Current Group           |
| Specialist ownership required | Reassign                 | New Support Group       |
| User response required        | Waiting on User          | Current Group           |
| Vendor support required       | Waiting on Vendor        | Current Group           |
| SLA at risk                   | Escalate                 | Current Group           |
| P1 identified                 | Accelerated escalation   | Assigned Resolver Group |
| Duplicate identified          | Link to primary incident | Defined Primary Owner   |
| Failed change suspected       | Link to change           | Incident Owner retained |
| Resolution unsuccessful       | Reopen                   | Owning Support Group    |

---

# 23. Required Controls

| Control                      | Purpose                             |
| ---------------------------- | ----------------------------------- |
| Minimum intake data          | Improve triage quality              |
| Calculated priority          | Standardize severity                |
| Restricted priority override | Preserve accountability             |
| Required ownership           | Prevent ownerless incidents         |
| Reassignment history         | Preserve handoff traceability       |
| SLA timers                   | Measure service expectation         |
| Waiting-state rules          | Prevent SLA manipulation            |
| Closure requirements         | Improve historical value            |
| Duplicate linkage            | Reduce repeated work                |
| Audit history                | Preserve material workflow activity |

Detailed controls will be maintained in:

[Governance and Controls](../06%20Governance%20and%20Controls/governance%20model.md)

---

# 24. Incident Metrics

Core incident measures include:

| Metric                     | Purpose                         |
| -------------------------- | ------------------------------- |
| First Response Time        | Measure engagement speed        |
| Mean Time to Resolution    | Measure restoration performance |
| SLA Compliance             | Measure service commitment      |
| Reassignment Rate          | Identify routing weakness       |
| Reopen Rate                | Identify resolution quality     |
| Repeat Incident Rate       | Identify recurring issues       |
| P1/P2 Volume               | Monitor high-impact demand      |
| Vendor Dependency Time     | Identify external delay         |
| Time to Correct Assignment | Measure routing quality         |
| CI Association Rate        | Measure operational context     |

Detailed metric definitions:

[Performance Framework](../11%20Metrics%20and%20Optimization/performance%20framework.md)

---

# 25. Testing Mapping

Representative validation scenarios include:

| Test ID   | Scenario                                         |
| --------- | ------------------------------------------------ |
| TC-INC-01 | Create and route standard incident               |
| TC-INC-02 | Associate duplicate incident                     |
| TC-INC-03 | Calculate P1 priority                            |
| TC-INC-04 | Require reassignment reason                      |
| TC-INC-05 | Retain ownership while waiting on vendor         |
| TC-SLA-01 | Pause and resume SLA                             |
| TC-SLA-02 | Trigger breach escalation                        |
| TC-CLS-01 | Prevent closure without required resolution data |
| TC-CHG-01 | Link incident to relevant change                 |

These will be formalized in:

[Testing and UAT](../09%20Testing%20and%20UAT/test%20cases.md)

---

# 26. Incident Workflow Success Criteria

The workflow is design-ready when:

* incident states are approved
* minimum intake data is defined
* impact and urgency rules are approved
* ownership and routing are defined
* escalation paths are defined
* waiting-state behavior is defined
* P1 handling is defined
* duplicate handling is defined
* vendor dependency is defined
* closure criteria are defined
* testing scenarios are identified
* reporting fields are known

---

# 27. Incident Management Conclusion

The target Incident Management workflow is not intended to control every technical decision a support team makes.

It is intended to make sure the organization does not lose the basics while people are solving the problem:

* what is affected
* how important it is
* who owns it
* what has already been tried
* whether another team or vendor is involved
* whether service expectations are at risk
* what actually resolved it

Technical troubleshooting can remain flexible.

The service process around that troubleshooting should not be.

**Next:** [Service Request Management](./service%20request%20management.md)
