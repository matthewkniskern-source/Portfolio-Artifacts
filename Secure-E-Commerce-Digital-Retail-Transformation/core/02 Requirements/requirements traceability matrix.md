# Requirements Traceability Matrix

## 1. Purpose

This matrix links project requirements to the design, implementation, and validation artifacts that address them.

The matrix is intended to provide traceability without duplicating the detailed content maintained elsewhere in the repository.

Implementation status reflects what was actually built or demonstrated in the academic website versus what remains part of the future-state design.

---

## 2. Status Definitions

| Status                   | Meaning                                                                                 |
| ------------------------ | --------------------------------------------------------------------------------------- |
| Implemented              | Capability was built and demonstrated                                                   |
| Prototype / Demonstrated | Capability was represented using mock data, client-side logic, or simulated behavior    |
| Proposed                 | Capability is documented as part of the future-state design but was not implemented     |
| Control Recommendation   | Security, privacy, or governance capability recommended for a production implementation |
| Not Applicable           | Requirement is not applicable to the selected implementation approach                   |

---

## 3. Priority Definitions

| Priority | Meaning                                                                     |
| -------- | --------------------------------------------------------------------------- |
| Must     | Required for the defined implementation or essential future-state operation |
| Should   | Important but may be deferred without invalidating the solution             |
| Could    | Useful enhancement where time and resources permit                          |
| Future   | Intentionally reserved for a later maturity phase                           |

---

# 4. Business Requirements Traceability

| ID    | Requirement Summary                       | Priority | Design / Artifact                           | Implementation Status  | Validation    |
| ----- | ----------------------------------------- | -------: | ------------------------------------------- | ---------------------- | ------------- |
| BR-01 | Centralized digital product discovery     |     Must | Information Architecture / Product Catalog  | TBD                    | TC-01, TC-02  |
| BR-02 | Store-level inventory visibility          |   Should | Data Model / Inventory Design               | TBD                    | TC-03         |
| BR-03 | Online purchasing capability              |   Future | E-Commerce Workflows / Payment Architecture | Proposed               | TC-04         |
| BR-04 | Structured special-order process          |     Must | Special Order Workflow                      | TBD                    | TC-05         |
| BR-05 | Customer communication                    |   Should | Information Architecture / Workflow Design  | TBD                    | TC-06         |
| BR-06 | Multi-store digital model                 |     Must | Data Model / Store and Inventory Design     | Proposed               | TC-07         |
| BR-07 | Operational reporting                     |   Future | Metrics and Continual Improvement           | Proposed               | TC-08         |
| BR-08 | Protect business and customer information |     Must | Security / Privacy / Payment Architecture   | Control Recommendation | TC-09         |
| BR-09 | Support incremental expansion             |   Should | Future State Roadmap / Architecture         | Proposed               | Design Review |
| BR-10 | Preserve physical retail operations       |     Must | Business Case / Future State Roadmap        | Proposed               | Design Review |

---

# 5. Functional Requirements Traceability

## 5.1 Product Discovery and Store Information

| ID    | Requirement Summary               | Priority | Design / Artifact           | Implementation Status | Validation |
| ----- | --------------------------------- | -------: | --------------------------- | --------------------- | ---------- |
| FR-01 | Browse product catalog            |     Must | Product Catalog             | TBD                   | TC-10      |
| FR-02 | Search products                   |     Must | Search Function             | TBD                   | TC-11      |
| FR-03 | Filter products                   |   Should | Catalog Filtering           | TBD                   | TC-12      |
| FR-04 | Product detail view               |     Must | Product Detail Page         | TBD                   | TC-13      |
| FR-05 | Display product price             |     Must | Product Detail Page         | TBD                   | TC-14      |
| FR-06 | Identify unavailable products     |   Should | Product / Inventory Display | TBD                   | TC-15      |
| FR-07 | Display store availability        |   Should | Inventory Display           | TBD                   | TC-16      |
| FR-08 | View retail locations             |     Must | Store Locations Page        | TBD                   | TC-17      |
| FR-09 | Display store details             |     Must | Store Locations Page        | TBD                   | TC-18      |
| FR-10 | Associate inventory with location |     Must | Data Model                  | Proposed              | TC-19      |

---

