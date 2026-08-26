# Problem Statement

New Source currently operates its public ecommerce channel and warehouse inventory process across separate systems.

Zoho Inventory is used for warehouse stock tracking, while Lightspeed manages public retail pricing, checkout, payment processing, and completed online transactions.

Website inventory availability is maintained manually, and completed web orders are handled through a manual internal handoff.

## Primary Issues

* Website inventory can fall out of sync with Zoho.
* Staff must maintain inventory information across multiple systems.
* Completed online sales do not automatically decrement Zoho inventory.
* Cart activity does not reserve stock.
* Inventory discrepancies require manual investigation.
* Current workflows provide limited transaction-to-inventory traceability.
* Out-of-stock products can end the customer purchase path rather than generating a sales opportunity.
* Repeat customers lack a streamlined reorder path.
* Product discovery and filtering can be improved for professional buyers.

## Target Condition

* Zoho remains the inventory source of truth.
* Lightspeed remains the fiscal and ecommerce source of truth.
* A middleware layer coordinates inventory, reservations, reconciliation, custom product metadata, and reporting.
* Website inventory reflects Zoho availability on a short synchronization interval.
* Completed Lightspeed sales trigger inventory decrement in Zoho.
* Cart inventory is temporarily reserved during checkout.
* Inventory discrepancies remain visible and traceable without automatically stopping sales.
* Out-of-stock products route customers toward direct contact and available alternatives.
* Returning customers gain an account-based reorder path.
* Staff gain operational and business-intelligence visibility through a shared dashboard.

