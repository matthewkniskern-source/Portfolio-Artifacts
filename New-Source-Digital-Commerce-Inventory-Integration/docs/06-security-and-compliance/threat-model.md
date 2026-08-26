# Threat Model

## Protected Assets

* Inventory data
* Customer account identifiers
* Order identifiers
* Reservation state
* Audit records
* Integration credentials
* Administrative functions
* Product metadata
* Reconciliation history

## Primary Threats

### Unauthorized Dashboard Access

Risk:

* Unauthorized inventory changes
* Access to internal operational data
* Role abuse

Controls:

* Authentication
* Role-based authorization
* Session expiration
* Server-side permission checks

### Credential Exposure

Risk:

* Unauthorized access to Zoho or Lightspeed
* Inventory manipulation
* Data exposure

Controls:

* Externalized secrets
* No credentials in source control
* No credentials in frontend code
* Credential rotation
* Least-privilege scopes

### Duplicate Sale Processing

Risk:

* Repeated Zoho inventory decrement
* Inventory corruption

Controls:

* Unique event identifiers
* Idempotent processing
* Duplicate-event rejection
* Audit logging

### Reservation Manipulation

Risk:

* Artificial stock depletion
* Inventory denial to legitimate buyers

Controls:

* Server-side reservation validation
* Quantity limits
* Expiration controls
* Session/customer association
* Available-quantity validation

### Inventory Synchronization Failure

Risk:

* Stale inventory
* Overselling
* Incorrect customer availability

Controls:

* Last trusted inventory state
* Passive discrepancy indicator
* Reconciliation
* Sync-status tracking

### API Tampering

Risk:

* Unauthorized inventory changes
* Invalid order events
* Metadata manipulation

Controls:

* Authentication
* Request validation
* Authorization
* HTTPS
* Input validation
* Vendor-event verification where supported

### Injection Attacks

Risk:

* Database manipulation
* Unauthorized command execution
* Data exposure

Controls:

* Parameterized queries
* Input validation
* Output encoding
* Restricted database permissions

### Cross-Site Scripting

Risk:

* Session theft
* Dashboard manipulation
* Customer-facing script injection

Controls:

* Output encoding
* Input sanitization
* Content Security Policy where practical
* Restrict unsafe HTML in custom metadata

### Cross-Site Request Forgery

Risk:

* Unauthorized administrative action through an authenticated session

Controls:

* CSRF protections
* SameSite cookies
* Request validation
* Reauthentication for sensitive actions where appropriate

### Broken Access Control

Risk:

* Employee performing manager or owner actions

Controls:

* Server-side RBAC
* Role validation on every restricted endpoint
* Audit logging of privileged actions

### Log Exposure

Risk:

* Credential or customer-data disclosure

Controls:

* Exclude secrets from logs
* Restrict log access
* Separate audit and application logs
* Use structured logging

### Payment Data Exposure

Risk:

* Expansion of PCI scope
* Cardholder-data compromise

Controls:

* Keep payment processing within Lightspeed
* Do not store raw cardholder data
* Do not proxy payment credentials through middleware

## Availability Risks

### Middleware Failure

Impact:

* Inventory refresh unavailable
* Reservations unavailable
* Dashboard unavailable

Response:

* Preserve last trusted inventory state where safe
* Continue storefront operation where possible
* Record failure for staff review

### External API Failure

Impact:

* Zoho or Lightspeed integration unavailable

Response:

* Retry according to policy
* Preserve transaction identifiers
* Prevent duplicate processing
* Display passive operational indicator

## Data Integrity Risks

### Incorrect Manual Adjustment

Controls:

* Restricted permissions
* Before-and-after logging
* User attribution
* Reconciliation review

### Product Identifier Mismatch

Controls:

* SKU validation
* Product-ID mapping
* Reconciliation checks
* Reject ambiguous or unmatched updates

## Proof-of-Concept Scope

The POC shall demonstrate control behavior using synthetic scenarios, including:

* Duplicate sale event
* Failed inventory sync
* Expired reservation
* Unauthorized action attempt
* Inventory discrepancy
* Invalid API request
