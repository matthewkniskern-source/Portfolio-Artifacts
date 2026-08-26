# Business Requirements

## Inventory Integration

**BR-01**
Zoho Inventory shall remain the authoritative source for warehouse inventory availability.

**BR-02**
The website shall retrieve inventory availability from Zoho on an approximately five-minute synchronization interval.

**BR-03**
Completed Lightspeed sales shall trigger an inventory decrement in Zoho for the confirmed quantities sold.

**BR-04**
The five-minute inventory synchronization process shall function primarily as a reconciliation mechanism rather than the primary sales-decrement mechanism.

**BR-05**
The system shall preserve the last trusted inventory state when a synchronization discrepancy occurs.

**BR-06**
Inventory discrepancies shall be visible to staff without automatically preventing continued web sales.

## Cart Reservation

**BR-07**
Adding an item to checkout shall create a temporary stock reservation.

**BR-08**
Temporary reservations shall expire after approximately ten minutes if the transaction is not completed.

**BR-09**
Expired reservations shall release the reserved quantity back to available web inventory.

**BR-10**
Reservation status shall not directly alter the authoritative Zoho quantity until a completed sale occurs.

## Inventory Presentation

**BR-11**
Products with normal availability shall display a general in-stock state rather than an exact quantity.

**BR-12**
Low-stock products shall display the remaining available quantity.

**BR-13**
Out-of-stock products shall not terminate the customer journey.

**BR-14**
Out-of-stock product pages shall provide a contact path tied automatically to the specific product.

**BR-15**
Out-of-stock pages shall present relevant in-stock alternatives through a “Customers Also Chose” section.

**BR-16**
Existing pre-order eligible products shall remain distinguishable from standard out-of-stock products.

## Commerce

**BR-17**
Lightspeed shall remain the authoritative source for public retail pricing, checkout, payment processing, and completed online transactions.

**BR-18**
The middleware shall not store or process payment-card data.

**BR-19**
Managed commercial accounts and negotiated pricing shall remain outside the public ecommerce workflow.

**BR-20**
Returning retail customers shall have an authenticated account-based reorder path.

## Product Data

**BR-21**
General product metadata shall synchronize on a scheduled nightly basis where appropriate.

**BR-22**
Application and compatibility information shall be maintained as descriptive product metadata rather than enforced relational compatibility rules.

**BR-23**
Staff shall be able to maintain application, compatibility, and related-product information through the middleware administration layer.

## Catalog and Customer Flow

**BR-24**
Search and category navigation shall receive approximately equal prominence within the storefront.

**BR-25**
Product listing pages shall use a cleaner grid/list hybrid optimized for professional buyers.

**BR-26**
Catalog filtering shall prioritize:

1. Category
2. Application / use case
3. Compatibility
4. Brand
5. Product specifications

**BR-27**
Product discovery features shall support, rather than replace, direct product and SKU retrieval.

## Middleware

**BR-28**
A middleware layer shall coordinate communication between the storefront, Lightspeed, and Zoho.

**BR-29**
The initial proof of concept shall use mocked Zoho and Lightspeed API endpoints.

**BR-30**
Integration services shall be designed so mocked adapters can later be replaced with production API connectors without redesigning the application.

**BR-31**
The middleware shall support inventory synchronization, reservation management, reconciliation, custom product metadata, audit events, and reporting.

## Dashboard and Reporting

**BR-32**
The system shall provide an internal dashboard for employees, managers, and owners.

**BR-33**
Business intelligence and operational trends shall be broadly visible across staff roles.

**BR-34**
Role-based access controls shall govern which users may perform administrative or system-changing actions.

**BR-35**
The dashboard shall provide inventory discrepancy and reconciliation visibility.

**BR-36**
Staff shall be able to trace inventory state across Zoho quantity, web reservations, completed Lightspeed sales, and reconciliation activity.

**BR-37**
Dashboard discrepancies and system conditions shall use passive indicators in the initial implementation.

## Audit and Traceability

**BR-38**
Inventory-changing actions shall generate auditable records.

**BR-39**
System configuration and reconciliation actions shall generate auditable records.

**BR-40**
Audit records shall identify the action, timestamp, responsible user or process, and relevant before-and-after state where applicable.

**BR-41**
Routine merchandising text changes shall not require the same audit depth as inventory or system actions.

## User Interface

**BR-42**
The existing New Source site-wide animated header/background treatment shall be retained across the storefront.

**BR-43**
The redesigned interface shall improve visual hierarchy without relying heavily on oversized category imagery.

**BR-44**
Product imagery shall carry greater visual emphasis on product listing and product-detail pages than on top-level category navigation.

## Proof of Concept

**BR-45**
The solution shall be implemented as a working proof of concept suitable for public portfolio presentation.

**BR-46**
The proof of concept shall use sample or synthetic data and shall not require production customer, payment, or credential data.

**BR-47**
The proof of concept shall demonstrate the major target-state workflows, including inventory synchronization, reservations, completed-sale decrement, reconciliation, out-of-stock lead routing, reorder behavior, and internal dashboard visibility.

