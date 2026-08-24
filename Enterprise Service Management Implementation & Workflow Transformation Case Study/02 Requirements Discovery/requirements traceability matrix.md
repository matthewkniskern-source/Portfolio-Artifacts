# Requirements Traceability Matrix

## Purpose

This matrix connects the current-state problems identified during discovery to the requirements, workflows, controls, test cases, and performance measures used throughout the Enterprise Service Management implementation.

The intent is straightforward:

> **Nothing important should appear in the final design without a reason, and nothing important identified during discovery should disappear before testing.**

This artifact is the primary traceability layer for the case study.

It demonstrates how the implementation moves from:

**Problem → Requirement → Design → Control → Validation → Measurement**

The matrix is intentionally maintained at a level that a business analyst, implementation consultant, process owner, or technical lead can use without needing to understand a specific ESM platform.

---

# 1. Traceability Model

The transformation lifecycle is structured as:

```text
Current-State Finding
        ↓
Business Requirement
        ↓
Functional / Nonfunctional Requirement
        ↓
Target-State Design
        ↓
Governance / Control
        ↓
Test / UAT Scenario
        ↓
Operational Metric
```

The purpose of this structure is not documentation for its own sake.

It provides three practical checks:

1. **Every major design decision should trace backward to a real need.**
2. **Every major requirement should trace forward to a validation method.**
3. **Every major implementation objective should eventually produce a measurable outcome.**

A visual version of this lifecycle will be maintained in:

[Requirements Traceability Flow](../diagrams/requirements%20traceability%20flow.md)

---

# 2. Traceability Status

Each requirement is assigned a traceability status during the implementation lifecycle.

| Status      | Meaning                                                  |
| ----------- | -------------------------------------------------------- |
| Identified  | Requirement has been captured but not yet fully designed |
| Designed    | Requirement has a defined target-state response          |
| Controlled  | Required governance or control has been identified       |
| Testable    | A validation or UAT scenario has been defined            |
| Validated   | Requirement has successfully passed acceptance testing   |
| Operational | Requirement is active in the production process          |
| Measured    | Operational performance is being monitored               |

During this case study, requirements will progress through these states as later sections are completed.

---

# 3. Core Traceability Matrix

| Source                                   | Business Requirement                      | Functional / Nonfunctional Requirement | Target-State Design                       | Control / Governance                         | Planned Test         | Operational Metric                             |
| ---------------------------------------- | ----------------------------------------- | -------------------------------------- | ----------------------------------------- | -------------------------------------------- | -------------------- | ---------------------------------------------- |
| FM-01 Undocumented work                  | BR-01 Authoritative service record        | FR-01, FR-02, FR-03                    | Standardized Intake Model                 | Mandatory managed record for qualifying work | TC-INT-01            | Service Capture Rate                           |
| FM-02 Duplicate work                     | BR-02 Consistent intake                   | FR-04                                  | Incident Correlation / Parent-Child Model | Duplicate designation and record association | TC-INC-02            | Duplicate Ticket Rate                          |
| FM-03 Subjective priority                | BR-03 Consistent prioritization           | FR-05, FR-06, FR-07                    | Impact / Urgency Priority Model           | Controlled priority override                 | TC-INC-03            | Priority Override Rate                         |
| FM-04 Reassignment loops                 | BR-04 Clear ownership                     | FR-08, FR-09, FR-10                    | Ownership and Escalation Model            | Required owner and reassignment reason       | TC-INC-04            | Reassignment Rate                              |
| FM-05 Manual escalation                  | BR-05 SLA and escalation                  | FR-11, FR-12, FR-13                    | SLA and Escalation Model                  | Timers, thresholds, exception reasons        | TC-SLA-01, TC-SLA-02 | SLA Compliance                                 |
| FM-06 Informal approval                  | BR-06 Auditable approvals                 | FR-14, FR-15                           | Approval Workflow                         | Structured approval record                   | TC-REQ-01            | Approval Completion Rate                       |
| FM-07 Self-approval                      | BR-07 Separation of duties                | FR-16, NFR-01                          | Controlled Approval Model                 | Self-approval prevention / RBAC              | TC-REQ-02            | Approval Exception Rate                        |
| FM-08 Missing asset / CI context         | BR-08 Service and configuration context   | FR-17, NFR-13                          | Service Data Model                        | Data ownership and relationship standards    | TC-DAT-01            | CI Association Rate                            |
| FM-09 Knowledge loss                     | BR-09 Operational knowledge reuse         | FR-18, FR-19                           | Knowledge Lifecycle                       | Review and publication control               | TC-KNW-01            | Knowledge Reuse Rate                           |
| FM-10 Failed change unlinked to incident | BR-10 Change traceability                 | FR-20, FR-21, FR-22                    | Change Workflow and Data Relationships    | Required outcome and validation              | TC-CHG-01, TC-CHG-02 | Change Success Rate                            |
| FM-11 Hidden vendor activity             | BR-11 Vendor accountability               | FR-23, FR-24                           | Vendor Support Workflow                   | Internal owner retained                      | TC-VND-01            | Vendor Dependency Time                         |
| FM-12 Persistent vendor access           | BR-12 Temporary access governance         | FR-25, FR-26, NFR-01                   | Vendor / Temporary Access Workflow        | Expiration and sponsorship                   | TC-VND-02            | Expired Access Exceptions                      |
| FM-13 Weak closure record                | BR-13 Closure quality                     | FR-27, FR-28                           | Record Closure Model                      | Mandatory closure data                       | TC-CLS-01            | Reopen Rate                                    |
| FM-14 Recurring issues hidden            | BR-14 Trend identification                | FR-29                                  | Trend and Pattern Analysis                | Management review / trend criteria           | TC-RPT-01            | Repeat Incident Rate                           |
| FM-15 Incomplete reporting               | BR-15 Reliable reporting                  | FR-30, FR-31, NFR-14                   | Performance Framework                     | Common metric definitions                    | TC-RPT-02            | Reporting Confidence / Data Completeness       |
| FM-16 Bad automation                     | BR-16 Controlled automation               | FR-32, FR-33, FR-34, NFR-10, NFR-11    | Automation Framework                      | Logging and manual exception path            | TC-AUT-01, TC-AUT-02 | Automation Failure Rate                        |
| FM-16 AI risk                            | BR-17 Responsible AI assistance           | FR-35–FR-40, NFR-19, NFR-20            | AI-Assisted Service Model                 | Human review / restricted actions            | TC-AI-01, TC-AI-02   | AI Recommendation Acceptance / Correction Rate |
| Stakeholder / baseline findings          | BR-18 Adoption and continuous improvement | FR-41, FR-42, NFR-05, NFR-06           | Adoption and Training Model               | Role-based training / feedback               | TC-UAT-01            | Adoption Rate / CSAT                           |

