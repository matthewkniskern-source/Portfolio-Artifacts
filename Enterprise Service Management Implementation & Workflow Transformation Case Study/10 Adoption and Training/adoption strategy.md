# Adoption Strategy

## Purpose

This artifact defines how the organization prepares users, support teams, approvers, and service owners to operate the target Enterprise Service Management model successfully after go-live.

A technically correct implementation can still fail if users continue to:

* email individual technicians
* bypass the service catalog
* avoid documenting work
* ignore approval responsibilities
* treat the new platform as additional administrative overhead

Adoption therefore has to address both system use and operating behavior.

The operating principle is:

> **Adoption means the new process becomes the normal way work gets done, not simply that users have access to the new platform.**

This artifact builds on:

* [Implementation Plan](../08%20Implementation%20Plan/implementation%20plan.md)
* [UAT Plan](../09%20Testing%20and%20UAT/uat%20plan.md)
* [Target Operating Model](../03%20Target%20Service%20Model/target%20operating%20model.md)

---

# 1. Adoption Objectives

The adoption strategy should:

* establish clear expectations
* prepare users before go-live
* train by operational role
* reduce dependence on legacy intake
* create visible support during transition
* capture feedback
* identify resistance early
* measure actual behavior after launch
* reinforce the target operating model

The objective is sustained use.

Not training completion alone.

---

# 2. Adoption Audiences

| Audience                | Primary Change                                |
| ----------------------- | --------------------------------------------- |
| End Users               | Use approved intake and self-service          |
| Service Desk            | Operate structured triage and ownership       |
| Specialist Teams        | Work through managed queues and relationships |
| Approvers               | Make timely documented decisions              |
| Support Leads           | Manage escalation and backlog                 |
| Service Owners          | Use SLA, reporting, and governance            |
| Change Authorities      | Apply controlled change decisions             |
| Platform Administrators | Maintain approved configuration               |
| Management              | Reinforce process expectations                |

Each group experiences a different version of the change.

---

# 3. Adoption Risks

Representative risks include:

| Risk                                      | Likely Effect                       |
| ----------------------------------------- | ----------------------------------- |
| Users continue direct technician requests | Work remains outside managed record |
| Technicians accept off-platform work      | Fragmentation continues             |
| Approvers ignore queues                   | Requests stall                      |
| Excessive mandatory data                  | Users enter poor-quality values     |
| Poor catalog design                       | Users avoid self-service            |
| Weak leadership reinforcement             | Legacy behavior returns             |
| Too many notifications                    | Users tune out communication        |
| Training delivered too early              | Knowledge fades before use          |
| Platform viewed as surveillance           | Resistance increases                |

Adoption problems should be treated as implementation issues, not merely user attitude.

---

# 4. Change Message

The core message should remain simple:

The organization is moving from fragmented, person-dependent service handling to a managed service process with:

* one record
* clear ownership
* visible status
* consistent approval
* measurable service performance

The new platform is the mechanism.

The operating change is the real project.

---

# 5. Stakeholder Readiness

Stakeholder groups should be evaluated for:

* awareness
* impact
* authority
* resistance
* training need
* support need

A simple readiness view may use:

| Group            | Impact | Readiness    | Adoption Risk |
| ---------------- | ------ | ------------ | ------------- |
| Service Desk     | High   | Medium       | High          |
| Specialist Teams | High   | Medium       | High          |
| End Users        | Medium | Low / Medium | Medium        |
| Approvers        | Medium | Medium       | High          |
| Service Owners   | High   | Medium       | Medium        |
| Management       | Medium | High         | Medium        |

The exact rating should be updated during implementation.

---

# 6. Adoption Phases

Adoption should follow implementation.

```text
Awareness
   ↓
Preparation
   ↓
Training
   ↓
Go-Live Support
   ↓
Reinforcement
   ↓
Optimization
```

Different communication and support are needed at each stage.

---

# 7. Awareness

Before launch, users should understand:

* why the change is happening
* what problems it is intended to solve
* when it will affect them
* what they will need to do differently

Early awareness should avoid deep technical detail.

The initial message is about the operating change.

---

# 8. Role-Based Preparation

Support teams need more preparation than general users.

Examples include:

## End Users

Need to know:

* where to submit
* how to check status
* when to use self-service

## Service Desk

Need to know:

* triage
* priority
* ownership
* SLA
* closure
* escalation

## Approvers

