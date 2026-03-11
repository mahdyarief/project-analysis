# NFA — Project Overview & Assumptions

> **Project:** NFA (Network Franchise Administration)
> **Analysis Date:** 2026-03-11
> **Apps in Scope:** Admin Panel · Head Office · Mobile App (Store)

---

## 1. Project Summary

NFA is a **B2B multi-tenant SaaS platform** enabling franchise networks to manage the full lifecycle of **print/merchandise production and distribution** across their store network.

The system has **three distinct user-facing applications**:

| App | Users | Primary Goal |
|-----|-------|-------------|
| **Admin Panel** | Super Admins (internal ops) | Manage network: head offices, suppliers, products, global orders |
| **Head Office** | Franchise group managers | Manage stores, catalogue, stock, templates, orders, dashboard analytics |
| **Mobile App (Store)** | Individual store owners/staff | Browse catalogue, add to cart, place and track orders |

---

## 2. Core Business Domain

This is a **Print-on-Demand + Distribution Network Management** platform:
- Head Offices define **templates** (InDesign files) → system generates per-store PDFs
- Head Offices manage **stock** and redistribute to stores
- Stores order via mobile app using **SEPA direct debit** (Stripe)
- Admins oversee the entire multi-network ecosystem

---

## 3. Key Assumptions

| # | Assumption | Category |
|---|-----------|----------|
| A1 | **Authentication** uses email+password for Admin Panel and Head Office; Mobile uses **OTP via email** (passwordless) | Auth |
| A2 | **Stripe** is the payment processor for SEPA mandate setup and billing | Payment |
| A3 | InDesign template files (.idml/.indd) are uploaded by Head Office and parsed server-side to extract variable tags | Template Engine |
| A4 | PDF generation from templates is an **async background job** (queue-based, not real-time) | Architecture |
| A5 | Multi-tenant isolation: each Head Office has its own workspace; stores belong to one Head Office | Data |
| A6 | The Mobile App is a **React Native or Flutter** application (cross-platform) | Tech |
| A7 | Admin Panel and Head Office are **web apps** (React/Next.js) | Tech |
| A8 | REST API backend with JWT authentication; separate auth flows for each app type | API |
| A9 | "Local Price" is a per-store variable that stores can override on product variants | Business Logic |
| A10 | Stock history tracking is real-time (not batch processed) | Analytics |

---

## 4. User Personas

| Persona | App | Key Actions |
|---------|-----|------------|
| **Super Admin** | Admin Panel | CRUD on head offices, suppliers, products; view all global orders |
| **HO Manager** | Head Office | Manage stores, catalogue, templates, stock, orders, account, dashboard |
| **Store Owner/Staff** | Mobile App | Browse catalogue, order, track deliveries, manage SEPA |

---

## 5. Open Questions for Product Owner

1. **Template PDF Generation SLA:** What is the expected turnaround time for InDesign template processing? Is there a max file size? What happens when the queue is overloaded?
2. **Stock Ownership Model:** Does the Head Office own one central warehouse, or can multiple warehouses exist per Head Office?
3. **SEPA Mandate Flow:** Who sets up the SEPA mandate — the store owner or the Head Office? Does it need Head Office approval?
4. **Order Approval Workflow:** Does a Head Office need to approve store orders before fulfillment, or are they auto-approved?
5. **Mobile App Distribution:** Is the Mobile App distributed via App Store/Google Play, or is it an internal/enterprise distribution?
6. **Admin Panel Access:** Is the Admin Panel accessible from the internet or only via VPN/internal network?
7. **Duplicate Order Feature:** The mobile app allows duplicating an order — does this pre-fill all fields including price, or just the product list?
8. **Localization:** The screens are in French — is multi-language support required, or is French the only supported language for this release?

---

## 6. Tech Stack Assumptions (for Sprint estimation)

| Layer | Assumed Stack |
|-------|--------------|
| Frontend (Web) | React + Next.js (Admin Panel + Head Office) |
| Frontend (Mobile) | React Native or Flutter |
| Backend | Node.js (NestJS) or Python (FastAPI) — REST API |
| Database | PostgreSQL (relational: orders, products, stores) |
| File Storage | AWS S3 or equivalent (InDesign files, generated PDFs) |
| Background Jobs | Bull/BullMQ or Celery (PDF generation queue) |
| Authentication | JWT + Refresh Tokens; OTP via email (Mobile) |
| Payment | Stripe (SEPA Direct Debit) |
| Infrastructure | Docker + CI/CD pipeline |
