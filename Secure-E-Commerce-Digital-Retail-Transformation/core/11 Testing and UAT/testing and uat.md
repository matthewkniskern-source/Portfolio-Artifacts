# Testing and UAT — Browser Demo Verification Plan

**Status:** A suggested manual verification checklist for the past academic website. These are **test cases**, not claims of executed tests or recorded pass results. Execute them before describing a function as verified.

| ID | Action | Expected demonstration behavior | Evidence to retain |
| --- | --- | --- | --- |
| WEB-01 | Open homepage and primary navigation | Catalog, stores, contact and special orders are reachable | Screenshot/browser URL |
| WEB-02 | Open product listing and individual item | Selected product details correspond to the fictional catalog | Item ID and screenshot |
| WEB-03 | Add item to cart | Item appears with selected quantity and displayed subtotal | Cart state |
| WEB-04 | Change quantity / remove item | Displayed cart and totals recalculate | Before/after totals |
| WEB-05 | Refresh cart page | Browser-local cart is retained as designed | Refresh screenshot |
| WEB-06 | Follow simulated checkout with empty required fields | Field-level error messages appear | Validation screenshot |
| WEB-07 | Use fictional checkout information | Confirmation page shows a demonstration order | No real payment entered |
| WEB-08 | Inspect store-locations screen | Fictional store information displays | Screenshot |
| WEB-09 | Use special-order interaction | Form/flow follows the browser prototype's documented behavior | Screenshot and limitations |
| WEB-10 | Resize to narrow viewport | Navigation, product cards, forms, and cart remain usable | Mobile screenshot |
| WEB-11 | Navigate using keyboard only | Essential links and form inputs remain focusable | Keyboard test notes |
| WEB-12 | Clear browser storage | Cart/order state resets as expected | Before/after observation |

## Test data

Use synthetic names, addresses and example payment strings only. Do not enter live financial or customer details. Use browser developer tools to confirm that this demonstration does not make successful real-payment API calls.

## Failure and limitation reporting

A failed case should record the browser and version, viewport, steps, observed result, expected result, and any console error. Classify findings as a **prototype defect** or **outside the deliberately limited scope**. Do not change expected results to mask bugs.

## Acceptance boundary

The website can be assessed for functioning static navigation and browser-state interactions. It cannot pass production checkout, authorization, payment reconciliation, PCI compliance, or cross-device order-continuity acceptance tests without a real backend and payment architecture.
