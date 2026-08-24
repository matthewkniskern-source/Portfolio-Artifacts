# Priority and SLA Model

## Purpose

The priority and SLA model defines how service work is ranked, timed, monitored, escalated, and measured.

The current-state environment allows urgency to be influenced too heavily by who is asking, how often they follow up, or which technician receives the request.

The target model replaces that with a consistent decision structure based on:

* business impact
* urgency
* service criticality
* defined service expectations
* documented exceptions

The objective is not to create the most complicated priority matrix possible.

It is to create one that support teams can apply consistently and that management can actually trust.

The operating principle is:

> **Priority should reflect business effect, not requester volume.**

---

# 1. Scope

This model applies primarily to:

* Incident Management
* selected Service Requests
* escalation logic
* SLA reporting
* management dashboards

Not every record type uses the same priority or SLA structure.

For example:

* incidents are generally driven by impact and urgency
* service requests are generally driven by catalog commitment
* changes are generally driven by risk, schedule, and authorization rather than incident priority
* knowledge records do not require operational SLA treatment

Detailed workflow behavior is defined in:

* [Incident Management](../04%20Workflow%20Design/incident%20management.md)
* [Service Request Management](../04%20Workflow%20Design/service%20request%20management.md)

---

# 2. Priority Model

Incident priority is derived from two primary inputs:

**Impact + Urgency → Priority**

The model uses three levels for each input and four resulting priority levels.

```text id="k8k4e9"
Impact
  +
Urgency
  ↓
Priority
  ↓
Response Target
  ↓
Resolution Target
  ↓
Escalation
```

This keeps the decision simple enough for frontline use while still producing meaningful differentiation.

---

# 3. Impact Definition

Impact measures the extent of business disruption.

| Impact | Definition                                                                | Typical Example                    |
| ------ | ------------------------------------------------------------------------- | ---------------------------------- |
| High   | Critical service, multiple departments, or large user population affected | Enterprise application outage      |
| Medium | Multiple users, one department, or important localized service affected   | Department application unavailable |
| Low    | Single user or limited business effect                                    | Individual workstation issue       |

Impact should consider:

* number of users affected
* service criticality
* operational consequence
* geographic scope
* availability of workaround
* safety or security consequence where applicable

Impact is not determined by job title alone.

A senior executive with a single-user issue may still represent Low impact if the broader business remains unaffected.

Where executive or operational dependency materially changes business effect, that condition should be captured as impact rather than treated as an undocumented exception.

---

# 4. Urgency Definition

Urgency measures how quickly action is required before business consequence increases.

| Urgency | Definition                                                            | Typical Example                                       |
| ------- | --------------------------------------------------------------------- | ----------------------------------------------------- |
| High    | Immediate action required; delay materially increases business impact | Critical service unavailable during active operations |
| Medium  | Timely action required but short delay is tolerable                   | Important function impaired with workaround           |
| Low     | Work can reasonably wait without material business consequence        | Minor issue or scheduled corrective action            |

Urgency may consider:

* availability of workaround
* business deadline
* operational timing
* duration sensitivity
* security exposure
* approaching service event

Urgency should not be used as another word for "the user wants this quickly."

---

# 5. Priority Matrix

The initial target model uses the following matrix:

| Impact | Urgency | Priority |
| ------ | ------- | -------- |
| High   | High    | P1       |
| High   | Medium  | P2       |
| High   | Low     | P3       |
| Medium | High    | P2       |
| Medium | Medium  | P3       |
| Medium | Low     | P4       |
| Low    | High    | P3       |
| Low    | Medium  | P4       |
| Low    | Low     | P4       |

This model deliberately reserves P1 for conditions where both business impact and urgency are high.

That keeps the highest priority meaningful.

If everything important becomes P1, P1 stops functioning as a priority.

---

# 6. Priority Definitions

## P1 — Critical

A P1 incident represents significant business disruption requiring immediate coordinated response.

Typical characteristics:

* critical service unavailable
* broad user impact
* severe operational disruption
* no reasonable workaround
* immediate security or safety consequence where included in service scope

Expected behavior:

* immediate assignment
* rapid acknowledgement
* active escalation
* coordinated technical response
* frequent stakeholder communication
* service owner or management visibility

P1 should be uncommon.

Its value depends on the organization being willing to reserve it for genuinely critical conditions.

---

## P2 — High

A P2 incident represents substantial service degradation or meaningful business impact requiring accelerated response.

Typical characteristics:

* important service unavailable to a department or group
* major function degraded
* workaround limited
* business impact likely to increase if unresolved

Expected behavior:

* priority assignment
* accelerated response
* proactive monitoring
* defined escalation
* stakeholder updates where appropriate

---

## P3 — Normal

A P3 incident represents standard operational disruption with limited broader impact.

