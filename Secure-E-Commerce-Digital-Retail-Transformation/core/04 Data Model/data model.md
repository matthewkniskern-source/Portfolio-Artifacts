# Data Model

## 1. Purpose

The data model defines the core business entities required to support the One-Punch Anime Emporium digital retail environment.

The academic website may use static or mock data rather than a live relational database. The model is therefore a future-state design artifact intended to show how customer, product, inventory, order, employee, supplier, and payment-reference data could be structured in a production implementation.

The model is intentionally limited to the entities required by the project. It is not intended to reproduce a full ERP, point-of-sale, warehouse, or accounting system.

---

## 2. Core Modeling Principles

The model follows several practical rules.

### Separate Products from Inventory

A product describes what the retailer sells.

Inventory describes where that product is available and in what quantity.

Because One-Punch Anime Emporium operates multiple stores, inventory cannot be stored as a single quantity on the Product record.

The core relationship is:

```text
Store + Product → Inventory
```

### Preserve Transaction History

Order records should preserve what occurred at the time of purchase.

For example, the price stored on an Order Item should represent the price actually charged for that transaction rather than relying on the current Product price.

### Minimize Sensitive Data

The proposed design should not store raw payment-card data.

Payment records should contain only the references and status information required to reconcile an order with an external payment provider.

### Support Future Growth Without Overbuilding

The model supports multiple stores, products, suppliers, employees, and orders while avoiding unrelated retail functions that are outside the project scope.

---

# 3. Conceptual Data Model

```text
ProductCategory
      1
      │
      └────< Product
                │
                │
                ├────< Inventory >──── Store
                │
                │
                ├────< OrderItem >──── Order >──── Customer
                │                         │
                │                         └────< PaymentReference
                │
                └────< ProductSupplier >──── Supplier


Customer
   │
   └────< SpecialOrderRequest


Employee
   │
   └────< EmployeeRole >──── Role
```

The model may later be expanded where implementation decisions create a legitimate need, but the current structure supports the primary project workflows.

---

# 4. Entity Overview

| Entity              | Purpose                                                                                |
| ------------------- | -------------------------------------------------------------------------------------- |
| Customer            | Represents a customer account or identifiable customer involved in an order or request |
| Product             | Represents merchandise offered or recognized by the retailer                           |
| ProductCategory     | Groups products into meaningful catalog categories                                     |
| Store               | Represents a physical retail location                                                  |
| Inventory           | Associates a product with a store and records location-specific availability           |
| Order               | Represents a customer purchase transaction                                             |
| OrderItem           | Represents individual products and quantities included in an order                     |
| PaymentReference    | Associates an order with an external payment-provider transaction or token/reference   |
| SpecialOrderRequest | Records a customer request for unavailable or specialty merchandise                    |
| Employee            | Represents a staff member requiring system access                                      |
| Role                | Defines a logical business or system-access role                                       |
| EmployeeRole        | Associates employees with one or more roles                                            |
| Supplier            | Represents a vendor or distributor capable of sourcing merchandise                     |
| ProductSupplier     | Associates products with one or more suppliers                                         |

---

# 5. Entity Definitions

## 5.1 Customer

Represents an identifiable customer using account, order, or special-order functionality.

```text
Customer
--------
CustomerID          PK
FirstName
LastName
Email
Phone
AccountStatus
CreatedDate
UpdatedDate
```

A production design may separate authentication credentials from the Customer entity and rely on an external identity provider or dedicated authentication service.

Sensitive authentication data should not be stored directly in this business table.

---

## 5.2 ProductCategory

Provides a controlled classification structure for products.

```text
ProductCategory
---------------
CategoryID          PK
CategoryName
Description
CategoryStatus
```

Example categories may include:

* Manga
* Comics
* Figures
* Collectibles
* Apparel
* Accessories

Categories should support customer browsing and administrative organization without becoming unnecessarily granular.

---

## 5.3 Product

Represents a product recognized by the retailer.

