# Ownership and Escalation

## Purpose

The ownership and escalation model defines who is responsible for moving service work forward, when that responsibility changes, and how additional technical or management attention is introduced without creating ambiguity.

The current-state environment relies heavily on informal handoffs.

A technician receives a request, forwards it to someone else, messages another team, waits on a vendor, or assumes another group has taken over.

That works until nobody is actually sure who owns the next action.

The target model replaces that ambiguity with a simple rule:

> **Every active record needs a visible owner, even when several teams are involved.**

Escalation should increase capability or visibility.

It should not create an ownership vacuum.

---

# 1. Operating Principles

The target ownership model is built around six principles.

## 1.1 One Active Owner

Every active service record shall have a defined owning support group or process owner.

There may be several participating teams.

There should not be several groups assuming someone else owns the next action.

---

## 1.2 Ownership and Assignment Are Different

Group ownership identifies the team accountable for progressing the record.

Individual assignment identifies the person currently working it.

Example:

```text
Owning Group: Network Support
Assigned Technician: J. Rivera
```

If the technician becomes unavailable, the group still owns the work.

This prevents individual absence from turning into process ambiguity.

---

## 1.3 Escalation Does Not Automatically Transfer Ownership

A ticket may be escalated technically or hierarchically without changing the current owner.

Ownership changes only when the workflow deliberately reassigns the record.

This distinction matters.

Notification is not reassignment.

Consultation is not reassignment.

Management visibility is not reassignment.

---

## 1.4 Handoffs Require Context

A handoff should transfer enough information for the receiving group to continue the work without rebuilding the case from scratch.

Required handoff information may include:

* current issue
* business impact
* troubleshooting performed
* findings
* affected service or CI
* reason for reassignment
* expected next action

A ticket should not be transferred with a note that effectively says:

> "Not ours."

---

## 1.5 External Dependency Does Not Remove Internal Accountability

A vendor, user, approver, or other external dependency may block progress.

The internal service record still retains an accountable owner.

Status can change.

Responsibility does not disappear.

---

## 1.6 Escalation Should Be Actionable

An escalation should answer:

* why escalation occurred
* who is expected to respond
* what decision or action is needed
* whether ownership changed
* what happens if no response occurs

Escalation that produces only another notification adds noise rather than control.

---

# 2. Ownership Model

The target model recognizes several distinct ownership roles.

| Role                    | Responsibility                                         |
| ----------------------- | ------------------------------------------------------ |
| Service Owner           | Accountable for overall service performance            |
| Process Owner           | Accountable for lifecycle design and governance        |
| Owning Support Group    | Accountable for moving an active record forward        |
| Assigned Technician     | Performs current work                                  |
| Approver                | Makes a defined authorization decision                 |
| Internal Vendor Sponsor | Maintains accountability for vendor-supported activity |
| Platform Administrator  | Maintains approved workflow configuration              |
| Escalation Owner        | Responds to defined management or service escalation   |

These roles may overlap in smaller organizations, but their responsibilities should remain conceptually separate.

---

# 3. Service Ownership

Each supported service should have an accountable service owner.

The service owner is responsible for:

* service definition
* service expectations
* escalation policy
* support relationships
* service-level review
* approval policy where applicable
* recurring performance issues
* improvement decisions

The service owner does not become the automatic ticket owner.

Example:

```text
Business Email Service
        │
        ├── Service Owner
        │
        ├── Service Desk
        │
        ├── Messaging Support
        │
        ├── Identity and Access
        │
        └── External Vendor
```

Several groups may support the service.

One role remains accountable for how the service performs overall.

---

# 4. Support Group Ownership

Each support group should have a defined service scope.

Representative groups include:

* Service Desk
* Endpoint Support
* Network Support
* Infrastructure Support
* Application Support
* Identity and Access
* Platform Administration

Each group should define:

* supported services
* supported categories
* intake conditions
* escalation targets
* transfer conditions
* responsible lead
* queue monitoring responsibility

This supports both manual and automated routing.

Related design:

[Target Operating Model](./target%20operating%20model.md)

---

