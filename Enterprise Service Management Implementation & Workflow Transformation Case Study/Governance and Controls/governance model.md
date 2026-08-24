# Governance Model

## Purpose

The Governance Model defines the decision boundaries, control ownership, approval expectations, and oversight mechanisms that keep the Enterprise Service Management environment reliable after implementation.

The target platform is not just a workflow engine.

It is also a system where people can:

* request access
* approve changes
* alter priorities
* assign work
* grant vendor access
* close records
* configure automation
* change workflow behavior

Those actions need enough control to preserve accountability without burying normal service work in unnecessary process.

The operating principle is:

> **Govern the decisions that create material risk. Do not add control just because the platform makes it possible.**

This model builds on:

* [Target Operating Model](../03%20Target%20Service%20Model/target%20operating%20model.md)
* [Data Governance](../05%20Data%20and%20Configuration%20Model/data%20governance.md)
* [Business Requirements](../02%20Requirements%20Discovery/business%20requirements.md)
* [Functional Requirements](../02%20Requirements%20Discovery/functional%20requirements.md)
* [Nonfunctional Requirements](../02%20Requirements%20Discovery/nonfunctional%20requirements.md)

---

# 1. Governance Objectives

The governance model is intended to ensure that:

* authority is clearly defined
* controlled actions require appropriate authorization
* self-approval is prevented where necessary
* privileged and vendor access is bounded
* material actions are auditable
* exceptions are visible
* service records retain enough information to support accountability
* production workflow changes are controlled
* control ownership remains clear after go-live

The objective is not to eliminate judgment.

The objective is to make sure that high-impact decisions are made by the right people and leave behind enough evidence to understand what happened.

---

# 2. Governance Principles

## 2.1 Authority Should Match the Decision

The person performing the technical work is not automatically the person who should authorize it.

Examples:

* a technician may fulfill access but not approve their own request
* a platform administrator may configure an SLA but should not define the business commitment
* a vendor may recommend a change but should not authorize it
* a service owner may accept service risk but should not bypass security controls without an approved exception path

---

## 2.2 Controls Should Scale With Risk

Routine support work should remain efficient.

Higher-risk activity should receive stronger control.

The target model therefore applies more governance to:

* privileged access
* sensitive system access
* high-risk change
* emergency exceptions
* vendor access
* priority override
* SLA exception
* production workflow configuration

---

## 2.3 Ownership Must Be Explicit

Every material control should have an accountable owner.

A control without an owner is usually a temporary idea rather than an operating control.

---

## 2.4 Exceptions Must Be Visible

There will be legitimate reasons to deviate from the standard workflow.

The problem is not the existence of exceptions.

The problem is when an exception looks exactly like normal processing.

Exceptions should therefore be:

* documented
* authorized where required
* time-bound where applicable
* reportable
* reviewable

---

## 2.5 Auditability Should Support Reconstruction

The organization should be able to determine:

* who acted
* what they did
* when they did it
* what record was affected
* why the exception or override occurred where required

Audit logging should support operational and control review, not just produce a large volume of events no one examines.

---

# 3. Governance Structure

The target governance model operates across four levels.

```text id="08ngdc"
Executive / Management Governance
            ↓
Process and Service Ownership
            ↓
Operational Control Ownership
            ↓
Platform Configuration / Execution
```

Each layer has a different responsibility.

---

# 4. Governance Roles

| Role                   | Governance Responsibility                               |
| ---------------------- | ------------------------------------------------------- |
| Executive Sponsor      | Supports transformation authority and major escalations |
| IT Management          | Owns overall service-performance governance             |
| Service Owner          | Accountable for service-specific expectations and risk  |
| Process Owner          | Owns workflow design and process policy                 |
| Security / Risk        | Defines security-related control requirements           |
| Change Authority       | Authorizes applicable changes                           |
| Access Owner           | Defines access approval and lifecycle expectations      |
| Support Group Lead     | Owns operational queue and escalation behavior          |
| Platform Administrator | Configures approved workflow and controls               |
| Data Owner             | Owns defined service-management data domain             |
| Auditor / Reviewer     | Validates control operation and evidence                |