Need to know:

* what they are authorizing
* expected response time
* delegation
* rejection
* accountability

## Service Owners

Need to know:

* SLA
* exceptions
* reporting
* governance
* service ownership

---

# 9. Champion Model

Selected champions may support adoption within:

* Service Desk
* technical teams
* business units

Champions should:

* understand the target process
* help peers
* identify recurring friction
* escalate design problems
* reinforce approved practice

Champions should not become permanent substitutes for training or support.

---

# 10. Leadership Reinforcement

Management behavior matters.

If leaders continue to:

* bypass the process
* request direct priority escalation
* approve through email
* tolerate undocumented work

users will quickly learn that the official workflow is optional.

Leadership should reinforce:

* approved intake
* documented approvals
* managed escalation
* visible ownership

The operating model needs behavioral support from the same people who approved it.

---

# 11. Legacy Behavior Transition

Legacy behavior will not disappear immediately.

The target response should be predictable.

Example:

```text
Direct Request
     ↓
Managed Record Created
     ↓
User Directed to Standard Channel
```

The organization should avoid both extremes:

* refusing urgent work because the user used the wrong channel
* permanently allowing informal channels to remain the real process

---

# 12. Service Desk Reinforcement

The Service Desk is the most important adoption point.

If the Service Desk consistently:

* creates records
* applies priority correctly
* maintains ownership
* uses knowledge
* follows closure requirements

the rest of the service model becomes much easier to sustain.

If it works around the model, users will follow.

---

# 13. Approver Adoption

Approval workflows fail when approvers:

* do not know they have authority
* ignore notifications
* approve without review
* continue using email or chat

Adoption should include:

* role confirmation
* short training
* escalation
* delegation
* approval aging monitoring

Approval behavior should become part of operational monitoring.

---

# 14. Catalog Adoption

Catalog adoption depends heavily on usability.

The catalog should:

* use language users understand
* expose common services
* avoid excessive options
* request only necessary information
* provide predictable outcomes

Poor catalog adoption may indicate a design problem.

Not simply a communication problem.

---

# 15. Knowledge Adoption

Technicians should be encouraged to:

* search before rebuilding a known solution
* link useful knowledge
* identify stale content
* create candidates from repeatable solutions

Knowledge usage should be integrated into normal work.

It should not depend on a separate documentation campaign.

---

# 16. Training Timing

Training should occur close enough to go-live that participants can use the material.

Recommended sequence:

```text
Awareness
   ↓
Role-Based Training
   ↓
Practice / UAT
   ↓
Go-Live
   ↓
Reinforcement
```

Long gaps between training and actual use reduce retention.

---

# 17. Go-Live Support

During early production, users should have visible support channels.

Examples:

* Service Desk support
* quick-reference material
* designated champions
* hypercare escalation
* targeted office hours where useful

The support model should reduce uncertainty without creating a second unmanaged help process.

---

# 18. Feedback Model

Feedback should distinguish:

* defect
* usability issue
* process gap
* training need
* enhancement
* resistance / adoption issue

Example:

```text
User Feedback
     ↓
Classify
     ↓
Correct Owner
     ↓
Action
```

This prevents every complaint from turning into another configuration change.

---

# 19. Resistance Analysis

Resistance may come from several sources.

| Resistance                        | Likely Root Cause                        |
| --------------------------------- | ---------------------------------------- |
| "The old way was faster"          | Extra steps or weak communication        |
| "I just call my technician"       | Established informal relationship        |
| "Too many fields"                 | Poor form design                         |
| "Approvals take too long"         | Approval ownership / escalation weakness |
| "This is just tracking us"        | Weak explanation of purpose              |
| "The system doesn't fit our work" | Genuine process or requirement gap       |

The response should address the cause rather than dismiss the concern.

---

# 20. Adoption Intervention

If adoption is low:

```text
Low Adoption
    ↓
Determine Why
 ┌──────┼───────┐
 ↓      ↓       ↓
Design Training Reinforcement
 ↓      ↓       ↓
Correct and Measure Again
```

The solution should match the problem.

More training does not fix a bad workflow.

---

# 21. Adoption Metrics

Useful measures include:

