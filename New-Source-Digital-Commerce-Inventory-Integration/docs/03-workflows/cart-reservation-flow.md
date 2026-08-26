# Cart Reservation Flow

## Reservation Creation

Customer adds eligible product to cart
→ Storefront requests reservation
→ Middleware checks available web quantity
→ Reservation created
→ Reserved quantity removed from web availability
→ 10-minute expiration timer begins

## Reservation Record

Each reservation stores:

* Reservation ID
* Customer or session identifier
* SKU
* Quantity
* Creation timestamp
* Expiration timestamp
* Reservation status

## Active Reservation

Reservation active
→ Quantity remains unavailable to other web customers
→ Customer may continue checkout
→ Zoho authoritative quantity remains unchanged

## Completed Checkout

Lightspeed confirms completed sale
→ Middleware identifies associated reservation
→ Reservation marked completed
→ Zoho inventory decrement submitted
→ Local availability recalculated
→ Audit event recorded

## Expired Reservation

10-minute timer expires
→ Reservation marked expired
→ Reserved quantity released
→ Web availability recalculated
→ Cart item removed or marked unavailable

## Insufficient Inventory

Requested quantity exceeds available web quantity
→ Reservation denied
→ Customer notified of current availability
→ Cart quantity adjusted or purchase prevented

## Concurrent Requests

Multiple customers request the same limited inventory
→ Reservation requests evaluated against current available web quantity
→ First valid reservations reduce available quantity
→ Later requests cannot reserve already committed stock

## Reservation Failure

Reservation service fails
→ Purchase flow does not assume inventory is reserved
→ Customer receives a controlled availability message
→ Failure recorded for staff visibility
