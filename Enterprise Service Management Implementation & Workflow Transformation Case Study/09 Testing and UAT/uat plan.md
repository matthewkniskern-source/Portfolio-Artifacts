# UAT Plan

## Purpose

This artifact defines how User Acceptance Testing will confirm that the target Enterprise Service Management environment is usable, controlled, and ready for production from the perspective of the people who will actually operate it.

UAT is not intended to repeat configuration testing.

It is intended to answer a different question:

> **Can the business use the configured solution to perform the intended service process correctly under realistic conditions?**

This plan builds on:

* [Test Strategy](./test%20strategy.md)
* [Test Cases](./test%20cases.md)
* [Requirements Traceability Matrix](../02%20Requirements%20Discovery/requirements%20traceability%20matrix.md)
* [Phase Exit Criteria](../08%20Implementation%20Plan/phase%20exit%20criteria.md)

---

# 1. UAT Objectives

UAT should confirm that:

* users can complete realistic service workflows
* ownership is clear
* approvals make sense operationally
* SLA behavior matches expectations
* support teams can work queues effectively
* controls do not create unnecessary friction
* exceptions remain visible
* reporting reflects actual activity
* process roles understand what they are responsible for
* the configured environment supports the approved requirements

The objective is business acceptance.

Not simply another technical pass.

---

# 2. UAT Scope

Initial UAT should cover:

* Incident Management
* Service Request Management
* Change Management
* Knowledge Management
* Service Catalog
* Priority and SLA
* Ownership and Escalation
* Approvals
* RBAC
* Vendor Access
* Automation
* Key Reporting
* Representative AI-assisted functions where in scope

Migration validation is primarily handled separately, but migrated data should be used in UAT where it affects workflow.

---

# 3. UAT Participants

Participants should represent actual operating roles.

| Role                     | UAT Responsibility                         |
| ------------------------ | ------------------------------------------ |
| End User                 | Submit requests and incidents              |
| Service Desk Analyst     | Triage, route, resolve                     |
| Specialist Resolver      | Work technical assignments                 |
| Support Group Lead       | Manage escalation and queue behavior       |
| Approver                 | Validate approval process                  |
| Service Owner            | Validate service and SLA behavior          |
| Change Authority         | Validate change-control process            |
| Security / Risk Reviewer | Validate controlled workflows              |
| Platform Administrator   | Support execution, not business acceptance |
| Business Analyst         | Coordinate scenarios and traceability      |
| UAT Lead                 | Manage execution and results               |

The configuration team may assist.

They should not be the only people determining whether the workflow is acceptable.

---

# 4. UAT Entry Criteria

UAT should begin when:

* core configuration is stable
* test environment is available
* required test data exists
* major integrations are functioning or simulated
* critical configuration testing is complete
* RBAC is configured
* Must requirements are mapped to tests
* no known defect makes UAT broadly unusable
* UAT participants are identified and scheduled

UAT should not become the first time basic workflow configuration is exercised.

---

# 5. UAT Scenario Design

UAT scenarios should reflect realistic business activity.

A good scenario should tell the tester:

* who they are
* what they need to accomplish
* what business condition exists
* what outcome should result

Example:

```text id="1pbh7e"
You are a department manager.

A new employee requires access to a business application.

Submit the request and complete the approval workflow.

Confirm:
- the correct approver receives the request
- self-approval is not possible
- fulfillment does not begin before authorization
- the final record contains approval history
```

This is more useful than telling the tester exactly which buttons to click.

---

# 6. UAT Test Philosophy

UAT should be scenario-based rather than script-heavy.

The tester should know:

* the business objective
* the expected control
* the expected outcome

They should have enough freedom to interact with the workflow naturally.

Over-scripted UAT can prove that the tester followed instructions without proving the solution is intuitive.

---

# 7. Core UAT Scenarios

The initial UAT set should include:

| UAT ID | Scenario                      |
| ------ | ----------------------------- |
| UAT-01 | Standard Incident             |
| UAT-02 | P1 Incident and Escalation    |
| UAT-03 | Standard Service Request      |
| UAT-04 | Controlled Access Request     |
| UAT-05 | Rejected Request              |
| UAT-06 | Failed Change and Backout     |
| UAT-07 | Emergency Change              |
| UAT-08 | Vendor-Dependent Incident     |
| UAT-09 | Temporary Vendor Access       |
| UAT-10 | Knowledge Reuse               |
| UAT-11 | Automation Failure            |
| UAT-12 | Role-Based Access Restriction |
| UAT-13 | SLA Exception                 |
| UAT-14 | Reporting Reconciliation      |

These scenarios cover the highest-value target-state behaviors without trying to turn UAT into a test of every field.

---

# 8. UAT-01 — Standard Incident

## Participant

End User + Service Desk Analyst

## Scenario

A user reports a normal application issue.

## Validate

* incident intake is understandable
* ticket routes correctly
* ownership is visible
* priority is appropriate
* technician can update and resolve
* required closure data is captured
* requester receives appropriate communication

## Acceptance Outcome

The incident can move from intake to closure without manual workaround outside the platform.

---

# 9. UAT-02 — P1 Incident and Escalation

## Participant

Service Desk + Group Lead + Service Owner

## Scenario

A critical service becomes unavailable to a broad user population.

## Validate

* P1 calculation
* rapid ownership
* SLA timer
* escalation
* communication
* Major Incident path where applicable

## Acceptance Outcome

The workflow makes the severity visible and accelerates coordination without losing ownership.

---

# 10. UAT-03 — Standard Service Request

## Participant

End User + Fulfillment Team

## Scenario

A user submits a low-risk catalog request.

## Validate

* request is easy to find
* required information is clear
* approval is skipped where not required
* task routes correctly
* completion is visible

## Acceptance Outcome

The process is faster and clearer than informal request handling.

---

# 11. UAT-04 — Controlled Access Request

## Participant

Requester + Approver + Fulfillment Team

## Scenario

A user requests privileged or sensitive access.

## Validate

* required justification
* correct approval path
* self-approval restriction
* fulfillment after approval only
* audit history
* expiration where applicable

## Acceptance Outcome

The request remains usable without weakening the control.

---

# 12. UAT-05 — Rejected Request

## Participant

Requester + Approver

## Scenario

A request is denied for a valid business reason.

## Validate

* approver can reject
* rejection reason retained
* requester receives clear status
* fulfillment does not continue

## Acceptance Outcome

The workflow handles denial cleanly rather than leaving the request stuck or ambiguous.

---

# 13. UAT-06 — Failed Change and Backout

## Participant

Change Owner + Implementer + Service Owner

## Scenario

A planned production change does not validate successfully.

## Validate

* change cannot simply close as successful
* backout or corrective path is available
* service condition is revalidated
* resulting incident can be linked
* final outcome is recorded accurately

## Acceptance Outcome

Failure is visible and recoverable.

---

# 14. UAT-07 — Emergency Change

## Participant

Change Authority + Technical Team

## Scenario

A critical operational condition requires immediate change.

## Validate

* expedited approval
* minimum required data
* implementation traceability
* post-implementation validation
* retrospective review

## Acceptance Outcome

The process allows speed without removing accountability.

---

# 15. UAT-08 — Vendor-Dependent Incident

## Participant

Support Team + Vendor Coordinator

## Scenario

An incident requires external vendor support.

## Validate

* internal owner remains visible
* vendor dependency is tracked
* vendor activity can be documented
* escalation remains internal
* SLA behavior remains understandable

## Acceptance Outcome

Vendor involvement does not make the ticket disappear from organizational ownership.

---

# 16. UAT-09 — Temporary Vendor Access

## Participant

Internal Sponsor + Approver + Access Team

## Scenario

A vendor requires temporary technical access.

## Validate

* named sponsor
* approval
* defined scope
* expiration
* extension behavior
* disablement or manual fallback

## Acceptance Outcome

Temporary access behaves like temporary access.

---

# 17. UAT-10 — Knowledge Reuse

