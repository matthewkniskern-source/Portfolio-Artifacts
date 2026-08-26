# Requirements Traceability

## Inventory and Commerce

| Business Requirement | Functional Requirement(s)         | Validation                                                         |
| -------------------- | --------------------------------- | ------------------------------------------------------------------ |
| BR-01                | FR-01, FR-60                      | Confirm Zoho mock inventory is treated as authoritative            |
| BR-02                | FR-02, FR-03                      | Verify scheduled inventory synchronization                         |
| BR-03                | FR-06, FR-07, FR-08               | Complete mock sale and verify Zoho decrement                       |
| BR-04                | FR-60, FR-61                      | Confirm polling detects and reconciles mismatches                  |
| BR-05                | FR-04, FR-63                      | Simulate sync failure and verify last trusted state remains active |
| BR-06                | FR-05, FR-51, FR-64               | Create discrepancy and confirm passive dashboard visibility        |
| BR-17                | FR-06, FR-45, FR-74               | Verify Lightspeed mock remains pricing and transaction authority   |
| BR-18                | FR-73, FR-74                      | Confirm middleware contains no payment-card data                   |
| BR-19                | N/A                               | Validate managed accounts remain outside POC workflow              |
| BR-20                | FR-41, FR-42, FR-43, FR-44, FR-45 | Test authenticated reorder flow                                    |

## Reservations

| Business Requirement | Functional Requirement(s) | Validation                                                     |
| -------------------- | ------------------------- | -------------------------------------------------------------- |
| BR-07                | FR-11, FR-12              | Begin checkout and verify reservation creation                 |
| BR-08                | FR-14                     | Allow reservation to reach configured expiration               |
| BR-09                | FR-15                     | Verify expired quantity returns to availability                |
| BR-10                | FR-16, FR-20              | Confirm reservation does not alter authoritative Zoho quantity |
| BR-11                | FR-17                     | Verify standard in-stock display                               |
| BR-12                | FR-18, FR-19              | Verify exact quantity appears below threshold                  |
| BR-13                | FR-20, FR-22              | Verify out-of-stock product enters alternate flow              |
| BR-14                | FR-22, FR-23, FR-24       | Confirm inquiry contains product context                       |
| BR-15                | FR-25, FR-26              | Verify in-stock alternatives appear                            |
| BR-16                | FR-21                     | Verify pre-order state remains distinct                        |

## Catalog and Product Data

| Business Requirement | Functional Requirement(s) | Validation                                                |
| -------------------- | ------------------------- | --------------------------------------------------------- |
| BR-21                | FR-36                     | Execute nightly metadata synchronization                  |
| BR-22                | FR-31, FR-32, FR-38       | Verify descriptive application and compatibility metadata |
| BR-23                | FR-37, FR-38, FR-39       | Edit product metadata through dashboard                   |
| BR-24                | FR-27, FR-28, FR-29       | Verify search and category navigation are both prominent  |
| BR-25                | FR-30–FR-35               | Validate grid/list catalog behavior and controls          |
| BR-26                | FR-30–FR-34               | Verify required filter hierarchy                          |
| BR-27                | FR-27, FR-28              | Confirm direct product and SKU lookup remains supported   |

## Middleware

| Business Requirement | Functional Requirement(s)  | Validation                                                                               |
| -------------------- | -------------------------- | ---------------------------------------------------------------------------------------- |
| BR-28                | FR-01, FR-06, FR-60        | Verify orchestration across storefront, Lightspeed mock, and Zoho mock                   |
| BR-29                | FR-69, FR-70               | Run POC entirely against mock services                                                   |
| BR-30                | FR-72                      | Confirm integration logic depends on service interfaces rather than mock implementations |
| BR-31                | FR-11, FR-36, FR-60, FR-65 | Validate required middleware functions                                                   |

## Dashboard and BI

| Business Requirement | Functional Requirement(s) | Validation                                     |
| -------------------- | ------------------------- | ---------------------------------------------- |
| BR-32                | FR-46                     | Authenticate as employee, manager, and owner   |
| BR-33                | FR-47, FR-54–FR-59        | Verify broad BI visibility                     |
| BR-34                | FR-48                     | Attempt restricted actions using each role     |
| BR-35                | FR-51, FR-60, FR-61       | Verify discrepancy visibility                  |
| BR-36                | FR-52, FR-62              | Trace inventory state through event history    |
| BR-37                | FR-64                     | Verify discrepancies remain passive indicators |

## Audit and Control

| Business Requirement | Functional Requirement(s) | Validation                                                             |
| -------------------- | ------------------------- | ---------------------------------------------------------------------- |
| BR-38                | FR-65                     | Perform inventory adjustment and inspect audit event                   |
| BR-39                | FR-66, FR-67              | Perform reconciliation/configuration change and inspect audit event    |
| BR-40                | FR-68                     | Verify required audit fields                                           |
| BR-41                | FR-37, FR-38, FR-39       | Confirm routine merchandising edits do not generate full audit records |

## User Interface

| Business Requirement | Functional Requirement(s) | Validation                                                           |
| -------------------- | ------------------------- | -------------------------------------------------------------------- |
| BR-42                | NFR-43                    | Verify animated site treatment across supported storefront pages     |
| BR-43                | NFR-32, NFR-33, NFR-35    | Review visual hierarchy and navigation efficiency                    |
| BR-44                | FR-25, FR-26              | Verify imagery remains product-focused rather than category-dominant |

## Proof of Concept

| Business Requirement | Functional Requirement(s) | Validation                                          |
| -------------------- | ------------------------- | --------------------------------------------------- |
| BR-45                | FR-69–FR-76               | Run complete POC locally or in test deployment      |
| BR-46                | NFR-47, NFR-48            | Verify repository contains only synthetic/mock data |
| BR-47                | FR-01–FR-76               | Execute end-to-end workflow test set                |

## Nonfunctional Coverage

| Area                      | Requirements  |
| ------------------------- | ------------- |
| Availability / Resilience | NFR-01–NFR-04 |
| Performance               | NFR-05–NFR-08 |
| Scalability               | NFR-09–NFR-11 |
| Security                  | NFR-12–NFR-17 |
| Data Integrity            | NFR-18–NFR-22 |
| Auditability              | NFR-23–NFR-26 |
| Maintainability           | NFR-27–NFR-31 |
| Usability                 | NFR-32–NFR-36 |
| Accessibility             | NFR-37–NFR-40 |
| Compatibility             | NFR-41–NFR-43 |
| Logging / Monitoring      | NFR-44–NFR-46 |
| POC Safety                | NFR-47–NFR-50 |