---

# 4. Requirement-to-Design Mapping

The matrix above provides the full lifecycle view.

The following table focuses specifically on where approved requirements will be implemented in the target-state design.

| Requirement Area          | Primary Design Artifact                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Intake and service record | [Target Operating Model](../03%20Target%20Service%20Model/target%20operating%20model.md)                           |
| Service catalog           | [Service Catalog](../03%20Target%20Service%20Model/service%20catalog.md)                                           |
| Priority and SLA          | [Priority and SLA Model](../03%20Target%20Service%20Model/priority%20and%20sla%20model.md)                         |
| Ownership and escalation  | [Ownership and Escalation](../03%20Target%20Service%20Model/ownership%20and%20escalation.md)                       |
| Incident lifecycle        | [Incident Management](../04%20Workflow%20Design/incident%20management.md)                                          |
| Service request lifecycle | [Service Request Management](../04%20Workflow%20Design/service%20request%20management.md)                          |
| Change lifecycle          | [Change Management](../04%20Workflow%20Design/change%20management.md)                                              |
| Knowledge lifecycle       | [Knowledge Management](../04%20Workflow%20Design/knowledge%20management.md)                                        |
| Data relationships        | [Service Management Data Model](../05%20Data%20and%20Configuration%20Model/service%20management%20data%20model.md) |
| RBAC and approvals        | [RBAC and Approval Controls](../06%20Governance%20and%20Controls/rbac%20and%20approval%20controls.md)              |
| Automation                | [Automation Opportunities](../07%20Automation%20and%20AI/automation%20opportunities.md)                            |
| AI governance             | [AI Governance](../07%20Automation%20and%20AI/ai%20governance.md)                                                  |
| Implementation            | [Implementation Plan](../08%20Implementation%20Plan/implementation%20plan.md)                                      |
| Validation                | [Testing and UAT](../09%20Testing%20and%20UAT/test%20strategy.md)                                                  |
| Adoption                  | [Adoption Strategy](../10%20Adoption%20and%20Training/adoption%20strategy.md)                                      |
| Measurement               | [Performance Framework](../11%20Metrics%20and%20Optimization/performance%20framework.md)                           |

---

# 5. Traceability Walkthrough — Incident Priority