```text
Product
-------
ProductID           PK
CategoryID          FK
SKU
ProductName
Description
CurrentPrice
ProductStatus
ImageReference
CreatedDate
UpdatedDate
```

`CurrentPrice` represents the current catalog price.

Historical transaction pricing is preserved separately on OrderItem.

`ProductStatus` may include values such as:

* Active
* Inactive
* Discontinued

Inventory availability is not stored on Product.

---

## 5.4 Store

Represents a physical One-Punch Anime Emporium location.

```text
Store
-----
StoreID             PK
StoreName
AddressLine1
AddressLine2
City
State
PostalCode
Phone
StoreStatus
```

Each physical location maintains its own inventory relationship with products.

---

## 5.5 Inventory

Represents the availability of a specific product at a specific store.

```text
Inventory
---------
InventoryID         PK
StoreID             FK
ProductID           FK
QuantityOnHand
QuantityReserved
AvailabilityStatus
LastUpdated
```

The pair:

```text
StoreID + ProductID
```

must be unique.

This prevents multiple active inventory records from representing the same product at the same store.

Possible availability states include:

* In Stock
* Low Stock
* Out of Stock
* Backordered
* Unknown

The exact customer-facing availability logic may later be derived from quantities rather than stored directly.

---

# 6. Customer Orders

## 6.1 Order

Represents a customer purchase.

```text
Order
-----
OrderID             PK
CustomerID          FK NULL
OrderDate
OrderStatus
FulfillmentMethod
FulfillmentStoreID  FK NULL
Subtotal
TaxAmount
ShippingAmount
OrderTotal
CreatedDate
UpdatedDate
```

`CustomerID` may be nullable if guest checkout is supported.

`FulfillmentMethod` may support values such as:

* Store Pickup
* Shipping

`FulfillmentStoreID` is relevant where a physical store is responsible for pickup or fulfillment.

Order status values may include:

* Pending
* Awaiting Payment
* Paid
* Processing
* Ready for Pickup
* Shipped
* Completed
* Cancelled
* Failed

Detailed status transitions are defined in the E-Commerce Workflows section.

---

## 6.2 OrderItem

Represents an individual product line within an order.

```text
OrderItem
---------
OrderItemID         PK
OrderID             FK
ProductID           FK
Quantity
UnitPrice
LineTotal
```

`UnitPrice` stores the price used when the order was created.

This protects transaction history if the current catalog price later changes.

A valid OrderItem must reference both an existing Order and Product.

---

# 7. Payment Reference

## 7.1 PaymentReference

Represents the retailer-side reference to payment activity performed by an external payment provider.

```text
PaymentReference
----------------
PaymentReferenceID  PK
OrderID             FK
ProviderReference
PaymentStatus
AuthorizedAmount
TransactionDate
LastUpdated
```

Possible payment states may include:

* Initiated
* Authorized
* Declined
* Cancelled
* Refunded
* Partially Refunded

The retailer-side record should not contain:

* full primary account number;
* CVV/CVC;
* magnetic-stripe data;
* PIN information;
* other sensitive authentication data.

The purpose of this entity is reconciliation, not payment-card storage.

Detailed payment scope and trust boundaries are defined in the Payment Architecture and PCI Scope section.

---

# 8. Special Orders

## 8.1 SpecialOrderRequest

Represents a request for merchandise that is unavailable or may not yet exist in the normal product catalog.

```text
SpecialOrderRequest
-------------------
SpecialOrderRequestID   PK
CustomerID              FK NULL
ProductID               FK NULL
CustomerName
CustomerEmail
CustomerPhone
RequestedItemDescription
RequestedQuantity
RequestStatus
QuotedPrice
CustomerApprovalStatus
AssignedEmployeeID      FK NULL
SupplierID              FK NULL
SubmittedDate
UpdatedDate
```

`ProductID` is nullable intentionally.

A customer may request a rare or specialty item that has not yet been entered into the retailer's product catalog.

Likewise, a supplier may not be identified when the request is first submitted.

Possible request states include:

