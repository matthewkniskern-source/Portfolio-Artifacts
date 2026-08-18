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

[Executive Case Summary](core/01%20executive%20case%20summary.md)

[Current-State and Future-State Workflow](core/02%20current%20future%20workflow.md)

[State and Decision Model](core/03%20state%20and%20decision%20model.md)

[Decision and Edge-Case Matrix](core/04%20decision%20and%20edge%20case%20matrix.md)

[Risk-Control Matrix](core/05%20risk%20control%20matrix.md)

[Requirements and Testing](core/06%20requirments%20and%20testing.md)
