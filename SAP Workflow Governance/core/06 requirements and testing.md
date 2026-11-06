# Requirements and Testing

## Purpose

This artifact translates the proposed SAP workflow redesign into business requirements, functional requirements, nonfunctional requirements, user stories, acceptance criteria, and test conditions.

The objective is to demonstrate that the conceptual workflow can be converted into implementable and testable system behavior.

The requirements are designed around five principles:

* quantitative SAP results remain independently traceable;
* approved exceptions are evaluated before adverse action;
* academic-plan compliance is explicitly represented;
* incomplete or conflicting information routes to controlled review; and
* final workflow dispositions are reproducible from documented decision inputs.

The requirements in this artifact describe a hypothetical SAP eligibility workflow and do not represent the proprietary requirements or system architecture of any specific institution.

<img width="1536" height="1024" alt="06 Reqs to Decision Trace" src="https://github.com/user-attachments/assets/93ee5c1b-4c06-4613-b521-e91c9c8b4d23" />

## Requirements Structure

The requirements are organized into four layers:

### Business Requirements

Define what the institution needs the SAP workflow to accomplish.

### Functional Requirements

Define what the system must do to satisfy those business needs.

### Nonfunctional Requirements

Define how reliably, securely, consistently, and audibly the system must operate.

### Acceptance Criteria

Define the observable conditions that demonstrate a requirement has been implemented successfully.

This structure creates traceability from business need through system behavior and validation.

## Business Requirements

### BR-01 — Preserve Quantitative SAP Results

The system must retain criterion-level GPA, pace, and Maximum Timeframe results independently of warning, exception, compliance, or final workflow states.

### BR-02 — Separate Calculation from Workflow Disposition

The system must not treat a failed quantitative SAP criterion as automatically equivalent to a final adverse disposition when additional decision-relevant states exist.

### BR-03 — Evaluate Applicable Warning Eligibility

The system must evaluate warning eligibility where institutional policy permits warning for the applicable SAP condition.

### BR-04 — Evaluate Approved Exceptions Before Adverse Action

The system must determine whether an active approved appeal, probation status, or academic plan applies before issuing a final adverse disposition.

### BR-05 — Associate Exceptions with Applicable SAP Criteria

An exception must be linked to the specific SAP criterion or criteria it is authorized to address.

### BR-06 — Evaluate Academic-Plan Compliance

Where continued eligibility depends on an academic plan, the workflow must distinguish confirmed compliance, confirmed noncompliance, and unresolved compliance.

### BR-07 — Validate Decision Readiness

The system must evaluate whether required decision inputs are complete, current, consistent, and effective for the applicable evaluation period before issuing a conclusive disposition.

### BR-08 — Support Controlled Review

Cases with incomplete, conflicting, exception-sensitive, or temporally ambiguous information must have a controlled review pathway.

### BR-09 — Support Multi-Criterion SAP Evaluation

The system must evaluate simultaneous GPA, pace, and Maximum Timeframe failures independently before determining the overall workflow outcome.

### BR-10 — Preserve Decision Auditability

The system must retain sufficient evidence to reconstruct the inputs, rules, exceptions, reviewer actions, and final disposition associated with each SAP determination.

### BR-11 — Restrict Decision Authority

Sensitive state changes, manual overrides, and final eligibility decisions must be restricted to authorized roles.

### BR-12 — Support Controlled Reprocessing

Decision-relevant changes to authoritative source data must support controlled recalculation or reprocessing where the change could affect the SAP outcome.

### BR-13 — Maintain Accessible Remediation Paths

Where policy permits appeal, review, or remediation following an adverse disposition, the workflow must provide or identify the applicable next-action pathway.

### BR-14 — Govern Rule and Configuration Changes

Changes to SAP rules, thresholds, integrations, exception logic, and workflow states must be versioned, approved, tested, and auditable.

### BR-15 — Preserve Operational Efficiency

The workflow should continue to process routine deterministic cases automatically and reserve human review for cases where automation lacks sufficient information or authority.

<img width="1536" height="1024" alt="06 Business Req Architecture" src="https://github.com/user-attachments/assets/a89e8abb-4d67-4990-9f7b-4ad1cf466abd" />

## Functional Requirements

### FR-01 — Criterion-Level Calculation State

The system shall store separate GPA, pace, and Maximum Timeframe calculation results for each SAP evaluation.

### FR-02 — Composite Failure Support

The system shall support multiple simultaneous failed SAP criteria within the same evaluation.

### FR-03 — Warning Rule Evaluation

The system shall evaluate whether the applicable failed criterion qualifies for warning under the active policy rule set.

