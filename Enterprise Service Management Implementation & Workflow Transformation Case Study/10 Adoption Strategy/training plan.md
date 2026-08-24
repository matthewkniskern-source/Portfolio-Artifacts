# Training Plan

## Purpose

This artifact defines the role-based training approach for the target Enterprise Service Management environment.

Training should prepare each audience to perform the parts of the process they actually own.

The objective is not to teach every platform feature to every user.

It is to make sure people know:

* what they are responsible for
* what actions they can take
* what controls they must follow
* where to go when the normal process fails

The operating principle is:

> **Train people for the decisions and tasks they actually perform.**

This artifact builds on:

* [Adoption Strategy](./adoption%20strategy.md)
* [UAT Plan](../09%20Testing%20and%20UAT/uat%20plan.md)
* [Target Operating Model](../03%20Target%20Service%20Model/target%20operating%20model.md)

---

# 1. Training Objectives

Training should ensure that:

* end users can submit and track service activity
* Service Desk staff can triage, route, prioritize, and close work correctly
* specialist teams understand ownership and escalation
* approvers understand their authority and accountability
* service owners can manage SLA and exceptions
* change authorities can apply the change model
* platform administrators understand controlled configuration
* support personnel know how to handle exceptions and failures

Training should reduce both user confusion and process bypass.

---

# 2. Training Audiences

| Audience                | Training Depth |
| ----------------------- | -------------- |
| End Users               | Basic          |
| Service Desk            | Extensive      |
| Specialist Support      | Moderate       |
| Support Group Leads     | Moderate       |
| Approvers               | Focused        |
| Service Owners          | Focused        |
| Change Authorities      | Focused        |
| Platform Administrators | Extensive      |
| Auditors / Reviewers    | Focused        |
| Champions               | Expanded       |

Training depth should follow responsibility.

---

# 3. Training Delivery Model

The target approach uses a mix of:

* short instructor-led sessions
* guided demonstrations
* hands-on practice
* quick-reference guides
* role-based job aids
* recorded walkthroughs where useful
* post-go-live reinforcement

The exact delivery method should fit the audience.

A 10-minute end-user walkthrough may be more effective than a one-hour platform class.

---

# 4. End-User Training

## Objectives

End users should understand how to:

* submit an incident
* submit a service request
* use the service catalog
* provide required information
* check status
* respond to information requests
* use available knowledge
* provide feedback

## Key Message

Users do not need to understand internal routing.

They need to know how to enter the process correctly and how to follow their request.

---

# 5. End-User Training Scope

Recommended topics:

```text id="k6n0gd"
Where to Get Help
      ↓
Incident vs Service Request
      ↓
Submit
      ↓
Track
      ↓
Respond
      ↓
Close / Feedback
```

Training should avoid unnecessary detail about:

* support-group structure
* internal SLA administration
* change governance
* platform configuration

---

# 6. Service Desk Training

The Service Desk requires the deepest operational training.

Key topics include:

* intake
* incident vs request distinction
* categorization
* impact and urgency
* priority
* ownership
* assignment
* reassignment
* SLA
* escalation
* waiting states
* knowledge
* vendor dependency
* resolution
* closure

The Service Desk should also understand which actions require elevated authority.

---

# 7. Service Desk Practice Scenarios

Recommended exercises include:

| Scenario               | Skill                   |
| ---------------------- | ----------------------- |
| Standard Incident      | Intake and ownership    |
| P1 Incident            | Priority and escalation |
| Duplicate Incident     | Relationship management |
| Waiting on Requester   | State handling          |
| Vendor Dependency      | Internal accountability |
| Failed Change Incident | Change correlation      |
| Weak Closure Attempt   | Closure control         |

Training should include at least one failure or exception scenario.

---

# 8. Specialist Support Training

Specialist teams should understand:

* assigned work
* queue ownership
* technical updates
* CI relationships
* consultation vs reassignment
* escalation
* vendor dependency
* change creation
* knowledge contribution
* closure responsibilities

Specialists should not need full Service Desk training unless they regularly perform triage.

---

# 9. Support Group Lead Training

Support leads require additional training on:

