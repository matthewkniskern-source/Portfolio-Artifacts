# Business Case

## 1. Business Overview

**One-Punch Anime Emporium** is a fictional specialty retailer operating multiple physical storefronts that sell anime, manga, comics, collectibles, apparel, and related merchandise.

The business currently relies primarily on in-store traffic and direct customer contact. Customers may know the company exists, but they have limited ability to determine what products are available, which store has an item in stock, or whether an unavailable product can be ordered.

The current model supports physical retail operations, but it does not provide a strong digital path between customer interest and purchase.

---

## 2. Current-State Business Problem

The primary business problem is not simply the absence of a modern website.

The larger issue is that customers have limited digital access to the retailer's products, inventory, and purchasing process.

In the current state:

* product discovery is largely dependent on visiting or contacting a store;
* customers cannot reliably search merchandise across locations;
* inventory availability is difficult to determine before a store visit;
* online purchasing is unavailable;
* special-order requests are handled informally or through direct communication;
* customers have limited visibility into product availability outside normal store hours;
* individual stores function as partially isolated inventory locations from the customer's perspective;
* management has limited digital data regarding customer demand, product searches, abandoned interest, or special-order activity.

These limitations increase friction for customers and place avoidable administrative work on store employees.

A customer looking for a specific figure, manga volume, collectible, or limited-release item may need to contact multiple locations individually. The business may have the requested product somewhere in its existing inventory while still failing to convert the customer's interest into a sale.

---

## 3. Business Need

One-Punch Anime Emporium requires a centralized digital presence that allows customers to move more easily from product interest to a purchasing decision.

The proposed transformation establishes a foundation for:

* centralized product discovery;
* improved store-level inventory visibility;
* online purchasing capability;
* structured special-order requests;
* more consistent customer communication;
* support for multiple retail locations through a common digital model;
* improved operational and customer-demand reporting.

The intent is not to replace the company's physical retail model.

The digital channel is designed to extend it.

Physical stores remain part of the customer experience, inventory model, fulfillment process, and brand identity.

---

## 4. Customer Pain Points

The current operating model creates several recurring customer problems.

### Product Discovery

Customers cannot easily determine whether the retailer carries a specific product without visiting or contacting a store.

### Inventory Visibility

Product availability is tied to individual locations, but customers lack a centralized way to determine which store may have an item in stock.

### Purchasing

A customer who finds a desired product has no reliable online path to complete the purchase.

### Special Orders

Rare, limited, or unavailable products may generate customer interest, but there is no structured process for capturing, reviewing, and tracking those requests.

### Convenience

Customer interaction is constrained by store hours and staff availability for questions that could otherwise be answered through a digital channel.

---

## 5. Operational Impact

The current model also creates internal inefficiencies.

Store employees may spend time responding to routine availability questions, checking inventory manually, or coordinating with other locations on behalf of customers.

Without a centralized digital channel, the business also has limited ability to measure:

* what customers are searching for;
* which products generate interest but are unavailable;
* how often customers seek inventory at another store;
* demand for special-order merchandise;
* digital conversion opportunities;
* customer activity outside physical store hours.

This reduces the business's ability to use customer behavior as an input to purchasing, inventory, merchandising, and staffing decisions.

---

## 6. Risks of Maintaining the Current Model

Maintaining the existing operating model creates several business risks.

| Risk                                     | Business Impact                                                                                         |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Limited digital product visibility       | Customers may purchase from competitors that provide easier product discovery                           |
| No online purchasing                     | Revenue opportunities are limited to customers able and willing to visit a store                        |
| Poor cross-location inventory visibility | Existing inventory may remain unsold while customers believe products are unavailable                   |
| Informal special-order handling          | Customer requests may be lost, delayed, or inconsistently processed                                     |
| Heavy reliance on employee assistance    | Staff time is consumed by routine product and inventory inquiries                                       |
| Limited customer-demand data             | Management has less information available for purchasing and merchandising decisions                    |
| Fragmented customer experience           | Customers receive different levels of information depending on store, employee, or communication method |

None of these risks independently justify a large enterprise technology program.

Together, however, they support a practical phased investment in digital retail capability.

---

## 7. Transformation Objective

The objective of this project is to establish a practical digital retail foundation that connects:

**customers → products → stores → inventory → orders → staff**

The initial academic implementation focuses on a hosted customer-facing website.

The broader portfolio case study evaluates the additional processes, architecture, data relationships, controls, and operational capabilities that would be required to move from an informational website toward a more complete e-commerce environment.

---

## 8. Project Objectives

The project is intended to achieve the following business outcomes.

### OBJ-01 — Improve Product Discovery

