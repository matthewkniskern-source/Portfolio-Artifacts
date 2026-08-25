# Information Architecture

## 1. Purpose

The information architecture defines how One-Punch Anime Emporium organizes customer-facing content and how users move through the website.

The goal is to support a straightforward retail experience without creating pages solely to satisfy a page-count requirement.

The site structure is designed around the primary customer questions:

* What does the retailer sell?
* Is the product I want available?
* Where can I get it?
* Can I buy it online?
* What if the item is unavailable?
* How do I contact or visit the business?

---

## 2. Design Principles

The site structure follows several practical principles.

### Keep Core Actions Visible

Customers should not have to search through multiple menus to reach products, store information, cart functions, or special-order requests.

### Organize Around Customer Intent

Navigation should reflect what customers are trying to accomplish rather than the internal organization of the retailer.

### Minimize Dead Ends

Product pages, search results, inventory information, and unavailable-product states should provide a logical next action.

### Support Physical and Digital Retail Together

The website should make it easy to move between online product discovery and physical store locations.

### Keep the Structure Extensible

Future capabilities such as customer accounts, live inventory, fulfillment options, and administrative functions should fit into the existing structure without requiring a complete redesign.

---

# 3. Site Hierarchy

```text
Home
│
├── Products
│   ├── Search
│   ├── Category / Filter Results
│   └── Product Detail
│       ├── Store Availability
│       ├── Add to Cart
│       └── Special Order
│
├── Store Locations
│   └── Store Detail
│
├── Special Orders
│
├── Cart
│   └── Checkout
│       └── Order Confirmation
│
├── About
│
├── Contact
│
└── Customer Account
    ├── Profile
    └── Order History
```

Customer Account functionality is part of the future-state design and may not be implemented in the academic website.

Administrative functionality is separated from the primary customer navigation.

---

# 4. Primary Navigation

The primary navigation should remain limited to the functions customers are most likely to use.

Recommended top-level navigation:

* Home
* Products
* Locations
* Special Orders
* About
* Contact
* Cart

Customer Account may be represented through a separate account icon or link if implemented later.

This keeps routine retail actions prominent while preventing the navigation bar from becoming overloaded.

---

# 5. Page and Function Purpose

## Home

The Home page serves as the primary entry point.

Its purpose is to quickly communicate:

* what One-Punch Anime Emporium sells;
* current featured or promoted merchandise;
* access to product browsing;
* access to store information;
* access to special-order capability.

The page should direct customers toward useful actions rather than functioning only as a promotional landing page.

---

## Products

The Products page serves as the main catalog entry point.

It should support:

* browsing;
* search;
* category navigation;
* product filtering;
* movement into product-detail pages.

The catalog should remain understandable even as the number of products grows.

---

## Product Detail

The Product Detail page provides the information needed to support a purchase decision.

Typical content includes:

* product name;
* image;
* category;
* description;
* price;
* store availability;
* purchase action;
* special-order option when appropriate.

The page should connect product discovery directly to inventory and purchase-related actions.

---

## Search

Search allows customers to locate products without browsing the entire catalog.

Search should support meaningful product terms such as:

* title;
* character;
* franchise;
* product category;
* keyword.

Search may be implemented within the Products page rather than as a separate standalone page.

---

## Store Locations

The Store Locations page connects the digital storefront to physical retail operations.

It should provide:

* store name;
* address;
* contact information;
* operating hours;
* other relevant visit information.

Where inventory visibility is supported, customers should also be able to understand which location carries a product.

---

## Cart

The Cart page allows customers to review intended purchases before checkout.

It should provide:

* selected products;
* quantities;
* pricing;
* subtotal;
* ability to remove or update items;
* checkout action.

The cart should make the customer's current transaction state clear.

---

## Checkout

Checkout collects the information required to complete or simulate a transaction.

Depending on implementation status, this may include:

* customer information;
* fulfillment information;
* order review;
* simulated payment transition.

Real payment-card information is not required for the academic demonstration environment.

---

## Order Confirmation

The Order Confirmation page provides a clear end state for the purchase workflow.

It should communicate:

* that the workflow completed;
* basic order information;
* next expected action;
* fulfillment or contact information where applicable.

A successful confirmation should only be displayed when the demonstrated workflow reaches the appropriate completion state.

---

