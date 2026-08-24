# Service Request Management

## Purpose

The Service Request Management workflow defines how the organization handles repeatable user requests for approved services, access, equipment, software, and other standard business needs.

Unlike incidents, service requests are not primarily about restoring failed service.

They are about delivering something the organization already knows how to provide.

The target workflow should therefore emphasize:

* clear request definition
* required information
* predictable approval
* repeatable fulfillment
* visible ownership
* measurable completion

The operating principle is:

> **If the request is repeatable, the process around it should be repeatable too.**

This workflow builds on:

* [Service Catalog](../03%20Target%20Service%20Model/service%20catalog.md)
* [Ownership and Escalation](../03%20Target%20Service%20Model/ownership%20and%20escalation.md)
* [Functional Requirements](../02%20Requirements%20Discovery/functional%20requirements.md)
* [Business Requirements](../02%20Requirements%20Discovery/business%20requirements.md)

---

# 1. Scope

Service Request Management applies to defined, repeatable user needs such as:

* standard application access
* privileged access
* software installation
* equipment requests
* shared mailbox creation
* VPN access
* temporary vendor access
* other approved catalog services

It does not apply to:

* unplanned service interruption
* emergency troubleshooting
* high-complexity project work
* large enhancement requests
* changes requiring separate Change Management treatment

Where a submitted request falls outside catalog scope, it should be redirected into the correct process rather than forced through an unsuitable request workflow.

---

# 2. Core States

The target request lifecycle uses the following states:

```text
Submitted
   ↓
Validation
   ↓
Pending Approval
   ↓
Fulfillment
   ↓
Validation / Confirmation
   ↓
Complete
```

Additional states may include:

* Rejected
* Cancelled
* Waiting on Requester
* Waiting on Vendor
* Scheduled
* Exception

The workflow should remain simple enough that status tells the user what is actually happening.

---

# 3. State Definitions

| State                     | Purpose                               | Primary Owner                     |
| ------------------------- | ------------------------------------- | --------------------------------- |
| Submitted                 | Request entered                       | Intake / Fulfillment Group        |
| Validation                | Required data and eligibility checked | Fulfillment Group                 |
| Pending Approval          | Required authorization outstanding    | Fulfillment Group / Approver      |
| Fulfillment               | Requested work being performed        | Fulfillment Group                 |
| Waiting on Requester      | Required user information outstanding | Fulfillment Group                 |
| Waiting on Vendor         | External dependency exists            | Internal Fulfillment Group        |
| Scheduled                 | Approved future action                | Fulfillment Group                 |
| Validation / Confirmation | Completion being verified             | Fulfillment Group                 |
| Complete                  | Request successfully fulfilled        | Final Owning Group                |
| Rejected                  | Required authorization denied         | Process Owner / Fulfillment Group |
| Cancelled                 | Request withdrawn or invalid          | Authorized Role                   |
| Exception                 | Normal workflow cannot continue       | Defined Exception Owner           |

---

# 4. Core Workflow

```text
Request Submitted
      ↓
Validate Required Data
      ↓
Validate Eligibility
      ↓
Approval Required?
   ↙              ↘
 No                Yes
 ↓                  ↓
Fulfillment       Approval
                     ↓
                 Approved?
                ↙        ↘
              Yes         No
               ↓           ↓
          Fulfillment    Rejected
               ↓
         Completion Check
               ↓
            Complete
```

A polished version will be maintained in:

[Service Request Workflow](../diagrams/service%20request%20workflow.md)

---

# 5. Request Intake

Requests should primarily enter through the approved [Service Catalog](../03%20Target%20Service%20Model/service%20catalog.md).

Each catalog item defines:

* user-facing request
* required information
* service owner
* fulfillment group
* approval logic
* target completion time
* closure criteria

Technician-assisted creation remains available when necessary.

The user should not need to know which support group fulfills the request.

The catalog should make that decision behind the scenes.

---

# 6. Validation

Before fulfillment begins, the request should be checked for:

* required information
* requester identity
* eligibility
* appropriate service selection
* required business justification
* approval requirement
* duplicate submission where applicable

Validation prevents avoidable downstream rework.

If required information is missing, the request moves to `Waiting on Requester` rather than being assigned incomplete.

---

# 7. Approval Logic

Not every service request requires approval.

Approval is driven by risk, cost, privilege, or business authority.

Three standard approval levels are used:

| Level | Approval Model                    | Example                     |
| ----- | --------------------------------- | --------------------------- |
| A0    | No manual approval                | Standard approved software  |
| A1    | Single approval                   | Shared mailbox              |
| A2    | Controlled / multi-party approval | Privileged or vendor access |

The approval level is defined by catalog item.

---

# 8. Approval Workflow

```text
Request Validated
      ↓
Approval Required?
   ↙              ↘
 No                Yes
 ↓                  ↓
Fulfill          Route Approval
                     ↓
                Approve / Reject
                  ↙       ↘
                Yes        No
                 ↓          ↓
             Fulfill     Rejected
```

Approval records shall capture:

* approver
* decision
* timestamp
* comments where required
* related request