Provide customers with a centralized method for browsing and locating merchandise.

### OBJ-02 — Improve Inventory Visibility

Provide meaningful visibility into product availability across multiple retail locations.

### OBJ-03 — Expand the Sales Channel

Establish a design capable of supporting online purchasing while preserving existing physical-store operations.

### OBJ-04 — Formalize Special Orders

Create a structured process for capturing and managing customer requests for unavailable or specialty merchandise.

### OBJ-05 — Support Multi-Store Operations

Represent stores, products, and inventory through a common digital model.

### OBJ-06 — Improve Customer Communication

Provide consistent mechanisms for inquiries, order-related information, and special-order status communication.

### OBJ-07 — Improve Operational Visibility

Create a foundation for reporting on customer activity, inventory availability, orders, and unmet demand.

### OBJ-08 — Support Incremental Growth

Avoid designing the initial website as a dead end. The solution should support reasonable expansion as the retailer's digital capabilities mature.

---

## 9. Current State vs. Target State

| Area                   | Current State                                | Target State                                         |
| ---------------------- | -------------------------------------------- | ---------------------------------------------------- |
| Product Discovery      | Primarily in-store or through direct contact | Centralized searchable product catalog               |
| Inventory Visibility   | Individual store inquiry                     | Store-level availability visibility                  |
| Sales                  | Physical retail                              | Physical retail plus digital purchasing capability   |
| Special Orders         | Informal customer request                    | Structured request and review process                |
| Store Operations       | Locations appear largely independent online  | Shared digital presence across locations             |
| Customer Communication | Ad hoc                                       | Structured customer contact and status communication |
| Reporting              | Limited digital customer data                | Measurable digital activity and operational metrics  |
| Digital Availability   | Dependent on store hours                     | Customer-facing information available continuously   |

---

## 10. Project Scope

### In Scope

The broader case study includes design and analysis for:

* a customer-facing retail website;
* product browsing and search;
* product-detail presentation;
* store information;
* store-level inventory visibility;
* shopping-cart functionality;
* checkout workflow;
* order confirmation;
* special-order requests;
* customer communication;
* customer-account concepts;
* administrative functions;
* multi-location inventory modeling;
* payment integration architecture;
* security and access-control considerations;
* privacy and data-governance considerations;
* implementation and hosting;
* testing and user acceptance;
* project management;
* continuity and operational support;
* post-launch metrics and improvement.

Detailed functional and technical definitions are maintained in the corresponding sections of the repository rather than repeated here.

---

## 11. Scope Exclusions

The project does not include implementation of:

* a custom payment-processing platform;
* storage of raw payment-card data;
* a production ERP replacement;
* a production warehouse-management system;
* native mobile applications;
* supplier EDI integration;
* production identity federation;
* production-grade high-availability infrastructure;
* formal PCI DSS certification;
* formal privacy or legal compliance certification;
* live financial transactions within the demonstration environment.

Where these areas affect the proposed design, they may be addressed conceptually without being represented as implemented capabilities.

---

## 12. Project Assumptions

The business case is based on the following assumptions:

* the retailer operates multiple physical stores;
* stores carry overlapping but non-identical inventory;
* product quantities vary by store;
* customers may search for products that are currently unavailable;
* unavailable products may sometimes be sourced through suppliers;
* staff require different levels of administrative access;
* the business intends to maintain its physical retail presence;
* a relational data model is appropriate for core retail entities;
* production online payments would be handled through a third-party provider;
* the academic implementation will not process real payment-card information;
* the project will be delivered incrementally rather than as a single large implementation;
* some portfolio capabilities will remain architectural or conceptual rather than executable.

---

## 13. Success Criteria

The project will be considered successful if the resulting design and implementation demonstrate a clear path from the existing retail model toward a more capable digital operating model.

At a minimum, the project should show that a customer can more easily:

* understand what the retailer sells;
* browse or locate products;
* identify relevant store information;
* understand product availability;
* initiate a purchase or simulated purchase workflow;
* submit a special-order request;
* communicate with the business through a defined digital channel.

From an operational perspective, the project should also establish a credible foundation for future inventory integration, order processing, access control, reporting, and ongoing improvement.

---

## 14. Business Case Conclusion

One-Punch Anime Emporium does not require digital transformation for its own sake.

It requires a better way to connect customer demand with products the business already sells or may be able to source.

The initial hosted website addresses the most visible customer-facing gap. The broader case study extends that implementation into a practical future-state model for product discovery, multi-store inventory visibility, e-commerce, special orders, security, and digital operations.

The project therefore treats the website as the entry point to the solution rather than the entire solution.

