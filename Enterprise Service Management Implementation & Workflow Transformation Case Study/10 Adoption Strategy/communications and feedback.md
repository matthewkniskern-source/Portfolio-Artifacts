# Communications and Feedback

## Purpose

This artifact defines how the implementation communicates change, gathers user and operational feedback, and turns that feedback into controlled improvement.

Communication should help people understand:

* what is changing
* why it is changing
* when it affects them
* what they need to do differently
* where to get help

Feedback should help the implementation team understand:

* what is unclear
* what is difficult
* what is broken
* what is being bypassed
* what should improve next

The operating principle is:

> **Communication should reduce uncertainty. Feedback should improve the operating model, not become another unmanaged intake channel.**

This artifact builds on:

* [Adoption Strategy](./adoption%20strategy.md)
* [Training Plan](./training%20plan.md)
* [Implementation Plan](../08%20Implementation%20Plan/implementation%20plan.md)
* [UAT Plan](../09%20Testing%20and%20UAT/uat%20plan.md)

---

# 1. Communication Objectives

Communication should:

* explain the business reason for the change
* set expectations before go-live
* prepare each audience for its role
* clarify legacy-channel changes
* reinforce approved intake
* support hypercare
* reduce rumor and confusion
* provide clear escalation and support paths

The objective is not more messaging.

It is better timing and relevance.

---

# 2. Communication Audiences

| Audience                | Primary Need                                     |
| ----------------------- | ------------------------------------------------ |
| End Users               | What changes for me?                             |
| Service Desk            | What changes in daily operations?                |
| Specialist Teams        | How does ownership and escalation change?        |
| Approvers               | What am I expected to approve and when?          |
| Service Owners          | What am I accountable for?                       |
| Platform Administrators | What changes are moving into production?         |
| Managers                | What behavior should I reinforce?                |
| Executives              | Is the implementation ready and producing value? |

---

# 3. Communication Phases

Communication should follow the implementation lifecycle.

```text id="m5ef3n"
Awareness
   ↓
Preparation
   ↓
Training
   ↓
Go-Live
   ↓
Hypercare
   ↓
Reinforcement
```

Each phase answers a different set of questions.

---

# 4. Awareness Communication

Initial awareness should explain:

* the current service-management problems
* the purpose of the new operating model
* the expected implementation timeline
* the broad impact to users

The message should stay simple.

Example themes:

* one managed service record
* clearer ownership
* more consistent status
* easier request tracking
* better visibility into service performance

Early communication should not overwhelm users with workflow detail.

---

# 5. Preparation Communication

As go-live approaches, communication should become more specific.

Users should learn:

* when the new system becomes active
* which intake channels are changing
* where the service catalog will be available
* what happens to existing requests
* where training and quick-reference material can be found

Support teams should receive more detailed operational preparation.

---

# 6. Role-Specific Communication

## End Users

Need:

* new intake location
* go-live date
* basic service-request guidance
* legacy-channel changes
* support contact

## Support Teams

Need:

* workflow changes
* ownership expectations
* escalation
* support schedule
* hypercare process

## Approvers

Need:

* approval responsibility
* expected response time
* delegation
* go-live timing

## Management

Need:

* implementation readiness
* adoption expectations
* known risks
* initial performance indicators

---

# 7. Go-Live Communication

Go-live communication should answer five basic questions:

1. What changed?
2. When is it active?
3. Where do I go for support?
4. What happens to my existing request?
5. What do I do if something does not work?

A user should not need to understand the project architecture to use the new service process.

---

# 8. Legacy Channel Communication

Where legacy channels are changing, the message should be explicit.

Example:

```text id="03s9mc"
Old Support Method
      ↓
Retired / Redirected
      ↓
New Managed Intake
```

Communication should identify whether:

* email remains supported
* phone remains supported
* direct technician requests are discouraged
* old portal is retired
* spreadsheet intake ends

Ambiguity here will preserve the current-state fragmentation.

---

# 9. Hypercare Communication

During early production, communication should focus on:

* known issues
* available support
* workaround guidance
* corrected defects
* high-impact process clarification

Hypercare updates should be frequent enough to be useful but not so frequent that users stop reading them.

---

# 10. Reinforcement Communication

After stabilization, communication should shift from launch messaging to targeted reinforcement.

Examples:

* reminder to use service catalog
* new catalog item announcement
* approval expectation reminder
* updated quick-reference guide
* recurring issue clarification

Reinforcement should be driven by observed adoption behavior.

