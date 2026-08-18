# Decision and Edge-Case Matrix

## Purpose

This artifact tests the proposed Satisfactory Academic Progress decision framework against routine, exception-sensitive, conflicting, and ambiguous scenarios.

The objective is to determine whether the state model consistently separates:

* quantitative SAP results
* warning and appeal conditions
* probation and academic-plan states
* compliance status
* data readiness
* workflow disposition

The matrix is intended to demonstrate that the redesigned process can handle both standard SAP cases and edge conditions without allowing incomplete or conflicting information to default automatically to either eligibility or disqualification.

[GRAPHIC PLACEHOLDER — Decision Matrix Overview]

## Decision Logic

The framework evaluates each case in the following order:

1. Determine the quantitative SAP result.
2. Identify the applicable policy pathway.
3. Evaluate warning, appeal, probation, or academic-plan states.
4. Determine compliance with any active exception conditions.
5. Validate data completeness, consistency, and effective dates.
6. Assign a workflow disposition only after all controlling conditions are resolved.

The expected disposition is based on the complete decision context rather than the quantitative result alone.

## Core Decision Matrix

| Scenario                                                          | Quantitative Result                 | Exception / Compliance Context                           | Data Readiness       | Expected Workflow Disposition                                      |
| ----------------------------------------------------------------- | ----------------------------------- | -------------------------------------------------------- | -------------------- | ------------------------------------------------------------------ |
| All SAP criteria satisfied                                        | GPA Pass, Pace Pass, MTF Pass       | No exception required                                    | Complete             | Eligible                                                           |
| Initial GPA failure with warning eligibility                      | GPA Fail                            | Warning eligible                                         | Complete             | Warning                                                            |
| Initial pace failure with warning eligibility                     | Pace Fail                           | Warning eligible                                         | Complete             | Warning                                                            |
| GPA failure with no warning or approved appeal                    | GPA Fail                            | No active exception                                      | Complete             | Appeal Eligible or Disqualified, according to policy               |
| Pace failure with no warning or approved appeal                   | Pace Fail                           | No active exception                                      | Complete             | Appeal Eligible or Disqualified, according to policy               |
| Maximum Timeframe failure with no approved appeal                 | MTF Fail                            | No active exception                                      | Complete             | Appeal Eligible or Disqualified, according to policy               |
| Maximum Timeframe failure with approved appeal and compliant plan | MTF Fail                            | Appeal approved, academic plan active, plan compliant    | Complete             | Requires Review, then Academic Plan Continuation                   |
| Approved appeal with confirmed plan noncompliance                 | Applicable SAP failure remains      | Appeal approved, academic plan active, plan noncompliant | Complete             | Plan Noncompliance, then applicable adverse disposition            |
| Active exception with unresolved compliance                       | Applicable SAP failure remains      | Exception active, compliance unknown                     | Incomplete           | Requires Review                                                    |
| Active exception with conflicting source records                  | Applicable SAP failure remains      | Exception active                                         | Conflicting          | Requires Review                                                    |
| Multiple SAP failures with exception covering only one criterion  | Multiple failures                   | Partial exception coverage                               | Complete             | Evaluate unresolved failure independently before final disposition |
| Late grade change affects SAP result                              | Current result potentially affected | No conclusive exception state                            | Not final            | Requires Review or reprocessing                                    |
| Approved plan modification not synchronized                       | Applicable SAP failure remains      | Plan status inconsistent across systems                  | Conflicting          | Requires Review                                                    |
| Effective-date ambiguity affects plan compliance                  | Applicable SAP failure remains      | Exception or plan may apply                              | Temporally ambiguous | Requires Review                                                    |

The matrix establishes a baseline for the more detailed edge-case scenarios that follow.

## Decision Categories

The test scenarios are organized into five categories.

### Category 1 — Routine Determinations

These cases should be handled almost entirely through deterministic automation.

They include:

* all SAP criteria passing
* initial warning-eligible GPA failure
* initial warning-eligible pace failure
* confirmed failure with no applicable exception
* confirmed plan noncompliance with complete supporting data

The purpose of these scenarios is to verify that the redesigned workflow does not create unnecessary manual review for straightforward cases.

