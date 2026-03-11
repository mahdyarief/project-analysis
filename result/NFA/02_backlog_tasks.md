# Backlog Tasks: Network Franchise Administration (NFA)

This file contains the high-level breakdown of Epic features into actionable tasks across the three architectural layers: `[FE]`, `[BE]`, `[WIRE]`.  
*Story Point (SP) estimates follow the Fibonacci sequence (1, 2, 3, 5, 8, 13).*

## Epic 1: Core Infrastructure, Security, & Authentication
| Issue Type | Tag | Summary | Story Points |
|------------|-----|---------|--------------|
| Task | `[BE]` | Setup PostgreSQL database schema & user relations (Admin, HO, Store) | 5 |
| Task | `[BE]` | Setup JWT Authentication Service & Role guards | 5 |
| Task | `[BE]` | Implement SendGrid OTP generation API for Mobile | 3 |
| Task | `[FE]` | Develop Admin Web Login UI (Email/Password, Eye icon, Errors) | 2 |
| Task | `[FE]` | Develop HO Web Login UI (Email/Password, Forgot PWD form) | 3 |
| Task | `[FE]` | Develop Mobile Login UI (Email input -> OTP screen) | 3 |
| Task | `[WIRE]`| Integrate Admin & HO Auth APIs with frontend Zustand/Redux state | 3 |
| Task | `[WIRE]`| Integrate Mobile OTP flow & handle token storage | 3 |

## Epic 2: Global Admin Console (HQ Management)
| Issue Type | Tag | Summary | Story Points |
|------------|-----|---------|--------------|
| Task | `[BE]` | Develop CRUD endpoints for Head Offices and Global Products | 5 |
| Task | `[BE]` | Develop CRUD endpoints for Suppliers (Filter by country) | 3 |
| Task | `[FE]` | Develop Admin Layout, Nav, and Global Orders Data Table | 3 |
| Task | `[FE]` | Develop Head Office page (Table, Details Drawer, Archive Modal) | 3 |
| Task | `[FE]` | Develop Product page (Table, Image Upload Drawer, Pagination) | 5 |
| Task | `[FE]` | Develop Supplier page (Table, Create/Edit modale) | 2 |
| Task | `[WIRE]`| Wire all Admin CRUD pages to API, handle pagination/skeletons | 8 |

## Epic 3: Head Office Hub & Business Intelligence
| Issue Type | Tag | Summary | Story Points |
|------------|-----|---------|--------------|
| Task | `[BE]` | Develop Dashboard aggregated KPI endpoints (Spend, Orders, Top Templates) | 8 |
| Task | `[FE]` | Develop HO Dashboard Layout (Widgets, Side Drawers for KPIs) | 5 |
| Task | `[FE]` | Develop "Orders with Issues" widget and empty/error states | 2 |
| Task | `[FE]` | Develop Store Management page (Table, 3-part Creation Form, Activity flow) | 5 |
| Task | `[WIRE]`| Integrate HO Dashboard charts/tables with aggregations API | 5 |
| Task | `[WIRE]`| Wire Store Management CRUD to frontend layout | 5 |

## Epic 4: Stock, Supply Chain, & Store Provisioning
| Issue Type | Tag | Summary | Story Points |
|------------|-----|---------|--------------|
| Task | `[BE]` | Build Inventory ledger API (Stock in/out, transfers to specific Store) | 8 |
| Task | `[FE]` | Develop Stock Table UI (Value metrics, Units, Table) | 3 |
| Task | `[FE]` | Develop "Send Stock" Drawer UI (Target Store, Quantity, Confirmation) | 3 |
| Task | `[FE]` | Develop "Stock History" UI with Date Pickers and CSV Export | 5 |
| Task | `[WIRE]`| Wire Send Stock flow with validation and real-time ledger refresh | 5 |

## Epic 5: The InDesign Template Engine
| Issue Type | Tag | Summary | Story Points |
|------------|-----|---------|--------------|
| Task | `[BE]` | Integrate 3rd-party InDesign parsing API to detect internal variable tags | 13 |
| Task | `[BE]` | Develop Background Worker payload for automated PDF generation | 8 |
| Task | `[BE]` | Build API routes to save mapped variable associations | 5 |
| Task | `[FE]` | Develop Template Creation Wizard (Step 1-6 UI flow) | 8 |
| Task | `[FE]` | Develop Asset Upload dropzone and tag mapping table UI | 5 |
| Task | `[FE]` | Develop Template Details View showing background task generation status | 3 |
| Task | `[WIRE]`| Wire the 6-step Wizard, handle heavy file uploads, and long-polling UI | 8 |

## Epic 6: Multi-Tier Ordering & E-Commerce
| Issue Type | Tag | Summary | Story Points |
|------------|-----|---------|--------------|
| Task | `[BE]` | Setup Stripe API Customer instances and SEPA Mandate hooks | 8 |
| Task | `[BE]` | Develop Cart & Ordering Core Engine (Total/Subtotal logic) | 8 |
| Task | `[BE]` | Develop Catalogue API with "Standard" and "Template" modes | 5 |
| Task | `[FE]` | Develop Cart UI (Subtotals, destination changers, confirmations) | 5 |
| Task | `[FE]` | Develop Catalogue Table (Categories, Grid view, Item detail drawer) | 5 |
| Task | `[WIRE]`| Wire HO and Mobile catalogue data. Connect Cart state arrays. | 8 |
| Task | `[WIRE]`| Connect checkout action to Stripe SEPA charge endpoint | 5 |

## Epic 7: Mobile Store Experience
| Issue Type | Tag | Summary | Story Points |
|------------|-----|---------|--------------|
| Task | `[FE]` | Develop Mobile Profile Tab (Readonly info, Stripe SEPA status block) | 3 |
| Task | `[FE]` | Develop Stripe Elements mobile wrapper modal for SEPA setup | 5 |
| Task | `[FE]` | Develop Mobile Catalogue Infinite Scroll Feed and Detail Page | 5 |
| Task | `[FE]` | Develop Mobile Cart (Swipe to delete, Qty spin box, Checkout btn) | 3 |
| Task | `[FE]` | Develop Mobile Orders History (Tabs, Duplicate order action) | 3 |
| Task | `[WIRE]`| Wire all mobile specific interactions to centralized backend APIs | 8 |
