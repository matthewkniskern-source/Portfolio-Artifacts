# Control Matrix

## Purpose

The Control Matrix consolidates the primary governance, access, workflow, data, approval, automation, and audit controls defined across the Enterprise Service Management case study.

This artifact is intended to answer a practical question:

> **What can fail, what control addresses it, who owns that control, and how do we know the control is actually working?**

The matrix is not intended to duplicate every workflow rule in the repository.

It provides a single control view that ties together:

* risk
* control objective
* control type
* implementation point
* ownership
* evidence
* testing
* monitoring

This artifact builds on:

* [Governance Model](./governance%20model.md)
* [RBAC and Approval Controls](./rbac%20and%20approval%20controls.md)
* [Data Governance](../05%20Data%20and%20Configuration%20Model/data%20governance.md)
* [Requirements Traceability Matrix](../02%20Requirements%20Discovery/requirements%20traceability%20matrix.md)

---

# 1. Control Categories

Controls are classified as:

| Type         | Purpose                                                              |
| ------------ | -------------------------------------------------------------------- |
| Preventive   | Stop an invalid or unauthorized condition                            |
| Detective    | Identify a control failure or exception                              |
| Corrective   | Restore the expected condition                                       |
| Compensating | Reduce risk where the preferred control is not technically available |

The target model uses preventive controls where the system can enforce the rule reliably.

Detective and corrective controls remain necessary because not every failure can or should be blocked automatically.

---

# 2. Control Domains

The matrix groups controls into seven domains.

| Domain                     | Scope                                                      |
| -------------------------- | ---------------------------------------------------------- |
| Access and Approval        | RBAC, privileged access, self-approval, approval authority |
| Workflow Integrity         | Ownership, routing, closure, escalation                    |
| Change and Configuration   | Change authorization, readiness, production configuration  |
| Data Governance            | Ownership, stale data, reference integrity                 |
| Vendor and External Access | Sponsorship, expiration, accountability                    |
| Automation and AI          | Rule ownership, logging, exception handling, human review  |
| Audit and Monitoring       | Evidence, review, reporting, remediation                   |

---

# 3. Master Control Matrix

