# Solution Architecture

## Core Systems

### Storefront

Customer-facing ecommerce layer.

Functions:

* Search
* Category browsing
* Product listings
* Product detail
* Inventory availability display
* Cart
* Reorder
* Out-of-stock lead flow
* Related-product display

### Lightspeed

Fiscal and ecommerce authority.

Functions:

* Public retail pricing
* Checkout
* Payment processing
* Completed-sale record
* Customer online order history

### Middleware

Integration and orchestration layer.

Functions:

* Inventory synchronization
* Reservation management
* Completed-sale processing
* Zoho inventory decrement
* Reconciliation
* Custom product metadata
* Audit events
* Dashboard data
* Business intelligence

### Zoho Inventory

Warehouse inventory authority.

Functions:

* Inventory quantity
* Product inventory status
* Inventory decrement
* Warehouse stock reconciliation

### Operations Dashboard

Internal staff interface.

Functions:

* Synchronization status
* Inventory visibility
* Active reservations
* Discrepancies
* Reconciliation history
* Sales activity
* BI metrics
* Product metadata maintenance
* Role-based administrative functions

## System Relationship

```text
Customer
   │
   ▼
Storefront
   │
   ├──────────────► Middleware
   │                   │
   │                   ├────────► Zoho Inventory
   │                   │
   │                   └────────► Operations Dashboard
   │
   ▼
Lightspeed
   │
   │ Completed Sale
   ▼
Middleware
   │
   ▼
Zoho Inventory
```

## Inventory Flow

Zoho Inventory
→ Middleware inventory sync
→ Active reservations applied
→ Web availability calculated
→ Storefront displays availability

## Sale Flow

Storefront
→ Lightspeed checkout
→ Payment completed
→ Completed-sale event
→ Middleware
→ Reservation closed
→ Zoho inventory decremented
→ Audit event recorded

## Reservation Flow

Storefront cart
→ Middleware reservation service
→ Available quantity validated
→ Temporary reservation created
→ Web availability reduced
→ Reservation completed or expired

## Reconciliation Flow

Zoho inventory

* Active reservations
* Completed Lightspeed sales
* Middleware event history
  → Reconciliation process
  → Expected state calculated
  → Discrepancy identified or state confirmed

## Metadata Flow

Scheduled nightly process
→ Product metadata retrieved
→ Middleware metadata store updated
→ Application and compatibility information combined
→ Storefront catalog refreshed

Lightspeed remains authoritative for public retail pricing.

## Integration Boundary

The middleware shall exchange:

* SKU
* Product identifiers
* Inventory quantity
* Reservation state
* Order identifiers
* Sale status
* Product metadata
* Audit events

The middleware shall not store or process payment-card data.

## Proof-of-Concept Architecture

```text
Storefront
   │
   ▼
Middleware API
   │
   ├────────► Mock Zoho Adapter
   │
   ├────────► Mock Lightspeed Adapter
   │
   ├────────► Reservation Service
   │
   ├────────► Reconciliation Service
   │
   ├────────► Metadata Service
   │
   ├────────► Audit Service
   │
   └────────► Analytics Service
                     │
                     ▼
              Operations Dashboard
```

## Production Transition

Mock adapters may later be replaced by production connectors.

```text
MockZohoAdapter
      ↓
ZohoApiAdapter

MockLightspeedAdapter
      ↓
LightspeedApiAdapter
```

Core storefront and middleware business logic shall remain unchanged.