| Metric                            | Purpose                            |
| --------------------------------- | ---------------------------------- |
| Managed Intake Rate               | Measure use of approved channels   |
| Direct / Off-Process Request Rate | Identify legacy behavior           |
| Catalog Utilization               | Measure self-service adoption      |
| Training Completion               | Measure preparation                |
| Knowledge Usage                   | Measure technician adoption        |
| Approval Aging                    | Measure approver participation     |
| Reassignment Rate                 | Identify routing or usage problems |
| Required-Field Completion         | Measure process quality            |
| User Satisfaction                 | Measure experience                 |
| Support-Team Feedback             | Identify operational friction      |

Adoption should be measured through behavior as well as sentiment.

---

# 22. Early Adoption Targets

Initial target behavior may include:

* majority of new service activity enters approved channels
* direct technician requests decline
* approval aging stabilizes
* catalog utilization increases
* support teams maintain ownership
* closure quality improves
* knowledge reuse increases

Exact numeric targets should be based on baseline data after implementation.

The case study should not invent precision where no production data exists.

---

# 23. Adoption Dashboard

A simple dashboard may track:

```text
Approved Intake
Catalog Use
Direct Requests
Approval Aging
Knowledge Reuse
Training
CSAT
```

The dashboard should identify where users are reverting to legacy behavior.

---

# 24. Reinforcement

Post-go-live reinforcement may include:

* manager reminders
* targeted retraining
* catalog improvements
* revised quick references
* champion feedback
* workflow correction
* recognition of effective adoption

Reinforcement should become lighter as the process becomes normal.

---

# 25. Adoption and Governance

Persistent bypass behavior may eventually become a governance issue.

Examples include:

* repeated self-approval attempt
* routine off-platform privileged requests
* undocumented production change
* repeated deliberate SLA manipulation

The initial response may be training.

Repeated controlled-process bypass should follow the governance model.

---

# 26. Adoption and Continuous Improvement

Adoption data should feed optimization.

Example:

```text
Low Catalog Use
      ↓
Analyze Cause
      ↓
Poor Search / Poor Language / Missing Item?
      ↓
Improve
      ↓
Measure Again
```

Adoption metrics become another source of requirements after go-live.

---

# 27. Adoption Ownership

| Area                  | Primary Owner                 |
| --------------------- | ----------------------------- |
| Overall Adoption      | Project / Adoption Lead       |
| End-User Behavior     | Business Management           |
| Service Desk Adoption | Service Desk Lead             |
| Specialist Adoption   | Support Group Leads           |
| Approver Adoption     | Process / Service Owners      |
| Training              | Training Lead                 |
| Communications        | Communications / Project Lead |
| Workflow Correction   | Process Owner                 |
| Platform Usability    | Platform Owner                |

Adoption should not become the responsibility of the training team alone.

---

# 28. Adoption Exit from Hypercare

Adoption is stable enough to exit Hypercare when:

* users can access standard intake
* support teams operate core workflow independently
* approvers are responding
* direct legacy intake is declining
* critical usability issues are resolved
* training issues are manageable
* normal operational ownership has taken over

Perfect adoption is not required.

A sustainable operating pattern is.

---

# 29. Adoption Guardrails

## Do Not Treat Training as Adoption

Training teaches the process.

Adoption proves people are using it.

## Do Not Blame Users for Bad Design

Repeated confusion may indicate a workflow or usability issue.

## Do Not Leave Legacy Channels Open Without a Plan

Users will choose the easiest path available.

## Do Not Overcommunicate

Too many messages become noise.

## Do Not Measure Adoption Only by Login Count

Logging in does not mean the service model is being followed.

## Do Not Make Champions Permanent Workarounds

If only champions can make the process work, the process still needs improvement.

---

# 30. Adoption Success Criteria

The adoption strategy is ready when:

* affected audiences are identified
* adoption risks are documented
* stakeholder readiness is understood
* training is role-based
* leadership reinforcement is planned
* legacy behavior handling is defined
* champions are identified where useful
* feedback can be classified
* adoption metrics exist
* remediation paths exist
* post-go-live reinforcement is planned

---

# 31. Adoption Strategy Conclusion

The implementation only becomes successful when the target process stops feeling like a project and starts feeling like the normal way service work is handled.

That will not happen because the platform went live.

It happens when:

* users know where to go
* support teams trust the workflow
* approvers participate
* leaders reinforce the process
* friction is corrected
* legacy workarounds stop being easier than the target model

The goal is not perfect compliance with a new tool.

The goal is a service process people can actually use consistently.

**Next:** [Training Plan](./training%20plan.md)
