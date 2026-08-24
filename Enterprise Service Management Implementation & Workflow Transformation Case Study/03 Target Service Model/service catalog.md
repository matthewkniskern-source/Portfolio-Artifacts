# Service Catalog

## Purpose

The service catalog provides a structured, user-facing entry point into repeatable services and requests supported by the organization.

The catalog should make it easier for users to ask for what they need without requiring them to understand:

* internal IT team structure
* assignment groups
* technical categories
* backend systems
* workflow states

The catalog is not simply a list of things IT does.

Each catalog item represents a defined service transaction with enough structure to support:

* consistent intake
* ownership
* approvals
* fulfillment
* SLA measurement
* automation
* reporting

The target catalog is intentionally limited in this case study.

The objective is to demonstrate a reusable design pattern that can be expanded as the service-management model matures.

---

# 1. Catalog Design Principles

The target catalog follows six principles.

## 1.1 Organize Around User Need

Users should select services based on the outcome they need.

For example:

**Request Application Access**

is preferable to:

**Identity Administration Queue**

The first describes the user's need.

The second describes the organization's internal structure.

---

## 1.2 Separate Incidents from Requests

A service catalog primarily supports repeatable requests.

An incident represents something that is broken or degraded.

A service request represents something the user is asking the organization to provide.

Examples:

| User Need                  | Record Type     |
| -------------------------- | --------------- |
| Email is unavailable       | Incident        |
| Create a shared mailbox    | Service Request |
| Laptop will not boot       | Incident        |
| Request replacement laptop | Service Request |
| VPN connection fails       | Incident        |
| Request VPN access         | Service Request |

The distinction matters because the workflows, approvals, and service expectations are different.

---

## 1.3 Collect Information Once

Catalog forms should collect information required to fulfill the request without repeatedly asking the user for information the organization already has.

Where available, the platform should populate known context such as:

* requester
* manager
* department
* location
* assigned device
* employment status

Forms should ask for information that changes the fulfillment decision.

They should not become questionnaires simply because fields are available.

---

## 1.4 Approval Should Follow Risk

Approval is applied where a business decision is required.

It should not be added to every request by default.

Examples:

| Request                                           | Approval Need                            |
| ------------------------------------------------- | ---------------------------------------- |
| Standard software installation from approved list | None or automated entitlement validation |
| New privileged account                            | Required                                 |
| Replacement keyboard                              | None                                     |
| New laptop outside lifecycle policy               | Manager / asset approval                 |
| Existing business application access              | Application owner where required         |
| Temporary vendor administrative access            | Sponsor + authorized access approval     |

This keeps control proportional to the request.

---

## 1.5 Ownership Must Be Defined Before Publication

A catalog item should not be published until the organization knows:

* who owns the service
* who fulfills the request
* who approves it where applicable
* what information is required
* what completion means

Publishing a request form without a defined fulfillment model simply makes intake cleaner while leaving the underlying process unresolved.

---

## 1.6 Catalog Items Should Be Measurable

Each production catalog item should support enough structured information to evaluate:

* request volume
* fulfillment time
* approval delay
* reassignment
* completion rate
* user satisfaction where applicable

Catalog maturity should be measured by service performance, not by how many items have been published.

---

# 2. Catalog Structure

The initial catalog is organized into six user-facing categories.

```text
Enterprise Service Catalog
│
├── Accounts and Access
│
├── End-User Technology
│
├── Business Applications
│
├── Collaboration and Communication
│
├── Network and Connectivity
│
└── Facilities Technology Support
```

A future expansion could introduce additional business-service areas without changing the underlying catalog model.

A visual representation will be maintained in:

[Service Catalog Structure](../diagrams/service%20catalog%20structure.md)

---

# 3. Catalog Item Standard

Every catalog item should define a common set of attributes.

