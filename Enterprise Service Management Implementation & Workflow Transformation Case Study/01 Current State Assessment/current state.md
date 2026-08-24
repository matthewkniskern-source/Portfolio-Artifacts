# Current-State Service Environment Assessment

## Purpose

Before redesigning workflows or configuring a new Enterprise Service Management platform, the existing service environment has to be understood as it actually operates.

The organization in this case has functioning support teams and established technical knowledge, but service delivery has developed around a mix of formal and informal practices. Work enters through multiple channels, ownership is not always clear, and technicians frequently compensate for process gaps through individual experience and direct coordination.

That model can work at a small scale. At approximately 750 employees across multiple facilities, it creates enough inconsistency that the organization can no longer reliably answer basic operational questions:

* What work is currently open?
* Who owns it?
* Which issues are actually urgent?
* Are service expectations being met?
* Which incidents are recurring?
* What assets or services are affected?
* Which changes contributed to an outage?
* Why was a request approved or denied?
* Are external vendors still authorized to access the environment?
* Is service performance improving over time?

This assessment establishes the baseline from which requirements and the target service model are developed.

> **Current-state assessment is not intended to criticize how individual teams work. Its purpose is to identify where the operating model depends on individual effort instead of repeatable process.**

---

# 1. Organizational Context

The fictional client is a midsize regional organization with approximately **750 employees** operating across a headquarters location and several satellite or operational facilities.

Technology services support a mixture of:

* corporate users
* operational personnel
* supervisors and managers
* business-system owners
* technical administrators
* local facility support personnel
* external vendors
* executive stakeholders

The support organization includes a centralized IT function with specialized technical teams as well as personnel who provide local or function-specific support.

Not every request reaches the centralized support function in the same way.

Some users know the formal process. Others contact whichever technician they already know.

This has gradually created two parallel service environments:

1. the **documented service process**, and
2. the **process that actually gets work done**.

The gap between those two processes is the primary transformation problem.

---

# 2. Current Service Channels

Service work currently enters the organization through several channels.

| Channel                 | Typical Use                                   | Current Issue                                                |
| ----------------------- | --------------------------------------------- | ------------------------------------------------------------ |
| Shared support email    | General incidents and requests                | Requires manual review and assignment                        |
| Direct technician email | Known issue or preferred technician           | Work may bypass centralized tracking                         |
| Phone                   | Urgent issues or users seeking immediate help | Documentation may occur after work begins or not at all      |
| Chat / messaging        | Quick questions and direct support            | Requests can become operational work without a formal record |
| Existing ticket form    | Formal incidents and requests                 | Adoption is inconsistent                                     |
| Spreadsheet             | Local tracking, projects, recurring requests  | Creates separate sources of truth                            |
| Verbal request          | Local or facility-level support               | Work may never be formally recorded                          |
| Vendor communication    | Specialized systems or equipment              | Vendor activity may exist outside the primary service record |

The number of channels is not itself the problem.

The problem is that the channels are not consistently routed into a common service-management process.

A phone call can become a ticket.

A chat message can become a ticket.

An email can become a ticket.

But whether that happens depends heavily on the technician receiving the request.

The target operating model will preserve reasonable ways for users to request help while ensuring that managed service activity ultimately enters a common system of record.

See:

* [Stakeholder Map](./02_stakeholder_map.md)
* [Current-State Workflow](../diagrams/current_state_workflow.md)

---

# 3. Current Stakeholders

The current environment involves more stakeholders than the service desk alone.

## End Users

Employees experiencing an issue or requesting a service.

Their primary concerns are straightforward:

* obtaining support quickly
* knowing whether someone owns the request
* understanding expected completion time
* receiving useful status updates
* avoiding repeated explanations of the same problem

Users currently receive different experiences depending on how they request support and which technician receives the request.

---

## Service Desk / General Support

The service desk functions as the closest thing to a centralized intake point.

Typical responsibilities include:

* initial troubleshooting
* request intake
* issue classification
* assignment
* user communication
* escalation

However, incomplete intake information and inconsistent categorization create additional work before technical resolution can begin.

---

## Specialized Technical Teams

Examples include:

* infrastructure
* network
* systems administration
* endpoint support
* applications
* identity and access management

These teams often receive escalated tickets but also receive work directly from users, managers, and other technicians.

Direct requests can reduce short-term friction while weakening centralized visibility.

