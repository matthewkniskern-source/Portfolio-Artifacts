# Current Order Flow

## Website Order

Customer
→ Searches or browses catalog
→ Selects product
→ Adds product to cart
→ Proceeds through Lightspeed checkout
→ Payment completed
→ Order confirmation generated
→ New Source receives order notification
→ Staff reviews order
→ Staff verifies fulfillment requirements
→ Staff handles internal fulfillment manually

## Phone Order

Customer calls New Source
→ Clerk identifies requested product
→ Clerk searches Zoho Inventory
→ Confirms available quantity
→ Clerk builds sales ticket
→ Payment / account handling completed
→ Order proceeds to fulfillment

## Current Inventory Dependency

Website sale
→ Does not directly decrement Zoho inventory
→ Staff must reconcile inventory separately

Phone sale
→ Staff checks Zoho before completing order
→ Inventory handling remains tied to internal staff process

## Current Control Points

* Product availability displayed on website
* Zoho inventory lookup for phone orders
* Lightspeed checkout for web orders
* Manual staff review after online purchase
* Manual inventory reconciliation

## Current Failure Opportunities

* Website stock may not match Zoho
* Web customer may purchase inventory no longer available
* Completed web sale may not be reflected in Zoho immediately
* Staff may need to resolve discrepancies manually
* Order handling depends on email/manual handoff
* Customer receives limited visibility into fulfillment state
