# Deployment Concept

## Proof-of-Concept Deployment

The POC is separated into three deployable components:

```text id="43sq9e"
Storefront
Middleware/API
Operations Dashboard
```

Mock Zoho and Lightspeed services run independently from the core application logic.

## Logical Deployment

```text id="u83qw2"
User Browser
   │
   ├── Storefront
   │
   └── Operations Dashboard
            │
            ▼
        Middleware API
            │
            ├── Mock Zoho Service
            ├── Mock Lightspeed Service
            ├── Reservation Service
            ├── Reconciliation Service
            ├── Metadata Store
            ├── Audit Store
            └── Analytics Store
```

## Storefront

Deploy as a public web application.

Responsibilities:

* Product search and browsing
* Product detail
* Availability display
* Cart and reservation interaction
* Account/reorder flow
* Out-of-stock lead flow
* Related-product display

## Middleware API

Deploy as an application service.

Responsibilities:

* Inventory synchronization
* Reservation management
* Completed-sale processing
* Reconciliation
* Product metadata
* Audit events
* BI aggregation
* Internal API access

## Operations Dashboard

Deploy as an authenticated internal web application.

Responsibilities:

* Operational status
* Inventory discrepancies
* Reconciliation history
* BI metrics
* Product metadata maintenance
* Authorized administrative actions

## Data Stores

POC storage may include:

* Inventory state
* Reservation records
* Product metadata
* Reconciliation records
* Audit events
* Lead records
* Analytics data

Production payment data shall not be stored.

## Scheduled Jobs

### Inventory Polling

Default interval:

`5 minutes`

### Metadata Synchronization

Default schedule:

`Nightly after business hours`

### Reservation Expiration

Reservation cleanup runs independently from inventory polling.

### Reconciliation

Runs on a configurable schedule and after relevant integration events.

## Configuration

Environment-specific configuration shall include:

* API base URLs
* Adapter selection
* Inventory polling interval
* Reservation duration
* Low-stock threshold
* Metadata sync schedule
* Retry settings
* Authentication settings
* Logging level

## Environment Separation

Recommended environments:

```text id="28i9pn"
Local Development
      ↓
POC / Demo
      ↓
Future Test / Sandbox
      ↓
Future Production
```

Production credentials and live customer data shall not be used in the public POC.

## Production Transition

The POC shall support replacement of:

```text id="n2pxhi"
MockZohoAdapter
→ ZohoApiAdapter

MockLightspeedAdapter
→ LightspeedApiAdapter
```

No storefront redesign should be required for adapter replacement.

## Availability Behavior

If an external integration is unavailable:

* Storefront remains operational
* Last trusted inventory state remains active
* Failed synchronization is logged
* Dashboard shows a passive discrepancy indicator

## Security Boundary

Public access:

* Storefront
* Customer-facing API routes required by the storefront

Restricted access:

* Operations dashboard
* Reconciliation actions
* Inventory adjustments
* System configuration
* Audit history
* Administrative endpoints

## Handoff

The deployment model should allow the existing hosting or implementation provider to:

* Review the POC independently
* Replace mock integrations with production connectors
* Configure environment-specific settings
* Deploy storefront and middleware components separately where needed
* Retain Lightspeed payment processing and Zoho inventory authority
