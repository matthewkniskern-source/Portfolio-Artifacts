# Stakeholder Map

## Purpose

The service-management environment touches more than the service desk.

A successful implementation depends on understanding who requests service, who delivers it, who approves it, who owns the underlying business services, who provides external support, and who ultimately measures whether the new operating model is working.

This stakeholder map identifies the major groups involved in the transformation and defines their role in discovery, design, approval, testing, adoption, and ongoing governance.

The intent is not to document every individual in the organization. It is to identify the stakeholder groups that materially influence how the service-management model should operate.

---

# 1. Stakeholder Overview

| Stakeholder Group                            | Primary Role                                        | Key Need                                            | Decision Authority             | Implementation Influence |
| -------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | ------------------------------ | ------------------------ |
| End Users                                    | Consume services and request support                | Simple, predictable service experience              | Low                            | High adoption impact     |
| Service Desk                                 | Primary intake and first-line support               | Clear intake, routing, ownership, and escalation    | Moderate operational authority | Very high                |
| Specialized Support Teams                    | Resolve escalated or technical work                 | Accurate assignment and usable context              | Moderate                       | Very high                |
| Service / Business-System Owners             | Accountable for specific services or applications   | Visibility, service performance, approval control   | High within owned service      | High                     |
| IT Management                                | Own service-delivery performance                    | Reliable reporting, workload visibility, governance | High                           | Very high                |
| Change Approvers                             | Authorize changes based on risk and business impact | Complete change information and traceable decisions | High                           | High                     |
| Security / Risk / Compliance                 | Define security and control expectations            | Access control, auditability, risk visibility       | High for controlled activities | High                     |
| Asset / Configuration Owners                 | Maintain asset and CI accuracy                      | Reliable relationships between work and technology  | Moderate                       | Medium                   |
| External Vendors                             | Provide specialized support                         | Controlled access and clear work context            | Limited                        | Medium                   |
| HR / Identity Administration                 | Support user lifecycle and access dependencies      | Accurate user status and lifecycle integration      | Moderate                       | Medium                   |
| Executive Sponsors                           | Sponsor transformation and remove barriers          | Business outcomes and measurable improvement        | Very high                      | High                     |
| Platform / Service Management Administrators | Configure and maintain the ESM platform             | Stable requirements and controlled configuration    | High technical authority       | Very high                |
| Champions / Super-Users                      | Support local adoption and feedback                 | Usable processes and early visibility               | Low formal authority           | High adoption impact     |

---

# 2. Stakeholder Detail

## 2.1 End Users

### Role

End users are the primary consumers of supported business and technology services.

They initiate:

* incidents
* service requests
* access requests
* equipment requests
* support questions

Their interaction with the service-management environment should be simple enough that the formal process does not encourage users to bypass it.

### Current-State Concerns

* unclear where requests should be submitted
* inconsistent response depending on contact method
* limited visibility into status
* repeated requests for the same information
* uncertainty about expected completion time
* escalation through direct contact when progress is unclear

### Target-State Needs

* clear service entry points
* understandable catalog options
* confirmation that work was received
* visible request status
* reasonable status communication
* predictable service expectations
* simple closure and feedback process

### Discovery Contribution

End-user discovery should focus on:

* how users currently seek help
* why they bypass formal channels
* which request types cause the most frustration
* what information they expect after submission
* which terminology is understandable to nontechnical users

### Adoption Risk

**High.**

If the target platform is harder to use than email, chat, or direct technician contact, users will continue using informal channels.

The implementation must therefore improve control **without making routine service access unnecessarily difficult**.

Related design:

* [Service Catalog](../03_TARGET_SERVICE_MODEL/02_service_catalog.md)
* [Service Request Workflow](../04_WORKFLOW_DESIGN/02_service_request_management.md)
* [Adoption Strategy](../10_ADOPTION_AND_TRAINING/01_adoption_strategy.md)

---

# 2.2 Service Desk

### Role

The service desk serves as the primary managed intake point for incidents and general service requests.

Typical responsibilities include:

* ticket review
* initial classification
* troubleshooting
* assignment
* communication
* escalation
* closure validation

### Current-State Concerns

* incomplete request information
* excessive manual categorization
* unclear ownership boundaries
* frequent reassignment
* informal requests arriving outside the queue
* inconsistent escalation
* duplicated tickets during larger incidents

### Target-State Needs

* standardized intake
* routing support
* clear category structure
* priority guidance
* visible SLA timers
* escalation rules
* useful asset and CI context
* reusable knowledge
* clear closure requirements