### FR-04 — Exception Lookup

When a SAP criterion fails, the system shall search for active warning, appeal, probation, and academic-plan records associated with the student and applicable criterion.

### FR-05 — Exception Scope Validation

The system shall verify that an identified exception applies to the failed SAP criterion before using the exception in workflow determination.

### FR-06 — Exception Effective-Period Validation

The system shall validate that an exception is active for the relevant SAP evaluation period.

### FR-07 — Academic-Plan Association

The system shall associate an approved academic plan with the appeal or probation condition under which it was established.

### FR-08 — Academic-Plan Version Control

The system shall retain the applicable academic-plan version and effective dates used for each determination.

### FR-09 — Compliance State Determination

The system shall support at least the following academic-plan compliance states:

* Compliant
* Noncompliant
* Unknown
* Data Conflict
* Review Required

### FR-10 — Decision-Readiness Validation

Before final automated disposition, the system shall validate:

* required-data completeness;
* source-data recency;
* source consistency;
* effective-date alignment; and
* unresolved conflicts.

### FR-11 — Review Routing

If required decision information is incomplete, conflicting, stale, or temporally ambiguous, the system shall assign Requires Review rather than issuing a conclusive adverse disposition.

### FR-12 — Adverse-Action Suppression

The system shall suppress automatic adverse disposition while an applicable approved exception or unresolved review condition remains active.

### FR-13 — Confirmed Noncompliance Processing

Where plan noncompliance is confirmed, the system shall allow the workflow to proceed to the applicable adverse or appeal pathway defined by policy.

### FR-14 — Criterion-Level Exception Processing

The system shall independently evaluate exceptions for each failed SAP criterion.

### FR-15 — Final Disposition Assignment

The system shall assign the final workflow disposition only after all applicable failed criteria, exception states, compliance conditions, and data-readiness checks have been resolved.

### FR-16 — Reviewer Queue

The system shall maintain a controlled review queue for cases requiring human validation.

### FR-17 — Review Reason

Each case routed for review shall include one or more standardized review-reason codes.

Representative review reasons may include:

* Missing Data
* Stale Data
* Data Conflict
* Temporal Conflict
* Compliance Unknown
* Exception Interpretation
* Multi-Criterion Conflict
* Policy Interpretation

### FR-18 — Reviewer Decision Capture

The system shall record the authorized reviewer's disposition, rationale, timestamp, and applicable supporting evidence.

### FR-19 — Manual Override Control

Manual override shall require authorized access and a documented justification.

### FR-20 — Override Logging

The system shall retain before-and-after values, user identity, role, timestamp, justification, and related case information for each override.

### FR-21 — Reprocessing Trigger

The system shall support recalculation or reprocessing when decision-relevant authoritative data changes.

### FR-22 — Historical State Retention

The system shall retain prior calculation states, workflow states, and disposition history after reprocessing or correction.

### FR-23 — Rule-Version Retention

Each determination shall identify the SAP policy or business-rule version used.

### FR-24 — Remediation-Path Validation

Where the final disposition permits an appeal, review, or remediation action, the system shall identify the available next step.

### FR-25 — Decision Communication

The final workflow outcome shall be available to authorized downstream processes and communication functions.

<img width="1536" height="1024" alt="06 Functional Req Model" src="https://github.com/user-attachments/assets/809f7fef-7236-47be-ab6e-b009fdb77631" />

## Nonfunctional Requirements

### NFR-01 — Auditability

The system must preserve enough decision evidence to reconstruct why a determination occurred.

### NFR-02 — Traceability

Business requirements, functional rules, control logic, and test cases must be traceable to one another.

### NFR-03 — Security

Access must follow role-based access control and least-privilege principles.

### NFR-04 — Segregation of Duties

Sensitive functions should be separated where practical, including:

* source-data maintenance;
* exception approval;
* system configuration;
* manual override; and
* final disposition authority.

### NFR-05 — Data Integrity

Decision-relevant records must preserve source, timestamp, version, and effective-date information where applicable.

### NFR-06 — Availability

SAP processing and review functions should be available during defined eligibility-processing windows.

### NFR-07 — Performance

Routine deterministic SAP evaluations should complete within an operationally acceptable processing interval.

### NFR-08 — Scalability

The workflow should support peak-term SAP evaluation volumes without requiring proportional growth in manual review staffing.

### NFR-09 — Reliability

A repeated evaluation using the same authoritative inputs and rule version should produce the same deterministic result.

### NFR-10 — Explainability

The workflow should expose the major factors that contributed to the disposition, including failed criteria, applicable exceptions, compliance state, and review conditions.

