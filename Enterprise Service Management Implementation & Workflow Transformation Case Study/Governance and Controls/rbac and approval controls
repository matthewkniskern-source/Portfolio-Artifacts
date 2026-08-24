# RBAC and Approval Controls

## Purpose

This artifact defines how roles, permissions, approvals, and separation-of-duty rules are applied across the target Enterprise Service Management environment.

The goal is not to build a permission model so complicated that no one can explain it.

The goal is to make sure users can do the work their role requires without being able to bypass the controls that matter.

The operating principle is:

> **Access should follow responsibility, and approval should represent a real decision.**

This artifact builds on:

* [Governance Model](./governance%20model.md)
* [Target Operating Model](../03%20Target%20Service%20Model/target%20operating%20model.md)
* [Service Request Management](../04%20Workflow%20Design/service%20request%20management.md)
* [Change Management](../04%20Workflow%20Design/change%20management.md)
* [Nonfunctional Requirements](../02%20Requirements%20Discovery/nonfunctional%20requirements.md)

---

# 1. RBAC Design Objectives

The role model should support:

* least privilege
* separation of duties where required
* clear administrative boundaries
* restricted access to sensitive records
* controlled priority override
* controlled approval authority
* auditable privilege assignment
* periodic access review

The platform should make the common path easy.

It should make the high-risk path controlled.

---

# 2. Core Roles

The initial RBAC model uses the following roles.

| Role                          | Primary Purpose                               |
| ----------------------------- | --------------------------------------------- |
| Requester                     | Submit and view own service activity          |
| Service Desk Analyst          | Triage, classify, resolve, assign             |
| Specialist Resolver           | Work technical records within assigned scope  |
| Support Group Lead            | Manage queue and operational escalation       |
| Service Owner                 | Govern service-level decisions                |
| Approver                      | Authorize defined transactions                |
| Change Authority              | Authorize applicable changes                  |
| Security / Risk Reviewer      | Review controlled or sensitive activity       |
| Platform Administrator        | Configure platform behavior                   |
| Auditor / Reviewer            | Read control evidence and audit history       |
| Vendor / External Participant | Restricted external interaction where enabled |

These are logical roles.

A specific platform may implement them through groups, profiles, permission sets, or another mechanism.

---

# 3. Permission Model

Permissions should be granted by role rather than individually wherever practical.

Representative permission categories include:

* create
* read
* update
* assign
* approve
* override
* administer
* audit
* export
* delete / retire

High-risk permissions should be more restricted than ordinary update access.

For example:

A Service Desk Analyst may update priority inputs.

They should not automatically have permission to change the priority model itself.

---

# 4. Core RBAC Matrix

| Action                   | Requester | Service Desk | Specialist | Group Lead | Service Owner | Approver | Change Authority | Platform Admin |     Auditor |
| ------------------------ | --------: | -----------: | ---------: | ---------: | ------------: | -------: | ---------------: | -------------: | ----------: |
| Create Incident          |         ✓ |            ✓ |          ✓ |          ✓ |             ✓ |          |                  |              ✓ |             |
| Create Service Request   |         ✓ |            ✓ |          ✓ |          ✓ |             ✓ |          |                  |              ✓ |             |
| View Own Requests        |         ✓ |            ✓ |          ✓ |          ✓ |             ✓ |          |                  |              ✓ |          ✓* |
| View Assigned Queue      |           |            ✓ |          ✓ |          ✓ |             ✓ |          |                  |              ✓ |          ✓* |
| Update Assigned Ticket   |           |            ✓ |          ✓ |          ✓ |               |          |                  |              ✓ |             |
| Reassign Ticket          |           |            ✓ |          ✓ |          ✓ |               |          |                  |              ✓ |             |
| Override Priority        |           |      Limited |            |          ✓ |       Limited |          |                  |              ✓ |       Audit |
| Approve Service Request  |           |              |            |    Limited |       Limited |        ✓ |                  |                |       Audit |
| Approve High-Risk Change |           |              |            |            |             ✓ |          |                ✓ |                |       Audit |
| Change RBAC              |           |              |            |            |               |          |                  |              ✓ |       Audit |
| Modify Workflow          |           |              |            |            |               |          |                  |              ✓ |       Audit |
| View Audit History       |           |      Limited |    Limited |    Limited |             ✓ |  Limited |                ✓ |              ✓ |           ✓ |
| Access Sensitive Records |  Own only |      Limited |     Scoped |     Scoped |        Scoped |   Scoped |           Scoped |          Admin | Audit scope |