### Decision Authority

Moderate.

The service desk should help shape operational workflow rules, but should not unilaterally define:

* service ownership
* privileged approvals
* security controls
* enterprise SLA commitments
* change authorization policy

### Discovery Contribution

The service desk is one of the most important discovery sources because it experiences process weaknesses repeatedly and at volume.

Workshops should focus on:

* common ticket types
* poor-quality intake
* reassignment causes
* escalation behavior
* recurring issues
* missing knowledge
* current workaround processes

### Adoption Risk

**Very High.**

If the workflow adds unnecessary administrative effort to frontline support, technicians are likely to create workarounds.

Related design:

* [Incident Management Workflow](../04_WORKFLOW_DESIGN/01_incident_management.md)
* [Priority and SLA Model](../03_TARGET_SERVICE_MODEL/03_priority_and_sla_model.md)
* [Knowledge Management Workflow](../04_WORKFLOW_DESIGN/04_knowledge_management.md)

---

# 2.3 Specialized Support Teams

### Role

Specialized support teams resolve work requiring deeper technical ownership.

Representative groups may include:

* infrastructure
* network
* endpoint
* systems administration
* application support
* identity and access management

### Current-State Concerns

* incorrectly assigned work
* incomplete technical context
* repeated troubleshooting
* weak handoffs
* direct requests bypassing the service desk
* poor visibility into prior incidents and recent changes

### Target-State Needs

* accurate assignment
* required diagnostic information
* ownership clarity
* service and CI context
* prior incident history
* related change visibility
* escalation support
* reusable knowledge

### Decision Authority

Moderate within their technical domain.

Technical teams should influence:

* assignment criteria
* escalation paths
* technical intake requirements
* closure data
* change implementation procedures

### Adoption Risk

**High.**

Teams that already maintain effective informal workflows may resist additional structure if they view the platform as administrative overhead.

The implementation should demonstrate that better records reduce repeated troubleshooting and poor handoffs rather than simply creating more fields to complete.

Related design:

* [Ownership and Escalation Model](../03_TARGET_SERVICE_MODEL/04_ownership_and_escalation.md)
* [Service Management Data Model](../05_DATA_AND_CONFIGURATION_MODEL/01_service_management_data_model.md)

---

# 2.4 Service and Business-System Owners

### Role

Service owners are accountable for the business or technical services delivered through the organization.

Examples may include owners of:

* enterprise applications
* collaboration services
* network services
* identity services
* line-of-business systems

### Current-State Concerns

* limited service-level visibility
* unclear escalation expectations
* inconsistent change notification
* weak connection between incidents and affected services
* limited trend information

### Target-State Needs

* defined service ownership
* service-level performance reporting
* change visibility
* major incident escalation
* approval authority where applicable
* clear service dependencies

### Decision Authority

**High within the owned service.**

Service owners may authorize or influence:

* service expectations
* escalation paths
* maintenance windows
* service-specific request approvals
* change risk acceptance

### Discovery Contribution

Service owners should help define:

* what the service is
* who depends on it
* acceptable service interruption
* required approvals
* critical dependencies
* escalation expectations

Related design:

* [Target Operating Model](../03_TARGET_SERVICE_MODEL/01_target_operating_model.md)
* [Service Catalog](../03_TARGET_SERVICE_MODEL/02_service_catalog.md)

---

# 2.5 IT Management

### Role

IT management is responsible for overall service-delivery performance, staffing, prioritization, and governance.

### Current-State Concerns

* unreliable workload data
* limited SLA visibility
* incomplete reporting
* difficulty identifying recurring problems
* unclear accountability
* inability to distinguish true performance problems from incomplete records

### Target-State Needs

* reliable operational reporting
* backlog visibility
* SLA performance
* aging analysis
* workload by group
* reassignment trends
* recurring incident trends
* change performance
* adoption indicators

### Decision Authority

**High.**

Management provides authority for:

* operating-model changes
* service ownership
* escalation policy
* resource prioritization
* implementation sequencing

### Discovery Contribution

Management should establish expected business outcomes while avoiding over-designing operational workflows without technician input.

Related design:

* [Metrics and Continuous Improvement](../11_METRICS_AND_OPTIMIZATION/01_performance_framework.md)
* [Implementation Plan](../08_IMPLEMENTATION_PLAN/01_implementation_plan.md)

---

# 2.6 Change Approvers

### Role

Change approvers evaluate whether proposed changes should proceed based on:

* risk
* impact
* timing
* technical readiness
* business requirements

