# Payment Boundary

## Payment Authority

Lightspeed remains responsible for:

* Checkout
* Payment authorization
* Payment processing
* Payment confirmation
* Completed online transaction status

## Middleware Exclusion

The middleware shall not store or process:

* Payment-card numbers
* CVV data
* Raw payment credentials
* Payment authentication secrets
* Full cardholder data

## Allowed Transaction Data

The middleware may receive:

* Order ID
* Event ID
* Customer account ID
* SKU
* Quantity
* Transaction status
* Completion timestamp
* Payment success / failure state

## Transaction Flow

```text id="x7cw23"
Customer
   │
   ▼
Storefront
   │
   ▼
Lightspeed Checkout
   │
   ▼
Payment Processor
   │
   ▼
Completed Sale
   │
   ▼
Middleware
```

## Completed Sale Handling

Completed transaction confirmed
→ Middleware receives sale event
→ Event validated
→ Duplicate event check performed
→ Reservation closed
→ Zoho inventory decrement submitted
→ Audit record created

## Failed Payment

Payment not completed
→ No inventory decrement
→ Reservation remains active until expiration or release
→ Customer may retry checkout within reservation window

## PCI Scope Reduction

The custom middleware should remain outside the cardholder-data environment wherever possible.

Payment entry and processing should remain within Lightspeed or its designated payment-processing components.

## Logging

Payment-related middleware logs may contain:

* Order ID
* Transaction status
* Timestamp
* Processing result

Logs shall not contain:

* Full card number
* CVV
* Payment tokens not intended for application logging
* Authentication secrets

## Production Integration Principle

Future production integration should consume transaction-status events only after Lightspeed has completed payment processing.

The middleware should not intercept or proxy customer payment-card data.
