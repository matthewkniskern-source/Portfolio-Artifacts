# Current-State and Future-State Workflow

## Purpose

This artifact models a conceptual current-state Satisfactory Academic Progress workflow and proposes a future-state design that separates quantitative SAP calculation from exception handling, compliance evaluation, and final eligibility disposition.

The current-state model is not intended to reproduce any institution's proprietary workflow. It represents a plausible simplified process consistent with the observed case scenario and common risks associated with automated eligibility systems.

The future-state model is designed to preserve automation for routine determinations while introducing controlled exception evaluation when the available information does not support a conclusive automated decision.

## Current-State Conceptual Workflow

A simplified SAP workflow may operate as a sequence in which quantitative criteria are evaluated and failed criteria lead directly to an adverse eligibility state.

### Simplified Adverse Path

The conceptual risk is that a quantitative SAP failure may become the controlling workflow state before relevant exception and compliance information is evaluated.

<img width="1672" height="941" alt="02 Current State Workflow" src="https://github.com/user-attachments/assets/8a422526-da53-479e-8400-f2ecd2b978ad" />


The issue is not that the calculation itself is necessarily incorrect.

The issue is that relevant decision context may exist outside the calculation result.

If these conditions are evaluated only after an adverse disposition is assigned, or are unavailable to the decision process entirely, the workflow can produce an outcome that is mathematically consistent but operationally incomplete.

## Current-State Failure Points

The case study identifies several points where an automated SAP workflow may become vulnerable to inappropriate or unsupported outcomes.

### Failure Point 1 — Calculation and Workflow State Are Collapsed

A failed quantitative criterion may be treated as equivalent to a final eligibility decision, even though calculation result, exception state, and workflow disposition are distinct system concepts.

### Failure Point 2 — Exception History Is Not Evaluated Before Adverse Action

Prior appeal or exception records may exist outside the immediate SAP calculation process. If an active approved exception is not evaluated before adverse action, the workflow may return the student to the same status that originally triggered the appeal.

### Failure Point 3 — Academic-Plan Compliance Is Treated as Secondary Data

Where an academic plan governs continued eligibility, plan status and prior-term compliance should function as decision inputs. If they are not incorporated into the workflow, the system may recognize the original SAP failure without recognizing successful compliance with the approved remediation path.

### Failure Point 4 — Effective Dates Are Not Reconciled

Appeals, academic plans, enrollment changes, substitutions, grades, and program changes may become effective at different times. Without temporal validation, the workflow may classify a student using information that was not yet available or actionable during the relevant decision period.

### Failure Point 5 — Cross-System Data Is Incomplete or Unsynchronized

SAP decisions may depend on records maintained across financial aid, advising, registration, degree-audit, grading, and student-information systems. If those records are incomplete or unsynchronized at evaluation time, the automated decision may rely on an incomplete decision set.

### Failure Point 6 — No Controlled Ambiguity State Exists

A workflow that lacks a controlled review state may have no safe destination for incomplete, conflicting, or exception-sensitive cases. In that environment, ambiguity may default to an adverse disposition rather than being routed for validation.

## Current-State Control Weakness

The central weakness is not necessarily an incorrect calculation, but an incomplete decision process. A quantitative engine may be allowed to exercise decision authority beyond the information available to it.

A robust control environment should distinguish calculation authority, exception interpretation, academic-plan compliance validation, and final adverse-action authority.

## Future-State Design Principle

The future-state workflow introduces an explicit decision layer between quantitative SAP calculation and final eligibility disposition.

The redesigned process evaluates quantitative results first, then determines whether policy, exception, compliance, temporal, or data-quality conditions affect the appropriate workflow outcome.


<img width="1672" height="941" alt="02 Future State Workflow" src="https://github.com/user-attachments/assets/8f1ba539-5903-484d-8387-5f072808ea34" />

Human review is introduced only when the available data, exception state, or policy context does not support a conclusive automated determination.

## Future-State Workflow

### Step 1 — Evaluate Quantitative SAP Criteria

The system evaluates cumulative GPA, pace of progression, and Maximum Timeframe. Each produces a discrete pass or fail result that remains authoritative even when an exception exists.

### Step 2 — Determine Whether Additional SAP Processing Is Required

If all applicable criteria pass, the student continues through standard eligibility processing.

If one or more criteria fail, the workflow evaluates the policy and exception context associated with the failure.

### Step 3 — Evaluate Warning Eligibility

Where institutional policy permits a warning period for the applicable GPA or pace condition, the system evaluates whether the student meets warning criteria.

If warning eligibility is confirmed, the workflow assigns a Warning status.

No appeal evaluation is required unless policy or subsequent conditions require it.

### Step 4 — Evaluate Approved Exceptions

The system checks the appeal type, status, applicable criterion, effective period, and any associated academic-plan requirements.

If no applicable approved exception exists, the case proceeds according to the normal adverse or appeal-eligible pathway defined by policy.

If an applicable approved exception exists, the workflow continues to compliance evaluation before adverse action is permitted.

### Step 5 — Evaluate Academic-Plan State

Where an approved exception includes an academic plan, the workflow validates the current plan version, effective dates, required milestones, approved substitutions, and prior-term compliance.

