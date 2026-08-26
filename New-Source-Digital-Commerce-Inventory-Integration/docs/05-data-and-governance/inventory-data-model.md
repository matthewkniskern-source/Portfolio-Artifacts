# Inventory Data Model

## Product Inventory Record

| Field                  | Description                                         |
| ---------------------- | --------------------------------------------------- |
| `sku`                  | Primary product identifier used across integrations |
| `productId`            | Internal or external product record identifier      |
| `zohoQuantity`         | Current authoritative warehouse quantity            |
| `lastTrustedQuantity`  | Most recent validated quantity                      |
| `reservedQuantity`     | Quantity held by active web reservations            |
| `availableWebQuantity` | Quantity currently available for web purchase       |
| `inventoryStatus`      | In stock, low stock, out of stock, pre-order        |
| `lowStockThreshold`    | Configured quantity threshold                       |
| `lastSyncedAt`         | Timestamp of last successful inventory sync         |
| `syncStatus`           | Current synchronization state                       |
| `discrepancyStatus`    | Current reconciliation/discrepancy state            |

## Availability Calculation

```text
availableWebQuantity
=
lastTrustedQuantity
-
reservedQuantity
```

The result shall not fall below zero.

## Inventory Status

### In Stock

```text
availableWebQuantity > lowStockThreshold
```

Display:

`In Stock`

### Low Stock

```text
0 < availableWebQuantity <= lowStockThreshold
```

Display:

`Only X remaining`

### Out of Stock

```text
availableWebQuantity = 0
```

Display:

* Out of Stock
* Contact options
* Related in-stock alternatives

### Pre-Order

Pre-order status is controlled independently from available warehouse quantity.

## Reservation Record

| Field           | Description                                       |
| --------------- | ------------------------------------------------- |
| `reservationId` | Unique reservation identifier                     |
| `sku`           | Reserved product                                  |
| `quantity`      | Reserved quantity                                 |
| `customerId`    | Authenticated customer identifier where available |
| `sessionId`     | Anonymous or temporary session identifier         |
| `createdAt`     | Reservation creation timestamp                    |
| `expiresAt`     | Reservation expiration timestamp                  |
| `status`        | Active, completed, expired, released, failed      |
| `orderId`       | Associated completed order where applicable       |

## Completed Sale Record

| Field         | Description                            |
| ------------- | -------------------------------------- |
| `eventId`     | Unique completed-sale event identifier |
| `orderId`     | Lightspeed order identifier            |
| `customerId`  | Customer account identifier            |
| `sku`         | Product sold                           |
| `quantity`    | Quantity sold                          |
| `completedAt` | Completed-sale timestamp               |
| `processedAt` | Middleware processing timestamp        |
| `status`      | Processing state                       |

## Reconciliation Record

| Field                   | Description                                    |
| ----------------------- | ---------------------------------------------- |
| `reconciliationId`      | Unique reconciliation identifier               |
| `sku`                   | Affected product                               |
| `zohoQuantity`          | Current Zoho quantity                          |
| `lastTrustedQuantity`   | Middleware trusted quantity                    |
| `reservedQuantity`      | Active reserved quantity                       |
| `completedSaleQuantity` | Relevant completed-sale quantity               |
| `expectedQuantity`      | Calculated expected quantity                   |
| `difference`            | Difference between expected and observed state |
| `status`                | Open, resolved, ignored                        |
| `createdAt`             | Detection timestamp                            |
| `resolvedAt`            | Resolution timestamp where applicable          |
| `resolvedBy`            | User or process responsible for resolution     |

## Inventory Event Record

| Field            | Description                                         |
| ---------------- | --------------------------------------------------- |
| `eventId`        | Unique event identifier                             |
| `eventType`      | Sync, reservation, sale, adjustment, reconciliation |
| `sku`            | Affected product                                    |
| `quantityBefore` | Previous quantity                                   |
| `quantityAfter`  | Updated quantity                                    |
| `quantityChange` | Net change                                          |
| `source`         | Zoho, Lightspeed, middleware, staff                 |
| `referenceId`    | Related order, reservation, or reconciliation ID    |
| `timestamp`      | Event timestamp                                     |

## Sync Status Values

* `current`
* `stale`
* `failed`
* `reconciling`

## Discrepancy Status Values

* `none`
* `open`
* `resolved`

## Data Rules

* Zoho quantity remains authoritative.
* Active reservations reduce web availability only.
* Completed sales decrement warehouse inventory.
* Duplicate completed-sale events shall not create duplicate decrements.
* Failed syncs preserve the last trusted quantity.
* Negative available web quantities are not permitted.
* Inventory-changing manual actions require audit records.