* Auditor access is read-only and scope controlled.

The matrix is intentionally simplified.

Detailed permissions should be based on actual process need rather than job title alone.

---

# 5. Requester Controls

A requester should generally be able to:

* create service records
* view their own requests
* add requested information
* view appropriate status
* respond to approval or fulfillment questions where applicable
* submit feedback

A requester should not generally be able to:

* alter approval history
* assign support groups
* modify SLA logic
* override priority
* access restricted tickets unrelated to them
* alter audit evidence

---

# 6. Service Desk Controls

The Service Desk should be able to:

* triage
* classify
* assign
* update
* resolve
* communicate
* associate assets or CIs
* link knowledge
* initiate escalation

More sensitive actions should be restricted.

Examples:

* priority override may require elevated role
* privileged-access approval should not be available
* platform configuration should remain separate

The Service Desk needs enough authority to keep work moving without quietly becoming a governance authority.

---

# 7. Specialist Resolver Controls

Specialist teams should have access to records relevant to their technical scope.

Typical permissions include:

* update assigned records
* add technical notes
* associate CIs
* request consultation
* reassign where permitted
* resolve work
* create change or knowledge candidates

They should not automatically receive:

* broad platform administration
* unrestricted sensitive-record access
* approval rights unrelated to their role

---

# 8. Support Group Lead Controls

Group leads may have additional operational authority such as:

* queue reassignment
* escalation
* priority override where authorized
* backlog review
* SLA exception initiation
* workload reporting

These permissions should remain operational.

They should not automatically extend into:

* privileged access approval
* high-risk change approval
* production workflow administration

---

# 9. Service Owner Controls

Service Owners may be authorized to:

* approve service-specific requests
* define or approve SLA expectations
* review service risk
* participate in high-risk change approval
* review recurring service issues
* approve service-specific exceptions

Service ownership creates accountability.

It does not automatically create unrestricted platform administration.

---

# 10. Approver Role

An Approver should only be able to act on requests for which they have valid authority.

The platform should evaluate where practical:

* approval type
* service
* requester relationship
* organizational role
* system ownership

Approval should be scoped.

A person authorized to approve equipment does not automatically become authorized to approve privileged system access.

---

# 11. Change Authority

Change Authority is separate from ordinary technical implementation.

The role may approve:

* medium-risk Normal Changes
* high-risk Normal Changes
* Emergency Changes depending on policy

The authority should be defined by:

* change risk
* service
* organizational policy

A technical expert may advise on a change without being the final approver.

---

# 12. Platform Administrator

Platform Administrator is a privileged role.

It may include authority to modify:

* workflows
* forms
* routing
* RBAC
* SLA rules
* integrations
* automation
* reports
* reference data

Because these changes can alter business behavior, platform administration should be tightly governed.

At minimum:

* admin access is limited
* access is reviewed
* production changes are logged
* material changes follow change control
* administrative activity is auditable

---

# 13. Auditor / Reviewer

The Auditor role should provide read access to relevant evidence without permitting operational alteration.

Typical access includes:

* approval history
* change history
* audit logs
* access-review evidence
* exception history
* configuration change evidence

Audit access should also respect sensitive-data boundaries.

Read-only does not automatically mean unrestricted.

---

# 14. Vendor / External Role

Where vendors are allowed direct platform access, permissions should be highly restricted.

Potential capabilities include:

* view assigned vendor task
* add approved technical update
* upload support evidence
* view limited related service context

Vendors should not receive broad access to:

