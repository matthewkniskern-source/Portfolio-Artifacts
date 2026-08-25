# E Commerce Workflows

## 1. Purpose

This section defines the primary business workflows that support customer discovery, purchasing, special orders, inventory visibility, and order fulfillment.

The workflows are designed to show:

* who owns each step;
* where decisions occur;
* how exceptions are handled;
* how status changes affect the next action.

Detailed page structure, data definitions, security controls, and test cases are maintained elsewhere in the repository.

---

# 2. Workflow Design Principles

The workflows follow several operating principles.

### Keep Customer Actions Simple

Customer-facing steps should remain straightforward even when the internal process is more complex.

### Separate Customer Experience from Internal Processing

The website may present a simple action such as "Submit Special Order", while staff and supplier review occurs behind that interaction.

### Use Defined Statuses

Orders, payments, special-order requests, and inventory should move through controlled states rather than relying on informal notes.

### Fail Safely

A failed payment, invalid request, inventory mismatch, or supplier rejection should not create an incorrect successful outcome.

### Preserve Ownership

Each operational step should have a clear responsible party.

---

# 3. Product Discovery Workflow

## Objective

Allow a customer to locate merchandise, review product information, and determine whether the product is available.

## Primary Actors

* Customer
* Website / Catalog
* Inventory Data Source

## Workflow

```text
Customer Enters Site
        ↓
Browse Products or Search
        ↓
Apply Category / Filter
        ↓
Select Product
        ↓
View Product Detail
        ↓
Check Store Availability
        ↓
┌──────────────────────────────┐
│ Is Product Available?        │
└──────────────┬───────────────┘
               │
         Yes   │   No
          ↓    │    ↓
  Purchase / Visit Store   Special Order Option
```

## Decision Points

### Product Found?

If the customer cannot locate the desired product:

* refine search;
* browse another category;
* submit a special-order request.

### Inventory Available?

If inventory is available:

* customer may add the product to the cart;
* customer may identify a store for in-person purchase.

If inventory is unavailable:

* customer may submit a special-order request where applicable.

## Ownership

| Step                 | Owner                      |
| -------------------- | -------------------------- |
| Search / Browse      | Customer                   |
| Product Presentation | Website                    |
| Inventory Display    | Website / Inventory Source |
| Product Maintenance  | Authorized Staff           |

---

# 4. Purchase Workflow

## Objective

Move a customer from product selection through a valid purchase or simulated purchase outcome.

## Primary Actors

* Customer
* Website
* Inventory Service
* External Payment Provider
* Fulfillment Staff

## Workflow

```text
Product Selected
      ↓
Add to Cart
      ↓
Review Cart
      ↓
Proceed to Checkout
      ↓
Enter Required Information
      ↓
Validate Input
      ↓
┌────────────────────────────┐
│ Is Input Valid?            │
└──────────────┬─────────────┘
               │
        No     │     Yes
        ↓      │      ↓
 Correct Input │   Recheck Availability
               │      ↓
               │   Submit Payment
               │      ↓
               │   External Provider
               │      ↓
               │ ┌───────────────────────┐
               │ │ Payment Authorized?   │
               │ └──────────┬────────────┘
               │            │
               │      No    │    Yes
               │      ↓     │     ↓
               │ Failed     │ Create / Finalize Order
               │ Payment    │
               │            ↓
               │      Reserve / Reduce Inventory
               │            ↓
               │      Generate Confirmation
               │            ↓
               │      Begin Fulfillment
```

## Key Rules

* required checkout data must be validated before payment processing;
* product availability should be confirmed before final order completion;
* failed payment must not create a successfully paid order;
* payment-card data should remain with the external payment provider;
* the retailer should store only necessary transaction references;
* inventory updates should follow successful order processing rather than cart activity alone.

## Exception Paths

### Product Becomes Unavailable During Checkout

Possible outcomes:

* prevent completion;
* adjust available quantity;
* notify customer;
* return customer to cart.

### Payment Declined

The system should:

* retain the cart where practical;
* display a clear failure state;
* allow another payment attempt;
* avoid marking the order as paid.

### Payment Provider Unavailable

The system should:

* avoid repeated uncontrolled payment attempts;
* inform the customer that checkout is temporarily unavailable;
* preserve the cart where practical;
* avoid creating an ambiguous transaction state.

---

# 5. Special Order Workflow

## Objective

Provide a structured path for merchandise that is unavailable or not currently listed.

## Primary Actors

* Customer
* Store or E Commerce Staff
* Supplier
* Customer Service / Assigned Employee

## Workflow

```text
Customer Cannot Locate Item
        ↓
Submit Special Order Request
        ↓
Validate Request
        ↓
Request Status: Submitted
        ↓
Staff Review
        ↓
┌─────────────────────────────┐
│ Is Request Sufficient?      │
└─────────────┬───────────────┘
              │
       No     │      Yes
       ↓      │       ↓
Request More  │   Supplier Review
Information   │       ↓
              │ ┌───────────────────────┐
              │ │ Can Item Be Sourced?  │
              │ └──────────┬────────────┘
              │            │
              │      No    │    Yes
              │      ↓     │     ↓
              │ Unable to  │ Determine Cost /
              │ Source     │ Lead Time
              │            ↓
              │      Provide Customer Quote
              │            ↓
              │ ┌─────────────────────────┐
              │ │ Customer Approves?      │
              │ └──────────┬──────────────┘
              │            │
              │      No    │    Yes
              │      ↓     │     ↓
              │ Cancelled  │ Place Supplier Order
              │            ↓
              │      Receive Merchandise
              │            ↓
              │      Notify Customer
              │            ↓
              │         Completed
```

## Status Progression

Typical states include:

```text
Submitted
   ↓
Under Review
   ↓
Supplier Inquiry
   ↓
Awaiting Customer Approval
   ↓
Approved
   ↓
Ordered
   ↓
Completed
```

Exception states include:

```text
Unable to Source
Cancelled
```

## Key Rules

* a request may reference an existing Product or an uncataloged item;
* customer contact information must be available;
* quoted price should not be treated as accepted until customer approval is recorded;
* supplier inability to source the item should produce a clear terminal state;
* ownership should remain assigned until the request is resolved.

---

# 6. Inventory Update Workflow

## Objective

Maintain store-level inventory information that supports both operational use and customer-facing availability.

## Primary Actors

* Store Staff
* Inventory Manager
* Inventory System
* Website

## Workflow

```text
Inventory Event
      ↓
Receipt / Sale / Adjustment / Reservation
      ↓
Identify Store
      ↓
Identify Product
      ↓
Validate Quantity Change
      ↓
Update Inventory Record
      ↓
Recalculate Availability
      ↓
Publish Customer Facing Status
```

## Common Inventory Events

Inventory may change because of:

* product receipt;
* sale;
* order reservation;
* order cancellation;
* manual adjustment;
* damaged merchandise;
* transfer or correction.

## Exception Paths

### Invalid Quantity

If the update would create an invalid inventory state:

* reject or flag the transaction;
* require authorized review;
* preserve the previous valid value until resolved.

### Inventory Synchronization Failure

If customer-facing availability cannot be updated:

* record the failure;
* avoid presenting stale data as highly reliable where practical;
* notify responsible staff;
* restore synchronization before normal operation resumes.

---

# 7. Order Management Workflow

## Objective

Move a valid paid order through fulfillment to completion.

## Primary Actors

* E Commerce System
* Store or Fulfillment Staff
* Customer

## Workflow

```text
Payment Authorized
      ↓
Order Status: Paid
      ↓
Assign Fulfillment
      ↓
Order Status: Processing
      ↓
Pick / Prepare Items
      ↓
┌────────────────────────────┐
│ Fulfillment Method?        │
└──────────────┬─────────────┘
               │
        Pickup │ Shipping
          ↓    │    ↓
 Ready for     │ Prepare Shipment
 Pickup        │
          ↓    │    ↓
 Customer      │ Shipped
 Notified      │
          ↓    │    ↓
 Pickup        │ Delivery / Completion
          └────┴───────┐
                       ↓
               Order Completed
```

## Order Statuses

Recommended order states:

* Pending
* Awaiting Payment
* Paid
* Processing
* Ready for Pickup
* Shipped
* Completed
* Cancelled
* Failed

## Key Rules

* order status must reflect the actual business state;
* payment state and fulfillment state should remain distinguishable;
* cancelled or failed orders must not appear completed;
* staff should only update orders within their authorized role;
* customer-facing status should be understandable without exposing internal administrative detail.

---

# 8. Refund Workflow

Refund behavior is included as an operational consideration but is not required for the academic implementation.

## Workflow

```text
Refund Requested
      ↓
Validate Order
      ↓
Determine Refund Eligibility
      ↓
Authorized Staff Approval
      ↓
Submit Refund to Payment Provider
      ↓
Receive Provider Result
      ↓
┌───────────────────────────┐
│ Refund Successful?        │
└─────────────┬─────────────┘
              │
        No    │    Yes
        ↓     │     ↓
Exception /   │ Update Payment Reference
Review        │
              ↓
        Update Order as Appropriate
              ↓
        Notify Customer
```

The retailer should retain the provider's transaction reference and refund status rather than handling raw payment-card data.

---

# 9. Workflow Ownership Summary

| Workflow          | Primary Owner                | Supporting Actors                   |
| ----------------- | ---------------------------- | ----------------------------------- |
| Product Discovery | Customer / Website           | Product and Inventory Staff         |
| Purchase          | Customer / E Commerce System | Payment Provider, Fulfillment Staff |
| Special Order     | Assigned Staff               | Customer, Supplier                  |
| Inventory Update  | Inventory / Store Staff      | System Administrator where needed   |
| Order Fulfillment | Fulfillment Staff            | Customer, E Commerce System         |
| Refund            | Authorized Staff             | Payment Provider, Customer          |

Ownership may differ by store size or staffing model, but each workflow should maintain clear responsibility for unresolved work.

---

# 10. Workflow Status Integrity

Status fields should represent actual business conditions rather than functioning as informal labels.

Examples:

* an order should not become `Paid` without a valid payment result;
* a special order should not become `Approved` without the appropriate customer or staff decision;
* inventory should not become `In Stock` solely because the product exists in the catalog;
* an order should not become `Completed` while fulfillment remains outstanding.

This separation supports more reliable reporting, testing, and operational troubleshooting.

---

# 11. Academic Implementation Boundary

The academic website may demonstrate several workflows using front-end behavior and mock data.

Likely demonstrable functions include:

* product discovery;
* search and filtering;
* product detail;
* cart activity;
* checkout validation;
* simulated payment outcome;
* order confirmation;
* special-order submission;
* store availability display.

The following remain future-state operational workflows unless actually implemented:

* live supplier interaction;
* production inventory synchronization;
* real payment authorization;
* authenticated staff order management;
* refund processing;
* production fulfillment integration.

These distinctions are maintained in the Requirements Traceability Matrix and implementation documentation.

---

# 12. Workflow Design Outcome

The workflows create a defined path from customer demand to an operational outcome.

At a high level:

```text
Discover
   ↓
Evaluate
   ↓
Purchase or Request
   ↓
Validate
   ↓
Process
   ↓
Fulfill
   ↓
Confirm
```

The workflow design keeps customer-facing interactions simple while preserving the internal decision points and status controls required for a credible future-state retail system.