## Special Orders

The Special Orders page provides a structured alternative when a customer cannot locate desired merchandise.

It should capture enough information for the business to understand:

* what the customer is requesting;
* how to contact the customer;
* any relevant product details.

The production workflow behind the request is defined separately in the E-Commerce Workflows section.

---

## About

The About page provides basic company and brand context.

Its purpose is to explain the retailer without competing with the primary shopping functions.

---

## Contact

The Contact page provides a general communication path for inquiries that do not belong in a product, order, or special-order workflow.

Where possible, structured functions should be used instead of sending every customer need through a generic contact form.

---

## Customer Account

The Customer Account area is a future-state capability.

Potential functions include:

* customer profile;
* saved information;
* order history;
* current order status.

It should not be presented as implemented unless authentication and account functionality are actually built.

---

# 6. Administrative Information Architecture

Administrative capabilities should not be mixed into normal customer navigation.

A future administrative area may include:

```text
Administration
│
├── Products
├── Inventory
├── Orders
├── Special Orders
├── Stores
├── Customers
├── Reporting
└── User / Role Management
```

Access to these functions would depend on assigned role and business responsibility.

The detailed authorization model is defined in the Security and Access Control section.

---

# 7. Primary User Journeys

## 7.1 Product Discovery Journey

```text
Home
  ↓
Products
  ↓
Browse / Search / Filter
  ↓
Product Detail
  ↓
Store Availability
  ↓
Purchase or Store Visit
```

The journey is designed to move directly from interest to availability and action.

---

## 7.2 Purchase Journey

```text
Product Detail
  ↓
Add to Cart
  ↓
Cart Review
  ↓
Checkout
  ↓
Payment Step
  ↓
Order Confirmation
```

In the academic environment, payment behavior may be simulated rather than connected to a real processor.

---

## 7.3 Special-Order Journey

```text
Product Unavailable
  ↓
Special Order
  ↓
Request Information
  ↓
Submit Request
  ↓
Acknowledgement
```

The customer-facing journey ends with acknowledgement.

Supplier review, pricing, approval, and fulfillment occur in the operational workflow defined elsewhere.

---

## 7.4 Store Visit Journey

```text
Product Detail
  ↓
Store Availability
  ↓
Locations
  ↓
Selected Store
  ↓
Visit / Contact
```

This journey supports customers who prefer or require physical retail fulfillment.

---

## 7.5 Returning Customer Journey

Future-state:

```text
Account
  ↓
Authentication
  ↓
Order History / Status
  ↓
Order Detail
```

This capability remains conceptual unless account functionality is implemented.

---

# 8. Navigation Relationships

The website should support cross-navigation where it helps the customer complete a task.

Examples include:

* Product Detail → Store Locations
* Product Detail → Special Order
* Product Detail → Cart
* Search Results → Product Detail
* Cart → Products
* Checkout → Cart
* Store Locations → Products
* Order Confirmation → Products or Home

Navigation should provide a logical recovery path when a customer changes direction.

---

# 9. Sitemap

```text
/
├── index.html
├── products.html
├── product.html
├── locations.html
├── special orders.html
├── cart.html
├── checkout.html
├── confirmation.html
├── about.html
└── contact.html
```

Additional functionality such as search and filtering may operate within existing pages rather than requiring separate HTML files.

Future-state functions may add:

```text
/account
/admin
/orders
```

These should only be added if the underlying functionality warrants them.

---

# 10. Academic Page Count Consideration

The academic project requires approximately ten pages or equivalent website components.

The selected structure meets that requirement without creating arbitrary content.

Each page exists because it supports one of three purposes:

1. product discovery and purchasing;
2. physical-store interaction;
3. customer or business communication.

Search, filtering, inventory display, and cart behavior may function as components within those pages rather than separate pages created only to increase the page count.

---

# 11. Implementation Boundary

The information architecture describes both the academic website and the broader future-state retail model.

Not every function shown in the architecture will necessarily be implemented.

The academic implementation is expected to focus on the customer-facing experience.

Capabilities such as:

* live inventory integration;
* authenticated customer accounts;
* administrative management;
* real order processing;
* real payment integration;

remain future-state functions unless they are explicitly developed and demonstrated.

Implementation status is maintained through the Requirements Traceability Matrix rather than duplicated throughout this document.

