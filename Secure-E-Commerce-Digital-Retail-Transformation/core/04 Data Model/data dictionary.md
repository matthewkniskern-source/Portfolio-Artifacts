# Data Dictionary

## 1. Purpose

This data dictionary defines the proposed fields used by the One-Punch Anime Emporium future-state relational data model.

It supports the logical model documented in `data model.md` and provides a consistent reference for:

* field purpose;
* key relationships;
* expected data type;
* nullability;
* validation expectations;
* basic integrity rules.

The academic website may use static or mock data rather than a live database. These definitions therefore represent the proposed production data structure rather than a claim of implemented database functionality.

---

# 2. Data Type Conventions

The data types below are logical recommendations rather than platform-specific implementation requirements.

| Type                    | Intended Use                                       |
| ----------------------- | -------------------------------------------------- |
| INTEGER                 | Numeric identifiers and whole-number quantities    |
| DECIMAL(10,2)           | Currency and monetary values                       |
| VARCHAR(n)              | Variable-length text                               |
| TEXT                    | Longer descriptions or customer-provided narrative |
| BOOLEAN                 | True/false state                                   |
| DATE                    | Calendar date                                      |
| DATETIME                | Date and time                                      |
| ENUM / Controlled Value | Field restricted to defined business states        |

Primary keys may be implemented using integer identity values, UUIDs, or another appropriate identifier strategy depending on the selected platform.

---

# 3. Customer

| Field         | Type         | Key | Null | Description / Rule                                     |
| ------------- | ------------ | --- | ---- | ------------------------------------------------------ |
| CustomerID    | INTEGER      | PK  | No   | Unique customer identifier                             |
| FirstName     | VARCHAR(100) |     | No   | Customer first name                                    |
| LastName      | VARCHAR(100) |     | No   | Customer last name                                     |
| Email         | VARCHAR(254) |     | No   | Primary customer email; must follow valid email format |
| Phone         | VARCHAR(25)  |     | Yes  | Optional customer contact number                       |
| AccountStatus | VARCHAR(30)  |     | No   | Controlled value such as Active, Inactive, Suspended   |
| CreatedDate   | DATETIME     |     | No   | Date/time customer record was created                  |
| UpdatedDate   | DATETIME     |     | No   | Date/time customer record was last updated             |

### Customer Rules

* Email should be unique where the system uses email as the primary account identifier.
* Authentication credentials should not be stored in this entity.
* Customer contact data should be accessible only where required by business role.
* Account deactivation should not automatically delete historical order records.

---

# 4. ProductCategory

| Field          | Type         | Key | Null | Description / Rule                          |
| -------------- | ------------ | --- | ---- | ------------------------------------------- |
| CategoryID     | INTEGER      | PK  | No   | Unique category identifier                  |
| CategoryName   | VARCHAR(100) |     | No   | Customer-facing category name               |
| Description    | VARCHAR(500) |     | Yes  | Optional category description               |
| CategoryStatus | VARCHAR(30)  |     | No   | Controlled value such as Active or Inactive |

### ProductCategory Rules

* CategoryName should be unique.
* Inactive categories should not normally appear in customer browsing.
* Products assigned to an inactive category require review before publication.

---

# 5. Product

| Field          | Type          | Key | Null | Description / Rule                                      |
| -------------- | ------------- | --- | ---- | ------------------------------------------------------- |
| ProductID      | INTEGER       | PK  | No   | Unique product identifier                               |
| CategoryID     | INTEGER       | FK  | No   | References ProductCategory.CategoryID                   |
| SKU            | VARCHAR(50)   |     | No   | Internal product stock-keeping identifier               |
| ProductName    | VARCHAR(200)  |     | No   | Customer-facing product name                            |
| Description    | TEXT          |     | Yes  | Customer-facing product description                     |
| CurrentPrice   | DECIMAL(10,2) |     | No   | Current catalog price                                   |
| ProductStatus  | VARCHAR(30)   |     | No   | Active, Inactive, Discontinued, or other approved state |
| ImageReference | VARCHAR(500)  |     | Yes  | Path or reference to product image                      |
| CreatedDate    | DATETIME      |     | No   | Product creation timestamp                              |
| UpdatedDate    | DATETIME      |     | No   | Product last-modified timestamp                         |

### Product Rules