### NFR-11 — Privacy

Access to student records and decision information must be limited to authorized institutional functions.

### NFR-12 — Change Control

Production rules, configurations, mappings, and workflow logic must be changed through an approved and auditable change-management process.

### NFR-13 — Logging

Material system and reviewer actions must be logged.

### NFR-14 — Recoverability

The system should support rollback or controlled remediation following a defective rule or configuration deployment.

### NFR-15 — Monitoring

Operational metrics and control indicators should support identification of abnormal workflow behavior, queue backlog, exception trends, and decision reversals.

<img width="1536" height="1024" alt="06 Non Functional Reqs" src="https://github.com/user-attachments/assets/15f73a9f-534a-45fc-b142-78b3436cf82e" />

## User Stories

### US-01 — Financial Aid Reviewer

**As a Financial Aid reviewer, I want cases with active exceptions and unresolved compliance conditions routed to review so that I can make a final determination using complete decision context.**

### US-02 — Financial Aid Processor

**As a Financial Aid processor, I want routine SAP cases processed automatically so that staff effort is reserved for cases requiring professional review.**

### US-03 — Academic Advisor

**As an Academic Advisor, I want approved academic-plan requirements and modifications represented accurately so that downstream SAP decisions use the current plan.**

### US-04 — Registrar / Records Function

**As a records owner, I want corrected grades, enrollment changes, and program changes to trigger appropriate downstream evaluation so that decisions reflect authoritative academic data.**

### US-05 — Compliance Reviewer

**As a compliance reviewer, I want each SAP disposition to be reconstructable from the data, rule, exception, and reviewer history so that control operation can be tested.**

### US-06 — System Administrator

**As a system administrator, I want rule and configuration changes versioned and approved so that SAP logic can be maintained without losing traceability.**

### US-07 — Governance Owner

**As a governance owner, I want decision authority and override capability restricted by role so that sensitive eligibility decisions remain controlled.**

### US-08 — Operations Manager

**As an operations manager, I want review-queue aging and exception metrics so that unresolved cases can be identified before they delay downstream aid processing.**

<img width="1536" height="1024" alt="06 Stakeholder Story Map" src="https://github.com/user-attachments/assets/7241b638-c87f-42cd-b545-3ecb1a438077" />

## Acceptance Criteria

### AC-01 — Quantitative Failure Retention

**Given** a student exceeds Maximum Timeframe
**When** the student has an approved Maximum Timeframe appeal
**Then** the quantitative Maximum Timeframe result remains failed
**And** the exception state is evaluated separately.

### AC-02 — Approved Exception Prevents Automatic Disqualification

**Given** a student has a failed SAP criterion
**And** an active approved exception applies to that criterion
**When** the SAP workflow is evaluated
**Then** the system does not automatically assign Disqualified before evaluating the exception conditions.

### AC-03 — Compliant Academic Plan

**Given** a student remains in a failed Maximum Timeframe state
**And** an approved appeal and active academic plan exist
**And** prior-term compliance is confirmed
**When** required decision data is complete
**Then** the case proceeds through the approved exception pathway
**And** may result in Academic Plan Continuation according to policy and decision authority.

### AC-04 — Unknown Compliance

**Given** an active academic plan exists
**And** required compliance information is unavailable
**When** the workflow attempts to determine final eligibility
**Then** the case is assigned Requires Review
**And** the system does not infer Plan Noncompliance.

### AC-05 — Confirmed Plan Noncompliance

**Given** an active academic plan exists
**And** authoritative data confirms the plan requirements were not satisfied
**When** the workflow is evaluated
**Then** the system assigns Plan Noncompliance
**And** proceeds according to the applicable adverse policy pathway.

### AC-06 — Data Conflict

**Given** two decision-relevant authoritative sources contain conflicting information
**When** the conflict could affect SAP eligibility
**Then** the case is routed to Requires Review
**And** no conclusive automated adverse or continuation disposition is issued.

### AC-07 — Effective-Date Conflict

**Given** an exception, plan, enrollment, or grade record has an effective-date relationship that cannot be resolved automatically
**When** the case is evaluated
**Then** the case is routed for review.

### AC-08 — Multiple Failed Criteria

**Given** GPA, pace, and Maximum Timeframe contain multiple failures
**And** an approved exception applies only to Maximum Timeframe
**When** the workflow is evaluated
**Then** the Maximum Timeframe exception does not resolve the GPA or pace failures
**And** each unresolved criterion is processed independently.

### AC-09 — Authorized Override

**Given** a reviewer has approved override authority
**When** the reviewer changes a controlled disposition
**Then** the system records the user, role, timestamp, previous state, new state, and justification.

