# Phase Exit Criteria

## Purpose

This artifact defines the minimum conditions that should be met before the implementation moves from one phase to the next.

The objective is to prevent schedule pressure from becoming the only reason a phase is considered complete.

Each phase should produce evidence that the next phase has a stable enough foundation to begin.

The operating principle is:

> **A phase is complete when its decisions and deliverables are usable, not simply because the calendar moved forward.**

This artifact builds on:

* [Implementation Plan](./implementation%20plan.md)
* [Requirements Traceability Matrix](../02%20Requirements%20Discovery/requirements%20traceability%20matrix.md)
* [Control Matrix](../06%20Governance%20and%20Controls/control%20matrix.md)
* [Testing and UAT](../09%20Testing%20and%20UAT/test%20strategy.md)

---

# 1. Exit Criteria Model

Each implementation phase should be evaluated against five general conditions.

| Area         | Question                                               |
| ------------ | ------------------------------------------------------ |
| Deliverables | Were required artifacts completed?                     |
| Decisions    | Are critical business decisions resolved?              |
| Quality      | Are known defects or gaps within acceptable tolerance? |
| Ownership    | Is responsibility for the next phase clear?            |
| Risk         | Are unresolved risks understood and accepted?          |

A phase may still contain open issues.

The important distinction is whether those issues prevent the next phase from operating safely or effectively.

---

# 2. Exit Decision Status

Each phase may receive one of three outcomes.

| Status         | Meaning                                     |
| -------------- | ------------------------------------------- |
| Go             | Exit criteria satisfied                     |
| Conditional Go | Minor gaps remain with assigned remediation |
| No-Go          | Critical criteria not satisfied             |

A Conditional Go should include:

* open item
* owner
* due date
* impact
* required follow-up

Conditional Go should not be used to carry major unresolved design decisions indefinitely.

---

# 3. Phase 1 — Discovery Confirmation

## Required Exit Criteria

* current-state assessment reviewed
* stakeholder roles confirmed
* major failure modes validated
* baseline measures identified
* project scope confirmed
* out-of-scope boundaries documented
* primary process owners identified
* major assumptions recorded
* unresolved critical discovery conflicts addressed

## Exit Evidence

* approved current-state assessment
* stakeholder map
* pain-point register
* baseline metrics
* decision log
* scope statement

## No-Go Conditions

Examples include:

* major stakeholder group missing
* project scope still materially disputed
* no identified owner for core service processes
* current-state problem not sufficiently understood

---

# 4. Phase 2 — Requirements Validation

## Required Exit Criteria

* Must business requirements approved
* Must functional requirements defined
* applicable nonfunctional requirements validated
* workflow boundaries confirmed
* approval requirements defined
* SLA assumptions agreed
* ownership expectations defined
* RBAC requirements understood
* critical data requirements identified
* requirements are testable
* traceability matrix updated

## Exit Evidence

* requirements baseline
* prioritization record
* traceability matrix
* outstanding requirement decisions

## No-Go Conditions

Examples include:

* conflicting Must requirements
* approval authority undefined
* core workflow requirements not testable
* unresolved scope materially affects configuration

---

# 5. Phase 3 — Core Configuration

## Required Exit Criteria

Core platform configuration should support complete testable workflow paths.

### Platform Foundation

* users available
* roles configured
* support groups configured
* service records available
* reference values configured

### Incident

* intake
* priority
* assignment
* SLA
* escalation
* resolution
* closure

### Service Request

* catalog items
* approvals
* tasks
* ownership
* fulfillment
* closure

### Change

* change types
* risk
* approval
* scheduling
* implementation
* validation
* failure path

### Knowledge

* draft
* review
* publication
* ownership
* retirement

## Additional Exit Criteria

* core RBAC configured
* required audit behavior enabled
* Phase 1 automation configured
* configuration documentation current
* major build defects resolved

## Exit Evidence

* configured development / test environment
* configuration register
* workflow demonstrations
* initial test results

## No-Go Conditions

* required workflow cannot complete end to end
* critical approval control bypass exists
* ownership can be lost during workflow
* critical role permissions are incorrect

---

# 6. Phase 4 — Data Preparation

## Required Exit Criteria

* active users validated
* support groups validated
* service ownership confirmed
* catalog data prepared
* required CI scope prepared
* active vendor records reviewed
* reference data cleaned
* obsolete values retired
* migration scope approved
* historical-data handling decided
* data owners identified

## Exit Evidence

* migration inventory
* data validation report
* approved source-to-target mapping
* rejected / excluded-data list
* data-owner confirmation

## No-Go Conditions

* active users cannot be reliably identified
* support-group structure remains invalid
* required services lack owners
* data cannot support routing or approval logic
* migration approach risks corrupting target data

---

# 7. Phase 5 — Pilot

## Required Exit Criteria