* SKU should be unique.
* CurrentPrice cannot be negative.
* ProductStatus determines whether a product can normally be displayed or sold.
* Inventory quantity must not be stored directly on Product.
* Historical order pricing must come from OrderItem.UnitPrice rather than CurrentPrice.

---

# 6. Store

| Field        | Type         | Key | Null | Description / Rule                                          |
| ------------ | ------------ | --- | ---- | ----------------------------------------------------------- |
| StoreID      | INTEGER      | PK  | No   | Unique store identifier                                     |
| StoreName    | VARCHAR(150) |     | No   | Customer-facing store name                                  |
| AddressLine1 | VARCHAR(200) |     | No   | Primary street address                                      |
| AddressLine2 | VARCHAR(200) |     | Yes  | Suite, unit, or secondary address                           |
| City         | VARCHAR(100) |     | No   | Store city                                                  |
| State        | VARCHAR(50)  |     | No   | State or region                                             |
| PostalCode   | VARCHAR(20)  |     | No   | Postal code                                                 |
| Phone        | VARCHAR(25)  |     | Yes  | Store contact number                                        |
| StoreStatus  | VARCHAR(30)  |     | No   | Active, Temporarily Closed, Closed, or other approved value |

### Store Rules

* Closed stores should not be shown as available fulfillment locations.
* Store records should not be deleted solely because a location closes if historical transactions depend on them.
* Address data should remain consistent enough to support customer directions and fulfillment logic.

---

# 7. Inventory

| Field              | Type        | Key | Null | Description / Rule                                      |
| ------------------ | ----------- | --- | ---- | ------------------------------------------------------- |
| InventoryID        | INTEGER     | PK  | No   | Unique inventory record identifier                      |
| StoreID            | INTEGER     | FK  | No   | References Store.StoreID                                |
| ProductID          | INTEGER     | FK  | No   | References Product.ProductID                            |
| QuantityOnHand     | INTEGER     |     | No   | Physical quantity currently recorded                    |
| QuantityReserved   | INTEGER     |     | No   | Quantity allocated to pending orders or holds           |
| AvailabilityStatus | VARCHAR(30) |     | No   | In Stock, Low Stock, Out of Stock, Backordered, Unknown |
| LastUpdated        | DATETIME    |     | No   | Most recent inventory update                            |

### Inventory Rules

* `StoreID + ProductID` must be unique.
* QuantityOnHand should not be negative unless the business explicitly permits negative inventory for reconciliation.
* QuantityReserved cannot be negative.
* QuantityReserved should not exceed valid available inventory without an approved exception.
* Customer-facing availability may be calculated from quantities rather than manually maintained.
* Inventory availability should be associated with one specific store.

---

# 8. Order

| Field              | Type          | Key | Null | Description / Rule                                           |
| ------------------ | ------------- | --- | ---- | ------------------------------------------------------------ |
| OrderID            | INTEGER       | PK  | No   | Unique order identifier                                      |
| CustomerID         | INTEGER       | FK  | Yes  | References Customer.CustomerID; nullable for guest checkout  |
| OrderDate          | DATETIME      |     | No   | Date/time order was initiated                                |
| OrderStatus        | VARCHAR(40)   |     | No   | Current order lifecycle state                                |
| FulfillmentMethod  | VARCHAR(30)   |     | No   | Store Pickup, Shipping, or approved future option            |
| FulfillmentStoreID | INTEGER       | FK  | Yes  | Store responsible for pickup or fulfillment where applicable |
| Subtotal           | DECIMAL(10,2) |     | No   | Sum of order-item values before tax/shipping                 |
| TaxAmount          | DECIMAL(10,2) |     | No   | Calculated tax amount                                        |
| ShippingAmount     | DECIMAL(10,2) |     | No   | Shipping charge; zero when not applicable                    |
| OrderTotal         | DECIMAL(10,2) |     | No   | Final order total                                            |
| CreatedDate        | DATETIME      |     | No   | Order creation timestamp                                     |
| UpdatedDate        | DATETIME      |     | No   | Last order update timestamp                                  |

### Order Rules

* Monetary values cannot be negative unless required by an approved adjustment process.
* OrderTotal should reconcile to Subtotal + TaxAmount + ShippingAmount.
* FulfillmentStoreID is required when fulfillment depends on a physical store.
* An order must not be represented as successfully paid solely because it was created.
* Order state transitions must follow the defined order-management workflow.

