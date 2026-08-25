# Security and Access Control

## 1. Purpose

This section defines the proposed security and access-control model for the One-Punch Anime Emporium future-state digital retail environment.

The goal is to protect customer, employee, inventory, order, and transaction-related information without imposing controls that are disproportionate to the scale of the business.

The model focuses on:

* authentication;
* role-based access control;
* least privilege;
* separation of duties;
* session protection;
* administrative access;
* application security;
* logging and monitoring;
* vulnerability management;
* backup and recovery;
* change control.

The academic website may demonstrate selected front-end controls, but production identity, authorization, and administrative security remain future-state capabilities unless explicitly implemented.

---

# 2. Security Design Principles

## Least Privilege

Users should receive only the access required to perform their assigned responsibilities.

Access should not be granted simply because a user works for the company or has access to another business system.

## Role-Based Access Control

Permissions should be assigned through defined roles rather than maintained individually for each employee wherever practical.

This supports:

* consistent access;
* easier onboarding;
* easier removal of access;
* reviewable responsibilities;
* reduced permission drift.

## Separation of Duties

High-impact activities should not be concentrated unnecessarily under one account or role.

Examples include:

* refund approval;
* user and role administration;
* inventory adjustments;
* security configuration;
* audit review.

## Secure by Default

New users, accounts, integrations, and administrative functions should begin with limited access until additional permissions are explicitly approved.

---

# 3. Proposed Roles

The future-state system uses the following logical roles.

| Role                         | Primary Responsibility                                             |
| ---------------------------- | ------------------------------------------------------------------ |
| Customer                     | Browse, purchase, submit requests, and access own information      |
| Sales Associate              | Support customers and perform limited store operations             |
| Store Manager                | Manage store-level operations and approve selected actions         |
| Inventory Manager            | Maintain and reconcile product inventory                           |
| E Commerce Administrator     | Manage online products, orders, and digital operations             |
| System Administrator         | Maintain technical configuration and system access                 |
| Auditor / Read-Only Reviewer | Review records, controls, and activity without modification rights |

These roles represent access groupings, not job titles that must exist exactly as written.

A single employee may hold more than one role where business responsibilities justify it.

---

# 4. RBAC Matrix

Legend:

* **R** — Read
* **C** — Create
* **U** — Update
* **A** — Approve / Authorize
* **D** — Delete or Deactivate
* **—** — No routine access

| Function                 |  Customer | Sales Associate | Store Manager | Inventory Manager | E Commerce Admin | System Admin | Auditor |
| ------------------------ | --------: | --------------: | ------------: | ----------------: | ---------------: | -----------: | ------: |
| Public Product Catalog   |         R |               R |             R |                 R |            R/C/U |            R |       R |
| Own Customer Profile     |       R/U |               — |             — |                 — |                — |            — |       — |
| Other Customer Profiles  |         — |       Limited R |     Limited R |                 — |        Limited R |            — |       R |
| Own Orders               |         R |               — |             — |                 — |                — |            — |       — |
| Store Orders             |         — |       Limited R |           R/U |                 — |              R/U |            — |       R |
| Order Status Update      |         — |       Limited U |             U |                 — |                U |            — |       R |
| Refund Request           |         — |               C |             C |                 — |                C |            — |       R |
| Refund Approval          |         — |               — |             A |                 — |                A |            — |       R |
| Product Information      |         R |               R |             R |                 R |              C/U |            — |       R |
| Inventory View           | Limited R |               R |             R |                 R |                R |            — |       R |
| Inventory Adjustment     |         — |       Limited C |         C/U/A |               C/U |                — |            — |       R |
| Special Order Submission |         C |               C |             C |                 — |                C |            — |       R |
| Special Order Review     |       Own |               R |           R/U |                 — |              R/U |            — |       R |
| Supplier Information     |         — |               — |             R |                 R |              R/U |            — |       R |
| Store Configuration      |         — |               — |     Limited U |                 — |                U |            — |       R |
| User Administration      |         — |               — |             — |                 — |          Limited |        C/U/D |       R |
| Role Assignment          |         — |               — |             — |                 — |                — |        C/U/D |       R |
| Technical Configuration  |         — |               — |             — |                 — |                — |        C/U/D |       R |
| Security Logs            |         — |               — |     Limited R |                 — |        Limited R |            R |       R |
| Audit Records            |         — |               — |             R |                 — |                R |            R |       R |

"Limited" access should be constrained by business context, such as assigned store, related order, or job responsibility.

---

# 5. Role Boundaries

## Customer

Customers should be able to:

* browse public products;
* manage their own account where implemented;
* view their own orders;
* submit special-order requests;
* interact with their own cart and checkout information.

Customers must not be able to:

