# Project Overview: Network Franchise Administration (NFA)

## 📌 Elevator Pitch
NFA is a comprehensive B2B SaaS platform designed to manage franchise networks, specifically focusing on product distribution, template management (print/merchandise), and multi-tier ordering. The ecosystem supports overarching Admins, regional Head Offices, and local Store managers, streamlining the supply chain and localized marketing asset generation.

## 👥 Target Personas
1. **Super Admin (Admin Panel)**: Manages the global network, creates Head Offices, manages global Products, and oversees Global Orders and Suppliers.
2. **Head Office Manager (Head Office App)**: Oversees a specific region or franchise group. They manage local Stores, control Stock distribution, upload InDesign Templates for localized printing, and place bulk orders.
3. **Store Manager (Mobile App)**: The end-user at the local shop level. They use a mobile app to log in via OTP, set up SEPA payments, order stock/templates from the Catalogue, and track their local orders.

## 🏢 Platform Ecosystem
- **Admin Panel (Web)**: Global management and oversight.
- **Head Office App (Web)**: Regional management, template creation, and stock distribution.
- **Mobile Store App (iOS/Android)**: Local ordering and store profile management.

## 🛠️ Tech Stack & Architecture Assumptions
- **Frontend (Web)**: React.js (Next.js recommended for SEO routing if public, but SPA is sufficient for internal tools)
- **Frontend (Mobile)**: React Native (to share logic with Web) or Flutter
- **Backend**: Node.js (NestJS or Express) / Python
- **Database**: PostgreSQL (ideal for multi-tenant relational data like Users, Stores, Orders, Stocks)
- **Authentication**: JWT based. OTP via Email for Mobile (SendGrid/AWS SES).
- **Payment Processing**: Stripe API (specifically SEPA Direct Debit mandates for stores).
- **File Processing**: InDesign Server or third-party API (like PrintOS) to parse InDesign packages, extract variable tags, and generate PDF outputs. AWS S3 for storage.

## ❓ Open Questions & Risks
1. **Template Generation Engine**: Does a backend engine already exist to parse InDesign files and map variables, or does this need to be built from scratch? This is a massive technical capability.
2. **SEPA Mandates**: Does the Store onboarding strictly block ordering until the Stripe SEPA mandate is verified by the bank (takes up to 14 days), or can they act on credit?
3. **Admin Provisioning**: Since the Admin has no "Forgot Password" or "Change Password" flow (per design constraint), how are Admin credentials securely rotated?
