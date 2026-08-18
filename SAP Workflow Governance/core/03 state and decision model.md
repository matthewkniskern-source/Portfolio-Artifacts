# State and Decision Model

## Purpose

This artifact defines the state model used by the proposed Satisfactory Academic Progress workflow.

The objective is to separate three concepts that are often treated as though they were interchangeable:

1. **Quantitative SAP results**
2. **Exception and compliance states**
3. **Workflow dispositions**

This separation allows the system to preserve an accurate SAP calculation while still applying the correct policy, exception, review, or adverse-action pathway.

The model is designed to support deterministic automation where the required data and business rules are complete, while providing controlled states for cases that require additional validation or human judgment.

[GRAPHIC PLACEHOLDER — Three-Layer SAP State Model]

## State Model Overview

The proposed framework treats SAP processing as a progression through three decision layers.

### Layer 1 — Quantitative SAP Result

The system determines whether the student satisfies the measurable SAP criteria.

These results describe the student's mathematical SAP condition.

They do not independently determine the final workflow action.

### Layer 2 — Exception and Compliance State

When a quantitative failure exists, the workflow evaluates additional policy and operational conditions that may affect how that failure should be processed.

These states describe whether the student qualifies for a warning, has an approved exception, remains compliant with an academic plan, or has unresolved information requiring review.

### Layer 3 — Workflow Disposition

The system assigns the operational state that determines what happens next.

This may include continued eligibility, warning, probation, academic-plan continuation, review, appeal eligibility, confirmed noncompliance, or disqualification.

The fundamental relationship is:

**Quantitative Result + Exception / Compliance State → Workflow Disposition**

The quantitative result remains independently traceable throughout the process.

## Quantitative SAP States

The quantitative layer evaluates the principal SAP measurements.

### GPA States

**PASS_GPA**
The student's cumulative GPA satisfies the applicable SAP standard.

**FAIL_GPA**
The student's cumulative GPA does not satisfy the applicable SAP standard.

### Pace States

**PASS_PACE**
The student's cumulative completion rate satisfies the applicable pace-of-progression requirement.

**FAIL_PACE**
The student's cumulative completion rate does not satisfy the applicable pace requirement.

### Maximum Timeframe States

**PASS_MTF**
The student remains within the applicable Maximum Timeframe threshold.

**FAIL_MTF**
The student exceeds the applicable Maximum Timeframe threshold.

These states are intended to represent calculation outcomes only.

An approved appeal, probation status, or academic plan does not convert a failed quantitative result into a passing one. Instead, those conditions are represented separately within the exception and compliance layer.

## Composite Quantitative Result

A student may fail more than one SAP criterion simultaneously.

The state model must therefore support combinations rather than assuming a single SAP result.

A student may, for example, have:

* PASS_GPA and PASS_PACE and FAIL_MTF
* FAIL_GPA and PASS_PACE and PASS_MTF
* FAIL_GPA and FAIL_PACE and PASS_MTF
* FAIL_GPA and FAIL_PACE and FAIL_MTF

The workflow should evaluate each failed criterion against the applicable policy pathway.

A single overall SAP status should not erase the underlying criterion-level results needed for later review, appeal processing, testing, or audit reconstruction.

## Exception and Compliance States

The second layer evaluates conditions that determine how a failed SAP result should be processed.

### WARNING_ELIGIBLE

The student meets the policy conditions for an automatic SAP warning period.

This state generally applies where institutional policy permits warning following an initial GPA or pace failure without requiring an appeal.

### WARNING_ACTIVE

A warning period has been assigned and remains active for the applicable evaluation period.

### APPEAL_REQUIRED

The student has failed an applicable SAP criterion and continued eligibility requires an approved appeal or other authorized exception.

### APPEAL_PENDING

An appeal has been submitted or initiated but a final decision has not yet been issued.

### APPEAL_APPROVED

The applicable SAP appeal has been approved.

Approval alone does not necessarily establish continuing eligibility across future terms. The workflow must also evaluate the effective period, conditions of approval, and any associated academic plan.

### APPEAL_DENIED

The applicable appeal has been denied and no other authorized continuation pathway has been established.

### PROBATION_ACTIVE

The student is permitted to continue under SAP probation for the applicable evaluation period.

The state should retain the basis for probation, effective dates, and any associated compliance requirements.

### ACADEMIC_PLAN_ACTIVE

An approved academic plan governs continued SAP eligibility.

The state should be associated with an identifiable plan version, effective period, and defined requirements.

### PLAN_COMPLIANT

Available authoritative data indicates that the student satisfied the applicable academic-plan requirements for the evaluation period.