A traceability matrix is only useful if the relationships actually make sense.

The following examples walk a requirement through the full lifecycle.

## Current-State Problem

**FM-03 — Priority is influenced by requester pressure.**

A manager directly contacting a technician may receive faster attention than a broader business-impact incident already in the queue.

---

## Business Requirement

**BR-03**

The organization shall prioritize managed service work using defined business impact and urgency criteria.

---

## Functional Requirements

**FR-05**

The platform shall support defined impact and urgency values.

**FR-06**

The platform shall calculate priority using approved impact and urgency rules.

**FR-07**

Authorized priority override shall require a documented reason.

---

## Target Design

The [Priority and SLA Model](../03%20Target%20Service%20Model/priority%20and%20sla%20model.md) will define the relationship between:

```text
Impact
   +
Urgency
   ↓
Priority
   ↓
Response Target
   ↓
Escalation Behavior
```

---

## Governance

Priority overrides will be:

* role restricted
* documented
* timestamped
* retained in history
* reportable

---

## Testing

**TC-INC-03 — Priority Calculation and Override**

A high-impact / high-urgency incident should receive the expected priority.

An unauthorized user should not be able to alter it.

An authorized user may override it only by entering an approved reason.

---

## Measurement

Relevant measures include:

* priority distribution
* priority override rate
* SLA compliance by priority
* override reasons

The original problem is therefore traceable all the way to operational measurement.

---

# 6. Traceability Walkthrough — Vendor Access

## Current-State Problem

**FM-12 — Temporary vendor access becomes permanent by accident.**

A vendor receives access for troubleshooting, the issue is resolved, and the access remains active because no workflow event requires removal.

---

## Business Requirement

**BR-12**

Temporary, vendor, and designated privileged access shall be governed throughout the access lifecycle.

---

## Functional Requirements

**FR-25**

The request shall capture:

* vendor
* sponsor
* business purpose
* system
* privilege
* start
* expiration
* approval

**FR-26**

The solution shall enforce or initiate access expiration.

---

## Nonfunctional Requirement

**NFR-01**

Role-based access shall restrict the ability to approve or administer access.

---

## Target Design

```text
Access Request
     ↓
Sponsor Validation
     ↓
Approval
     ↓
Provision
     ↓
Active Access
     ↓
Expiration
     ↓
Disable / Extend
```

Detailed design will be incorporated into:

[Governance and Controls](../06%20Governance%20and%20Controls/governance%20model.md)

---

## Governance

Controls will include:

* internal sponsor
* authorized approver
* defined expiration
* extension approval
* access history
* periodic review

---

## Testing

**TC-VND-02 — Vendor Access Expiration**

A vendor receives approved temporary access.

At expiration, the integrated access action occurs or a tracked disablement task is generated.

No extension may occur without a new authorized decision.

---

## Measurement

Relevant measures include:

* temporary access requests
* expired access exceptions
* access extensions
* overdue disablement actions

A current-state access weakness therefore becomes a testable and measurable process control.

---

# 7. Traceability Walkthrough — SLA Escalation

## Current-State Problem

**FM-05 — Escalation depends on someone noticing that work is late.**

The requester effectively becomes the escalation system by asking for an update.

---

## Business Requirement

**BR-05**

The organization shall define measurable service-level expectations and escalation behavior.

---

## Functional Requirements

**FR-11**

The platform shall apply defined SLA timer behavior.

**FR-12**

The platform shall generate warnings and escalation at defined thresholds.

**FR-13**

SLA exceptions shall require documented reason.

---

## Target Design

```text
Ticket Created
     ↓
SLA Active
     ↓
Warning Threshold
     ↓
Technician / Group Alert
     ↓
Breach Threshold
     ↓
Escalation
```

Approved states may pause the clock where policy permits.

---

## Governance

The organization must define:

* when the SLA starts
* when it pauses
* who may apply an exception
* what counts as a legitimate pause
* who receives escalation

The platform should enforce the agreed model rather than invent it.

---

## Testing

**TC-SLA-01 — SLA Pause / Resume**

Confirm that an approved pause state stops the timer and that returning to active support resumes it.

**TC-SLA-02 — SLA Breach Escalation**

Confirm that a ticket crossing the defined threshold generates the expected escalation.

---

## Measurement

Relevant metrics include:

* SLA compliance
* warning volume
* breach volume
* exception rate
* breach by support group

---

# 8. Traceability Walkthrough — Failed Change

## Current-State Problem

**FM-10 — A failed change appears as an unrelated incident.**

The incident team may spend time rediscovering that the affected service changed hours earlier.