## 5.2 Shopping Cart and Checkout

| ID    | Requirement Summary                       | Priority | Design / Artifact     | Implementation Status | Validation |
| ----- | ----------------------------------------- | -------: | --------------------- | --------------------- | ---------- |
| FR-11 | Add product to cart                       |     Must | Cart Workflow         | TBD                   | TC-20      |
| FR-12 | Remove product from cart                  |     Must | Cart Workflow         | TBD                   | TC-21      |
| FR-13 | Modify cart quantity                      |   Should | Cart Workflow         | TBD                   | TC-22      |
| FR-14 | Calculate cart total                      |     Must | Cart Logic            | TBD                   | TC-23      |
| FR-15 | Initiate checkout                         |     Must | Checkout Workflow     | TBD                   | TC-24      |
| FR-16 | Collect checkout information              |     Must | Checkout Form         | TBD                   | TC-25      |
| FR-17 | Validate required checkout fields         |     Must | Checkout Validation   | TBD                   | TC-26      |
| FR-18 | Transfer payment to external provider     |   Future | Payment Architecture  | Proposed              | TC-27      |
| FR-19 | Distinguish successful and failed payment |   Future | Payment Workflow      | Proposed              | TC-28      |
| FR-20 | Generate order confirmation               |     Must | Confirmation Workflow | TBD                   | TC-29      |

---

## 5.3 Special Orders

| ID    | Requirement Summary          | Priority | Design / Artifact               | Implementation Status | Validation |
| ----- | ---------------------------- | -------: | ------------------------------- | --------------------- | ---------- |
| FR-21 | Submit special-order request |     Must | Special Order Form              | TBD                   | TC-30      |
| FR-22 | Capture request information  |     Must | Special Order Form              | TBD                   | TC-31      |
| FR-23 | Staff review of request      |   Future | Special Order Workflow          | Proposed              | TC-32      |
| FR-24 | Track request status         |   Future | Special Order Workflow          | Proposed              | TC-33      |
| FR-25 | Record request outcome       |   Future | Special Order Workflow          | Proposed              | TC-34      |
| FR-26 | Communicate request outcome  |   Future | Customer Communication Workflow | Proposed              | TC-35      |

---

## 5.4 Customer Accounts

| ID    | Requirement Summary                         | Priority | Design / Artifact           | Implementation Status  | Validation |
| ----- | ------------------------------------------- | -------: | --------------------------- | ---------------------- | ---------- |
| FR-27 | Optional customer accounts                  |   Future | Customer Account Design     | Proposed               | TC-36      |
| FR-28 | Customer authentication                     |   Future | Security and Access Control | Proposed               | TC-37      |
| FR-29 | Customer views own orders                   |   Future | Customer Account Design     | Proposed               | TC-38      |
| FR-30 | Prevent access to another customer's orders |     Must | Access Control Design       | Control Recommendation | TC-39      |

---

## 5.5 Inventory and Order Administration

| ID    | Requirement Summary                    | Priority | Design / Artifact           | Implementation Status  | Validation |
| ----- | -------------------------------------- | -------: | --------------------------- | ---------------------- | ---------- |
| FR-31 | Product-store-inventory relationship   |     Must | Data Model                  | Proposed               | TC-40      |
| FR-32 | Authorized inventory updates           |   Future | Admin / RBAC Design         | Proposed               | TC-41      |
| FR-33 | Reflect inventory changes to customers |   Future | Inventory Workflow          | Proposed               | TC-42      |
| FR-34 | Prevent unauthorized inventory changes |     Must | Security and Access Control | Control Recommendation | TC-43      |
| FR-35 | Correct inventory discrepancies        |   Future | Inventory Workflow          | Proposed               | TC-44      |
| FR-36 | Staff view fulfillment orders          |   Future | Order Management Workflow   | Proposed               | TC-45      |
| FR-37 | Update order status                    |   Future | Order Management Workflow   | Proposed               | TC-46      |
| FR-38 | Identify pickup or shipping            |   Future | Order Management Workflow   | Proposed               | TC-47      |
| FR-39 | Distinguish order states               |   Future | Order Management Workflow   | Proposed               | TC-48      |
| FR-40 | Restrict order administration by role  |     Must | RBAC Design                 | Control Recommendation | TC-49      |