* unrelated tickets
* internal approvals
* sensitive user information
* unrestricted CI data
* administrative controls

If direct access is unnecessary, internal personnel should maintain the authoritative ESM record instead.

---

# 15. Approval Control Model

Approval workflows should distinguish three things:

1. who requested the action
2. who is authorized to approve it
3. who fulfills it

Example:

```text id="p47fo2"
Requester
   ↓
Approver
   ↓
Fulfillment Group
```

These roles may overlap for low-risk activity where policy permits.

Higher-risk transactions require stronger separation.

---

# 16. Approval Levels

The target model uses three reusable approval patterns.

| Level | Approval Pattern                  | Example                     |
| ----- | --------------------------------- | --------------------------- |
| A0    | No manual approval                | Approved standard software  |
| A1    | Single authorized approval        | Shared mailbox              |
| A2    | Multi-party / controlled approval | Privileged or vendor access |

This keeps approval logic reusable rather than designing every request from scratch.

---

# 17. A0 — No Manual Approval

A0 applies where:

* request is low risk
* eligibility is clear
* cost or entitlement is already governed
* no independent business decision is required

Example:

```text id="dp41dk"
Standard Software
      ↓
Eligibility Check
      ↓
Fulfill
```

Removing unnecessary approval is itself a process improvement.

---

# 18. A1 — Single Approval

A1 applies where one accountable decision is sufficient.

Examples:

* shared mailbox
* nonstandard equipment
* selected application access

Example:

```text id="mrg5me"
Request
  ↓
Manager / Service Owner
  ↓
Approve / Reject
  ↓
Fulfillment
```

---

# 19. A2 — Controlled Approval

A2 applies where risk, privilege, or external access requires multiple perspectives.

Example:

```text id="xuao6n"
Privileged Access
      ↓
Manager / Sponsor
      ↓
System Owner
      ↓
Security / Access Authority
      ↓
Fulfillment
```

Not every A2 request must use exactly three approvers.

The pattern means stronger, structured authorization applies.

---

# 20. Self-Approval Prevention

For controlled request types, the platform shall prevent a requester from approving their own request.

This applies at minimum to:

* privileged access
* vendor access
* high-risk changes where requester approval conflict exists
* other defined sensitive requests

Example:

```text id="218awv"
Requester = Approver?
    ↙          ↘
  Yes           No
   ↓             ↓
 Block         Continue
```

The blocked attempt should be auditable.

---

# 21. Delegated Approval

Delegation may be necessary during:

* leave
* absence
* temporary role coverage

Delegation should be:

* time-bound
* authorized
* scoped
* auditable

Delegation should not silently convert into permanent approval authority.

---

# 22. Approval Escalation

Unanswered approvals should follow a defined path.

Example:

```text id="9wvs60"
Approval Pending
      ↓
Reminder
      ↓
Escalation
      ↓
Delegate / Higher Authority
      ↓
Decision / Expiration
```

The requester should not have to manually chase the approver indefinitely.

---

# 23. Approval Expiration

Some approval requests should expire if no decision is made within a defined period.

This may be appropriate where:

* requested date has passed
* business need has changed
* temporary access window is no longer valid

Expired approval should not automatically mean approved or denied.

It means the request must be revalidated.

---

# 24. Approval Evidence

Every controlled approval should retain:

* parent record
* approver
* approval type
* decision
* timestamp
* comments where required

Where the request changes materially after approval, the workflow should determine whether reapproval is required.

Approval should apply to the thing that was actually authorized.

---

# 25. Material Change After Approval

Example:

```text id="1iovyn"
Access Request
     ↓
Approved for Read-Only
     ↓
Request Changed to Admin
     ↓
Reapproval Required
```

The platform should not treat the original approval as blanket authorization for a materially different request.

---

# 26. Privileged Access Controls

Privileged access requires:

* named user
* system
* privilege level
* business justification
* authorized approver
* fulfillment evidence
* expiration where temporary
* audit history

Additional controls may include:

