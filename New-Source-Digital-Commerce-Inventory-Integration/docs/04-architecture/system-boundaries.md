# System Boundaries

## Storefront Boundary

The storefront is responsible for:

* Public catalog presentation
* Search
* Category navigation
* Product detail
* Inventory status display
* Cart interaction
* Reorder entry point
* Out-of-stock lead routing
* Related-product presentation

The storefront does not own:

* Warehouse inventory truth
* Public pricing authority
* Payment processing
* Completed-sale authority

## Lightspeed Boundary

Lightspeed is responsible for:

* Public retail pricing
* Checkout
* Payment processing
* Completed online transactions
* Customer online order history

Lightspeed remains outside the custom middleware payment boundary.

## Zoho Boundary

Zoho Inventory is responsible for:

* Warehouse inventory quantity
* Inventory availability source data
* Inventory adjustment after confirmed sale
* Warehouse-side stock reconciliation

Zoho does not manage temporary cart reservations.

## Middleware Boundary

The middleware is responsible for:

* Inventory synchronization
* Web availability calculation
* Temporary reservations
* Completed-sale event processing
* Zoho decrement requests
* Reconciliation
* Custom product metadata
* Audit records
* Dashboard data
* Business intelligence aggregation

The middleware does not own:

* Cardholder data
* Payment authorization
* Negotiated commercial pricing
* Managed-account sales processes

## Dashboard Boundary

The dashboard is responsible for:

* Operational visibility
* BI visibility
* Inventory discrepancy review
* Reconciliation traceability
* Product metadata maintenance
* Authorized system actions
* Role-based administrative access

## Managed Commercial Accounts

Managed commercial accounts remain outside the public storefront workflow.

Included processes remain with sales staff:

* Negotiated pricing
* Financing terms
* High-touch account management
* Phone or text ordering
* Custom commercial arrangements

## Payment Boundary

```text id="m7ax2p"
Customer
   │
   ▼
Storefront
   │
   ▼
Lightspeed Checkout
   │
   ▼
Payment Processor

Middleware
   X
No Cardholder Data
```

The middleware may receive transaction status and order identifiers but shall not receive raw payment-card data.

## Inventory Boundary

```text id="74f95j"
Zoho Inventory
   │
   │ Authoritative Quantity
   ▼
Middleware
   │
   ├── Reservations
   ├── Availability Calculation
   └── Reconciliation
        │
        ▼
Storefront
```

## Transaction Boundary

```text id="v03mwm"
Lightspeed
   │
   │ Completed Sale
   ▼
Middleware
   │
   ├── Validate
   ├── Deduplicate
   ├── Close Reservation
   └── Decrement Zoho
```

## Proof-of-Concept Boundary

The POC includes:

* Mock storefront
* Mock Zoho endpoints
* Mock Lightspeed endpoints
* Reservation service
* Reconciliation service
* Audit logging
* Internal dashboard
* Synthetic product, customer, order, and inventory data

The POC excludes:

* Production credentials
* Production customer data
* Production payment data
* Live managed-account pricing
* Direct production integration
