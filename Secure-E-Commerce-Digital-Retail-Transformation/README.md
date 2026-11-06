# Secure E-Commerce and Digital Retail Transformation

**Project:** One-Punch Anime Emporium — a fictional multi-location specialty retailer

**Artifact type:** Past academic browser prototype with associated business-analysis and security-design documents. This is **not** a production storefront, payment integration, live inventory service, or enterprise deployment.

## At a glance

The project explores how a physical retailer could add product discovery, multi-location browsing, carts, checkout demonstrations, special-order paths, and clearer customer navigation. The implemented artifact is a static HTML/CSS/JavaScript website using **fictional catalog and location data**. It provides a working *demonstration* of customer-facing flows; browser-local cart/order handling does not implement real payment authorization, inventory reservation, or order processing.

The accompanying design material covers the business case, requirements, information architecture, data model, payment-boundary intent, access controls, privacy, and threats.

## Where to start

| Artifact | What to expect | Status |
| --- | --- | --- |
| [Website homepage](Implementation/Academic%20Website/index.html) | Public-facing mock storefront | Browser demo source present |
| [Product catalog](Implementation/Academic%20Website/products.html) and [cart](Implementation/Academic%20Website/cart.html) | Client-side discovery and cart interactions | Browser demo source present |
| [Checkout](Implementation/Academic%20Website/checkout.html) | Fictional checkout flow, browser-local order confirmation | **Simulation only**, no payment processing |
| [Business case](core/01%20Business%20Case/business%20case.md) | Operational problem, objectives, scope and desired outcomes | Design document |
| [Requirements](core/02%20Requirements/requirements.md) and [traceability](core/02%20Requirements/requirements%20traceability%20matrix.md) | Functional/nonfunctional expectations and mapping | Design documents |
| [Information architecture](core/03%20Information%20Architecture/information%20architecture.md) | Navigation, page relationships and user journeys | Design document |
| [Data model](core/04%20Data%20Model/data%20model.md) | Conceptual business entities and relationships | Proposed model |
| [Payment architecture](core/06%20Payment%20Architecture%20and%20PCI%20Scope/payment%20architecture.md) | Intended external payment-provider boundary | Proposed architecture |
| [Threat model](core/09%20Threat%20Model%20and%20Risk%20Analysis/threat%20model%20and%20risk%20analysis.md) | Potential risks and controls | Conceptual assessment |
| [Implementation boundary](core/10%20Implementation%20and%20Hosting/implementation%20and%20hosting.md) | What the static demo does and does not demonstrate | Portfolio documentation |
| [Testing and UAT guide](core/11%20Testing%20and%20UAT/testing%20and%20uat.md) | Reproducible manual verification steps | Test plan, not test results |

## Demonstration boundaries

- Inventory and products are predefined in JavaScript, not synchronized with store systems.
- Cart state and a demonstration order are maintained in the browser.
- Checkout fields use fictional values. **Do not enter real card, account, address, or customer information.**
- Pricing/tax behavior is simplified for the example and is not a production fiscal or sales-tax calculation.
- Customer authentication, administrative authorization, real payments, server-side reconciliation, and durable order storage are outside this browser demonstration.
- The design documents describe future-state controls; their presence does not mean those controls are implemented.

## Intended review sequence

1. Read the business case and requirements.
2. Open `Implementation/Academic Website/index.html` in a browser (or serve that directory through a local static server); explore catalog, cart, store information and special-order screens.
3. Use only fictional checkout data if testing the simulated order flow.
4. Compare behaviors against the information architecture and testing guide; distinguish observed behavior from unimplemented proposals.

## Documentation status

The most developed written sections cover business, requirements, architecture, data modeling, security and privacy. Some later project-management, continuity, deployment and validation artifacts remain planning placeholders; **do not interpret their presence as completed deliverables**. This README and the implementation/testing guides make those limits explicit.

## Project takeaway

The case demonstrates the relationship between a customer-facing retail prototype and the requirements, data flows, security boundaries, and operational decisions necessary before a similar concept could become a reliable production system.
