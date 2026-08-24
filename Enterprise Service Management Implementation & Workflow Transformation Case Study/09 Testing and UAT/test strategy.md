# Test Strategy

## Purpose

This artifact defines how the target Enterprise Service Management environment will be validated before production release.

Testing should confirm more than whether screens load or workflow buttons work.

It should determine whether the configured environment supports the business requirements, enforces the intended controls, handles exceptions correctly, and remains usable under realistic operating conditions.

The operating principle is:

> **Test the process the way people will actually use it, including the ways it can fail.**

This strategy builds on:

* [Requirements Traceability Matrix](../02%20Requirements%20Discovery/requirements%20traceability%20matrix.md)
* [Control Matrix](../06%20Governance%20and%20Controls/control%20matrix.md)
* [Implementation Plan](../08%20Implementation%20Plan/implementation%20plan.md)
* [Phase Exit Criteria](../08%20Implementation%20Plan/phase%20exit%20criteria.md)

---

# 1. Test Objectives

Testing should validate that:

* business requirements are implemented
* workflow paths operate end to end
* ownership remains visible
* approvals enforce authority boundaries
* RBAC limits inappropriate access
* SLA behavior matches design
* automation operates predictably
* exceptions fail visibly
* data relationships remain valid
* migration results are usable
* reporting reflects actual workflow behavior
* AI-assisted capabilities remain advisory where required
* users can perform realistic tasks without unnecessary friction

The objective is confidence in the operating model.

Not simply confidence that the platform is technically available.

---

# 2. Test Scope

The initial test scope includes:

* Incident Management
* Service Request Management
* Change Management
* Knowledge Management
* Service Catalog
* Priority and SLA
* Ownership and Escalation
* RBAC
* Approvals
* Data Relationships
* Vendor Access
* Automation
* AI-Assisted Functions
* Reporting
* Migration
* Cutover Readiness

Testing should prioritize the paths most likely to affect:

* service continuity
* access
* authorization
* ownership
* auditability

---

# 3. Test Levels

The strategy uses five primary levels.

| Level                   | Purpose                                         |
| ----------------------- | ----------------------------------------------- |
| Configuration Testing   | Verify individual configuration components      |
| Integration Testing     | Validate interaction between systems or modules |
| End-to-End Testing      | Validate complete business workflows            |
| Control Testing         | Validate governance and security controls       |
| User Acceptance Testing | Validate business usability and outcomes        |

These levels may overlap.

The important distinction is what question each level is trying to answer.

---

# 4. Configuration Testing

Configuration testing validates individual platform components.

Examples include:

* form fields
* required values
* state transitions
* assignment rules
* SLA timers
* notification rules
* approval routing
* reference values

Example:

```text
Impact = High
Urgency = High
      ↓
Expected Priority = P1
```

Configuration testing should happen before business users are asked to validate complete workflows.

---

# 5. Integration Testing

Integration testing validates connections between the ESM platform and external systems.

Potential integrations include:

* identity
* email
* asset management
* configuration discovery
* software deployment
* access provisioning
* vendor systems

Testing should verify both:

```text
Successful Integration
```

and:

```text
Integration Failure
      ↓
Visible Exception
      ↓
Manual Recovery
```

A successful API response is not enough if the intended business outcome does not occur.

---

# 6. End-to-End Testing

End-to-end testing validates complete operating scenarios.

Example:

```text
Incident Submitted
      ↓
Prioritized
      ↓
Routed
      ↓
Assigned
      ↓
SLA Monitored
      ↓
Resolved
      ↓
Closed
```

The test should confirm:

* workflow state
* ownership
* notifications
* SLA
* record history
* closure requirements

at each relevant stage.

---

# 7. Control Testing

Control testing validates whether governance rules actually operate.

Examples include:

* self-approval blocked
* unauthorized user denied access
* vendor access expires
* priority override requires authority
* SLA exception requires reason
* high-risk change cannot bypass approval
* closure blocked without required evidence
* production configuration change is logged

Controls should be tested as operating behavior.

Not just verified by looking at configuration settings.

---

# 8. Positive Testing

Positive testing confirms approved activity succeeds.

Example:

```text
Authorized Approver
      ↓
Approves Request
      ↓
Approval Recorded
      ↓
Fulfillment Continues
```

Positive tests answer:

> Can the system perform the intended process?

---

# 9. Negative Testing