Typical characteristics:

* single-user or small-group issue
* workaround available
* business process remains functional
* no immediate escalation need

This should represent a large portion of normal incident activity.

---

## P4 — Low

A P4 incident represents low-impact work that can be scheduled within normal service operations.

Typical characteristics:

* cosmetic or minor defect
* low operational consequence
* nonurgent corrective action
* issue with acceptable workaround

P4 should not mean "ignore."

It means the work can be handled behind higher-impact conditions without material business harm.

---

# 7. Priority Decision Example

Consider three simultaneous incidents:

| Incident                                      | Impact | Urgency | Result |
| --------------------------------------------- | ------ | ------- | ------ |
| Enterprise scheduling system unavailable      | High   | High    | P1     |
| Finance team cannot access reporting function | Medium | High    | P2     |
| Executive printer unavailable                 | Low    | Medium  | P4     |

The third request may come from a more senior employee.

That does not automatically make it the highest operational priority.

This is one of the practical differences between service priority and organizational hierarchy.

---

# 8. Priority Override

The calculated priority may be overridden by authorized roles when legitimate business circumstances are not adequately represented by the standard matrix.

Examples may include:

* regulatory deadline
* unusual operational dependency
* significant security condition
* executive business continuity requirement
* declared major incident

Priority override shall require:

* authorized role
* original priority
* revised priority
* reason
* timestamp
* actor

Related requirement:

**FR-07 — Controlled Priority Override**

Priority override should be available.

It should not become the normal way to use the priority model.

---

# 9. Service-Level Model

Service-level targets define expected response and completion behavior.

The model separates:

## First Response

How quickly the support organization acknowledges and begins engagement.

## Resolution

How quickly an incident is restored or resolved.

## Fulfillment

How quickly a defined service request is completed.

These are different measurements and should not be treated interchangeably.

---

# 10. Initial Incident SLA Targets

The following targets are design assumptions for the fictional client and would require stakeholder validation before production implementation.

| Priority |   First Response | Resolution Target | Escalation Profile   |
| -------- | ---------------: | ----------------: | -------------------- |
| P1       |       15 minutes |           4 hours | Immediate / active   |
| P2       |       30 minutes |  8 business hours | Accelerated          |
| P3       | 4 business hours |   2 business days | Standard             |
| P4       |   1 business day |   5 business days | Standard / scheduled |

These targets are intentionally reasonable for a midsize regional organization rather than modeled after a 24x7 global enterprise.

Service-specific requirements may override the standard model where justified.

---

# 11. Business Hours

SLA design must define what counts as service time.

The initial model assumes:

* standard business services operate during defined organizational business hours
* selected critical services may require extended or 24x7 coverage
* P1 response expectations for critical supported services apply according to the service's support window

The platform should not apply a 24x7 resolution clock to a service that is contractually or operationally supported only during business hours unless that expectation is deliberate.

Each service should therefore define:

* support window
* SLA calendar
* holiday handling
* after-hours escalation where applicable

---

# 12. SLA Timer States

A timer should behave according to workflow state.

Example:

| Status            | SLA State          |
| ----------------- | ------------------ |
| New               | Running            |
| Assigned          | Running            |
| In Progress       | Running            |
| Waiting on User   | Paused if approved |
| Waiting on Vendor | Policy dependent   |
| Scheduled         | Policy dependent   |
| Resolved          | Stopped            |
| Closed            | Stopped            |

Detailed state behavior will be finalized in the workflow designs.

---

# 13. Waiting on User

`Waiting on User` may pause applicable resolution or fulfillment targets when:

* the support team has requested information required to continue
* the request is documented
* the user has been notified

It should not be used simply because the technician is busy or the next action is unclear.

A pause state must represent an actual external dependency.

---

# 14. Waiting on Vendor

Vendor dependency requires more care.

A ticket may legitimately be blocked by external support, but automatically excluding all vendor time creates an incentive to hide service delay outside SLA measurement.

The target model therefore separates:

* **internal service commitment**
* **vendor dependency**
* **contractual vendor performance**

Depending on the service, the internal SLA may:

* continue running
* pause under approved conditions
* transition to a separate vendor-dependent measure

The rule must be defined by service rather than improvised ticket by ticket.

Related design:

[Ownership and Escalation](./ownership%20and%20escalation.md)

---

# 15. Scheduled Work

Some work cannot or should not be completed immediately.

Examples include:

* maintenance window
* user-requested date
* scheduled equipment deployment
* approved after-hours activity

Scheduled status may pause fulfillment measurement only where the scheduled delay is legitimate and documented.

A ticket should not be moved to `Scheduled` simply to protect an SLA.

---

# 16. SLA Warning Thresholds

The workflow should identify risk before a breach occurs.