* Submitted
* Under Review
* Supplier Inquiry
* Awaiting Customer Approval
* Approved
* Ordered
* Unable to Source
* Cancelled
* Completed

The detailed lifecycle is maintained in the Special Order workflow rather than duplicated here.

---

# 9. Employees and Access Roles

## 9.1 Employee

Represents an employee who may require access to administrative functions.

```text
Employee
--------
EmployeeID          PK
StoreID             FK NULL
FirstName
LastName
Email
EmploymentStatus
CreatedDate
UpdatedDate
```

An employee may be assigned primarily to a store or may operate across multiple locations.

If multi-store employee assignment becomes necessary, a separate EmployeeStore relationship can be introduced rather than overloading this table.

---

## 9.2 Role

Defines an access or business responsibility grouping.

```text
Role
----
RoleID              PK
RoleName
Description
RoleStatus
```

Potential roles include:

* Sales Associate
* Store Manager
* Inventory Manager
* E-Commerce Administrator
* System Administrator
* Auditor / Read-Only Reviewer

Detailed permissions are maintained in the Security and Access Control section.

---

## 9.3 EmployeeRole

Supports the many-to-many relationship between employees and roles.

```text
EmployeeRole
------------
EmployeeRoleID      PK
EmployeeID          FK
RoleID              FK
AssignedDate
ActiveStatus
```

The pair:

```text
EmployeeID + RoleID
```

should be unique for active assignments.

This allows one employee to hold multiple responsibilities without duplicating employee records.

---

# 10. Suppliers

## 10.1 Supplier

Represents a vendor, distributor, or other source from which merchandise may be obtained.

```text
Supplier
--------
SupplierID          PK
SupplierName
ContactName
Email
Phone
SupplierStatus
```

Supplier information is intended for internal operational use.

---

## 10.2 ProductSupplier

Supports the many-to-many relationship between products and suppliers.

```text
ProductSupplier
---------------
ProductSupplierID   PK
ProductID           FK
SupplierID          FK
SupplierSKU
UnitCost
TypicalLeadTimeDays
PreferredSupplier
SupplierProductStatus
```

A single product may be available through multiple suppliers.

Likewise, one supplier may provide many products.

The pair:

```text
ProductID + SupplierID
```

should be unique unless the business has a valid reason to maintain multiple supplier relationships for the same product.

---

# 11. Primary Relationships

| Parent          | Relationship | Child               | Purpose                                             |
| --------------- | ------------ | ------------------- | --------------------------------------------------- |
| ProductCategory | 1:M          | Product             | One category contains many products                 |
| Product         | 1:M          | Inventory           | A product may exist at multiple stores              |
| Store           | 1:M          | Inventory           | A store may hold many products                      |
| Customer        | 1:M          | Order               | A customer may place multiple orders                |
| Order           | 1:M          | OrderItem           | An order contains one or more line items            |
| Product         | 1:M          | OrderItem           | A product may appear in many orders                 |
| Order           | 1:M          | PaymentReference    | An order may generate multiple payment events       |
| Customer        | 1:M          | SpecialOrderRequest | A customer may submit multiple requests             |
| Employee        | 1:M          | EmployeeRole        | An employee may hold multiple roles                 |
| Role            | 1:M          | EmployeeRole        | A role may be assigned to many employees            |
| Product         | 1:M          | ProductSupplier     | A product may be sourced through multiple suppliers |
| Supplier        | 1:M          | ProductSupplier     | A supplier may provide multiple products            |

Together, `Inventory`, `OrderItem`, `EmployeeRole`, and `ProductSupplier` resolve the primary many-to-many relationships in the model.

---

# 12. Data Integrity Rules

The proposed model should enforce the following rules.

### Products and Inventory

* each Product must belong to a valid ProductCategory;
* each Inventory record must reference a valid Store and Product;
* duplicate Store/Product inventory relationships should not be permitted;
* inventory quantities should not accept invalid negative values unless a defined business process explicitly permits them;
* inactive or discontinued products should not automatically be represented as available for sale.

### Orders

