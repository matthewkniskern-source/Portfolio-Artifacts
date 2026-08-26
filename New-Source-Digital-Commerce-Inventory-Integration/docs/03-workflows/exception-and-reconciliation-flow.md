# Exception and Reconciliation Flow

## Reconciliation Trigger

Scheduled reconciliation process
→ Compare Zoho inventory state
→ Compare active reservations
→ Compare completed Lightspeed sales
→ Compare local middleware event history

## No Discrepancy

Expected inventory matches Zoho
→ Reconciliation marked successful
→ Last trusted state maintained

## Discrepancy Detected

Expected inventory differs from Zoho
→ Discrepancy record created
→ Affected SKU identified
→ Relevant reservations associated
→ Relevant completed-sale events associated
→ Last trusted inventory state retained
→ Passive dashboard indicator displayed

## Traceability

Reconciliation view shall show:

* SKU
* Zoho quantity
* Last trusted quantity
* Active reserved quantity
* Completed-sale quantity
* Expected quantity
* Discrepancy amount
* Related event timestamps
* Related transaction identifiers
* Reconciliation status

## Automatic Resolution

Resolvable mismatch detected
→ Middleware recalculates expected state
→ Valid authoritative quantity confirmed
→ Local inventory state updated
→ Discrepancy closed
→ Resolution event recorded

## Manual Resolution

Discrepancy cannot be resolved automatically
→ Manager or owner reviews event history
→ Authorized adjustment or reconciliation action performed
→ Updated state validated
→ Discrepancy closed
→ Audit record created

## Integration Failure

Zoho or Lightspeed integration unavailable
→ Reconciliation attempt marked failed
→ Last trusted state retained
→ Storefront continues operating
→ Passive dashboard indicator remains visible

## Duplicate Event

Previously processed completed-sale event received again
→ Event identifier checked
→ Duplicate rejected
→ Inventory not decremented again
→ Duplicate event recorded

## Reservation Mismatch

Expired or completed reservation remains active
→ Reservation state corrected
→ Available web quantity recalculated
→ Reconciliation event recorded

## Audit

Manual inventory adjustments, reconciliation actions, and system-level corrections shall record:

* Timestamp
* User or process
* Action
* Affected SKU
* Previous value
* New value
* Related transaction or event identifier
