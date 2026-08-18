# Risk-Control Matrix

## Purpose

This artifact translates the SAP workflow weaknesses identified in the case study into defined risks, control objectives, and preventive, detective, and corrective controls.

The objective is not to eliminate all SAP processing risk or replace professional judgment with additional control layers.

The objective is to establish a controlled decision environment in which:

* routine determinations remain automated;
* approved exceptions are evaluated before adverse action;
* incomplete or conflicting information is detected;
* human review occurs only when necessary;
* overrides are governed and traceable; and
* final decisions can be reconstructed from authoritative data, policy, system rules, and reviewer actions.

The matrix treats SAP processing as both an eligibility workflow and a governed information system.

<img width="1491" height="1055" alt="05 RC Framework Overview" src="https://github.com/user-attachments/assets/eefbe29c-7b50-4a76-ae63-80111e40db66" />

## Control Model

The proposed framework uses three complementary control types.

### Preventive Controls

Preventive controls act before an incorrect or unsupported workflow disposition occurs.

They are intended to stop known control failures such as:

* bypassing an approved exception;
* assigning an adverse disposition from incomplete data;
* applying an exception to the wrong SAP criterion;
* processing against invalid effective dates; or
* permitting an unauthorized user to change a controlled state.

### Detective Controls

Detective controls identify conditions that preventive logic may not fully eliminate.

They are intended to identify:

* data synchronization failures;
* stale or conflicting records;
* unusually aged review cases;
* inconsistent outcomes;
* unauthorized or unusual overrides; and
* differences between expected and actual system behavior.

### Corrective Controls

Corrective controls restore the process to a valid state after an issue has been identified.

They may include:

* source-data correction;
* controlled reprocessing;
* disposition correction;
* authorized override;
* policy escalation; or
* remediation of a system or configuration defect.

A mature SAP control environment uses all three rather than relying primarily on manual remediation after an adverse decision has already occurred.

<img width="1448" height="1086" alt="05 Control Model" src="https://github.com/user-attachments/assets/2d162ff1-ab11-4b08-bc83-e1a721641ea5" />


## Risk Assessment Method

Risks are evaluated using two dimensions:

**Likelihood** — the probability that the condition could occur within the workflow.

**Impact** — the potential effect on eligibility, financial-aid processing, compliance, operations, auditability, or student service.

For the purposes of this case study, qualitative ratings are used:

* Low
* Moderate
* High
* Critical

The ratings are intended to prioritize control design within the conceptual model rather than represent measured institutional risk.

## Core Risk-Control Matrix

