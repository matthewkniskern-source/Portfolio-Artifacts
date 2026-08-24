# Requirements Discovery

## Purpose

The current-state assessment identified where the existing service model breaks down.

Requirements discovery turns those findings into specific business and system expectations that can be designed, configured, tested, and traced.

The objective is not to collect a wish list.

A useful requirement should answer one of three questions:

* What business outcome must be achieved?
* What must the future platform or workflow be capable of doing?
* What quality, security, performance, or governance condition must the solution satisfy?

The requirements in this case are therefore separated into:

* **Business Requirements (BR)** — what the organization needs to achieve
* **Functional Requirements (FR)** — what the solution must do
* **Nonfunctional Requirements (NFR)** — how the solution must perform or be governed

The requirements are vendor-neutral and are intended to remain portable across modern Enterprise Service Management platforms.

---

# 1. Discovery Inputs

Requirements are derived from the findings established during the current-state phase.

Primary discovery inputs include:

* [Current-State Assessment](../01_CURRENT_STATE/01_current_state_assessment.md)
* [Stakeholder Map](../01_CURRENT_STATE/02_stakeholder_map.md)
* [Pain Points and Failure Modes](../01_CURRENT_STATE/03_pain_points_and_failure_modes.md)
* [Baseline Service Metrics](../01_CURRENT_STATE/04_baseline_metrics.md)

Additional inputs include:

* stakeholder interviews
* support-team workshops
* current forms and request channels
* existing ticket records
* approval practices
* escalation practices
* service ownership
* vendor-support processes
* reporting needs
* security and access-control expectations

The discovery process follows a simple rule:

> **A requirement should solve an identified business or operational need, not exist because the platform happens to support the feature.**

---

# 2. Discovery Objectives

The requirements phase is intended to establish enough detail to support:

* target operating-model design
* workflow configuration
* service-catalog design
* approval logic
* SLA configuration
* routing and escalation
* role-based access
* asset and CI relationships
* vendor workflow
* reporting
* automation
* AI-assisted capabilities
* testing
* implementation planning

The goal is not to define every field and screen before configuration begins.

The goal is to make the important operating decisions early enough that configuration does not become the place where unresolved business questions are quietly answered.

---

# 3. Stakeholder Discovery Approach

Different stakeholder groups contribute different types of requirements.

| Stakeholder               | Primary Discovery Focus                                |
| ------------------------- | ------------------------------------------------------ |
| End Users                 | Intake, usability, communication, status visibility    |
| Service Desk              | Classification, routing, priority, escalation, closure |
| Specialized Support Teams | Assignment, technical context, handoffs                |
| Service Owners            | Ownership, service expectations, approvals             |
| IT Management             | Performance, reporting, governance                     |
| Security / Risk           | Access, auditability, privileged actions               |
| Change Approvers          | Risk, authorization, validation, backout               |
| Asset / CI Owners         | Data relationships and ownership                       |
| Vendors                   | External support and access boundaries                 |
| HR / Identity             | User lifecycle and organizational data                 |
| Platform Administrators   | Configuration feasibility and maintainability          |
| Champions / Super-Users   | Adoption and usability                                 |

The detailed stakeholder model is maintained in:

[Stakeholder Map](../01_CURRENT_STATE/02_stakeholder_map.md)

---

# 4. Discovery Method

The discovery process uses four steps.

## Step 1 — Identify the Business Problem

Start with an observed problem or failure mode.

Example:

**FM-04 — Tickets are repeatedly reassigned because ownership is unclear.**

---

## Step 2 — Define the Business Need

Translate the problem into the outcome the organization needs.

Example:

**BR-04 — The organization shall establish clear ownership for managed service work throughout the ticket lifecycle.**

---

## Step 3 — Define Required System Behavior

Determine what the target solution must do to support that outcome.

Example:

**FR-08 — The platform shall assign each active ticket to a defined support group.**

**FR-09 — The platform shall record reassignment history and reassignment reason.**

---

## Step 4 — Define Validation

Determine how the requirement will later be tested.

Example:

**TC-INC-04 — Reassignment requires destination group and reason and retains previous ownership history.**

This establishes the traceability chain:

```text
Failure Mode
     ↓
Business Requirement
     ↓
Functional / Nonfunctional Requirement
     ↓
Workflow or Control
     ↓
Test Case
     ↓
Operational Metric
```