* queue health
* reassignment
* escalation
* SLA risk
* priority override
* backlog
* exception handling
* support metrics

They should understand both operational action and governance boundaries.

---

# 10. Approver Training

Approvers should receive short, focused training.

Topics include:

* what they are approving
* what information should be reviewed
* approve vs reject
* comments
* delegation
* expiration
* escalation
* self-approval restrictions

Approver training should emphasize:

> **Approval is a decision, not a notification acknowledgement.**

---

# 11. Service Owner Training

Service Owners should understand:

* service ownership
* SLA expectations
* escalation
* approval responsibility
* service performance
* exception governance
* change impact
* reporting

They do not need platform-administrator training.

They need enough visibility to govern the service they own.

---

# 12. Change Authority Training

Change authorities should understand:

* Standard vs Normal vs Emergency Change
* risk
* approval
* implementation readiness
* backout
* validation
* failed change
* incident linkage
* emergency retrospective review

Training should include at least one failed-change scenario.

---

# 13. Platform Administrator Training

Platform Administrators require detailed technical and governance training.

Topics include:

* users and roles
* support groups
* workflow configuration
* reference data
* SLA logic
* approval rules
* automation
* integrations
* audit history
* reporting configuration
* production change control
* rollback

The key distinction is:

> **Platform administration implements approved process decisions. It does not replace process ownership.**

---

# 14. Auditor / Reviewer Training

Reviewers should understand how to retrieve and interpret:

* approval history
* access records
* change history
* audit logs
* SLA exceptions
* priority overrides
* vendor access
* control exceptions

They should know where evidence exists without receiving unnecessary modification access.

---

# 15. Champion Training

Champions should receive enough depth to help peers with:

* common workflow questions
* service catalog use
* basic troubleshooting
* process clarification
* escalation of recurring issues

Champions should also understand when to stop troubleshooting and escalate a genuine platform or process problem.

---

# 16. Training Environment

Hands-on training should use a safe environment where participants can:

* create records
* approve
* reject
* reassign
* close
* trigger test scenarios

without affecting production.

The training environment should resemble production closely enough that the experience transfers.

---

# 17. Training Data

Training scenarios should use representative but non-sensitive data.

Examples include:

* fictional users
* sample services
* sample assets
* sample vendors
* test approvers
* test incidents
* test change records

The objective is realistic workflow without unnecessary production exposure.

---

# 18. Training Schedule

Recommended timing:

| Audience         | Timing                    |
| ---------------- | ------------------------- |
| Champions        | 2–3 weeks before go-live  |
| Service Desk     | 1–2 weeks before go-live  |
| Specialist Teams | 1–2 weeks before go-live  |
| Approvers        | Within 1 week of go-live  |
| Service Owners   | 1–2 weeks before go-live  |
| End Users        | Days before go-live       |
| Platform Admins  | Throughout implementation |

Refresher support should follow go-live.

---

# 19. Training Sequence

```text id="h0cxnm"
Overview
   ↓
Role Responsibility
   ↓
Demonstration
   ↓
Hands-On Practice
   ↓
Exception Scenario
   ↓
Quick Reference
```

This keeps training grounded in actual work.

---

# 20. Quick-Reference Materials

Recommended job aids include:

* how to submit an incident
* how to submit a service request
* incident priority guide
* approval guide
* reassignment guide
* change-type guide
* vendor-access guide
* closure checklist
* escalation guide

Quick-reference material should answer common operational questions faster than a long manual.

---

# 21. Role-Based Job Aids

Example:

## Service Desk Quick Reference

```text id="s3b3hf"
1. Confirm Incident or Request
2. Validate Service
3. Determine Impact / Urgency
4. Confirm Ownership
5. Check SLA
6. Document Action
7. Resolve / Escalate
8. Complete Closure Data
```

A one-page reference may have more long-term value than a 40-page training guide.

---

# 22. Training and Controls

Controlled actions should receive explicit training.

Examples:

* self-approval prohibition
* privileged access
* priority override
* SLA exception
* vendor access
* high-risk change
* administrative configuration

Users should understand both:

* what the control does
* why it exists

This reduces accidental bypass.

---

# 23. Training Exceptions

If a participant cannot complete required training before go-live:

* identify operational impact
* assign manager
* provide expedited training
* restrict controlled access where necessary
* track completion

Critical roles should not receive production authority without enough training to use it safely.

---

# 24. Training Validation

Training effectiveness should be validated through behavior.

Possible methods include:

* practice scenarios
* short knowledge checks
* UAT participation
* observed workflow use
* early production metrics

The objective is not to make every user pass a formal exam.

It is to confirm that critical roles understand the process.

---

# 25. Training Completion

Training completion should be tracked for roles where readiness matters.

Priority audiences include:

* Service Desk
* platform administrators
* approvers
* change authorities
* support leads
* service owners

End-user completion may be measured more broadly through communications and available self-service materials.

---

# 26. Training Metrics

| Metric                            | Purpose                        |
| --------------------------------- | ------------------------------ |
| Critical Role Training Completion | Measure readiness              |
| Practice Scenario Completion      | Measure understanding          |
| Post-Training Support Questions   | Identify unclear content       |
| Training-Related UAT Issues       | Identify gaps                  |
| Post-Go-Live Training Issues      | Identify reinforcement needs   |
| Repeat Process Errors             | Measure retained understanding |
| Quick-Reference Usage             | Measure support value          |

Training success should ultimately show up in operational behavior.

---

# 27. Post-Go-Live Reinforcement

After launch, training should shift toward:

* targeted refreshers
* short issue-based guidance
* updated quick references
* champion support
* new-hire onboarding
* recurring-role training

Broad retraining should only be used when the issue is actually widespread.

---

# 28. Training Feedback

Participants should be able to identify:

* unclear instruction
* confusing workflow
* missing scenario
* poor quick reference
* process contradiction

Feedback should be separated into:

```text id="5yafh5"
Training Issue
Process Issue
Platform Issue
```

This helps make sure training is not used to cover up a design problem.

---

# 29. Training Maintenance

Training content should be reviewed when:

* workflow changes
* service catalog changes materially
* approval logic changes
* RBAC changes
* major automation is introduced
* AI capabilities change
* recurring user errors appear

Training should follow the operating model.

It should not describe a version of the process that no longer exists.

---

# 30. New-Hire Training

After stabilization, role-based ESM training should become part of normal onboarding.

Examples:

* Service Desk onboarding
* support-team onboarding
* approver onboarding
* platform admin onboarding

This prevents knowledge from remaining tied to the original implementation team.

---

# 31. Training Ownership

| Area                     | Owner                        |
| ------------------------ | ---------------------------- |
| Training Strategy        | Adoption / Training Lead     |
| Process Content          | Process Owners               |
| Platform Demonstration   | Platform Team                |
| Service-Specific Content | Service Owners               |
| Security-Control Content | Security / Risk              |
| Delivery                 | Training / Operational Leads |
| Training Maintenance     | Process + Platform Owners    |

Training ownership should transfer into operations after implementation.

---

# 32. Training Guardrails

## Do Not Train Everyone on Everything

Role relevance improves retention.

## Do Not Use Training to Fix Bad Workflow

If the process is confusing for everyone, fix the process.

## Do Not Deliver Training Too Early

People forget what they cannot use.

## Do Not Rely Only on Slide Decks

Practice matters for operational roles.

## Do Not Give Controlled Roles Access Before They Understand the Control

Privilege requires readiness.

## Do Not Let Training Material Become Stale

Operational guidance should track the current production model.

---

# 33. Training Success Criteria

The training plan is ready when:

* audiences are defined
* learning objectives are role-based
* critical roles receive hands-on practice
* control responsibilities are included
* training timing aligns with go-live
* quick-reference materials exist
* completion tracking is defined
* reinforcement is planned
* ownership transfers to operations

---

# 34. Training Plan Conclusion

The training plan is intentionally role-based because the organization does not need every employee to understand the entire service-management architecture.

Users need to know how to ask for help.

Technicians need to know how to own and document work.

Approvers need to know what they are authorizing.

Service owners need to know what they are accountable for.

Administrators need to know where configuration authority ends.

If each role understands those boundaries, the platform becomes much easier to operate.

**Next:** [Communications and Feedback](./communications%20and%20feedback.md)