# 5. Initial Ownership Matrix

| Work Type                 | Initial Owner                     | Possible Next Owner                | Service Owner           |
| ------------------------- | --------------------------------- | ---------------------------------- | ----------------------- |
| General Incident          | Service Desk                      | Specialist Support                 | Relevant Service Owner  |
| Endpoint Incident         | Service Desk / Endpoint           | Endpoint Support                   | Endpoint Service Owner  |
| Network Incident          | Service Desk                      | Network Support                    | Network Service Owner   |
| Application Incident      | Service Desk                      | Application Support                | Application Owner       |
| Standard Service Request  | Catalog Fulfillment Group         | Specialist Fulfillment             | Relevant Service Owner  |
| Privileged Access Request | Identity / Access                 | Security / System Owner            | Access / System Owner   |
| Standard Change           | Change Implementer / Owning Group | Technical Support                  | Relevant Service Owner  |
| High-Risk Change          | Change Owner                      | Change Authority / Technical Teams | Relevant Service Owner  |
| Knowledge Article         | Article Owner                     | Reviewer                           | Knowledge Process Owner |
| Vendor-Supported Incident | Internal Support Group            | Vendor Dependency                  | Relevant Service Owner  |

This matrix establishes a default.

Detailed workflow logic determines when ownership changes.

---

# 6. Initial Assignment

Assignment occurs after sufficient intake information is available.

Target logic:

```text
Record Created
      ↓
Classify Work
      ↓
Identify Service / Category
      ↓
Determine Owning Group
      ↓
Assign Group
      ↓
Optional Individual Assignment
```

Where reliable rules exist, group assignment may be automated.

Where confidence is low, the record may enter a controlled triage queue instead of being automatically sent to the wrong team.

That is preferable to automating reassignment loops.

---

# 7. Triage Ownership

The Service Desk owns initial triage for general incidents and requests that do not enter through a dedicated catalog workflow.

Triage responsibilities include:

* confirm record type
* validate minimum information
* identify likely service
* determine impact and urgency
* resolve when possible
* assign correct support group

The service desk should not become permanent ownership for every ticket simply because it was the first team involved.

Its role is to resolve appropriate work and route the rest cleanly.

---

# 8. Reassignment

Reassignment transfers active ownership from one support group to another.

The platform shall record:

* previous group
* destination group
* reason
* actor
* timestamp

Representative reassignment reasons include:

* incorrect initial classification
* specialist expertise required
* service ownership transfer
* escalation
* fulfillment dependency

A destination group must be identified before ownership changes.

The record should not enter an unowned intermediate state.

Related requirements:

* FR-08 — Owning Support Group
* FR-09 — Assignment History
* FR-10 — Reassignment Reason

---

# 9. Reassignment Acceptance

For higher-impact work or complex inter-team transfers, the target process may require explicit receiving-group acknowledgement.

Example:

```text
Network Support
      ↓
Reassignment to Infrastructure
      ↓
Infrastructure Accepts
      ↓
Ownership Transfers
```

If the receiving group rejects the transfer, the original owner remains accountable until routing is resolved.

This prevents tickets from being passed back and forth without clear responsibility.

The implementation should use this control selectively.

Requiring formal acceptance for every low-risk reassignment would add unnecessary overhead.

---

# 10. Handoff Standard

A meaningful handoff should contain enough information for the receiving team to continue.

Minimum handoff content may include:

| Field                     | Purpose                                      |
| ------------------------- | -------------------------------------------- |
| Current Condition         | What is happening now                        |
| Business Impact           | Why it matters                               |
| Troubleshooting Completed | Prevent repeated work                        |
| Findings                  | What has been learned                        |
| Related Service / CI      | Provide operational context                  |
| Reassignment Reason       | Explain why ownership is changing            |
| Expected Next Action      | Clarify what the receiving group needs to do |

A strong handoff saves time.

A weak handoff just moves the delay somewhere else.

---

# 11. Functional Escalation

Functional escalation introduces additional technical capability.

It may involve:

* more specialized support group
* senior technical resource
* engineering
* vendor support
* product specialist

