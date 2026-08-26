# Out-of-Stock Lead Flow

## Trigger

Available web quantity reaches zero
→ Standard purchase disabled
→ Product page remains active

## Customer Options

Out-of-stock product page displays:

* Product name
* SKU
* Out-of-stock status
* Email contact option
* Phone contact option
* “Customers Also Chose” alternatives

## Email Inquiry

Customer selects email contact
→ Product name and SKU inserted automatically
→ Customer enters contact information and message
→ Inquiry submitted
→ Lead record created
→ Staff receives product-specific inquiry

## Phone Inquiry

Customer selects phone contact
→ Product context remains visible
→ Customer contacts New Source directly
→ Staff can reference displayed product name and SKU

## Alternative Products

System identifies relevant products using:

* Category
* Application/use-case metadata
* Compatibility text
* Brand
* Available inventory

Only currently available alternatives are displayed.

## Lead Record

Lead record stores:

* Lead ID
* Product name
* SKU
* Customer contact information when provided
* Inquiry method
* Timestamp
* Lead status

## Pre-Order Exception

Product configured as pre-order eligible
→ Standard out-of-stock lead flow does not replace pre-order behavior
→ Pre-order option remains available
