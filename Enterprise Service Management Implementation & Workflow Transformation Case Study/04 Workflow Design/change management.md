# Change Management

## Purpose

The Change Management workflow defines how the organization evaluates, authorizes, schedules, implements, validates, and closes changes that may affect supported services, systems, or configuration items.

The goal is not to slow down technical work.

The goal is to make sure changes with meaningful operational impact are reviewed with enough discipline that the organization understands:

* what is changing
* why it is changing
* what may be affected
* who authorized it
* how it will be implemented
* how failure will be handled
* whether the change actually worked

The operating principle is:

> **Change control should scale with risk, not treat every technical action the same.**

This workflow builds on:

* [Target Operating Model](../03%20Target%20Service%20Model/target%20operating%20model.md)
* [Priority and SLA Model](../03%20Target%20Service%20Model/priority%20and%20sla%20model.md)
* [Ownership and Escalation](../03%20Target%20Service%20Model/ownership%20and%20escalation.md)
* [Functional Requirements](../02%20Requirements%20Discovery/functional%20requirements.md)

---

# 1. Scope

Change Management applies to planned activity that may alter:

* production systems
* infrastructure
* applications
* configuration
* access-control logic
* integrations
* service-management workflows
* other supported technical services

Not every technical action requires the same change process.

The target model distinguishes between:

* Standard Change
* Normal Change
* Emergency Change

This keeps low-risk repeatable work moving while applying stronger review to higher-risk activity.

---

# 2. Change Types

## Standard Change

A pre-authorized, repeatable, low-risk change with a documented implementation pattern.

Examples may include:

* approved routine endpoint configuration
* recurring certificate update
* standard account configuration
* known maintenance activity

A Standard Change still requires a record.

It simply does not require the same approval cycle every time.

---

## Normal Change

A planned change requiring evaluation and authorization before implementation.

Examples include:

* application configuration change
* infrastructure modification
* network rule change
* production integration change
* significant workflow configuration change

The approval path depends on risk and impact.

---

## Emergency Change

A change required quickly to:

* restore critical service
* contain serious risk
* address urgent vulnerability
* prevent material business disruption

Emergency does not mean uncontrolled.

It means the approval path is compressed because delay creates greater risk than normal review time.

---

# 3. Core Change States

```text id="wx2i13"
Draft
  ↓
Assessment
  ↓
Pending Approval
  ↓
Scheduled
  ↓
Implementation
  ↓
Validation
  ↓
Completed
```

Exception states may include:

* Rejected
* Cancelled
* Failed
* Backout
* Emergency Review

---

# 4. State Definitions

| State            | Purpose                                             | Primary Owner               |
| ---------------- | --------------------------------------------------- | --------------------------- |
| Draft            | Proposed change being documented                    | Change Requester / Owner    |
| Assessment       | Risk, impact, dependencies, and readiness evaluated | Change Owner                |
| Pending Approval | Required authorization outstanding                  | Change Owner / Approver     |
| Scheduled        | Approved change awaiting implementation window      | Change Owner                |
| Implementation   | Technical work in progress                          | Change Implementer          |
| Validation       | Outcome and service condition being confirmed       | Change Owner / Validator    |
| Completed        | Successful change closed                            | Change Owner                |
| Failed           | Change did not achieve expected result              | Change Owner                |
| Backout          | Reversal or recovery activity underway              | Change Owner / Implementer  |
| Rejected         | Authorization denied                                | Approver / Change Authority |
| Cancelled        | Change withdrawn or no longer required              | Change Owner                |

---

# 5. Core Workflow

```text id="fefb6e"
Change Proposed
      ↓
Document Scope / Reason
      ↓
Assess Risk and Impact
      ↓
Change Type
      ↓
Approval Required?
   ↙              ↘
 No                Yes
 ↓                  ↓
Schedule          Approval
                     ↓
                  Approved?
                 ↙        ↘
               Yes         No
                ↓           ↓
             Schedule     Rejected
                ↓
          Implementation
                ↓
           Validate Result
            ↙          ↘
        Successful     Failed
            ↓            ↓
         Complete      Backout /
                       Stabilize
                          ↓
                     Review / Close
```

A polished visual will be maintained in:

[Change Management Workflow](../diagrams/change%20management%20workflow.md)

---

# 6. Change Record Requirements

Before a change can move into approval or scheduling, it should contain enough information to support a real decision.

Required information should include:

* change title
* business or technical reason
* change owner
* implementer
* affected service
* affected CI or asset where applicable
* implementation plan
* validation plan
* risk assessment
* expected impact
* planned date/time
* backout plan where required
* related incident or request where applicable

A change record should explain the work well enough that an approver can understand what they are authorizing.