Example:

```text
Service Desk
     ↓
Application Support
     ↓
Database Support
     ↓
External Vendor
```

Functional escalation may or may not change ownership.

## Consultation

Another team provides expertise while the current group remains owner.

## Transfer

The receiving team becomes the new owner.

The distinction should be explicit.

---

# 12. Consultation Model

Not every request for help should trigger reassignment.

A consultation allows another group to contribute without transferring ownership.

Example:

```text
Application Support
        │
        ├── Owns Incident
        │
        └── Requests Network Consultation
                       ↓
                 Network Findings
                       ↓
                Application Support
```

This is especially useful when:

* the likely cause is still uncertain
* several teams need to collaborate
* ownership of the affected service remains clear

Consultation reduces unnecessary assignment churn.

---

# 13. Hierarchical Escalation

Hierarchical escalation increases management or service-owner visibility.

Typical triggers include:

* SLA risk
* SLA breach
* high business impact
* unresolved ownership conflict
* repeated reassignment
* extended vendor dependency
* high-risk exception
* major incident declaration

Example:

```text
Assigned Technician
       ↓
Group Lead
       ↓
Service Owner
       ↓
IT Management
```

Hierarchical escalation normally does not transfer technical ownership.

The support team still owns the work unless a deliberate transfer occurs.

---

# 14. Time-Based Escalation

The SLA model provides time-based escalation thresholds.

Standard model:

```text
Ticket Active
     ↓
75% SLA
     ↓
Support Group Warning
     ↓
90% SLA
     ↓
Group Lead
     ↓
100% SLA
     ↓
Service Owner / Management
```

P1 incidents follow a faster and more active escalation model.

See:

[Priority and SLA Model](./priority%20and%20sla%20model.md)

---

# 15. Priority-Based Escalation

High-priority incidents receive escalation independent of ticket age.

## P1

Immediate:

* owning group notification
* technical lead engagement
* service owner visibility
* management communication
* defined update cadence

## P2

Accelerated:

* owning group priority
* lead visibility
* SLA monitoring
* service-owner escalation if performance risk increases

## P3 / P4

Standard queue management and SLA-based escalation.

This prevents the organization from waiting for a P1 SLA clock to get close to breach before treating it like a critical event.

---

# 16. Major Incident Escalation

A P1 incident may be designated as a Major Incident when organizational coordination is required beyond standard technical escalation.

Potential criteria include:

* critical business service unavailable
* broad organizational impact
* multiple facilities affected
* severe security or operational consequence
* significant external/customer effect

Major Incident handling may introduce:

* incident coordinator
* technical workstream leads
* service owner
* communications lead
* management stakeholders

Example:

```text
Major Incident
      ↓
Incident Coordinator
      │
 ┌────┼─────┐
 ↓    ↓     ↓
Network App Infrastructure
  Team Team     Team
      │
      ↓
Central Status / Communication
      ↓
Service Restoration
      ↓
Review
```

This case study does not attempt to build a complete Major Incident Management framework.

The objective is to establish the escalation relationship to the core incident workflow.

---

# 17. Ownership During Approval

An approval requirement does not remove request ownership.

Example:

```text
Service Request
      ↓
Fulfillment Group Owns
      ↓
Pending Approval
      ↓
Approver Decision
      ↓
Fulfillment Group Continues
```

During approval:

* the fulfillment group remains operationally accountable
* the approver owns the decision
* the platform tracks approval aging
* escalation may occur if approval is delayed

This makes it possible to separate technical delay from approval delay later in reporting.

---

# 18. Approval Escalation

Approval workflows should include defined behavior when no decision is made.

Example:

```text
Approval Requested
      ↓
Reminder
      ↓
Escalation
      ↓
Delegate / Manager / Process Owner
      ↓
Decision or Expiration
```

Possible outcomes include:

* reminder
* escalation
* delegation
* request expiration
* cancellation

The process should not leave requests permanently sitting in `Pending Approval`.

---

# 19. Ownership During User Dependency

When the organization is waiting for requester information:

```text
Support Group Owns
       ↓
Waiting on User
       ↓
Requester Response
       ↓
Support Resumes
```

The user does not become the ticket owner.

The support group remains accountable for:

* tracking the request
* sending reminders
* applying closure or cancellation rules
* resuming work when information arrives

This distinction is important for reporting and accountability.

---

# 20. User Response Escalation

The target model may use:

| Condition                           | Action                                |
| ----------------------------------- | ------------------------------------- |
| Initial information request         | User notification                     |
| No response after defined period    | Reminder                              |
| Continued no response               | Final notice                          |
| No response after closure threshold | Resolve / cancel under defined policy |

Any automatic closure behavior should preserve:

* notification history
* reason
* reopen option where appropriate

Automation should reduce forgotten tickets without making it easy to close inconvenient work.

---

# 21. Ownership During Vendor Dependency

Vendor dependency follows the same principle.

```text
Internal Support Group
        ↓
Vendor Needed
        ↓
Vendor Case Open
        ↓
Internal Owner Retained
        ↓
Vendor Response
        ↓
Internal Validation
        ↓
Resolution
```

The vendor owns its contractual action.

The internal group owns the organization's service record.

Required vendor information may include:

* vendor
* case number
* latest update
* next follow-up
* escalation contact
* expected action

Related design:

[Service Catalog — Temporary Vendor Access](./service%20catalog.md)

---

# 22. Vendor Escalation

Vendor escalation may occur based on:

* contractual response target
* prolonged dependency
* high service impact
* failed support response
* P1/P2 condition

Example:

```text
Vendor Case
    ↓
Standard Support
    ↓
Vendor SLA Risk
    ↓
Vendor Escalation
    ↓
Account / Support Management
```

Internal management visibility may increase at the same time.

The internal ticket should record enough information to show that external escalation occurred.

---

# 23. Ownership During Change

Change Management introduces several roles:

| Role                        | Responsibility                   |
| --------------------------- | -------------------------------- |
| Change Requester            | Initiates change                 |
| Change Owner                | Accountable for change lifecycle |
| Implementer                 | Performs technical activity      |
| Approver / Change Authority | Authorizes                       |
| Service Owner               | Represents affected service      |
| Validator                   | Confirms outcome                 |

These roles may be filled by the same individual for low-risk standard changes where policy allows.

Higher-risk changes require stronger separation.

Detailed workflow:

[Change Management](../04%20Workflow%20Design/change%20management.md)

---

# 24. Failed Change Escalation

If a change fails:

```text
Implementation
      ↓
Failure Detected
      ↓
Backout Required?
   ↙             ↘
 Yes              No
  ↓                ↓
Backout        Stabilization
  ↓                ↓
Validation ←───────┘
      ↓
Incident Required?
      ↓
Change Review
```

Ownership remains with the Change Owner until:

* service is stabilized
* required incident ownership is established
* change outcome is documented
* review requirements are assigned

A failed change should not simply disappear into a newly created incident.

Both records remain connected.

---

# 25. Ownership Conflict

Disagreement between support groups is inevitable.

The target model needs a defined way to resolve it.

Example:

```text
Group A
  ↓
Attempts Transfer
  ↓
Group B Rejects
  ↓
Ownership Conflict
  ↓
Service Desk Lead /
Process Owner / Service Owner
  ↓
Ownership Decision
```

While the conflict is being resolved, the record retains an owner.

The system should not permit a dispute over responsibility to become a reason no one progresses the work.

---

# 26. Escalation for Reassignment Loops

Repeated reassignment is itself an operational signal.

Example threshold:

| Condition           | Action                      |
| ------------------- | --------------------------- |
| First reassignment  | Normal workflow             |
| Second reassignment | Queue visibility            |
| Third reassignment  | Group lead / process review |

The exact threshold would be validated during implementation.

The principle is that repeated transfer should eventually trigger review rather than continue indefinitely.

This supports later analysis of:

* poor categorization
* unclear ownership
* bad routing rules
* training gaps

---

# 27. Ownership Transition Rules

A valid ownership transition should meet four conditions.

### 1. Destination Identified