---

## Business-System and Service Owners

These stakeholders are responsible for specific applications, services, or business capabilities.

They may participate in:

* service priorities
* approvals
* outage decisions
* change authorization
* escalation
* service expectations

Current ownership boundaries are not consistently documented.

---

## Management

Management needs visibility into:

* service volume
* backlog
* SLA performance
* recurring issues
* team workload
* escalation patterns
* change performance
* service quality

Existing reporting is limited because service records do not consistently represent all work being performed.

---

## External Vendors

Vendors support selected systems, equipment, and specialized technologies.

Vendor involvement may include:

* remote troubleshooting
* maintenance
* implementation
* software support
* configuration changes
* hardware support

Vendor activity is not always tied cleanly to the associated incident, change, asset, or configuration item.

This creates both operational and governance concerns.

A more detailed stakeholder and responsibility view is maintained in the [Stakeholder Map](./02_stakeholder_map.md).

---

# 4. Current-State Workflow

The current operating model can be summarized as:

```text
User experiences issue or needs service
                ↓
Chooses available contact method
                ↓
Email / Phone / Chat / Ticket / Direct Contact
                ↓
Technician or team receives request
                ↓
Is request formally recorded?
          ↙                 ↘
        Yes                  No
         ↓                    ↓
 Manual classification    Work begins informally
 and assignment               ↓
         ↓               Possible later entry
 Technician evaluates         or no record
 priority
         ↓
 Resolves / escalates /
 hands off
         ↓
 Documentation varies
         ↓
 Request considered complete
```

The supporting visual will be maintained separately so it can be referenced from the README, requirements section, target-state comparison, and implementation material:

[View Current-State Workflow Diagram](../diagrams/current_state_workflow.md)

The important feature of this workflow is the number of points where individual judgment substitutes for defined process.

Those decisions include:

* whether work should be documented
* what type of record should be created
* who owns the request
* how urgent it is
* when escalation should occur
* what information must be recorded
* whether approval is needed
* when the work is considered complete

The target environment will convert those decisions into defined workflow behavior where doing so provides operational value.

---

# 5. Current-State Pain Points

## 5.1 Fragmented Intake

Requests originate through multiple channels without consistent capture into a centralized record.

### Operational impact

* incomplete workload visibility
* work lost in personal inboxes or chat history
* difficulty measuring demand
* inconsistent user experience
* duplicate requests

---

## 5.2 Inconsistent Prioritization

Technicians frequently determine urgency based on personal judgment, user pressure, or perceived importance.

An issue reported directly by a manager may receive faster attention than a more serious service impact already in the queue.

### Operational impact

* inconsistent response
* queue jumping
* poor SLA reliability
* difficulty defending prioritization decisions
* excessive escalation

A formal impact/urgency model will be developed in the [Target Service Model](../03_TARGET_SERVICE_MODEL/03_priority_and_sla_model.md).

---

# 5.3 Unclear Ownership

Tickets and informal requests may move between individuals and groups without clear ownership expectations.

A request can be transferred because:

* the wrong team received it
* required information is missing
* responsibility is unclear
* one technician believes another team is better positioned to handle it

### Operational impact

* reassignment loops
* delayed resolution
* weak accountability
* users repeatedly explaining the same issue
* backlog aging without clear responsibility

Ownership and escalation rules will be addressed in:

[Ownership and Escalation Model](../03_TARGET_SERVICE_MODEL/04_ownership_and_escalation.md)

---

# 5.4 Weak SLA Tracking

Service-level expectations exist informally for some types of work but are not consistently measurable.

Timing may depend on:

* who received the request
* whether it was formally recorded
* which support group owns it
* whether anyone manually follows up

### Operational impact

Management cannot reliably distinguish between:

* requests completed within expectation
* requests delayed by the support organization
* requests awaiting user action
* requests awaiting approval
* requests dependent on a vendor
* requests blocked by another team

The future SLA model will separate service expectations from legitimate pause conditions and documented exceptions.

---

# 5.5 Duplicate Work

The same issue may be reported through multiple channels or by multiple users.

Without reliable duplicate detection or parent/child relationships, technicians may investigate the same condition independently.

### Operational impact

* wasted support effort
* inconsistent communication
* conflicting resolutions
* distorted ticket-volume reporting

This becomes particularly significant during widespread service disruption.

