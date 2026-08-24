# Baseline Service Metrics

## Purpose

The current environment has enough information to identify performance problems, but not enough reliable data to claim precise enterprise-wide service metrics.

That distinction matters.

If a large portion of work occurs through email, chat, phone calls, direct technician contact, or spreadsheets, the existing ticketing data only represents part of the operation.

The baseline should therefore separate:

* what can be measured now
* what can only be estimated
* what is currently unknown
* what must be measured after implementation

The goal is not to force a clean numerical baseline where one does not exist.

The goal is to establish a credible starting point for future comparison.

---

# 1. Baseline Measurement Principle

The current service environment has a data-quality problem before it has a dashboard problem.

A metric is only useful when the process generating the data is reasonably complete and consistent.

For this case, baseline measures are classified as:

| Classification | Meaning                                                                |
| -------------- | ---------------------------------------------------------------------- |
| Reliable       | Existing data is sufficiently complete for operational use             |
| Partial        | Data exists but does not represent all service activity                |
| Estimated      | Directional assessment is possible but not defensible as a precise KPI |
| Unavailable    | Current process does not capture the required data consistently        |

This classification prevents incomplete source data from being presented with false precision.

---

# 2. Current-State Baseline

| Metric                      | Current-State Status  | Baseline Observation                                                             |
| --------------------------- | --------------------- | -------------------------------------------------------------------------------- |
| First Response Time         | Partial               | Available for formal tickets but excludes some informal requests                 |
| Mean Time to Resolution     | Partial               | Measurable for recorded incidents only                                           |
| SLA Compliance              | Partial / Estimated   | Service targets are inconsistent and pause conditions are poorly defined         |
| Ticket Reassignment Rate    | Partial               | Reassignment is visible in some ticket records and appears higher than desired   |
| Reopen Rate                 | Partial               | Closure and reopen behavior are not consistently defined                         |
| Repeat Incident Rate        | Unavailable           | Related incidents are not consistently correlated                                |
| Knowledge Reuse             | Unavailable           | Informal reuse is common but not measured                                        |
| Change Success Rate         | Partial               | Change records exist but failed changes are not consistently linked to incidents |
| Customer Satisfaction       | Limited               | No consistent post-resolution feedback model                                     |
| Backlog Age                 | Partial               | Available only for work captured in the ticketing system                         |
| Vendor Dependency           | Unavailable           | Vendor involvement is not consistently structured                                |
| First-Contact Resolution    | Unavailable / Partial | Inconsistent intake and closure data reduce reliability                          |
| Ticket Volume by Channel    | Unavailable           | Informal channels are not consistently converted into service records            |
| Asset / CI Association Rate | Partial               | Asset and CI relationships are inconsistently populated                          |
| Approval Cycle Time         | Unavailable           | Approvals may occur outside the service record                                   |
| SLA Exception Rate          | Unavailable           | Exception reasons are not consistently recorded                                  |

---

# 3. Baseline Data Limitations

Several conditions prevent the current environment from producing a complete performance baseline.

## Incomplete Transaction Capture

Not all service activity creates a formal record.

This means ticket volume cannot be assumed to equal actual support demand.

---

## Inconsistent Start and Stop Points

A timing metric only works if the organization agrees on when the clock begins and ends.

Current ambiguity includes:

* whether work begins when the user first contacts support or when a ticket is created
* whether waiting for user response pauses the clock
* whether waiting for vendor support pauses the clock
* whether approval delays count against fulfillment time
* whether scheduled work is treated as overdue

Without consistent definitions, two teams can report the same metric and still be measuring different things.

---

## Inconsistent Classification

Category, priority, assignment group, and resolution fields are not consistently populated.

This weakens:

* trend analysis
* workload comparison
* recurring incident identification
* service-level reporting

---

## Weak Record Relationships

Tickets are not consistently linked to:

* affected assets
* configuration items
* services
* related changes
* vendors
* knowledge articles

This limits performance analysis beyond basic ticket counts.

---

# 4. Initial Baseline Findings

Even without precise enterprise-wide numbers, several current-state findings are clear.

## Response Performance Varies by Channel

A direct technician message may receive an immediate response while a formal request remains in a queue.

That makes raw response-time comparisons unreliable unless intake is standardized.

---

## Reassignment Is a Significant Source of Delay

The [Pain Points and Failure Modes](./03_pain_points_and_failure_modes.md) assessment identifies routing and ownership ambiguity as a recurring source of lost time.

The target model should therefore measure both:

* number of reassignments
* time spent before correct ownership is established

---