| Risk ID | Risk                                                        | Inherent Risk | Primary Control Objective                                                             | Key Controls                                                                             | Control Type            | Residual Risk |
| ------- | ----------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------- | ------------- |
| R-01    | False-positive disqualification                             | Critical      | Prevent unsupported adverse dispositions                                              | Exception validation, compliance checks, review-state routing                            | Preventive / Detective  | Moderate      |
| R-02    | False eligibility                                           | High          | Prevent continuation where SAP requirements or exception conditions are not satisfied | Criterion-level evaluation, confirmed noncompliance handling, exception-scope validation | Preventive              | Low–Moderate  |
| R-03    | Incomplete or stale decision data                           | High          | Ensure decisions use sufficiently complete and current information                    | Data-readiness checks, timestamps, stale-data detection                                  | Preventive / Detective  | Moderate      |
| R-04    | Cross-system synchronization failure                        | High          | Detect disagreement between decision-relevant systems                                 | Reconciliation controls, synchronization monitoring, conflict routing                    | Detective / Corrective  | Moderate      |
| R-05    | Effective-date or temporal error                            | High          | Apply records and rules to the correct evaluation period                              | Effective-date validation, temporal conflict state                                       | Preventive / Detective  | Low–Moderate  |
| R-06    | Approved exception bypassed                                 | Critical      | Ensure active exceptions are evaluated before adverse action                          | Exception lookup, criterion association, adverse-action suppression                      | Preventive              | Low           |
| R-07    | Academic-plan compliance misclassified                      | High          | Distinguish compliant, noncompliant, and unresolved plan status                       | Plan validation, compliance state model, reviewer routing                                | Preventive / Detective  | Moderate      |
| R-08    | Exception applied to wrong SAP criterion                    | High          | Limit exception effect to its authorized scope                                        | Criterion-level linkage and independent failure evaluation                               | Preventive              | Low           |
| R-09    | Unauthorized override or status change                      | High          | Restrict controlled state changes to authorized roles                                 | RBAC, approval controls, audit logging                                                   | Preventive / Detective  | Low–Moderate  |
| R-10    | Poor decision auditability                                  | High          | Preserve sufficient evidence to reconstruct each determination                        | Decision logs, rule versions, timestamps, reviewer records                               | Detective / Governance  | Low           |
| R-11    | Review queue backlog                                        | Moderate–High | Prevent legitimate review cases from becoming operational failures                    | Queue aging, escalation thresholds, workload monitoring                                  | Detective / Corrective  | Moderate      |
| R-12    | Inconsistent policy application                             | High          | Produce materially consistent decisions from materially equivalent inputs             | Version-controlled rules, decision testing, exception governance                         | Preventive / Detective  | Low–Moderate  |
| R-13    | Appeal or remediation pathway unavailable                   | High          | Ensure adverse outcomes connect to policy-authorized next actions                     | Workflow completeness validation, remediation-path monitoring                            | Preventive / Detective  | Low–Moderate  |
| R-14    | Configuration or rule change introduces unintended behavior | High          | Govern changes to eligibility logic and workflow states                               | Change approval, testing, versioning, rollback capability                                | Preventive / Corrective | Moderate      |
| R-15    | Excessive manual review                                     | Moderate      | Preserve automation efficiency while controlling ambiguity                            | Defined review triggers, deterministic rule processing, queue analytics                  | Preventive / Detective  | Low–Moderate  |

<img width="1536" height="1024" alt="05 Core Risk Landscape" src="https://github.com/user-attachments/assets/d8bc3ab9-df3b-42e6-98ae-e718e0e5c2b3" />

## R-01 — False-Positive Disqualification

### Risk Statement

A student may receive an adverse SAP disposition even though an applicable warning, approved exception, compliant academic plan, unresolved data issue, or other controlling condition should prevent automatic adverse action.

### Potential Impact

* delayed or interrupted financial aid;
* unnecessary appeal or administrative workload;
* inconsistent policy application;
* student-service impact;
* increased remediation effort;
* reputational risk; and
* difficulty defending the determination during review.

### Control Objective

Prevent a quantitative SAP failure from becoming a final adverse disposition until all applicable exception, compliance, and data-readiness conditions have been evaluated.

### Preventive Controls

* evaluate active exceptions before adverse action;
* validate academic-plan state and compliance;
* validate effective dates;
* suppress automatic adverse disposition when a review condition exists.

### Detective Controls

* identify adverse dispositions involving active exceptions;
* reconcile disqualification records against approved appeal and academic-plan records;
* monitor disposition reversals and post-processing corrections.

### Corrective Controls

* route identified cases for authorized review;
* correct source data where necessary;
* reprocess the determination;
* preserve both original and corrected decision records.

### Control Evidence

Evidence may include:

* decision logs;
* exception-state records;
* academic-plan compliance records;
* review-queue records;
* reprocessing history; and
* disposition-change logs.

## R-02 — False Eligibility

### Risk Statement

A student may remain eligible when applicable SAP requirements, probation terms, or academic-plan conditions are not satisfied.

This risk is the inverse of false-positive disqualification and must be controlled with equal discipline.

### Control Objective

Ensure that approved exceptions permit continuation only within their authorized scope and conditions.

### Key Controls

* maintain quantitative failures independently;
* link exceptions to the criteria they address;
* validate probation and academic-plan conditions;
* treat confirmed noncompliance as an enforceable state;
* prevent an exception for one criterion from automatically resolving another failure.

### Control Evidence

* criterion-level results;
* exception-scope records;
* compliance determination;
* final disposition;
* policy or rule version.

## R-03 — Incomplete or Stale Decision Data

### Risk Statement

The workflow may issue a determination before required academic, enrollment, appeal, plan, or compliance information is complete or current.

### Control Objective

