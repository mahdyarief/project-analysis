# NFA — Figma Analysis & Design Constraints

> **Purpose:** Document all technical blockers, constraints, flow-mappings, and feature flags identified explicitly via Figma Integration (Master Design File) before Sprint execution starts.

## 1. Authentication & Security (Admin)
- **No Forgot Password Flow:** Admin users do NOT have a "Forgot Password" or "Password Change" flow accessible on the front-end. Resetting an admin password must require database/backend intervention directly by operations.
- **No Impersonation Sandbox:** There is no dedicated intermediate screen for "Impersonation". When a Super Admin logs into a Head Office account, it directly dumps them into the *live* production environment of that HO.

## 2. Navigation & Shell Layout (Head Office)
- **Standardized Profile Location:** The "My Account" / Avatar area must be rendered at the top-right of the screen globally to match standard application heuristics.

## 3. Product & Catalogue Modifications
- **Store Shop Preview Cut:** The "Store Shop Preview" screen initially floated for the Catalogue navigation has been completely *removed* from the project scope by the design team. Engineering does not need to build or architect this preview view.
- **Mobile E-Commerce Flow:** The "Cart" entrypoint must be accessible from the top-right of the catalogue on Mobile—functioning identically to standard marketplaces (Amazon, Shopify).
- **Export Requirements:** "Export CSV" functionality is explicitly required on data tables (specifically noted by the PO on the data views). This should be implemented as a standard component for tables across Admin/HO.

## 4. Design Systems Notes
- **Figma Variables vs Styles:** Designers are actively migrating typography and colors from "Figma Styles" to "Figma Variables". The frontend engineering team should implement the UI component library using a token-based system (CSS Variables / Tailwind Theme) that easily maps to Figma's new variable architecture.