### Category 2 — Approved Exception Continuation

These cases involve an active warning, appeal, probation status, or academic plan that must be evaluated before an adverse disposition can be issued.

They include:

* approved Maximum Timeframe appeal
* active SAP probation
* active academic plan
* confirmed prior-term compliance
* approved plan continuation

The purpose is to ensure that an active exception state is recognized as a required decision input rather than being bypassed by the underlying quantitative failure.

### Category 3 — Compliance Exceptions

These cases test whether the system can distinguish confirmed compliance, confirmed noncompliance, and unresolved compliance.

The key requirement is that:

* confirmed compliance preserves the continuation pathway;
* confirmed noncompliance permits the applicable adverse pathway; and
* unresolved compliance routes to review.

### Category 4 — Data and Timing Exceptions

These cases involve data that is incomplete, stale, conflicting, or temporally ambiguous.

Examples include:

* late grade posting
* grade changes
* transfer-credit changes
* delayed academic-plan synchronization
* program changes
* effective-date conflicts
* registration changes
* incomplete grades

The purpose is to verify that uncertainty is treated as a controlled decision state rather than silently resolved through default logic.

### Category 5 — Multi-Criterion SAP Failures

These cases test simultaneous failure of GPA, pace, and Maximum Timeframe criteria.

An exception applicable to one SAP criterion should not automatically resolve another.

The workflow must retain criterion-level results and evaluate the applicable policy pathway for each failed condition before assigning the final disposition.

[GRAPHIC PLACEHOLDER — Edge-Case Categories]

## Edge Case 1 — Approved Maximum Timeframe Appeal with Continued Compliance

### Conditions

* Maximum Timeframe remains failed.
* A Maximum Timeframe appeal has been approved.
* An academic plan remains active.
* Prior-term plan compliance is confirmed.
* Required decision data is complete and consistent.

### Expected Decision

The Maximum Timeframe calculation remains failed.

The approved exception and confirmed compliance prevent the quantitative failure from being converted directly into automatic disqualification.

The case enters controlled review and may proceed to Academic Plan Continuation after validation.

### Control Tested

* exception-state recognition
* academic-plan compliance validation
* separation of quantitative result and workflow disposition
* adverse-action suppression

[GRAPHIC PLACEHOLDER — Approved MTF Continuation Path]

## Edge Case 2 — Approved Appeal but Academic-Plan Data Is Not Synchronized

### Conditions

* A SAP appeal is approved.
* The approved academic plan exists in one authoritative source.
* The SAP decision process does not yet contain the corresponding plan record or current plan status.

### Expected Decision

The system should not assume either compliance or noncompliance.

The case should enter Requires Review until the plan state is reconciled.

### Control Tested

* cross-system reconciliation
* data completeness validation
* decision-readiness control
* prevention of unsupported adverse action

## Edge Case 3 — Academic Plan Approved After Add/Drop Deadline

### Conditions

* The student enrolled before the academic plan received final approval.
* One or more registered courses may differ from the subsequently approved plan.
* Withdrawing from the course after plan approval may itself create academic or financial consequences.

### Expected Decision

The workflow should evaluate the effective dates of enrollment, plan approval, and applicable registration deadlines before determining compliance.

A course should not be treated automatically as evidence of plan noncompliance solely because the final plan was approved after the student became committed to the enrollment decision.

Where policy interpretation is required, the case should enter Requires Review.

### Control Tested

* temporal validation
* effective-date reconciliation
* professional-judgment routing
* protection against retrospective rule application

## Edge Case 4 — Course Becomes Non-Degree-Applicable After Enrollment

### Conditions

* The student enrolls in a course before final plan or degree-applicability validation.
* The course is later identified as non-degree-applicable.
* Dropping or withdrawing from the course may create a separate compliance issue.

### Expected Decision

The system should distinguish between:

* a course known to be non-degree-applicable at enrollment; and
* a course whose status changed or was clarified after enrollment.

The case should route to review where the timing materially affects whether the student could reasonably have complied with the approved plan.

### Control Tested

* enrollment-context validation
* degree-applicability validation
* temporal reasoning
* controlled exception review