The existence of an academic plan does not automatically establish continued eligibility.

It establishes that plan compliance is a required decision input.

### Step 6 — Validate Prior-Term Compliance

Prior-term compliance is evaluated against the authoritative academic-plan requirements. Possible states include Compliant, Noncompliant, Unknown, Data Conflict, and Review Required. Confirmed compliance preserves the exception pathway unless another policy condition prevents continuation; confirmed noncompliance proceeds to the applicable adverse state; unresolved compliance routes to controlled review.

### Step 7 — Validate Enrollment and Degree Applicability

The workflow evaluates current degree-applicable enrollment, approved substitutions, registration changes, withdrawals, incomplete grades, program changes, and other conditions that may affect plan compliance.

### Step 8 — Validate Effective Dates and Data Completeness

Before a conclusive adverse determination is issued, the workflow validates data completeness, recency, synchronization, effective-date alignment, and unresolved conflicts. Incomplete, stale, conflicting, or temporally ambiguous data routes the case to Requires Review.

### Step 9 — Assign Workflow Disposition

The workflow assigns the appropriate operational disposition based on the full decision context. The resulting workflow state reflects the business action to be taken without altering the underlying quantitative SAP result.

## Primary Maximum Timeframe Path

The primary case demonstrates how the proposed workflow handles a continuing Maximum Timeframe failure under an approved exception.

<img width="1672" height="941" alt="02 Primary MTF Exception" src="https://github.com/user-attachments/assets/89f756b1-5f47-4535-9439-b7b1c421a472" />


The Maximum Timeframe calculation remains failed throughout the process. The workflow does not redefine the student as mathematically compliant; it recognizes that an approved exception, active academic plan, and confirmed compliance require additional evaluation before a final adverse disposition.

## Human-in-the-Loop Review

Human review is not intended to replace routine automation.

It serves as a controlled decision mechanism for cases in which automation lacks sufficient authority or information to act conclusively.

### Review Triggers

A case should be considered for controlled review when:

* an active approved exception exists
* an academic plan requires compliance validation
* required data is missing or stale
* authoritative sources conflict
* effective dates are ambiguous
* an approved substitution or plan modification requires interpretation
* a late grade or transfer-credit change affects the result
* multiple SAP criteria fail under different policy pathways
* system rules cannot determine a single defensible disposition

### Reviewer Responsibilities

The reviewer validates:

* applicable SAP policy
* appeal and exception status
* academic-plan version and effective dates
* prior-term compliance
* current enrollment context
* relevant data conflicts
* final workflow disposition

The reviewer should not alter quantitative results without correcting the underlying authoritative data.

### Review Outcomes

Controlled review may result in:

*academic-plan continuation
*SAP probation or appeal eligibility
*confirmed plan noncompliance
*disqualification
*source-data correction or policy escalation

## Decision Authority Boundaries

Final Adverse-Action Authority: Automated adverse action should occur only when the applicable SAP failure is established and no unresolved exception, data conflict, effective-date issue, or policy ambiguity prevents a conclusive determination.

### Calculation Authority

Automation may determine quantitative SAP results when the required academic data is complete and authoritative.

### Rule-Evaluation Authority

Automation may evaluate deterministic policy conditions where the required inputs and rules are clearly defined.

### Exception-Interpretation Authority

Automation may identify approved exceptions and test defined conditions, but ambiguous exception interpretation should be routed to an authorized reviewer.

### Final Adverse-Action Authority

Automatic adverse action should occur only where:

* the applicable SAP failure is established
* no active exception prevents automated disposition
* required data is complete
* required data is authoritative
* no unresolved conflict exists
* applicable effective dates are valid
* the business rule produces a single unambiguous outcome

Otherwise, the workflow should enter a controlled review state.

## Control Improvements

The future-state workflow introduces preventive, detective, and corrective controls.

### Preventive Controls

* required exception-state evaluation before adverse action
* academic-plan compliance validation
* effective-date validation
* required-input completeness checks

### Detective Controls

* reconciliation between SAP, appeal, advising, degree-audit, and enrollment records
* stale-data detection
* exception-status monitoring
* review-queue aging reports

### Corrective Controls

* controlled manual review
* documented disposition changes
* source-data correction and reprocessing

## Auditability Requirements

Each SAP determination should retain sufficient information to reconstruct the decision.

The audit record should identify:

* quantitative SAP results
* source-data timestamps
* policy or rule version applied
* applicable appeal or exception record
* academic-plan identifier and version
* compliance state
* workflow rules evaluated
* workflow disposition
* review trigger, if applicable
* reviewer identity
* reviewer action
* override reason, if applicable
* final disposition
* decision timestamp

This creates a traceable relationship between data, rules, human actions, and outcomes.

## Key Takeaway

The proposed future-state workflow does not weaken SAP enforcement.

It strengthens the decision process by separating quantitative calculation from exception handling and final workflow authority.

**Routine cases remain automated. Clear adverse cases remain enforceable. Exception-sensitive, incomplete, or conflicting cases receive controlled review before a final determination is made.**

The result is a workflow designed to be more accurate, auditable, consistent, and defensible without unnecessarily replacing automation with manual processing.

