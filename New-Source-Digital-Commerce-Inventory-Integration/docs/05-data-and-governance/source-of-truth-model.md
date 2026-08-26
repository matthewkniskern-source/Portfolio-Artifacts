# Source of Truth Model

## System Authority

| Data Domain                   | Source of Truth          |
| ----------------------------- | ------------------------ |
| Warehouse inventory quantity  | Zoho Inventory           |
| Public retail pricing         | Lightspeed               |
| Checkout                      | Lightspeed               |
| Payment processing            | Lightspeed               |
| Completed online sale         | Lightspeed               |
| Temporary cart reservation    | Middleware               |
| Calculated web availability   | Middleware               |
| Reconciliation state          | Middleware               |
| Custom application metadata   | Middleware               |
| Custom compatibility text     | Middleware               |
| Related-product configuration | Middleware               |
| Audit history                 | Middleware               |
| BI aggregation                | Middleware               |
| Managed commercial pricing    | Outside public web scope |

## Inventory Quantity

Zoho Inventory owns warehouse quantity.

The middleware may:

* Read current quantity
* Calculate available web quantity
* Apply temporary reservations
* Submit confirmed sale decrements
* Flag discrepancies

The middleware shall not independently redefine authoritative warehouse inventory.

## Web Availability

```text
Zoho Quantity
-
Active Reservations
=
Available Web Quantity
```

Available web quantity is operational state, not warehouse truth.

## Completed Sales

Lightspeed owns completed online transaction status.

A completed sale may trigger:

* Reservation completion
* Zoho inventory decrement
* Reconciliation event
* Audit event
* Analytics update

## Pricing

Lightspeed owns current public retail pricing.

The middleware may read price for:

* Product display
* Reorder validation
* Related-product presentation

The middleware shall not override public retail price.

## Reservations

The middleware owns temporary reservation state.

Reservation status values:

* Active
* Completed
* Expired
* Released
* Failed

Reservations do not alter Zoho warehouse quantity until a completed sale is confirmed.

## Product Metadata

Middleware-managed metadata may include:

* Application / use case
* Compatibility text
* Related products
* Supplemental technical notes
* Merchandising attributes

These fields supplement vendor-system data and do not override inventory or pricing authority.

## Reconciliation

The middleware compares:

* Zoho warehouse quantity
* Last trusted quantity
* Active reservations
* Completed Lightspeed sales
* Inventory-affecting middleware events

Zoho remains authoritative unless an authorized manual correction is performed against the inventory system itself.

## Failure State

If a source system becomes temporarily unavailable:

* Last trusted data remains active where appropriate
* Current state is marked stale
* Passive discrepancy indicator is displayed
* System does not silently assign authority to another source

## Authority Principle

No data domain should have competing sources of truth.

Where multiple systems contain similar data, one system remains authoritative and the others consume, calculate, or reconcile against it.