| ID     | Control                               | Type                      | Risk Addressed                                 | Control Owner                     | Evidence                               | Test               |
| ------ | ------------------------------------- | ------------------------- | ---------------------------------------------- | --------------------------------- | -------------------------------------- | ------------------ |
| AC-01  | Role-based permission assignment      | Preventive                | Excessive or inappropriate access              | Security / Platform Governance    | Role configuration, membership records | TC-RBAC-01, 02, 03 |
| AC-02  | Self-approval prevention              | Preventive                | Unauthorized self-authorization                | Process / Access Owner            | Blocked transaction, audit event       | TC-RBAC-05         |
| AC-03  | Restricted privileged approval        | Preventive                | Unauthorized privileged access                 | Access / System Owner             | Approval record                        | TC-RBAC-04         |
| AC-04  | Time-bound vendor access              | Preventive                | Persistent external access                     | Security / Internal Sponsor       | Start/expiration data                  | TC-VND-02          |
| AC-05  | Approval history retention            | Detective                 | Loss of authorization evidence                 | Process Owner                     | Approval audit history                 | TC-RBAC-07         |
| AC-06  | Periodic privileged-role review       | Detective                 | Stale or excessive privilege                   | Security / IT Management          | Review record                          | TC-RBAC-09         |
| AC-07  | Priority override restriction         | Preventive                | Manipulated incident priority                  | Service Management Owner          | Override history                       | TC-GOV-05          |
| AC-08  | SLA exception restriction             | Preventive                | Manipulated service reporting                  | Service / Process Owner           | Exception record                       | TC-GOV-04          |
| AC-09  | Administrative change logging         | Detective                 | Untracked platform change                      | Platform Owner                    | Configuration history                  | TC-GOV-07          |
| AC-10  | Access revocation                     | Corrective                | Invalid retained privilege                     | Security / Identity               | Revocation record                      | TC-RBAC-10         |
| WF-01  | Required active ownership             | Preventive                | Unowned service records                        | Process Owner                     | Ticket owner field                     | TC-REL-02          |
| WF-02  | Controlled reassignment               | Preventive / Detective    | Reassignment loops and lost context            | Support Management                | Assignment history                     | TC-INC-04          |
| WF-03  | SLA escalation                        | Detective / Corrective    | Missed service commitment                      | Service Owner                     | Escalation history                     | TC-SLA-02          |
| WF-04  | Required closure data                 | Preventive                | Incomplete service records                     | Process Owner                     | Closure fields                         | TC-GOV-06          |
| WF-05  | Waiting-state governance              | Preventive                | Artificial SLA pause / hidden delay            | Process Owner                     | State history                          | TC-SLA-01          |
| WF-06  | Duplicate / related incident linkage  | Detective                 | Fragmented incident history                    | Service Management Owner          | Parent/child relationships             | TC-INC-02          |
| WF-07  | Exception ownership                   | Corrective                | Unresolved workflow exceptions                 | Process Owner                     | Exception queue                        | TC-GOV-10          |
| CHG-01 | Risk-based change approval            | Preventive                | Unauthorized or insufficiently reviewed change | Change Authority                  | Approval history                       | TC-CHG-02, 03      |
| CHG-02 | Implementation readiness gate         | Preventive                | Change proceeds without preparation            | Change Owner                      | Readiness checklist                    | TC-CHG-04          |
| CHG-03 | Backout requirement                   | Preventive / Corrective   | Failed change without recovery path            | Change Owner                      | Backout plan                           | TC-CHG-05          |
| CHG-04 | Post-change validation                | Detective                 | Change closed without confirming outcome       | Change Owner                      | Validation result                      | TC-CHG-10          |
| CHG-05 | Change-to-incident linkage            | Detective                 | Change-related failures hidden                 | Change / Incident Owner           | Linked records                         | TC-CHG-06          |
| CHG-06 | Emergency-change review               | Detective / Corrective    | Emergency process abuse                        | Change Authority                  | PIR record                             | TC-CHG-07          |
| CHG-07 | Standard-change boundary              | Preventive                | Unapproved work treated as standard            | Change Owner                      | Template / scope validation            | TC-CHG-08          |
| CHG-08 | Production configuration control      | Preventive                | Uncontrolled ESM platform change               | Platform Owner / Change Authority | Change record                          | TC-GOV-07          |
| DG-01  | Required data ownership               | Preventive                | Orphaned data domain                           | Data Owner                        | Ownership record                       | TC-DG-01           |
| DG-02  | Controlled reference values           | Preventive                | Inconsistent routing/reporting data            | Process / Data Owner              | Reference configuration                | TC-DG-02           |
| DG-03  | Inactive-reference restriction        | Preventive                | New work linked to invalid records             | Data Steward                      | Validation rule                        | TC-DAT-02          |
| DG-04  | Periodic stale-data review            | Detective                 | Stale service, CI, vendor, or knowledge data   | Data Owner                        | Review report                          | TC-DG-06           |
| DG-05  | Historical relationship preservation  | Detective                 | Loss of operational history                    | Data / Platform Owner             | Record history                         | TC-DG-05           |
| DG-06  | Data-quality exception reporting      | Detective                 | Silent integrity failures                      | Data Owner                        | DQ exception report                    | TC-DG-06           |
| DG-07  | Correction workflow                   | Corrective                | Known data error remains unresolved            | Data Steward                      | Correction record                      | TC-DG-06           |
| VND-01 | Internal vendor sponsor               | Preventive                | External activity without accountability       | Service / Vendor Owner            | Sponsor field                          | TC-DAT-05          |
| VND-02 | Vendor access approval                | Preventive                | Unauthorized external access                   | Access Authority                  | Approval record                        | TC-RBAC-04         |
| VND-03 | Vendor-access expiration              | Preventive                | External access persists indefinitely          | Security / Identity               | Expiration / disablement evidence      | TC-VND-02          |
| VND-04 | Manual disablement exception          | Compensating / Corrective | Integration cannot revoke access automatically | Internal Sponsor                  | Assigned disablement task              | TC-GOV-03          |
| VND-05 | Vendor activity traceability          | Detective                 | External action is invisible                   | Service Owner                     | Vendor case/activity history           | TC-DAT-05          |
| AUT-01 | Automation rule ownership             | Preventive                | Unowned or undocumented automation             | Process Owner                     | Rule owner / documentation             | TC-AUT-01          |
| AUT-02 | Automation execution logging          | Detective                 | Automated actions cannot be reconstructed      | Platform Owner                    | Execution log                          | TC-AUT-01          |
| AUT-03 | Automation failure exception          | Corrective                | Silent automation failure                      | Platform / Process Owner          | Exception record                       | TC-AUT-02          |
| AUT-04 | Automation change control             | Preventive                | Untested production rule change                | Platform Owner                    | Change record / UAT                    | TC-GOV-07          |
| AI-01  | Human review for controlled decisions | Preventive                | AI independently authorizes sensitive action   | Process / Security Owner          | Review / decision record               | TC-AI-01           |
| AI-02  | AI action attribution                 | Detective                 | AI-assisted action lacks provenance            | Platform Owner                    | Attribution metadata                   | TC-AI-02           |
| AI-03  | Restricted autonomous actions         | Preventive                | AI bypasses governance control                 | Security / Platform Governance    | Permission / configuration evidence    | TC-AI-03           |
| AI-04  | AI feedback and correction            | Corrective                | Poor recommendations persist                   | Process Owner                     | Feedback history                       | TC-AI-04           |
| AUD-01 | Material-action audit logging         | Detective                 | Significant actions cannot be reconstructed    | Platform / Security               | Audit log                              | TC-GOV-05          |
| AUD-02 | Audit review                          | Detective                 | Logged exceptions never reviewed               | Security / Process Owner          | Review record                          | TC-GOV-10          |
| AUD-03 | Control failure escalation            | Corrective                | Known control failure remains unresolved       | Control Owner                     | Incident / exception record            | TC-GOV-10          |
| AUD-04 | Exception aging                       | Detective                 | Temporary exception becomes permanent          | Governance Owner                  | Exception-aging report                 | TC-GOV-10          |

