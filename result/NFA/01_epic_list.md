# NFA — Epic List

> **Project:** NFA (Network Franchise Administration)
> **Total Epics:** 9 | **Coverage:** Admin Panel + Head Office + Mobile App

---

## Epic Overview

```
EPIC-01  Authentication & Access Control
EPIC-02  Admin Panel — Network Management
EPIC-03  Admin Panel — Product & Supplier Management
EPIC-04  Head Office — Dashboard & Analytics
EPIC-05  Head Office — Store Network Management
EPIC-06  Head Office — Catalogue & Template Management
EPIC-07  Head Office — Stock & Inventory Management
EPIC-08  Head Office — Order Management
EPIC-09  Mobile App (Store) — End-to-End Ordering
```

---

## EPIC-01 · Authentication & Access Control

**Business Value:** No user can do anything without being securely logged in. This is the entry gate for all three apps.

**Scope:**
- Admin Panel: Email + Password login with clear error states
- Head Office: Email + Password login with validation states, forgot password flow
- Mobile App: OTP (One-Time Password) via email — passwordless login
- First-time SEPA payment setup flow (Mobile)

**Apps Affected:** Admin Panel · Head Office · Mobile App

---

## EPIC-02 · Admin Panel — Network Management

**Business Value:** Admins need to oversee and manage the entire franchise ecosystem — multiple Head Offices — from a single interface.

**Scope:**
- List all Head Offices with search and country filter
- View Head Office details
- Access and navigate into a Head Office's environment

**Apps Affected:** Admin Panel

---

## EPIC-03 · Admin Panel — Product, Supplier & Order Management

**Business Value:** Admins control the master product catalog and supplier relationships that all Head Offices operate from.

**Scope:**
- Product management: list, create, edit products with search/filter/pagination
- Supplier management: list, create, edit suppliers with search/filter
- Global Orders: view all orders across all Head Offices with filters; access order details
- Account management: view/edit admin user profile

**Apps Affected:** Admin Panel

---

## EPIC-04 · Head Office — Dashboard & Analytics

**Business Value:** Managers need at-a-glance performance indicators to make operational decisions without diving into raw data.

**Scope:**
- KPI dashboard: key business metrics
- "Orders with Issues" alert block: surface problematic orders
- Network overview widgets

**Apps Affected:** Head Office

---

## EPIC-05 · Head Office — Store Network Management

**Business Value:** Head Office manages their store network — adding new stores, monitoring status, tracking activity.

**Scope:**
- Store list: search, filter, CRUD actions
- Store creation form: general info, legal, addresses (multi-step or drawer)
- Store detail view: info + compliance + activity
- Empty state for no stores
- Account / User management: view Head Office account info, list users, edit users

**Apps Affected:** Head Office

---

## EPIC-06 · Head Office — Catalogue & Template Management

**Business Value:** The catalogue defines what stores can order. Templates are the core of the print production workflow — this is the platform's core differentiator.

**Scope:**

**Catalogue:**
- Browse product catalogue (templates + standard products) with loading/empty/error states
- Product filters and search

**Templates:**
- Template list with status states (loading, empty, populated)
- Archive a template
- Template creation wizard (4 steps):
  - Step 1: Select support/format
  - Step 2: Name template + upload InDesign package
  - Step 3: Map InDesign tags to system fields
  - Step 4: Review summary and confirm creation
- Upload success feedback + tag detection display
- Background async PDF generation status tracking
- Template detail view: status, PDF generation progress, variable mapping

**Apps Affected:** Head Office

---

## EPIC-07 · Head Office — Stock & Inventory Management

**Business Value:** Visibility and control over stock levels enables Head Office to proactively restock stores and prevent out-of-stock situations.

**Scope:**
- Warehouse stock view: total value, unit counts, product list with search/filter/export
- Send stock from warehouse to a store: panel with store selection + quantity input + validation
- Confirm send + success/error feedback
- Stock movement history: chronological log of in/out movements, filterable by type/period, exportable

**Apps Affected:** Head Office

---

## EPIC-08 · Head Office — Order Management

**Business Value:** Head Office must track and manage all orders placed by their stores, identify anomalies, and access full order details.

**Scope:**
- Order list: filters by status, date, store; loading/empty/error states
- Order detail view: full order information
- Cart: view cart (empty or filled), adjust quantities/destinations, subtotal/shipping/total summary, modify cart items
- Cart modification flow

**Apps Affected:** Head Office

---

## EPIC-09 · Mobile App (Store) — End-to-End Ordering

**Business Value:** The Mobile App is the primary touchpoint for individual store owners. A smooth, self-contained ordering experience directly impacts revenue velocity.

**Scope:**

**Authentication:**
- OTP login: enter email → receive OTP → enter OTP → access app
- SEPA mandate setup (first order): configure SEPA payment via Stripe

**Catalogue:**
- Browse catalogue with search + filters + loading/empty/error states
- Product detail: view info, fill required fields, trigger order
- Product error states with retry

**Cart & Orders:**
- Cart view: item list, quantities, delete items, total
- Order confirmation (SEPA) + success/error feedback
- Order list: search + filter by status + loading/error/empty states
- Order detail: full info + duplicate order action
- Price modification: edit "Local Price" variable per item via modal

**Profile:**
- View profile + SEPA mandate status
- Edit profile + activate/manage SEPA via Stripe

**Apps Affected:** Mobile App

---

## Epic Summary Table

| Epic | Name | Apps | Sprint Target | Complexity |
|------|------|------|--------------|-----------|
| EPIC-01 | Authentication & Access Control | All | Sprint 1 | High |
| EPIC-02 | Admin — Network Management | Admin | Sprint 1 | Medium |
| EPIC-03 | Admin — Product/Supplier/Order Mgmt | Admin | Sprint 1-2 | Medium |
| EPIC-04 | HO — Dashboard & Analytics | HO | Sprint 2 | Medium |
| EPIC-05 | HO — Store Network Management | HO | Sprint 1-2 | Medium |
| EPIC-06 | HO — Catalogue & Template Mgmt | HO | Sprint 2 | High |
| EPIC-07 | HO — Stock & Inventory | HO | Sprint 2 | Medium |
| EPIC-08 | HO — Order Management | HO | Sprint 1-2 | Medium |
| EPIC-09 | Mobile App — E2E Ordering | Mobile | Sprint 1-2 | High |