### PLAN_NONCOMPLIANT

Available authoritative data confirms that the student failed to satisfy one or more required academic-plan conditions.

### PLAN_COMPLIANCE_UNKNOWN

The system cannot determine plan compliance because required information is missing, incomplete, unavailable, or not yet final.

### DATA_CONFLICT

Two or more authoritative or decision-relevant sources contain information that cannot be reconciled automatically.

### TEMPORAL_CONFLICT

Effective dates, processing dates, enrollment deadlines, plan approvals, grade changes, or other time-sensitive records create ambiguity regarding which rule or record should govern the determination.

### REVIEW_REQUIRED

The system has identified a condition that prevents a reliable final automated disposition.

This is a controlled workflow state, not an eligibility outcome.

[GRAPHIC PLACEHOLDER — Exception and Compliance State Map]

## Workflow Disposition States

The third layer determines the operational outcome of the decision process.

### ELIGIBLE

The student satisfies applicable SAP requirements and no adverse or exception-sensitive condition prevents normal aid processing.

### WARNING

The student has failed an applicable SAP criterion but qualifies for a policy-defined warning period.

### SAP_PROBATION

The student is permitted to continue under an approved SAP probation status.

### ACADEMIC_PLAN_CONTINUATION

The student remains mathematically noncompliant with one or more SAP criteria but is authorized to continue under an approved and compliant academic-plan pathway.

### REQUIRES_REVIEW

The system cannot support a final automated determination because exception-sensitive, incomplete, conflicting, or temporally ambiguous information exists.

The case is routed to an authorized reviewer.

### APPEAL_ELIGIBLE

The student is not currently eligible under the automated SAP determination but may enter an available appeal process under applicable policy.

### PLAN_NONCOMPLIANCE

The student is subject to an academic plan and confirmed noncompliance has been identified.

The resulting adverse action is determined according to applicable policy.

### DISQUALIFIED

The available authoritative information supports an adverse SAP determination and no active warning, approved exception, compliant plan, unresolved conflict, or other condition prevents final disposition.

## Why Separate States Matter

The proposed model prevents one data point from simultaneously representing a calculation, an exception decision, and a workflow action.

Consider a student who exceeds Maximum Timeframe.

The quantitative state remains:

**FAIL_MTF**

If the student has no applicable exception, the workflow may proceed toward an adverse or appeal-eligible disposition.

If the student has an approved appeal and active academic plan, the quantitative result still remains:

**FAIL_MTF**

The additional state may instead be:

**APPEAL_APPROVED + ACADEMIC_PLAN_ACTIVE + PLAN_COMPLIANT**

That combination can then support a workflow state such as:

**REQUIRES_REVIEW**

followed by:

**ACADEMIC_PLAN_CONTINUATION**

The system therefore preserves both truths:

* the student exceeds the quantitative Maximum Timeframe threshold
* the student may remain eligible under a valid approved exception pathway

[GRAPHIC PLACEHOLDER — MTF State Separation]

## Decision Precedence

Not every state should have equal authority.

The future-state model uses decision precedence to prevent a lower-level calculation result from bypassing a higher-level exception or control condition.

### Precedence 1 — Data Integrity and Decision Readiness

Before a final adverse determination is allowed, required information must be sufficiently complete, authoritative, current, and internally consistent.

If required data is unavailable or conflicting, the workflow moves to Requires Review.

### Precedence 2 — Active Policy or Exception State

An active warning, approved appeal, probation status, or academic plan must be evaluated before a failed quantitative criterion is converted into a final adverse disposition.

### Precedence 3 — Compliance Determination

Where an exception depends on continued compliance, the system evaluates whether the applicable conditions were satisfied.

Confirmed compliance preserves the applicable exception pathway.

Confirmed noncompliance permits the workflow to proceed toward the policy-defined adverse state.

Unknown or conflicting compliance requires review.

### Precedence 4 — Final Workflow Disposition

Only after the calculation, exception, compliance, and data-readiness states are resolved should the system assign a conclusive workflow disposition.

[GRAPHIC PLACEHOLDER — Decision Precedence Model]

## Decision-State Relationships

The relationship between states can be expressed through several core decision patterns.

### Standard Passing Path

All applicable quantitative criteria pass.

**Result:** Eligible

### Warning Path

An applicable GPA or pace failure occurs and policy-defined warning eligibility is confirmed.

**Result:** Warning

### Failure Without Exception

A quantitative SAP failure exists and no applicable warning, approved exception, or other continuation state exists.

**Result:** Appeal Eligible or Disqualified, according to policy

### Approved Exception Path

A quantitative failure exists and an applicable approved exception remains active.