## Edge Case 5 — Advisor-Approved Course Substitution

### Conditions

* A required course is unavailable or otherwise unsuitable during the planned term.
* An authorized substitution is approved.
* The degree-audit or financial-aid system has not yet reflected the substitution.

### Expected Decision

The student should not be classified automatically as noncompliant when an authorized substitution exists but has not yet synchronized across systems.

The case should remain on the exception pathway until the substitution is validated.

### Control Tested

* approved modification recognition
* system synchronization
* authoritative-source validation
* exception persistence

## Edge Case 6 — Required Course Is Not Offered

### Conditions

* The academic plan requires a specific course during a particular term.
* The institution does not offer the course during that term.
* The student enrolls in other degree-applicable coursework.

### Expected Decision

The workflow should not classify the student automatically as noncompliant where the required course was unavailable.

The case should evaluate approved substitutions, plan modification, or reviewer authorization.

### Control Tested

* external dependency handling
* plan-change workflow
* human review
* prevention of impossible compliance requirements

## Edge Case 7 — Late Grade Posting

### Conditions

* SAP evaluation occurs before one or more final grades are posted.
* The missing grade could materially affect GPA, pace, or plan compliance.

### Expected Decision

The SAP determination should remain non-final until the required grade data is available or policy defines a specific treatment for the missing grade.

Where the outcome could materially change, the case should enter Requires Review or be reprocessed automatically when the grade posts.

### Control Tested

* decision-readiness validation
* incomplete-data handling
* event-driven reprocessing
* adverse-action suppression

## Edge Case 8 — Grade Change After SAP Evaluation

### Conditions

* A final SAP determination has been issued.
* A grade is subsequently corrected or changed.
* The new grade affects one or more SAP criteria or academic-plan compliance.

### Expected Decision

The affected SAP evaluation should be reprocessed using the corrected authoritative data.

The system should preserve both the original determination and the revised determination for audit purposes.

### Control Tested

* corrective reprocessing
* historical decision retention
* audit trail
* source-data correction

## Edge Case 9 — Transfer-Credit Change

### Conditions

* Transfer credits are added, removed, or reclassified after a prior SAP evaluation.
* The change affects attempted hours, completed hours, degree applicability, or Maximum Timeframe.

### Expected Decision

The system should identify the change as potentially decision-relevant and re-evaluate the affected SAP criteria.

Where the impact cannot be calculated conclusively, the case should enter review.

### Control Tested

* data-change detection
* recalculation
* dependency management
* auditability

## Edge Case 10 — Program Change

### Conditions

* The student changes academic programs.
* Applicable attempted-credit, degree-audit, or Maximum Timeframe calculations may change.
* An existing appeal or academic plan may have been approved under the previous program.

### Expected Decision

The workflow should determine whether the existing exception remains applicable to the new program before continuation or adverse action is assigned.

The system should not assume either continued validity or automatic expiration without applying the governing policy.

### Control Tested

* exception applicability
* program-state validation
* Maximum Timeframe recalculation
* policy interpretation

## Edge Case 11 — Incomplete Grade

### Conditions

* The student has an incomplete grade at SAP evaluation.
* The incomplete may affect GPA, pace, academic-plan compliance, or degree progress.

### Expected Decision

The system should apply the institution's SAP treatment of incomplete grades consistently.

If final compliance cannot be determined until the grade is resolved, the workflow should preserve a review or pending state rather than inferring compliance.

### Control Tested

* policy-rule implementation
* incomplete-data treatment
* consistent application
* review routing

## Edge Case 12 — Multiple Simultaneous SAP Failures

### Conditions

The student fails more than one SAP criterion.

For example:

* GPA Fail
* Pace Fail
* Maximum Timeframe Fail

An approved exception may address only one of those failures.

### Expected Decision

Each failed criterion should be evaluated independently against the applicable warning, appeal, probation, or exception pathway.

The final workflow disposition should be assigned only after all unresolved failures have been evaluated.

### Control Tested

* criterion-level state retention
* exception scope
* composite decision logic
* prevention of overbroad exception application

[GRAPHIC PLACEHOLDER — Multi-Criterion Decision Logic]