---

# 11. Communication Channels

Potential channels include:

* email
* intranet
* service portal
* team meetings
* manager communication
* training sessions
* quick-reference documents
* collaboration platform announcements

Channel selection should match audience and urgency.

Critical operational changes should not rely on a single communication method.

---

# 12. Message Ownership

| Message Type                | Owner                          |
| --------------------------- | ------------------------------ |
| Executive / Business Change | Project Sponsor                |
| Implementation Update       | Project Lead                   |
| Operational Change          | Process Owner                  |
| User Communication          | Adoption / Communications Lead |
| Technical Outage / Issue    | Platform / Service Owner       |
| Training                    | Training Lead                  |
| Governance Change           | Process / Security Owner       |

Someone should own both message content and timing.

---

# 13. Communication Approval

Higher-impact communication should be reviewed before release.

Examples include:

* go-live announcement
* major legacy-channel retirement
* significant outage
* security or access-related change
* broad process-policy change

Routine training reminders should remain lightweight.

---

# 14. Communication Calendar

A representative sequence may look like:

| Timing                   | Communication                      |
| ------------------------ | ---------------------------------- |
| 4–6 weeks before go-live | Awareness                          |
| 2–3 weeks before         | Role-specific preparation          |
| 1–2 weeks before         | Training and quick references      |
| Several days before      | Final go-live reminder             |
| Go-live day              | Launch announcement                |
| First week               | Hypercare updates                  |
| First month              | Reinforcement / adoption feedback  |
| Ongoing                  | Targeted operational communication |

Timing should be adjusted to actual implementation pace.

---

# 15. Feedback Objectives

Feedback should identify:

* defects
* usability problems
* process gaps
* unclear training
* missing catalog items
* unnecessary friction
* recurring workarounds
* improvement opportunities

Feedback should not bypass normal incident or request processes.

If something is broken operationally, it should still become a managed service record.

---

# 16. Feedback Channels

Potential feedback sources include:

* UAT
* training sessions
* hypercare
* user surveys
* Service Desk observations
* support group meetings
* champion input
* service-owner reviews
* operational metrics

The goal is to collect enough signal without creating several parallel feedback systems.

---

# 17. Feedback Classification

| Type        | Meaning                                      | Owner                     |
| ----------- | -------------------------------------------- | ------------------------- |
| Defect      | Configured behavior is wrong                 | Platform Team             |
| Process Gap | Business rule is incomplete                  | Process Owner             |
| Usability   | Process works but is unnecessarily difficult | Process / Platform Owner  |
| Training    | User does not understand correct behavior    | Training Lead             |
| Data        | Incorrect or missing information             | Data Owner                |
| Enhancement | New improvement opportunity                  | Product / Process Backlog |
| Adoption    | Users are bypassing or resisting the model   | Adoption Lead             |

Classification determines response.

---

# 18. Feedback Workflow

```text id="rybq5b"
Feedback Received
      ↓
Classify
      ↓
Assign Owner
      ↓
Evaluate
      ↓
Correct / Explain / Defer
      ↓
Close Loop
```

The person providing meaningful feedback should receive an outcome where practical.

Otherwise users learn that feedback disappears.

---

# 19. Feedback Prioritization

Feedback should be prioritized based on:

* business impact
* user population affected
* control impact
* frequency
* operational workaround
* implementation effort

A frequently repeated small friction point may deserve higher priority than a rare cosmetic issue.

---

# 20. Feedback vs Defect

Not every negative reaction indicates a defect.

Example:

> "I do not like needing approval."

If approval is an intentional control, this may be:

* communication
* training
* process resistance

rather than a platform defect.

By contrast:

> "The request bypassed required approval."

is a control defect.

The distinction matters.

---

# 21. Feedback vs Enhancement

An enhancement is a valid improvement outside the approved implementation baseline.

Examples:

* additional dashboard
* new catalog item
* optional notification
* convenience automation

Enhancements should enter the optimization backlog rather than expanding immediate go-live scope automatically.

---

# 22. Feedback During Hypercare

Hypercare feedback should be reviewed frequently.

Recommended categories:

```text id="yfz4i8"
Critical Defect
High Defect
Process Issue
Training Issue
Data Issue
Enhancement
```

Critical and high issues should receive rapid ownership.

Lower-priority feedback should be consolidated rather than interrupting stabilization work.

---

# 23. User Satisfaction

A lightweight satisfaction model may ask:

* Was the process easy to use?
* Did you understand the status?
* Was the outcome satisfactory?

Detailed surveys should be used selectively.

Long surveys usually reduce participation without producing better operational insight.

---

# 24. Technician Feedback

Support teams should be asked:

* Is routing accurate?
* Is ownership clear?
* Are required fields useful?
* Are approvals working?
* Are workflows creating unnecessary steps?
* Are users bypassing the process?
* Is knowledge helping?

Technician feedback is especially valuable during early stabilization.

---

# 25. Approver Feedback

Approvers should be asked:

* Are requests understandable?
* Is required context available?
* Is approval volume reasonable?
* Are reminders useful?
* Is delegation working?
* Are requests reaching the correct authority?

Approval delay may be a process-design issue rather than an approver-performance issue.

---

# 26. Service Owner Feedback

Service Owners should review:

* SLA performance
* backlog
* escalation
* exceptions
* recurring incident patterns
* catalog demand
* vendor dependency

This moves feedback from individual preference toward operational improvement.

---

# 27. Feedback Metrics

Useful measures include:

| Metric                 | Purpose                         |
| ---------------------- | ------------------------------- |
| Feedback Volume        | Measure engagement              |
| Defect Rate            | Identify implementation quality |
| Usability Issue Rate   | Identify process friction       |
| Training Issue Rate    | Identify readiness gaps         |
| Enhancement Backlog    | Track improvement demand        |
| Feedback Closure Time  | Measure responsiveness          |
| Repeat Feedback Themes | Identify systemic issues        |
| CSAT                   | Measure user experience         |

Raw feedback volume is not itself a success or failure measure.

---

# 28. Feedback Trend Analysis

Repeated feedback should be grouped by theme.

Example:

```text id="zgr56h"
Repeated Complaint
      ↓
Theme Identified
      ↓
Root Cause
      ↓
Process / Platform / Training / Data
      ↓
Improvement
```

This prevents the team from solving the same issue repeatedly one ticket at a time.

---

# 29. Closing the Feedback Loop

Where feedback results in change, the organization should communicate:

* what changed
* why
* when it becomes effective

This is especially useful for highly visible recurring issues.

Users are more likely to continue providing useful feedback when they can see that it produces outcomes.

---

# 30. Communication and Feedback Governance

Material changes resulting from feedback should still follow:

* requirement review
* configuration control
* testing
* approval where required

Feedback is an input.

It does not automatically authorize production change.

---

# 31. Communication and Feedback Metrics Dashboard

A lightweight view might include:

```text id="a4msdv"
Legacy Channel Usage
Training Issues
User Satisfaction
Approval Aging
Usability Feedback
Open High-Impact Feedback
Enhancement Backlog
```

The dashboard should help identify where the operating model still needs reinforcement or adjustment.

---

# 32. Communication Guardrails

## Do Not Send Every Message to Everyone

Audience relevance matters.

## Do Not Hide Problems During Go-Live

Clear known-issue communication builds more trust than pretending everything is perfect.

## Do Not Overload Users With Technical Detail

Most users need operating guidance, not implementation architecture.

## Do Not Leave Legacy-Channel Changes Ambiguous

Users will default to familiar behavior.

---

# 33. Feedback Guardrails

## Do Not Create Another Unmanaged Intake Channel

Operational problems still belong in the service process.

## Do Not Turn Every Complaint Into Configuration

Identify the root cause first.

## Do Not Ignore Repeated Friction

Repeated workaround behavior usually indicates a real problem somewhere in the design.

## Do Not Let Feedback Become a Dead End

Provide disposition where practical.

## Do Not Let Enhancements Expand Go-Live Scope Automatically

Prioritize them through the normal improvement process.

---

# 34. Success Criteria

The communications and feedback model is ready when:

* audiences are defined
* message ownership is defined
* communication timing is planned
* legacy-channel changes are clear
* go-live communication is prepared
* feedback channels are identified
* feedback classification exists
* response ownership is defined
* high-impact feedback can be escalated
* enhancement feedback feeds future optimization
* the feedback loop can be closed

---

# 35. Communications and Feedback Conclusion

Good communication should make the target operating model easier to understand.

Good feedback should make it better over time.

Neither should become a parallel service-management process.

Users should know where work belongs.

Support teams should know where feedback belongs.

Process owners should know what needs to change.

And when the organization makes an improvement, people should be able to see that their experience helped shape it.

**Next:** [Performance Framework](../11%20Metrics%20and%20Optimization/performance%20framework.md)