Negative testing confirms prohibited or invalid behavior fails safely.

Example:

```text
Requester
   ↓
Attempts Self-Approval
   ↓
Blocked
   ↓
Attempt Logged
```

Negative testing is especially important for:

* RBAC
* approval
* change control
* vendor access
* automation
* AI governance

A control has not been meaningfully validated if only the approved path was tested.

---

# 10. Exception Testing

Exception testing validates what happens when normal assumptions fail.

Examples include:

* routing destination missing
* approver inactive
* integration unavailable
* automation fails
* vendor access cannot be revoked automatically
* required CI unavailable
* approval expires
* AI service unavailable

The expected result should be:

```text
Failure
  ↓
Visible Exception
  ↓
Assigned Owner
  ↓
Recovery Path
```

Silent failure should be treated as a defect.

---

# 11. Role-Based Testing

Test execution should include the perspectives of actual operational roles.

| Role                   | Example Validation                      |
| ---------------------- | --------------------------------------- |
| Requester              | Intake and status visibility            |
| Service Desk           | Triage, assignment, closure             |
| Specialist Resolver    | Technical workflow and CI relationships |
| Group Lead             | Escalation and queue control            |
| Approver               | Authorization workflow                  |
| Service Owner          | SLA and service decisions               |
| Change Authority       | Change approval                         |
| Platform Administrator | Controlled administration               |
| Auditor                | Evidence visibility                     |
| Vendor User            | Restricted external access              |

Testing with only administrative accounts can hide permission problems.

---

# 12. Incident Test Coverage

Incident testing should include:

* normal incident
* P1 incident
* duplicate incident
* reassignment
* vendor dependency
* waiting on requester
* SLA warning
* SLA breach
* resolution
* reopen
* incident related to failed change

Representative IDs include:

* TC-INC-01 through TC-INC-05
* TC-SLA-01 through TC-SLA-05
* TC-CLS-01

---

# 13. Service Request Test Coverage

Service Request testing should include:

* A0 request
* A1 request
* A2 controlled request
* rejected request
* delayed approval
* multi-task fulfillment
* vendor access
* temporary access
* automation success
* automation failure

Representative IDs include:

* TC-REQ-01 through TC-REQ-06
* TC-VND-02
* TC-AUT-01
* TC-AUT-02

---

# 14. Change Test Coverage

Change testing should include:

* Standard Change
* Normal Change
* high-risk approval
* incomplete readiness
* successful implementation
* failed implementation
* backout
* incident linkage
* Emergency Change
* Standard Change outside approved scope
* vendor-implemented change

Representative IDs include:

* TC-CHG-01 through TC-CHG-10

---

# 15. Knowledge Test Coverage

Knowledge testing should include:

* draft creation
* review
* publication
* audience restriction
* ticket relationship
* stale-content review
* retirement
* prohibited unapproved publication

Representative IDs include:

* TC-KNW-01 through TC-KNW-06

---

# 16. Data and Relationship Testing

Testing should validate:

* required relationships
* valid reference data
* inactive-reference restrictions
* ownership
* historical preservation
* vendor relationships
* approval parent relationships
* temporary access expiration

Representative IDs include:

* TC-DAT-01 through TC-DAT-09
* TC-REL-01 through TC-REL-09
* TC-DG-01 through TC-DG-07

---

# 17. RBAC and Governance Testing

Testing should validate:

* role permissions
* sensitive-record restrictions
* self-approval prevention
* delegated approval
* privileged access
* vendor restrictions
* priority override
* SLA exception
* platform administration
* access revocation

Representative IDs include:

* TC-RBAC-01 through TC-RBAC-10
* TC-GOV-01 through TC-GOV-10
* TC-CTL-01 through TC-CTL-10

---

# 18. Automation Testing

Automation testing should cover:

* expected trigger
* valid inputs
* invalid inputs
* missing data
* duplicate execution
* downstream failure
* permissions failure
* manual fallback
* execution logging

Representative IDs include:

* TC-AUT-01 through TC-AUT-10

Automation testing should confirm both:

```text
Rule Works
```

and:

```text
Rule Fails Predictably
```

---

# 19. AI-Assisted Testing

AI testing should focus on workflow behavior around the AI capability.

Test scenarios should include:

* useful recommendation
* incorrect recommendation
* low confidence
* restricted data
* rejected recommendation
* AI outage
* stale knowledge
* material configuration change

Representative IDs include:

* TC-AI-01 through TC-AI-10
* TC-AIG-01 through TC-AIG-10

The objective is not to prove AI always produces the correct answer.

It is to prove the process remains controlled when it does not.

---

# 20. Migration Testing

Migration testing should validate:

* extract completeness
* transformation
* load
* relationships
* ownership
* record counts
* excluded data
* exception handling
* historical visibility

Representative tests should include:

```text
Source Record
    ↓
Transform
    ↓
Target Record
    ↓
Reconcile
```

Migration should be rehearsed before production cutover.

---

# 21. Reporting Testing

Reporting should be tested against known underlying records.

Examples include:

* SLA compliance
* backlog
* reassignment
* approval aging
* failed change
* vendor dependency
* access expiration
* control exceptions

A dashboard should not be accepted simply because it renders successfully.

Its calculations need to reconcile to the source records.

---

# 22. Test Data

Test data should represent realistic business conditions without relying unnecessarily on production-sensitive information.

Required test data may include:

* standard users
* manager relationships
* support groups
* services
* assets
* CIs
* vendors
* approvers
* knowledge
* access types

Test personas should support both valid and invalid scenarios.

---

# 23. Test Environment

Testing should occur in an environment that represents production behavior closely enough to validate:

* workflows
* roles
* integrations
* notifications
* data relationships
* automation

Known environment differences should be documented.

A test environment that behaves materially differently from production reduces UAT value.

---

# 24. Test Preconditions

Each test case should identify relevant preconditions.

Examples:

* user exists
* role assigned
* service active
* support group active
* approval relationship configured
* vendor active
* CI available
* automation enabled

This makes test results repeatable.

---

# 25. Test Case Structure

Each formal test case should include:

| Field           | Purpose                            |
| --------------- | ---------------------------------- |
| Test ID         | Unique reference                   |
| Requirement     | Traceability                       |
| Scenario        | Business condition                 |
| Preconditions   | Required setup                     |
| Steps           | Execution                          |
| Expected Result | Intended behavior                  |
| Actual Result   | Observed behavior                  |
| Status          | Pass / Fail / Blocked              |
| Evidence        | Supporting record                  |
| Defect ID       | Failure reference where applicable |

Detailed cases will be maintained in:

[Test Cases](./test%20cases.md)

---

# 26. Test Status

The standard test status model is:

| Status           | Meaning                                           |
| ---------------- | ------------------------------------------------- |
| Not Run          | Test not executed                                 |
| Pass             | Expected result achieved                          |
| Fail             | Expected result not achieved                      |
| Blocked          | Test cannot execute due to dependency             |
| Conditional Pass | Minor issue exists but primary objective achieved |

Conditional Pass should be used sparingly.

A failed control should not be hidden behind a conditional status.

---

# 27. Defect Severity

| Severity    | Definition                                                    |
| ----------- | ------------------------------------------------------------- |
| Critical    | Prevents required service or creates material control failure |
| High        | Major workflow or business requirement failure                |
| Medium      | Meaningful issue with workaround                              |
| Low         | Minor usability or cosmetic issue                             |
| Enhancement | Desired behavior outside approved requirement                 |

Severity should reflect business impact.

Not how difficult the defect is to fix.

---

# 28. Defect Workflow

```text
Defect Identified
      ↓
Classify
      ↓
Assign
      ↓
Correct
      ↓
Retest
      ↓
Close / Defer
```

A failed test remains failed until:

* the defect is corrected and retested
* or the risk is formally accepted

---

# 29. Regression Testing

Changes made during:

* configuration
* pilot
* UAT
* defect remediation

may affect previously validated workflows.

Regression testing should focus on:

* shared workflows
* routing
* RBAC
* approvals
* SLA
* automation
* integrations

The scope should match the impact of the change.

---

# 30. Requirement Coverage

Testing should demonstrate coverage of approved requirements.

Example:

```text
BR-07
  ↓
FR-16
  ↓
AC-02 Self-Approval Prevention
  ↓
TC-RBAC-05
  ↓
Pass
```

Requirements without tests should be treated as traceability gaps.

---

# 31. Control Coverage

Critical controls should have at least one validation method.

Where appropriate they should include both:

* positive test
* negative test

Example:

```text
AC-02
├── Authorized Approval → Pass
└── Self-Approval Attempt → Blocked
```

This provides stronger evidence that the control actually distinguishes permitted from prohibited behavior.

