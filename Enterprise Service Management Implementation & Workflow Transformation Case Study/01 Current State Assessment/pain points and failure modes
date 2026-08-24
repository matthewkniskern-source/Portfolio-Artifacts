# Pain Points and Failure Modes

## Purpose

The current environment is not failing because people are unwilling or unable to support the business.

In most cases, the opposite is true.

Technicians, managers, system owners, and vendors have developed ways to keep work moving despite gaps in the service process. Direct emails get answered. People walk over to someone they know. Technicians message each other to figure out who owns a problem. Spreadsheets fill gaps the ticketing system does not cover.

That works until scale, urgency, turnover, or complexity exposes the weaknesses underneath it.

The purpose of this assessment is to separate everyday frustration from actual process failure. Those failure modes provide the bridge between the [Current-State Assessment](./01_current_state_assessment.md) and the formal requirements developed during [Requirements Discovery](../02_REQUIREMENTS_DISCOVERY/01_requirements_discovery.md).

The target environment should solve these problems without replacing informal inefficiency with formal inefficiency.

---

# 1. Assessment Approach

Current-state findings are evaluated across six questions:

1. **Where does work enter the process?**
2. **Where can ownership become unclear?**
3. **Where does the process depend on individual judgment?**
4. **Where can required information or authorization be lost?**
5. **Where does the organization lose visibility into what happened?**
6. **Where can the same problem happen repeatedly without being recognized as a pattern?**

Failure modes are grouped into the following areas:

* intake and record creation
* categorization and prioritization
* ownership and handoffs
* SLA and escalation
* approvals and authorization
* asset and configuration context
* knowledge management
* change management
* vendor activity
* closure and record quality
* reporting and measurement

A visual summary will be maintained in:

[Current-State Failure Landscape](../diagrams/current_state_failure_landscape.md)

---

# 2. Failure-Mode Summary

| ID    | Failure Mode                                       | Primary Cause                  | Business Effect                                       | Severity    |
| ----- | -------------------------------------------------- | ------------------------------ | ----------------------------------------------------- | ----------- |
| FM-01 | Work remains outside the managed service record    | Fragmented intake              | Lost visibility and incomplete workload data          | High        |
| FM-02 | Duplicate requests create duplicate effort         | Multiple intake channels       | Wasted technician time and inconsistent communication | Medium      |
| FM-03 | Priority is influenced by requester pressure       | Undefined priority model       | Resources assigned to the wrong work                  | High        |
| FM-04 | Tickets are repeatedly reassigned                  | Weak ownership and routing     | Increased resolution time                             | High        |
| FM-05 | Escalation occurs only after someone notices delay | Manual escalation              | SLA failures and reactive management                  | High        |
| FM-06 | Approval occurs outside the service record         | Informal authorization         | Weak auditability                                     | High        |
| FM-07 | Requester can influence or bypass approval path    | Weak separation of duties      | Unauthorized fulfillment risk                         | High        |
| FM-08 | Asset or CI relationship is missing                | Weak data integration          | Reduced troubleshooting and impact analysis           | Medium      |
| FM-09 | Knowledge remains with individual technicians      | Weak knowledge process         | Repeated troubleshooting                              | Medium      |
| FM-10 | Failed change is not linked to resulting incident  | Weak record relationships      | Poor root-cause visibility                            | High        |
| FM-11 | Vendor activity is not fully recorded              | External support workflow gap  | Weak accountability and access visibility             | High        |
| FM-12 | Vendor access remains active beyond need           | Weak lifecycle control         | Unnecessary access exposure                           | High        |
| FM-13 | Ticket closes without useful resolution data       | Weak closure standards         | Poor historical and knowledge value                   | Medium      |
| FM-14 | Repeat incidents are treated independently         | Limited trend analysis         | Recurring problems remain unresolved                  | Medium-High |
| FM-15 | Reporting excludes informal work                   | Incomplete transaction capture | Misleading management information                     | High        |
| FM-16 | Automation acts on poor or incomplete data         | Weak data quality              | Incorrect routing, escalation, or decisions           | Medium-High |

Severity represents implementation priority, not a formal enterprise risk score.

A detailed risk-and-control treatment will be developed later in [Governance and Controls](../06_GOVERNANCE_AND_CONTROLS/01_governance_model.md).

---

# 3. Intake and Record-Creation Failures

## FM-01 — Work Remains Outside the Managed Service Record

### Scenario

