# Epics List: Network Franchise Administration (NFA)

These Epics bucket the high-level features into logical streams of work, allowing the development team to understand the overarching business goals.

## Epic 1: Core Infrastructure, Security, & Authentication
**Description:** Establish the foundational backend architecture, authentication flows (Admin web vs. Mobile OTP), Role-Based Access Control (RBAC), and global database environments.
**Business Value:** Ensures the system is secure, compliant, and correctly permissions the three distinct layers of users (Admin -> Head Office -> Store).

## Epic 2: Global Admin Console (HQ Management)
**Description:** Build the highest-level operational dashboard where Super Admins can govern the entire network, create Head Office instances, manage global Suppliers, and oversee the global Products catalog.
**Business Value:** Gives the proprietary owners total control over what is sold in the network and who has access to distribute it.

## Epic 3: Head Office Hub & Business Intelligence
**Description:** Develop the web portal tailored for regional Head Office managers, including the high-level Dashboard visualizations, granular user management, and real-time network KPIs.
**Business Value:** Empowers regional franchises to make data-driven decisions regarding stock movement, top templates, and store compliance.

## Epic 4: Stock, Supply Chain, & Store Provisioning
**Description:** Implement the sophisticated flow for managing warehouse stock, transferring products directly to individual Stores, and tracking the historical movement logs.
**Business Value:** Guarantees auditability of physical and digital goods across the ecosystem and prevents localized out-of-stock environments.

## Epic 5: The InDesign Template Engine
**Description:** Create the end-to-end engine allowing Head Offices to upload `.indd` packages, map embedded variable tags to dynamic database fields, and asynchronously generate customized, print-ready PDFs for local stores.
**Business Value:** Digitizes and standardizes the marketing efforts across thousands of franchisees while maintaining strict brand compliance.

## Epic 6: Multi-Tier Ordering & E-Commerce
**Description:** Build the catalogue browsing, cart logic, and checkout pipeline (including Stripe SEPA bank mandates) utilized by both the Head Office ordering for stores, and the Stores ordering directly from the Mobile App.
**Business Value:** Generates the core revenue stream by allowing seamless bulk supply purchasing and customized local marketing asset requests.

## Epic 7: Mobile Store Experience
**Description:** Develop the iOS/Android mobile application allowing local Store Managers to easily authorize payments, adjust local pricing variables on PDFs, and restock supplies from the palm of their hand.
**Business Value:** Maximizes operational efficiency and adoption at the lowest level of the franchise network by providing an incredibly low-friction ordering interface.
