# Metrics Catalog

## Purpose

This artifact defines the core performance metrics used to evaluate the target Enterprise Service Management environment.

The catalog is intended to standardize:

* metric names
* business purpose
* calculation logic
* ownership
* review cadence
* interpretation

The goal is to prevent different teams from using the same metric name to mean different things.

The operating principle is:

> **A metric should have one definition, one purpose, and an owner who knows what to do when it moves.**

This artifact builds on:

* [Performance Framework](./performance%20framework.md)
* [Baseline Metrics](../01%20Current%20State/baseline%20metrics.md)
* [Control Matrix](../06%20Governance%20and%20Controls/control%20matrix.md)
* [Adoption Strategy](../10%20Adoption%20and%20Training/adoption%20strategy.md)

---

# 1. Metric Categories

The catalog groups metrics into:

| Category            | Focus                            |
| ------------------- | -------------------------------- |
| Service Performance | Response and resolution          |
| Workflow Quality    | Ownership and process efficiency |
| SLA                 | Service commitment               |
| Change              | Change quality and stability     |
| Knowledge           | Reuse and content value          |
| Vendor              | External dependency              |
| Governance          | Control performance              |
| Adoption            | Use of target process            |
| User Experience     | Service perception               |
| Automation and AI   | Capability effectiveness         |

---

# 2. Service Performance Metrics

| Metric                   | Definition                                                     | Purpose                         | Owner                  | Review           |
| ------------------------ | -------------------------------------------------------------- | ------------------------------- | ---------------------- | ---------------- |
| First Response Time      | Time from valid ticket creation to meaningful support response | Measure responsiveness          | Incident Process Owner | Weekly / Monthly |
| Mean Time to Resolution  | Average elapsed time from intake to resolution                 | Measure resolution efficiency   | Incident Process Owner | Monthly          |
| Median Resolution Time   | Median elapsed resolution time                                 | Reduce distortion from outliers | Incident Process Owner | Monthly          |
| First Contact Resolution | Percentage resolved without unnecessary transfer               | Measure frontline effectiveness | Service Desk Lead      | Monthly          |
| Backlog Volume           | Count of active unresolved records                             | Measure workload                | Support Leads          | Daily / Weekly   |
| Backlog Age              | Age distribution of active work                                | Identify stale work             | Support Leads          | Weekly           |
| Reopen Rate              | Percentage of resolved records reopened                        | Measure resolution quality      | Incident Process Owner | Monthly          |

---

# 3. First Response Time

## Definition

Elapsed time between valid ticket creation and the first meaningful operational response.

## Formula

```text id="u6x9hd"
First Response Timestamp
-
Ticket Creation Timestamp
```

## Exclusions

An automated acknowledgement alone should not count unless the organization explicitly defines it as meaningful response.

## Segment By

* service
* priority
* support group
* channel

## Interpretation

Increasing response time may indicate:

* workload
* poor routing
* understaffing
* queue ownership issues

---

# 4. Mean Time to Resolution

## Definition

Average elapsed time between valid intake and resolution.

## Formula

```text id="9u3qqm"
Sum of Resolution Durations
÷
Resolved Records
```

## Segment By

* priority
* service
* support group
* incident category

## Interpretation

MTTR should be reviewed alongside:

* reopen rate
* reassignment
* vendor wait
* SLA exceptions

Lower MTTR is not automatically better if resolution quality declines.

---

# 5. SLA Metrics

| Metric             | Definition                                      | Purpose                       |
| ------------------ | ----------------------------------------------- | ----------------------------- |
| SLA Compliance     | Percentage of applicable records meeting target | Measure service commitment    |
| SLA Breach Rate    | Percentage exceeding target                     | Identify service failure      |
| SLA Warning Rate   | Percentage reaching defined risk threshold      | Identify near-breach workload |
| SLA Exception Rate | Percentage receiving approved exception         | Detect policy pressure        |
| SLA Pause Time     | Time excluded under defined policy              | Understand delay context      |

---

# 6. SLA Compliance

## Formula

```text id="9l5eqt"
Records Meeting SLA
÷
Applicable Records
× 100
```

The denominator should include only records governed by the applicable SLA.

Approved exceptions should remain separately reportable.

---

# 7. SLA Exception Rate

## Formula

```text id="ff0x1q"
Approved SLA Exceptions
÷
SLA-Governed Records
× 100
```

## Interpretation

A rising exception rate may indicate:

* unrealistic SLA
* poor workflow design
* vendor dependency
* misuse of exception policy

An improving SLA percentage with a sharply rising exception rate deserves review.

---

# 8. Workflow Quality Metrics