An employee messages a technician directly about a recurring application problem.

The technician knows the user, understands the application, and fixes the issue in ten minutes.

No ticket is created.

From the user's perspective, the process worked.

From the organization's perspective, the work effectively never happened.

### Failure

The organization loses:

* demand data
* technician workload visibility
* incident history
* affected service history
* recurring-problem information
* resolution knowledge

The individual interaction may have been efficient while the overall process was not.

### Root Cause

The current model does not consistently distinguish between a quick conversation and work that should become a managed service record.

### Target-State Direction

The target process should make record creation easy enough that technicians are not forced to choose between helping the user and documenting the work.

Where practical, supported intake channels should create or update records automatically.

Related design:

* [Target Operating Model](../03_TARGET_SERVICE_MODEL/01_target_operating_model.md)
* [Automation Opportunities](../07_AUTOMATION_AND_AI/01_automation_opportunities.md)

---

# 4. Duplicate-Work Failures

## FM-02 — Multiple Channels Create Multiple Records

### Scenario

A business application becomes unavailable.

One user opens a ticket.

Another calls the service desk.

A manager emails an application administrator.

Several employees begin messaging technicians directly.

Different support personnel begin investigating what is actually the same outage.

### Failure

The organization may create several independent records for one underlying condition.

This leads to:

* duplicate troubleshooting
* conflicting user communication
* inflated ticket volume
* fragmented technical notes
* inconsistent closure

### Root Cause

The current process lacks reliable correlation between related reports.

### Target-State Direction

The target incident workflow should support:

* duplicate identification
* parent/child relationships
* major-incident association
* common communication
* affected-user tracking

Responsible duplicate detection may also become an appropriate AI-assisted capability.

Related design:

* [Incident Management Workflow](../04_WORKFLOW_DESIGN/01_incident_management.md)
* [AI-Assisted Service Management](../07_AUTOMATION_AND_AI/02_ai_assisted_service_management.md)

---

# 5. Priority Failures

## FM-03 — The Loudest Request Becomes the Highest Priority

### Scenario

A manager directly contacts a technician regarding a printer problem while a multi-user application incident is already in the queue.

The manager expects immediate help.

Without a defined priority model, the technician has to make the call.

### Failure

Urgency becomes influenced by:

* organizational position
* persistence
* personal relationships
* whichever technician receives the request
* subjective interpretation of "critical"

This is not a sustainable priority model.

### Root Cause

Impact and urgency have not been translated into consistent business rules.

### Target-State Direction

Priority should be determined through a defined combination of factors such as:

* number of users affected
* business-service impact
* operational impact
* availability of workaround
* time sensitivity
* safety or security considerations where applicable

Executive importance alone should not automatically equal operational severity.

The proposed model will be developed in:

[Priority and SLA Model](../03_TARGET_SERVICE_MODEL/03_priority_and_sla_model.md)

---

# 6. Ownership and Handoff Failures

## FM-04 — Reassignment Becomes the Workflow

### Scenario

A ticket reaches the service desk with limited information.

It is assigned to endpoint support.

Endpoint determines that it appears application-related and sends it to application support.

Application support believes the issue is network-related.

Network reviews the ticket and determines that the original issue was probably endpoint configuration.

The ticket returns to the original group.

### Failure

Technically, the ticket remained active throughout the process.

Operationally, very little happened.

### Effects

* delayed resolution
* wasted technician effort
* frustrated users
* distorted workload measures
* unclear accountability

### Root Cause

Three problems are combining:

1. incomplete intake information,
2. weak routing criteria, and
3. unclear ownership during reassignment.

### Target-State Direction

The future model should define:

* support-group scope
* assignment rules
* mandatory handoff information
* current ownership during escalation
* reassignment reason
* escalation thresholds

Reassignment should remain available because the first assignment will not always be correct.

It should not become the organization's substitute for knowing who owns what.

Related design:

* [Ownership and Escalation Model](../03_TARGET_SERVICE_MODEL/04_ownership_and_escalation.md)
* [Incident Management Workflow](../04_WORKFLOW_DESIGN/01_incident_management.md)

---

# 7. SLA and Escalation Failures

## FM-05 — Escalation Depends on Someone Remembering

### Scenario

A service request is approaching its expected completion time.

The technician is working other issues and does not notice.

The requester sends another email.

Only then does the aging request receive attention.

### Failure

The escalation mechanism is the customer asking again.

### Root Cause