---

## Business Requirement

**BR-10**

Changes shall be traceable to affected services, configuration items, implementation outcomes, and related incidents.

---

## Functional Requirements

**FR-20**

Changes shall support affected service and CI relationships.

**FR-21**

Incidents shall support relationships to relevant changes.

**FR-22**

Change records shall capture implementation outcome and validation.

---

## Target Design

```text
Proposed Change
      ↓
Risk / Approval
      ↓
Implementation
      ↓
Validation
   ↙       ↘
Success   Failure
            ↓
          Backout
            ↓
          Incident
```

---

## Governance

Change closure requires:

* implementation outcome
* validation result
* backout status where applicable
* resulting incident relationship

---

## Testing

**TC-CHG-02 — Failed Change and Backout**

Implement a simulated failed change.

Confirm:

* unsuccessful outcome is recorded
* backout path activates
* associated incident can be linked
* change cannot close as successful

---

## Measurement

Relevant measures include:

* change success rate
* backed-out changes
* incidents caused by change
* failed changes by service

---

# 9. Traceability Walkthrough — AI-Assisted Categorization

## Business Need

AI assistance may reduce repetitive classification work, but it should not quietly become an unreviewable decision engine.

---

## Business Requirement

**BR-17**

AI-assisted service-management capabilities shall support human decision-making while maintaining restrictions for sensitive or governance-related actions.

---

## Functional Requirements

**FR-36**

AI may recommend categorization.

**FR-39**

AI recommendations shall be distinguishable from human decisions.

**FR-40**

AI shall not independently execute designated restricted actions.

---

## Nonfunctional Requirements

**NFR-19**

AI functionality shall respect existing data restrictions.

**NFR-20**

Designated AI-assisted decisions shall remain subject to human review.

---

## Target Design

```text
Ticket Created
      ↓
AI Suggestion
      ↓
Confidence / Policy Check
      ↓
Human Review
   ↙          ↘
Accept       Correct
   ↓            ↓
Workflow Continues
```

For low-risk use cases, later implementation maturity may allow higher levels of automation.

Restricted decisions remain controlled regardless of confidence.

---

## Testing

**TC-AI-01 — AI Recommendation Correction**

Confirm an authorized technician can reject or correct an AI categorization recommendation.

**TC-AI-02 — Restricted AI Action**

Confirm AI functionality cannot independently approve a privileged-access request or high-risk change.

---

## Measurement

Potential measures include:

* recommendation acceptance rate
* correction rate
* category accuracy
* manual review rate
* AI-related exception rate

The goal is not to prove that AI is being used.

The goal is to determine whether it is actually helping.

---

# 10. Nonfunctional Traceability

Nonfunctional requirements cut across multiple workflows and therefore require their own traceability view.

| NFR    | Primary Concern          | Applies To                                        | Validation                         |
| ------ | ------------------------ | ------------------------------------------------- | ---------------------------------- |
| NFR-01 | RBAC                     | Approvals, changes, vendor access, administration | Role access testing                |
| NFR-02 | Sensitive records        | Restricted workflows                              | Permission testing                 |
| NFR-03 | Material action logging  | All controlled workflows                          | Audit-log review                   |
| NFR-04 | Audit context            | All controlled workflows                          | Audit evidence inspection          |
| NFR-05 | End-user usability       | Portal, request forms, approvals                  | UAT                                |
| NFR-06 | Administrative burden    | Technician workflows                              | Pilot feedback / UAT               |
| NFR-07 | Maintainability          | Platform configuration                            | Design review                      |
| NFR-08 | Controlled configuration | Platform administration                           | Change-control test                |
| NFR-09 | Scalability              | Entire platform                                   | Architecture / capacity validation |
| NFR-10 | No silent failure        | Automation / integration                          | Negative-path testing              |
| NFR-11 | Recoverable failure      | Automation / integration                          | Failure recovery test              |
| NFR-12 | Retention                | Service data                                      | Configuration review               |
| NFR-13 | Data ownership           | Services / CI / assets / vendors                  | Data-governance review             |
| NFR-14 | Metric consistency       | Reporting                                         | Report-definition validation       |
| NFR-15 | Reporting access         | Dashboards                                        | Permission testing                 |
| NFR-16 | Accessibility            | End-user experience                               | Accessibility review               |
| NFR-17 | Integration security     | Connected systems                                 | Security review                    |
| NFR-18 | Integration traceability | Connected systems                                 | Failure-log testing                |
| NFR-19 | AI data handling         | AI functions                                      | Security / privacy test            |
| NFR-20 | AI human review          | AI functions                                      | Workflow testing                   |
| NFR-21 | Recoverability           | Platform operation                                | Recovery walkthrough               |
| NFR-22 | Performance              | User and technician operations                    | Performance observation            |

