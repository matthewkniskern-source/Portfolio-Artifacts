# Integration Architecture

## Integration Pattern

```text
Storefront
   │
   ▼
Middleware API
   │
   ├────────► Zoho Adapter
   │
   └────────► Lightspeed Adapter
```

The middleware isolates storefront logic from external platform-specific APIs.

## Zoho Integration

### Reads

* SKU
* Product identifier
* Current warehouse quantity
* Inventory status
* Selected product metadata

### Writes

* Confirmed inventory decrement
* Authorized inventory adjustment where supported

### Primary Uses

* Five-minute inventory synchronization
* Completed-sale decrement
* Reconciliation
* Nightly metadata synchronization

## Lightspeed Integration

### Reads

* Product identifier
* SKU
* Current public retail price
* Completed order information
* Customer online order history
* Product transaction status

### Events / Inputs

* Completed-sale event
* Order identifier
* Purchased SKU
* Quantity
* Customer account identifier where applicable

### Primary Uses

* Checkout authority
* Pricing authority
* Completed-sale confirmation
* Reorder pricing
* Customer purchase history

## Adapter Model

```text
InventoryService
   │
   ├── MockZohoAdapter
   └── ZohoApiAdapter

CommerceService
   │
   ├── MockLightspeedAdapter
   └── LightspeedApiAdapter
```

Application services depend on shared interfaces rather than vendor-specific implementations.

## Inventory Synchronization

```text
Scheduler
   │
   ▼
Inventory Service
   │
   ▼
Zoho Adapter
   │
   ▼
Current Quantity
   │
   ▼
Middleware Inventory State
   │
   ├── Apply active reservations
   └── Publish web availability
```

Default interval:

`5 minutes`

## Completed-Sale Processing

```text
Lightspeed
   │
   ▼
Completed Sale Event
   │
   ▼
Commerce Adapter
   │
   ▼
Middleware
   │
   ├── Validate event
   ├── Check duplicate event ID
   ├── Close reservation
   ├── Submit Zoho decrement
   ├── Update local state
   └── Record audit event
```

## Reservation Integration

Reservations exist within the middleware.

```text
Zoho Quantity
      -
Active Reservations
      =
Available Web Quantity
```

Reservations do not alter Zoho inventory until a completed sale occurs.

## Nightly Metadata Synchronization

```text
Scheduler
   │
   ▼
Configured Product Metadata
   │
   ▼
Middleware Metadata Store
   │
   ├── Application text
   ├── Compatibility text
   └── Related-product data
```

Public retail pricing remains under Lightspeed authority.

## Reconciliation

```text
Zoho Inventory
        +
Lightspeed Completed Sales
        +
Active Reservations
        +
Middleware Event History
        │
        ▼
Reconciliation Service
        │
        ├── Match
        └── Discrepancy
```

Unresolved discrepancies retain the last trusted inventory state and remain visible through passive dashboard indicators.

## Error Handling

### Zoho Unavailable

* Preserve last trusted inventory state
* Record failed synchronization
* Continue storefront operation
* Display passive dashboard indicator

### Lightspeed Event Failure

* Record failed event processing
* Preserve transaction identifier
* Retry according to configured policy
* Prevent duplicate inventory decrement

### Duplicate Sale Event

* Compare event identifier
* Reject duplicate processing
* Preserve current inventory state
* Record duplicate event

### Reservation Failure

* Do not assume stock is reserved
* Return controlled availability response
* Record failure for staff visibility

## Security Boundary

The middleware may process:

* Product identifiers
* SKUs
* Inventory quantities
* Order identifiers
* Transaction status
* Customer account identifiers
* Product metadata

The middleware shall not process or store:

* Payment-card numbers
* CVV data
* Payment authentication secrets
* Raw cardholder data

## Proof-of-Concept Endpoints

Mock services should support representative endpoints for:

### Zoho Mock

* Retrieve products
* Retrieve inventory
* Retrieve individual SKU quantity
* Update inventory quantity
* Simulate integration failure
* Simulate inventory discrepancy

### Lightspeed Mock

* Retrieve product pricing
* Retrieve customer order history
* Generate completed sale
* Retrieve completed order
* Simulate duplicate sale event
* Simulate failed event delivery

## Configuration

Externalized configuration should include:

* Inventory polling interval
* Reservation duration
* Low-stock threshold
* Metadata synchronization schedule
* Retry settings
* Adapter selection
* API base URLs
* Credential references