Time-based service expectations are not consistently connected to workflow automation.

### Target-State Direction

The future environment should support:

* response timers
* resolution or fulfillment targets
* warning thresholds
* automated escalation
* documented pause conditions
* manager visibility
* exception reason capture

Not every aging ticket requires management escalation.

The workflow should distinguish between:

* work actively delayed by the support organization
* work awaiting requester information
* approved scheduling delays
* vendor dependency
* legitimate business exceptions

That distinction matters if SLA reporting is expected to mean anything.

Related design:

* [Priority and SLA Model](../03_TARGET_SERVICE_MODEL/03_priority_and_sla_model.md)
* [Automation Opportunities](../07_AUTOMATION_AND_AI/01_automation_opportunities.md)

---

# 8. Approval and Authorization Failures

## FM-06 — Approval Exists, but the Evidence Does Not

### Scenario

A user requests hardware requiring manager approval.

The technician receives an email from the manager saying, "Go ahead."

The hardware is ordered.

Months later, the organization can confirm the purchase but cannot easily reconstruct the approval within the service record.

### Failure

The business decision occurred, but the system of record does not reliably preserve:

* approver identity
* decision date
* decision scope
* request state at approval
* approval comments

### Root Cause

Approval is treated as communication rather than a controlled workflow state.

### Target-State Direction

Where formal approval is required, approval should be captured as structured workflow activity.

Related design:

* [Service Request Management](../04_WORKFLOW_DESIGN/02_service_request_management.md)
* [RBAC and Approval Controls](../06_GOVERNANCE_AND_CONTROLS/02_rbac_and_approval_controls.md)

---

## FM-07 — Self-Approval or Approval Bypass

### Scenario

A requester also holds a role that technically permits approval of that request type.

The platform allows the same individual to request and approve the action.

### Failure

Permission alone becomes authorization.

### Root Cause

The process has not distinguished between:

* having an approval role, and
* being an appropriate approver for a specific transaction.

### Target-State Direction

Selected workflows should prohibit self-approval and require appropriate separation between requester and approver.

This becomes especially important for:

* privileged access
* higher-cost purchases
* sensitive system access
* selected changes

Related controls will be defined in:

[Governance and Controls](../06_GOVERNANCE_AND_CONTROLS/01_governance_model.md)

This failure will also become a formal UAT scenario:

[Testing and UAT](../09_TESTING_AND_UAT/01_test_strategy.md)

---

# 9. Asset and Configuration Failures

## FM-08 — The Ticket Describes the Problem but Not the Environment

### Scenario

A user reports:

> "My application stopped working."

The ticket contains the user's name and description, but no reliable relationship to:

* workstation
* application instance
* supporting server
* location
* business service
* recent change

### Failure

Technical investigation begins with information gathering that could already exist in the service-management environment.

### Root Cause

Ticket records and configuration data are maintained as separate information rather than related operational context.

### Target-State Direction

The target data model should allow relevant relationships among:

**User → Ticket → Asset/CI → Service → Change → Vendor → Knowledge**

The goal is not to create an enormous CMDB for its own sake.

Only relationships that support real operational decisions should be maintained.

Related design:

[Service Management Data Model](../05_DATA_AND_CONFIGURATION_MODEL/01_service_management_data_model.md)

---

# 10. Knowledge Failures

## FM-09 — Known Problems Are Solved Like New Problems

### Scenario

A technician resolves an issue that another technician solved several weeks earlier.

Both solutions are correct.

Neither technician knew the other resolution existed.

### Failure

The organization pays repeatedly for the same troubleshooting.

### Root Cause

Useful operational knowledge exists in places that are difficult to search or reuse:

* old tickets
* email
* chat
* personal notes
* technician memory

### Target-State Direction

Knowledge creation should be connected to actual service activity.

Potential triggers include:

* recurring incidents
* high-value resolutions
* new support procedures
* successful troubleshooting patterns
* known workarounds

Not every closed ticket needs to become a knowledge article.

The goal is useful knowledge, not a larger pile of documents.

Related design:

[Knowledge Management Workflow](../04_WORKFLOW_DESIGN/04_knowledge_management.md)

---

# 11. Change-Management Failures

## FM-10 — A Failed Change Looks Like an Unrelated Incident

### Scenario

A configuration change is implemented overnight.

The next morning, users begin reporting a service problem.

Incident responders see the affected service but have no immediate indication that a relevant change occurred several hours earlier.

### Failure