## Edge Case 13 — Appeal Workflow Unavailable After Disqualification

### Conditions

* The system assigns an adverse SAP disposition.
* Institutional policy allows an appeal or remediation pathway.
* The appeal mechanism is unavailable, disabled, or not yet open to the student.

### Expected Decision

The workflow should identify whether the adverse disposition has a valid associated remediation path.

Where policy provides an appeal right, the system should not leave the student in a terminal status without an accessible next action or documented administrative process.

### Control Tested

* workflow completeness
* remediation-path validation
* student-service continuity
* control over terminal states

## Edge Case 14 — Administrative Review Delays Downstream Aid Processing

### Conditions

* A case properly enters Requires Review.
* Manual review remains unresolved for an extended period.
* Downstream financial-aid processing depends on resolution.

### Expected Decision

The system should retain the review state while monitoring queue age and downstream impact.

Escalation thresholds should identify cases approaching operational or regulatory deadlines.

### Control Tested

* queue aging
* escalation
* SLA/KPI monitoring
* downstream dependency management

## Edge Case 15 — Conflicting Authoritative Sources

### Conditions

Two or more decision-relevant systems contain conflicting information.

Potential conflicts include:

* different academic-plan versions
* differing program records
* inconsistent enrollment status
* conflicting degree applicability
* inconsistent appeal status
* inconsistent effective dates

### Expected Decision

The workflow should not choose a source silently where the conflict affects eligibility.

The case enters Requires Review until the authoritative state is established.

### Control Tested

* authoritative-source governance
* reconciliation
* conflict detection
* controlled resolution

## Negative Testing

The framework must also demonstrate that review controls do not become a mechanism for avoiding valid SAP enforcement.

### Confirmed Failure with No Exception

A student who fails an applicable SAP criterion, has no warning eligibility, no approved appeal, and no unresolved data issue should proceed through the applicable adverse workflow without unnecessary manual review.

### Confirmed Plan Noncompliance

A student with an active academic plan who clearly fails the approved requirements should not remain in Academic Plan Continuation merely because the plan exists.

### Expired Exception

An appeal or probation state that has expired should not continue to suppress an otherwise valid adverse determination unless another applicable state exists.

### Exception Applies to Different Criterion

An approved Maximum Timeframe exception should not resolve an unrelated GPA or pace failure unless policy explicitly establishes that effect.

These tests are important because an exception-aware workflow must control both false-positive disqualification and false eligibility.

## Decision Consistency

Two cases with materially equivalent decision inputs should produce equivalent workflow states.

Consistency testing should compare:

* quantitative results
* exception status
* plan status
* compliance status
* effective dates
* data readiness
* resulting disposition

Differences in outcome should be explainable through a documented difference in input, policy, or authorized judgment.

## Expected Test Outcomes

The redesigned workflow should demonstrate the following behaviors:

* deterministic cases remain automated;
* warning eligibility is recognized before adverse action;
* approved exceptions are evaluated before disqualification;
* academic-plan compliance is represented explicitly;
* confirmed noncompliance remains enforceable;
* unknown compliance does not become assumed noncompliance;
* missing or conflicting data routes to review;
* exceptions apply only to the criteria they address;
* multiple failures are evaluated independently;
* data changes can trigger recalculation or review;
* final dispositions remain traceable to their decision inputs.

## Acceptance Principle

A decision scenario passes testing when the resulting workflow disposition can be explained using:

1. the quantitative SAP result;
2. the applicable policy state;
3. the exception and compliance state;
4. data completeness and effective-date conditions; and
5. the defined decision authority.

If the resulting disposition cannot be reconstructed from those inputs, the decision process is not sufficiently auditable.

## Key Takeaway

A robust SAP workflow must work not only for routine cases, but also for the cases where policy, timing, data, and exceptions intersect.

The edge-case matrix tests whether the redesigned framework behaves consistently at those boundaries.

**The goal is not to route every unusual case to a human. The goal is to ensure that automation acts conclusively only when the available decision context supports a conclusive result.**

[GRAPHIC PLACEHOLDER — Decision Matrix Closing Summary]