---

# 7. Change Ownership

Each change must have a defined Change Owner.

The Change Owner is accountable for the lifecycle of the change.

That includes:

* record completeness
* assessment
* coordination
* approval
* scheduling
* implementation readiness
* validation
* closure

The Change Owner may not personally perform the technical work.

Example:

```text id="cqg3h5"
Change Owner
    │
    ├── Implementer
    ├── Service Owner
    ├── Approver
    └── Validator
```

---

# 8. Risk Assessment

Change risk should reflect the likely business consequence if the change causes a problem.

A simple risk model may consider:

* service criticality
* number of users affected
* technical complexity
* reversibility
* testing maturity
* implementation duration
* dependency count
* prior history
* security effect

The model should remain practical enough to use consistently.

---

# 9. Initial Risk Levels

| Risk   | General Condition                                                             | Example                          |
| ------ | ----------------------------------------------------------------------------- | -------------------------------- |
| Low    | Limited impact, proven method, easy backout                                   | Routine approved configuration   |
| Medium | Meaningful service impact or moderate complexity                              | Application configuration change |
| High   | Critical service, broad impact, difficult backout, or significant uncertainty | Core infrastructure change       |

Risk level drives the approval and validation model.

---

# 10. Change Approval Model

Approval authority should scale with risk.

| Change Type / Risk | Approval Model                                                         |
| ------------------ | ---------------------------------------------------------------------- |
| Standard Change    | Pre-authorized pattern                                                 |
| Low-Risk Normal    | Technical / Service Owner approval                                     |
| Medium-Risk Normal | Service Owner + Change Authority                                       |
| High-Risk Normal   | Change Authority + Service Owner + additional stakeholders as required |
| Emergency          | Emergency Change Authority / defined expedited approval                |

This structure keeps governance proportional to actual risk.

---

# 11. Approval Decision

Approvers should evaluate:

* business need
* service impact
* timing
* risk
* implementation readiness
* validation
* backout
* conflicts with other scheduled work

Approval is not a technical rubber stamp.

The approver is authorizing the organization to accept the implementation risk under the proposed conditions.

---

# 12. Separation of Duties

Higher-risk changes may require separation among:

* requester
* implementer
* approver
* validator

The exact separation should depend on risk.

For a low-risk routine change, one individual may reasonably hold several roles.

For a high-risk production change, independent approval and validation may be required.

The target model avoids both extremes:

* no separation where risk demands it
* unnecessary separation for trivial work

---

# 13. Scheduling

Approved changes should be scheduled against:

* service support windows
* maintenance windows
* business events
* other planned changes
* known freeze periods

The platform should support enough visibility to identify potentially conflicting changes.

A scheduled change should have:

* approved date/time
* expected duration
* affected service
* implementation owner
* communication requirements

---

# 14. Change Collision

Two individually reasonable changes may create unnecessary risk when implemented at the same time.

Example:

```text id="ik87ia"
Network Change
      +
Application Deployment
      ↓
Same Service Window
      ↓
Higher Combined Risk
```

The target workflow should make overlapping affected services or CIs visible during scheduling where possible.

Not every collision requires cancellation.

It requires awareness and a deliberate decision.

---

# 15. Implementation Readiness Gate

Before entering `Implementation`, the change should satisfy applicable readiness conditions.

| Readiness Item                       | Required         |
| ------------------------------------ | ---------------- |
| Approval complete                    | Yes              |
| Implementation plan complete         | Yes              |
| Validation plan complete             | Yes              |
| Backout plan complete where required | Yes              |
| Required personnel available         | Yes              |
| Maintenance window confirmed         | Where applicable |
| Stakeholder communication complete   | Where applicable |
| Dependencies available               | Yes              |

If required readiness conditions are not met, the change should be rescheduled rather than pushed forward because the calendar says it is time.

---

# 16. Implementation

During implementation, the change record should capture material activity such as:

* implementation start
* technical actions
* unexpected condition
* deviation from plan
* decision to continue or back out
* implementation completion

The level of detail should match the change risk.

A low-risk standard change does not need the same running record as a high-risk infrastructure change.

---

# 17. Validation

A change is not successful simply because the implementation steps finished.

Validation should confirm that:

* expected change occurred
* affected service is operating
* required function works
* no unexpected impact is observed

Example:

```text id="a4hqqx"
Implementation Complete
       ↓
Technical Validation
       ↓
Service Validation
       ↓
Expected Result?
   ↙            ↘
 Yes             No
 ↓                ↓
Success         Failure Path
```

The validation method should be identified before implementation, not invented afterward.

---

# 18. Change Outcomes

The target model distinguishes three primary outcomes.