## Participant

Service Desk Analyst

## Scenario

An incident matches a known issue.

## Validate

* relevant knowledge can be found
* article is understandable
* article can be linked to ticket
* article supports resolution
* technician can flag poor or outdated content

## Acceptance Outcome

Knowledge reduces repeat troubleshooting effort.

---

# 18. UAT-11 — Automation Failure

## Participant

Service Desk / Platform Support

## Scenario

An automated routing or fulfillment action fails.

## Validate

* failure is visible
* original record remains active
* exception gets an owner
* manual recovery path exists
* user is not falsely told the work completed

## Acceptance Outcome

Automation failure does not create invisible work.

---

# 19. UAT-12 — Role-Based Access Restriction

## Participant

Multiple Roles

## Scenario

Users attempt actions outside their authorized role.

## Validate

* requester cannot view unrelated sensitive records
* technician cannot administer workflow
* unauthorized approver cannot approve controlled request
* vendor cannot see unrelated internal records

## Acceptance Outcome

Permissions match responsibility.

---

# 20. UAT-13 — SLA Exception

## Participant

Support Lead / Service Owner

## Scenario

A valid business condition requires SLA exception treatment.

## Validate

* authorized role required
* reason required
* exception remains visible
* reporting reflects the exception accurately

## Acceptance Outcome

The exception does not become a hidden way to improve SLA results.

---

# 21. UAT-14 — Reporting Reconciliation

## Participant

Service Owner / IT Management

## Scenario

Management reviews known service activity.

## Validate

* SLA numbers match ticket records
* backlog is accurate
* reassignment is reflected
* failed changes appear correctly
* vendor dependency is visible

## Acceptance Outcome

Management can trust the reporting enough to make operational decisions.

---

# 22. UAT Expected Results

UAT should validate outcomes rather than exact screen layout.

For example:

```text id="jw8po2"
Requirement:
Temporary access expires.

Acceptable Outcome:
Access is automatically disabled
OR
a controlled manual disablement action is created and owned.
```

This allows the implementation to remain vendor-neutral while still validating the business requirement.

---

# 23. UAT Feedback Categories

Tester feedback should be classified as:

| Type        | Meaning                                             |
| ----------- | --------------------------------------------------- |
| Defect      | Configured behavior does not meet requirement       |
| Usability   | Workflow works but creates unnecessary friction     |
| Process Gap | Business rule is unclear or incomplete              |
| Training    | Behavior is correct but misunderstood               |
| Data        | Incorrect or missing data                           |
| Enhancement | Useful future improvement                           |
| Preference  | Individual preference without clear business impact |

This classification prevents every piece of feedback from immediately becoming a system defect.

---

# 24. UAT Defect Severity

| Severity    | Example                                            |
| ----------- | -------------------------------------------------- |
| Critical    | Required workflow cannot complete or control fails |
| High        | Material process failure                           |
| Medium      | Significant inconvenience with workaround          |
| Low         | Minor usability issue                              |
| Enhancement | Outside approved requirement                       |

Critical UAT defects block acceptance.

High defects require remediation or explicit acceptance.

---

# 25. UAT Issue Triage

```text id="pn97f2"
UAT Feedback
    ↓
Classify
    ↓
Defect / Process / Training / Data / Enhancement
    ↓
Assign Owner
    ↓
Correct or Decide
    ↓
Retest if Required
```

The team should fix the right problem.

A training issue should not automatically produce another field or workflow rule.

---

# 26. UAT Retesting

Retesting is required when a change affects:

* workflow
* approval
* RBAC
* SLA
* automation
* data relationship
* reporting logic

The original UAT scenario should be rerun where applicable.

---

# 27. UAT Acceptance Criteria

UAT is acceptable when:

* all critical scenarios executed
* Must requirements represented
* no unresolved critical defects
* high defects resolved or formally accepted
* critical controls validated
* testers can complete core workflows
* process owners accept the result
* usability is sufficient for production
* unresolved enhancements are documented separately

---

# 28. UAT Sign-Off

Acceptance should include representatives from:

* process ownership
* operations
* business users
* security / governance where applicable

A simple sign-off record may capture:

| Field            | Value                         |
| ---------------- | ----------------------------- |
| UAT Cycle        | Release / Pilot               |
| Scope            | Tested processes              |
| Critical Defects | Open / Closed                 |
| High Defects     | Status                        |
| Accepted Risks   | References                    |
| Decision         | Accept / Conditional / Reject |
| Approvers        | Named Roles                   |
| Date             | Decision Date                 |

---

# 29. Conditional Acceptance

Conditional acceptance may be appropriate when:

* no critical control is affected
* workaround exists
* business impact is understood
* owner is assigned
* remediation is scheduled

Example:

```text id="6z82vb"
UAT Issue
   ↓
Not Critical
   ↓
Workaround Available
   ↓
Risk Accepted
   ↓
Conditional Acceptance
```

Conditional acceptance should remain visible through go-live readiness.

---

# 30. UAT Metrics

Useful UAT measures include:

| Metric               | Purpose                    |
| -------------------- | -------------------------- |
| Scenarios Executed   | Track coverage             |
| Pass Rate            | Measure initial acceptance |
| Critical Defects     | Measure release risk       |
| High Defects         | Measure workflow quality   |
| Retest Pass Rate     | Measure remediation        |
| Requirements Covered | Validate business scope    |
| Usability Issues     | Identify adoption friction |
| Training Issues      | Identify readiness gaps    |
| Enhancement Requests | Capture future backlog     |

UAT quality should not be judged only by pass percentage.

The type of failures matters more.

---

# 31. UAT Roles and Ownership

| Role             | Responsibility                |
| ---------------- | ----------------------------- |
| UAT Lead         | Plan and coordinate           |
| Business Analyst | Map scenarios to requirements |
| Tester           | Execute scenario              |
| Process Owner    | Resolve process questions     |
| Platform Team    | Correct defects               |
| Security / Risk  | Review control failures       |
| Project Lead     | Manage readiness impact       |
| Business Owner   | Approve acceptance            |

---

# 32. UAT Communication

Participants should receive:

* scope
* schedule
* role
* scenario instructions
* issue-reporting method
* support contact
* acceptance expectations

Testers should understand that the objective is to identify problems.

A UAT cycle with no feedback is not automatically a strong UAT cycle.

---

# 33. UAT Evidence

Representative evidence may include:

* ticket ID
* request ID
* approval record
* change record
* audit event
* screenshot
* report output
* tester comment

Evidence should support the acceptance decision without turning UAT into excessive documentation.

---

# 34. UAT Guardrails

## Do Not Turn UAT Into Training

Testers should receive enough orientation to participate, but UAT should still reveal whether the workflow is intuitive.

## Do Not Tell Testers Every Click

The business objective matters more than reproducing a demonstration.

## Do Not Treat Preferences as Defects Automatically

Ask whether the issue prevents or materially degrades the intended outcome.

## Do Not Hide Failed Controls Behind Usability Discussion

Control failures require direct remediation.

## Do Not Let Enhancements Block the Initial Release Without Reason

Future improvements belong in the backlog unless they expose a real requirement gap.

## Do Not Seek a Perfect Pass Rate

Seek enough evidence to understand whether the solution is ready.

---

# 35. UAT Success Criteria

The UAT model is complete when:

* representative users are identified
* realistic scenarios exist
* critical workflows are covered
* controls are included
* feedback classification is defined
* defect handling is defined
* retesting is planned
* acceptance authority is clear
* sign-off criteria are documented

---

# 36. UAT Plan Conclusion

User Acceptance Testing is the point where the design stops being theoretical.

The question is no longer whether the workflow looks correct in a diagram.

It is whether the people responsible for using it can:

* submit work
* own work
* approve work
* escalate work
* recover from failure
* trust the result

If they can do that without routinely leaving the platform to finish the process somewhere else, then the implementation is doing what it was designed to do.

**Next:** [Requirements Test Traceability](./requirements%20test%20traceability.md)