Permit conclusive automation only when required decision inputs meet defined readiness standards.

### Key Controls

* source-data timestamps;
* completeness checks;
* stale-record thresholds;
* required-field validation;
* Requires Review routing when decision-critical information is unresolved.

<img width="1448" height="1086" alt="05 Decision Readiness Control Gate" src="https://github.com/user-attachments/assets/ba058209-ac1e-4a91-abdb-5c252590061b" />

## R-04 — Cross-System Synchronization Failure

### Risk Statement

Decision-relevant systems may contain different versions of the same student, plan, appeal, enrollment, or degree-applicability state.

### Control Objective

Detect material disagreement before it affects eligibility disposition.

### Key Controls

* scheduled or event-driven reconciliation;
* authoritative-source designation;
* synchronization monitoring;
* data-conflict state;
* controlled resolution and reprocessing.

### Representative Systems

The conceptual workflow may depend on data from:

* financial-aid systems;
* student information systems;
* academic advising;
* degree audit;
* registration;
* grading; and
* transfer-credit processing.

The project does not assume a specific institutional architecture.

## R-05 — Effective-Date and Temporal Error

### Risk Statement

A correct record may be applied to the wrong decision period because enrollment, appeal approval, academic-plan approval, grade changes, or program changes occurred at different times.

### Control Objective

Ensure that each decision uses the version of the record and rule applicable to the relevant evaluation period.

### Key Controls

* effective-date validation;
* record-version history;
* temporal conflict detection;
* decision-date logging;
* review routing where date relationships cannot be resolved automatically.

## R-06 — Approved Exception Bypassed

### Risk Statement

A valid approved appeal, probation state, or academic plan may not be evaluated before the underlying SAP failure is converted into an adverse disposition.

### Control Objective

Make exception-state evaluation a mandatory control gate before adverse action.

### Key Controls

* active-exception lookup;
* criterion-level exception association;
* effective-period validation;
* adverse-action suppression;
* reconciliation of adverse cases against approved exceptions.

<img width="1448" height="1086" alt="05 Exception Control Gate" src="https://github.com/user-attachments/assets/5dcb7ded-a90f-4326-992e-40d55fd3b176" />

## R-07 — Academic-Plan Compliance Misclassification

### Risk Statement

The workflow may treat the existence of an academic plan as automatic compliance, or conversely treat unresolved plan information as confirmed noncompliance.

### Control Objective

Maintain explicit distinction among:

* Plan Compliant
* Plan Noncompliant
* Plan Compliance Unknown

### Key Controls

* plan-version validation;
* milestone or requirement validation;
* approved-substitution recognition;
* compliance evidence;
* controlled review where compliance cannot be determined.

## R-08 — Exception Scope Error

### Risk Statement

An approved exception may be applied beyond the SAP criterion it was intended to address.

For example, a Maximum Timeframe appeal should not automatically resolve an unrelated GPA or pace failure unless the governing policy explicitly permits that result.

### Control Objective

Preserve criterion-level decision logic throughout the workflow.

### Key Controls

* criterion-specific exception linkage;
* independent evaluation of simultaneous failures;
* exception-scope validation;
* multi-criterion decision testing.

## R-09 — Unauthorized Override or State Change

### Risk Statement

An unauthorized or insufficiently governed user may alter eligibility, exception, compliance, or final disposition states.

### Control Objective

Ensure controlled workflow states can be changed only by authorized roles and that material changes remain traceable.

### Preventive Controls

* role-based access;
* least privilege;
* defined override authority;
* segregation of duties for sensitive changes.

### Detective Controls

* override logging;
* privileged-action monitoring;
* periodic access review;
* unusual-change reporting.

### Corrective Controls

* revoke inappropriate access;
* reverse unauthorized changes;
* investigate affected determinations;
* reprocess impacted cases where necessary.

<img width="1536" height="1024" alt="05 RBAC" src="https://github.com/user-attachments/assets/5dfb6a3d-86f2-4982-bcbb-200a9feaa810" />


## R-10 — Poor Decision Auditability

### Risk Statement

The institution may be unable to reconstruct why a specific SAP disposition occurred.

### Control Objective