---

# 11. Implementation Priority View

Not every requirement should be implemented at the same time.

A practical implementation sequence is:

## Foundation

* BR-01 — Authoritative record
* BR-02 — Consistent intake
* BR-04 — Ownership
* BR-13 — Closure quality
* NFR-01 — RBAC
* NFR-03 — Auditability

Without these, the platform cannot act as a trustworthy operating record.

---

## Core Workflow

* BR-03 — Priority
* BR-05 — SLA
* BR-06 — Approval
* BR-07 — Separation of duties
* BR-10 — Change traceability
* BR-11 — Vendor accountability
* BR-12 — Access governance

These establish consistent service behavior.

---

## Operational Context

* BR-08 — Asset / CI context
* BR-09 — Knowledge
* BR-14 — Trend analysis
* BR-15 — Reporting

These improve troubleshooting, visibility, and management value.

---

## Optimization

* BR-16 — Automation
* BR-17 — AI assistance
* BR-18 — Continuous improvement

Automation and AI sit after the core workflow model for a reason.

> **There is very little value in automating a process the organization has not stabilized yet.**

---

# 12. Traceability Gaps

Traceability review should identify four types of gap.

## Orphan Requirement

A requirement exists without a documented source need.

**Question:** Why are we building this?

---

## Unresolved Finding

A material current-state problem has no requirement assigned to it.

**Question:** Did we actually solve the problem we identified?

---

## Untested Requirement

A requirement has design coverage but no validation path.

**Question:** How will we know it works?

---

## Unmeasured Outcome

A requirement passes testing but has no meaningful operational measure.

**Question:** How will we know it continues working or provides value after go-live?

These gaps should be treated as implementation issues rather than documentation cleanup.

---

# 13. Traceability Quality Gate

Before the solution moves into production, all **Must** requirements should satisfy the following:

| Gate                                           | Required |
| ---------------------------------------------- | -------- |
| Source business need identified                | Yes      |
| Business owner identified                      | Yes      |
| Functional / NFR coverage identified           | Yes      |
| Target-state design identified                 | Yes      |
| Required control identified                    | Yes      |
| Test case defined                              | Yes      |
| Acceptance result recorded                     | Yes      |
| Production owner identified                    | Yes      |
| Operational metric identified where applicable | Yes      |

A requirement should not be marked complete simply because a field or workflow was configured.

Completion means the required business behavior has been implemented and validated.

---

# 14. Traceability During Change

Requirements traceability should continue after initial implementation.

When a workflow changes, the organization should be able to determine:

* which requirement is affected
* which control may change
* which test cases need to be repeated
* which reporting logic may change
* which users require updated training

This is especially important for changes involving:

* priority rules
* SLA logic
* approvals
* RBAC
* vendor access
* automation
* AI behavior

The traceability matrix therefore becomes part of ongoing configuration governance rather than an artifact that is abandoned after go-live.

---

# 15. Showcase View

The complete transformation can be reduced to one working model:

```text
CURRENT STATE
Fragmented service process
        ↓
FAILURE MODE
Specific operational weakness
        ↓
BUSINESS REQUIREMENT
Required organizational outcome
        ↓
FUNCTIONAL / NFR
Required platform behavior and operating condition
        ↓
TARGET DESIGN
Workflow, data, ownership, approval, or automation model
        ↓
CONTROL
Required governance and decision boundary
        ↓
TEST
Evidence that the design behaves as intended
        ↓
METRIC
Evidence that the process continues to perform
        ↓
CONTINUOUS IMPROVEMENT
Use operational results to adjust the process
```

This is the core implementation logic of the case study.

The platform is important.

The traceability around why it is being configured is more important.

---

# 16. Requirements Phase Exit Criteria

The requirements phase is considered ready to move into target-state design when:

* all major current-state failure modes have requirement coverage
* all Must business requirements have defined functional or nonfunctional support
* requirement owners are identified
* assumptions and constraints are documented
* major requirement conflicts have been resolved
* requirements are sufficiently specific to guide design
* requirements are testable
* no critical requirement is dependent on an undefined business decision

At that point, configuration is no longer guesswork.

The implementation can move from **what the organization needs** to **how the operating model should work**.

**Next:** [Target Operating Model](../03%20Target%20Service%20Model/target%20operating%20model.md)
