# Executive Case Summary

## Case Classification

This artifact is an anonymized systems-analysis and GRC case study focused on Satisfactory Academic Progress (SAP) workflow governance in higher education.

The project develops a generalized SAP eligibility and exception-handling framework using a Maximum Timeframe appeal scenario as the primary case. The analysis is designed to demonstrate how quantitative eligibility calculations, exception states, academic-plan compliance, data quality, and workflow authority should interact within a controlled decision process.

The case study does not claim access to or knowledge of any institution's proprietary source code, architecture, configuration, or internal automation logic.

## Business Problem

SAP processing depends on quantitative measurements such as cumulative GPA, pace of progression, and Maximum Timeframe.

Those calculations are necessary, but a quantitative result alone may not always provide sufficient information to determine the correct eligibility workflow outcome.

A student may fail one SAP criterion while simultaneously having:

* warning eligibility
* an approved appeal
* SAP probation
* an active academic plan
* documented prior-term compliance
* approved academic-plan modifications
* unresolved grade or transfer-credit changes
* conflicting records between authoritative systems
* effective-date conditions that affect plan compliance

If these states are not incorporated into the decision process, a mathematically correct SAP result can still contribute to an incomplete or inappropriate workflow disposition.

The core business risk is not limited to incorrect calculation. A correct calculation can also create an incorrect workflow outcome when it is given more decision authority than the surrounding policy, exception, and compliance context supports.

## Primary Case Scenario

The case study is anchored by an anonymized Maximum Timeframe scenario:

1. A student exceeds the 150% Maximum Timeframe threshold.
2. The student completes the institution's SAP appeal process.
3. The Maximum Timeframe appeal is approved.
4. An academic plan is established for continued progress toward degree completion.
5. The student successfully completes the subsequent term and remains compliant with the approved plan.
6. A later SAP evaluation again identifies the underlying Maximum Timeframe failure.
7. The workflow returns the student to a generic disqualified status.
8. An immediately accessible continuation, remediation, or appeal pathway is not available at the time of the adverse status.

The quantitative result may remain correct throughout the entire sequence.

The systems-analysis question is whether the decision process evaluated sufficient exception, compliance, temporal, and data-state information before converting that quantitative result into a final workflow disposition.

## Analytical Finding

The case identifies a fundamental distinction between three different system concepts.

<img width="1448" height="1086" alt="Analytical Findings" src="https://github.com/user-attachments/assets/d62f142c-0d89-4e23-9bff-7f38ed9e0bf5" />


These layers are related, but they are not interchangeable.

A Maximum Timeframe calculation can properly remain failed while the workflow recognizes an approved exception and routes the case to additional review or academic-plan continuation.

**The redesign therefore treats SAP calculation outputs as decision inputs rather than universal final determinations.**

## Proposed Control Principle

The proposed control model preserves deterministic automation where the available data is complete, authoritative, and unambiguous.

Automation should be constrained when relevant exception, compliance, or conflicting information exists.

<img width="1448" height="1086" alt="Proposed Control Principle" src="https://github.com/user-attachments/assets/4bba0e9e-6930-4fcd-877d-5a3fc1dab49a" />


A representative control rule is:

**SAP Failure + Active Approved Exception + Confirmed Prior-Term Compliance → Requires Review, not automatic disqualification**

The reviewer then determines whether the applicable exception or academic plan remains valid.

## Governance and Risk Significance

The issue extends beyond financial-aid processing efficiency.

A poorly governed eligibility workflow can create several material risks:

<img width="1448" height="1086" alt="Governance and Risk" src="https://github.com/user-attachments/assets/56e49040-c387-40f6-af29-3ad5ce9e4134" />

Collectively, these risks demonstrate that SAP workflow governance is a balance between decision accuracy, automation efficiency, policy consistency, data integrity, and controlled human authority.

The future-state design therefore emphasizes both automation efficiency and controlled decision authority.

## Expected Benefits

The proposed framework is intended to improve the process in five areas.

<img width="1448" height="1086" alt="Expected Benefit" src="https://github.com/user-attachments/assets/13421bb7-1dc4-409e-8d14-6c7be8551fe3" />

These benefits depend on selective automation rather than maximum automation.

The objective is not to replace automation with manual processing.

The objective is to make automation more reliable by defining the conditions under which it may act conclusively.

## Scope Boundaries

This case study is intentionally limited to systems analysis, workflow governance, business rules, controls, data-state management, and decision design.

It does not:

* claim to reproduce any institution's actual SAP software
* infer a specific technical defect from a single observed outcome
* recommend that approved appeals override federal or institutional SAP requirements
* assume that every exception should result in continued eligibility
* eliminate professional judgment where policy requires review
* propose unrestricted manual override authority

The future-state model remains subordinate to applicable federal requirements and institutional SAP policy.

## Core Deliverables

The case study is organized around six primary portfolio artifacts:

<img width="1448" height="1086" alt="Core Deliverables" src="https://github.com/user-attachments/assets/2a1d926a-a583-4c7e-bf8b-c2b0bfd39f23" />


Supporting regulatory, policy, governance, data, and expanded risk analysis is maintained separately to keep the core case concise, navigable, and appropriate for an executive audience.

