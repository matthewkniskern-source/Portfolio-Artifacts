# Threat Model and Risk Analysis

## 1. Purpose

This section identifies realistic security risks affecting the One-Punch Anime Emporium future-state digital retail environment.

The goal is not to simulate a penetration test or produce a formal enterprise risk assessment.

The objective is to identify:

* important assets;
* plausible threats;
* likely weaknesses;
* business impact;
* practical mitigating controls;
* remaining residual risk.

The analysis is scaled to a small multi-location retailer and focuses on risks that would materially affect customers, transactions, inventory, or business operations.

---

# 2. Risk Method

Risks are evaluated using a simple qualitative scale.

## Likelihood

| Rating | Meaning                                                   |
| ------ | --------------------------------------------------------- |
| Low    | Unlikely under normal operating conditions                |
| Medium | Plausible and should reasonably be anticipated            |
| High   | Common, attractive, or likely without additional controls |

## Impact

| Rating | Meaning                                                              |
| ------ | -------------------------------------------------------------------- |
| Low    | Limited operational or customer effect                               |
| Medium | Noticeable business disruption or limited data exposure              |
| High   | Significant financial, customer, operational, or reputational impact |

## Residual Risk

Residual risk represents the expected risk remaining after recommended controls are applied.

The ratings are directional rather than mathematical.

---

# 3. Primary Assets

The environment contains several assets requiring protection.

| Asset                   | Why It Matters                                                       |
| ----------------------- | -------------------------------------------------------------------- |
| Customer Accounts       | May expose customer identity, order history, and contact information |
| Customer Data           | Supports fulfillment and customer service                            |
| Product Catalog         | Drives customer discovery and pricing                                |
| Inventory Records       | Directly affect availability and fulfillment decisions               |
| Orders                  | Represent customer purchases and business revenue                    |
| Payment References      | Support transaction reconciliation and refunds                       |
| Administrative Accounts | Provide elevated access to business functions                        |
| Supplier Data           | Supports sourcing and special orders                                 |
| Application Source      | Controls website and business logic                                  |
| Logs and Backups        | Support recovery, troubleshooting, and investigation                 |
| Website Availability    | Supports customer access and online business activity                |

---

# 4. Risk Register

| ID   | Asset                          | Threat / Scenario                   | Vulnerability                                           | Likelihood | Impact     | Mitigating Controls                                                                                             | Residual Risk |
| ---- | ------------------------------ | ----------------------------------- | ------------------------------------------------------- | ---------- | ---------- | --------------------------------------------------------------------------------------------------------------- | ------------- |
| R-01 | Customer / Admin Accounts      | Credential theft                    | Weak passwords, credential reuse, phishing              | High       | High       | MFA for privileged users, secure password handling, login monitoring, account lockout/rate controls             | Medium        |
| R-02 | Customer Accounts              | Account takeover                    | Stolen credentials or session data                      | Medium     | High       | Secure sessions, authentication controls, reauthentication for sensitive actions, anomaly monitoring            | Medium        |
| R-03 | Application / Database         | SQL injection                       | Unsafe handling of user input                           | Medium     | High       | Parameterized queries, server-side validation, least-privileged database accounts, secure development practices | Low           |
| R-04 | Customer Browser / Application | Cross-site scripting                | Unvalidated or improperly encoded output                | Medium     | Medium     | Input validation, output encoding, appropriate browser security controls, secure development practices          | Low           |
| R-05 | Customer Orders                | Insecure direct object reference    | Authorization based only on user-supplied identifiers   | Medium     | High       | Server-side authorization on every protected object, ownership validation, access testing                       | Low           |
| R-06 | Authenticated Sessions         | Session theft                       | Weak token handling or insecure transport               | Medium     | High       | HTTPS/TLS, secure cookies, session expiration, token protection                                                 | Low           |
| R-07 | Administrative Functions       | Malicious or careless administrator | Excessive privilege or weak oversight                   | Medium     | High       | RBAC, least privilege, separation of duties, logging, periodic access review                                    | Medium        |
| R-08 | Payment Workflow               | Payment fraud                       | Stolen payment credentials or fraudulent transactions   | Medium     | High       | External payment provider, provider fraud controls, transaction review, limited retailer payment exposure       | Medium        |
| R-09 | Inventory                      | Unauthorized inventory manipulation | Excessive access or compromised staff account           | Medium     | High       | RBAC, inventory adjustment logging, approval for high-impact changes, reconciliation                            | Medium        |
| R-10 | Website Availability           | Denial of service                   | Public internet exposure and limited capacity           | Medium     | Medium     | Managed hosting, provider protections, monitoring, recovery procedures                                          | Medium        |
| R-11 | Customer / Business Data       | Third-party compromise              | Vendor breach or insecure integration                   | Medium     | High       | Vendor review, data minimization, limited integrations, incident escalation requirements                        | Medium        |
| R-12 | Customer Data                  | Accidental data leakage             | Misconfigured permissions, logs, exports, or storage    | Medium     | High       | Access control, log restrictions, data minimization, configuration review                                       | Medium        |
| R-13 | Application / Data             | Backup failure                      | Missing, corrupt, inaccessible, or untested backups     | Medium     | High       | Scheduled backups, protected copies, restoration testing, recovery procedures                                   | Low-Medium    |
| R-14 | Product Pricing                | Unauthorized price modification     | Excessive administrative access                         | Low-Medium | High       | Restricted catalog administration, change logging, review of significant changes                                | Low           |
| R-15 | Special Orders                 | Fraudulent or abusive requests      | Public form misuse or automated submissions             | Medium     | Low-Medium | Input validation, rate limiting, staff review, anti-automation controls where justified                         | Low           |
| R-16 | Application                    | Vulnerable third-party dependency   | Outdated library or unsupported software                | Medium     | High       | Dependency tracking, patch management, vulnerability review, supported components                               | Medium        |
| R-17 | Administrative Accounts        | Former employee retains access      | Weak offboarding process                                | Medium     | High       | Access lifecycle, prompt account disablement, periodic access review                                            | Low           |
| R-18 | Orders / Payments              | Duplicate transaction               | Retry or integration error                              | Low-Medium | High       | Transaction identifiers, idempotent processing, reconciliation, controlled retry logic                          | Low           |
| R-19 | Inventory / Orders             | Stale inventory creates oversell    | Synchronization delay or failure                        | Medium     | Medium     | Checkout availability recheck, inventory reservation, sync monitoring, exception handling                       | Medium        |
| R-20 | Source Repository              | Unauthorized source changes         | Compromised contributor account or weak branch controls | Low-Medium | Medium     | MFA, controlled repository permissions, change review, version history                                          | Low           |

