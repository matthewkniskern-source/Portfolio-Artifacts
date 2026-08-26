# Functional Requirements

## Inventory Synchronization

**FR-01**
The middleware shall retrieve inventory availability from the Zoho mock API.

**FR-02**
The middleware shall synchronize inventory availability approximately every five minutes.

**FR-03**
The system shall store the timestamp of the most recent successful inventory synchronization.

**FR-04**
The system shall retain the last trusted inventory state if a synchronization attempt fails.

**FR-05**
The dashboard shall display synchronization failures and inventory discrepancies.

## Completed Sales

**FR-06**
The Lightspeed mock service shall generate a completed-sale event after successful checkout.

**FR-07**
The middleware shall process completed-sale events and identify the purchased SKU and quantity.

**FR-08**
The middleware shall decrement the corresponding Zoho inventory quantity after a confirmed completed sale.

**FR-09**
The system shall prevent duplicate processing of the same completed-sale event.

**FR-10**
Completed-sale processing shall generate an audit record.

## Cart Reservations

**FR-11**
The system shall create a temporary reservation when a customer begins checkout with available inventory.

**FR-12**
The reservation shall identify SKU, quantity, customer/session identifier, creation time, and expiration time.

**FR-13**
Reserved quantities shall reduce the quantity available for other web customers.

**FR-14**
Reservations shall expire automatically after approximately ten minutes if checkout is not completed.

**FR-15**
Expired reservations shall restore the reserved quantity to available web inventory.

**FR-16**
A completed sale shall close the associated reservation.

## Product Availability

**FR-17**
The storefront shall display an in-stock status for products above the configured low-stock threshold.

**FR-18**
The storefront shall display an exact remaining quantity for products at or below the low-stock threshold.

**FR-19**
The low-stock threshold shall be configurable.

**FR-20**
Products with no available inventory shall be unavailable for normal purchase unless configured as pre-order eligible.

**FR-21**
Pre-order eligible products shall display a distinct pre-order state.

## Out-of-Stock Lead Flow

**FR-22**
Out-of-stock product pages shall display contact options.

**FR-23**
The contact flow shall automatically include the relevant product name and SKU.

**FR-24**
The contact flow shall support email and phone contact options.

**FR-25**
The product page shall display relevant in-stock alternatives when available.

**FR-26**
Alternative products shall be sourced from available inventory and product metadata.

## Product Search and Catalog

**FR-27**
The storefront shall support product search by name.

**FR-28**
The storefront shall support search by SKU.

**FR-29**
The storefront shall support category-based browsing.

**FR-30**
Product listings shall support filtering by category.

**FR-31**
Product listings shall support filtering by application or use case.

**FR-32**
Product listings shall support compatibility-related keyword filtering.

**FR-33**
Product listings shall support filtering by brand.

**FR-34**
Product listings shall support filtering by relevant technical specifications.

**FR-35**
Product listings shall support sorting by relevant customer-facing criteria.

## Product Metadata

**FR-36**
The middleware shall support nightly synchronization of general product metadata.

**FR-37**
Staff shall be able to edit application notes.

**FR-38**
Staff shall be able to edit compatibility text.

**FR-39**
Staff shall be able to define or maintain related-product recommendations.

**FR-40**
Routine merchandising metadata changes shall not require detailed audit history.

## Customer Accounts and Reorder

**FR-41**
Customers shall be able to authenticate to a retail account.

**FR-42**
Authenticated customers shall be able to view prior eligible online purchases.

**FR-43**
Authenticated customers shall be able to initiate a reorder from prior purchases.

**FR-44**
Reorder actions shall validate current inventory before adding products to cart.

**FR-45**
Reorder actions shall use current Lightspeed retail pricing rather than historical order pricing.

## Internal Dashboard

**FR-46**
The dashboard shall support employee, manager, and owner roles.

**FR-47**
All authorized staff roles shall be able to view operational and business-intelligence metrics.

**FR-48**
Role permissions shall restrict system-changing actions.

**FR-49**
The dashboard shall display current synchronization status.

**FR-50**
The dashboard shall display active reservations.

**FR-51**
The dashboard shall display inventory discrepancies.

**FR-52**
The dashboard shall display recent completed-sale processing activity.

**FR-53**
The dashboard shall provide a reconciliation view for inventory-related events.

## Business Intelligence

**FR-54**
The dashboard shall display online sales trends.

**FR-55**
The dashboard shall display stockout frequency.

**FR-56**
The dashboard shall display abandoned or expired reservation trends.

**FR-57**
The dashboard shall display out-of-stock lead activity.

**FR-58**
The dashboard shall display frequently reordered products.

**FR-59**
The dashboard shall display product-level inventory trend indicators where data is available.

## Reconciliation

**FR-60**
The system shall compare Zoho inventory, active reservations, and processed completed sales.

**FR-61**
The system shall identify mismatched inventory states.

**FR-62**
The reconciliation view shall show the event sequence associated with a discrepancy.

**FR-63**
The system shall continue using the last trusted inventory state when a discrepancy cannot be resolved automatically.

**FR-64**
Unresolved discrepancies shall remain passively visible to authorized staff.

## Audit

**FR-65**
Inventory adjustments initiated by the system or staff shall generate audit records.

**FR-66**
Manual reconciliation actions shall generate audit records.

**FR-67**
System configuration changes affecting inventory or transaction processing shall generate audit records.

**FR-68**
Audit records shall include timestamp, actor or process, action type, affected object, and relevant before-and-after values.

## Mock Integration Layer

**FR-69**
The proof of concept shall expose mocked Zoho inventory endpoints.

**FR-70**
The proof of concept shall expose mocked Lightspeed commerce endpoints.

**FR-71**
Mock endpoints shall support representative success, failure, low-stock, out-of-stock, and discrepancy scenarios.

**FR-72**
Mock service interfaces shall be replaceable with production adapters without changing storefront business logic.

## Security Boundaries

**FR-73**
The middleware shall not store payment-card data.

**FR-74**
Payment processing shall remain within the Lightspeed commerce boundary.

**FR-75**
API credentials and secrets shall be externalized from application source code.

**FR-76**
Administrative functions shall require authenticated and authorized access.
