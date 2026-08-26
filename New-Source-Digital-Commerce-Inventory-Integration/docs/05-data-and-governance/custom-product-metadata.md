# Custom Product Metadata

## Managed Fields

Middleware-managed product metadata may include:

* Application / use case
* Compatibility text
* Related products
* Supplemental technical notes
* Merchandising tags
* Replacement-product references
* Discontinued-product notes

## Ownership

Custom product metadata is maintained through the internal dashboard.

It does not replace:

* Zoho inventory authority
* Lightspeed pricing authority
* Vendor-controlled product data

## Application / Use Case

Free-text or tag-based field used to support:

* Catalog filtering
* Search
* Product discovery
* Related-product recommendations

Example:

`Commercial water extraction and structural drying`

## Compatibility

Compatibility shall remain descriptive rather than relational.

Example:

`Commonly used with portable extraction systems and supported hose assemblies.`

The system shall not represent compatibility as guaranteed unless a reliable source of truth is available.

## Related Products

Related-product configuration may support:

* Customers Also Chose
* Accessories
* Replacement products
* Commonly paired items
* Out-of-stock alternatives

Related products should be validated against current product status and inventory before display.

## Merchandising Tags

Optional tags may support:

* Application filters
* Use-case filters
* Product grouping
* Internal search
* Featured product logic

## Staff Editing

Authorized staff may:

* Add or update application text
* Add or update compatibility text
* Add or remove related products
* Update supplemental technical notes
* Maintain merchandising tags

## Audit Treatment

Routine merchandising edits do not require full inventory-level audit logging.

Inventory-affecting or system-control changes remain subject to audit requirements.

## Nightly Synchronization

Where product metadata is sourced from external systems:

→ Scheduled nightly sync
→ Match by SKU / product identifier
→ Update configured fields
→ Preserve middleware-managed custom fields
→ Record sync status

## Data Conflict Rule

If external product metadata and middleware-managed custom metadata overlap:

* Vendor-system fields remain in their assigned domain.
* Custom middleware fields remain separately managed.
* One field shall not silently overwrite another system’s authoritative value.