* MFA
* separate admin identity
* session logging
* periodic review

These supporting technical controls may exist outside the ESM platform.

The ESM workflow remains the authorization and accountability record.

---

# 27. Vendor Access Controls

Vendor access requires:

* named vendor
* individual identity where practical
* internal sponsor
* target system
* requested privilege
* business purpose
* approval
* start
* expiration

Example:

```text id="i5cct7"
Vendor Request
    ↓
Sponsor
    ↓
System Owner
    ↓
Security / Access Approval
    ↓
Provision
    ↓
Expiration
```

An extension requires a new or renewed approval decision.

---

# 28. Approval and Fulfillment Separation

The platform should distinguish between:

**Authorization**

and:

**Execution**

Example:

```text id="rlttpe"
Security Approves Access
          ↓
Identity Team Provisions
```

The same team may participate in both processes.

The approval record should still show who made the decision and who performed the technical action.

---

# 29. Sensitive Record Access

Some records may require restricted visibility.

Examples include:

* privileged-access requests
* security incidents
* sensitive HR-related requests
* vendor credentials or access information
* selected executive or legal matters

Access restrictions may be based on:

* role
* support group
* service
* sensitivity
* direct participation

Sensitive status should not simply rely on technicians remembering not to share information.

---

# 30. Priority Override Permissions

Priority override should be limited to designated roles such as:

* support group lead
* service owner
* service-management authority

The platform should retain:

* calculated priority
* new priority
* reason
* actor
* time

A technician may recommend escalation without necessarily having override permission.

---

# 31. SLA Exception Permissions

SLA exception authority should be limited to designated roles.

Possible authorities include:

* service owner
* process owner
* support management

The person working the ticket should not be able to exclude inconvenient time from SLA reporting without defined authority.

---

# 32. Administrative Separation

Where staffing permits, the target model should distinguish:

* platform configuration
* control approval
* operational use
* audit review

Example:

```text id="77l6zv"
Process Owner
      ↓ approves rule

Platform Admin
      ↓ configures rule

UAT Owner
      ↓ validates rule

Auditor
      ↓ reviews evidence
```

For a midsize organization, perfect personnel separation may not always be practical.

Where roles overlap, auditability and management review become more important.

---

# 33. Access Lifecycle

Platform roles should follow a lifecycle.

```text id="83jigb"
Request
  ↓
Approve
  ↓
Provision
  ↓
Use
  ↓
Review
  ↓
Modify / Revoke
```

Triggers for review include:

* job change
* team transfer
* termination
* role change
* temporary assignment expiration

---

# 34. Periodic Role Review

At minimum, periodic review should include:

* platform administrators
* approvers
* change authorities
* sensitive support groups
* audit roles
* external/vendor users

Review should confirm:

* user is active
* business role remains valid
* permission level is still appropriate
* temporary access has expired

---

# 35. RBAC Exceptions

If standard RBAC cannot support a legitimate business need, an exception should require:

* business justification
* requested permission
* risk review where applicable
* owner
* approval
* expiration where temporary

An RBAC exception should not become a workaround for poor role design.

Repeated exceptions should trigger role-model review.

---

# 36. RBAC and Approval Controls

| Control ID | Control                          | Type                    |
| ---------- | -------------------------------- | ----------------------- |
| AC-01      | Role-based permission assignment | Preventive              |
| AC-02      | Self-approval prevention         | Preventive              |
| AC-03      | Restricted privileged approval   | Preventive              |
| AC-04      | Time-bound vendor access         | Preventive              |
| AC-05      | Approval history retention       | Detective               |
| AC-06      | Periodic role review             | Detective               |
| AC-07      | Priority override restriction    | Preventive              |
| AC-08      | SLA exception restriction        | Preventive              |
| AC-09      | Administrative change logging    | Detective               |
| AC-10      | Access revocation / correction   | Corrective              |
| AC-11      | Approval escalation              | Corrective              |
| AC-12      | RBAC exception expiration        | Preventive / Corrective |

These controls will be consolidated in:

[Control Matrix](./control%20matrix.md)

---

# 37. Decision Table

| Condition                   | Control Response                       |
| --------------------------- | -------------------------------------- |
| Standard low-risk request   | A0 or A1                               |
| Privileged request          | A2                                     |
| Requester equals approver   | Block where controlled                 |
| Approver unavailable        | Authorized delegation / escalation     |
| Request materially changes  | Reapproval                             |
| Vendor access requested     | Sponsor + scoped approval + expiration |
| Temporary role granted      | Expiration required                    |
| SLA exception requested     | Authorized role only                   |
| Priority override requested | Authorized role + reason               |
| User changes job            | Role review                            |
| User leaves organization    | Revoke access                          |

---

# 38. Testing Mapping

Representative tests include:

| Test ID    | Scenario                                             |
| ---------- | ---------------------------------------------------- |
| TC-RBAC-01 | Requester cannot access unrelated restricted ticket  |
| TC-RBAC-02 | Service Desk can update but not administer workflow  |
| TC-RBAC-03 | Specialist access limited to permitted service scope |
| TC-RBAC-04 | Unauthorized user cannot approve privileged request  |
| TC-RBAC-05 | Requester cannot self-approve A2 request             |
| TC-RBAC-06 | Delegated approver access expires                    |
| TC-RBAC-07 | Material request change triggers reapproval          |
| TC-RBAC-08 | Vendor role cannot view unrelated internal records   |
| TC-RBAC-09 | Admin role assignment appears in access review       |
| TC-RBAC-10 | Revoked user loses privileged role                   |
| TC-REQ-03  | Prohibited self-approval                             |
| TC-VND-02  | Vendor access expiration                             |

These will be formalized in:

[Testing and UAT](../09%20Testing%20and%20UAT/test%20cases.md)

---

# 39. RBAC Metrics

| Metric                               | Purpose                          |
| ------------------------------------ | -------------------------------- |
| Privileged Role Count                | Track elevated platform access   |
| Access Review Completion             | Validate periodic review         |
| Self-Approval Blocks                 | Validate separation control      |
| Approval Exception Rate              | Identify governance pressure     |
| Temporary Role Expiration Compliance | Validate lifecycle               |
| Vendor Access Expiration Compliance  | Validate external access control |
| RBAC Exception Count                 | Identify poor role fit           |
| Inactive User Role Count             | Detect access-cleanup failure    |

---

# 40. Design Guardrails

## Do Not Assign Permissions Individually Without Need

Individual permission grants become difficult to review and maintain.

Use roles and groups where possible.

---

## Do Not Confuse Technical Expertise With Approval Authority

Knowing how to perform the work does not automatically mean someone is authorized to approve it.

---

## Do Not Over-Control Routine Work

A control model that requires three approvals for a standard mouse replacement will not survive contact with actual users.

---

## Do Not Treat Read Access as Harmless

Sensitive records may expose operational, security, personnel, or vendor information even if the user cannot modify them.

---

## Do Not Let Temporary Roles Become Permanent

Temporary privilege should have a defined end condition.

---

# 41. Success Criteria

The RBAC and approval model is design-ready when:

* core roles are defined
* permissions are mapped
* sensitive-record boundaries are defined
* approval levels are defined
* approver authority is scoped
* self-approval rules are defined
* delegated approval is governed
* privileged-access controls are defined
* vendor-access controls are defined
* priority and SLA exception authority is defined
* platform admin access is controlled
* periodic review is defined
* representative tests exist

---

# 42. RBAC and Approval Conclusion

The target model is not trying to lock every user into the smallest possible box.

It is trying to establish clear boundaries around the decisions that matter.

Support teams need enough access to do their jobs.

Approvers need authority that matches the decisions they are responsible for.

Platform administrators need enough privilege to maintain the system without quietly becoming the source of business policy.

And controlled actions need enough separation that an approval actually means something.

That is the balance this model is designed to maintain.

**Next:** [Control Matrix](./control%20matrix.md)