---

# 5. Credential Theft and Account Takeover

Credential-based attacks are among the most realistic threats to the environment.

Customers may reuse passwords across services, while privileged employee accounts provide access to higher-impact functions.

Potential outcomes include:

* exposure of customer order history;
* unauthorized order changes;
* inventory manipulation;
* fraudulent refunds;
* administrative configuration changes.

Primary controls include:

* secure authentication;
* MFA for privileged accounts;
* limited administrative access;
* secure session handling;
* authentication-event logging;
* prompt disablement of inactive accounts.

Residual risk remains because authentication controls cannot completely prevent credential theft or successful social engineering.

---

# 6. Application Injection and Input Attacks

Customer-facing applications process multiple types of untrusted input, including:

* search queries;
* account information;
* checkout fields;
* contact forms;
* special-order descriptions;
* administrative data entry.

Improper handling can create vulnerabilities such as:

* SQL injection;
* cross-site scripting;
* malformed requests;
* data-integrity errors.

Recommended controls include:

* server-side validation;
* parameterized database operations;
* output encoding;
* controlled error handling;
* dependency maintenance;
* security-oriented testing.

Client-side validation alone is insufficient for a production system.

---

# 7. Authorization Failure

Authentication determines who the user is.

Authorization determines what the user is permitted to access.

A customer who changes an order identifier in a URL or request must not gain access to another customer's order simply because the identifier exists.

Likewise, staff should not gain higher privileges by manipulating request parameters or navigating directly to administrative functions.

Authorization decisions should be enforced server-side for each protected resource and action.

---

# 8. Administrative Misuse

Administrative accounts present greater potential impact than ordinary customer accounts.

Misuse may be:

* malicious;
* accidental;
* caused by a compromised privileged account.

High-impact actions include:

* inventory adjustments;
* price changes;
* refunds;
* role assignments;
* customer-data access;
* security configuration changes.

Controls should include:

* defined roles;
* least privilege;
* separation of duties;
* MFA;
* logging;
* access review.

A small business may not be able to separate every duty across different employees, so review and logging become more important where responsibilities overlap.

---

# 9. Inventory Manipulation

Inventory accuracy directly affects the customer experience and business operation.

Incorrect or malicious inventory changes may result in:

* customers traveling to stores for unavailable products;
* overselling;
* products incorrectly appearing unavailable;
* fulfillment failures;
* distorted management reporting.

Inventory changes should be limited to authorized roles and significant adjustments should be reviewable.

Checkout should also revalidate inventory rather than assuming previously displayed availability remains accurate indefinitely.

---

# 10. Payment Risk

The retailer reduces direct payment risk by using an external payment provider.

However, risk remains around:

* fraudulent purchases;
* compromised customer payment credentials;
* duplicate payment activity;
* refund abuse;
* false payment-state handling;
* payment-provider compromise or outage.

Controls include:

* hosted or tokenized payment processing;
* provider fraud capabilities;
* payment/order reconciliation;
* limited refund permissions;
* separation of payment and order state;
* logging of refund and transaction actions.

Payment architecture is defined in detail in the Payment Architecture and PCI Scope section.

---

# 11. Third-Party Risk

The future-state system may depend on providers for:

* hosting;
* payments;
* identity;
* email;
* analytics.

A compromise or outage affecting one of these services can affect the retailer even when the retailer's own application is functioning correctly.

Risk reduction includes:

* limiting the number of unnecessary integrations;
* sharing only required data;
* selecting established providers;
* understanding service dependencies;
* maintaining escalation contacts;
* considering fallback procedures for critical services.

Third-party use transfers some operational responsibility but does not transfer all business risk.

---

# 12. Availability Risk

Public e-commerce capability creates dependency on website and provider availability.

Potential causes of disruption include:

* denial-of-service activity;
* hosting outages;
* deployment errors;
* payment-provider outages;
* DNS failures;
* application defects.

For a small retailer, the goal is reasonable resilience rather than enterprise-scale redundancy.

Recommended controls include:

* managed hosting;
* monitoring;
* backups;
* rollback capability;
* outage communication;
* manual fallback where practical.

Detailed recovery considerations are addressed in Business Continuity and Operations.

---

# 13. Backup Risk

A backup that cannot be restored provides little operational value.

Relevant risks include:

* backups never occurring;
* backups being overwritten;
* backup corruption;
* unauthorized access;
* backups existing in the same failure domain as the primary system;
* restoration procedures never being tested.

Production backup design should therefore include both backup creation and periodic recovery validation.

---

# 14. OWASP Alignment

Several risks in this project align with common web-application security themes identified by OWASP, including:

* broken access control;
* injection;
* authentication failures;
* security misconfiguration;
* vulnerable components;
* insufficient logging and monitoring.

OWASP concepts are used as practical design guidance.

This project does not claim to perform a formal OWASP assessment or penetration test.

---

# 15. Highest-Priority Risks

The risks receiving the greatest attention in a production implementation should be:

1. unauthorized administrative access;
2. customer account takeover;
3. customer-to-customer data exposure;
4. payment and refund fraud;
5. unauthorized inventory manipulation;
6. vulnerable application components;
7. third-party compromise;
8. loss of recoverable business data.

These risks combine relatively plausible attack paths with meaningful business consequences.

---

# 16. Risk Treatment Approach

Risks may be handled through one or more of the following approaches.

| Treatment | Application                                                                    |
| --------- | ------------------------------------------------------------------------------ |
| Mitigate  | Implement controls to reduce likelihood or impact                              |
| Transfer  | Use external providers for specialized capabilities such as payment processing |
| Avoid     | Do not implement unnecessary high-risk capabilities                            |
| Accept    | Retain lower-level risk where mitigation cost is disproportionate              |

For example, the decision not to process raw cardholder data directly is both a risk-avoidance and scope-reduction decision.

---

# 17. Academic Implementation Boundary

The academic website provides only limited exposure to the future-state threat environment.

Applicable demonstration concerns may include:

* unsafe form input;
* cross-site scripting;
* insecure external resources;
* repository compromise;
* accidental exposure of test information;
* insecure hosting configuration.

Risks involving:

* real customer authentication;
* production databases;
* live payment processing;
* administrative RBAC;
* production inventory synchronization;

remain future-state risks unless those functions are actually implemented.

---

# 18. Risk Analysis Outcome

The proposed digital retail environment introduces new risks because the business is expanding beyond physical-store-only operation.

That does not mean the transformation should be avoided.

It means the new digital capabilities should be introduced with controls appropriate to the value of the data and functions being exposed.

The security objective is therefore not elimination of risk.

It is to keep risk visible, assign practical controls, and avoid creating unnecessary exposure through poor design.