The same individual may hold more than one role in a midsize organization.

The decision authority should still remain clear.

---

# 5. Decision Authority Model

| Decision                       | Primary Authority                              |
| ------------------------------ | ---------------------------------------------- |
| Define service owner           | IT Management                                  |
| Define SLA commitment          | Service Owner / IT Management                  |
| Change incident priority model | Process Owner / IT Management                  |
| Approve privileged access      | Authorized Access / System Owner               |
| Approve high-risk change       | Change Authority / Service Owner               |
| Grant vendor access            | Authorized Internal Sponsor + Access Authority |
| Approve SLA exception          | Defined Process / Service Owner                |
| Change production workflow     | Process Owner + Change Authority               |
| Modify RBAC structure          | Security / Platform Governance                 |
| Retire service catalog item    | Service Owner / Process Owner                  |
| Approve emergency change       | Emergency Change Authority                     |

The platform administrator implements these decisions.

They should not quietly become the person making them.

---

# 6. Control Categories

Controls are grouped as:

## Preventive

Designed to stop an invalid or unauthorized action before it occurs.

Examples:

* self-approval prevention
* RBAC
* required approval
* mandatory expiration
* required closure fields
* inactive-reference restriction

---

## Detective

Designed to identify a problem after or as it occurs.

Examples:

* audit logging
* overdue access reporting
* SLA exception reporting
* repeated reassignment monitoring
* stale knowledge reporting

---

## Corrective

Designed to restore the expected condition.

Examples:

* access revocation
* workflow correction
* data remediation
* incident escalation
* configuration rollback

A strong design generally uses all three where the risk justifies it.

---

# 7. Core Control Objectives

The target governance model establishes ten primary control objectives.

| ID    | Control Objective                                            |
| ----- | ------------------------------------------------------------ |
| CO-01 | Only authorized users perform controlled actions             |
| CO-02 | Request and approval are separated where required            |
| CO-03 | Temporary and vendor access expires as intended              |
| CO-04 | Material workflow actions remain auditable                   |
| CO-05 | Controlled records contain required closure evidence         |
| CO-06 | SLA exceptions and priority overrides are documented         |
| CO-07 | Production workflow changes are governed                     |
| CO-08 | Sensitive records are restricted appropriately               |
| CO-09 | Control ownership remains current                            |
| CO-10 | Exceptions and control failures are detectable and corrected |

These objectives will be expanded in:

[Control Matrix](./control%20matrix.md)

---

# 8. Role-Based Access Control

RBAC should align access with job responsibility.

Representative role groups include:

* requester
* service desk
* specialist resolver
* approver
* service owner
* change authority
* platform administrator
* security reviewer
* auditor
* vendor / external user where allowed

RBAC should govern abilities such as:

* record visibility
* assignment
* priority override
* approval
* workflow administration
* sensitive-record access
* reporting access

Detailed design:

[RBAC and Approval Controls](./rbac%20and%20approval%20controls.md)

---

# 9. Approval Separation

Selected workflows should prevent inappropriate overlap among:

* requester
* approver
* fulfiller

The strongest separation applies to higher-risk activity.

Example:

```text id="h7r20y"
Requester
   ↓
Approver
   ↓
Fulfillment
```

For low-risk routine activity, fewer roles may be required.

The goal is not maximum separation.

The goal is enough separation that the approval represents a real independent decision.

---

# 10. Privileged Request Governance

Privileged requests require stronger controls than standard service requests.

At minimum, the workflow should support:

* defined requester
* business purpose
* target system
* requested privilege
* approving authority
* prohibited self-approval
* fulfillment record
* expiration where temporary
* retained approval history

Privileged access should not be granted solely because the requester has enough technical standing to perform the work.

Technical capability and authorization are different things.

---

# 11. Vendor Access Governance

Vendor access introduces both external dependency and access risk.

Required controls may include:

* named internal sponsor
* business purpose
* defined system / service
* scoped privilege
* approval
* start date
* expiration
* extension approval
* audit history
* termination or disablement

Target lifecycle:

```text id="a6x614"
Request
  ↓
Sponsor
  ↓
Approval
  ↓
Provision
  ↓
Active
  ↓
Expiration
 ↙       ↘
Disable  Authorized Extension
```

The internal sponsor remains accountable for the access need.

---

# 12. Vendor Access Exception

If access cannot be automatically disabled, the workflow should create a tracked manual disablement action.

The control objective remains the same.

The platform should not claim that access was revoked if the integrated system cannot actually perform the action.

Where integration stops, accountability has to continue manually.

---

# 13. Audit Logging

Material actions should remain traceable.

Representative events include:

* approval
* rejection
* priority override
* SLA exception
* ownership transfer
* privileged request
* vendor access
* change authorization
* automation execution
* configuration change
* sensitive-record access where required

Audit records should identify, where technically available:

* actor
* action
* timestamp
* affected record
* previous value
* new value

---

# 14. Audit Review

Logging by itself is not a control outcome.

Selected audit information should be reviewed based on risk.

Examples:

* priority overrides
* privileged access approvals
* expired vendor access
* emergency changes
* SLA exceptions
* production configuration changes

The review frequency should be proportional to the risk and transaction volume.

---

# 15. Mandatory Closure Data

Certain workflow records should not close without required evidence.

Examples:

## Incident

* resolution category
* resolution summary
* relevant service / CI where applicable

## Service Request

* fulfillment result
* approval evidence where required
* delivered asset / access where applicable

## Change

* implementation outcome
* validation result
* backout status where applicable

This prevents `Closed` from becoming a substitute for actual completion evidence.

---

# 16. SLA Exception Governance

SLA exceptions should require:

* defined exception type
* reason
* applicable period
* authorized role where required
* retained history

Examples may include:

* customer-requested delay
* approved scheduling dependency
* defined vendor dependency
* documented business exception

An exception should remain visible in reporting.

Otherwise the organization is changing the denominator instead of managing the service.

---

# 17. Priority Override Governance

Priority override is allowed only for authorized roles.

Required evidence includes:

* calculated priority
* override priority
* reason
* actor
* timestamp

Repeated overrides should be reviewed.

A high override rate may indicate:

* poor priority definitions
* training gaps
* pressure-driven behavior
* inadequate service context

---

# 18. Periodic Access Review

Selected access roles should be reviewed periodically.

Scope may include:

* privileged ESM roles
* platform administrators
* approvers
* sensitive support groups
* vendor access
* audit roles

The review should validate:

* user remains active
* role is still required
* access level remains appropriate
* temporary access has not become permanent

---

# 19. Platform Administration Governance

Platform administrators can materially affect service behavior.

Their access should therefore be treated as privileged.

Administrative actions may affect:

* routing
* approvals
* SLA logic
* forms
* RBAC
* reporting
* automation
* integrations

Production administration should follow:

* least privilege
* controlled change
* audit logging
* testing
* rollback capability where practical

---

# 20. Configuration Change Governance

Material production configuration changes should follow a controlled lifecycle.

```text id="y1c2mp"
Change Requested
      ↓
Impact Review
      ↓
Approval
      ↓
Test
      ↓
Production
      ↓
Validation
```

Examples include:

* workflow change
* routing rule
* approval logic
* SLA calculation
* RBAC change
* automation
* integration
* production form logic

A platform used to manage change should not itself become an uncontrolled source of change.

---

# 21. Automation Governance

Automation should be based on documented business rules.

Controls should include:

* defined rule owner
* test coverage
* execution logging
* failure handling
* manual exception path
* change control

Examples:

```text id="m0o8dy"
Routing Rule
   ↓
Condition Met
   ↓
Automated Assignment
   ↓
Logged Result
```

If the rule fails:

```text id="6mxp08"
Automation Failure
      ↓
Exception Record
      ↓
Manual Owner
```