* pilot users trained
* pilot support groups available
* selected workflows operational
* pilot service catalog active
* routing tested with real use
* SLA behavior validated
* approval paths exercised
* closure behavior validated
* pilot feedback captured
* critical pilot issues remediated
* pilot success measures reviewed

## Exit Evidence

* pilot results
* issue log
* configuration corrections
* user feedback
* technician feedback
* updated test cases

## No-Go Conditions

* routing remains unreliable
* approval failures are common
* critical workflow states behave incorrectly
* ownership is frequently lost
* pilot users cannot complete basic processes

---

# 8. Phase 6 — User Acceptance Testing

## Required Exit Criteria

* all Must requirements tested
* critical controls tested
* positive and negative scenarios completed
* no open critical defects
* high defects accepted or remediated
* required integrations validated
* data relationships validated
* RBAC behavior validated
* test evidence captured
* business acceptance obtained

## Exit Evidence

* test execution results
* defect log
* acceptance sign-off
* requirement-test traceability
* unresolved defect acceptance

## No-Go Conditions

* critical business process fails
* unauthorized access is possible
* self-approval control fails
* SLA logic is materially incorrect
* vendor expiration control fails without compensating control
* change failure path cannot be executed

---

# 9. Phase 7 — Training and Readiness

## Required Exit Criteria

* role-based training delivered
* support procedures available
* user communication prepared
* quick-reference material available
* support teams understand escalation
* production roles validated
* cutover responsibilities assigned
* hypercare team identified
* business readiness confirmed

## Exit Evidence

* training records
* support documentation
* communications
* readiness checklist
* support roster

## No-Go Conditions

* Service Desk not trained
* approvers do not understand new responsibilities
* production support owner undefined
* cutover roles unclear
* critical user communications missing

---

# 10. Phase 8 — Go-Live Readiness Gate

This is the strongest implementation gate.

## Required Exit Criteria

### Requirements

* Must requirements accepted
* critical scope complete

### Testing

* no unresolved critical defect
* accepted high defects documented
* production configuration matches tested configuration

### Data

* production data validated
* users and groups confirmed
* service ownership valid

### Controls

* RBAC active
* required approvals active
* self-approval restrictions active
* audit logging active
* critical access expiration controls active

### Operations

* Service Desk ready
* specialist support ready
* escalation path confirmed
* hypercare coverage scheduled

### Technology

* production environment ready
* required integrations operational
* monitoring active
* rollback / recovery path available

### Change and Communication

* production change authorized
* cutover schedule approved
* communication ready

---

# 11. Go-Live Decision Matrix

| Area         | Green               | Yellow                   | Red                          |
| ------------ | ------------------- | ------------------------ | ---------------------------- |
| Requirements | Must scope complete | Minor deferral           | Critical requirement missing |
| Testing      | No critical defects | Accepted high defect     | Critical defect              |
| Data         | Validated           | Minor correction pending | Core data unreliable         |
| Controls     | Operating           | Compensating control     | Critical control absent      |
| Training     | Complete            | Limited follow-up        | Core support not ready       |
| Integration  | Stable              | Manual fallback          | Required path unavailable    |
| Operations   | Staffed             | Minor coverage gap       | No support ownership         |

A single Red item in a critical area should normally result in No-Go.

---

# 12. Phase 8 — Go-Live Exit

Go-live itself should also have an exit condition before moving into normal Hypercare.

## Required Conditions

* production workflows enabled
* intake channels functioning
* routing operating
* approvals functioning
* no immediate critical control failure
* support teams receiving work
* monitoring collecting expected data
* production issues being captured

Go-live is not complete simply because the platform became available.

---

# 13. Phase 9 — Hypercare Exit

## Required Exit Criteria

* no open critical implementation defects
* issue volume is declining
* routing accuracy stable
* SLA calculations stable
* approval paths stable
* critical integrations stable
* data-quality exceptions manageable
* support teams resolving normal issues independently
* governance exceptions assigned
* platform ownership transferred to normal operations

## Exit Evidence

* hypercare issue trend
* defect status
* support handoff
* production metric review
* known-issue backlog
* operational acceptance

## No-Go Conditions

Hypercare should continue if:

* critical defects remain
* implementation team is still required for routine work
* major integrations are unstable
* access controls are unreliable
* workflow failure rate remains materially high

---

# 14. Phase 10 — Optimization Entry

Optimization begins when production performance is stable enough to distinguish real improvement opportunities from implementation defects.

## Entry Criteria

* baseline production metrics available
* core workflows stable
* support ownership established
* major defects resolved
* data quality sufficient for analysis
* improvement backlog exists
* optimization governance defined

At this point the organization can begin improving the model based on evidence.

---

# 15. Deferred Items

Not every requirement or improvement needs to block phase exit.

A deferred item should include:

| Field               | Requirement             |
| ------------------- | ----------------------- |
| Item                | What is deferred        |
| Reason              | Why                     |
| Impact              | Operational consequence |
| Risk                | Exposure created        |
| Owner               | Accountability          |
| Target Phase        | When addressed          |
| Compensating Action | Interim handling        |