* view another customer's information;
* access staff functions;
* modify inventory;
* modify product information;
* access internal supplier or audit data.

---

## Sales Associate

Sales Associates should receive limited operational access appropriate to front-line customer support.

Typical access may include:

* product information;
* store-level inventory visibility;
* limited order lookup;
* special-order intake;
* customer assistance.

They should not routinely administer users, roles, system configuration, or broad customer datasets.

---

## Store Manager

Store Managers may require broader access within their assigned location.

Typical responsibilities may include:

* store order management;
* inventory adjustment approval;
* customer-service escalation;
* refund approval within defined limits;
* store-level reporting.

Store Manager access should remain constrained where centralized functions are not part of the role.

---

## Inventory Manager

Inventory Managers require operational access to:

* inventory records;
* product availability;
* stock adjustments;
* reconciliation.

They do not require unrestricted access to customer accounts, payment functions, or system administration.

---

## E Commerce Administrator

The E Commerce Administrator manages the digital retail channel.

Typical access may include:

* product catalog administration;
* online orders;
* special-order administration;
* store content;
* reporting;
* limited transaction review.

This role should not automatically receive infrastructure-level administrative privileges.

---

## System Administrator

The System Administrator maintains the technical environment.

Typical access may include:

* system configuration;
* user provisioning;
* role assignment;
* technical logging;
* deployment configuration;
* security configuration.

System administration does not inherently require authority to approve refunds, modify business transactions, or perform routine customer-service functions.

---

## Auditor / Read-Only Reviewer

This role exists to support independent review.

Access should be:

* read-only;
* sufficient to review controls, records, access assignments, and activity;
* restricted from operational modification.

---

# 6. Authentication

Protected customer and administrative functions should require authentication.

The production design should use established platform or identity-service authentication mechanisms rather than custom password handling where practical.

Minimum expectations include:

* passwords must not be stored in plaintext;
* password storage should use an appropriate modern password-hashing implementation;
* login traffic must use encrypted transport;
* authentication failures should not reveal unnecessary account information;
* inactive accounts should not remain indefinitely usable.

Administrative and privileged accounts should use stronger protections than ordinary customer accounts.

---

# 7. Multifactor Authentication

MFA should be required for privileged or administrative users in the proposed production environment.

At minimum, this should include:

* System Administrators;
* E Commerce Administrators;
* other roles capable of high-impact administrative actions.

MFA may also be appropriate for Store Managers depending on the selected platform and risk.

Customer MFA may be offered or required later where the account model warrants it.

The academic website does not need to implement production MFA.

---

# 8. Session Management

Authenticated sessions should be managed so that possession of an old or stolen session does not provide indefinite access.

Recommended controls include:

* session expiration after appropriate inactivity;
* logout capability;
* invalidation after password or security changes where supported;
* protection of session tokens in transit;
* secure cookie settings where applicable;
* avoiding sensitive values in URLs;
* reauthentication for selected high-risk actions where appropriate.

Administrative sessions should generally use stricter controls than ordinary public browsing.

---

# 9. Input Validation

User-controlled input should be treated as untrusted.

Relevant inputs include:

* product search;
* customer contact forms;
* special-order requests;
* checkout fields;
* account information;
* administrative data-entry fields;
* URL parameters.

The production application should:

* validate input against expected type and length;
* reject invalid values;
* safely handle unexpected characters;
* use appropriate output encoding;
* use parameterized database interaction;
* avoid exposing internal errors to customers.

Front-end validation may improve usability but should not be treated as a substitute for server-side validation in a production system.

---

# 10. Secure Transport

Production customer and administrative traffic should use TLS.

The design should:

* redirect insecure HTTP requests to HTTPS where applicable;
* use valid certificates;
* avoid mixed secure and insecure content;
* protect administrative interfaces using the same or stronger transport controls.

The academic hosted website should use HTTPS where supported by the selected hosting platform.

---

# 11. Administrative Access

Administrative interfaces should not rely only on obscurity or unpublished URLs for protection.

Controls should include:

* authenticated access;
* role-based authorization;
* MFA for privileged roles;
* least privilege;
* logging of high-impact actions;
* removal of access when no longer required.

Administrative functions should be logically separated from normal customer activity.

---

# 12. Separation of Duties

Selected activities warrant additional separation.

| Activity                        | Recommended Separation                              |
| ------------------------------- | --------------------------------------------------- |
| Refund Request                  | May be initiated by support or operational staff    |
| Refund Approval                 | Store Manager or E Commerce Administrator           |
| Role Assignment                 | System Administrator                                |
| Audit Review                    | Auditor / Read-Only Reviewer                        |
| Inventory Adjustment            | Inventory role                                      |
| High-Impact Adjustment Approval | Store Manager or authorized reviewer                |
| Technical Configuration         | System Administrator                                |
| Routine Business Orders         | Operational staff, not infrastructure administrator |

