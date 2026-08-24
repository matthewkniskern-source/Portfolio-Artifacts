# Performance Framework

## Purpose

This artifact defines how the target Enterprise Service Management environment will be measured after implementation.

The objective is not to build a dashboard full of activity counts.

It is to determine whether the new operating model is actually improving:

* service responsiveness
* ownership
* workflow efficiency
* control performance
* user experience
* change quality
* knowledge reuse
* adoption

The operating principle is:

> **Measure whether the process is getting better, not just whether the platform is getting busier.**

This artifact builds on:

* [Baseline Metrics](../01%20Current%20State/baseline%20metrics.md)
* [Target Operating Model](../03%20Target%20Service%20Model/target%20operating%20model.md)
* [Control Matrix](../06%20Governance%20and%20Controls/control%20matrix.md)
* [Adoption Strategy](../10%20Adoption%20and%20Training/adoption%20strategy.md)

---

# 1. Performance Objectives

The performance model should answer five questions:

| Question                               | Performance Area       |
| -------------------------------------- | ---------------------- |
| Are users getting help faster?         | Service Performance    |
| Is work reaching the right owner?      | Workflow Quality       |
| Are controls operating correctly?      | Governance             |
| Are users adopting the target process? | Adoption               |
| Are changes improving the environment? | Continuous Improvement |

The framework should connect operational activity to measurable outcomes.

---

# 2. Measurement Layers

The target model uses four measurement layers.

```text id="xqfq72"
Operational Activity
        ↓
Process Performance
        ↓
Control / Quality Performance
        ↓
Business Outcome
```

Example:

```text id="b5f3vx"
Tickets Created
      ↓
Reassignment Rate
      ↓
Routing Accuracy
      ↓
Faster Resolution
```

Counting tickets alone does not tell the full story.

---

# 3. Measurement Categories

| Category         | Examples                                             |
| ---------------- | ---------------------------------------------------- |
| Responsiveness   | First response, resolution time                      |
| Reliability      | SLA, backlog, reopen                                 |
| Workflow Quality | Reassignment, ownership, closure quality             |
| Change Quality   | Success, failure, emergency change                   |
| Knowledge        | Reuse, helpfulness, deflection                       |
| Governance       | Access review, exceptions, control failures          |
| Vendor           | Dependency, access expiration                        |
| Adoption         | Managed intake, catalog use                          |
| User Experience  | Satisfaction, feedback                               |
| Improvement      | Repeat incident reduction, remediation effectiveness |

---

# 4. Baseline Before Target

Performance should be compared against the baseline established during current-state analysis.

The baseline may contain:

* reliable data
* partial data
* estimates
* unavailable metrics

The implementation should not invent a precise historical benchmark where none exists.

Instead:

```text id="ffgg8i"
Current State
     ↓
Best Available Baseline
     ↓
Production Stabilization
     ↓
Reliable New Baseline
     ↓
Trend
```

The stabilized production environment becomes the more reliable comparison point.

---

# 5. Core Service Metrics

The initial performance framework should prioritize a small group of operational measures.

| Metric                   | Purpose                            |
| ------------------------ | ---------------------------------- |
| First Response Time      | Measure initial responsiveness     |
| Mean Time to Resolution  | Measure resolution efficiency      |
| SLA Compliance           | Measure service commitment         |
| Reassignment Rate        | Measure routing quality            |
| Reopen Rate              | Measure resolution quality         |
| Backlog Age              | Measure unresolved work            |
| First Contact Resolution | Measure Service Desk effectiveness |
| User Satisfaction        | Measure experience                 |

These should form the core service-performance view.

---

# 6. First Response Time

First Response Time measures elapsed time from valid ticket creation until meaningful support engagement.

The metric should distinguish:

* automated acknowledgement
* actual operational response

An automatic email saying:

> "Your ticket was received"

should not automatically count as meaningful first response.

---

# 7. Mean Time to Resolution

MTTR should measure how long it takes to move from valid intake to resolution.

Analysis should segment by:

* priority
* service
* support group
* incident type

A single enterprise-wide MTTR can hide poor performance in important services.

---