| Metric                     | Definition                                   | Purpose                        |
| -------------------------- | -------------------------------------------- | ------------------------------ |
| Reassignment Rate          | Percentage of records reassigned             | Measure routing quality        |
| Average Reassignments      | Average ownership changes per ticket         | Measure workflow friction      |
| Unowned Record Count       | Active records without valid owner           | Measure accountability failure |
| Closure Validation Failure | Attempts blocked due to missing closure data | Measure closure quality        |
| Waiting-State Age          | Time records remain in waiting status        | Identify hidden delay          |
| Escalation Rate            | Percentage requiring escalation              | Measure workflow pressure      |

---

# 9. Reassignment Rate

## Formula

```text id="fck42v"
Records Reassigned at Least Once
÷
Total Records
× 100
```

High reassignment may indicate:

* weak intake
* poor service mapping
* unclear ownership
* routing-rule problems

Legitimate escalation should be distinguished from avoidable routing churn where possible.

---

# 10. Change Metrics

| Metric                     | Definition                               | Purpose                        |
| -------------------------- | ---------------------------------------- | ------------------------------ |
| Change Success Rate        | Percentage validated successful          | Measure implementation quality |
| Failed Change Rate         | Percentage unsuccessful                  | Identify change instability    |
| Backout Rate               | Percentage requiring backout             | Measure recovery demand        |
| Emergency Change Rate      | Emergency changes as percentage of total | Identify planning pressure     |
| Incidents Caused by Change | Incidents linked to change activity      | Measure service impact         |
| Rescheduled Change Rate    | Percentage moved after approval          | Measure readiness quality      |

---

# 11. Change Success Rate

## Formula

```text id="2gy6dp"
Successful Changes
÷
Completed Changes
× 100
```

"Successful with Issue" should remain distinguishable from fully successful change where the platform supports it.

---

# 12. Failed Change Rate

## Formula

```text id="023guc"
Failed Changes
÷
Completed Changes
× 100
```

This metric should be analyzed by:

* service
* risk
* change type
* implementation team

---

# 13. Emergency Change Rate

## Formula

```text id="i6xrlh"
Emergency Changes
÷
Total Changes
× 100
```

A sustained increase may indicate:

* poor planning
* unstable systems
* delayed remediation
* vulnerability pressure
* misuse of emergency classification

---

# 14. Knowledge Metrics

| Metric                      | Definition                                          | Purpose                            |
| --------------------------- | --------------------------------------------------- | ---------------------------------- |
| Knowledge Reuse Rate        | Articles used in support activity                   | Measure operational value          |
| Knowledge Helpful Rate      | Positive helpful feedback                           | Measure usefulness                 |
| Articles Used in Resolution | Resolved records linked to article                  | Measure support contribution       |
| Stale Article Count         | Published articles beyond review date               | Measure lifecycle quality          |
| Knowledge Gap Candidates    | Repeat issues lacking suitable knowledge            | Identify documentation opportunity |
| Self-Service Deflection     | User issue resolved without ticket where measurable | Measure avoided demand             |

---

# 15. Knowledge Reuse Rate

A practical implementation may calculate:

```text id="dhdq7d"
Tickets Using Knowledge
÷
Eligible Tickets
× 100
```

The exact denominator should be defined carefully.

Not every ticket is an appropriate knowledge-use candidate.

---

# 16. Vendor Metrics

| Metric                              | Definition                                | Purpose                              |
| ----------------------------------- | ----------------------------------------- | ------------------------------------ |
| Vendor-Dependent Ticket Rate        | Tickets requiring vendor involvement      | Measure external dependency          |
| Average Vendor Wait                 | Average time waiting on vendor            | Measure dependency delay             |
| Aging Vendor Cases                  | Vendor-dependent records beyond threshold | Identify escalation need             |
| Vendor Access Expiration Compliance | Temporary access disabled on schedule     | Measure access control               |
| Vendor-Related Change Failure       | Failed changes involving vendor           | Measure external implementation risk |

---

# 17. Vendor Access Expiration Compliance

## Formula

```text id="elbh3u"
Vendor Access Disabled on Time
÷
Expired Vendor Access Records
× 100
```

If manual disablement is the compensating control, completion of that action should be included.

---

# 18. Governance Metrics

| Metric                             | Definition                                | Purpose                                        |
| ---------------------------------- | ----------------------------------------- | ---------------------------------------------- |
| Self-Approval Block Count          | Blocked prohibited self-approval attempts | Validate SoD enforcement                       |
| Priority Override Rate             | Tickets with authorized override          | Assess priority model                          |
| Access Review Completion           | Required reviews completed                | Measure RBAC governance                        |
| Control Failure Count              | Recorded control failures                 | Identify governance weakness                   |
| Open Control Exceptions            | Active unresolved exceptions              | Measure current exposure                       |
| Exception Age                      | Time exception remains open               | Identify temporary controls becoming permanent |
| Unauthorized Configuration Attempt | Blocked or detected config activity       | Measure platform governance                    |