---

## 5.6 Product and Administrative Management

| ID    | Requirement Summary           | Priority | Design / Artifact            | Implementation Status | Validation |
| ----- | ----------------------------- | -------: | ---------------------------- | --------------------- | ---------- |
| FR-41 | Manage product information    |   Future | Admin Design                 | Proposed              | TC-50      |
| FR-42 | Manage product categories     |   Future | Admin Design                 | Proposed              | TC-51      |
| FR-43 | Manage store information      |   Future | Admin Design                 | Proposed              | TC-52      |
| FR-44 | Review special-order activity |   Future | Admin Design                 | Proposed              | TC-53      |
| FR-45 | Access operational reporting  |   Future | Metrics and Reporting Design | Proposed              | TC-54      |

---

# 6. Nonfunctional Requirements Traceability

| ID     | Requirement Summary                                      | Priority | Design / Artifact                    | Implementation Status  | Validation        |
| ------ | -------------------------------------------------------- | -------: | ------------------------------------ | ---------------------- | ----------------- |
| NFR-01 | Routine website availability                             |     Must | Hosting Design                       | TBD                    | TC-55             |
| NFR-02 | Noncritical failure should not block basic access        |   Should | Hosting / Application Design         | Proposed               | TC-56             |
| NFR-03 | Recoverable application and business data                |     Must | Continuity and Operations            | Control Recommendation | TC-57             |
| NFR-04 | Reasonable page-load performance                         |   Should | Front-End Design                     | TBD                    | TC-58             |
| NFR-05 | Responsive search and navigation                         |   Should | Front-End Design                     | TBD                    | TC-59             |
| NFR-06 | Review performance as usage grows                        |   Future | Metrics and Continual Improvement    | Proposed               | Design Review     |
| NFR-07 | Understandable navigation                                |     Must | Information Architecture             | TBD                    | TC-60             |
| NFR-08 | Consistent access to major functions                     |     Must | Information Architecture             | TBD                    | TC-61             |
| NFR-09 | Clear form validation                                    |     Must | Form Design                          | TBD                    | TC-62             |
| NFR-10 | Desktop and mobile support                               |     Must | Responsive Design                    | TBD                    | TC-63             |
| NFR-11 | Follow appropriate accessibility guidance                |     Must | Information Architecture / UI Design | TBD                    | TC-64             |
| NFR-12 | Alternative text for meaningful images                   |     Must | UI Implementation                    | TBD                    | TC-65             |
| NFR-13 | Do not rely exclusively on color                         |     Must | UI Design                            | TBD                    | TC-66             |
| NFR-14 | Support keyboard interaction where practical             |   Should | UI Design                            | TBD                    | TC-67             |
| NFR-15 | Maintainable code and content structure                  |   Should | Implementation Structure             | TBD                    | Design Review     |
| NFR-16 | Separate product, store, and inventory concepts          |     Must | Data Model                           | Proposed               | Design Review     |
| NFR-17 | Support additional stores and products                   |   Should | Data Model / Architecture            | Proposed               | Design Review     |
| NFR-18 | Maintain source and documentation in version control     |     Must | GitHub Repository                    | Implemented            | Repository Review |
| NFR-19 | Defined production backup schedule                       |   Future | Continuity and Operations            | Control Recommendation | TC-68             |
| NFR-20 | Protect backup data                                      |   Future | Continuity and Security Design       | Control Recommendation | TC-69             |
| NFR-21 | Define recovery priorities                               |   Future | Business Continuity                  | Proposed               | Design Review     |
| NFR-22 | Record important administrative and transaction activity |   Future | Logging Design                       | Control Recommendation | TC-70             |
| NFR-23 | Avoid sensitive information in logs                      |     Must | Logging / Security Design            | Control Recommendation | TC-71             |
| NFR-24 | Preserve valid business-data relationships               |     Must | Data Model                           | Proposed               | TC-72             |
| NFR-25 | Reject invalid or incomplete business records            |     Must | Data Validation Design               | TBD                    | TC-73             |

---

# 7. Security Requirements Traceability