For designated controlled requests, self-approval is prohibited.

---

# 9. Approval Aging

Approval should not become a black hole.

If a decision remains outstanding, the platform should support:

* reminder
* escalation
* delegation where authorized
* expiration or cancellation where appropriate

Example:

```text
Approval Requested
      ↓
Reminder
      ↓
Escalation
      ↓
Decision / Expiration
```

Approval time should be measured separately from fulfillment time.

---

# 10. Fulfillment

Once required approval and validation are complete, the fulfillment group performs the requested work.

Fulfillment may involve:

* one technician action
* several tasks
* automated action
* external vendor participation
* coordinated work across groups

The parent request remains the user-facing record.

Individual fulfillment tasks should not force the user to track several separate work records.

---

# 11. Fulfillment Tasks

A request may generate multiple tasks.

Example:

```text
Laptop Request
     ↓
Approved
     ↓
 ┌───────┬────────┬──────────┐
 ↓       ↓        ↓
Prepare  Update   Configure
Device   Asset    Access
 └───────┴────────┴──────────┘
          ↓
       Deliver
          ↓
      Confirm
```

Each task may have a separate owner.

The parent request retains overall fulfillment accountability.

---

# 12. Ownership

Each active request must have a defined owning fulfillment group.

During:

* approval
* user dependency
* vendor dependency
* scheduled activity

the internal owner remains visible.

Example:

```text
Request
  ↓
Fulfillment Group Owns
  ↓
Pending Approval
  ↓
Approval Decision
  ↓
Same Group Continues
```

The approver owns the decision.

The fulfillment group still owns the service outcome.

---

# 13. Reassignment

Reassignment should be less common for catalog-based requests than for incidents because ownership is predefined.

A catalog request should normally know its fulfillment group before publication.

If reassignment occurs, the platform should capture:

* previous owner
* new owner
* reason
* timestamp

Repeated reassignment may indicate:

* poor catalog design
* incorrect service ownership
* unclear fulfillment responsibilities

---

# 14. Waiting on Requester

A request may enter `Waiting on Requester` when information required for fulfillment is missing.

The workflow should support:

1. initial request for information
2. reminder
3. final notice
4. controlled cancellation or closure where policy permits

The fulfillment group retains ownership throughout the wait.

---

# 15. Vendor Dependency

Some service requests may require external participation.

Example:

```text
Service Request
      ↓
Internal Fulfillment
      ↓
Vendor Action Required
      ↓
Vendor Dependency
      ↓
Internal Validation
      ↓
Complete
```

The request should retain:

* internal owner
* vendor
* vendor case or activity reference
* current dependency
* next follow-up

Vendor involvement does not transfer the organization's accountability for fulfillment.

---

# 16. Scheduled Fulfillment

Some approved requests are intentionally fulfilled later.

Examples include:

* equipment deployment
* scheduled access activation
* maintenance-related service request
* user-selected installation window

Scheduled status should require:

* approved date
* reason
* accountable owner

A request should not be moved into scheduled status simply to protect fulfillment metrics.

---

# 17. Controlled Access Requests

Requests involving privileged or sensitive access require additional controls.

Examples:

* privileged account
* elevated application role
* vendor administrative access
* selected remote-access privileges

Required controls may include:

* manager or sponsor validation
* system owner approval
* security approval
* prohibited self-approval
* expiration
* access scope
* retained approval history

Detailed controls:

[RBAC and Approval Controls](../06%20Governance%20and%20Controls/rbac%20and%20approval%20controls.md)

---

# 18. Temporary Access Lifecycle

Temporary access should follow an explicit lifecycle.

```text
Request
  ↓
Approval
  ↓
Provision
  ↓
Active
  ↓
Expiration
 ↙        ↘
Disable   Approved Extension
```

An extension is a new authorization decision.

The original approval should not silently become indefinite permission.

---

# 19. Request Completion

A service request may move to `Complete` when:

* required approvals are satisfied
* fulfillment tasks are complete
* requested service or item has been delivered
* required data relationships are updated
* user notification has occurred
* closure information is complete

Completion criteria should be defined by catalog item.

---

# 20. Closure Data

Applicable closure information may include:

* fulfillment result
* completion summary
* delivered asset
* provisioned access
* related CI
* fulfillment task status
* exception or deviation
* requester notification

The request record should be useful later for both audit and service analysis.

---

# 21. Rejection

A request may be rejected when:

* required approval is denied
* requester is not eligible
* requested service is not available
* request violates defined policy
* required business justification is not accepted

Rejection shall capture:

* decision
* approver or decision authority
* reason
* timestamp

The requester should receive a clear outcome.

---

# 22. Cancellation

A request may be cancelled when:

* requester withdraws it
* duplicate request exists
* request was submitted in error
* required information is never provided
* business need no longer exists

Cancellation requires reason and remains auditable.

---

# 23. Exception Handling