---

# 4. Control-to-Failure Mapping

The controls directly address current-state failure modes identified earlier in the case study.

| Failure Mode                             | Primary Controls      |
| ---------------------------------------- | --------------------- |
| FM-01 Work outside managed record        | WF-01, AUD-01         |
| FM-02 Duplicate work                     | WF-06                 |
| FM-03 Subjective priority                | AC-07                 |
| FM-04 Reassignment loops                 | WF-02                 |
| FM-05 Manual escalation                  | WF-03                 |
| FM-06 Approval outside record            | AC-05                 |
| FM-07 Self-approval / bypass             | AC-02, AC-03          |
| FM-08 Missing asset / CI context         | DG-02, DG-03          |
| FM-09 Knowledge trapped with individuals | DG-01, DG-04          |
| FM-10 Failed change unlinked to incident | CHG-05                |
| FM-11 Hidden vendor activity             | VND-01, VND-05        |
| FM-12 Persistent vendor access           | AC-04, VND-03, VND-04 |
| FM-13 Weak closure                       | WF-04                 |
| FM-14 Recurring issues hidden            | WF-06, DG-06          |
| FM-15 Incomplete reporting               | DG-02, DG-06, AUD-01  |
| FM-16 Automation of poor decisions       | AUT-01, AUT-04, AI-01 |