Recommended initial thresholds:

| Threshold              | Action                            |
| ---------------------- | --------------------------------- |
| 50% of target consumed | Technician visibility             |
| 75% of target consumed | Technician / group warning        |
| 90% of target consumed | Group lead escalation             |
| 100%                   | SLA breach and defined escalation |

Thresholds may differ for P1 incidents because their response cadence is substantially shorter.

---

# 17. P1 Escalation Model

P1 incidents require a distinct escalation path.

```text id="su1r7u"
P1 Created
    ↓
Immediate Assignment
    ↓
Service Desk / Resolver Acknowledgement
    ↓
Technical Lead Engaged
    ↓
Service Owner / Management Notification
    ↓
Active Resolution
    ↓
Periodic Communication
    ↓
Service Restored
    ↓
Validation / Review
```

The exact communication interval should be defined during implementation.

The important point is that communication becomes part of the P1 operating model instead of relying on someone remembering to send an update.

---

# 18. Standard Escalation Model

For P2–P4 incidents:

```text id="02xjyi"
Ticket Active
     ↓
SLA 75%
     ↓
Support Group Warning
     ↓
SLA 90%
     ↓
Group Lead
     ↓
SLA Breach
     ↓
Service Owner / Management
```

Escalation does not necessarily transfer ownership.

The current support group remains responsible unless a deliberate reassignment occurs.

---

# 19. Functional vs Hierarchical Escalation

The target model distinguishes two types of escalation.

## Functional Escalation

Moves work to a team with the required expertise.

Example:

```text id="v0iq5r"
Service Desk
     ↓
Network Support
     ↓
Infrastructure Engineering
```

## Hierarchical Escalation

Raises visibility because delay, risk, or impact has increased.

Example:

```text id="kwevfs"
Technician
    ↓
Team Lead
    ↓
Service Owner
    ↓
IT Management
```

These paths may operate at the same time.

A technical escalation does not automatically eliminate management visibility.

---

# 20. SLA Exception Model

There will be legitimate conditions where normal SLA treatment should not apply.

Examples may include:

* documented customer-requested delay
* approved maintenance dependency
* declared disaster or business-continuity condition
* confirmed external dependency under defined policy
* formally approved exception

An exception shall require:

* exception type
* reason
* approving authority where required
* effective period
* retained history

The organization should be able to report:

* SLA performance
* SLA exceptions
* exception reasons
* exception frequency

If exception use starts growing, that is an operational signal worth investigating.

---

# 21. Service Request Targets

Service requests do not necessarily use incident priorities.

Instead, fulfillment targets are normally defined by catalog item.

Examples from the [Service Catalog](./service%20catalog.md):

| Catalog Item                |          Target |
| --------------------------- | --------------: |
| Standard Application Access | 2 Business Days |
| Privileged Access           | 3 Business Days |
| Standard Software           | 2 Business Days |
| Computer Equipment          | 5 Business Days |
| Shared Mailbox              | 3 Business Days |
| VPN Access                  | 2 Business Days |

A service request may still be escalated when:

* fulfillment target is at risk
* approval is overdue
* operational impact changes
* an exception has been declared

---

# 22. Approval Time

Approval time should be visible separately from technical fulfillment time.

Example:

```text id="pi3cc1"
Request Submitted
      ↓
Approval Pending
      ↓
Approved
      ↓
Fulfillment
      ↓
Complete
```

The organization should be able to distinguish:

**Total Request Time**

from:

**Approval Time + Fulfillment Time**

Otherwise a slow approval process may appear to be a support-team performance problem.

This becomes important during optimization.

---

# 23. SLA Ownership

Different stakeholders own different parts of the SLA model.

| Responsibility            | Owner                                  |
| ------------------------- | -------------------------------------- |
| Define service commitment | Service Owner / IT Management          |
| Define priority rules     | IT Management / Process Owner          |
| Configure timers          | Platform Administrator                 |
| Monitor active SLA        | Support Group                          |
| Escalate risk             | Group Lead / Service Owner             |
| Approve exception         | Authorized Process Owner               |
| Report performance        | Service Management / IT Management     |
| Review recurring breach   | Service Owner / Continuous Improvement |

The platform administrator configures the rule.

They should not be the person deciding what the business commitment should be.

---

# 24. SLA Reporting

At minimum, reporting should include:

* first response compliance
* resolution compliance
* fulfillment compliance
* breaches by priority
* breaches by service
* breaches by support group
* SLA exceptions
* pause duration
* vendor-dependent time
* approval delay

The goal is not simply to produce an overall SLA percentage.

A single percentage can hide where the process is actually failing.

---

# 25. SLA Dashboard Model

A practical management view may include:

```text id="4pgkcd"
SERVICE HEALTH

Open P1/P2
SLA at Risk
SLA Breached
Oldest Open Ticket
Backlog Age
Approval Delays
Vendor Dependencies
Priority Overrides
```

Operational teams may require more detailed queue-level views.

Executive reporting should remain focused on service risk and trend rather than ticket-by-ticket activity.

A future visual will be maintained in:

[SLA and Escalation Dashboard Concept](../diagrams/sla%20and%20escalation%20dashboard.md)

---

# 26. Priority and SLA Controls

The model introduces several control points.

| Control                     | Purpose                                  |
| --------------------------- | ---------------------------------------- |
| Defined impact values       | Reduce subjective classification         |
| Defined urgency values      | Reduce requester-driven urgency          |
| Calculated priority         | Standardize incident treatment           |
| Restricted override         | Preserve flexibility with accountability |
| SLA state rules             | Standardize timer behavior               |
| Pause criteria              | Prevent arbitrary SLA manipulation       |
| Warning thresholds          | Enable proactive escalation              |
| Exception documentation     | Preserve reporting integrity             |
| Ownership during escalation | Prevent responsibility gaps              |
| Service-specific calendar   | Prevent invalid time measurement         |

These controls will be incorporated into:

[Governance and Controls](../06%20Governance%20and%20Controls/governance%20model.md)

---

# 27. Testing Requirements

The priority and SLA model will require explicit testing.

Representative tests include:

### TC-INC-03 — Priority Calculation

Confirm that defined impact and urgency values produce the expected priority.

### TC-INC-04 — Priority Override

Confirm unauthorized users cannot override priority and authorized overrides require reason.

### TC-SLA-01 — SLA Start

Confirm SLA begins at the correct workflow state.

### TC-SLA-02 — Pause / Resume

Confirm an approved pause condition stops and resumes timing correctly.

### TC-SLA-03 — Warning Threshold

Confirm the expected alert occurs before breach.

### TC-SLA-04 — Breach Escalation

Confirm a breached ticket generates the required escalation.

### TC-SLA-05 — Exception

Confirm an SLA exception requires the defined documentation and remains reportable.

These will later be formalized in:

[Testing and UAT](../09%20Testing%20and%20UAT/test%20cases.md)

---

# 28. Priority and SLA Metrics

The model will support several continuous-improvement measures.

| Metric                    | What It Tells Us                                     |
| ------------------------- | ---------------------------------------------------- |
| SLA Compliance            | Whether service commitments are being met            |
| First Response Compliance | Whether work is acknowledged quickly                 |
| Resolution Compliance     | Whether incidents are restored within target         |
| Priority Override Rate    | Whether standard priority logic is adequate          |
| SLA Exception Rate        | Whether the standard service model fits reality      |
| SLA Pause Time            | Where external or workflow dependencies exist        |
| Breaches by Group         | Where operational bottlenecks exist                  |
| Breaches by Service       | Which services are consistently difficult to support |
| Approval Delay            | Whether authorization is slowing fulfillment         |
| Vendor Dependency Time    | Whether external support is a recurring constraint   |

A metric should trigger questions.

It should not automatically trigger blame.

---

# 29. Design Guardrails

The priority and SLA model should avoid several common failure patterns.

## Priority Inflation

Too many P1 and P2 incidents reduce the usefulness of the model.

## SLA Gaming

Pause states, exceptions, or status changes should not be used primarily to protect performance statistics.

## False Precision

Service targets should reflect actual staffing and support capability.

An impressive-looking SLA that the organization has no reasonable ability to deliver is not a useful commitment.

## Universal SLA Design

Not every service needs the same target.

The standard model should provide consistency while allowing justified service-specific variation.

## Over-Escalation

If every aging ticket generates management escalation, escalation becomes background noise.

---

# 30. Priority and SLA Success Criteria

The model is considered design-ready when:

* impact definitions are approved
* urgency definitions are approved
* priority matrix is approved
* priority override authority is defined
* response targets are defined
* resolution / fulfillment targets are defined
* support calendars are known
* pause conditions are defined
* exception authority is defined
* warning thresholds are defined
* escalation paths are defined
* reporting definitions are documented

If those decisions are unresolved, configuring SLA timers would simply automate uncertainty.

---

# 31. Priority and SLA Conclusion

The target priority and SLA model is designed to create consistency without pretending every service condition fits perfectly into a matrix.

The matrix provides the default.

Governed exceptions provide flexibility.

Clear timers provide measurement.

Escalation provides visibility before service failure becomes a surprise.

Most importantly, the model moves priority away from:

**Who is asking?**

and toward:

**What is the actual business effect if this does not get fixed?**

That is a much stronger basis for service decisions.

**Next:** [Ownership and Escalation](./ownership%20and%20escalation.md)