| ID     | Requirement Summary                                 | Priority | Design / Artifact           | Implementation Status  | Validation          |
| ------ | --------------------------------------------------- | -------: | --------------------------- | ---------------------- | ------------------- |
| SEC-01 | Authenticate protected admin access                 |     Must | Security and Access Control | Proposed               | TC-74               |
| SEC-02 | MFA for privileged accounts                         |     Must | Security and Access Control | Control Recommendation | TC-75               |
| SEC-03 | Do not store plaintext passwords                    |     Must | Authentication Design       | Control Recommendation | TC-76               |
| SEC-04 | Secure password handling                            |     Must | Authentication Design       | Control Recommendation | TC-77               |
| SEC-05 | Role-based authorization                            |     Must | RBAC Matrix                 | Proposed               | TC-78               |
| SEC-06 | Least privilege                                     |     Must | RBAC Matrix                 | Control Recommendation | TC-79               |
| SEC-07 | Separate customer and staff permissions             |     Must | RBAC Matrix                 | Proposed               | TC-80               |
| SEC-08 | Protect administrative functions                    |     Must | Access Control Design       | Proposed               | TC-81               |
| SEC-09 | Secure session lifecycle                            |     Must | Security Design             | Control Recommendation | TC-82               |
| SEC-10 | Validate user-controlled input                      |     Must | Application Security Design | TBD                    | TC-83               |
| SEC-11 | Encrypt production traffic                          |     Must | Hosting / TLS Design        | Control Recommendation | TC-84               |
| SEC-12 | Vulnerability and patch management                  |     Must | Security Operations         | Control Recommendation | Design Review       |
| SEC-13 | Log security-relevant admin activity                |   Should | Logging Design              | Control Recommendation | TC-85               |
| SEC-14 | Review and revoke admin access                      |     Must | Access Governance           | Control Recommendation | Design Review       |
| SEC-15 | Do not store raw payment-card numbers               |     Must | Payment Architecture        | Proposed               | Architecture Review |
| SEC-16 | Use external hosted or tokenized payment processing |     Must | Payment Architecture        | Proposed               | Architecture Review |
| SEC-17 | Payment failure cannot appear as successful payment |     Must | Payment Workflow            | Proposed               | TC-86               |
| SEC-18 | Exclude sensitive data from logs                    |     Must | Logging Design              | Control Recommendation | TC-87               |

---

# 8. Privacy Requirements Traceability

| ID      | Requirement Summary                               | Priority | Design / Artifact                  | Implementation Status  | Validation    |
| ------- | ------------------------------------------------- | -------: | ---------------------------------- | ---------------------- | ------------- |
| PRIV-01 | Collect only required customer information        |     Must | Privacy and Data Governance        | Control Recommendation | Design Review |
| PRIV-02 | Collect data for defined purposes                 |     Must | Privacy and Data Governance        | Control Recommendation | Design Review |
| PRIV-03 | Limit employee access to customer data            |     Must | RBAC / Privacy Design              | Control Recommendation | TC-88         |
| PRIV-04 | Prevent unauthorized customer-data exposure       |     Must | Access Control Design              | Control Recommendation | TC-89         |
| PRIV-05 | Establish retention expectations                  |   Should | Data Governance                    | Proposed               | Design Review |
| PRIV-06 | Define deletion or retention handling             |   Should | Data Governance                    | Proposed               | Design Review |
| PRIV-07 | Limit data shared with third parties              |     Must | Third-Party / Payment Architecture | Control Recommendation | Design Review |
| PRIV-08 | Provide customer privacy notice                   |   Should | Privacy Design                     | Proposed               | TC-90         |
| PRIV-09 | Limit sensitive information in logs and analytics |     Must | Logging / Privacy Design           | Control Recommendation | TC-91         |
| PRIV-10 | Protect stored customer information               |     Must | Security and Access Control        | Control Recommendation | TC-92         |

---

# 9. Traceability Maintenance

This matrix should be updated as implementation and testing progress.

The primary fields expected to change are:

* priority;
* implementation status;
* linked design artifact;
* test case;
* validation result.

A requirement should not be marked **Implemented** solely because it is described in project documentation.

Implementation status should reflect observable functionality or configuration present in the project.

Where a requirement remains architectural or operational in nature, **Proposed** or **Control Recommendation** is the appropriate status.