| Attribute            | Purpose                                 |
| -------------------- | --------------------------------------- |
| Catalog Item         | User-facing request name                |
| Service              | Business or technical service supported |
| Service Owner        | Accountable service owner               |
| Fulfillment Group    | Group performing the work               |
| Required Information | Information needed to begin fulfillment |
| Approval             | Required authorization                  |
| Target               | Expected fulfillment time               |
| Automation           | Candidate automated behavior            |
| Closure Criteria     | Conditions required for completion      |

This common structure supports consistent implementation across different service areas.

---

# 4. Representative Catalog

The following catalog items represent the initial implementation pattern.

| ID     | Catalog Item                                       | Category                        | Owner                   | Fulfillment Group              | Approval    | Target                 |
| ------ | -------------------------------------------------- | ------------------------------- | ----------------------- | ------------------------------ | ----------- | ---------------------- |
| CAT-01 | Request Standard Application Access                | Accounts and Access             | Application Owner       | Identity / Application Support | Conditional | 2 Business Days        |
| CAT-02 | Request Privileged Access                          | Accounts and Access             | Security / System Owner | Identity and Access            | Required    | 3 Business Days        |
| CAT-03 | Request Standard Software                          | End-User Technology             | Endpoint Service Owner  | Endpoint Support               | Conditional | 2 Business Days        |
| CAT-04 | Request Computer Equipment                         | End-User Technology             | Endpoint Service Owner  | Endpoint / Asset Support       | Conditional | 5 Business Days        |
| CAT-05 | Request Shared Mailbox                             | Collaboration and Communication | Messaging Service Owner | Messaging Support              | Required    | 3 Business Days        |
| CAT-06 | Request VPN Access                                 | Network and Connectivity        | Network Service Owner   | Network / Identity             | Conditional | 2 Business Days        |
| CAT-07 | Request Business Application Support / Enhancement | Business Applications           | Application Owner       | Application Support            | Conditional | Varies by Request Type |
| CAT-08 | Request Temporary Vendor Access                    | Accounts and Access             | System / Service Owner  | Identity / Security            | Required    | Defined Access Window  |

The service targets shown here are design assumptions for the fictional organization and would be validated with service owners before implementation.

---

# 5. CAT-01 — Standard Application Access

## User Need

The user requires access to an approved business application.

## Service

Business Application Access

## Service Owner

Application Owner

## Fulfillment Group

Identity and Access or Application Support, depending on application architecture.

## Required Information

The form should capture or derive:

* requester
* user receiving access
* application
* requested role or access level
* business justification where required
* manager
* department
* effective date

## Approval Logic

Approval depends on application and requested role.

```text
Application Access Request
          ↓
Standard Role?
     ↙          ↘
   Yes           No
    ↓             ↓
Entitlement    Application /
Validation     Data Owner Approval
    ↓             ↓
Fulfillment ←─────┘
```

Standard low-risk access may require no manual approval where authoritative entitlement rules already exist.

Elevated or sensitive application roles require designated authorization.

## Target

**2 Business Days**

## Automation Opportunities

* populate requester information
* retrieve manager relationship
* route by selected application
* route approval
* notify fulfillment group
* notify requester at completion

## Closure Criteria

* required approval satisfied
* access provisioned
* fulfillment result recorded
* requester notified

Related control:

[RBAC and Approval Controls](../06%20Governance%20and%20Controls/rbac%20and%20approval%20controls.md)

---

# 6. CAT-02 — Privileged Access

## User Need

An authorized employee requires elevated administrative access to perform defined job responsibilities.

## Service

Privileged Access Management

## Service Owner

Security / System Owner

## Fulfillment Group

Identity and Access

## Required Information

* user
* target system
* requested privilege
* business purpose
* requested duration
* manager
* system owner
* relevant ticket/change where applicable

## Approval Logic

Privileged access requires explicit approval.

```text
Privileged Access Request
          ↓
Manager / Sponsor Validation
          ↓
System Owner Approval
          ↓
Security / Access Approval
          ↓
Provision
          ↓
Validation
```

The exact approval sequence may vary by risk and organizational policy.

## Control Requirements

* self-approval prohibited
* approver authority validated
* approval history retained
* privilege scoped to required access
* expiration applied where temporary
* fulfillment recorded

