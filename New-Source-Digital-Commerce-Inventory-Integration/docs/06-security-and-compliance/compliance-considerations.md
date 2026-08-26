# Compliance Considerations

## Payment Card Environment

Payment processing remains within Lightspeed and its designated payment-processing environment.

The custom storefront and middleware should avoid handling raw cardholder data.

Relevant design implications:

* Do not store card numbers
* Do not store CVV data
* Do not proxy raw payment credentials through middleware
* Use Lightspeed-hosted or Lightspeed-controlled payment workflows where possible
* Keep payment logs limited to transaction status and reference identifiers

## PCI DSS Scope

The solution should be designed to minimize PCI DSS scope by keeping the middleware outside the cardholder-data environment.

Production implementation should validate:

* Payment integration method
* Hosting architecture
* Redirect or embedded checkout behavior
* Responsibility boundaries between New Source, Lightspeed, and the hosting provider

## Authentication and Access Control

Internal dashboard access requires authentication.

Administrative and inventory-affecting actions require role-based authorization.

Privileged actions should remain limited to assigned manager or owner roles.

## Data Minimization

The custom application should store only data required for:

* Inventory synchronization
* Reservation management
* Order reconciliation
* Customer reorder functionality
* Product metadata
* Auditability
* Business intelligence

Sensitive production data should not be duplicated without operational need.

## Customer Data

Customer account identifiers and order-history references may be processed where required for authenticated reorder functionality.

Production implementation should define:

* Customer-data retention
* Access restrictions
* Deletion procedures where applicable
* Incident-response handling
* Vendor responsibility boundaries

## Privacy

Customer-facing data collection should remain limited to necessary transactional and lead-generation information.

Out-of-stock lead forms should disclose what customer information is being collected and how it will be used.

## Auditability

Inventory-affecting and system-control actions should remain attributable to:

* User
* Service process
* Timestamp
* Affected record
* Result

Audit records should support operational investigation and system accountability.

## Third-Party Services

Production implementation should review the security and compliance responsibilities of:

* Lightspeed
* Zoho
* Website hosting provider
* Middleware hosting provider
* Authentication provider where applicable

## API Security

Production API integrations should use:

* HTTPS
* Vendor-supported authentication
* Least-privilege credentials
* Secret rotation
* Controlled administrative access

## Public Repository

The portfolio repository shall not contain:

* Production credentials
* Production customer records
* Live order data
* Payment-card data
* Proprietary account pricing
* Private API secrets

Synthetic and mocked data shall be used throughout the proof of concept.

## Production Review

Before production deployment, the implementation provider should validate:

* Current Lightspeed API and webhook capabilities
* Current Zoho Inventory API capabilities
* Payment-flow architecture
* PCI DSS responsibilities
* Privacy requirements
* Hosting security controls
* Backup and recovery requirements
* Incident-response procedures