---

# 9. OrderItem

| Field       | Type          | Key | Null | Description / Rule                    |
| ----------- | ------------- | --- | ---- | ------------------------------------- |
| OrderItemID | INTEGER       | PK  | No   | Unique order-line identifier          |
| OrderID     | INTEGER       | FK  | No   | References Order.OrderID              |
| ProductID   | INTEGER       | FK  | No   | References Product.ProductID          |
| Quantity    | INTEGER       |     | No   | Number of units purchased             |
| UnitPrice   | DECIMAL(10,2) |     | No   | Price per unit at time of transaction |
| LineTotal   | DECIMAL(10,2) |     | No   | Quantity multiplied by UnitPrice      |

### OrderItem Rules

* Quantity must be greater than zero.
* UnitPrice cannot be negative.
* LineTotal must reconcile to Quantity × UnitPrice.
* UnitPrice is preserved as transaction history even when Product.CurrentPrice later changes.
* OrderItem cannot exist without a valid Order and Product.

---

# 10. PaymentReference

| Field              | Type          | Key | Null | Description / Rule                                          |
| ------------------ | ------------- | --- | ---- | ----------------------------------------------------------- |
| PaymentReferenceID | INTEGER       | PK  | No   | Unique retailer-side payment reference                      |
| OrderID            | INTEGER       | FK  | No   | References Order.OrderID                                    |
| ProviderReference  | VARCHAR(200)  |     | No   | Transaction or token reference returned by payment provider |
| PaymentStatus      | VARCHAR(30)   |     | No   | Initiated, Authorized, Declined, Cancelled, Refunded, etc.  |
| AuthorizedAmount   | DECIMAL(10,2) |     | Yes  | Amount authorized or captured by processor                  |
| TransactionDate    | DATETIME      |     | No   | Date/time payment event occurred                            |
| LastUpdated        | DATETIME      |     | No   | Last payment-state update                                   |

### PaymentReference Rules

The entity must not store:

* full primary account numbers;
* CVV/CVC values;
* PIN information;
* magnetic-stripe data;
* sensitive authentication data.

Additional rules:

* ProviderReference should be unique where supported by the provider.
* Payment status must be derived from valid provider information.
* Declined or failed payment states must not be treated as successful authorization.
* Refund activity may generate additional payment-reference records rather than overwriting transaction history.

---

# 11. SpecialOrderRequest

| Field                    | Type          | Key | Null | Description / Rule                                             |
| ------------------------ | ------------- | --- | ---- | -------------------------------------------------------------- |
| SpecialOrderRequestID    | INTEGER       | PK  | No   | Unique request identifier                                      |
| CustomerID               | INTEGER       | FK  | Yes  | References Customer.CustomerID where customer account exists   |
| ProductID                | INTEGER       | FK  | Yes  | References Product.ProductID if item already exists in catalog |
| CustomerName             | VARCHAR(200)  |     | No   | Requestor name                                                 |
| CustomerEmail            | VARCHAR(254)  |     | Yes  | Requestor email                                                |
| CustomerPhone            | VARCHAR(25)   |     | Yes  | Requestor phone                                                |
| RequestedItemDescription | TEXT          |     | No   | Description of requested merchandise                           |
| RequestedQuantity        | INTEGER       |     | No   | Number of requested units                                      |
| RequestStatus            | VARCHAR(40)   |     | No   | Current special-order workflow state                           |
| QuotedPrice              | DECIMAL(10,2) |     | Yes  | Price quoted to customer where known                           |
| CustomerApprovalStatus   | VARCHAR(30)   |     | Yes  | Pending, Approved, Declined, or equivalent                     |
| AssignedEmployeeID       | INTEGER       | FK  | Yes  | Employee responsible for review                                |
| SupplierID               | INTEGER       | FK  | Yes  | Supplier selected for sourcing                                 |
| SubmittedDate            | DATETIME      |     | No   | Request submission timestamp                                   |
| UpdatedDate              | DATETIME      |     | No   | Most recent request update                                     |

### SpecialOrderRequest Rules

* ProductID may be null when the requested item is not in the catalog.
* At least one usable customer contact method must be supplied.
* RequestedQuantity must be greater than zero.
* SupplierID may remain null until sourcing begins.
* QuotedPrice may remain null until supplier pricing is available.
* RequestStatus must follow the defined special-order workflow.