## Target

**3 Business Days**

Emergency access may follow a separate controlled process.

## Automation Opportunities

* manager lookup
* system-owner lookup
* approval routing
* expiration reminders
* temporary-access expiration
* notification

## Closure Criteria

* approval complete
* access provisioned
* effective access validated
* expiration defined where applicable
* audit record complete

Related requirements:

* BR-07 — Separation of Duties
* FR-16 — Self-Approval Prevention
* BR-12 — Temporary Access Governance

---

# 7. CAT-03 — Standard Software Request

## User Need

The user requires approved software on an organization-managed endpoint.

## Service

End-User Software

## Service Owner

Endpoint Service Owner

## Fulfillment Group

Endpoint Support

## Required Information

* user
* managed device
* requested software
* business need where required

## Approval Logic

```text
Software Request
       ↓
Approved Standard?
   ↙            ↘
 Yes             No
  ↓               ↓
License /      Review /
Entitlement    Approval
Check             ↓
  ↓               │
Install ←─────────┘
```

Approved software with available entitlement should not require unnecessary manager approval.

## Target

**2 Business Days**

## Automation Opportunities

Where endpoint-management integration supports it:

* entitlement validation
* software deployment
* status updates
* fulfillment confirmation

## Closure Criteria

* entitlement confirmed
* installation completed
* device relationship recorded
* user notified

---

# 8. CAT-04 — Computer Equipment Request

## User Need

The user requires organization-provided computer equipment.

Representative equipment may include:

* laptop
* desktop
* monitor
* docking station
* approved peripheral

## Service

End-User Hardware

## Service Owner

Endpoint Service Owner

## Fulfillment Group

Endpoint / Asset Support

## Required Information

* user
* equipment type
* location
* business need
* replacement or new equipment
* existing asset where applicable

## Approval Logic

Routine lifecycle replacement may follow established asset policy without additional approval.

New equipment, nonstandard equipment, or out-of-cycle replacement may require:

* manager approval
* budget approval
* asset-management validation

## Target

**5 Business Days**, subject to inventory availability.

## Automation Opportunities

* retrieve assigned assets
* route approval
* create fulfillment tasks
* update asset assignment
* generate pickup / delivery notification

## Closure Criteria

* approval complete where required
* equipment assigned
* asset record updated
* user receipt confirmed where applicable

---

# 9. CAT-05 — Shared Mailbox Request

## User Need

A team requires a shared organizational mailbox.

## Service

Messaging and Collaboration

## Service Owner

Messaging Service Owner

## Fulfillment Group

Messaging Support

## Required Information

* requested mailbox name
* business purpose
* owner
* members
* access levels
* department
* requested effective date

## Approval

A designated manager or service owner must authorize mailbox creation.

## Target

**3 Business Days**

## Automation Opportunities

* naming validation
* approval routing
* fulfillment task
* membership configuration
* completion notification

## Closure Criteria

* approved owner identified
* mailbox created
* membership applied
* owner notified

---

# 10. CAT-06 — VPN Access

## User Need

An employee requires approved remote connectivity to organizational resources.

## Service

Remote Access

## Service Owner

Network Service Owner

## Fulfillment Group

Network / Identity

## Required Information

* user
* business requirement
* employment / identity status
* device where applicable
* requested access scope

## Approval Logic

Approval may depend on:

* user role
* access scope
* remote-access policy
* system sensitivity

## Target

**2 Business Days**

## Automation Opportunities

* identity validation
* device eligibility check
* approval routing
* group membership
* notification

## Closure Criteria

* authorization validated
* required access provisioned
* access test completed where applicable
* user notified

---

# 11. CAT-07 — Business Application Support / Enhancement Request

## User Need

A business user requires a non-incident change, configuration adjustment, report, enhancement, or application service.

## Service

Business Applications

## Service Owner

Application Owner

## Fulfillment Group

Application Support

## Required Information

Depending on request subtype:

* application
* requested outcome
* business justification
* affected users
* desired completion date
* expected business impact

## Request Classification