# 8. SLA Compliance

SLA compliance should be measured using the approved timing model.

Reporting should distinguish:

* met
* breached
* approved exception
* paused time
* vendor dependency where applicable

The target model should avoid improving SLA performance simply by excluding inconvenient time.

---

# 9. Reassignment Rate

Reassignment Rate measures how often work changes ownership.

High reassignment may indicate:

* poor intake
* bad routing
* unclear service ownership
* weak support-group boundaries

The metric should not automatically penalize legitimate escalation.

Context matters.

---

# 10. Reopen Rate

Reopen Rate helps identify:

* weak resolution
* premature closure
* incomplete validation
* recurring symptoms

A rising reopen rate may indicate that improved closure speed is creating lower resolution quality.

Metrics should be interpreted together.

---

# 11. Backlog Age

Backlog should be analyzed by age rather than only total volume.

Example:

| Age       | Interpretation                 |
| --------- | ------------------------------ |
| 0–2 days  | Normal working inventory       |
| 3–7 days  | Review                         |
| 8–14 days | Aging                          |
| 15+ days  | Escalation / root-cause review |

Actual thresholds should depend on service and request type.

---

# 12. First Contact Resolution

First Contact Resolution measures work resolved during the initial support interaction without unnecessary transfer.

This may indicate:

* Service Desk capability
* useful knowledge
* good intake
* proper scope

It should not create pressure to keep work at the Service Desk when specialist support is actually required.

---

# 13. Change Performance

Change metrics should include:

| Metric                     | Purpose                        |
| -------------------------- | ------------------------------ |
| Change Success Rate        | Measure implementation quality |
| Failed Change Rate         | Identify instability           |
| Backout Rate               | Measure recovery frequency     |
| Emergency Change Rate      | Identify planning pressure     |
| Incidents Caused by Change | Measure service impact         |
| Rescheduled Change Rate    | Identify readiness problems    |

The most useful question is not:

> How many changes did we make?

It is:

> How reliably are we changing production without creating avoidable impact?

---

# 14. Knowledge Performance

Useful knowledge metrics include:

* knowledge reuse
* article helpfulness
* articles linked to resolution
* stale article count
* self-service deflection
* knowledge-gap candidates

Raw article count should remain secondary.

A large knowledge base that no one uses is not a strong outcome.

---

# 15. Governance Performance

Governance metrics may include:

| Metric                       | Purpose                                 |
| ---------------------------- | --------------------------------------- |
| Self-Approval Blocks         | Validate separation control             |
| Vendor Expiration Compliance | Validate temporary access               |
| Access Review Completion     | Validate RBAC governance                |
| SLA Exception Rate           | Identify policy pressure                |
| Priority Override Rate       | Validate prioritization                 |
| Control Failure Count        | Identify control weakness               |
| Exception Age                | Identify permanent temporary exceptions |

Governance metrics should lead to review and action.

---

# 16. Vendor Performance

Vendor-related measures may include:

* vendor-dependent ticket volume
* average vendor wait
* unresolved vendor dependency
* repeated vendor escalation
* vendor access expiration compliance
* service impact by vendor

Vendor performance should remain connected to the internal service owner.

---

# 17. Adoption Performance

Adoption should be measured through behavior.

Useful measures include:

| Metric                      | Purpose                         |
| --------------------------- | ------------------------------- |
| Managed Intake Rate         | Measure use of approved process |
| Legacy Channel Usage        | Measure bypass                  |
| Service Catalog Utilization | Measure self-service            |
| Approval Aging              | Measure approver participation  |
| Knowledge Usage             | Measure support-team adoption   |
| Training-Related Error Rate | Identify readiness gaps         |

A login count is not an adoption metric.

---

# 18. User Experience

User experience should include both:

* quantitative measures
* qualitative feedback

Potential indicators include:

* satisfaction
* ease of submission
* clarity of status
* repeat contacts
* complaint themes

User satisfaction should be interpreted alongside service performance.

A fast process that users cannot understand is still weak.

---

# 19. Metric Definition Standard

Every formal metric should define:

| Field            | Requirement                                 |
| ---------------- | ------------------------------------------- |
| Metric Name      | Clear name                                  |
| Business Purpose | Why it matters                              |
| Formula          | How it is calculated                        |
| Data Source      | Where data comes from                       |
| Owner            | Who owns interpretation                     |
| Frequency        | How often reviewed                          |
| Segmentation     | Priority / service / group where applicable |
| Threshold        | Trigger for review where useful             |

This prevents teams from using the same metric name with different definitions.

---

# 20. Metric Ownership

| Metric Area          | Primary Owner                       |
| -------------------- | ----------------------------------- |
| Incident Performance | Incident Process Owner              |
| Request Performance  | Request Process Owner               |
| SLA                  | Service Owners                      |
| Change               | Change Process Owner                |
| Knowledge            | Knowledge Owner                     |
| Governance           | Control Owners                      |
| Adoption             | Adoption / Process Owner            |
| User Satisfaction    | Service Management / Business Owner |
| Vendor               | Service / Vendor Owner              |

Reporting teams may produce the metric.

They should not automatically own what it means.

---

# 21. Metric Frequency

Representative cadence:

| Frequency           | Example                                |
| ------------------- | -------------------------------------- |
| Real-Time / Daily   | P1, SLA risk, backlog                  |
| Weekly              | Routing, aging, unresolved exceptions  |
| Monthly             | SLA, MTTR, change, adoption            |
| Quarterly           | Control trends, vendor, service review |
| Semiannual / Annual | Strategic operating-model review       |

The cadence should match how quickly action can realistically occur.

---

# 22. Segmentation

Metrics should be segmented when aggregate values hide meaningful differences.

Useful segmentation includes:

* service
* priority
* support group
* request type
* location
* vendor
* change type

Example:

```text id="5vemx9"
Enterprise MTTR = Stable

But

Critical Application MTTR = Increasing
```

The aggregate number should not hide a service-specific problem.

---

# 23. Thresholds and Triggers

Not every metric needs a hard target.

Some are better used for trend detection.

Example:

| Metric             | Trigger                    |
| ------------------ | -------------------------- |
| Reassignment Rate  | Sustained increase         |
| Priority Overrides | Unexpected spike           |
| Reopen Rate        | Above normal trend         |
| Vendor Wait        | Persistent aging           |
| Emergency Changes  | Increasing percentage      |
| Legacy Intake      | Fails to decline           |
| Automation Failure | Repeated exception pattern |

Thresholds should be refined after stable production data exists.

---

# 24. Performance Review Model

```text id="qkyhla"
Metric
  ↓
Trend
  ↓
Threshold / Concern?
      ↓
Investigate
      ↓
Root Cause
      ↓
Action
      ↓
Measure Again
```

Measurement without this loop produces reporting, not management.

---

# 25. Metric Relationships

Metrics should be interpreted together.

Example:

```text id="qepctn"
MTTR ↓
but
Reopen Rate ↑
```

This may indicate faster but weaker resolution.

Another example:

```text id="yk9oip"
SLA Compliance ↑
but
SLA Exception Rate ↑
```

This may indicate reporting improvement without actual service improvement.

The framework should discourage isolated metric optimization.

---

# 26. Balanced Performance View

The target dashboard should balance:

| Dimension   | Example                   |
| ----------- | ------------------------- |
| Speed       | MTTR                      |
| Quality     | Reopen Rate               |
| Commitment  | SLA                       |
| Ownership   | Reassignment              |
| Control     | Exception Rate            |
| Experience  | CSAT                      |
| Adoption    | Managed Intake            |
| Improvement | Repeat Incident Reduction |

This reduces the risk of optimizing one measure at the expense of the operating model.

---

# 27. Service Performance Review

A service-owner review should consider:

* demand
* SLA
* backlog
* recurring incidents
* change impact
* vendor dependency
* user satisfaction
* improvement backlog

The purpose is to identify where service behavior requires intervention.

---

# 28. Operational Review

Support management should focus more frequently on:

* P1/P2 activity
* aging backlog
* SLA risk
* reassignment
* stuck approvals
* vendor waits
* unresolved automation failures

This is the day-to-day operational view.

