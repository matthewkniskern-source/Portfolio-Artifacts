# Privacy and Data Governance

## 1. Purpose

This section defines practical privacy and data-governance considerations for the One-Punch Anime Emporium future-state digital retail environment.

The goal is to establish clear expectations for:

* what customer and operational data is collected;
* why that data is needed;
* who may access it;
* how long it should be retained;
* when it should be removed or anonymized;
* how third-party providers may use it.

This section is not a formal legal-compliance analysis.

---

# 2. Data Collected

The proposed solution may collect or maintain the following information.

## Customer Data

* name;
* email address;
* phone number;
* shipping address;
* billing address where required;
* account information;
* order history;
* special-order history;
* customer-service interactions.

## Operational Data

* product information;
* inventory quantities;
* store information;
* supplier information;
* employee role assignments;
* order status;
* fulfillment status;
* payment references;
* administrative activity.

The system should avoid collecting information that is not required to support a defined business function.

---

# 3. Data Minimization

Customer information should be limited to what is reasonably necessary for the interaction.

Examples:

| Business Function        | Data Normally Required                                     |
| ------------------------ | ---------------------------------------------------------- |
| General Product Browsing | No customer identification required                        |
| Contact Inquiry          | Name, contact method, inquiry                              |
| Special Order            | Name, contact method, requested merchandise                |
| Guest Checkout           | Contact and fulfillment information                        |
| Customer Account         | Identity, contact information, authentication relationship |
| Order Fulfillment        | Customer, order, address or pickup information             |
| Refund                   | Order and payment reference information                    |

Optional information should not be made mandatory without a business reason.

---

# 4. Purpose Limitation

Data collected for one business purpose should not automatically be used for unrelated purposes.

Examples:

* an email address collected for order confirmation should not automatically be treated as marketing consent;
* special-order information should be used to manage the request rather than create unrelated customer profiles;
* supplier contact information should remain operational rather than customer-facing;
* payment references should be used for transaction management and reconciliation.

Where new uses are introduced, the business should review whether additional notice or customer choice is appropriate.

---

# 5. Access to Customer Information

Employee access should be limited according to business responsibility.

| Role                     | Customer Data Access                           |
| ------------------------ | ---------------------------------------------- |
| Sales Associate          | Limited information needed to assist customer  |
| Store Manager            | Store-related customer and order information   |
| Inventory Manager        | Normally little or no customer information     |
| E Commerce Administrator | Order and digital customer-service information |
| System Administrator     | Technical access only where necessary          |
| Auditor / Reviewer       | Read-only access where required for review     |

Access should not be granted simply because the information exists in the system.

The RBAC model is maintained in the Security and Access Control section.

---

# 6. Customer Accounts

If customer accounts are implemented, customers should be able to access only information associated with their own account.

Examples include:

* profile information;
* saved addresses where supported;
* order history;
* order status;
* special-order history where appropriate.

The system should prevent one customer from accessing another customer's information through account manipulation, URL modification, or other unauthorized methods.

---

# 7. Retention

Retention should be based on legitimate operational and business needs.

Different data types may require different retention periods.

Examples include:

| Data Type                   | Retention Consideration                                          |
| --------------------------- | ---------------------------------------------------------------- |
| Active Customer Account     | While account remains active and business need exists            |
| Completed Orders            | Customer service, accounting, dispute, and business-record needs |
| Special Order Requests      | Until request is completed plus defined operational period       |
| Failed / Abandoned Requests | Shorter period where no continued business need exists           |
| Payment References          | Reconciliation, refund, or dispute requirements                  |
| Employee Access Records     | Access governance and audit requirements                         |
| Security Logs               | Troubleshooting, monitoring, and incident-review requirements    |

Specific retention periods should be defined before production deployment.

The project does not assign legal retention periods where those requirements have not been formally determined.

---

# 8. Deletion and Deactivation

Deletion should be handled according to the nature of the record.

Examples:

* unused customer accounts may be deactivated or removed according to defined policy;
* historical orders should not be deleted simply because an account is closed;
* customer information may be anonymized where the business no longer requires direct identification;
* former employee accounts should be disabled promptly;
* obsolete supplier relationships should be deactivated rather than used for new transactions.

Deletion should not break required historical or referential relationships.

---

# 9. Third-Party Providers

The future-state environment may rely on third parties such as:

* hosting providers;
* payment processors;
* email or notification services;
* analytics providers;
* identity services.

Only information required to perform the service should be transferred.

Third-party use should be reviewed for:

* what data is shared;
* why it is shared;
* how long it is retained;
* where responsibility for protection resides;
* how incidents are communicated;
* how access is terminated when the service relationship ends.

Payment-card data should remain with the payment provider whenever possible.

---

# 10. Privacy Notice

A production website should provide customers with an understandable privacy notice.

The notice should describe, at an appropriate level:

* what information is collected;
* why it is collected;
* how it is used;
* whether it is shared with service providers;
* how customers may contact the business regarding their information.

The notice should reflect actual system behavior rather than generic language copied from another organization.

---

# 11. Logging and Analytics

Logs and analytics should collect only what is needed for operational or security purposes.

The system should avoid unnecessary collection of:

* full customer addresses;
* passwords;
* authentication secrets;
* raw payment information;
* sensitive form contents;
* unnecessary customer identifiers.

Where aggregate metrics are sufficient, individually identifiable data should not be collected solely for reporting convenience.

---

# 12. Employee Handling of Customer Data

Technical controls do not replace basic operational discipline.

Employees with access to customer data should:

* use it only for assigned business tasks;
* avoid copying customer information into informal notes or personal systems;
* avoid sharing customer information through unauthorized channels;
* close or lock administrative sessions when unattended;
* report suspected exposure or misuse.

Higher-risk access should be limited and reviewable.

---

# 13. Data Accuracy

Customer and operational decisions depend on reasonably accurate information.

The business should provide mechanisms to correct information such as:

* customer contact details;
* store information;
* inventory discrepancies;
* order status;
* supplier information.

Corrections should be made through authorized processes rather than direct uncontrolled changes to production records.

---

# 14. Breach and Exposure Considerations

If customer or operational information is suspected to have been exposed, the business should be able to determine:

* what system was affected;
* what data may have been involved;
* which customers or employees may be affected;
* whether third-party providers are involved;
* what access should be disabled or changed;
* what records are available for investigation.

Incident-response and notification obligations would depend on the actual event and applicable requirements.

This case study does not attempt to provide formal legal breach-notification analysis.

---

# 15. Data Governance Responsibilities

For a small retailer, governance does not require a large dedicated compliance organization.

Responsibilities may be assigned across existing business roles.

| Responsibility         | Likely Owner                                     |
| ---------------------- | ------------------------------------------------ |
| Product Data Quality   | E Commerce / Product Administration              |
| Inventory Accuracy     | Inventory / Store Management                     |
| Customer Data Access   | Business Management / System Administration      |
| Role Administration    | System Administrator                             |
| Retention Decisions    | Business Management                              |
| Payment Data Handling  | E Commerce / Payment Provider Relationship Owner |
| Security Logging       | System Administration                            |
| Privacy Notice Content | Business Management with appropriate review      |

Ownership should be clear even where one employee performs multiple responsibilities.

---

# 16. Academic Implementation Boundary

The academic website may use mock or demonstration customer information.

Real customer information should not be required to demonstrate:

* checkout flow;
* account concepts;
* special-order submissions;
* contact forms;
* order confirmation.

Where forms are publicly hosted for demonstration, test data should be used whenever practical.

Production privacy controls, retention rules, customer account management, and formal third-party agreements remain future-state considerations unless specifically implemented.

---

# 17. Governance Outcome

The proposed approach is based on a simple principle:

> Collect what the business needs, use it for the reason it was collected, restrict access, retain it only as long as necessary, and avoid exposing it without a legitimate purpose.

For this project, privacy and data governance are treated as operating requirements rather than as documentation added after the system is designed.