The organization loses one of the most valuable pieces of troubleshooting context available.

### Root Cause

Change and incident records exist independently.

### Target-State Direction

Relevant changes should be associated with affected:

* services
* configuration items
* implementation windows
* resulting incidents

A failed or partially successful change should trigger defined backout, escalation, and review behavior.

Related design:

* [Change Management Workflow](../04_WORKFLOW_DESIGN/03_change_management.md)
* [Service Management Data Model](../05_DATA_AND_CONFIGURATION_MODEL/01_service_management_data_model.md)

---

# 12. Vendor Failures

## FM-11 — Internal Visibility Ends When the Vendor Takes Over

### Scenario

An internal team opens a support case with a vendor.

Technical discussion shifts to vendor email or a separate support portal.

The internal ticket remains open with a note such as:

> "Waiting on vendor."

### Failure

Internal stakeholders lose visibility into:

* current action
* latest vendor response
* accountable internal owner
* expected follow-up
* troubleshooting performed externally

### Root Cause

Vendor support is treated as an external interruption to the workflow instead of a managed dependency within it.

### Target-State Direction

The internal service record should remain authoritative even when an external vendor performs part of the work.

The vendor does not need unrestricted access to the ESM platform to achieve that.

---

## FM-12 — Temporary Vendor Access Becomes Permanent by Accident

### Scenario

A vendor receives remote or privileged access to troubleshoot a technical issue.

The issue is resolved.

The access remains active because no workflow event requires it to expire.

### Failure

A temporary operational requirement becomes persistent access.

### Root Cause

Access provisioning and service activity are not tied to the same lifecycle.

### Target-State Direction

Where vendor access is required, the workflow should capture:

* internal sponsor
* business purpose
* system or service
* approved access level
* start time
* expiration
* extension approval if required

Expiration should be automatic where technically feasible.

Related design:

* [RBAC and Approval Controls](../06_GOVERNANCE_AND_CONTROLS/02_rbac_and_approval_controls.md)
* [Automation Opportunities](../07_AUTOMATION_AND_AI/01_automation_opportunities.md)

---

# 13. Closure and Record-Quality Failures

## FM-13 — "Fixed" Is Not a Resolution Record

### Scenario

A technician closes an incident with:

> "Resolved."

The user is satisfied and the ticket is technically complete.

Several months later, the same issue occurs.

The prior record provides no useful information.

### Failure

Closure satisfies workflow status without creating operational value.

### Root Cause

Required closure information is weak or inconsistent.

### Target-State Direction

Closure requirements should vary by record type but may include:

* resolution category
* resolution summary
* action performed
* affected asset or CI
* user confirmation where appropriate
* related knowledge
* change relationship where applicable

The goal is enough information to make the historical record useful without turning every ticket into a technical report.

Related design:

[Governance and Controls](../06_GOVERNANCE_AND_CONTROLS/01_governance_model.md)

---

# 14. Repeat-Incident Failures

## FM-14 — Repeated Symptoms Never Become a Trend

### Scenario

Five users report the same intermittent issue over several weeks.

Each incident is solved individually.

No single ticket appears severe enough to attract management attention.

### Failure

The organization becomes good at repeatedly repairing the symptom.

### Root Cause

Incident resolution is measured individually while trend identification remains weak.

### Target-State Direction

Reporting and analysis should identify patterns by:

* category
* service
* configuration item
* location
* resolution type
* time period

AI-assisted trend detection may support this process, but human review should determine whether a statistical pattern represents an actual operational problem.

Related design:

* [AI-Assisted Service Management](../07_AUTOMATION_AND_AI/02_ai_assisted_service_management.md)
* [Metrics and Optimization](../11_METRICS_AND_OPTIMIZATION/01_performance_framework.md)

---

# 15. Reporting and Measurement Failures

## FM-15 — The Dashboard Is Correct About Incomplete Data

This is one of the larger problems in the current environment.

A dashboard can accurately report every ticket in the platform and still provide a misleading picture of service performance.

If work occurring through email, chat, phone, and direct contact never becomes a managed record, it does not appear in:

* workload
* SLA performance
* service demand
* repeat-incident analysis
* technician activity
* backlog

The dashboard is not necessarily wrong.

The process feeding it is incomplete.

### Target-State Direction

The organization should improve transaction capture before treating management dashboards as authoritative.

This is why adoption is not separate from reporting.

Poor adoption becomes poor data.

Poor data becomes poor management information.