This maintains the traceability path:

```text id="9oyd7v"
Failure Mode
    ↓
Requirement
    ↓
Design
    ↓
Control
    ↓
Test
    ↓
Metric
```

---

# 5. Preventive Control View

The most important preventive controls include:

| Control | Prevention Objective                   |
| ------- | -------------------------------------- |
| AC-01   | Prevent excessive permissions          |
| AC-02   | Prevent self-approval                  |
| AC-03   | Prevent unauthorized privilege         |
| AC-04   | Prevent indefinite vendor access       |
| AC-07   | Prevent uncontrolled priority override |
| AC-08   | Prevent unauthorized SLA exclusion     |
| WF-01   | Prevent unowned active work            |
| WF-04   | Prevent incomplete closure             |
| CHG-01  | Prevent unauthorized change            |
| CHG-02  | Prevent unready implementation         |
| DG-03   | Prevent invalid data relationships     |
| AUT-04  | Prevent uncontrolled automation change |
| AI-03   | Prevent autonomous sensitive action    |

Preventive controls should be used where the rule can be stated clearly and enforced consistently.

---

# 6. Detective Control View

Representative detective controls include:

| Control | Detection Objective                       |
| ------- | ----------------------------------------- |
| AC-05   | Preserve approval evidence                |
| AC-06   | Identify stale privileged access          |
| WF-03   | Detect approaching or breached SLA        |
| CHG-04  | Detect unsuccessful implementation        |
| CHG-05  | Identify change-related incidents         |
| CHG-06  | Detect emergency-change misuse            |
| DG-04   | Identify stale data                       |
| DG-06   | Identify relationship-quality failures    |
| VND-05  | Identify hidden external activity         |
| AUT-02  | Preserve automation execution evidence    |
| AUD-01  | Preserve material action history          |
| AUD-02  | Identify actionable governance exceptions |
| AUD-04  | Identify aging exceptions                 |

Detective controls are only useful if someone owns the response.

---

# 7. Corrective Control View

Representative corrective controls include:

| Control | Corrective Objective                                  |
| ------- | ----------------------------------------------------- |
| AC-10   | Remove invalid access                                 |
| WF-03   | Escalate service failure                              |
| WF-07   | Route unresolved exception                            |
| CHG-03  | Restore service after failed change                   |
| DG-07   | Correct known data error                              |
| VND-04  | Remove vendor access manually where automation cannot |
| AUT-03  | Recover from automation failure                       |
| AI-04   | Correct ineffective AI recommendation behavior        |
| AUD-03  | Escalate and remediate control failure                |

A control environment that only detects problems but does not define what happens next is incomplete.

---

# 8. Compensating Controls

The preferred control may not always be technically available during initial implementation.

Example:

```text id="07jix7"
Vendor Access Expiration
        ↓
Automatic Revocation Unavailable
        ↓
Generate Manual Disablement Task
        ↓
Assigned Internal Owner
        ↓
Completion Evidence
```

The manual control is weaker than direct automated enforcement.

It can still provide acceptable temporary control if it is:

* assigned
* time-bound
* monitored
* evidenced

Compensating controls should be treated as known design limitations rather than quietly presented as equivalent automation.

---

# 9. Control Ownership Model

Each control should have one accountable owner.

Supporting teams may operate the control.

Example:

```text id="ya6gz3"
Process Owner
     ↓ owns control

Platform Administrator
     ↓ configures control

Support Team
     ↓ operates process

Governance / Auditor
     ↓ reviews evidence
```

The distinction prevents control ownership from defaulting to whoever happens to administer the platform.

---

# 10. Control Evidence Matrix