### AC-10 — Unauthorized Override

**Given** a user does not have override authority
**When** the user attempts to modify a protected disposition
**Then** the system denies the action
**And** the attempted action is logged according to security policy.

### AC-11 — Grade Change Reprocessing

**Given** a SAP determination has already been issued
**And** an authoritative grade change alters a decision-relevant input
**When** the change is accepted by the source system
**Then** the affected SAP determination is flagged for reprocessing or review
**And** the original decision history remains retained.

### AC-12 — Rule-Version Traceability

**Given** a SAP determination is issued
**When** the decision record is reviewed
**Then** the rule or policy version used to produce the determination can be identified.

### AC-13 — Remediation Path

**Given** a final adverse disposition permits appeal under policy
**When** the disposition is issued
**Then** the applicable appeal or remediation pathway is identifiable and available to the downstream workflow.

### AC-14 — Deterministic Reproducibility

**Given** identical authoritative inputs and the same business-rule version
**When** the SAP evaluation is executed multiple times
**Then** the deterministic calculation and routing results are consistent.

### AC-15 — Complete Audit Reconstruction

**Given** a completed SAP determination
**When** an authorized reviewer examines the decision record
**Then** the reviewer can identify:

* quantitative results;
* relevant exception state;
* academic-plan state;
* compliance state;
* data-readiness status;
* applied rule version;
* reviewer action, if any; and
* final disposition.

<img width="1536" height="1024" alt="06 Acceptance Criteria Decision Path" src="https://github.com/user-attachments/assets/a77654f5-c2a8-4328-8e40-6556c1c7572e" />

## Test Strategy

Testing should verify both calculation correctness and workflow-control behavior.

The strategy should include:

### Unit Testing

Validate individual business rules, including:

* GPA pass/fail rule;
* pace pass/fail rule;
* Maximum Timeframe pass/fail rule;
* warning eligibility;
* exception validity;
* effective-date logic;
* compliance-state logic.

### Integration Testing

Validate information movement among conceptual source domains such as:

* student information;
* financial aid;
* advising;
* degree audit;
* registration;
* grading;
* transfer-credit processing.

### Workflow Testing

Validate routing among:

* Eligible;
* Warning;
* SAP Probation;
* Academic Plan Continuation;
* Requires Review;
* Appeal Eligible;
* Plan Noncompliance; and
* Disqualified.

### Security Testing

Validate:

* RBAC;
* privileged state changes;
* manual overrides;
* segregation of duties;
* audit logging.

### Regression Testing

Validate that policy or configuration changes do not unintentionally alter unrelated SAP pathways.

### User Acceptance Testing

Validate that authorized business users can correctly interpret, review, resolve, and audit cases using the redesigned process.

<img width="1536" height="1024" alt="06 SAP Test Strat Model" src="https://github.com/user-attachments/assets/e539e72c-8fa3-4262-8b0d-3a50637886b6" />

## Core Test Cases

### TC-01 — Standard Eligible Case

**Inputs**

* GPA Pass
* Pace Pass
* MTF Pass

**Expected Result**

Eligible

**Review Required**

No

### TC-02 — Initial Warning-Eligible GPA Failure

**Inputs**

* GPA Fail
* warning criteria satisfied
* no conflicting data

**Expected Result**

Warning

**Review Required**

No

### TC-03 — Maximum Timeframe Failure Without Exception

**Inputs**

* MTF Fail
* no approved MTF appeal
* decision data complete

**Expected Result**

Appeal Eligible or Disqualified according to policy

**Review Required**

No, unless policy requires review

### TC-04 — Approved MTF Appeal with Plan Compliance

**Inputs**

* MTF Fail
* appeal approved
* academic plan active
* prior-term compliance confirmed
* decision data complete

**Expected Result**

Approved exception pathway leading to Academic Plan Continuation following required validation

### TC-05 — Academic Plan Compliance Unknown

**Inputs**

* applicable SAP failure
* academic plan active
* compliance data incomplete

**Expected Result**

Requires Review

### TC-06 — Academic Plan Noncompliance

**Inputs**

* applicable SAP failure
* academic plan active
* noncompliance confirmed

**Expected Result**

Plan Noncompliance followed by applicable adverse workflow

### TC-07 — Conflicting Plan Versions

**Inputs**

* applicable SAP failure
* different academic-plan versions in decision-relevant sources

**Expected Result**

Requires Review

### TC-08 — Late Grade Change

**Inputs**

* completed SAP determination
* authoritative grade corrected after evaluation
* SAP result potentially affected

**Expected Result**