## Successful

Implementation completed and expected result validated.

## Successful with Issue

Primary objective achieved, but a secondary issue or deviation occurred.

## Unsuccessful

Expected result was not achieved or service impact required rollback, recovery, or corrective action.

These distinctions support more useful change metrics than a simple open/closed status.

---

# 19. Failed Change

A failed change requires deliberate response.

```text id="hsxs9v"
Validation Fails
      ↓
Service Impact?
   ↙           ↘
 Yes            No
 ↓               ↓
Stabilize      Evaluate
 ↓
Backout Required?
 ↙            ↘
Yes             No
 ↓               ↓
Backout       Corrective Action
 ↓               ↓
Validate ←───────┘
      ↓
Incident Required?
      ↓
Change Review
```

A failed change should remain identifiable as a failed change even when service has been restored.

---

# 20. Backout

Backout is the defined method for reversing or recovering from an unsuccessful implementation.

Where required, the change record should identify:

* backout trigger
* backout steps
* responsible implementer
* expected recovery time
* validation after backout

A backout plan of:

> "Restore previous configuration"

is not sufficient for a high-risk change unless the method is actually understood and tested.

---

# 21. Incident Relationship

If a change causes or materially contributes to a service interruption, the resulting incident should be linked to the change.

```text id="pmwvhg"
Change
  ↓
Implementation Failure
  ↓
Incident
  ↕
Change Relationship
```

The relationship should remain visible from both records.

This allows incident responders to quickly see relevant implementation context and allows change reporting to identify service impact caused by change.

---

# 22. Change Related to Incident or Request

A change may also originate from existing service activity.

Examples:

```text id="xc0ppm"
Incident
   ↓
Permanent Fix Requires Change
   ↓
Change Record
```

or:

```text id="y1fsg5"
Service Request
      ↓
Request Exceeds Standard Fulfillment
      ↓
Change Required
```

The original business context should remain traceable rather than disappearing when a new record type is created.

---

# 23. Emergency Change

Emergency change exists for conditions where waiting for normal approval creates greater risk.

Potential triggers include:

* P1 incident
* active security vulnerability
* critical service restoration
* urgent production defect
* significant operational exposure

Emergency workflow:

```text id="p0fxfq"
Emergency Condition
      ↓
Document Minimum Required Information
      ↓
Emergency Authority
      ↓
Approve / Reject
      ↓
Implementation
      ↓
Validation
      ↓
Post-Implementation Review
```

Emergency process should reduce approval time.

It should not remove accountability.

---

# 24. Emergency Change Requirements

At minimum, an emergency change should capture:

* reason emergency treatment is required
* affected service / CI
* implementation plan
* expected impact
* emergency approver
* implementation result
* validation
* post-implementation review

Where time prevents full documentation before implementation, required information should be completed immediately afterward.

---

# 25. Emergency Change Review

Emergency changes should receive retrospective review.

The review should ask:

* Was emergency classification justified?
* Did the change succeed?
* Was service impact acceptable?
* Was the approval process followed?
* Should this become a Standard Change?
* Could the emergency have been avoided through better planning?

Emergency volume itself should become a metric.

Too many emergency changes usually indicate another process problem.

---

# 26. Standard Change Model

Standard Changes represent repeatable work with known risk and method.

A Standard Change template should define:

* scope
* prerequisites
* implementation steps
* expected duration
* affected service / CI
* validation
* backout
* pre-authorized conditions

If the implementation falls outside the approved pattern, it becomes a Normal Change.

---

# 27. Standard Change Review

Standard Change templates should be reviewed periodically.

Review should consider:

* success rate
* failure history
* changed dependencies
* updated implementation method
* continued appropriateness of pre-authorization

Pre-authorized does not mean permanently exempt from governance.

---

# 28. Change Communication

Communication requirements should scale with impact.

| Risk / Impact | Communication                                  |
| ------------- | ---------------------------------------------- |
| Low           | Internal technical notification where required |
| Medium        | Affected stakeholders / service owner          |
| High          | Broad stakeholder communication                |
| Emergency     | Immediate operational communication            |

Communication may include:

* planned start
* expected impact
* service interruption
* completion
* failure / extension
* restoration

---

# 29. Vendor-Implemented Change

A vendor may perform the technical work.

The internal organization still retains a Change Owner.

```text id="usfd69"
Internal Change Owner
        ↓
Vendor Implementer
        ↓
Internal Validation
        ↓
Change Outcome
```

The change record should include:

* vendor
* vendor reference
* approved implementation scope
* vendor activity
* internal validation

Vendor implementation does not remove internal authorization or accountability.

---

# 30. Change and Configuration Relationships

