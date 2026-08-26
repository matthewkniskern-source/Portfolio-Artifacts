# Target Order Flow

## Website Order

Customer
→ Searches or browses catalog
→ Selects product
→ Website checks current available inventory
→ Customer adds item to cart
→ 10-minute reservation created
→ Customer proceeds to Lightspeed checkout
→ Payment completed
→ Lightspeed confirms completed sale
→ Middleware closes reservation
→ Middleware decrements Zoho inventory
→ Audit event recorded
→ Order proceeds to fulfillment

## Reservation Expiration

Customer adds item to cart
→ Reservation created
→ Checkout not completed within 10 minutes
→ Reservation expires
→ Reserved quantity released
→ Web availability recalculated
→ Cart item removed or marked unavailable

## Low Inventory

Product availability reaches configured threshold
→ Website displays exact remaining quantity
→ Customer may continue normal purchase flow

## Out of Stock

Product availability reaches zero
→ Standard purchase disabled
→ Product-specific contact options displayed
→ Email or phone inquiry path offered
→ Product name and SKU carried into inquiry
→ In-stock alternatives displayed under “Customers Also Chose”

## Pre-Order

Product configured as pre-order eligible
→ Pre-order state displayed
→ Customer follows existing pre-order purchase path
→ Product remains distinct from standard out-of-stock workflow

## Reorder

Authenticated customer
→ Opens prior online purchase history
→ Selects eligible product for reorder
→ Current inventory checked
→ Current Lightspeed price applied
→ Product added to cart
→ Standard reservation and checkout flow begins

## Integration Failure

Inventory synchronization fails
→ Last trusted inventory state retained
→ Storefront continues operating
→ Dashboard displays passive discrepancy indicator
→ Reconciliation process records mismatch for staff review