Automation should fail visibly.

---

# 22. AI Governance

AI-assisted capabilities require additional boundaries.

Permitted use cases may include:

* ticket summarization
* suggested categorization
* suggested knowledge
* duplicate detection
* response drafting
* trend analysis

Restricted autonomous actions include:

* privileged-access approval
* high-risk change approval
* control bypass
* audit modification
* access-rule changes

Human review remains required where a recommendation materially affects a controlled decision.

Detailed model:

[AI Governance](../07%20Automation%20and%20AI/ai%20governance.md)

---

# 23. Exception Governance

Exceptions may be required when standard process cannot reasonably apply.

Every material exception should answer:

* What standard rule is being bypassed?
* Why is the exception necessary?
* Who authorized it?
* How long does it apply?
* What additional risk exists?
* What corrective or compensating control applies?
* When will the exception be reviewed?

Example lifecycle:

```text id="v263gn"
Exception Requested
       ↓
Risk / Business Review
       ↓
Approve / Reject
       ↓
Time-Bound Exception
       ↓
Review / Expire
```

An exception that never expires is effectively a policy change and should be treated as one.

---

# 24. Control Ownership

| Control Area         | Primary Owner                          |
| -------------------- | -------------------------------------- |
| RBAC                 | Security / Platform Governance         |
| Approval Logic       | Process / Service Owner                |
| Privileged Requests  | Access / System Owner                  |
| Vendor Access        | Security / Internal Sponsor            |
| Change Authorization | Change Authority                       |
| SLA Exceptions       | Service / Process Owner                |
| Priority Overrides   | Service Management Owner               |
| Audit Logging        | Platform / Security                    |
| Closure Requirements | Process Owner                          |
| Configuration Change | Platform Owner / Change Authority      |
| Automation           | Process Owner / Platform Administrator |
| AI Governance        | IT Management / Security               |

Control ownership should be explicit enough that a failed control has somewhere to go.

---

# 25. Control Evidence

Representative evidence includes:

* approval records
* access records
* audit logs
* change records
* configuration history
* exception reports
* access-review results
* SLA exception history
* test results
* remediation records

The artifact should prove that the control operated.

A policy statement by itself does not do that.

---

# 26. Control Failure Handling

A control failure should trigger a defined response.

Examples:

| Failure                             | Response                            |
| ----------------------------------- | ----------------------------------- |
| Unauthorized self-approval          | Block transaction and log attempt   |
| Vendor access remains active        | Disable / escalate / investigate    |
| SLA exception lacks authorization   | Flag reporting exception            |
| Audit event missing                 | Technical investigation             |
| Change implemented without approval | Incident / governance review        |
| Closure data missing                | Prevent closure                     |
| RBAC assignment invalid             | Revoke / correct access             |
| Automation silently fails           | Generate exception and assign owner |

---

# 27. Governance Reporting

Management should receive focused governance information rather than raw control-event volume.

Representative measures include:

* privileged access requests
* self-approval blocks
* expired vendor access exceptions
* emergency changes
* SLA exceptions
* priority overrides
* overdue access reviews
* control failures
* unresolved exceptions
* unauthorized configuration attempts

A high number is not automatically bad.

The trend and root cause matter more.

---

# 28. Governance Metrics

| Metric                              | Purpose                                 |
| ----------------------------------- | --------------------------------------- |
| Self-Approval Block Count           | Validate separation-of-duty enforcement |
| Privileged Access Exception Rate    | Identify control pressure               |
| Vendor Access Expiration Compliance | Validate temporary-access lifecycle     |
| SLA Exception Rate                  | Measure service-policy exceptions       |
| Priority Override Rate              | Assess priority model quality           |
| Emergency Change Rate               | Identify operational pressure           |
| Access Review Completion            | Validate periodic review                |
| Control Failure Count               | Identify governance breakdown           |
| Configuration Change Failure Rate   | Measure platform governance             |
| Exception Age                       | Identify exceptions becoming permanent  |

---

# 29. Governance Review Cadence

