# Data Flow

## Product and Inventory Data

```text
Zoho Inventory
   │
   ├── SKU
   ├── Product ID
   ├── Warehouse Quantity
   └── Inventory Status
        │
        ▼
Middleware
   │
   ├── Last Trusted Quantity
   ├── Active Reservations
   ├── Calculated Web Availability
   └── Sync Timestamp
        │
        ▼
Storefront
```

## Pricing Data

```text
Lightspeed
   │
   ├── SKU
   ├── Product ID
   └── Current Retail Price
        │
        ▼
Storefront
```

Historical order price shall not override current Lightspeed pricing during reorder.

## Reservation Data

```text
Customer Cart
   │
   ▼
Middleware Reservation Service
   │
   ├── Reservation ID
   ├── SKU
   ├── Quantity
   ├── Customer / Session ID
   ├── Created At
   ├── Expires At
   └── Status
        │
        ▼
Calculated Web Availability
```

## Completed-Sale Data

```text
Lightspeed
   │
   ├── Order ID
   ├── Event ID
   ├── Customer Account ID
   ├── SKU
   ├── Quantity
   └── Sale Status
        │
        ▼
Middleware
   │
   ├── Validate Event
   ├── Check Idempotency
   ├── Match Reservation
   ├── Close Reservation
   └── Submit Inventory Decrement
        │
        ▼
Zoho Inventory
```

## Reconciliation Data

```text
Zoho Quantity
      +
Active Reservations
      +
Completed Sales
      +
Middleware Event History
      │
      ▼
Reconciliation Service
      │
      ├── Expected Quantity
      ├── Observed Quantity
      ├── Difference
      └── Status
```

## Product Metadata

```text
Nightly Source Data
   │
   ▼
Middleware Metadata Store
   │
   ├── Application / Use Case
   ├── Compatibility Text
   ├── Related Products
   └── Supplemental Specifications
        │
        ▼
Storefront
```

## Customer Account Data

```text
Lightspeed Customer Account
   │
   ├── Customer ID
   ├── Order History
   └── Eligible Prior Purchases
        │
        ▼
Reorder Interface
```

Managed commercial-account data remains outside this flow.

## Out-of-Stock Lead Data

```text
Out-of-Stock Product
   │
   ▼
Contact Flow
   │
   ├── Product Name
   ├── SKU
   ├── Customer Contact Information
   ├── Inquiry Method
   └── Timestamp
        │
        ▼
Lead Record / Staff Follow-Up
```

## Audit Data

Audit events may include:

* Event ID
* Timestamp
* Actor or process
* Action type
* SKU or affected object
* Previous value
* New value
* Related order ID
* Related reservation ID
* Reconciliation ID
* Result

## Dashboard Data

The operations dashboard consumes:

* Inventory synchronization status
* Current inventory state
* Active reservations
* Completed-sale processing activity
* Discrepancy records
* Reconciliation history
* Audit events
* Out-of-stock lead activity
* Reorder activity
* Sales and inventory trend data

## Data Authority

| Data                          | Authority  |
| ----------------------------- | ---------- |
| Warehouse inventory quantity  | Zoho       |
| Public retail pricing         | Lightspeed |
| Completed online sale         | Lightspeed |
| Payment processing            | Lightspeed |
| Temporary reservation state   | Middleware |
| Calculated web availability   | Middleware |
| Custom application metadata   | Middleware |
| Custom compatibility text     | Middleware |
| Related-product configuration | Middleware |
| Inventory audit history       | Middleware |
| Reconciliation state          | Middleware |

## Excluded Data

The custom application shall not store:

* Payment-card number
* CVV
* Raw payment credentials
* Production API secrets in source code
* Managed commercial pricing
* Negotiated customer account terms
