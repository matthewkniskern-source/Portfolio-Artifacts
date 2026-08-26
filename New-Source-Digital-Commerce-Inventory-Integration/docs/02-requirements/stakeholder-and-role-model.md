# Stakeholder and Role Model

## External Customers

### Retail Customer

* Browse and search public catalog
* View product availability
* Purchase through Lightspeed
* Maintain authenticated retail account
* View eligible prior purchases
* Reorder previously purchased products
* Use out-of-stock contact path
* View suggested alternatives

### Managed Commercial Customer

* Remains outside the public ecommerce workflow
* Works directly with New Source sales staff
* Negotiated pricing and account terms remain outside the proof-of-concept scope

## Internal Users

### Employee

**View**

* Inventory status
* Synchronization status
* Active reservations
* Inventory discrepancies
* Completed web-sale activity
* Reconciliation history
* Sales trends
* Stockout trends
* Reservation abandonment trends
* Out-of-stock lead activity
* Frequently reordered products

**Maintain**

* Application/use-case text
* Compatibility text
* Related-product recommendations

**Restricted**

* System configuration
* Role administration
* Inventory overrides
* Reconciliation resolution actions reserved for higher roles

### Manager

Includes employee capabilities plus:

* Investigate inventory discrepancies
* Perform authorized reconciliation actions
* Make approved inventory adjustments
* Configure merchandising controls
* Review audit records
* Manage operational configuration within assigned scope

### Owner / Administrator

Includes manager capabilities plus:

* Manage user roles and permissions
* Configure integration settings
* Configure synchronization intervals
* Configure reservation duration
* Configure low-stock thresholds
* Review system-wide audit history
* Access all dashboard and BI views
* Manage system-level operational settings

## System Actors

### Storefront

* Displays catalog and availability
* Initiates reservations
* Submits customer checkout activity to Lightspeed
* Displays customer account and reorder functions
* Routes out-of-stock inquiries

### Lightspeed

* Public retail price authority
* Cart and checkout
* Payment processing
* Completed-sale authority
* Customer online transaction history

### Middleware

* Coordinates storefront, Lightspeed, and Zoho
* Maintains reservation state
* Processes completed-sale events
* Executes inventory synchronization
* Performs reconciliation
* Stores custom product metadata
* Produces audit events
* Supplies operational and BI data

### Zoho Inventory

* Warehouse inventory authority
* Supplies available inventory quantities
* Receives confirmed inventory decrements after completed sales
* Supplies inventory data for reconciliation

### Scheduled Jobs

* Five-minute inventory polling
* Nightly product metadata synchronization
* Reconciliation processing

## Access Principle

Operational and business-intelligence visibility shall be broad across internal users.

System-changing authority shall be restricted by role.

## Role Matrix

| Capability                            | Employee | Manager | Owner / Admin |
| ------------------------------------- | -------: | ------: | ------------: |
| View operational dashboard            |      Yes |     Yes |           Yes |
| View BI metrics                       |      Yes |     Yes |           Yes |
| View inventory discrepancies          |      Yes |     Yes |           Yes |
| View reconciliation history           |      Yes |     Yes |           Yes |
| Maintain merchandising metadata       |      Yes |     Yes |           Yes |
| Resolve reconciliation exceptions     |       No |     Yes |           Yes |
| Make authorized inventory adjustments |       No |     Yes |           Yes |
| Review audit records                  |  Limited |     Yes |           Yes |
| Configure inventory thresholds        |       No |     Yes |           Yes |
| Configure integration settings        |       No |      No |           Yes |
| Manage roles and permissions          |       No |      No |           Yes |
| Manage system-wide configuration      |       No |      No |           Yes |
