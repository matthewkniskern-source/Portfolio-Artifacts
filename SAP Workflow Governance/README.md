# SAP Workflow Governance and Automation Case Study

# SAP Workflow Governance and Automation Case Study

> An anonymized systems-analysis and GRC case study developing a generalized Satisfactory Academic Progress eligibility and exception-handling framework using a Maximum Timeframe appeal scenario as the primary case.

## Case Study Scope

This project develops a generalized framework for evaluating higher-education Satisfactory Academic Progress (SAP) outcomes across quantitative criteria, exception states, academic plans, and workflow decisions.

The framework considers the principal SAP dimensions of:

* cumulative GPA
* pace of progression
* Maximum Timeframe
* warning eligibility
* appeals
* probation
* academic plans
* continuation
* noncompliance
* review
* disqualification

An anonymized real-world Maximum Timeframe scenario is used as the primary case because it illustrates a broader systems-design problem: a student may correctly fail a quantitative SAP criterion while simultaneously having an approved exception or compliance state that should affect the resulting workflow.

The case study does not attempt to reconstruct or represent any institution's proprietary system architecture, source code, internal procedures, or actual automation logic. Instead, the observed outcome is used as the basis for a conceptual systems-analysis and governance exercise.

The project distinguishes between:

* **Observed facts** — outcomes and statuses visible to the affected user
* **Known policy conditions** — documented SAP requirements and approved exception states
* **Root-cause hypotheses** — plausible data, integration, timing, state-management, or workflow-control failures
* **Proposed controls and future-state design** — conceptual improvements intended to support more complete and defensible eligibility decisions

All institutional and student-identifying information is excluded or anonymized.

## Executive Summary

Satisfactory Academic Progress systems typically evaluate multiple quantitative criteria, including cumulative GPA, pace of progression, and Maximum Timeframe. These calculations are necessary for determining whether a student satisfies SAP requirements, but they do not always provide enough information to determine the correct business-process outcome.

A student may fail one or more quantitative SAP criteria while simultaneously having conditions that affect how the failure should be processed, including:

* eligibility for a warning period
* an approved appeal
* SAP probation
* an active academic plan
* successful prior-term compliance
* an approved course substitution
* unresolved or conflicting academic data
* late grade or transfer-credit changes
* effective-date conditions that affect plan compliance

If the system treats the quantitative calculation as the final eligibility determination without evaluating these additional states, a technically correct SAP result can still contribute to an incomplete or inappropriate workflow decision.

This case study therefore separates SAP processing into three distinct layers:

1. **Quantitative SAP Result**
   Determines whether GPA, pace, and Maximum Timeframe criteria pass or fail.

2. **Exception and Compliance State**
   Evaluates warning eligibility, approved appeals, probation, academic plans, prior-term compliance, effective dates, enrollment conditions, and data completeness.

3. **Workflow Disposition**
   Determines whether the case should proceed as eligible, warning, probation, academic-plan continuation, review, appeal eligible, noncompliant, or disqualified.

The proposed future-state model preserves automation for routine deterministic calculations while limiting the authority of automation when approved exceptions, incomplete data, conflicting information, or other controlled conditions require additional evaluation.

## Primary Case Scenario

The generalized framework is anchored by the following anonymized Maximum Timeframe scenario:

1. A student exceeds the 150% Maximum Timeframe threshold.
2. The student completes the institution's SAP appeal process.
3. The Maximum Timeframe appeal is approved.
4. An academic plan is established to support continued progress toward degree completion.
5. The student successfully completes the subsequent academic term and remains compliant with the approved plan.
6. A later SAP evaluation again identifies the underlying mathematical Maximum Timeframe failure.
7. The resulting workflow returns the student to a generic disqualified status.
8. An immediately accessible continuation, remediation, or new appeal workflow is not available at the time of the adverse status.

The quantitative Maximum Timeframe result may be mathematically correct throughout this sequence.

The analytical question is therefore not:

> **Why did the system calculate a Maximum Timeframe failure?**

The more useful systems question is:

> **What additional exception, compliance, temporal, and data states should be evaluated before that calculation is converted into a final eligibility workflow decision?**

The observed outcome does not establish a specific technical cause. Possible explanations could include incomplete decision inputs, stale exception data, synchronization failure, incorrect effective-date handling, inadequate workflow-state modeling, or business rules that do not sufficiently distinguish calculation status from exception and eligibility status.

The event is therefore treated as an **operational anomaly requiring analysis**, rather than proof of a particular system defect.

## Generalized SAP Decision Model

The central design principle of this case study is that **SAP calculation results, exception states, and final workflow dispositions are related but distinct system concepts.**

A simplified SAP implementation might effectively behave as:

<img width="1448" height="1086" alt="Simplified Processing Model" src="https://github.com/user-attachments/assets/a7788a87-a714-4a1a-add0-0af964cf8bd8" />


That logic may be sufficient for some routine cases, but it becomes inadequate when additional policy or exception conditions exist.

A generalized decision process should instead evaluate:

<img width="1448" height="1086" alt="Proposed Decision Process" src="https://github.com/user-attachments/assets/a29e9b36-d806-44da-8542-ce40902ff2b6" />


This separation allows a quantitative failure to remain unchanged while the business workflow appropriately reflects an approved exception or another relevant state.

For example:

<img width="1448" height="1086" alt="MTF Scenario" src="https://github.com/user-attachments/assets/27971882-fb79-473b-a1ac-4131f66685ad" />


The system does not need to convert "Fail MTF" into a passing calculation. Instead, it needs to recognize that the calculation alone may not provide sufficient authority for automatic disqualification.

## Core Problem

The broader problem addressed by this case study is the risk of treating a quantitative SAP result as though it were equivalent to a final eligibility workflow state.

Different SAP conditions require different decision paths.

For example:

* a GPA or pace failure may qualify for an institutional warning period;
* a repeated GPA or pace failure may require appeal or probation;
* a Maximum Timeframe failure may require an approved exception to continue;
* an approved appeal may establish an academic plan spanning multiple terms;
* plan compliance may need to be evaluated independently of the original quantitative failure;
* missing or conflicting data may prevent a reliable automated determination;
* multiple simultaneous SAP failures may require different treatment than a single failed criterion.

A robust workflow therefore needs to evaluate more than:

<img width="1448" height="1086" alt="Workflow Evaluation" src="https://github.com/user-attachments/assets/ad2fb5cd-2446-46bb-89e1-2f8f7ffa5638" />

The central principle is:

> **The result of an automated SAP calculation should not automatically become the final student eligibility workflow status when relevant warning, exception, compliance, incomplete, conflicting, or temporally significant data exists.**

Where automation has sufficient, complete, and unambiguous information, deterministic processing should continue.

Where relevant exception or conflicting states exist, the system should route the case into a controlled workflow such as "Requires Review", rather than automatically issuing a final adverse determination.