The completed cross-reference will be maintained in:

[Requirements Traceability Matrix](./05_requirements_traceability_matrix.md)

---

# 5. Business Requirements

Business requirements define what the organization needs the transformation to accomplish.

They intentionally avoid prescribing specific vendor features.

| ID    | Business Requirement                                                                                                                      | Source                          |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| BR-01 | The organization shall maintain an authoritative record for managed service activity.                                                     | FM-01, FM-15                    |
| BR-02 | The organization shall provide consistent intake for incidents and service requests across approved channels.                             | FM-01, FM-02                    |
| BR-03 | The organization shall prioritize service work using defined business-impact and urgency criteria.                                        | FM-03                           |
| BR-04 | The organization shall maintain clear ownership of active service work throughout its lifecycle.                                          | FM-04                           |
| BR-05 | The organization shall define measurable service-level expectations and escalation behavior.                                              | FM-05                           |
| BR-06 | The organization shall maintain auditable approval records for activities requiring authorization.                                        | FM-06, FM-07                    |
| BR-07 | The organization shall maintain appropriate separation between request, approval, and fulfillment for controlled activities.              | FM-07                           |
| BR-08 | Service records shall provide relevant relationships to users, services, assets, and configuration items.                                 | FM-08                           |
| BR-09 | The organization shall capture and reuse operational knowledge where it provides measurable support value.                                | FM-09                           |
| BR-10 | Changes shall be traceable to affected services, configuration items, implementation outcomes, and related incidents where applicable.    | FM-10                           |
| BR-11 | Vendor-supported work shall remain visible and accountable within the internal service process.                                           | FM-11                           |
| BR-12 | Vendor and temporary privileged access shall be time-bound and governed.                                                                  | FM-12                           |
| BR-13 | Closed service records shall contain sufficient information to support history, auditability, and future troubleshooting.                 | FM-13                           |
| BR-14 | The organization shall be capable of identifying recurring service issues and patterns.                                                   | FM-14                           |
| BR-15 | Management reporting shall be based on consistently captured and defined service-management data.                                         | FM-15                           |
| BR-16 | Automation shall support approved business rules and include defined exception handling.                                                  | FM-16                           |
| BR-17 | AI-assisted capabilities shall support human decision-making without independently executing restricted privileged or governance actions. | FM-16                           |
| BR-18 | The target service model shall support adoption, training, feedback, and continuous improvement after go-live.                            | Stakeholder / baseline findings |

Detailed business-requirement definitions are maintained in:

[Business Requirements](./02_business_requirements.md)

---

# 6. Functional Requirement Domains

Functional requirements will define platform behavior across the major process areas.

## 6.1 Intake and Record Creation

The solution must support:

* standardized ticket creation
* approved intake channels
* required fields
* request-type differentiation
* duplicate handling
* user association

---

## 6.2 Classification and Routing

The solution must support:

* category and subcategory
* service association
* support-group assignment
* routing rules
* reassignment history
* assignment exceptions

---

## 6.3 Priority and SLA

The solution must support:

* impact and urgency
* calculated priority
* response targets
* resolution / fulfillment targets
* SLA pause conditions
* warning thresholds
* breach escalation
* exception documentation

---

## 6.4 Approvals

The solution must support:

* approval routing
* multiple approval types
* recorded approval decisions
* approver identity
* approval timestamps
* rejection
* prohibited self-approval where required
* escalation for unanswered approval

---

## 6.5 Incident Management

The solution must support:

* incident lifecycle states
* ownership
* escalation
* major-incident handling
* duplicates
* related incidents
* affected services / CIs
* resolution
* reopen handling

Detailed workflow:

[Incident Management](../04_WORKFLOW_DESIGN/01_incident_management.md)

---

## 6.6 Service Request Management

The solution must support:

* catalog-based requests
* request-specific forms
* approvals
* fulfillment tasks
* request ownership
* service expectations
* completion confirmation

Detailed workflow:

[Service Request Management](../04_WORKFLOW_DESIGN/02_service_request_management.md)

---

## 6.7 Change Management

The solution must support:

* change classification
* risk evaluation
* approval
* scheduling
* implementation
* backout
* validation
* unsuccessful-change handling
* related incidents and CIs

Detailed workflow:

[Change Management](../04_WORKFLOW_DESIGN/03_change_management.md)

---

## 6.8 Knowledge Management

The solution must support:

* article creation
* review
* approval
* publication
* expiration / review date
* service association
* search
* ticket linkage
* retirement

Detailed workflow:

[Knowledge Management](../04_WORKFLOW_DESIGN/04_knowledge_management.md)

---

## 6.9 Vendor Management

The solution must support:

* vendor identification
* internal sponsorship
* support dependency tracking
* access expiration
* associated service / asset / CI
* vendor-related activity history

---

## 6.10 Reporting

The solution must support reporting for:

* ticket volume
* backlog
* SLA
* reassignment
* reopen
* repeat incidents
* knowledge reuse
* change success
* vendor dependency
* customer satisfaction
* aging
* service and support-group performance

Detailed metric definitions will be maintained in:

[Performance Framework](../11_METRICS_AND_OPTIMIZATION/01_performance_framework.md)

---

# 7. Initial Functional Requirements

The following requirements establish the first functional baseline.

| ID    | Functional Requirement                                                                                                        | Related BR   |
| ----- | ----------------------------------------------------------------------------------------------------------------------------- | ------------ |
| FR-01 | The platform shall create a unique service record for each managed incident or service request.                               | BR-01        |
| FR-02 | The platform shall support ticket creation through approved service channels.                                                 | BR-02        |
| FR-03 | The platform shall require defined minimum information before a ticket enters active fulfillment.                             | BR-02        |
| FR-04 | The platform shall support identification and association of duplicate or related incidents.                                  | BR-02, BR-14 |
| FR-05 | The platform shall calculate or guide priority using defined impact and urgency values.                                       | BR-03        |
| FR-06 | Authorized users shall be able to override calculated priority only with documented reason.                                   | BR-03        |
| FR-07 | Each active record shall have a defined owning support group.                                                                 | BR-04        |
| FR-08 | The platform shall maintain assignment and reassignment history.                                                              | BR-04        |
| FR-09 | Reassignment shall require a destination group and reassignment reason.                                                       | BR-04        |
| FR-10 | SLA timers shall begin, pause, resume, and stop based on defined workflow states.                                             | BR-05        |
| FR-11 | The platform shall generate warning and breach escalation actions based on defined SLA thresholds.                            | BR-05        |
| FR-12 | SLA exceptions shall require a documented exception reason.                                                                   | BR-05        |
| FR-13 | Approval-required requests shall not proceed beyond the defined approval gate without authorization.                          | BR-06        |
| FR-14 | Approval records shall include approver, decision, timestamp, and comments where required.                                    | BR-06        |
| FR-15 | The platform shall prevent self-approval for designated controlled request types.                                             | BR-07        |
| FR-16 | Service records shall support relationships to user, service, asset, and configuration item where applicable.                 | BR-08        |
| FR-17 | Service records shall support linkage to relevant knowledge articles.                                                         | BR-09        |
| FR-18 | Change records shall support relationships to affected services and configuration items.                                      | BR-10        |
| FR-19 | Change records shall support linkage to related incidents.                                                                    | BR-10        |
| FR-20 | Vendor-dependent work shall retain an accountable internal owner.                                                             | BR-11        |
| FR-21 | Vendor access records shall include sponsor, purpose, scope, start date, and expiration.                                      | BR-12        |
| FR-22 | The platform shall support automatic expiration or disablement of temporary vendor access where integrated capability exists. | BR-12        |
| FR-23 | Closure shall require defined resolution data based on record type.                                                           | BR-13        |
| FR-24 | The platform shall support trend reporting by category, service, CI, location, and time period.                               | BR-14        |
| FR-25 | Reporting shall distinguish active work, paused work, completed work, and approved exceptions.                                | BR-15        |
| FR-26 | Automated actions shall log execution status and exceptions.                                                                  | BR-16        |
| FR-27 | Failed automation shall route the record to a defined manual exception path.                                                  | BR-16        |
| FR-28 | AI-generated recommendations shall be distinguishable from human-entered decisions.                                           | BR-17        |
| FR-29 | AI-assisted categorization and routing shall support human correction.                                                        | BR-17        |
| FR-30 | AI functionality shall not independently approve privileged access, high-risk change, or other designated restricted actions. | BR-17        |

Detailed functional requirements will be maintained in:

[Functional Requirements](./03_functional_requirements.md)

---

# 8. Nonfunctional Requirement Domains

The target solution must also meet operational and governance expectations that are not tied to a single workflow function.

Key domains include:

* availability
* usability
* performance
* security
* auditability
* maintainability
* data retention
* accessibility
* integration
* scalability
* reporting performance
* recoverability

---

# 9. Initial Nonfunctional Requirements

| ID     | Nonfunctional Requirement                                                                                                           | Domain                       |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| NFR-01 | The solution shall enforce role-based access according to defined job responsibilities.                                             | Security                     |
| NFR-02 | Sensitive and privileged records shall be restricted to authorized roles.                                                           | Security                     |
| NFR-03 | Material record changes, approvals, access actions, and workflow transitions shall be auditable.                                    | Auditability                 |
| NFR-04 | Audit records shall identify actor, action, date/time, and affected record.                                                         | Auditability                 |
| NFR-05 | Standard end-user request submission shall be understandable without specialized service-management training.                       | Usability                    |
| NFR-06 | Core service workflows shall be maintainable without unnecessary custom development where standard configuration is sufficient.     | Maintainability              |
| NFR-07 | The solution shall support at least the current organization size and reasonable growth without redesign of the core service model. | Scalability                  |
| NFR-08 | Required service records shall follow organizational retention requirements.                                                        | Data Governance              |
| NFR-09 | Integration failures shall not silently discard service records or critical workflow events.                                        | Reliability                  |
| NFR-10 | Reporting shall use documented metric definitions and common status logic.                                                          | Reporting                    |
| NFR-11 | AI-assisted functions shall comply with defined data-handling and access restrictions.                                              | AI Governance                |
| NFR-12 | Configuration changes to production workflows shall follow controlled change and testing procedures.                                | Maintainability / Governance |

Detailed definitions:

[Nonfunctional Requirements](./04_nonfunctional_requirements.md)

---

# 10. Assumptions

The case study uses the following assumptions to maintain a realistic but disciplined scope.

| ID    | Assumption                                                                                                         |
| ----- | ------------------------------------------------------------------------------------------------------------------ |
| AS-01 | The organization has executive sponsorship for service-management transformation.                                  |
| AS-02 | A modern vendor-neutral ESM platform will be selected or is already available.                                     |
| AS-03 | Core user and organizational identity information is available from an authoritative source.                       |
| AS-04 | Support groups and service owners can be formally assigned.                                                        |
| AS-05 | Existing ticket and asset information can be assessed for migration or reference.                                  |
| AS-06 | Not every historical ticket must be migrated into the production platform.                                         |
| AS-07 | Selected business systems can provide integration capabilities where needed.                                       |
| AS-08 | Vendor access is technically capable of being time-limited through an integrated or supporting access process.     |
| AS-09 | The implementation will use configuration before custom development where practical.                               |
| AS-10 | The organization is willing to retire or constrain informal service channels where they undermine the new process. |

Assumptions should be validated during implementation and converted to risks or constraints when they prove incorrect.

---

# 11. Constraints

| ID    | Constraint                                                                                                                         |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------- |
| CN-01 | The implementation must remain vendor-neutral at the process-design level.                                                         |
| CN-02 | Business operations must continue during implementation and transition.                                                            |
| CN-03 | The organization cannot assume that existing ticket data is complete or consistently classified.                                   |
| CN-04 | Historical asset and configuration data may require cleanup before use.                                                            |
| CN-05 | Not every vendor can be provided direct access to the ESM platform.                                                                |
| CN-06 | Workflow standardization must not introduce excessive administrative burden for routine support work.                              |
| CN-07 | Security and approval controls may increase workflow steps for designated sensitive activities.                                    |
| CN-08 | Integration capability may vary across existing systems.                                                                           |
| CN-09 | Training must support users across multiple facilities and job functions.                                                          |
| CN-10 | The initial implementation should prioritize high-value workflows rather than attempt full enterprise process coverage at go-live. |

---

# 12. Out of Scope

To keep the implementation credible and manageable, the following areas are outside the core scope of this artifact:

* full ITIL implementation
* complete CMDB population
* enterprise project portfolio management
* full HR case management
* procurement-system replacement
* software-development lifecycle management
* complete identity-governance implementation
* custom AI model development
* autonomous AI approval
* detailed platform infrastructure design