Related design:

* [Adoption Strategy](../10_ADOPTION_AND_TRAINING/01_adoption_strategy.md)
* [Performance Framework](../11_METRICS_AND_OPTIMIZATION/01_performance_framework.md)

---

# 16. Automation Failure

## FM-16 — Automating a Bad Decision Faster

Automation can remove repetitive work, but it can also make a weak process fail more consistently.

Examples include:

* routing based on unreliable categories
* escalating tickets with invalid SLA states
* automatically approving poorly defined requests
* generating notifications no one acts on
* allowing AI-generated categorization to drive sensitive workflow decisions without review

### Root Cause

Automation is introduced before:

* the workflow is stable
* ownership is defined
* data quality is adequate
* exception handling is understood

### Target-State Direction

Automation should follow defined process logic.

The rule for this implementation is:

> **Automate repeatable decisions. Do not use automation to avoid making the decision in the first place.**

AI-assisted functionality will follow the same principle.

Related design:

[Automation and AI](../07_AUTOMATION_AND_AI/01_automation_opportunities.md)

---

# 17. Cross-Cutting Failure Themes

The individual failure modes reduce to several broader operating problems.

## Process Fragmentation

There is no reliable guarantee that managed service work enters a common process.

## Decision Inconsistency

Priority, routing, escalation, approval, and closure depend too heavily on individual interpretation.

## Weak Relationship Data

Users, tickets, services, assets, configuration items, changes, vendors, and knowledge are not consistently connected.

## Incomplete Governance

Approval, privileged activity, vendor access, exceptions, and required records are not consistently controlled.

## Limited Organizational Memory

Historical tickets and technician experience are not being converted into reusable operational knowledge.

## Measurement Without Complete Capture

The organization can report what the platform knows.

It cannot assume the platform knows everything the organization is doing.

A summary visual will group these themes in the:

[Current-State Failure Landscape](../diagrams/current_state_failure_landscape.md)

---

# 18. Failure Mode to Design Response

The current-state assessment should connect directly to future design.

| Failure                        | Required Design Response                     |
| ------------------------------ | -------------------------------------------- |
| FM-01 Undocumented work        | Standardized intake and record creation      |
| FM-02 Duplicate work           | Correlation and duplicate handling           |
| FM-03 Subjective priority      | Impact/urgency priority matrix               |
| FM-04 Reassignment loops       | Defined support ownership and routing        |
| FM-05 Manual escalation        | SLA timers and escalation logic              |
| FM-06 Informal approval        | Structured approval workflow                 |
| FM-07 Self-approval            | Separation-of-duty control                   |
| FM-08 Missing CI context       | Service and CI relationships                 |
| FM-09 Knowledge loss           | Knowledge workflow and reuse                 |
| FM-10 Unlinked failed change   | Change/incident relationships                |
| FM-11 Hidden vendor activity   | Managed vendor dependency                    |
| FM-12 Persistent vendor access | Time-bound access controls                   |
| FM-13 Weak closure record      | Mandatory closure criteria                   |
| FM-14 Repeat incidents         | Trend analysis                               |
| FM-15 Incomplete reporting     | Adoption and transaction capture             |
| FM-16 Bad automation           | Automation governance and exception handling |

This mapping becomes an early traceability layer.

Later sections will formalize the chain as:

**Failure Mode → Requirement → Workflow / Control → Test Case → Metric**

The completed traceability model will be maintained in:

[Requirements Traceability Matrix](../02_REQUIREMENTS_DISCOVERY/05_requirements_traceability_matrix.md)

and

[Requirements-to-Test Traceability](../09_TESTING_AND_UAT/04_requirements_test_traceability.md)

---

# 19. Current-State Conclusion

The core issue is not that the organization lacks support capability.

It lacks a consistent operating model around that capability.

People are compensating for process gaps through experience, relationships, manual follow-up, and workarounds. That has kept the environment functional, but it also hides demand, creates inconsistent decisions, weakens auditability, and makes performance difficult to measure.

The target ESM implementation should not attempt to eliminate every informal conversation or force every action through an elaborate workflow.

It should establish enough structure that the organization can reliably answer:

* what happened
* who owns it
* how important it is
* what it affects
* who authorized it
* what was done
* whether the expected service was delivered
* whether the same problem is happening again

That is the point where the platform begins supporting the operation instead of merely storing tickets.

**Next:** [Baseline Service Metrics](./04_baseline_metrics.md)