Reprocessing or controlled review

### TC-09 — MTF Exception with Independent GPA Failure

**Inputs**

* MTF Fail
* GPA Fail
* approved exception applies only to MTF

**Expected Result**

MTF exception evaluated independently
GPA failure remains unresolved and follows its applicable pathway

### TC-10 — Unauthorized Override Attempt

**Inputs**

* standard user
* protected workflow disposition

**Action**

User attempts manual override.

**Expected Result**

Action denied and logged.

<img width="1536" height="1024" alt="06 Core Test Matrix" src="https://github.com/user-attachments/assets/8f99f9ea-4794-461d-873d-26a95f216a89" />

## Negative Testing

Negative tests verify that controls do not create unintended eligibility.

### NT-01 — Exception Expired

An expired exception must not continue to suppress a valid adverse workflow.

### NT-02 — Exception Applies to Different Criterion

An MTF exception must not automatically resolve a GPA or pace failure.

### NT-03 — Plan Exists but Noncompliance Is Confirmed

The existence of an academic plan must not by itself produce Academic Plan Continuation.

### NT-04 — Review State Without Trigger

A deterministic case with complete and unambiguous data should not be routed unnecessarily to human review.

### NT-05 — Missing Approval Authority

A user without required decision authority must not be able to approve an exception or final disposition.

## Requirements Traceability

Each requirement should map to one or more controls and tests.

| Business Requirement                    | Functional Requirement     | Control / Design Element        | Test Reference      |
| --------------------------------------- | -------------------------- | ------------------------------- | ------------------- |
| BR-01 Preserve quantitative results     | FR-01, FR-02               | Three-layer state model         | AC-01, TC-09        |
| BR-04 Evaluate approved exceptions      | FR-04, FR-05, FR-06        | Exception Control Gate          | AC-02, TC-04        |
| BR-06 Evaluate academic-plan compliance | FR-07, FR-08, FR-09        | Compliance state model          | AC-03, AC-04, AC-05 |
| BR-07 Validate decision readiness       | FR-10, FR-11               | Decision Readiness Control Gate | AC-06, AC-07, TC-07 |
| BR-08 Support controlled review         | FR-16, FR-17, FR-18        | Human-in-the-loop review        | TC-05, TC-07        |
| BR-09 Multi-criterion evaluation        | FR-02, FR-14               | Multi-Criterion Decision Logic  | AC-08, TC-09        |
| BR-10 Preserve auditability             | FR-18, FR-20, FR-22, FR-23 | Audit logging and state history | AC-09, AC-12, AC-15 |
| BR-11 Restrict decision authority       | FR-19, FR-20               | RBAC / decision authority model | AC-09, AC-10, TC-10 |
| BR-12 Controlled reprocessing           | FR-21, FR-22               | Corrective control process      | AC-11, TC-08        |
| BR-14 Govern changes                    | NFR-12, NFR-14             | SAP Change-Control Lifecycle    | Regression testing  |
| BR-15 Preserve efficiency               | FR-11, FR-16               | Defined review triggers         | NT-04               |

<img width="1536" height="1024" alt="06 Req Traceability Map" src="https://github.com/user-attachments/assets/c9b495d5-3817-4a55-90e3-f1bbbac939a5" />

## Definition of Done

A requirement is considered complete only when:

* the business objective is documented;
* the functional behavior is defined;
* the associated control is identified;
* acceptance criteria are documented;
* test coverage exists;
* security and audit implications are addressed;
* evidence of successful validation can be retained.

A technically implemented rule that cannot be traced to a business requirement or validated through testing should not be considered production-ready.

## Validation Outcomes

The redesigned workflow should demonstrate that:

* calculation results remain accurate and independently traceable;
* active exceptions are recognized;
* exceptions remain within authorized scope;
* compliance is represented explicitly;
* unknown states do not become unsupported assumptions;
* conflicting information prevents premature conclusive action;
* authorized users can resolve review cases;
* unauthorized users cannot perform privileged actions;
* data changes can trigger controlled re-evaluation;
* materially equivalent cases produce consistent deterministic behavior;
* decisions remain reconstructable after completion.

## Key Takeaway

The requirements and test model converts the SAP workflow redesign from a conceptual governance proposal into a system that can be specified, built, tested, and audited.

**A good decision model is not complete when the logic sounds reasonable. It is complete when the required behavior is explicit, the controls are traceable, and the expected outcomes can be tested.**

<img width="1536" height="1024" alt="06 Req and Test Closing Summary" src="https://github.com/user-attachments/assets/fd1c9bc7-68f2-4e7d-9332-3407528f270a" />