Applicable changes should link to affected:

* service
* CI
* asset
* application
* location

This supports:

* risk assessment
* scheduling
* impact analysis
* incident correlation
* change reporting

Detailed relationships:

[Service Management Data Model](../05%20Data%20and%20Configuration%20Model/service%20management%20data%20model.md)

---

# 31. Change Controls

| Control                   | Purpose                               |
| ------------------------- | ------------------------------------- |
| Required Change Owner     | Maintain lifecycle accountability     |
| Risk classification       | Scale governance                      |
| Approval gate             | Prevent unauthorized change           |
| Separation of duties      | Reduce conflict of interest           |
| Implementation plan       | Define execution                      |
| Backout plan              | Support recovery                      |
| Validation requirement    | Confirm outcome                       |
| Change / CI relationship  | Improve impact visibility             |
| Change / incident linkage | Preserve failure traceability         |
| Emergency review          | Prevent emergency-process abuse       |
| Standard Change review    | Maintain pre-authorization quality    |
| Audit history             | Preserve decision and activity record |

Detailed control mapping will be maintained in:

[Governance and Controls](../06%20Governance%20and%20Controls/governance%20model.md)

---

# 32. Change Decision Table

| Condition                                       | Change Type / Action             |
| ----------------------------------------------- | -------------------------------- |
| Repeatable, approved, low-risk pattern          | Standard Change                  |
| Planned change outside Standard pattern         | Normal Change                    |
| Delay creates unacceptable operational risk     | Emergency Change                 |
| Risk increases during assessment                | Increase approval level          |
| Readiness criteria incomplete                   | Reschedule                       |
| Validation succeeds                             | Complete                         |
| Validation identifies issue                     | Successful with Issue / evaluate |
| Service impact occurs                           | Stabilize / Incident             |
| Backout required                                | Execute Backout                  |
| Change falls outside approved Standard template | Convert to Normal Change         |

---

# 33. Change Metrics

| Metric                     | Purpose                                   |
| -------------------------- | ----------------------------------------- |
| Change Success Rate        | Measure implementation quality            |
| Failed Change Rate         | Identify unstable change activity         |
| Backout Rate               | Measure recovery frequency                |
| Emergency Change Rate      | Identify planning or operational pressure |
| Incidents Caused by Change | Measure service impact                    |
| Changes by Service         | Understand change volume                  |
| Approval Cycle Time        | Identify governance delay                 |
| Rescheduled Change Rate    | Identify readiness problems               |
| Standard Change Success    | Validate pre-authorized templates         |
| Change Collision Count     | Identify scheduling risk                  |

Metrics should be reviewed by service and change type rather than only as an enterprise total.

---

# 34. Testing Mapping

Representative validation scenarios include:

| Test ID   | Scenario                                                  |
| --------- | --------------------------------------------------------- |
| TC-CHG-01 | Standard change follows pre-authorized path               |
| TC-CHG-02 | Normal change requires risk-based approval                |
| TC-CHG-03 | High-risk change cannot bypass approval                   |
| TC-CHG-04 | Incomplete readiness prevents implementation              |
| TC-CHG-05 | Failed change activates backout path                      |
| TC-CHG-06 | Failed change links to resulting incident                 |
| TC-CHG-07 | Emergency change requires retrospective review            |
| TC-CHG-08 | Standard change outside approved scope converts to Normal |
| TC-CHG-09 | Vendor-implemented change retains internal owner          |
| TC-CHG-10 | Change cannot close without validation result             |

These will be formalized in:

[Testing and UAT](../09%20Testing%20and%20UAT/test%20cases.md)

---

# 35. Change Workflow Success Criteria

The Change Management workflow is design-ready when:

* change types are defined
* risk levels are defined
* approval authority is defined
* change ownership is defined
* readiness criteria are defined
* scheduling behavior is defined
* implementation data requirements are defined
* validation requirements are defined
* failed-change behavior is defined
* backout expectations are defined
* incident relationships are defined
* emergency treatment is defined
* Standard Change governance is defined
* metrics and tests are identified

---

# 36. Change Management Conclusion

The target Change Management process is designed to reduce unnecessary operational risk without creating a heavyweight approval process around every technical action.

Routine, proven work should move quickly.

Higher-risk work should receive more scrutiny.

Emergency work should move fast without becoming invisible.

And when a change fails, the organization should be able to see exactly what changed, what was affected, how service was restored, and what should be learned from it.

The goal is not zero failed changes.

That is not realistic.

The goal is fewer avoidable failures, faster recovery when they occur, and enough traceability to stop making the same mistake twice.

**Next:** [Knowledge Management](./knowledge%20management.md)