---

# 5.6 Inconsistent Handoffs

Technical handoffs are frequently based on message forwarding, informal conversations, or minimal ticket notes.

The receiving technician may have to reconstruct:

* the original issue
* troubleshooting already performed
* user impact
* affected device
* recent changes
* current status

### Operational impact

Every weak handoff effectively restarts part of the troubleshooting process.

---

# 5.7 Limited Knowledge Reuse

Technical knowledge exists primarily across:

* technician experience
* old emails
* chat history
* personal notes
* previous tickets

Known fixes may be repeatedly rediscovered.

### Operational impact

* longer resolution times
* inconsistent answers
* dependence on specific employees
* weak onboarding of new support staff

The target knowledge workflow will connect reusable knowledge directly to service delivery.

[Knowledge Management Workflow](../04_WORKFLOW_DESIGN/04_knowledge_management.md)

---

# 5.8 Weak Asset and Configuration Context

Service records do not consistently identify the affected:

* device
* application
* server
* service
* network component
* configuration item

A technician may know that a user's workstation is involved but have limited immediate visibility into:

* assigned hardware
* related configuration
* service dependencies
* previous incidents
* active changes
* warranty or vendor information

This limits both troubleshooting and broader impact analysis.

The proposed relationship model is developed in:

[Service Management Data Model](../05_DATA_AND_CONFIGURATION_MODEL/01_service_management_data_model.md)

---

# 5.9 Inconsistent Approval Evidence

Some requests require management, budget, security, or system-owner approval.

Approvals may currently occur through:

* email
* chat
* verbal authorization
* ticket comments
* separate business processes

### Operational impact

The organization may know that something was approved without having a reliable record of:

* who approved it
* what was approved
* when approval occurred
* whether the approver had appropriate authority
* whether the request changed after approval

Approval requirements will therefore be treated as workflow controls rather than simple notification steps.

---

# 5.10 Limited Reporting

Existing metrics are based primarily on the records that happen to exist.

If a technician resolves ten requests from email but creates tickets for only five, the reporting system sees five.

This creates a fundamental data-quality problem.

A dashboard built on incomplete process adoption can look precise while still being wrong.

Before management reporting becomes useful, the organization needs consistent transaction capture and workflow behavior.

Future measurement design is addressed in:

[Metrics and Continuous Improvement](../11_METRICS_AND_OPTIMIZATION/01_performance_framework.md)

---

# 6. Current-State Failure Modes

The detailed failure-mode assessment is maintained separately:

[View Pain Points and Failure Modes](./03_pain_points_and_failure_modes.md)

The highest-impact failures identified during discovery are summarized below.

| ID    | Failure Mode                                              | Likely Effect                    |
| ----- | --------------------------------------------------------- | -------------------------------- |
| FM-01 | Service request remains in personal communication channel | Lost or undocumented work        |
| FM-02 | Same issue entered through multiple channels              | Duplicate effort                 |
| FM-03 | Priority determined by requester pressure                 | Misallocated resources           |
| FM-04 | Ticket repeatedly reassigned                              | Increased resolution time        |
| FM-05 | Escalation depends on manual follow-up                    | Missed service expectations      |
| FM-06 | Required approval occurs outside service record           | Weak auditability                |
| FM-07 | Incident closed without meaningful resolution detail      | Reduced knowledge value          |
| FM-08 | Affected asset or CI not recorded                         | Weak impact analysis             |
| FM-09 | Vendor receives access without defined expiration         | Persistent access risk           |
| FM-10 | Failed change not linked to resulting incident            | Weak root-cause visibility       |
| FM-11 | Repeat incidents treated independently                    | Recurring problems remain hidden |
| FM-12 | Informal work excluded from reporting                     | Misleading operational metrics   |

These failure modes will be used later to validate that the target design addresses actual current-state problems rather than introducing functionality for its own sake.

---

# 7. Process Bottlenecks

Several bottlenecks appear repeatedly across the environment.

## Intake Bottleneck

Support personnel spend time converting incomplete user messages into usable technical records.

---

## Assignment Bottleneck

Incorrect categorization or unclear ownership creates avoidable reassignment.

---

## Approval Bottleneck

Requests requiring authorization can remain open while approval is pursued through external communication.

---

## Escalation Bottleneck

Escalation is frequently reactive.