Depending on the change, approval authority may include:

* technical leads
* service owners
* management
* security
* business stakeholders

### Current-State Concerns

* approvals occurring in email or chat
* incomplete change information
* unclear approval authority
* poor record of why a change was accepted
* inconsistent post-change validation

### Target-State Needs

* risk-based approval routing
* documented decisions
* separation of request and approval where appropriate
* implementation plans
* validation criteria
* backout plans
* change history

### Decision Authority

**High for applicable changes.**

Related design:

* [Change Management Workflow](../04_WORKFLOW_DESIGN/03_change_management.md)
* [Governance Model](../06_GOVERNANCE_AND_CONTROLS/01_governance_model.md)

---

# 2.7 Security, Risk, and Compliance

### Role

This group ensures that service-management workflows appropriately support security, privacy, risk, and audit requirements.

The goal is not to turn routine service delivery into a compliance exercise. Security involvement should be concentrated where risk justifies it.

### Current-State Concerns

* inconsistent privileged approvals
* weak vendor access expiration
* incomplete approval evidence
* limited access review
* poor audit history for sensitive actions

### Target-State Needs

* RBAC
* controlled privileged requests
* approval separation
* audit logging
* vendor expiration
* periodic access review
* defined exception handling

### Decision Authority

**High for security-controlled activities.**

### Discovery Contribution

Security should help identify which workflows require explicit controls and which routine processes do not.

Related design:

* [RBAC and Approval Controls](../06_GOVERNANCE_AND_CONTROLS/02_rbac_and_approval_controls.md)
* [Control Matrix](../06_GOVERNANCE_AND_CONTROLS/03_control_matrix.md)

---

# 2.8 Asset and Configuration Owners

### Role

These stakeholders maintain or validate information about:

* hardware
* software
* applications
* infrastructure
* configuration items
* technical relationships

### Current-State Concerns

* incomplete asset linkage
* inaccurate or stale ownership
* weak service dependency visibility
* limited incident/change relationship data

### Target-State Needs

* consistent asset association
* CI ownership
* service relationships
* change history
* support-group relationships
* lifecycle status

### Decision Authority

Moderate.

They influence how asset and CI records are structured and maintained but do not generally control service workflows.

Related design:

* [Service Management Data Model](../05_DATA_AND_CONFIGURATION_MODEL/01_service_management_data_model.md)
* [Data Governance](../05_DATA_AND_CONFIGURATION_MODEL/03_data_governance.md)

---

# 2.9 External Vendors

### Role

Vendors provide support for selected systems, products, infrastructure, and specialized services.

### Current-State Concerns

* vendor activity may occur outside the primary service record
* unclear ownership while waiting on vendor support
* access may outlive the original support need
* vendor communication may not be visible to internal stakeholders

### Target-State Needs

* vendor relationship recorded
* access tied to defined purpose
* expiration date
* responsible internal sponsor
* activity logging
* clear ownership while vendor support is active

### Decision Authority

Limited.

Vendors may recommend technical actions but should not independently authorize internal changes or privileged access.

### Adoption / Control Risk

**Medium to High.**

Vendor workflows must remain practical enough to support troubleshooting while preserving internal accountability.

Related design:

* [Governance and Controls](../06_GOVERNANCE_AND_CONTROLS/01_governance_model.md)
* [Automation Opportunities](../07_AUTOMATION_AND_AI/01_automation_opportunities.md)

---

# 2.10 HR and Identity Administration

### Role

HR and identity administration provide authoritative information related to:

* employee lifecycle
* organizational assignment
* manager relationships
* status changes
* access dependencies

### Current-State Concerns

* manual lifecycle notifications
* inconsistent account expiration
* delayed updates to organizational relationships

### Target-State Needs

Where technically and organizationally feasible:

* authoritative user status
* current manager relationship
* automated routing based on organization
* lifecycle-triggered access actions
* predictable termination or expiration handling

### Decision Authority

Moderate within user lifecycle processes.

Related design:

* [Automation Opportunities](../07_AUTOMATION_AND_AI/01_automation_opportunities.md)
* [Service Management Data Model](../05_DATA_AND_CONFIGURATION_MODEL/01_service_management_data_model.md)

---

# 2.11 Executive Sponsor

### Role

The executive sponsor provides organizational authority for the transformation.

The sponsor is not responsible for designing ticket fields or workflow states.

Their role is to:

* establish the business priority
* resolve cross-functional barriers
* support adoption expectations
* approve major scope or funding decisions
* hold leadership accountable for implementation outcomes