A deferred item without ownership is simply unfinished work.

---

# 16. Defect Acceptance

A known defect may be accepted where:

* business impact is understood
* workaround exists
* risk is acceptable
* owner is assigned
* remediation target exists

Example:

```text id="9f4te3"
Defect Found
    ↓
Critical?
 ↙         ↘
Yes         No
 ↓           ↓
Fix        Assess Risk
            ↓
       Accept / Fix / Defer
```

Defect acceptance should be a decision, not the absence of a fix.

---

# 17. Compensating Controls at Exit

A phase may proceed with a compensating control where the preferred control is unavailable.

Example:

```text id="hp32fk"
Automatic Vendor Revocation
        ↓
Not Available
        ↓
Manual Disablement Task
        ↓
Assigned Owner + Monitoring
```

The compensating control should be:

* documented
* tested
* owned
* monitored
* temporary where possible

---

# 18. Exit Criteria Ownership

| Phase            | Primary Exit Authority            |
| ---------------- | --------------------------------- |
| Discovery        | Project Lead / Process Owners     |
| Requirements     | Business / Process Owners         |
| Configuration    | Platform Lead + Process Owners    |
| Data Preparation | Data Owners / Implementation Lead |
| Pilot            | Project Lead + Pilot Stakeholders |
| UAT              | Business Owners / Test Lead       |
| Training         | Adoption Lead / Operations        |
| Go-Live          | Sponsor / Project Governance      |
| Hypercare        | Operations + Implementation Lead  |
| Optimization     | Service / Process Governance      |

No single technical role should declare the entire implementation ready independently.

---

# 19. Exit Review

Each phase review should answer:

* What was supposed to be completed?
* What evidence shows it is complete?
* What remains open?
* Does the open work block the next phase?
* Who owns unresolved items?
* What risk is being carried forward?

The review should be short enough to use consistently.

---

# 20. Phase Exit Register

A simple implementation register may use:

| Phase         | Status      | Critical Gaps   | Owner            | Decision |
| ------------- | ----------- | --------------- | ---------------- | -------- |
| Discovery     | Complete    | None            | Project Lead     | Go       |
| Requirements  | Complete    | None            | Business Analyst | Go       |
| Configuration | In Progress | RBAC validation | Platform Lead    | Pending  |
| Data          | In Progress | Vendor cleanup  | Data Owner       | Pending  |
| Pilot         | Not Started | —               | Pilot Lead       | —        |

This provides management-level visibility without replacing detailed project tracking.

---

# 21. Traceability at Phase Exit

Phase completion should preserve the repository traceability model.

Example:

```text id="1vzt7n"
BR-07
  ↓
FR-16
  ↓
Self-Approval Control
  ↓
Configured
  ↓
TC-RBAC-05
  ↓
Passed
```

The implementation should be able to demonstrate that required outcomes survived the transition from design to configuration.

---

# 22. Exit Criteria and Scope Change

If a required criterion cannot be met because the underlying scope has changed, the team should not simply waive the criterion.

The change should be handled as:

```text id="1pbeqm"
Exit Criterion Fails
      ↓
Underlying Requirement Changed?
   ↙                       ↘
 Yes                       No
 ↓                          ↓
Scope / Requirement       Remediate
Change Control
```

This preserves the integrity of the implementation baseline.

---

# 23. Exit Criteria Guardrails

## Do Not Mark a Phase Complete Because Activity Stopped

Completion requires usable output.

## Do Not Carry Critical Design Questions Into Build

Configuration is an expensive place to continue requirements discovery.

## Do Not Use Conditional Go for Everything

If every phase exits conditionally, the implementation is simply accumulating debt.

## Do Not Let Go-Live Date Override Control Failure

A known critical access or workflow defect is more important than maintaining an arbitrary date.

## Do Not Require Perfection

Minor defects and improvements can be handled after release when risk is understood.

## Do Not Lose Deferred Items

Every accepted gap needs ownership and a future decision point.

---

# 24. Phase Exit Success Criteria

The phase-gate model is effective when:

* every phase has measurable completion criteria
* exit authority is defined
* evidence exists
* critical defects block progression
* minor gaps can be managed intentionally
* deferred work remains owned
* risks carried forward are visible
* go-live is based on readiness rather than schedule alone

---

# 25. Phase Exit Criteria Conclusion

The implementation plan defines what the team intends to do.

The exit criteria define when the team has done enough of it to move forward responsibly.

That distinction matters.

A project can be busy, on schedule, and still not be ready.

The purpose of these gates is to catch that before an unfinished decision becomes a production problem.

The model is intentionally practical:

**finish the critical work, prove that it works, document what remains, assign the risk, and then move forward.**

**Next:** [Migration and Cutover](./migration%20and%20cutover.md)