---

# 19. Priority Override Rate

## Formula

```text id="eoq3rp"
Priority Overrides
÷
Priority-Governed Incidents
× 100
```

Repeated override patterns should trigger review of:

* matrix design
* service context
* training
* requester pressure

---

# 20. Access Review Completion

## Formula

```text id="s9lmlk"
Completed Required Reviews
÷
Scheduled Reviews
× 100
```

Priority review populations may include:

* platform administrators
* privileged roles
* approvers
* vendor users
* audit roles

---

# 21. Adoption Metrics

| Metric                      | Definition                                | Purpose                        |
| --------------------------- | ----------------------------------------- | ------------------------------ |
| Managed Intake Rate         | Work entering approved channels           | Measure process adoption       |
| Legacy Channel Usage        | Work entering retired / informal channels | Measure bypass                 |
| Catalog Utilization         | Requests submitted through catalog        | Measure self-service use       |
| Approval Aging              | Pending approval duration                 | Measure approver participation |
| Training-Related Error Rate | Issues attributable to misunderstanding   | Measure readiness              |
| Knowledge Usage             | Knowledge use during service activity     | Measure support adoption       |

---

# 22. Managed Intake Rate

## Formula

```text id="yuz5eo"
Records Entering Approved Intake
÷
Known Service Activity
× 100
```

This metric may be difficult to calculate precisely at first because off-process work is inherently difficult to count.

Initial reporting may use best available operational estimates until managed intake becomes dominant.

---

# 23. Legacy Channel Usage

Examples include:

* direct technician contact
* unmanaged email
* spreadsheet request
* old portal
* informal chat

The metric should trend downward after go-live.

A persistent rate may indicate:

* poor communication
* catalog usability issue
* process resistance
* management bypass

---

# 24. User Experience Metrics

| Metric                    | Purpose                                            |
| ------------------------- | -------------------------------------------------- |
| CSAT                      | Measure satisfaction with completed interaction    |
| Ease of Submission        | Measure intake usability                           |
| Status Clarity            | Measure user understanding                         |
| Repeat Contact Rate       | Identify unclear communication or unresolved issue |
| Complaint Theme Frequency | Identify recurring experience problems             |

User-experience metrics should complement operational data.

---

# 25. CSAT

A simple implementation may ask:

> How satisfied were you with the support you received?

A short scale is sufficient.

The goal is trend and context.

Not survey complexity.

---

# 26. Automation Metrics

| Metric                     | Definition                                | Purpose                              |
| -------------------------- | ----------------------------------------- | ------------------------------------ |
| Automation Success Rate    | Successful executions                     | Measure reliability                  |
| Automation Failure Rate    | Failed executions                         | Identify unstable rules/integrations |
| Manual Exception Rate      | Automated flows requiring manual recovery | Measure operational dependency       |
| Routing Accuracy           | Correct automated assignments             | Measure rule quality                 |
| Automated Fulfillment Rate | Eligible requests fulfilled automatically | Measure efficiency                   |
| Automation Recovery Time   | Time to recover failed automated flow     | Measure resilience                   |

---

# 27. Automation Success Rate

## Formula

```text id="3y11zk"
Successful Executions
÷
Automation Executions
× 100
```

Automation should be reviewed by rule or process.

An aggregate platform rate may hide one unstable automation.

---

# 28. AI Metrics

| Metric                      | Definition                                 | Purpose                        |
| --------------------------- | ------------------------------------------ | ------------------------------ |
| Suggestion Acceptance Rate  | Recommendations accepted without change    | Measure usefulness             |
| Modification Rate           | Recommendations accepted after edit        | Measure partial value          |
| Rejection Rate              | Recommendations rejected                   | Identify weak fit              |
| Categorization Accuracy     | Correct classifications                    | Measure recommendation quality |
| Duplicate Confirmation Rate | Suggested duplicates confirmed             | Measure correlation quality    |
| AI Correction Rate          | Outputs requiring correction               | Identify reliability issues    |
| AI-Related Incident Count   | Operational incidents caused by AI feature | Measure risk                   |
| AI Feature Availability     | Availability of AI assistance              | Monitor dependency             |

AI metrics should be evaluated by use case.

---

# 29. Reporting Quality Metrics