---

# 12. Employee

| Field            | Type         | Key | Null | Description / Rule                                          |
| ---------------- | ------------ | --- | ---- | ----------------------------------------------------------- |
| EmployeeID       | INTEGER      | PK  | No   | Unique employee identifier                                  |
| StoreID          | INTEGER      | FK  | Yes  | Primary store assignment where applicable                   |
| FirstName        | VARCHAR(100) |     | No   | Employee first name                                         |
| LastName         | VARCHAR(100) |     | No   | Employee last name                                          |
| Email            | VARCHAR(254) |     | No   | Business or authorized login-associated email               |
| EmploymentStatus | VARCHAR(30)  |     | No   | Active, Inactive, Leave, Terminated, or approved equivalent |
| CreatedDate      | DATETIME     |     | No   | Record creation timestamp                                   |
| UpdatedDate      | DATETIME     |     | No   | Last record update timestamp                                |

### Employee Rules

* Employee email should be unique where used for system identity.
* Inactive or terminated employees must not retain active system access.
* StoreID may be null for centralized or cross-location staff.
* Authentication credentials should be maintained separately from the employee business record.

---

# 13. Role

| Field       | Type         | Key | Null | Description / Rule              |
| ----------- | ------------ | --- | ---- | ------------------------------- |
| RoleID      | INTEGER      | PK  | No   | Unique role identifier          |
| RoleName    | VARCHAR(100) |     | No   | Defined business or access role |
| Description | VARCHAR(500) |     | Yes  | Role purpose and responsibility |
| RoleStatus  | VARCHAR(30)  |     | No   | Active or Inactive              |

### Role Rules

* RoleName should be unique.
* Roles should represent legitimate business responsibilities rather than individual users.
* Detailed permissions are defined in the Security and Access Control section.

---

# 14. EmployeeRole

| Field          | Type     | Key | Null | Description / Rule                          |
| -------------- | -------- | --- | ---- | ------------------------------------------- |
| EmployeeRoleID | INTEGER  | PK  | No   | Unique role-assignment identifier           |
| EmployeeID     | INTEGER  | FK  | No   | References Employee.EmployeeID              |
| RoleID         | INTEGER  | FK  | No   | References Role.RoleID                      |
| AssignedDate   | DATETIME |     | No   | Date/time role assignment became effective  |
| ActiveStatus   | BOOLEAN  |     | No   | Indicates whether assignment remains active |

### EmployeeRole Rules

* Active `EmployeeID + RoleID` combinations should be unique.
* Role assignments should be removed or disabled when no longer required.
* An inactive employee should not have active role assignments.
* Role assignment does not override other access-governance restrictions.

---

# 15. Supplier

| Field          | Type         | Key | Null | Description / Rule                         |
| -------------- | ------------ | --- | ---- | ------------------------------------------ |
| SupplierID     | INTEGER      | PK  | No   | Unique supplier identifier                 |
| SupplierName   | VARCHAR(200) |     | No   | Supplier or distributor business name      |
| ContactName    | VARCHAR(200) |     | Yes  | Primary business contact                   |
| Email          | VARCHAR(254) |     | Yes  | Supplier contact email                     |
| Phone          | VARCHAR(25)  |     | Yes  | Supplier contact phone                     |
| SupplierStatus | VARCHAR(30)  |     | No   | Active, Inactive, Suspended, or equivalent |

### Supplier Rules

* SupplierName should be sufficiently unique to distinguish vendors.
* Inactive suppliers should not be selected for new sourcing without review.
* Supplier data is operational and should not be exposed through the customer-facing website unless specifically intended.

---

# 16. ProductSupplier

| Field                 | Type          | Key | Null | Description / Rule                                  |
| --------------------- | ------------- | --- | ---- | --------------------------------------------------- |
| ProductSupplierID     | INTEGER       | PK  | No   | Unique product/supplier relationship identifier     |
| ProductID             | INTEGER       | FK  | No   | References Product.ProductID                        |
| SupplierID            | INTEGER       | FK  | No   | References Supplier.SupplierID                      |
| SupplierSKU           | VARCHAR(100)  |     | Yes  | Supplier-specific identifier                        |
| UnitCost              | DECIMAL(10,2) |     | Yes  | Current supplier acquisition cost                   |
| TypicalLeadTimeDays   | INTEGER       |     | Yes  | Estimated sourcing lead time                        |
| PreferredSupplier     | BOOLEAN       |     | No   | Indicates preferred sourcing relationship           |
| SupplierProductStatus | VARCHAR(30)   |     | No   | Available, Backordered, Discontinued, Unknown, etc. |