### Target-State Need

The sponsor needs concise evidence that the transformation is improving service delivery.

That means reporting should emphasize outcomes rather than simply platform activity.

### Decision Authority

**Very High.**

Related design:

* [Implementation Plan](../08_IMPLEMENTATION_PLAN/01_implementation_plan.md)
* [Performance Framework](../11_METRICS_AND_OPTIMIZATION/01_performance_framework.md)

---

# 2.12 Platform / Service Management Administrators

### Role

Platform administrators translate approved requirements into system configuration.

Typical responsibilities include:

* forms
* fields
* workflow states
* routing rules
* notifications
* SLA configuration
* access roles
* reports
* automation

### Current-State Concern

In poorly governed implementations, administrators can become responsible for resolving business-process ambiguity through configuration.

That should be avoided.

The platform team should configure **approved business rules**, not invent them because requirements were never settled.

### Target-State Needs

* stable requirements
* approved workflow designs
* configuration standards
* controlled change process
* testing criteria
* configuration documentation

### Decision Authority

High technical authority, but limited authority to redefine business policy independently.

Related design:

* [Requirements Traceability Matrix](../02_REQUIREMENTS_DISCOVERY/05_requirements_traceability_matrix.md)
* [Testing and UAT](../09_TESTING_AND_UAT/01_test_strategy.md)

---

# 2.13 Champions / Super-Users

### Role

Champions are selected personnel who receive early exposure to the new model and help reinforce adoption within their teams.

They may provide:

* pilot feedback
* local support
* usability observations
* communication reinforcement
* post-go-live feedback

### Decision Authority

Low formal authority but potentially high cultural influence.

### Adoption Value

Champions help identify usability problems before they become organization-wide resistance.

Related design:

* [Adoption Strategy](../10_ADOPTION_AND_TRAINING/01_adoption_strategy.md)
* [Training Plan](../10_ADOPTION_AND_TRAINING/02_training_plan.md)

---

# 3. Stakeholder Influence and Engagement

A simple engagement model helps determine how each stakeholder should participate during implementation.

| Stakeholder               |      Influence | Process Impact | Engagement Approach                  |
| ------------------------- | -------------: | -------------: | ------------------------------------ |
| Executive Sponsor         |           High |           High | Sponsor / decision escalation        |
| IT Management             |           High |           High | Steering and requirements approval   |
| Service Desk              |         Medium |      Very High | Workshops, prototyping, UAT          |
| Specialized Support Teams |         Medium |           High | Workshops, workflow validation, UAT  |
| Service Owners            |           High |           High | Requirements and approval design     |
| Security / Risk           |           High |    Medium-High | Control and exception design         |
| Change Approvers          |           High |         Medium | Approval workflow validation         |
| End Users                 |     Low formal |           High | Interviews, pilot, usability testing |
| Platform Administrators   | High technical |           High | Design/configuration workshops       |
| Vendors                   |            Low |         Medium | Targeted workflow review             |
| Asset / CI Owners         |         Medium |         Medium | Data-model workshops                 |
| HR / Identity             |         Medium |         Medium | Integration / lifecycle workshops    |
| Champions                 |     Low formal |  High adoption | Pilot, training, feedback            |

A later visual can convert this into an influence-versus-impact matrix:

[Stakeholder Influence & Impact Diagram](../diagrams/stakeholder_influence_map.md)

---

# 4. Decision Authority

One of the current-state weaknesses is that operational participation and decision authority are not always clearly separated.

The future implementation should distinguish between:

* **process contributors** — provide operational knowledge
* **process owners** — accountable for process outcomes
* **approvers** — authorize defined actions
* **platform administrators** — configure approved rules
* **executive sponsors** — resolve organizational barriers and major scope decisions

This avoids two common implementation failures:

1. configuring business policy based solely on whoever participates most actively in workshops; and
2. allowing technical configuration decisions to quietly become governance decisions.

A detailed responsibility model will be developed later in:

[Governance and Control Ownership](../06_GOVERNANCE_AND_CONTROLS/01_governance_model.md)

---

# 5. Discovery Priorities by Stakeholder

Not every stakeholder needs to participate in every workshop.

