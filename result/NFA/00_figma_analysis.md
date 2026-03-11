# Figma Analysis & Design Specifications

## 🛑 Strict Design Constraints & UX Rules (Extracted via Figma MCP)
These specific rules were found directly in the developer handoff notes and comments from the design team on the Figma master file. They **must** be implemented exactly as stated to fulfill standard acceptance criteria:

*   **Rule 1: No Admin Self-Service Security.** The Super Admin persona does **not** have a "Change Password" or "Forgot Password" flow. (If they trigger an error, it is a hard stop).
*   **Rule 2: "Store Shop Preview" is Deprecated.** Do not build a standalone "Store Shop Preview" navigation item. It must be seamlessly integrated directly inside the standard `Catalogue` view instead of acting as its own product page.
*   **Rule 3: Unified "Cart" Pattern.** The Cart icon/button must mirror major marketplaces. It must be locked into the **top right corner** exclusively when inside the `Catalogue` context.
*   **Rule 4: Global "My Account" Position.** The "My Account" dropdown/button must permanently live in the **top right corner** of every single application layout.
*   **Rule 5: Table Utilities.** Any primary table view (like Orders or Stocks) must include an "Export CSV" feature.
*   **Rule 6: Impersonation Mechanics.** The "Impersonate" feature (e.g., Head Office into Store) acts as a direct auth injection. It does not load an intermediate "Impersonation UI" screen. The user is just functionally logged in as the target.

---

## 🧭 Deep Page-by-Page Feature Breakdown
This section outlines the exact components, data entities, and interactions required on a page-by-page basis across the three platform applications based on a deep review of the UI hierarchy.

### 1. Admin Panel (React Web SPA)
| Screen | Required Features & Visual Mechanics |
|--------|------------------------------------|
| **Login** | Email/Password inputs. Button remains disabled until regex validation passes. Show/hide password eye icon. Strict invalid credential error states. |
| **Account** | Logout button triggering a destructive confirmation modal. |
| **Head Office** | **List View:** Search bar, table. **Drawer (Right):** Read-only details of the Head Office (HO) entity. **Create Flow:** multi-step form, review confirmation before API POST. **Archive Action:** destructive confirmation modal with immediate visual feedback. |
| **Suppliers** | **List View:** Global search, specific "Filter by Country" dropdown. **Create/Edit Flow:** Modals for updating coords/address. **Delete Action:** Destructive modal. |
| **Products** | **List View:** Search, complex filters, standard pagination. **Create Flow (Drawer):** Text fields, rich image uploader, validation block. **Edit/Archive/Delete:** Must include visible skeleton loading states during API transitions to prevent duplicate clicks. |
| **Orders** | **List View:** Global orders across all HOs. Heavy filtering required. **Drawer:** Display order timeline, price recap, and line items. |

### 2. Head Office Portal (React Web SPA)
| Screen | Required Features & Visual Mechanics |
|--------|------------------------------------|
| **Login** | Standard Login. Includes a functional "Forgot Password" request flow that sends a reset link to the email. |
| **Dashboard** | **KPI Blocks:** Total Spend, Total Orders, Avg Spend/Store, Active Stores, eShop Adoption. **Widgets:** "Orders with Issues" list, "Top Templates" rankings. **Drawers:** Clicking any widget slides out a Right Drawer for deep-dive tabular data. Skeleton loaders required on mount. Error state with "Try again" refresh button. |
| **Stores** | **List View:** Table of local shops. **Create Flow:** Massive form splitting Info, Legal, Address. **Drawer:** Read-only info + Compliance status + Recent Activity feed. Empty state illustration when zero stores exist. |
| **Stock** | **List View:** Value metrics, available units, product table. Export CSV capability. **Send Stock Flow:** Select target Store -> Input Qty -> Validate -> Confirm payload. **History:** Log of all In/Out movements with date range pickers. |
| **Catalogue** | Tab system for "Templates" vs "Standard Products". Loading/Empty states required. **Detail View:** Assign product to a specific entity/store. **Shop Visibility Toggle:** Immediate success/error toast notification on toggle. Qty selector. Add to Cart. |
| **Templates** | **List View:** Cards of InDesign assets. **Creation Wizard (6 Steps):** 1) Format selection 2) Name & Upload `.indd` package 3) System scans file & returns variable tags 4) Map tags to system data fields 5) Review & Confirm 6) Generation kicks off in background. |
| **Cart** | List line items. Adjust Qty. Ability to completely change the destination Store for a specific line item. Subtotal/Shipping/Total breakdown. Confirm Order (Checkout). |
| **Orders** | Table view with filters. Empty/Error states. Drawer timeline. |
| **Account** | HO Info block. "Users List" table. Edit User modal (change Name, Email, Role permissions). |

### 3. Store Mobile App (iOS / Android)
| Screen | Required Features & Visual Mechanics |
|--------|------------------------------------|
| **Login** | Passwordless Auth. Input Email -> Prompt for OTP -> Input 6-digit OTP -> Logged In. Resend OTP timer logic. |
| **Profile** | Read-only user data. Critical "SEPA Mandate" status block. Button triggering Stripe Elements wrapper to setup/edit bank DD mandate. |
| **Catalogue** | Infinite scroll list. Search, category filters. **Detail Page:** Quantity picker, Add to Cart. Must gracefully handle network errors with Retry button. |
| **Cart** | Swipe-to-delete items. Adjust quantities. Final Checkout button (hooks into SEPA mandate for automated local billing). |
| **Orders** | Status tabs (Pending, Delivered). **Detail View:** Duplicate entire historical order to Cart. **Price Adjust Popup:** Store manager can manually override the "Local Price" variable on the item for their specific shop's PDF templates. |
