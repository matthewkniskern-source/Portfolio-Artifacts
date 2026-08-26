# API Contracts

## Inventory Service

### Get Current Inventory

`GET /api/inventory`

Returns current inventory state for all exposed products.

```json
{
  "items": [
    {
      "sku": "SKU-1001",
      "productId": "P-1001",
      "quantity": 12,
      "status": "in_stock",
      "updatedAt": "2026-08-26T17:00:00Z"
    }
  ]
}
```

### Get Inventory by SKU

`GET /api/inventory/{sku}`

```json
{
  "sku": "SKU-1001",
  "productId": "P-1001",
  "quantity": 3,
  "status": "low_stock",
  "updatedAt": "2026-08-26T17:00:00Z"
}
```

### Adjust Inventory

`POST /api/inventory/{sku}/adjust`

```json
{
  "quantityChange": -1,
  "reason": "completed_sale",
  "referenceId": "ORD-5001"
}
```

## Reservation Service

### Create Reservation

`POST /api/reservations`

```json
{
  "sku": "SKU-1001",
  "quantity": 1,
  "customerId": "CUST-1001"
}
```

Response:

```json
{
  "reservationId": "RES-9001",
  "sku": "SKU-1001",
  "quantity": 1,
  "status": "active",
  "expiresAt": "2026-08-26T17:10:00Z"
}
```

### Get Reservation

`GET /api/reservations/{reservationId}`

### Release Reservation

`POST /api/reservations/{reservationId}/release`

### Complete Reservation

`POST /api/reservations/{reservationId}/complete`

## Commerce Service

### Get Product Price

`GET /api/commerce/products/{sku}/price`

```json
{
  "sku": "SKU-1001",
  "price": 1299.00,
  "currency": "USD"
}
```

### Get Customer Order History

`GET /api/commerce/customers/{customerId}/orders`

### Get Completed Order

`GET /api/commerce/orders/{orderId}`

```json
{
  "orderId": "ORD-5001",
  "customerId": "CUST-1001",
  "status": "completed",
  "items": [
    {
      "sku": "SKU-1001",
      "quantity": 1,
      "unitPrice": 1299.00
    }
  ]
}
```

## Completed-Sale Event

### Receive Completed Sale

`POST /api/events/completed-sale`

```json
{
  "eventId": "EVT-7001",
  "orderId": "ORD-5001",
  "customerId": "CUST-1001",
  "status": "completed",
  "items": [
    {
      "sku": "SKU-1001",
      "quantity": 1
    }
  ],
  "completedAt": "2026-08-26T17:05:00Z"
}
```

Processing shall:

1. Validate event
2. Check event ID for duplicate processing
3. Identify related reservation
4. Close reservation
5. Decrement Zoho inventory
6. Update local inventory state
7. Record audit event

## Product Metadata Service

### Get Product Metadata

`GET /api/products/{sku}/metadata`

```json
{
  "sku": "SKU-1001",
  "application": "Commercial water damage restoration",
  "compatibility": "Suitable for use with supported extraction systems",
  "relatedProducts": [
    "SKU-1002",
    "SKU-1003"
  ]
}
```

### Update Product Metadata

`PUT /api/products/{sku}/metadata`

```json
{
  "application": "Commercial water damage restoration",
  "compatibility": "Suitable for supported extraction and drying workflows",
  "relatedProducts": [
    "SKU-1002",
    "SKU-1003"
  ]
}
```

## Out-of-Stock Lead Service

### Create Product Lead

`POST /api/leads`

```json
{
  "sku": "SKU-1001",
  "productName": "Example Product",
  "customerName": "Jane Customer",
  "email": "customer@example.com",
  "phone": "555-0100",
  "contactMethod": "email",
  "message": "Please contact me when this becomes available."
}
```

## Reconciliation Service

### Get Discrepancies

`GET /api/reconciliation/discrepancies`

### Get Discrepancy Detail

`GET /api/reconciliation/discrepancies/{id}`

```json
{
  "discrepancyId": "REC-3001",
  "sku": "SKU-1001",
  "zohoQuantity": 8,
  "lastTrustedQuantity": 9,
  "activeReservedQuantity": 1,
  "completedSaleQuantity": 1,
  "expectedQuantity": 8,
  "difference": 0,
  "status": "resolved"
}
```

### Resolve Discrepancy

`POST /api/reconciliation/discrepancies/{id}/resolve`

```json
{
  "resolution": "manual_adjustment",
  "newQuantity": 8,
  "notes": "Validated against warehouse count."
}
```

## Dashboard Service

### Get Operational Summary

`GET /api/dashboard/operations`

Response may include:

* Last inventory sync
* Active reservations
* Open discrepancies
* Recent completed sales
* Failed integration jobs

### Get BI Summary

`GET /api/dashboard/analytics`

Response may include:

* Sales trends
* Stockout frequency
* Expired reservations
* Out-of-stock leads
* Reorder activity
* Frequently reordered products

## Audit Service

### Get Audit Events

`GET /api/audit`

Audit record:

```json
{
  "eventId": "AUD-8001",
  "timestamp": "2026-08-26T17:05:02Z",
  "actor": "system",
  "action": "inventory_decrement",
  "sku": "SKU-1001",
  "before": 9,
  "after": 8,
  "referenceId": "ORD-5001"
}
```

## Error Model

```json
{
  "error": {
    "code": "INVENTORY_SYNC_FAILED",
    "message": "Inventory synchronization could not be completed.",
    "timestamp": "2026-08-26T17:00:00Z"
  }
}
```

Customer-facing responses shall not expose internal credentials, stack traces, or vendor-specific implementation details.

## Proof-of-Concept Adapter Mapping

```text
InventoryService
→ MockZohoAdapter

CommerceService
→ MockLightspeedAdapter
```

Production transition:

```text
InventoryService
→ ZohoApiAdapter

CommerceService
→ LightspeedApiAdapter
```

Application routes and business logic shall remain unchanged.