* an OrderItem cannot exist without a valid Order;
* an OrderItem must reference a valid Product;
* ordered quantities must be greater than zero;
* unit price must represent the transaction price used when the order was created;
* an order should not be represented as paid unless the associated payment state supports that conclusion;
* order totals should reconcile to their component amounts.

### Special Orders

* a request must contain enough information to identify the requested merchandise;
* a request must contain a usable customer-contact method;
* ProductID may be null when the requested item does not yet exist in the catalog;
* supplier assignment may remain null until sourcing begins;
* status changes should follow the defined special-order workflow.

### Access Data

* an EmployeeRole must reference an existing Employee and Role;
* duplicate active employee/role assignments should not be created;
* inactive employees should not retain active system access.

---

# 13. Normalization Rationale

The core model is intended to approximate third normal form without pursuing normalization for its own sake.

Separate entities are used where independent business concepts have different lifecycles or where duplication would create avoidable integrity problems.

Examples include:

### Store and Product

Product information is stored once in Product.

Location-specific stock is stored in Inventory.

Without the Inventory entity, the business would either need to duplicate Product records by store or add store-specific quantity columns to Product, both of which would scale poorly.

### Order and Product

The OrderItem entity resolves the many-to-many relationship between orders and products.

It also preserves transaction-specific information such as quantity and unit price.

### Product and Supplier

ProductSupplier allows a product to be sourced through more than one supplier without duplicating product information.

### Employee and Role

EmployeeRole allows multiple role assignments while keeping employee and role definitions independent.

The model intentionally allows limited denormalization where transaction history or practical operation requires it, such as storing UnitPrice on OrderItem.

---

# 14. Data Ownership and Classification Considerations

The model contains data with different operational and security requirements.

| Data Area           | Examples                                                       | General Handling                         |
| ------------------- | -------------------------------------------------------------- | ---------------------------------------- |
| Public Catalog Data | Product names, descriptions, prices, store locations           | Customer-facing                          |
| Operational Data    | Inventory quantities, supplier information, fulfillment status | Restricted to appropriate staff          |
| Customer Data       | Name, email, phone, address, order history                     | Protected business information           |
| Employee Data       | Name, email, role assignments                                  | Restricted internal information          |
| Transaction Data    | Orders, totals, payment status                                 | Restricted business/customer information |
| Payment References  | Provider transaction IDs, payment status                       | Restricted; no raw cardholder data       |

Detailed retention, privacy, and employee-access rules are maintained in the Privacy and Data Governance section.

---

# 15. Retention Considerations

Retention periods are not defined here as legal requirements.

Instead, the design recognizes that different data types may require different retention decisions.

Examples include:

* active product and store information may remain while operationally relevant;
* inventory records require current-state accuracy and may also generate historical records where reporting requires them;
* completed orders may need to be retained for business, customer-service, accounting, or dispute purposes;
* customer account information should not be retained indefinitely without a business need;
* failed or abandoned special-order requests may require shorter retention than completed transactions;
* payment references should be retained only as long as required for legitimate reconciliation, refund, or business-record purposes;
* obsolete employee access relationships should be disabled or removed according to access-governance procedures.

Specific retention expectations are addressed separately in the Privacy and Data Governance section.

---

# 16. Academic Implementation Boundary

The academic website is not required to operate this data model as a live production database.

The site may demonstrate product, inventory, cart, and other functionality using:

* static files;
* mock JSON data;
* browser-side storage;
* simulated transaction data.

Those implementation choices should not be confused with the proposed production data architecture.

The relational model documents how the underlying business information could be structured if the retailer moved from the demonstration website into an integrated e-commerce environment.

---

# 17. Model Extension Points

Several additional entities could become appropriate if project scope expands.

Examples include:

* EmployeeStore
* Address
* Shipment
* Return
* Refund
* Promotion
* PurchaseOrder
* InventoryTransaction
* AuditEvent

These entities are intentionally excluded from the current model because the case study does not yet require them.

The design should be extended when a documented business requirement creates the need, rather than adding structures simply to make the model appear more complex.