Preserve a complete relationship between the data evaluated, the rules applied, exceptions considered, reviewer actions, and final disposition.

### Required Evidence

A decision record should retain:

* quantitative SAP results;
* applicable exception or appeal;
* academic-plan identifier and version;
* compliance state;
* source-data timestamps;
* rule or policy version;
* workflow disposition;
* reviewer or override action;
* final decision timestamp.

Auditability is treated as a system requirement rather than an after-the-fact reporting function.

## R-11 — Review Queue Backlog

### Risk Statement

A correctly designed review state may still create harm if cases remain unresolved long enough to delay downstream aid processing.

### Control Objective

Ensure human-in-the-loop controls remain operationally sustainable.

### Key Controls

* queue aging;
* priority classification;
* escalation thresholds;
* workload monitoring;
* downstream-dependency indicators;
* service-level reporting.

A Requires Review state is only effective if the associated review process is itself governed.

## R-12 — Inconsistent Policy Application

### Risk Statement

Materially equivalent cases may receive different outcomes because of inconsistent configuration, undocumented manual interpretation, or rule-version differences.

### Control Objective

Ensure materially equivalent inputs produce materially equivalent outcomes unless an authorized and documented difference justifies the variation.

### Key Controls

* version-controlled business rules;
* approved policy mapping;
* regression testing;
* decision consistency testing;
* documented professional judgment.

## R-13 — Missing Remediation Path

### Risk Statement

A student may receive an adverse disposition without access to an appeal, remediation, continuation, or administrative process that applicable policy makes available.

### Control Objective

Ensure terminal and adverse workflow states have valid next-action logic.

### Key Controls

* remediation-path validation;
* workflow completeness testing;
* appeal availability monitoring;
* exception for unavailable workflow functionality;
* escalation to administrative review.

## R-14 — Configuration and Change Risk

### Risk Statement

A change to SAP thresholds, decision rules, exception logic, workflow configuration, integration mappings, or state transitions may unintentionally alter eligibility outcomes.

### Control Objective

Prevent untested or unauthorized changes from affecting production eligibility decisions.

### Preventive Controls

* documented change request;
* impact assessment;
* approval authority;
* test environment validation;
* requirements traceability.

### Detective Controls

* post-deployment validation;
* exception-rate monitoring;
* disposition trend monitoring;
* regression testing.

### Corrective Controls

* rollback capability;
* configuration restoration;
* affected-case identification;
* controlled reprocessing.

<img width="1536" height="1024" alt="05 SAP Change Control LC" src="https://github.com/user-attachments/assets/7bd1cc9f-72a5-4cab-8b6a-948d866b5f29" />


## R-15 — Excessive Manual Review

### Risk Statement

An overly conservative control design may route too many deterministic cases to human reviewers, reducing the operational value of automation.

### Control Objective

Reserve human review for cases in which automation genuinely lacks sufficient information or authority.

### Key Controls

* explicit review triggers;
* deterministic routing where rules are conclusive;
* review-reason classification;
* queue-volume monitoring;
* periodic analysis of avoidable review cases.

The control objective is not maximum human involvement.

It is **appropriate human involvement**.

## Control Ownership

Controls should have clearly assigned ownership.

Representative ownership domains include:

### Financial Aid

* SAP policy implementation;
* appeal and exception decisions;
* final eligibility authority;
* review disposition.

### Academic Advising

* academic-plan development;
* approved plan modifications;
* plan-related academic context.

### Registrar / Academic Records

* enrollment;
* grade records;
* program status;
* applicable academic-record corrections.

### Information Technology

* system integration;
* workflow configuration;
* access control;
* logging;
* change deployment;
* technical reconciliation.

### Governance / Compliance

* policy-control alignment;
* control testing;
* access review;
* audit support;
* exception governance.

Actual ownership should follow the institution's governance structure.

<img width="1536" height="1024" alt="05 Control Ownership Model" src="https://github.com/user-attachments/assets/a5216dbe-968e-4e55-97a8-a29755a9068a" />

## Segregation of Duties

Sensitive decisions should not rely on unrestricted authority concentrated in a single role.

The conceptual model separates:

* source-data maintenance;
* academic-plan approval;
* appeal determination;
* system configuration;
* manual override authority;
* control monitoring.

