# Website Sitemap — Implemented Academic Demo

This is a navigation view of the static browser prototype, not a claim of real account or inventory services.

```mermaid
flowchart TD
  H["Home"] --> P["Products / Category Browsing"]
  P --> D["Product Details"]
  D --> C["Cart"]
  C --> K["Simulated Checkout"]
  K --> O["Demonstration Confirmation"]
  H --> L["Locations"]
  H --> S["Special Orders"]
  H --> A["About"]
  H --> T["Contact"]
```

The corresponding HTML pages are maintained in [Implementation/Academic Website](../../Implementation/Academic%20Website/). The fuller design rationale and proposed account/administrative pathways appear in [Information Architecture](information%20architecture.md). Mermaid is used for an exportable diagram; no dynamic checkout service is represented here.