---

# 32. Risk-Based Test Priority

Testing should prioritize the areas where failure creates the greatest impact.

## Priority 1

* RBAC
* privileged access
* approval separation
* Incident workflow
* P1 behavior
* SLA
* vendor expiration
* high-risk change
* audit logging

## Priority 2

* Service Requests
* Knowledge
* data-quality controls
* reporting
* standard automation

## Priority 3

* optimization
* lower-risk AI assistance
* secondary reports
* usability enhancements

Every approved Must requirement should still receive validation.

---

# 33. Entry Criteria

Formal testing should begin when:

* configuration is stable enough to test
* requirements baseline exists
* test environment available
* required test data exists
* major integrations available or simulated
* roles configured
* critical dependencies identified

Testing too early can create noise from unfinished configuration.

Testing too late removes time to correct meaningful defects.

---

# 34. Exit Criteria

Testing is complete enough for production progression when:

* Must requirements tested
* critical controls passed
* no unresolved critical defects
* high defects resolved or formally accepted
* end-to-end workflows passed
* RBAC passed
* required integrations passed
* migration validation completed
* business acceptance criteria met
* test evidence retained

These criteria feed:

[Phase Exit Criteria](../08%20Implementation%20Plan/phase%20exit%20criteria.md)

---

# 35. Test Evidence

Evidence may include:

* service record ID
* approval record
* audit event
* screenshot
* log entry
* report result
* migration reconciliation
* configuration record

Evidence should be sufficient to demonstrate the expected outcome.

It does not need to become excessive documentation for every trivial test.

---

# 36. Test Ownership

| Role              | Responsibility                     |
| ----------------- | ---------------------------------- |
| Test Lead         | Coordinates overall testing        |
| Business Analyst  | Maintains requirement traceability |
| Platform Team     | Performs configuration testing     |
| Integration Owner | Performs integration testing       |
| Process Owner     | Validates workflow behavior        |
| Security / Risk   | Validates critical controls        |
| Data Owner        | Validates migrated data            |
| Business User     | Performs UAT                       |
| Project Lead      | Tracks readiness and defects       |

The person who configured a feature may help test it.

They should not be the only person deciding whether the business requirement has been satisfied.

---

# 37. Test Reporting

Testing status should summarize:

* tests planned
* tests executed
* pass rate
* failed tests
* blocked tests
* critical defects
* high defects
* requirement coverage
* control coverage

The purpose is readiness visibility.

Not generating a large testing dashboard for its own sake.

---

# 38. Daily Test Triage

During active test cycles, the team should review:

* new critical defects
* blocked scenarios
* environment problems
* repeated failure patterns
* fixes requiring regression
* decisions required from process owners

This keeps defects from aging without ownership.

---

# 39. Test Strategy Guardrails

## Do Not Test Only the Happy Path

Controls and exceptions require negative testing.

## Do Not Let Configuration Teams Be the Only Testers

Users who own the business process need to validate the outcome.

## Do Not Treat a Demo as UAT

Watching someone execute the workflow is not the same as performing it.

## Do Not Ignore Data

Correct workflow behavior with bad ownership or relationships is still a failed implementation.

## Do Not Accept Reports Without Reconciliation

A polished dashboard can still calculate the wrong thing.

## Do Not Test AI as if It Were Deterministic Automation

Test the controls around uncertainty and error.

## Do Not Chase Perfect Pass Rates by Reclassifying Failures

A test result should reflect what happened.

---

# 40. Test Strategy Success Criteria

The testing approach is ready when:

* scope is defined
* test levels are defined
* positive and negative testing are included
* exception paths are covered
* role-based testing is planned
* requirements map to tests
* critical controls map to tests
* test data is available
* environments are ready
* defect handling is defined
* entry and exit criteria are understood
* business participation is assigned

---

# 41. Test Strategy Conclusion

The testing model is designed to prove that the target service-management environment works as an operating system for service delivery, not just as configured software.

The important questions are practical:

* Does work reach the right owner?
* Does priority behave correctly?
* Do approvals actually control the action?
* Can someone bypass the workflow?
* Does a failure become visible?
* Can the organization recover?
* Does the data support the decision?
* Can users actually operate the process?

If the test strategy can answer those questions with evidence, then the implementation has something meaningful to take into UAT and ultimately into production.

**Next:** [Test Cases](./test%20cases.md)
