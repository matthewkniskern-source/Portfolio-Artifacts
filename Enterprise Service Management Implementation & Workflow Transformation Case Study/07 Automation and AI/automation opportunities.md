# Automation Opportunities

## Purpose

This artifact identifies where automation can improve the target Enterprise Service Management environment without automating around poor process, incomplete data, or unclear decision authority.

The target state already defines:

* standardized intake
* ownership
* prioritization
* SLA behavior
* approvals
* workflow states
* data relationships
* governance controls

Automation should build on those decisions.

It should not replace them.

The operating principle is:

> **Automate repeatable decisions. Do not use automation to avoid making the decision in the first place.**

This artifact builds on:

* [Target Operating Model](../03%20Target%20Service%20Model/target%20operating%20model.md)
* [Service Catalog](../03%20Target%20Service%20Model/service%20catalog.md)
* [Governance Model](../06%20Governance%20and%20Controls/governance%20model.md)
* [Control Matrix](../06%20Governance%20and%20Controls/control%20matrix.md)
* [Data Governance](../05%20Data%20and%20Configuration%20Model/data%20governance.md)

---

# 1. Automation Objectives

Automation should reduce:

* manual routing
* repetitive approvals
* missed SLA events
* unnecessary technician touch
* duplicate administrative work
* avoidable follow-up
* stale temporary access
* inconsistent notifications
* hidden automation failures

The objective is not to maximize the number of automated steps.

The objective is to remove repeatable friction while preserving visibility and control.

---

# 2. Automation Design Principles

## 2.1 Automate Stable Rules

A good automation candidate has:

* clear trigger
* reliable data
* predictable decision logic
* known outcome
* defined exception path

If the process still depends on argument or interpretation every time it runs, it is probably not ready for automation.

---

## 2.2 Keep Ownership Visible

Automation may perform an action.

It should not make ownership disappear.

Example:

```text id="1lym1t"
Service Request
      ↓
Automatic Routing
      ↓
Fulfillment Group
```

The record still has an accountable owner after the automation executes.

---

## 2.3 Fail Visibly

Automation failure should create a condition someone can act on.

Example:

```text id="fs57jy"
Automation
    ↓
Execution Fails
    ↓
Exception
    ↓
Assigned Owner
```

Silent failure is worse than manual work because it creates the appearance that the process is functioning.

---

## 2.4 Log Material Actions

Automated actions that affect:

* assignment
* approval
* access
* SLA
* status
* notifications
* configuration

should remain traceable.

---

## 2.5 Do Not Automate Weak Data

Automation depends on structured data being reliable.

A routing rule based on stale service ownership will simply route bad data faster.

---

# 3. Automation Candidate Evaluation

Each candidate should be evaluated against five questions.

| Question                       | Why It Matters                   |
| ------------------------------ | -------------------------------- |
| Is the trigger clear?          | Prevents unpredictable execution |
| Is the required data reliable? | Prevents bad automated decisions |
| Is the action repeatable?      | Confirms automation fit          |
| Is the risk acceptable?        | Determines control strength      |
| Is there an exception path?    | Prevents silent process failure  |

A candidate that fails several of these checks should remain manual until the underlying design improves.

---

# 4. Automation Opportunity Categories

The target implementation identifies six primary automation areas.

| Area                        | Examples                                      |
| --------------------------- | --------------------------------------------- |
| Intake and Routing          | Categorization, assignment, queue routing     |
| SLA and Escalation          | Timers, warnings, breach escalation           |
| Approval                    | Routing, reminders, delegation                |
| Fulfillment                 | Task creation, standard execution             |
| Access Lifecycle            | Provisioning support, expiration, disablement |
| Notifications and Follow-Up | Status, reminders, confirmation               |

Additional automation may support:

* change management
* knowledge
* reporting
* data quality

---

# 5. Intake Automation

Potential intake automation includes:

* form prepopulation
* identity lookup
* department / location population
* service selection
* category suggestion
* request template selection
* duplicate detection
* required-field validation

Example:

```text id="4co3ym"
User Submits Request
      ↓
Identity Data Added
      ↓
Service Identified
      ↓
Required Fields Validated
      ↓
Route
```

The user should not be required to manually supply data already known by the organization.

---

# 6. Routing Automation

Routing is one of the strongest automation candidates because ownership has already been defined in the target model.

Example:

```text id="2a8q1b"
Service
  ↓
Owning Support Group
  ↓
Automatic Assignment
```

Possible routing inputs include:

* service
* catalog item
* category
* location
* CI
* request type

The routing hierarchy should be explicit.

---

# 7. Routing Exception

If the rule cannot identify a valid destination:

```text id="ydv8u5"
Request
   ↓
Routing Rule
   ↓
No Valid Group
   ↓
Triage Exception Queue
```