Some of these areas may integrate with the target service model, but they are not being redesigned here.

This boundary matters.

A service-management implementation becomes difficult to control very quickly when every adjacent business process is treated as part of the initial transformation.

---

# 13. Requirement Prioritization

Requirements will be classified using three implementation priorities.

| Priority | Meaning                                                               |
| -------- | --------------------------------------------------------------------- |
| Must     | Required for initial operating model, control, or successful go-live  |
| Should   | High-value capability that may follow after core workflow stability   |
| Could    | Valuable optimization that is not required for initial implementation |

Priority will be based on:

* operational dependency
* control requirement
* user impact
* implementation complexity
* risk reduction
* measurable business value

Priority should not be based solely on which stakeholder argues hardest for a feature.

---

# 14. Requirement Quality Standard

Each requirement should be:

* specific
* testable
* traceable
* understandable
* vendor-neutral where practical
* tied to a business need
* limited to one primary behavior or condition

Requirements should avoid language such as:

* user friendly
* intelligent
* seamless
* best in class
* intuitive
* robust

unless the term is supported by measurable acceptance criteria.

A requirement that cannot be tested is usually not finished.

---

# 15. Requirement Validation

Requirements will be validated before configuration begins.

Validation should answer:

* Does this requirement solve a documented problem?
* Is the responsible stakeholder identified?
* Is the requirement clear enough to configure?
* Can it be tested?
* Does it conflict with another requirement?
* Does it create unnecessary operational overhead?
* Does it require a policy decision?
* Does it depend on an integration or data source?
* Is it actually a requirement, or simply a preferred implementation method?

Where disagreement exists, the issue should be resolved through defined decision authority rather than left to the platform administrator.

---

# 16. Traceability Model

The formal requirements matrix will maintain relationships across the transformation lifecycle.

Example:

| Source | Requirement   | Design            | Control                  | Test      | Metric                    |
| ------ | ------------- | ----------------- | ------------------------ | --------- | ------------------------- |
| FM-05  | BR-05         | SLA Model         | Automated Escalation     | TC-SLA-02 | SLA Compliance            |
| FM-07  | BR-07 / FR-15 | Approval Workflow | Self-Approval Prevention | TC-REQ-03 | Approval Exceptions       |
| FM-10  | BR-10 / FR-19 | Change Workflow   | Change/Incident Linkage  | TC-CHG-05 | Change Success Rate       |
| FM-12  | BR-12 / FR-21 | Vendor Workflow   | Access Expiration        | TC-VND-02 | Expired Access Exceptions |

The full model will be maintained in:

[Requirements Traceability Matrix](./05_requirements_traceability_matrix.md)

This becomes one of the primary quality checks for the artifact.

If a major requirement cannot be traced back to a business need, there is a good chance the solution is being over-designed.

If a major business need cannot be traced forward to a design and test, there is a good chance it has not actually been solved.

---

# 17. Requirements Discovery Deliverables

This phase produces five primary artifacts:

| Artifact                                                                     | Purpose                                                  |
| ---------------------------------------------------------------------------- | -------------------------------------------------------- |
| [Requirements Discovery](./01_requirements_discovery.md)                     | Defines the discovery and requirements methodology       |
| [Business Requirements](./02_business_requirements.md)                       | Defines required organizational outcomes                 |
| [Functional Requirements](./03_functional_requirements.md)                   | Defines solution behavior                                |
| [Nonfunctional Requirements](./04_nonfunctional_requirements.md)             | Defines quality, security, and operating conditions      |
| [Requirements Traceability Matrix](./05_requirements_traceability_matrix.md) | Connects current-state findings to design and validation |

Together, these documents establish the implementation baseline for the target operating model.

---

# 18. Requirements Discovery Conclusion

The current-state phase identified what is not working.

This phase defines what the organization needs instead.

That sounds simple, but this is where a large portion of implementation quality is determined.

If requirements are vague, platform configuration becomes guesswork.

If requirements are driven by features instead of business needs, the organization ends up automating whatever the software makes easy.

If requirements are clear and traceable, configuration becomes much more straightforward:

**Problem → Requirement → Design → Test → Outcome**

That is the standard this implementation will carry into the target service model.

**Next:** [Business Requirements](./02_business_requirements.md)