| Control Area           | Representative Evidence                       |
| ---------------------- | --------------------------------------------- |
| RBAC                   | Role assignments, access reviews              |
| Approval               | Approval history                              |
| Vendor Access          | Sponsor, approval, expiration, revocation     |
| Ticket Ownership       | Assignment history                            |
| Closure                | Required closure values                       |
| SLA                    | Timer and exception history                   |
| Change                 | Risk, approval, implementation, validation    |
| Data Governance        | Quality reports, ownership reviews            |
| Automation             | Execution and exception logs                  |
| AI                     | Recommendation attribution and human decision |
| Platform Configuration | Change and configuration history              |
| Audit Review           | Review record and remediation                 |

Evidence should be generated by normal operation where possible.

A control that requires someone to manually reconstruct proof every time will be difficult to sustain.

---

# 11. Control Operating Frequency

| Frequency                    | Example                                                |
| ---------------------------- | ------------------------------------------------------ |
| Transactional                | Approval, self-approval prevention, closure validation |
| Continuous / System-Enforced | RBAC, inactive-record restrictions                     |
| Event-Driven                 | Termination, vendor expiration, failed automation      |
| Per Change                   | Configuration control, change approval                 |
| Monthly                      | SLA exception review, vendor exception review          |
| Quarterly                    | Privileged-access review                               |
| Semiannual                   | Control ownership / service ownership review           |
| Annual                       | Governance model review                                |

The frequency should follow how quickly the underlying risk can change.

---

# 12. Control Status

During implementation, controls may use the following status model:

| Status      | Meaning                           |
| ----------- | --------------------------------- |
| Proposed    | Control identified                |
| Designed    | Control behavior defined          |
| Configured  | Implemented in target environment |
| Tested      | Validation completed              |
| Operational | Control in production use         |
| Monitored   | Ongoing evidence reviewed         |
| Exception   | Control not operating as designed |

This makes control readiness visible during implementation.

---

# 13. Control Effectiveness

A control should be evaluated on more than whether it exists.

Questions include:

* Is it configured correctly?
* Does it execute consistently?
* Can users bypass it?
* Does it create useful evidence?
* Is the evidence reviewed?
* Does failure trigger correction?
* Is the control creating excessive operational friction?

A technically effective control that users routinely work around is still a weak operating control.

---

# 14. Control Failure Model

```text id="rllyy2"
Control Expected
      ↓
Control Operates?
   ↙            ↘
 Yes             No
 ↓                ↓
Evidence        Exception
                  ↓
              Assign Owner
                  ↓
               Correct
                  ↓
                Verify
```

Control failure should not disappear into general operational backlog.

---

# 15. Control Exception Record

Material control exceptions should include:

* control ID
* affected process or service
* exception description
* business reason
* risk
* owner
* compensating control
* approval where required
* expiration
* review date
* remediation status

This creates a consistent method for managing known control gaps.

---

# 16. Control Testing Approach

Controls should be tested through both:

## Positive Testing

Verify the approved action succeeds.

Example:

```text id="fw01cw"
Authorized Approver
       ↓
Approve Request
       ↓
Approval Recorded
```

## Negative Testing

Verify prohibited activity fails.

Example:

```text id="azepbw"
Requester
    ↓
Attempts Self-Approval
    ↓
Blocked
    ↓
Attempt Logged
```

Negative testing is especially important for access and governance controls.

---

# 17. Representative Control Test Set

| Test ID   | Control                                               |
| --------- | ----------------------------------------------------- |
| TC-CTL-01 | Authorized role receives expected permissions         |
| TC-CTL-02 | Unauthorized role denied controlled action            |
| TC-CTL-03 | Self-approval blocked                                 |
| TC-CTL-04 | Ticket cannot close without required data             |
| TC-CTL-05 | Priority override requires authorized role and reason |
| TC-CTL-06 | Vendor access expires                                 |
| TC-CTL-07 | Failed automation creates assigned exception          |
| TC-CTL-08 | Production configuration change remains auditable     |
| TC-CTL-09 | Expired exception appears in review                   |
| TC-CTL-10 | Failed change retains incident relationship           |