---

# 29. Governance Review

Governance review should focus on:

* access exceptions
* self-approval attempts
* vendor expiration
* emergency changes
* priority overrides
* SLA exceptions
* control failures
* aging exceptions

It should remain separate enough from operational metrics that control issues do not disappear inside general service reporting.

---

# 30. Improvement Candidate Identification

Metrics should feed an improvement backlog.

Example:

```text id="hz0kkr"
Reassignment Rate High
      ↓
Analyze Service / Category
      ↓
Routing Problem Identified
      ↓
Improve Routing Rule
      ↓
Test
      ↓
Measure Again
```

The metric creates the question.

Root-cause analysis determines the action.

---

# 31. Performance and Automation

Automation should be evaluated through operational outcomes.

Examples:

* routing accuracy
* manual touches reduced
* automation exception rate
* approval-cycle reduction
* fulfillment time reduction

The number of automations deployed is not itself a meaningful success metric.

---

# 32. Performance and AI

AI-assisted features should be evaluated by:

* acceptance
* correction
* rejection
* accuracy
* time saved where measurable
* error impact

High usage does not automatically prove value.

AI should remain in the performance framework like any other capability: measured against the work it is supposed to improve.

---

# 33. Performance Data Quality

A metric should not be relied on when the underlying data is materially incomplete.

Example:

```text id="qq2pby"
CI Failure Rate
   ↓
Only 30% of Incidents Have CI
   ↓
Metric Reliability = Low
```

Data-quality context should be visible where it materially affects interpretation.

---

# 34. Performance Maturity

The performance model can mature in phases.

## Stage 1 — Visibility

* volume
* backlog
* SLA
* response
* resolution

## Stage 2 — Quality

* reassignment
* reopen
* knowledge
* change success
* data quality

## Stage 3 — Optimization

* repeat-incident reduction
* automation value
* service trend analysis
* predictive / AI-assisted analysis where justified

Measurement maturity should follow process maturity.

---

# 35. Executive View

Executive reporting should remain small.

A useful view may include:

* service performance
* critical backlog
* SLA trend
* change quality
* user experience
* adoption
* major governance exceptions

Executives generally need trend, risk, and decision context.

They do not need every queue-level metric.

---

# 36. Process Owner View

Process Owners should receive deeper measures relevant to their process.

Example:

## Incident

* priority
* response
* resolution
* reassignment
* reopen
* repeat incidents

## Change

* success
* failure
* emergency
* backout
* incident caused by change

This supports direct process improvement.

---

# 37. Metric Actionability

Before adding a metric, ask:

> **What would we do differently if this number changed?**

If there is no credible answer, the metric may not belong on the primary dashboard.

This keeps reporting focused.

---

# 38. Performance Guardrails

## Do Not Measure Everything Because the Platform Can

More metrics can create less clarity.

## Do Not Compare Bad Historical Data to Precise New Data Without Context

Baseline quality matters.

## Do Not Optimize a Single Metric in Isolation

Speed, quality, and control interact.

## Do Not Treat Targets as Permanent

Targets should mature with the service.

## Do Not Punish Teams for Metrics They Cannot Control

Metric ownership and process ownership should align.

## Do Not Let Dashboards Replace Investigation

A metric tells you where to look.

It does not automatically tell you why the problem exists.

---

# 39. Performance Framework Success Criteria

The framework is ready when:

* core metrics are defined
* baseline limitations are understood
* owners are assigned
* formulas and data sources can be defined
* segmentation is understood
* review cadence exists
* metric relationships are considered
* governance and adoption are included
* performance feeds improvement
* executive reporting can remain concise

---

# 40. Performance Framework Conclusion

The target ESM environment should produce better data than the fragmented current state.

That creates an opportunity.

It also creates a temptation to measure everything.

The better approach is to focus on the measures that tell the organization whether service is becoming:

* faster
* more consistent
* better owned
* better controlled
* easier to use
* easier to improve

The dashboard is not the outcome.

The outcome is a service operation that can use its own data to see where it is working, where it is not, and what should happen next.

**Next:** [Metrics Catalog](./metrics%20catalog.md)