The workflow evaluates probation, academic-plan requirements, and compliance before issuing an adverse disposition.

### Compliant Academic-Plan Path

A quantitative failure remains present, an academic plan is active, and compliance is confirmed.

**Result:** Academic Plan Continuation or controlled review prior to continuation, according to policy and decision authority

### Confirmed Plan Noncompliance Path

An active academic plan exists and noncompliance is confirmed.

**Result:** Plan Noncompliance followed by the applicable adverse workflow

### Incomplete or Conflicting Data Path

A final determination depends on information that is missing, stale, conflicting, or temporally ambiguous.

**Result:** Requires Review

## Multiple-Failure Logic

Simultaneous failure of multiple SAP criteria requires criterion-level evaluation.

A workflow should not assume that one exception automatically resolves every failed criterion.

For example, an approved Maximum Timeframe appeal may address FAIL_MTF while an independent FAIL_GPA or FAIL_PACE condition may require separate warning, appeal, probation, or adverse-action logic.

The decision process should therefore:

1. retain each quantitative result independently;
2. identify the applicable policy pathway for each failed criterion;
3. identify exceptions applicable to each failure;
4. determine whether one or more unresolved failures remain;
5. assign the final workflow disposition only after all applicable conditions have been evaluated.

This prevents an exception authorized for one SAP condition from being improperly applied to another.

## Controlled Ambiguity

One of the most important additions to the future-state model is a formal state for uncertainty.

Traditional workflow designs may attempt to force every case into a final eligibility or ineligibility state.

The proposed model instead recognizes that some cases are not decision-ready.

A case may be decision-incomplete when:

* required information is missing
* records disagree
* an academic-plan modification has not synchronized
* a grade change is pending
* transfer-credit evaluation is incomplete
* an effective date is unclear
* a policy rule requires interpretation
* multiple SAP pathways produce conflicting outcomes

In these circumstances, Requires Review is the correct system state because the available information does not yet support a defensible final decision.

This state prevents ambiguity from being silently converted into either false eligibility or false disqualification.

## State Transition Controls

Transitions between major workflow states should occur only when defined conditions are satisfied.

A controlled transition should identify:

* current state
* triggering event
* required inputs
* business rule evaluated
* resulting state
* authority responsible for the transition
* timestamp
* policy or rule version
* reviewer action where applicable

For example, a transition from Requires Review to Academic Plan Continuation should require documented validation of the applicable exception, academic-plan status, compliance state, and decision authority.

A transition from Requires Review to Disqualified should likewise preserve the basis for the adverse determination.

This approach treats state transitions as auditable business events rather than simple status-field updates.

## State Persistence

Important states should remain available historically even after the student's current workflow status changes.

For example, a student may move through:

Warning → Appeal Required → Appeal Approved → SAP Probation → Academic Plan Continuation

The current disposition alone does not explain how that outcome was reached.

Historical state retention supports:

* audit reconstruction
* appeal review
* policy consistency
* root-cause analysis
* control testing
* student-service review
* operational reporting

The system should therefore distinguish current status from historical decision-state records.

## State Ownership

Different states may depend on different authoritative sources or business owners.

Quantitative results may originate from academic and financial-aid calculations.

Appeal decisions may be owned by Financial Aid or another designated authority.

Academic-plan requirements may originate from advising or an approved planning process.

Enrollment and degree applicability may depend on registration and degree-audit data.

Final adverse or continuation dispositions may require Financial Aid decision authority.

The future-state model should therefore identify both:

* the authoritative source of each state
* the role authorized to create, validate, modify, or resolve that state

Detailed data-source and governance mappings are maintained in the supporting artifacts.

## Model Design Principles

The state model is governed by the following principles:

* quantitative calculations remain independently traceable;
* approved exceptions do not erase failed quantitative results;
* exceptions must be linked to the SAP criteria they actually address;
* academic-plan compliance must be explicitly represented;
* unresolved information must have a controlled workflow state;
* confirmed noncompliance must remain distinguishable from unknown compliance;
* multiple SAP failures must be evaluated independently;
* workflow dispositions must reflect the complete decision context;
* state transitions must be auditable;
* final adverse actions require sufficient decision authority and data completeness.

## Key Takeaway

The proposed SAP framework does not rely on a single status field to represent the entire eligibility decision.

It separates:

**What the calculation determined**

from

**What exception or compliance conditions exist**

from

**What the workflow should do next**

That separation allows the system to preserve quantitative accuracy while applying policy, exceptions, compliance requirements, and human review in a controlled and auditable manner.

[GRAPHIC PLACEHOLDER — Calculation → Context → Disposition Closing Model]