These tests will be incorporated into:

[Testing and UAT](../09%20Testing%20and%20UAT/test%20cases.md)

---

# 18. Monitoring Priorities

Not every control needs a dashboard tile.

Priority monitoring should focus on controls where failure can create material operational or security exposure.

Initial monitoring priorities include:

* privileged-access exceptions
* vendor access past expiration
* self-approval attempts
* emergency changes
* failed changes
* priority overrides
* SLA exceptions
* inactive privileged users
* automation failures
* aging governance exceptions

---

# 19. Control Metrics

| Metric                       | Purpose                                   |
| ---------------------------- | ----------------------------------------- |
| Control Pass Rate            | Measure test effectiveness                |
| Open Control Exceptions      | Measure unresolved exposure               |
| Exception Age                | Identify persistent gaps                  |
| Self-Approval Blocks         | Validate approval separation              |
| Vendor Expiration Compliance | Validate external-access lifecycle        |
| Access Review Completion     | Validate periodic RBAC review             |
| Unauthorized Change Count    | Identify configuration governance failure |
| Automation Exception Rate    | Measure automation reliability            |
| Closure Validation Failures  | Identify process-quality issue            |
| Control Remediation Time     | Measure corrective effectiveness          |

These metrics should support action.

They should not become another set of numbers reviewed without ownership.

---

# 20. Control Priority

Controls may be prioritized during implementation based on risk.

## Priority 1 — Foundational

* RBAC
* ownership
* approval separation
* vendor expiration
* change authorization
* audit logging

## Priority 2 — Workflow Integrity

* SLA exception control
* priority override control
* closure validation
* data integrity
* emergency-change review

## Priority 3 — Optimization

* automation governance
* AI controls
* advanced quality reporting
* trend-based governance monitoring

This allows the organization to establish the controls that matter most before optimizing the environment.

---

# 21. Control Dependencies

Controls frequently depend on other controls.

Example:

```text id="26zdkk"
User Identity
    ↓
RBAC
    ↓
Approval Authority
    ↓
Self-Approval Prevention
```

Another example:

```text id="68j2h6"
Vendor Record
    ↓
Internal Sponsor
    ↓
Access Approval
    ↓
Expiration
    ↓
Revocation
```

A downstream control cannot be considered reliable if its supporting data or identity control is unreliable.

---

# 22. Control Design Guardrails

## Do Not Create Controls Without an Owner

If no one owns the control, it will eventually fail silently.

## Do Not Rely Only on Policy

Where the platform can enforce a critical rule, system enforcement is stronger than written expectation alone.

## Do Not Automate Around an Undefined Decision

The control should reflect an agreed operating rule before automation is added.

## Do Not Treat Logs as Monitoring

A log becomes a useful detective control only when relevant events are reviewed.

## Do Not Hide Compensating Controls

If the preferred control cannot be implemented, document the weaker interim method and its limitations.

## Do Not Measure Controls That No One Will Act On

Monitoring should connect to ownership and response.

---

# 23. Control Matrix Success Criteria

The control model is implementation-ready when:

* controls are identified
* control type is defined
* risk addressed is understood
* ownership is assigned
* implementation point is known
* evidence is defined
* testing exists
* monitoring expectations are defined
* exception handling is defined
* compensating controls are documented where necessary

---

# 24. Control Matrix Conclusion

The purpose of the control environment is not to make the ESM platform harder to use.

It is to make important decisions dependable.

The strongest controls in this design are attached to the places where failure actually matters:

* access
* authorization
* ownership
* change
* vendor dependency
* data integrity
* automation
* auditability

Everything else should remain as lightweight as the risk allows.

A useful control should do four things:

**prevent or detect a real problem, produce evidence, have an owner, and lead to action when it fails.**

If it cannot do those things, it probably does not belong in the control matrix.

**Next:** [Control Framework Mapping](./control%20framework%20mapping.md)
