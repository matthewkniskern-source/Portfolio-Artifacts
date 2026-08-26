# Security Controls

## Authentication

* Internal dashboard access requires authentication.
* Customer reorder functions require authenticated retail accounts.
* Service processes shall use separate service identities where practical.

## Authorization

* Role-based access controls apply to internal functions.
* Restricted actions shall be enforced server-side.
* Inventory adjustments, reconciliation actions, and system configuration shall require elevated roles.

## Secrets Management

* API credentials shall not be committed to source control.
* Secrets shall be supplied through environment variables or equivalent secret-management mechanisms.
* Production credentials shall remain outside the public POC repository.

## Payment Isolation

* Payment processing remains within Lightspeed.
* Middleware shall not store or process raw payment-card data.
* Payment-related logs shall contain transaction state only.

## API Security

* Internal and administrative endpoints require authentication.
* Input shall be validated before processing.
* Invalid or malformed requests shall be rejected.
* Vendor credentials shall never be returned to clients.
* Internal stack traces shall not be exposed in customer-facing responses.

## Inventory Integrity

* Completed-sale events shall be idempotent.
* Duplicate event IDs shall not create duplicate inventory decrements.
* Reservation quantities shall not reduce web availability below zero.
* Failed synchronization shall preserve the last trusted inventory state.
* Inventory-affecting manual changes shall be auditable.

## Session Security

Internal dashboard sessions should support:

* Secure authentication
* Session expiration
* Logout
* Protection against unauthorized reuse

## Transport Security

Production deployment shall use encrypted HTTPS connections for:

* Storefront traffic
* Dashboard traffic
* Middleware APIs
* Zoho integration
* Lightspeed integration

## Logging

Logs shall exclude:

* Passwords
* API secrets
* Authentication tokens
* Full payment-card data
* CVV
* Sensitive production credentials

## Audit Controls

The system shall record:

* Inventory adjustments
* Reconciliation actions
* Role changes
* Permission changes
* Integration configuration changes
* System-control changes
* Completed-sale inventory decrements

## Availability Controls

If an external integration fails:

* Storefront remains operational where safe
* Last trusted inventory state remains active
* Failure is logged
* Passive dashboard indicator is displayed

## Proof-of-Concept Controls

* Use synthetic product, customer, order, and inventory data.
* Use mock Zoho and Lightspeed endpoints.
* Do not include production credentials.
* Do not include production customer data.
* Do not include live payment information.