| Metric                       | Purpose                                 |
| ---------------------------- | --------------------------------------- |
| Report Reconciliation Rate   | Validate dashboard accuracy             |
| Missing Data Rate            | Identify weak source data               |
| Invalid Relationship Count   | Identify data-integrity failures        |
| Metric Definition Exceptions | Identify inconsistent calculation logic |

The reporting layer should be tested like any other part of the implementation.

---

# 30. Data Quality Metrics

| Metric                              | Definition                                    |
| ----------------------------------- | --------------------------------------------- |
| Active Services with Owner          | Percentage of active services with owner      |
| Tickets with Service Association    | Percentage of tickets linked to service       |
| Changes with CI Association         | Percentage of applicable changes linked to CI |
| CIs with Active Owner               | Percentage of managed CIs with owner          |
| Knowledge Past Review               | Count of stale articles                       |
| Invalid Reference Count             | Records using inactive/invalid reference data |
| Temporary Access Missing Expiration | Count of invalid temporary access records     |

These measures provide context for the reliability of downstream metrics.

---

# 31. Metric Priority

The initial dashboard should not include the entire catalog.

## Tier 1 — Operational

* First Response Time
* MTTR
* SLA Compliance
* Backlog Age
* Reassignment Rate
* P1/P2 Volume

## Tier 2 — Quality and Governance

* Reopen Rate
* Change Success
* Emergency Change Rate
* Vendor Expiration Compliance
* Control Exceptions
* Knowledge Reuse

## Tier 3 — Optimization

* Managed Intake
* Self-Service Deflection
* Automation Value
* AI Performance
* Repeat Incident Reduction

---

# 32. Executive Metrics

A hiring-manager or executive-style view should remain small.

Recommended indicators:

| Metric                | Why It Matters     |
| --------------------- | ------------------ |
| SLA Trend             | Service commitment |
| Critical Backlog      | Operational risk   |
| MTTR Trend            | Responsiveness     |
| Change Success        | Stability          |
| CSAT                  | User experience    |
| Managed Intake        | Adoption           |
| Governance Exceptions | Control health     |

These should provide enough context to prompt deeper review.

---

# 33. Process Owner Metrics

## Incident Owner

* FRT
* MTTR
* SLA
* reassignment
* reopen
* repeat incident

## Request Owner

* fulfillment time
* approval time
* catalog demand
* rejection
* cancellation

## Change Owner

* success
* failure
* backout
* emergency
* incident caused by change

## Knowledge Owner

* reuse
* helpfulness
* stale articles
* knowledge gaps

---

# 34. Metric Review Rules

A metric should trigger investigation when:

* it crosses an approved threshold
* trend worsens repeatedly
* performance differs materially by service
* another related metric indicates contradictory behavior

Example:

```text id="js37qk"
SLA Compliance ↑
+
SLA Exceptions ↑
=
Review Required
```

---

# 35. Metric Interpretation Guardrails

## Do Not Use MTTR Alone

Fast closure may hide poor resolution quality.

## Do Not Use SLA Alone

Exception behavior can distort the result.

## Do Not Penalize Legitimate Escalation

Reassignment requires context.

## Do Not Treat More Knowledge as Better Knowledge

Usefulness matters.

## Do Not Treat Automation Volume as Value

Operational outcome matters.

## Do Not Treat AI Acceptance as Accuracy

Users may accept weak recommendations.

---

# 36. Metric Definition Ownership

Metric definitions should change only through controlled governance.

A formula change may affect:

* trends
* targets
* management reporting
* historical comparison

Changes should therefore be:

* documented
* reviewed
* communicated
* versioned where practical

---

# 37. Metric Lifecycle

```text id="v67jp6"
Define
  ↓
Validate
  ↓
Measure
  ↓
Review
  ↓
Improve / Retire
```

Metrics that no longer support decisions should be removed from primary reporting.

---

# 38. Metrics Catalog Success Criteria

The catalog is ready when:

* core metric definitions are consistent
* business purpose is clear
* owners are identified
* formulas are understood
* data sources can support calculation
* segmentation is defined where needed
* review cadence is known
* related metrics are interpreted together
* dashboard priority is established

---

# 39. Metrics Catalog Conclusion

The metrics catalog gives the target service-management environment a common measurement language.

That matters because the same platform can produce dozens of dashboards and still leave teams arguing over what the numbers actually mean.

The useful metrics are the ones that help the organization answer:

* Are we responding?
* Are we resolving?
* Are we routing correctly?
* Are controls working?
* Are users adopting the process?
* Are changes making the environment better or worse?

If a metric cannot help answer one of those kinds of questions, it probably does not belong on the primary dashboard.

**Next:** [Continuous Improvement](./continuous%20improvement.md)
