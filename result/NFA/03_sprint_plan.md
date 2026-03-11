# Sprint Plan: Overview & Phasing

*Velocity Rules: To ensure team success, Sprints are capped at approximately 80 Story Points (SP). Any features exceeding the bounds of Sprint 1 and Sprint 2 have been delegated to the general Backlog (Sprint 3+).*

---

## 🏃 Sprint 1: "The Walking Skeleton" (Foundation)
**Total Estimated SP:** 67 SP
**Goal:** Prove the foundational architecture works. The team focuses heavily on standing up the core backend engines, securing the environments with JWT/OTP authentication, managing database relationships, and launching the central Administrative dashboard where Super Admins can provision Head Offices. Without this sprint, no other persona can enter the apps.

**Scope:**
1. **Epic 1: Core Infrastructure & Auth (27 SP)**
   - Initial database migrations and relational mapping (Postgres).
   - JWT Auth for Web, SendGrid OTP payload logic for mobile.
   - Frontend and Backend integration for login on all 3 clients.
2. **Epic 2: Global Admin Console (29 SP)**
   - Full CRUD endpoints and UI for Head Offices, Global Products, and Suppliers.
3. **Epic 4: Stock, Supply Chain (Partial - 11 SP)**
   - Basic Inventory ledger API.
   - Stock Table UI rendering.

***

## 🚀 Sprint 2: "Value Delivery" (Operations & E-Commerce)
**Total Estimated SP:** 74 SP
**Goal:** Deliver the multi-tenant business value. Enable Head Offices to view their business intelligence dashboards, create localized Stores, and allow the actual checkout/ordering flow via Stripe integration. 

**Scope:**
1. **Epic 3: Head Office Hub & Business Intelligence (30 SP)**
   - Advanced aggregations for KPI dashboards (Spend, Top Templates).
   - Dashboard UI with complex drawer sliding actions and skeleton loaders.
   - Store Management table architecture.
2. **Epic 6: Multi-Tier Ordering & E-Commerce (44 SP)**
   - Stripe API setup (SEPA mandate endpoints).
   - Core Cart sub-totaling engine.
   - Catalogue views across the Head Office environment.
   - The entire cart and checkout payload flow.

***

## 📦 General Backlog (Future Sprints due to Velocity Caps)
**Total Estimated SP:** 77 SP
**Reasoning:** Attempting to build a bespoke InDesign server engine and a fully native iOS/Android shell concurrently with Web development represents massive technical risk and breaks the 80 SP-per-sprint rule. They will be sequenced after Web/API validation.

**Deferred Scope:**
1. **Epic 5: The InDesign Template Engine (50 SP)**
   - API integration to parse InDesign files.
   - Upload UI and Field Mapping Wizard.
   - Asynchronous PDF generation queue architectures.
2. **Epic 7: Mobile Store Experience (27 SP)**
   - Building the React Native mobile shell.
   - Developing Mobile-specific interactions (Swipe to delete on Cart).
   - Native integration for Stripe Elements wrapper.
