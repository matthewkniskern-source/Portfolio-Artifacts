# Reorder Flow

## Entry

Authenticated retail customer
→ Opens account
→ Views eligible prior online purchases
→ Selects product for reorder

## Validation

Selected product
→ Current SKU status checked
→ Current inventory checked
→ Current Lightspeed retail price retrieved
→ Product eligibility confirmed

## Available Product

Product available
→ Customer selects quantity
→ Item added to cart
→ Standard 10-minute reservation created
→ Customer proceeds through normal checkout

## Low Stock

Requested quantity exceeds available inventory
→ Exact remaining quantity displayed
→ Customer may adjust requested quantity
→ Valid quantity may proceed to cart

## Out of Stock

Current availability equals zero
→ Reorder purchase disabled
→ Product-specific contact path displayed
→ “Customers Also Chose” alternatives presented

## Changed Product Status

Product discontinued, replaced, or otherwise unavailable
→ Prior order remains visible in history
→ Reorder action disabled
→ Replacement or related products displayed when configured

## Pricing

Historical order price shall not control the reorder.

Current Lightspeed public retail pricing applies at the time of reorder.

## Scope

Reorder history applies to authenticated public retail ecommerce purchases.

Managed commercial-account purchases remain outside the web reorder workflow.