### ProductSupplier Rules

* `ProductID + SupplierID` should normally be unique.
* UnitCost cannot be negative.
* TypicalLeadTimeDays cannot be negative.
* More than one supplier may provide the same product.
* A preferred supplier flag should not prevent alternate sourcing where required.

---

# 17. Controlled Values

Where practical, status fields should use controlled values rather than unrestricted user-entered text.

Examples include:

| Field                  | Example Values                                                                                                                   |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| ProductStatus          | Active, Inactive, Discontinued                                                                                                   |
| CategoryStatus         | Active, Inactive                                                                                                                 |
| StoreStatus            | Active, Temporarily Closed, Closed                                                                                               |
| AvailabilityStatus     | In Stock, Low Stock, Out of Stock, Backordered, Unknown                                                                          |
| AccountStatus          | Active, Inactive, Suspended                                                                                                      |
| OrderStatus            | Pending, Awaiting Payment, Paid, Processing, Ready for Pickup, Shipped, Completed, Cancelled, Failed                             |
| PaymentStatus          | Initiated, Authorized, Declined, Cancelled, Refunded, Partially Refunded                                                         |
| RequestStatus          | Submitted, Under Review, Supplier Inquiry, Awaiting Customer Approval, Approved, Ordered, Unable to Source, Cancelled, Completed |
| CustomerApprovalStatus | Pending, Approved, Declined                                                                                                      |
| EmploymentStatus       | Active, Inactive, Leave, Terminated                                                                                              |
| RoleStatus             | Active, Inactive                                                                                                                 |
| SupplierStatus         | Active, Inactive, Suspended                                                                                                      |

Final values should be aligned with workflow definitions before implementation.

---

# 18. Referential Integrity Summary

Foreign-key relationships should prevent orphaned records where the parent entity is required.

| Child Entity        | Foreign Key        | Parent Entity   |
| ------------------- | ------------------ | --------------- |
| Product             | CategoryID         | ProductCategory |
| Inventory           | StoreID            | Store           |
| Inventory           | ProductID          | Product         |
| Order               | CustomerID         | Customer        |
| Order               | FulfillmentStoreID | Store           |
| OrderItem           | OrderID            | Order           |
| OrderItem           | ProductID          | Product         |
| PaymentReference    | OrderID            | Order           |
| SpecialOrderRequest | CustomerID         | Customer        |
| SpecialOrderRequest | ProductID          | Product         |
| SpecialOrderRequest | AssignedEmployeeID | Employee        |
| SpecialOrderRequest | SupplierID         | Supplier        |
| Employee            | StoreID            | Store           |
| EmployeeRole        | EmployeeID         | Employee        |
| EmployeeRole        | RoleID             | Role            |
| ProductSupplier     | ProductID          | Product         |
| ProductSupplier     | SupplierID         | Supplier        |

Nullable foreign keys are permitted only where the business process legitimately allows the related entity to be unknown or absent.

---

# 19. Deletion and Historical Data

Hard deletion should be used cautiously where records participate in historical transactions.

Examples:

* Products referenced by completed orders should generally be made inactive rather than deleted.
* Stores referenced by historical orders should remain available for historical reporting even after closure.
* Customers may be deactivated or anonymized where appropriate without invalidating required order records.
* Employees with historical administrative activity should not simply disappear from audit-related records.
* Supplier relationships may be disabled when no longer active.
* Payment references associated with legitimate transactions should remain available according to applicable reconciliation and retention requirements.

Specific retention periods are intentionally addressed outside this data dictionary.

---

# 20. Implementation Boundary

This dictionary defines the proposed logical structure of the future-state retail system.

It does not indicate that a production database containing these entities has been implemented.

The academic website may represent equivalent information through mock records, JSON data, browser-side storage, or other demonstration methods.

If a live database is later implemented, this dictionary should be updated to reflect:

* actual platform-specific data types;
* final constraints;
* indexing;
* generated identifiers;
* default values;
* audit columns;
* migration decisions;
* implemented validation rules.

