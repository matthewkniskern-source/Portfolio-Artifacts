# Inventory Sync Flow

## Scheduled Inventory Poll

Scheduler
→ Triggers approximately every 5 minutes
→ Middleware requests current inventory from Zoho
→ Response received
→ Inventory records validated
→ Last successful sync timestamp updated
→ Storefront availability refreshed

## Successful Sync

Zoho quantity received
→ Active web reservations subtracted
→ Available web quantity calculated
→ Product availability state updated

## Availability States

Available quantity above low-stock threshold
→ Display **In Stock**

Available quantity at or below low-stock threshold
→ Display exact remaining quantity

Available quantity equals zero
→ Disable standard purchase
→ Enable product-specific contact flow
→ Display in-stock alternatives

Pre-order eligible
→ Display distinct pre-order state

## Sync Failure

Zoho request fails
→ Existing inventory state preserved
→ Last trusted quantity remains active
→ Failure recorded
→ Passive dashboard indicator displayed
→ Storefront remains operational

## Inventory Discrepancy

Zoho quantity differs from expected inventory state
→ Discrepancy record created
→ Relevant reservation and sale events associated
→ Last trusted state retained
→ Dashboard reconciliation view updated

## Completed Sale Interaction

Lightspeed confirms completed sale
→ Middleware processes sale event immediately
→ Associated reservation closed
→ Zoho decrement submitted
→ Local inventory state updated
→ Audit event recorded

The scheduled 5-minute poll remains a reconciliation mechanism and does not replace completed-sale processing.

## Nightly Metadata Sync

Scheduled after business hours
→ Retrieve configured product metadata
→ Validate product identifiers
→ Update applicable catalog metadata
→ Preserve Lightspeed pricing authority
→ Record synchronization status