Segregation of duties reduces the risk that one user can both create a decision condition and independently approve the resulting exception or override without oversight.

Where staffing limitations require combined roles, compensating controls should be defined.

## Access-Control Principles

Access to SAP workflow functions should follow:

* least privilege;
* role-based access;
* need-to-know;
* controlled administrative access;
* periodic entitlement review;
* separation between standard processing and privileged override functions.

Sensitive student information should be exposed only to roles that require it for authorized functions.

Detailed privacy and access-governance requirements are maintained in the supporting governance artifact.

## Control Evidence and Audit Trail

Controls are useful only when their operation can be demonstrated.

Representative control evidence includes:

* automated decision logs;
* reconciliation reports;
* exception records;
* review-queue history;
* access logs;
* override records;
* rule-version history;
* change approvals;
* test results;
* reprocessing records.

Evidence should be retained according to applicable institutional recordkeeping requirements.

## Monitoring Indicators

Operational monitoring can identify whether the control environment is functioning as intended.

Potential indicators include:

* percentage of SAP failures routed to review;
* percentage of reviewed cases resulting in disposition change;
* adverse determinations involving active exceptions;
* exception cases missing academic-plan data;
* number of data conflicts detected;
* review-queue age;
* override volume;
* corrected or reprocessed determinations;
* inconsistent outcomes identified through control testing.

These measures can reveal both under-control and over-control conditions.

<img width="1536" height="1024" alt="05 RC Dashboard" src="https://github.com/user-attachments/assets/b819f099-5d69-4d6b-9c83-452a23047de2" />

## Key Risk Indicators

KRIs should identify increasing exposure before control failure becomes widespread.

Potential KRIs include:

* rising reconciliation-error rate;
* increased stale-data detections;
* growth in review backlog;
* increase in manual overrides;
* increase in post-decision reversals;
* increase in exception records lacking required supporting data;
* repeated failures following system or rule changes.

## Key Performance Indicators

KPIs should measure whether the redesigned workflow delivers efficient and reliable processing.

Potential KPIs include:

* percentage of deterministic cases processed automatically;
* median review resolution time;
* percentage of review cases resolved within target time;
* reduction in avoidable adverse reversals;
* reduction in manual intervention for routine cases;
* percentage of decisions with complete audit evidence.

The objective is to improve both **decision quality** and **operational efficiency**.

## Control Testing

Controls should be tested using the decision and edge-case scenarios defined in the preceding artifact.

Testing should verify that:

* preventive controls block unsupported dispositions;
* detective controls identify conflicts and synchronization failures;
* corrective controls support controlled remediation;
* controls do not suppress valid adverse action;
* review routing occurs only when defined conditions exist;
* privileged actions remain traceable.

Control failure should generate a defined remediation action rather than merely being documented.

## Residual Risk

No workflow can eliminate all SAP processing risk.

Residual risk may remain because of:

* professional judgment;
* delayed source information;
* external dependencies;
* policy ambiguity;
* human error;
* integration latency;
* operational workload.

The purpose of the control framework is to reduce those risks to a level consistent with institutional policy, compliance obligations, operational capability, and defined risk tolerance.

## Control Design Principles

The proposed control environment follows several principles:

* automation should remain authoritative for deterministic calculations;
* automated adverse action requires complete decision context;
* exceptions should be evaluated before adverse disposition;
* confirmed noncompliance must remain enforceable;
* uncertainty must be represented explicitly;
* human review must have defined triggers and authority;
* overrides must be restricted and logged;
* policy and configuration changes must be governed;
* material decisions must be reconstructable;
* controls must balance accuracy with operational efficiency.

## Key Takeaway

The purpose of the risk-control model is not to create friction around SAP processing.

It is to ensure that the level of control matches the consequence of the decision.

**Prevent where possible. Detect what cannot be fully prevented. Correct what is identified. Preserve evidence throughout.**

The redesigned workflow therefore treats SAP automation as a governed decision system rather than only a calculation process.

<img width="1536" height="1024" alt="RC Matrix Summary" src="https://github.com/user-attachments/assets/f1eb2ba7-9197-4e64-83b7-8149bb881401" />