This catalog item requires additional triage because not every request should remain a service request.

```text
Application Request
        ↓
What is being requested?
   ┌────┼─────┐
   │    │     │
Support Config Enhancement
   │    │     │
Request Request Assessment
               ↓
        Change / Project?
```

A larger enhancement may leave the standard service-request process and enter change, project, or development governance.

## Target

Depends on request subtype.

## Design Note

This boundary matters.

The service catalog should provide a clean front door without pretending every piece of business demand can be fulfilled through the same workflow.

---

# 12. CAT-08 — Temporary Vendor Access

## User Need

An approved external vendor requires temporary access to support a defined system, service, or implementation activity.

## Service

Vendor / Third-Party Access

## Service Owner

Relevant System or Service Owner

## Fulfillment Group

Identity / Security

## Required Information

* vendor organization
* individual user
* internal sponsor
* business purpose
* target system
* required access
* access start
* access expiration
* related incident or change where applicable

## Approval Logic

```text
Vendor Access Request
        ↓
Internal Sponsor
        ↓
System Owner
        ↓
Security / Access Approval
        ↓
Provision
        ↓
Temporary Access
        ↓
Expiration
     ↙       ↘
 Disable    Approved Extension
```

## Control Requirements

* named internal sponsor
* defined business purpose
* scoped access
* defined expiration
* no self-approval
* extension requires authorization
* access activity retained where applicable

## Target

Target completion is based on the requested access window.

Requests requiring immediate access should use a defined urgent-access path rather than bypass normal authorization.

## Automation Opportunities

* approval routing
* expiration scheduling
* pre-expiration reminder
* expiration action
* extension workflow
* overdue-disablement escalation

## Closure Criteria

* access removed or confirmed expired
* vendor activity completed
* associated service record updated
* extension history retained where applicable

Related design:

* [Governance and Controls](../06%20Governance%20and%20Controls/governance%20model.md)
* [Automation Opportunities](../07%20Automation%20and%20AI/automation%20opportunities.md)

---

# 13. Catalog Approval Model

Approval complexity is grouped into three levels.

| Level | Description                       | Example                      |
| ----- | --------------------------------- | ---------------------------- |
| A0    | No manual approval required       | Standard approved peripheral |
| A1    | Single business approval          | Shared mailbox               |
| A2    | Controlled / multi-party approval | Privileged or vendor access  |

This keeps approval design reusable across catalog items.

The exact approver is determined through:

* request type
* service ownership
* requester relationship
* privilege level
* financial threshold
* risk

Detailed approval control will be maintained in:

[RBAC and Approval Controls](../06%20Governance%20and%20Controls/rbac%20and%20approval%20controls.md)

---

# 14. Catalog Fulfillment Pattern

Most catalog items follow a common fulfillment structure.

```text
Request
   ↓
Validate
   ↓
Approval Required?
 ↙             ↘
No              Yes
│                ↓
│             Approve?
│             ↙      ↘
│           Yes       No
│            │         ↓
└────────────┤      Rejected
             ↓
         Fulfillment
             ↓
          Validate
             ↓
          Complete
```

Individual catalog items may add specialized tasks without abandoning the common model.

---

# 15. Fulfillment Tasks

A service request may create one or more fulfillment tasks.

Example:

```text
New Laptop Request
        ↓
Approved Request
        ↓
 ┌──────┼────────┐
 ↓      ↓        ↓
Prepare Asset   Identity /
Device Record   Access Setup
 └──────┼────────┘
        ↓
     Delivery
        ↓
   User Validation
        ↓
      Complete
```

The parent request remains responsible for the user-facing outcome.

Individual teams may own fulfillment tasks without making the requester track several separate records.

---

# 16. Catalog Data Relationships

Catalog transactions should connect to relevant operational records.

```text
Requester
    ↓
Service Request
    ↓
Catalog Item
    ↓
Service
    ↓
Fulfillment Group
```

Additional relationships may include:

```text
Service Request
├── Approval
├── Asset
├── CI
├── Vendor
├── Knowledge
└── Fulfillment Tasks
```