For a small retailer, complete separation may not always be possible.

Where one employee holds multiple responsibilities, higher-risk actions should still be logged and periodically reviewed.

---

# 13. Zero Trust and RBAC

RBAC and Zero Trust are related but not interchangeable.

### RBAC

RBAC answers:

> What functions is this user permitted to perform based on assigned role?

### Zero Trust

Zero Trust principles consider broader questions such as:

* who is requesting access;
* what resource is being accessed;
* whether the user and device can be trusted sufficiently for that request;
* whether access remains appropriate throughout the session.

For this project, RBAC is the primary access-control mechanism.

Zero Trust concepts may inform stronger production controls, but the artifact does not claim implementation of a full Zero Trust architecture.

---

# 14. Logging and Monitoring

Security-relevant events should generate sufficient records to support troubleshooting, review, and incident investigation.

Examples include:

* successful and failed administrative authentication;
* role changes;
* account creation or deactivation;
* significant inventory adjustments;
* refund actions;
* administrative product changes;
* access-control failures;
* system errors affecting transactions.

Logs should avoid unnecessary collection of sensitive information.

The system should not record:

* passwords;
* payment-card data;
* CVV/CVC;
* authentication secrets;
* unnecessary customer data.

Log access should itself be restricted.

---

# 15. Vulnerability and Patch Management

Production components should be maintained throughout their operating life.

The process should include:

* identification of software and dependencies;
* review of relevant security updates;
* timely patching based on risk;
* replacement of unsupported software;
* review of third-party libraries;
* remediation of identified vulnerabilities;
* validation following significant security updates.

The exact process should remain appropriate to the scale of the retailer.

---

# 16. Backup and Recovery Security

Backups should receive protections comparable to the data they contain.

Recommended controls include:

* restricted backup access;
* protected storage;
* defined retention;
* recovery testing;
* separation from routine application modification where practical.

Backup availability is addressed further in the Business Continuity and Operations section.

---

# 17. Change Control

Changes to production functionality or security-sensitive configuration should follow a basic controlled process.

At minimum:

```text id="6wvsou"
Change Requested
      ↓
Impact Reviewed
      ↓
Approved
      ↓
Tested
      ↓
Deployed
      ↓
Validated
      ↓
Closed or Rolled Back
```

Higher-risk changes include:

* authentication changes;
* access-role changes;
* payment integration changes;
* database changes;
* security configuration;
* customer-data handling changes.

Minor content changes do not require the same level of control as security-sensitive application changes.

---

# 18. Access Lifecycle

Employee access should follow a defined lifecycle.

```text id="0clp5h"
Business Need Identified
        ↓
Access Approved
        ↓
Role Assigned
        ↓
User Performs Duties
        ↓
Periodic Review
        ↓
Role Changed or Removed
        ↓
Access Disabled at Separation
```

Access should be reviewed when:

* employees change roles;
* store responsibilities change;
* privileged permissions are added;
* employment ends;
* access is no longer required.

Inactive accounts should not remain available indefinitely.

---

# 19. Security Review Priorities

For a production implementation, the highest-priority protections are:

1. preventing unauthorized administrative access;
2. preventing customer-to-customer data exposure;
3. preventing unauthorized inventory or order modification;
4. protecting authentication and session information;
5. preventing direct handling of raw payment-card data;
6. validating untrusted input;
7. protecting customer information;
8. maintaining recoverable systems and data;
9. maintaining usable security logs;
10. controlling privileged access throughout the employee lifecycle.

---

# 20. Academic Implementation Boundary

The academic website may directly demonstrate:

* HTTPS through the hosting platform;
* client-side input validation;
* basic session-like cart behavior;
* constrained forms;
* avoidance of real payment data;
* safe handling of mock customer information.

The following remain proposed production controls unless explicitly implemented:

* authenticated customer accounts;
* administrative authentication;
* MFA;
* production RBAC enforcement;
* centralized security logging;
* production vulnerability management;
* formal access reviews;
* enterprise backup controls;
* production change-management enforcement.

These capabilities should not be presented as implemented solely because they are documented in this design.

---

# 21. Security Model Outcome

The proposed model separates access according to business responsibility while keeping customer, operational, administrative, and technical privileges distinct.

The intended access structure is:

```text id="0j8vde"
Customer
   ↓
Own Data and Retail Functions

Operational Staff
   ↓
Store / Inventory / Order Functions

Administrative Staff
   ↓
E Commerce and Business Administration

System Administrator
   ↓
Technical Administration

Auditor
   ↓
Read Only Review
```

The objective is not to maximize the number of controls.

It is to ensure that access is deliberate, reviewable, limited to business need, and appropriate to the risk of the function being performed.