Representative review cadence:

| Area                           | Review                                  |
| ------------------------------ | --------------------------------------- |
| Privileged platform access     | Quarterly                               |
| Vendor temporary access        | Monthly exception review / event-driven |
| Approval-role membership       | Quarterly                               |
| SLA exception trends           | Monthly                                 |
| Priority override trends       | Monthly                                 |
| Emergency changes              | Per event + monthly trend               |
| Platform configuration changes | Per change                              |
| Control ownership              | Semiannual                              |
| Governance model               | Annual or major process change          |

The cadence should be adjusted based on transaction volume and risk.

---

# 30. Light NIST Alignment

The governance model broadly aligns with established security-control concepts without turning the case study into a compliance exercise.

Representative alignment includes:

| ESM Control Area        | Broad NIST Concept                     |
| ----------------------- | -------------------------------------- |
| RBAC / privileged roles | Access Control                         |
| Approval separation     | Separation of Duties / Least Privilege |
| Audit logging           | Audit and Accountability               |
| Vendor access           | Access Control / Supply Chain Risk     |
| Change authorization    | Configuration Management               |
| Access review           | Account Management                     |
| Incident records        | Incident Response                      |
| Data ownership          | Governance / Asset Management          |
| Exception handling      | Risk Management                        |
| Automation controls     | Configuration / System Integrity       |

A more explicit mapping will be maintained in:

[Control Framework Mapping](./control%20framework%20mapping.md)

---

# 31. Governance Decision Table

| Condition                      | Required Governance Response       |
| ------------------------------ | ---------------------------------- |
| Routine low-risk request       | Standard workflow                  |
| Privileged request             | Approval + separation control      |
| High-risk change               | Elevated authorization             |
| Vendor requires access         | Sponsor + approval + expiration    |
| SLA exception required         | Document and authorize             |
| Priority override required     | Restricted role + reason           |
| Platform workflow changed      | Controlled configuration change    |
| Automation fails               | Manual exception path              |
| AI recommends sensitive action | Human review                       |
| Exception remains long-term    | Reassess as policy / design change |

---

# 32. Testing Mapping

Representative governance tests include:

| Test ID   | Scenario                                               |
| --------- | ------------------------------------------------------ |
| TC-GOV-01 | Unauthorized user cannot approve privileged request    |
| TC-GOV-02 | Requester cannot self-approve controlled request       |
| TC-GOV-03 | Vendor access expires as configured                    |
| TC-GOV-04 | SLA exception requires approved reason                 |
| TC-GOV-05 | Priority override retains audit history                |
| TC-GOV-06 | Ticket cannot close without required data              |
| TC-GOV-07 | Production workflow change requires authorized process |
| TC-GOV-08 | Automation failure creates manual exception            |
| TC-GOV-09 | Sensitive record restricted by role                    |
| TC-GOV-10 | Expired exception appears in governance reporting      |

These will be formalized in:

[Testing and UAT](../09%20Testing%20and%20UAT/test%20cases.md)

---

# 33. Governance Success Criteria

The governance model is design-ready when:

* governance roles are defined
* decision authority is documented
* control ownership is assigned
* RBAC boundaries are defined
* approval separation is defined
* vendor-access controls are defined
* privileged-request controls are defined
* audit requirements are defined
* SLA and priority exceptions are governed
* platform configuration changes are controlled
* automation and AI boundaries are defined
* control evidence is identified
* failure response is defined
* representative tests exist

---

# 34. Governance Model Conclusion

The target ESM environment needs enough governance to keep important decisions controlled without turning normal service delivery into a compliance exercise.

The practical distinction is simple.

Routine support work should move.

Sensitive actions should be authorized.

Exceptions should be visible.

Changes to the platform should be controlled.

And when something important happens, the organization should be able to reconstruct who made the decision and why.

That is the level of governance this implementation is trying to establish.

Not control for control’s sake.

Control where it actually protects the operation.

**Next:** [RBAC and Approval Controls](./rbac%20and%20approval%20controls.md)