Detailed relationships are maintained in:

[Service Management Data Model](../05%20Data%20and%20Configuration%20Model/service%20management%20data%20model.md)

---

# 17. Catalog Automation Decision

Automation should be applied where the required decision is:

* repeatable
* based on reliable data
* sufficiently low risk
* recoverable when it fails

Example:

```text
Standard Software Request
          ↓
Approved Software?
          ↓
License Available?
          ↓
Eligible Managed Device?
          ↓
Automatic Deployment
```

By comparison:

```text
Privileged Access
        ↓
AI / Automation Suggestion
        ↓
Human Authorization
        ↓
Provision
```

The second process may automate routing and notification.

It should not automate the authorization decision away.

---

# 18. Catalog Metrics

Catalog performance should be measured using a small number of useful indicators.

| Metric                    | Purpose                                    |
| ------------------------- | ------------------------------------------ |
| Request Volume            | Understand service demand                  |
| Fulfillment Time          | Measure delivery performance               |
| SLA Compliance            | Measure service expectation                |
| Approval Cycle Time       | Identify approval bottlenecks              |
| Reassignment Rate         | Identify routing problems                  |
| Rejection Rate            | Identify inappropriate or unclear requests |
| Automation Rate           | Identify repeatable work being automated   |
| Automation Exception Rate | Identify unstable automated workflow       |
| CSAT                      | Measure user experience                    |
| Catalog Abandonment       | Identify confusing request design          |

Detailed metric definitions will be maintained in:

[Performance Framework](../11%20Metrics%20and%20Optimization/performance%20framework.md)

---

# 19. Catalog Governance

A catalog item should have an owner throughout its lifecycle.

Catalog governance should include periodic review of:

* request volume
* required fields
* approval requirements
* fulfillment ownership
* SLA performance
* user feedback
* automation
* knowledge links
* continued business need

A catalog item should be modified or retired when it no longer represents the way the service is actually delivered.

The catalog should not become an archive of every request form the organization has ever created.

---

# 20. Catalog Publication Gate

Before a catalog item is published, the following questions must be answered:

| Gate                                | Required |
| ----------------------------------- | -------- |
| User-facing need is clear           | Yes      |
| Service owner identified            | Yes      |
| Fulfillment group identified        | Yes      |
| Required intake information defined | Yes      |
| Approval rule defined               | Yes      |
| SLA / target defined                | Yes      |
| Closure criteria defined            | Yes      |
| Required RBAC defined               | Yes      |
| Reporting fields defined            | Yes      |
| Test case defined                   | Yes      |

If ownership, approval, or fulfillment is still being debated, the catalog item is not ready for production.

A clean form does not fix an unresolved service process.

---

# 21. Initial Catalog Scope

The initial implementation intentionally limits catalog scope.

The first production catalog should favor:

* high-volume requests
* repeatable fulfillment
* well-understood ownership
* clear approval rules
* measurable service value

Lower-volume or poorly understood requests may continue through generalized intake until their process is mature enough to become a dedicated catalog item.

This avoids building dozens of forms before the organization knows whether it needs them.

---

# 22. Catalog Maturity Path

The service catalog can mature in stages.

```text
Stage 1
Core high-volume requests
        ↓
Stage 2
Broader service coverage
        ↓
Stage 3
Workflow automation
        ↓
Stage 4
Integrated fulfillment
        ↓
Stage 5
Usage-driven optimization
```

The organization should expand the catalog based on demonstrated service demand rather than a goal of maximum catalog size.

---

# 23. Service Catalog Conclusion

The service catalog gives users a cleaner front door into the service organization.

The larger value is behind that front door.

Each mature catalog item connects a user need to:

**Service → Ownership → Data → Approval → Fulfillment → SLA → Closure → Measurement**

That structure makes requests easier to fulfill, easier to govern, and easier to improve.

The catalog should grow as those processes become stable.

It should not grow simply because adding another form is easy.

**Next:** [Priority and SLA Model](./priority%20and%20sla%20model.md)