The system should not select a random group simply to avoid an unassigned record.

---

# 8. Priority Automation

Incident priority may be calculated from:

* impact
* urgency

Example:

```text id="pxggxr"
Impact + Urgency
       ↓
Priority Matrix
       ↓
P1 / P2 / P3 / P4
```

This is a strong automation candidate because the decision model is explicitly defined.

Authorized override remains available through governance controls.

---

# 9. SLA Automation

The platform should automate:

* SLA start
* pause
* resume
* warning
* breach
* stop

according to the defined SLA state model.

Example:

```text id="9tg97w"
Ticket Created
     ↓
SLA Starts
     ↓
75% Threshold
     ↓
Warning
     ↓
90%
     ↓
Escalation
```

The SLA logic should not depend on technicians manually remembering when escalation is due.

---

# 10. Escalation Automation

Potential automated escalation includes:

* approaching SLA breach
* actual breach
* aging approval
* repeated reassignment
* inactive ticket
* high-priority incident

Example:

```text id="noqxez"
P1 Incident
    ↓
Defined Time Threshold
    ↓
Group Lead
    ↓
Service Owner / Management
```

Automation can initiate the escalation.

Human ownership still determines the response.

---

# 11. Approval Routing Automation

Approval routing should use defined business logic.

Possible inputs include:

* request type
* requester manager
* service owner
* system owner
* risk
* access type

Example:

```text id="fhah2i"
Privileged Access
      ↓
Manager
      ↓
System Owner
      ↓
Security
```

Routing can be automated.

The approval decision should remain with the authorized approver.

---

# 12. Approval Reminder Automation

Pending approval should trigger reminders based on time.

Example:

```text id="k9lj2g"
Approval Requested
      ↓
Reminder
      ↓
Second Reminder
      ↓
Escalation
```

This removes the need for requesters to manually chase approval status.

---

# 13. Approval Delegation

Where approved delegation exists, the platform may automatically redirect approvals during a defined absence.

Required conditions include:

* authorized delegate
* start date
* end date
* approval scope

Delegation should expire automatically.

---

# 14. Service Request Task Automation

Approved catalog requests may automatically generate fulfillment tasks.

Example:

```text id="rgg8ie"
Laptop Request
     ↓
Approved
     ↓
Create Tasks
 ├── Prepare Device
 ├── Update Asset
 ├── Configure Access
 └── Deliver
```

This creates consistent fulfillment without requiring a coordinator to recreate the same task structure every time.

---

# 15. Standard Fulfillment Automation

Some low-risk fulfillment actions may be integrated directly with downstream systems.

Examples may include:

* standard software deployment
* group membership
* mailbox creation
* account configuration
* device-management action

Automation should only proceed when:

* approval requirements are satisfied
* identity is validated
* target is clear
* failure can be detected

---

# 16. Fulfillment Exception

Example:

```text id="hl2fcu"
Approved Request
      ↓
Automated Fulfillment
      ↓
Failure
      ↓
Manual Fulfillment Task
      ↓
Assigned Technical Owner
```

The user-facing request should remain active until actual fulfillment is confirmed.

---

# 17. Temporary Access Expiration

Temporary access is a high-value automation candidate.

Example:

```text id="zgr1p2"
Temporary Access
      ↓
Start
      ↓
Active
      ↓
Expiration Date
      ↓
Disable
```

Where direct disablement is supported, the system should perform or trigger it automatically.

Where it is not:

```text id="t7vhym"
Expiration
    ↓
Manual Disablement Task
    ↓
Assigned Owner
    ↓
Completion Evidence
```

The control objective remains the same.

---

# 18. Vendor Access Automation

Vendor access may use automation for:

* approval routing
* expiration
* reminders
* extension workflow
* disablement task generation
* sponsor notification

The system should never automatically extend vendor access because the expiration date arrived.

An extension is a new authorization decision.

---

# 19. Incident Notification Automation

Potential incident notifications include:

* assignment
* P1 escalation
* requester update
* waiting-state reminder
* resolution
* closure

Notifications should support the process.

They should not flood users with messages for every minor state transition.

---

# 20. Major Incident Automation

For defined P1 or Major Incident conditions, automation may:

* create major incident record
* notify designated responders
* establish bridge / coordination channel
* identify affected services
* trigger management communication
* increase update cadence

The platform should accelerate coordination without pretending that incident command itself can be automated.

---

# 21. Waiting-on-Requester Automation

Example:

```text id="3bn7hl"
Waiting on Requester
      ↓
Reminder
      ↓
Final Reminder
      ↓
Cancel / Close per Policy
```

This reduces stale tickets while preserving a documented communication path.

---

# 22. Change Management Automation

Potential change automation includes:

* risk calculation support
* approval routing
* readiness validation
* scheduling notifications
* change collision warning
* implementation reminders
* post-change validation task
* PIR creation for failed or emergency change

Example:

```text id="e4860g"
Normal Change
     ↓
Risk Level
     ↓
Approval Path
```

The automation should support the decision model rather than determine risk from opaque logic.

---

# 23. Standard Change Automation

Approved Standard Change templates may automate:

* required fields
* implementation tasks
* scheduling
* validation steps
* notification

If the proposed work falls outside the approved Standard Change boundary, automation should stop and route it as a Normal Change.

---

# 24. Knowledge Automation

Potential knowledge automation includes:

* create article candidate from resolution
* review-date reminders
* stale article notification
* owner notification
* article usage tracking
* retirement workflow

Example:

```text id="9yi8gg"
Resolved Incident
      ↓
Knowledge Candidate Flag
      ↓
Draft Article
```

Automatic candidate creation does not mean automatic publication.

---

# 25. Data Quality Automation

The platform may automatically identify conditions such as:

* inactive support group
* service with no owner
* knowledge past review
* expired vendor
* retired CI referenced in new work
* temporary access past expiration
* missing required relationship

These should feed data-quality exceptions.

---

# 26. Reporting Automation

Scheduled reporting may provide:

* SLA performance
* backlog
* change success
* vendor dependency
* approval aging
* control exceptions
* service performance
* data quality

Automated reporting is only valuable if definitions remain consistent and the data behind the metric is reliable.

---

# 27. Automation Priority Matrix

| Candidate                        | Value  | Complexity | Risk   | Priority      |
| -------------------------------- | ------ | ---------- | ------ | ------------- |
| Routing                          | High   | Low        | Low    | High          |
| SLA timers                       | High   | Low        | Low    | High          |
| SLA escalation                   | High   | Low        | Low    | High          |
| Approval routing                 | High   | Medium     | Medium | High          |
| Approval reminders               | Medium | Low        | Low    | High          |
| Request task creation            | High   | Low        | Low    | High          |
| Waiting reminders                | Medium | Low        | Low    | High          |
| Temporary access expiration      | High   | Medium     | High   | High          |
| Standard software fulfillment    | High   | Medium     | Medium | Medium        |
| Change collision detection       | Medium | Medium     | Medium | Medium        |
| Knowledge candidate creation     | Medium | Low        | Low    | Medium        |
| Data-quality exception detection | Medium | Medium     | Low    | Medium        |
| Complex automated risk scoring   | Medium | High       | High   | Low initially |

This supports phased automation rather than attempting to automate everything during initial configuration.

---

# 28. Automation Readiness Model

Automation should move through four readiness states.

```text id="r0taxa"
Process Defined
      ↓
Data Reliable
      ↓
Rule Validated
      ↓
Automation Enabled
```

Skipping a stage increases implementation risk.

---

# 29. Phase 1 Automation

Initial implementation should prioritize low-risk, high-value automation.

Recommended Phase 1 candidates:

* service routing
* required-field validation
* priority calculation
* SLA timers
* SLA warnings
* approval routing
* approval reminders
* fulfillment task creation
* standard notifications
* waiting-user reminders

These improve consistency without requiring deep external integration.

---

# 30. Phase 2 Automation

After workflow and data stabilization:

* software deployment integration
* account fulfillment
* vendor-access expiration
* automated access disablement
* asset updates
* change collision detection
* knowledge workflow
* data-quality monitoring

These depend more heavily on reliable integration and data.

---

# 31. Phase 3 Automation

Later optimization may include:

* advanced trend-driven routing
* predictive workload balancing
* broader orchestration
* higher-confidence AI recommendations
* more advanced service-impact automation

Phase 3 should be justified by measurable operational need.

It should not exist simply because the platform supports it.

---

# 32. Automation Risk Categories

| Risk      | Example                                               |
| --------- | ----------------------------------------------------- |
| Low       | Notification or task creation                         |
| Medium    | Routing or standard fulfillment                       |
| High      | Access provisioning or disablement                    |
| Very High | Autonomous approval or sensitive configuration change |

Higher-risk automation requires stronger:

* testing
* authorization
* monitoring
* rollback
* human oversight

---

# 33. Automation Control Model

Every material automation should define:

| Element        | Requirement                |
| -------------- | -------------------------- |
| Owner          | Who is accountable         |
| Trigger        | What starts it             |
| Inputs         | What data it uses          |
| Action         | What it does               |
| Evidence       | What it logs               |
| Failure Path   | What happens when it fails |
| Test           | How it is validated        |
| Change Control | How updates are governed   |

This turns automation from convenience scripting into managed production behavior.

---

# 34. Automation Logging

Material executions should capture:

* automation identifier
* affected record
* execution time
* result
* error where applicable
* automated change made

The logging depth should match the risk of the action.

---

# 35. Automation Failure Handling

The preferred failure model is:

```text id="1lbaae"
Automation Executes
      ↓
Success?
  ↙        ↘
Yes         No
 ↓           ↓
Continue   Log Error
              ↓
          Create Exception
              ↓
          Assign Owner
              ↓
          Manual Recovery
```

The process should remain visible from the original service record.

---

# 36. Automation Testing

Automation should be validated before production use.

Testing should include:

* expected trigger
* valid input
* invalid input
* missing data
* duplicate execution
* downstream failure
* permissions failure
* recovery path

Higher-risk automation should receive stronger negative testing.

---

# 37. Automation Metrics

| Metric                       | Purpose                        |
| ---------------------------- | ------------------------------ |
| Automation Success Rate      | Measure reliability            |
| Automation Failure Rate      | Identify unstable processes    |
| Manual Exception Rate        | Measure fallback demand        |
| Automated Routing Accuracy   | Validate assignment logic      |
| Auto-Fulfillment Rate        | Measure repeatable fulfillment |
| Average Manual Touches       | Measure effort reduction       |
| Automation Recovery Time     | Measure failure response       |
| Access Expiration Compliance | Validate lifecycle automation  |

Automation value should be measured in operational improvement, not the number of rules configured.

---

# 38. Candidate ROI View

Automation should be favored where it reduces:

* technician handling
* waiting
* handoff
* error
* repeated manual entry

Example:

```text id="1pskgc"
Manual Request
  ↓
Triage
  ↓
Route
  ↓
Approval Reminder
  ↓
Task Creation
```

may become:

```text id="kl5ih7"
Structured Request
     ↓
Automatic Route
     ↓
Automatic Approval Path
     ↓
Automatic Task Creation
```

The technical work remains.

The administrative friction around it is reduced.

---

# 39. Automation Governance

Material automation should follow:

```text id="6jyc3f"
Business Rule
     ↓
Design
     ↓
Test
     ↓
Approval
     ↓
Production
     ↓
Monitor
     ↓
Change / Retire
```

Detailed controls are defined in:

[Control Matrix](../06%20Governance%20and%20Controls/control%20matrix.md)

---

# 40. Automation Guardrails

## Do Not Automate Undefined Ownership

The rule should know who receives an exception.

## Do Not Hide Failure

Failure must produce an observable outcome.

## Do Not Let Automation Bypass Approval

Automation may route approval.

It should not invent approval authority.

## Do Not Make Integration Status Equal Business Outcome

A downstream API returning success does not always mean the user received the intended service.

Validation may still be required.

## Do Not Keep Bad Automation Because It Exists

Automation should be changed or retired when:

* exception volume is high
* rules no longer match the process
* data dependencies become unreliable
* operational cost exceeds value

---

# 41. Testing Mapping

Representative tests include:

| Test ID   | Scenario                                            |
| --------- | --------------------------------------------------- |
| TC-AUT-01 | Valid service automatically routes to correct group |
| TC-AUT-02 | Routing failure creates triage exception            |
| TC-AUT-03 | SLA warning triggers at defined threshold           |
| TC-AUT-04 | Approval reminder triggers correctly                |
| TC-AUT-05 | Approved request generates required tasks           |
| TC-AUT-06 | Fulfillment integration failure creates manual task |
| TC-AUT-07 | Temporary access expiration triggers disablement    |
| TC-AUT-08 | Automation cannot bypass required approval          |
| TC-AUT-09 | Automation execution remains auditable              |
| TC-AUT-10 | Invalid input prevents unsafe automated action      |

These will be formalized in:

[Testing and UAT](../09%20Testing%20and%20UAT/test%20cases.md)

---

# 42. Automation Success Criteria

The automation model is design-ready when:

* candidate processes are identified
* trigger logic is defined
* required data is known
* risk is classified
* ownership is assigned
* exception paths are defined
* logging requirements are defined
* testing is planned
* automation priority is established
* phased implementation is defined
* measurable outcomes exist

---

# 43. Automation Opportunities Conclusion

Automation should remove the parts of service management that people should not have to keep doing manually.

Routing the same service to the same team.

Watching the same SLA clock.

Sending the same reminder.

Creating the same fulfillment tasks.

Disabling access when an approved temporary period ends.

Those are good automation targets because the organization has already made the underlying decision.

The harder judgment should stay where it belongs:

with the people responsible for the service, risk, approval, and technical outcome.

The target state is not automation-first.

It is **process-first, data-supported, control-aware automation**.

That distinction matters.

**Next:** [AI Assisted Service Management](./ai%20assisted%20service%20management.md)