A specific support group or process owner is selected.

### 2. Reason Identified

The transfer has a documented business or technical reason.

### 3. Context Available

The receiving team has enough information to continue.

### 4. History Preserved

Previous ownership remains visible.

These conditions apply whether reassignment occurs manually or automatically.

---

# 28. Automation and Ownership

Automation may support:

* initial routing
* assignment based on service
* assignment based on location
* escalation notification
* approval routing
* vendor follow-up reminders
* queue-aging alerts

Automation should not create hidden ownership changes.

Material automated reassignment should remain visible in assignment history.

If automated routing repeatedly produces incorrect assignments, the rule should be corrected rather than expecting technicians to clean it up indefinitely.

Related design:

[Automation Opportunities](../07%20Automation%20and%20AI/automation%20opportunities.md)

---

# 29. AI-Assisted Routing

AI may suggest:

* category
* service
* support group
* duplicate relationship

AI-assisted routing should initially operate as recommendation or low-risk automation where confidence and governance permit.

Example:

```text
Ticket Created
      ↓
AI Routing Suggestion
      ↓
Confidence Threshold
   ↙              ↘
High              Low
 ↓                 ↓
Approved Rule     Triage Queue
 ↓
Assignment
```

High confidence should not become an excuse to automate sensitive ownership or approval decisions without defined controls.

Human correction must remain available.

---

# 30. Ownership and Escalation Controls

| Control                        | Purpose                         |
| ------------------------------ | ------------------------------- |
| Required owning group          | Prevent ownerless records       |
| Assignment history             | Preserve accountability         |
| Reassignment reason            | Identify transfer cause         |
| Selective acceptance           | Prevent inappropriate handoff   |
| Defined escalation path        | Ensure actionable escalation    |
| Internal vendor owner          | Preserve accountability         |
| Approval aging                 | Prevent stalled decisions       |
| Ownership conflict path        | Resolve disputed responsibility |
| Reassignment threshold         | Identify routing problems       |
| Controlled priority escalation | Focus management attention      |

Detailed control ownership will be maintained in:

[Governance and Controls](../06%20Governance%20and%20Controls/governance%20model.md)

---

# 31. Ownership Metrics

The operating model should measure whether ownership is working.

| Metric                        | Purpose                                |
| ----------------------------- | -------------------------------------- |
| Reassignment Rate             | Identify routing or ownership weakness |
| Reassignments per Ticket      | Identify ticket bouncing               |
| Time to Correct Assignment    | Measure routing efficiency             |
| Queue Age                     | Identify neglected work                |
| Unassigned Record Count       | Detect ownership failures              |
| Escalations by Group          | Identify service pressure              |
| Approval Aging                | Identify stalled decisions             |
| Vendor Dependency Time        | Identify external bottlenecks          |
| Ownership Conflict Count      | Identify unclear operating boundaries  |
| Consultation vs Transfer Rate | Understand cross-team collaboration    |

These metrics will feed:

[Performance Framework](../11%20Metrics%20and%20Optimization/performance%20framework.md)

---

# 32. Testing Requirements

Representative tests include:

### TC-OWN-01 — Initial Ownership

Create a standard incident and confirm it receives the expected owning support group.

### TC-OWN-02 — Reassignment

Transfer a ticket between groups and confirm:

* destination required
* reason required
* history retained

### TC-OWN-03 — Ownership Retention During Approval

Move a service request into pending approval and confirm operational ownership remains defined.

### TC-OWN-04 — Vendor Dependency

Move a ticket to vendor-dependent status and confirm the internal owner remains assigned.

### TC-OWN-05 — Ownership Conflict

Simulate rejected reassignment and confirm the ticket does not become unassigned.

### TC-ESC-01 — SLA Escalation

Confirm defined SLA threshold generates the expected hierarchical escalation without unintentionally transferring ownership.

### TC-ESC-02 — Approval Escalation

Confirm unanswered approval follows defined reminder and escalation behavior.

### TC-ESC-03 — Reassignment Loop

Confirm repeated reassignment reaches the configured review threshold.

Tests will be formalized in:

[Testing and UAT](../09%20Testing%20and%20UAT/test%20cases.md)

---

# 33. Ownership Decision Table

| Condition                      | Current Owner         | Action                  | Ownership After Action                      |
| ------------------------------ | --------------------- | ----------------------- | ------------------------------------------- |
| Service desk resolves incident | Service Desk          | Resolve                 | Service Desk until closure                  |
| Specialist consultation needed | Current Support Group | Consult                 | Current Support Group                       |
| Specialist ownership required  | Current Support Group | Reassign                | Receiving Support Group                     |
| Manager notified of SLA risk   | Support Group         | Hierarchical Escalation | Same Support Group                          |
| Approval required              | Fulfillment Group     | Request Approval        | Same Fulfillment Group                      |
| Waiting on user                | Support Group         | Pause / Wait            | Same Support Group                          |
| Waiting on vendor              | Support Group         | Vendor Dependency       | Same Internal Group                         |
| Vendor escalation              | Support Group         | Escalate Vendor         | Same Internal Group                         |
| Change fails                   | Change Owner          | Backout / Incident      | Change Owner + Incident Owner as applicable |
| Ownership dispute              | Current Group         | Escalate Decision       | Current Group until decision                |

This table is intentionally simple.

The target process should make ownership obvious without forcing users to understand every internal relationship.

---

# 34. Current-to-Target Ownership Comparison

| Current State                           | Target State                                |
| --------------------------------------- | ------------------------------------------- |
| Direct technician ownership             | Defined group ownership                     |
| Informal handoff                        | Recorded reassignment                       |
| Forwarding equals transfer              | Transfer requires explicit ownership change |
| Technical question creates reassignment | Consultation available                      |
| Vendor means "waiting"                  | Internal owner retained                     |
| Approval stalls ticket                  | Approval aging and escalation               |
| Management notification unclear         | Defined hierarchical escalation             |
| Reassignment loop continues             | Threshold triggers review                   |
| Ownership dispute delays work           | Defined conflict-resolution path            |
| Limited assignment history              | Full ownership history                      |

A visual comparison will be maintained in:

[Ownership and Escalation Model](../diagrams/ownership%20and%20escalation%20model.md)

---

# 35. Design Guardrails

The ownership model should avoid several predictable problems.

## Queue Dumping

A group should not be able to move work out of its queue simply because another team might be involved.

## Over-Assignment

Every participant does not need to become an assignee.

Consultation and collaboration should remain possible without destroying ownership clarity.

## Escalation Noise

If every ticket generates leadership notifications, escalation loses meaning.

## Ownerless Waiting

`Waiting on User`, `Waiting on Vendor`, and `Pending Approval` describe workflow state.

They are not owners.

## Artificial Reassignment Reduction

A low reassignment rate is not automatically good if teams are holding work they cannot actually resolve.

The objective is correct ownership, not a perfect metric.

---

# 36. Success Criteria

The ownership and escalation model is design-ready when:

* every active workflow state has a defined owner
* support-group scopes are documented
* reassignment rules are defined
* consultation is distinguished from transfer
* escalation paths are defined
* P1 escalation is defined
* approval ownership is defined
* vendor dependency ownership is defined
* ownership conflict has a resolution path
* reassignment history is retained
* ownership metrics are defined
* representative scenarios are testable

At that point, the organization can answer the question that was frequently unclear in the current state:

**Who is responsible for moving this forward right now?**

---

# 37. Ownership and Escalation Conclusion

The target model does not try to prevent work from crossing team boundaries.

That would be unrealistic.

Complex service environments require collaboration, technical escalation, vendors, approvals, and handoffs.

The improvement is that those transitions become deliberate.

A specialist can be consulted without automatically inheriting the ticket.

Management can be escalated without becoming the technical owner.

A vendor can hold the next external action without becoming responsible for the organization's internal service record.

And when ownership does change, the transfer is visible, documented, and traceable.

The basic rule survives every one of those conditions:

> **Someone always owns the next move.**

**Next:** [Incident Management](../04%20Workflow%20Design/incident%20management.md)