## SLA Performance Cannot Yet Be Treated as Authoritative

Existing SLA reporting is weakened by:

* incomplete transaction capture
* unclear pause conditions
* inconsistent priority
* manual escalation

The first implementation goal is therefore not to improve a percentage on a dashboard.

It is to make the percentage worth trusting.

---

## Knowledge Reuse Is Mostly Invisible

Technicians may reuse prior experience, old tickets, or informal notes, but the organization cannot reliably measure:

* article use
* article effectiveness
* deflection
* reuse during ticket resolution

A formal knowledge process is required before knowledge metrics become meaningful.

---

## Repeat Incidents Are Under-Identified

The current process is better at counting individual incidents than identifying recurring conditions.

This limits the organization's ability to distinguish:

* isolated user issues
* repeating technical defects
* service degradation
* failed changes
* location-specific patterns

---

# 5. Target Measurement Framework

The target environment should establish a stable set of operational measures after implementation.

Core measures will include:

| Metric                      | Purpose                                                 |
| --------------------------- | ------------------------------------------------------- |
| First Response Time         | Measure speed of initial support engagement             |
| Mean Time to Resolution     | Measure incident-resolution efficiency                  |
| SLA Compliance              | Measure performance against defined service commitments |
| Reassignment Rate           | Identify routing and ownership problems                 |
| Reopen Rate                 | Identify weak resolution or closure quality             |
| Repeat Incident Rate        | Identify recurring operational issues                   |
| Knowledge Reuse             | Measure reuse of validated support knowledge            |
| Change Success Rate         | Measure quality of implemented changes                  |
| Customer Satisfaction       | Measure user perception of service quality              |
| Backlog Age                 | Identify aging unresolved work                          |
| First-Contact Resolution    | Measure resolution efficiency at initial support tier   |
| Asset / CI Association Rate | Measure data completeness for operational context       |
| Approval Cycle Time         | Identify approval bottlenecks                           |
| Vendor Dependency Time      | Measure externally dependent service delay              |

Detailed KPI definitions are developed later in:

[Metrics and Continuous Improvement](../11_METRICS_AND_OPTIMIZATION/01_performance_framework.md)

---

# 6. Measurement Design Requirements

The future platform should not merely display metrics.

It should support the data quality necessary to make them credible.

Measurement design therefore requires:

* consistent ticket creation
* standardized status definitions
* defined SLA clock behavior
* controlled priority logic
* required ownership
* structured closure data
* defined exception reasons
* asset and CI relationships
* vendor dependency status
* approval timestamps
* change relationships
* knowledge usage data

Several of these will become formal requirements in:

[Requirements Discovery](../02_REQUIREMENTS_DISCOVERY/01_requirements_discovery.md)

---

# 7. Post-Implementation Baseline Period

The organization should establish a short stabilization period after go-live before declaring performance improvement.

The initial post-implementation period should be used to validate:

* data completeness
* routing accuracy
* SLA behavior
* status usage
* closure quality
* adoption
* reporting accuracy

Once the process is stable, the organization can establish a credible target-state baseline.

This prevents early implementation noise from being mistaken for long-term service performance.

---

# 8. Baseline-to-Target Comparison

A later optimization artifact should compare the current-state condition against mature target-state performance.

The comparison should emphasize measurable operational change rather than arbitrary improvement claims.

Example structure:

| Measure              | Current State | Target State                       |
| -------------------- | ------------- | ---------------------------------- |
| Service capture      | Partial       | Managed work consistently recorded |
| Priority consistency | Subjective    | Rule-based                         |
| SLA measurement      | Partial       | Defined and auditable              |
| Ownership visibility | Inconsistent  | Explicit                           |
| Knowledge reuse      | Informal      | Measurable                         |
| Vendor tracking      | Limited       | Structured                         |
| Change relationship  | Inconsistent  | Linked                             |
| Reporting confidence | Limited       | Trusted operational data           |

A visual version will be maintained in:

[Current-to-Target Metrics View](../diagrams/current_target_metrics.md)

---

# 9. Baseline Conclusion

The most important baseline finding is not a specific response time or ticket count.

It is that the organization currently lacks enough process consistency to trust several of its own service metrics.

That gives the implementation a clear measurement objective:

> **Improve the process first, then use the resulting data to prove whether performance improved.**

The target ESM model should make management reporting more useful because the underlying service activity is being captured and governed more consistently.

The next phase converts these current-state findings into formal requirements.

**Next:** [Requirements Discovery](../02_REQUIREMENTS_DISCOVERY/01_requirements_discovery.md)
