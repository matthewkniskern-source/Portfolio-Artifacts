# Implementation and Hosting — Demonstration Boundary

## Implemented browser artifact

The academic storefront under [Implementation/Academic Website](../../Implementation/Academic%20Website/) consists of static HTML pages, local CSS, JavaScript catalog data and product images. The code contains browse/search, cart, special-order and simulated checkout interactions. It is suitable for opening locally or serving with a simple static web server.

**Not implemented:** a backend, user identity provider, live API integration, inventory reservation service, payment gateway, financial ledger, or real order-management system. Checkout confirmation is based on local browser state, not on verified payment or server-side persistence.

## Local demonstration procedure

1. Obtain the repository and navigate to `Implementation/Academic Website/`.
2. Serve that folder with a local static file server or open `index.html` in a modern browser.
3. Browse the product categories, store locations, cart, and checkout using only fictional values.
4. Refresh or clear browser storage to observe the distinction between demonstration state and durable enterprise records.

No package installation or external service credentials are required by the static pages themselves.

## Proposed production migration (not built)

A real rollout would first require a verified commerce/payment platform, authoritative product and inventory data, inventory consistency rules, backend account management, server-side validation, audit logging, fulfillment operations, and operational recovery. Payment-card data should be handled by an appropriate payment provider instead of a homegrown browser-only checkout.

The [requirements](../02%20Requirements/requirements.md), [data model](../04%20Data%20Model/data%20model.md), and [payment architecture](../06%20Payment%20Architecture%20and%20PCI%20Scope/payment%20architecture.md) describe proposed considerations; they are not deployment records.

## Deployment and acceptance status

No public hosting performance, browser matrix, penetration test, live payment integration or production acceptance evidence is asserted by this case study. The verification steps are documented in [Testing and UAT](../11%20Testing%20and%20UAT/testing%20and%20uat.md).
