# Audit and Traceability

## Audited Actions

Audit records are required for:

* Inventory adjustments
* Completed-sale inventory decrements
* Manual reconciliation actions
* System-driven reconciliation corrections
* Reservation state changes affecting inventory availability
* Role and permission changes
* Integration configuration changes
* Inventory threshold changes
* System-control changes

## Non-Audited Routine Content Changes

Full audit history is not required for:

* Application text
* Compatibility text
* Merchandising tags
* Related-product descriptions
* Routine product presentation changes

## Audit Record

| Field         | Description                                                 |
| ------------- | ----------------------------------------------------------- |
| `auditId`     | Unique audit identifier                                     |
| `timestamp`   | Event timestamp                                             |
| `actor`       | User or system process                                      |
| `role`        | Actor role where applicable                                 |
| `action`      | Action performed                                            |
| `objectType`  | Inventory, reservation, reconciliation, configuration, role |
| `objectId`    | Affected SKU, reservation, user, or record                  |
| `beforeValue` | Previous value where applicable                             |
| `afterValue`  | New value where applicable                                  |
| `referenceId` | Related order, event, reservation, or reconciliation ID     |
| `result`      | Success, failed, rejected                                   |
| `notes`       | Optional resolution or context                              |

## Inventory Traceability

For any SKU, staff should be able to trace:

```text
Zoho Quantity
→ Inventory Sync
→ Reservation Activity
→ Completed Sale
→ Inventory Decrement
→ Reconciliation
→ Current State
```

## Transaction Traceability

Completed-sale processing shall preserve:

* Lightspeed order ID
* Completed-sale event ID
* Customer account ID where applicable
* Purchased SKU
* Quantity
* Related reservation ID
* Zoho update result
* Processing timestamp

## Reservation Traceability

Reservation history shall preserve:

* Reservation ID
* SKU
* Quantity
* Customer or session ID
* Creation time
* Expiration time
* Completion or release time
* Final status
* Related order ID where applicable

## Reconciliation Traceability

Each discrepancy shall retain:

* Reconciliation ID
* Affected SKU
* Zoho quantity
* Last trusted quantity
* Reserved quantity
* Relevant completed sales
* Expected quantity
* Difference
* Detection timestamp
* Resolution action
* Resolving user or process
* Resolution timestamp

## Duplicate Event Handling

Completed-sale event IDs shall be checked before processing.

Previously processed event
→ Reject duplicate
→ Do not decrement inventory
→ Record duplicate event result

## Manual Adjustment

Authorized user performs inventory-related correction
→ Capture before state
→ Apply change
→ Capture after state
→ Record user
→ Record timestamp
→ Record reason / reference

## Failed Actions

Failed inventory or system actions shall record:

* Attempted action
* Actor or process
* Affected object
* Timestamp
* Failure result
* Reference identifier where available

## Dashboard Access

Authorized staff may view traceability records.

Action permissions remain role-based.

## Retention

Audit and reconciliation records shall be retained long enough to support:

* Inventory investigation
* Transaction review
* Operational troubleshooting
* Proof-of-concept validation
* Future production governance requirements