| Discovery Topic            | Primary Stakeholders                              |
| -------------------------- | ------------------------------------------------- |
| Intake channels            | End Users, Service Desk                           |
| Categorization and routing | Service Desk, Specialized Teams                   |
| Service ownership          | IT Management, Service Owners                     |
| Priority model             | Service Desk, Service Owners, IT Management       |
| SLA expectations           | IT Management, Service Owners                     |
| Approval rules             | Service Owners, Security, Management              |
| Change workflow            | Technical Teams, Change Approvers, Service Owners |
| Knowledge workflow         | Service Desk, Specialized Teams                   |
| Asset / CI relationships   | Asset Owners, Technical Teams                     |
| Vendor access              | Security, Technical Owners, Vendors               |
| User lifecycle             | HR, Identity Administration                       |
| Reporting                  | IT Management, Executive Sponsor                  |
| Adoption                   | End Users, Champions, Support Teams               |

This approach keeps discovery focused and reduces the tendency to bring every stakeholder into every design decision.

---

# 6. Key Stakeholder Risks

| ID    | Stakeholder Risk                                    | Potential Effect                          | Mitigation                                         |
| ----- | --------------------------------------------------- | ----------------------------------------- | -------------------------------------------------- |
| SR-01 | End users bypass new intake channels                | Incomplete service records                | Simplify intake and reinforce communication        |
| SR-02 | Service desk views workflow as added administration | Workarounds and poor data quality         | Involve service desk in design and pilot           |
| SR-03 | Technical teams resist centralized ownership        | Continued direct-request culture          | Define ownership without blocking technical access |
| SR-04 | Service owners do not participate                   | Weak SLA and approval design              | Assign accountable owners early                    |
| SR-05 | Security controls are added too late                | Redesign and implementation delay         | Include security during requirements phase         |
| SR-06 | Platform team configures unresolved business rules  | Rework and inconsistent workflows         | Require approved requirements before configuration |
| SR-07 | Managers over-focus on dashboard output             | Metrics disconnected from service quality | Define outcome metrics before dashboard design     |
| SR-08 | Vendors remain outside controlled workflow          | Weak auditability and access control      | Define vendor workflow and sponsorship             |
| SR-09 | Champions are selected too late                     | Weak local adoption support               | Identify champions before pilot                    |
| SR-10 | Stakeholder workshops become too broad              | Slow decisions and requirement conflict   | Match participation to decision area               |

These risks will feed the broader implementation risk register:

[Implementation Risk and Issue Register](../supporting_materials/risk_and_issue_register.md)

---

# 7. Stakeholder-to-Lifecycle Mapping

The stakeholder model continues throughout the implementation lifecycle.

| Lifecycle Stage | Major Stakeholder Participation                          |
| --------------- | -------------------------------------------------------- |
| Current State   | End Users, Service Desk, Support Teams, Management       |
| Requirements    | Service Owners, Support Teams, Security, Management      |
| Solution Design | Process Owners, Platform Administrators, Technical Teams |
| Governance      | Security, Service Owners, Management                     |
| Testing         | Support Teams, End Users, Platform Administrators        |
| Pilot           | Service Desk, Champions, Selected Users                  |
| Training        | Support Teams, End Users, Champions                      |
| Go-Live         | All operational stakeholders                             |
| Hypercare       | Service Desk, Platform Team, Support Teams               |
| Optimization    | Management, Process Owners, Service Teams                |

The intent is to maintain stakeholder involvement throughout implementation rather than treating discovery as a one-time interview exercise.

---

# 8. Stakeholder Deliverables

This stakeholder assessment supports several later artifacts:

* [Requirements Discovery](../02_REQUIREMENTS_DISCOVERY/01_requirements_discovery.md)
* [Target Operating Model](../03_TARGET_SERVICE_MODEL/01_target_operating_model.md)
* [Governance Model](../06_GOVERNANCE_AND_CONTROLS/01_governance_model.md)
* [Implementation Plan](../08_IMPLEMENTATION_PLAN/01_implementation_plan.md)
* [UAT Plan](../09_TESTING_AND_UAT/03_uat_plan.md)
* [Adoption Strategy](../10_ADOPTION_AND_TRAINING/01_adoption_strategy.md)

It also establishes the basis for a later **RACI / decision-authority matrix** once process ownership and workflow responsibilities have been finalized.

---

# 9. Current-State Finding

The organization does not have a stakeholder problem in the sense that no one is responsible for service delivery.

It has a **responsibility-definition problem**.

People generally know what work they perform, but that knowledge is not always represented clearly in the service process.

The target model needs to make four things explicit:

**Who requests the work.
Who owns the work.
Who is authorized to approve it.
Who is accountable for the service outcome.**

Those distinctions will be carried into requirements, workflow design, RBAC, approval logic, testing, and reporting.