A technician notices that work is aging and manually asks for assistance rather than the workflow identifying risk before the commitment is missed.

---

## Knowledge Bottleneck

Technicians repeatedly solve known problems because existing resolution knowledge is difficult to locate or has never been formalized.

---

## Vendor Bottleneck

External support often introduces a separate communication chain that is not fully visible within the service record.

This can obscure:

* ownership
* response time
* access status
* actions taken
* dependency on outside support

---

# 8. Baseline Performance Problems

The current organization does not have sufficiently reliable data to establish defensible numerical baselines for every service measure.

That limitation is itself a current-state finding.

Where records exist, management can measure activity. It cannot yet be assumed that those records represent the entire service environment.

The baseline assessment therefore begins with observable process conditions.

| Measure                   | Current-State Observation                         |
| ------------------------- | ------------------------------------------------- |
| First response time       | Inconsistent across intake channels               |
| Mean time to resolution   | Measurable only for formally recorded work        |
| SLA compliance            | Limited and inconsistently defined                |
| Reassignment rate         | Higher than desired due to ownership ambiguity    |
| Reopen rate               | Inconsistently measured                           |
| Repeat incidents          | Difficult to identify systematically              |
| Knowledge reuse           | Low and largely informal                          |
| Change success rate       | Not consistently connected to resulting incidents |
| Customer satisfaction     | Limited structured measurement                    |
| Backlog age               | Available only for recorded work                  |
| Vendor dependency         | Poorly represented in service reporting           |
| Workload by support group | Understated where informal work exists            |

The detailed baseline view is maintained in:

[Baseline Service Metrics](./04_baseline_metrics.md)

The implementation should establish a short post-go-live measurement period before claiming improvement. The goal is to compare reliable target-state measurements against an understood baseline, not manufacture precision where the current environment does not support it.

---

# 9. Root Cause Themes

Although the current environment contains many individual symptoms, most can be grouped into five broader causes.

### 1. No authoritative intake model

The organization has several ways to request help but no consistent requirement that managed service activity enter a common workflow.

### 2. Undefined workflow rules

Classification, assignment, escalation, approval, and closure rely too heavily on individual judgment.

### 3. Weak service ownership

Responsibility exists operationally but is not always represented clearly enough in the service-management process.

### 4. Incomplete service data relationships

Tickets are not consistently connected to the people, services, assets, configuration items, changes, vendors, and knowledge needed to provide context.

### 5. Measurement follows tooling rather than process

The organization reports what the existing system captures rather than ensuring the system captures what the organization needs to manage.

These themes become the starting point for formal requirements discovery.

[Continue to Requirements Discovery](../02_REQUIREMENTS_DISCOVERY/01_requirements_discovery.md)

---

# 10. Current-State Risk Summary

The current process does not represent an immediate technical failure. It represents **operational control weakness created by inconsistency**.

The organization can still resolve incidents and fulfill requests, but it does so with unnecessary dependence on individual behavior.

That creates several business risks:

* important work can be overlooked
* service commitments cannot always be demonstrated
* approvals may be difficult to reconstruct
* vendor activity may remain insufficiently controlled
* repeated operational failures may remain hidden
* management decisions may rely on incomplete data
* technical knowledge can leave with individual employees
* service performance may vary significantly between teams

The target state should therefore improve process control without making normal support work unnecessarily difficult.

The goal is not to force every interaction through bureaucracy.

The goal is to make sure that work requiring management, accountability, authorization, measurement, or historical context leaves behind a reliable service record.

---

# 11. Current-State Deliverables

This phase produces four primary artifacts:

| Artifact                                                                | Purpose                                                              |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [Current-State Assessment](./01_current_state_assessment.md)            | Establishes the operating baseline                                   |
| [Stakeholder Map](./02_stakeholder_map.md)                              | Identifies participants, needs, responsibilities, and influence      |
| [Pain Points and Failure Modes](./03_pain_points_and_failure_modes.md)  | Converts observed problems into defined failure conditions           |
| [Baseline Service Metrics](./04_baseline_metrics.md)                    | Defines what can and cannot currently be measured                    |
| [Current-State Workflow Diagram](../diagrams/current_state_workflow.md) | Visualizes how service work currently moves through the organization |

Together, these artifacts establish the evidence base for the next phase:

**Current State → Requirements Discovery**

The future-state solution should be traceable back to a problem identified here.