| Condition                             | Workflow Response                               |
| ------------------------------------- | ----------------------------------------------- |
| Missing information                   | Waiting on Requester                            |
| Wrong catalog item                    | Reclassify / redirect                           |
| Approval delayed                      | Reminder / escalation                           |
| Approval denied                       | Reject                                          |
| Fulfillment automation fails          | Manual exception                                |
| Vendor delayed                        | Vendor dependency / escalation                  |
| Asset unavailable                     | Scheduled / exception                           |
| Temporary access expiration fails     | Manual disablement action                       |
| Request expands beyond standard scope | Route to Change / Project / Enhancement process |

---

# 24. Request Boundary Decision

A service request should leave the normal workflow when scope changes materially.

Example:

```text
Request Submitted
      ↓
Standard Fulfillment?
   ↙              ↘
 Yes               No
 ↓                  ↓
Request Process   Change /
                 Project /
                Enhancement
```

This prevents the service-request queue from becoming a holding area for work that belongs somewhere else.

---

# 25. Automation Opportunities

Good candidates include:

* form prepopulation
* eligibility checks
* routing
* approval routing
* reminders
* fulfillment-task creation
* expiration
* standard notifications
* integrated software deployment
* asset assignment update

Automation is most appropriate when the decision is stable and the data supporting it is reliable.

---

# 26. AI-Assisted Opportunities

Potential low-risk AI support includes:

* request summarization
* suggested catalog item
* suggested knowledge
* duplicate-request detection
* response drafting

AI should not independently:

* approve privileged access
* override required approval
* change access policy
* authorize sensitive exceptions

Related governance:

[AI Governance](../07%20Automation%20and%20AI/ai%20governance.md)

---

# 27. Controls

| Control                     | Purpose                          |
| --------------------------- | -------------------------------- |
| Catalog-defined ownership   | Prevent routing ambiguity        |
| Required fields             | Improve fulfillment quality      |
| Eligibility validation      | Prevent invalid requests         |
| Approval gate               | Prevent unauthorized fulfillment |
| Self-approval restriction   | Preserve separation of duties    |
| Approval history            | Maintain auditability            |
| Temporary-access expiration | Prevent persistent access        |
| Closure criteria            | Preserve complete records        |
| Exception routing           | Prevent silent failure           |

---

# 28. Service Request Metrics

| Metric                  | Purpose                                |
| ----------------------- | -------------------------------------- |
| Fulfillment Time        | Measure delivery performance           |
| SLA Compliance          | Measure service commitment             |
| Approval Cycle Time     | Identify approval delay                |
| Reassignment Rate       | Identify catalog or ownership weakness |
| Rejection Rate          | Identify request-policy mismatch       |
| Cancellation Rate       | Identify intake or usability issues    |
| Automation Rate         | Measure repeatable fulfillment         |
| Automation Failure Rate | Identify unstable integrations         |
| Catalog Item Volume     | Measure demand                         |
| CSAT                    | Measure user experience                |

---

# 29. Testing Mapping

Representative tests include:

| Test ID   | Scenario                                       |
| --------- | ---------------------------------------------- |
| TC-REQ-01 | Standard request with no approval              |
| TC-REQ-02 | Hardware request requiring approval            |
| TC-REQ-03 | Prohibited self-approval                       |
| TC-REQ-04 | Rejected request                               |
| TC-REQ-05 | Approval aging escalation                      |
| TC-REQ-06 | Multi-task fulfillment                         |
| TC-VND-02 | Temporary vendor access expiration             |
| TC-AUT-01 | Automated fulfillment success                  |
| TC-AUT-02 | Failed automation enters manual exception path |

These will be formalized in:

[Testing and UAT](../09%20Testing%20and%20UAT/test%20cases.md)

---

# 30. Service Request Decision Table

| Condition                            | Action              | Result                         |
| ------------------------------------ | ------------------- | ------------------------------ |
| Valid standard request / no approval | Fulfill             | Fulfillment                    |
| Approval required                    | Route approval      | Pending Approval               |
| Approval denied                      | Reject              | Rejected                       |
| Missing information                  | Request information | Waiting on Requester           |
| Vendor action required               | Track dependency    | Waiting on Vendor              |
| Scheduled delivery required          | Schedule            | Scheduled                      |
| Automation fails                     | Manual exception    | Exception                      |
| Request exceeds catalog scope        | Redirect            | Change / Project / Enhancement |
| Fulfillment complete                 | Validate            | Completion                     |
| Closure criteria met                 | Close               | Complete                       |

---

# 31. Workflow Success Criteria

The Service Request workflow is design-ready when:

* catalog items have owners
* required intake data is defined
* approval logic is defined
* fulfillment groups are defined
* task patterns are defined
* SLA targets are defined
* waiting behavior is defined
* rejection and cancellation paths are defined
* temporary-access behavior is defined
* automation exceptions are defined
* closure criteria are documented
* test scenarios exist

---

# 32. Service Request Management Conclusion

The target request workflow takes work that is already repeatable and makes the process around it predictable.

Users should know what they are requesting.

Approvers should know what decision they are making.

Fulfillment teams should know what they own.

Management should be able to see where the process is slowing down.

The service request process should not make simple work complicated.

It should make repeatable work consistent.

**Next:** [Change Management](./change%20management.md)
