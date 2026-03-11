# NFA — Detailed Task Specifications (Sprint 2)

> **Purpose:** Detailed implementation guidance for Sprint 2 (Value Delivery). Every task includes a description, acceptance criteria, and implementation notes (Item 2) to guide engineers during execution.

---

## EPIC-02 · Admin Panel — Network Management

### STORY-06 · Head Office Detail

#### T-06-01 `[FE]` Build HO Detail Drawer/Page
**Description:**
Build a side-drawer or full page displaying the complete details of a specific Head Office.
**Acceptance Criteria:**
- [ ] Renders per Figma spec including company logo, legal entity, and contact info blocks.
- [ ] Drawer can be closed to return to the previously filtered list state without a page refresh.
**Tech Notes / Implementation Guidance:**
- Use a routing-aware drawer (e.g. `?ho_id=123`) so managers can share links to specific Head Office profiles.

#### T-06-02 `[BE]` GET /admin/head-offices/:id
**Description:**
Endpoint retrieving full Head Office entity profile.
**Acceptance Criteria:**
- [ ] Retrieves all fields belonging to the HO.
- [ ] Ensures 404 is thrown if an invalid ID is requested.
**Tech Notes / Implementation Guidance:**
- Include statistics summary inside the payload (e.g., total active stores under this HO).

#### T-06-03 `[WIRE]` Connect Detail View to API
**Description:**
Wire the drawer UI to fetch data dynamically when opened.
**Acceptance Criteria:**
- [ ] Shows a loading skeleton while the `GET /admin/head-offices/:id` is executing.
**Tech Notes / Implementation Guidance:**
- Use a data-fetching library like `react-query` or `SWR` to cache identical requests and optimize performance.

---

## EPIC-03 · Admin Panel — Product & Supplier Mgmt

### STORY-07 · Product Management

#### T-07-01 `[FE]` Build Product List Page
**Description:**
Data table showing the master catalogue of all products managed by the Admin.
**Acceptance Criteria:**
- [ ] Paginated table mapping directly to the products database.
- [ ] Text search and multi-select category filter.
- [ ] Include an "Add Product" primary CTA.
**Tech Notes / Implementation Guidance:**
- Must scale to 10k+ rows (server-side pagination only).

#### T-07-02 `[FE]` Build Add/Edit Form UI
**Description:**
A comprehensive multi-section form to create or modify products in the system.
**Acceptance Criteria:**
- [ ] Sections for: General (Title, SKU, Description), Assets (Image upload), Variables/Pricing.
- [ ] Required fields enforce validation before submittal.
- [ ] File upload UI includes progress and drag-and-drop state.
**Tech Notes / Implementation Guidance:**
- Break form into logical `Fieldset` partials to keep the component cleanly organized. Use `FormData` to handle image blobs.

#### T-07-03 `[BE]` GET /admin/products & GET /admin/products/:id
**Description:**
Paginated catalogue API for Admins to manage master pricing and availability.
**Acceptance Criteria:**
- [ ] Handles query parameters `?page`, `?search`, `?category`.
- [ ] Returns structured product variants alongside the main product entity.
**Tech Notes / Implementation Guidance:**
- Setup indices on `SKU` and `Product Name` column.

#### T-07-04 `[BE]` POST /admin/products
**Description:**
Endpoint to ingest a new product.
**Acceptance Criteria:**
- [ ] Requires Super Admin authorization.
- [ ] Validates payload schema completely.
- [ ] If multipart form contains image, uploads image to S3 (or equivalent) and stores URL mapping.
**Tech Notes / Implementation Guidance:**
- Enforce transactional integrity when saving the Product and its related Variants (all pass, or all roll back).

#### T-07-05 `[BE]` PUT /admin/products/:id
**Description:**
Endpoint to update existing product schemas.
**Acceptance Criteria:**
- [ ] Supports partial updates (PATCH style).
- [ ] Properly handles replacing product image assets.
**Tech Notes / Implementation Guidance:**
- Avoid deleting and recreating variants; identify and update existing UUIDs where possible.

#### T-07-06 `[WIRE]` Connect Product CRUD
**Description:**
Hook up the API calls to the FE table and form elements.
**Acceptance Criteria:**
- [ ] Images successfully display immediately after uploading due to local blob preview or cache invalidation.
- [ ] Toast notifications confirm successful add/edit.
**Tech Notes / Implementation Guidance:**
- Utilize optimistic UI updates on the table while the `PUT` or `POST` call resolves in the background.

---

## EPIC-05 · Head Office — Store Network Management

### STORY-12 · Store List

#### T-12-01 `[FE]` Build Stores List Page
**Description:**
List of all active stores belonging to the currently logged-in Head Office.
**Acceptance Criteria:**
- [ ] Data table UI matches Figma HO dashboard styling.
- [ ] Filters by "Store Status" (Active, Disabled, Pending Setup).
- [ ] "Create Store" button on the top right.
**Tech Notes / Implementation Guidance:**
- Use shared table component created in Sprint 1 to ensure visual consistency.

#### T-12-02 `[FE]` Build Store Empty State
**Description:**
The fallback UI for immediately after an HO registers but before they add stores.
**Acceptance Criteria:**
- [ ] Empty state illustration/icon with direct CTA to the store creation wizard.
**Tech Notes / Implementation Guidance:**
- Ensure it centers gracefully on all screen resolutions.

#### T-12-03 `[BE]` GET /ho/stores
**Description:**
API ensuring an HO only sees stores tied to their `ho_id`.
**Acceptance Criteria:**
- [ ] Security strictly asserts `user.ho_id == store.ho_id`.
- [ ] Supports pagination.
**Tech Notes / Implementation Guidance:**
- Validate `ho_id` directly from the JWT; ignore any `ho_id` passed by the client.

#### T-12-04 `[WIRE]` Connect Store List API
**Description:**
Wire the list view to the HO stores API route.
**Acceptance Criteria:**
- [ ] Seamless filter applications trigger refetching.
**Tech Notes / Implementation Guidance:**
- Debounce text inputs 500ms to avoid unnecessary API roundtrips.

---

### STORY-13 · Store Creation

#### T-13-01 `[FE]` Build Store Creation Form
**Description:**
Multi-segmented form gathering all vital setup info for a store.
**Acceptance Criteria:**
- [ ] Organized into tabs/accordions: 1) General Info 2) Legal Entity 3) Main Address & Shipping Address.
- [ ] Email field validation to ensure valid invite email.
**Tech Notes / Implementation Guidance:**
- Form validation library (e.g. Zod) should evaluate all tabs on submission, jumping the user back slightly if errors exist on hidden tabs.

#### T-13-02 `[BE]` POST /ho/stores
**Description:**
Endpoint capturing new store entities.
**Acceptance Criteria:**
- [ ] Store entity is created and permanently linked to the auth token's `ho_id`.
- [ ] Triggers a transactional invite email to the manager email specified.
**Tech Notes / Implementation Guidance:**
- Do not let clients pass `ho_id` directly to prevent manipulating other organizations. Inherit from server-side token identity.

#### T-13-03 `[WIRE]` Connect Fetching & UI Handling
**Description:**
Handle creation validation states.
**Acceptance Criteria:**
- [ ] Navigates user back to the store list automatically on successful 201 Created.
**Tech Notes / Implementation Guidance:**
- Must catch HTTP 409 (Conflict) explicitly gracefully if identical email exists across the network.

---

## EPIC-09 · Mobile App (Store) End-to-End Ordering

### STORY-25 · Mobile Catalogue Browse

#### T-25-01 `[FE]` Build Catalogue Screen
**Description:**
Primary shopping grid on the mobile app displaying active products.
**Acceptance Criteria:**
- [ ] Render 2-column or 1-column grid seamlessly using standard React Native FlatList constraints.
- [ ] Include top search bar and scrollable category pills horizontally above the grid.
**Tech Notes / Implementation Guidance:**
- Lazy-load images with an appropriate placeholder to conserve device memory.

#### T-25-02 `[FE]` Build Product Detail View
**Description:**
Expanded details showing inputs required from the user.
**Acceptance Criteria:**
- [ ] Hero Image carousel, Price, Title, and Description.
- [ ] Renders dynamic form fields if standard variables must strictly be filled (e.g., Size, Material).
- [ ] Persistent "Add to Cart" sticky footer at the bottom with quantity selector.
**Tech Notes / Implementation Guidance:**
- Form fields must map directly to API-driven `variant` definitions, do not hard code specific selectors (sizes/colors) unlinked from data payload.

#### T-25-03 `[BE]` GET /mobile/catalogue
**Description:**
Fetch product lines authorized for this store.
**Acceptance Criteria:**
- [ ] Reads the Store's `ho_id` and queries all products mapped into that HO catalogue safely.
**Tech Notes / Implementation Guidance:**
- Do not transmit deleted or deactivated SKUs. Implement offset cursor pagination due to mobile performance limits versus strict desktop.

#### T-25-04 `[BE]` GET /mobile/catalogue/:id
**Description:**
Deep-dive single product item load.
**Acceptance Criteria:**
- [ ] Provide full variant tree and attribute matrix required.
**Tech Notes / Implementation Guidance:**
- Optimize the payload to strictly the parameters a device needs to render the screen.

#### T-25-05 `[WIRE]` Connect Mobile Catalogue API
**Description:**
Connect UI interaction to the API endpoints and local caching layer.
**Acceptance Criteria:**
- [ ] Pull to refresh re-initializes `page 1` successfully.
- [ ] Navigating inside item view and clicking "Back" retains scroll position.
**Tech Notes / Implementation Guidance:**
- A robust query state manager (`urql` or React Query specific for RN) prevents duplicate API roundtrips when paging back and forth.

---

### STORY-26 · Mobile Cart & SEPA Order Placement

#### T-26-01 `[FE]` Build Cart Screen
**Description:**
Review line items and quantities before finalization.
**Acceptance Criteria:**
- [ ] List maps exactly to user-selected variants and quantities.
- [ ] User can swipe-to-delete line items.
- [ ] Total calculates immediately upon a quantity + / - adjust.
**Tech Notes / Implementation Guidance:**
- Ensure subtotal explicitly separates from shipping/taxes.

#### T-26-02 `[FE]` Build Order Confirmation Screen
**Description:**
The final gate mapping to an active SEPA trigger.
**Acceptance Criteria:**
- [ ] Explicitly states: "By confirming, your associated SEPA account (IBAN ending in X) will be charged."
- [ ] Success state transitions into the "Order Placed" celebratory screen.
**Tech Notes / Implementation Guidance:**
- Use Lottie animations for the celebratory success screen to improve perceived value.

#### T-26-03 `[BE]` GET /mobile/cart (State Machine)
**Description:**
Return the server-side authorized cart state to prevent client tempering.
**Acceptance Criteria:**
- [ ] Pulls the persistent cart for the user safely based on auth token.
**Tech Notes / Implementation Guidance:**
- Re-verify all item unit prices against the DB master index. Reject invalid prices.

#### T-26-04 `[BE]` PUT /mobile/cart
**Description:**
Updates quantities and selections persistently against the user session.
**Acceptance Criteria:**
- [ ] Synchronizes line items. If item count = 0, prune it from the DB payload altogether.
**Tech Notes / Implementation Guidance:**
- Simple JSON payload updates (`{ item_id, quantity }`). Ensure you handle lock constraints if multiple users share an account.

#### T-26-05 `[BE]` POST /mobile/orders (SEPA Trigger)
**Description:**
Charge handling routing inside the backend via Stripe SDK trigger.
**Acceptance Criteria:**
- [ ] Confirms cart values one last time.
- [ ] Captures `SetupIntent` and generates a live `PaymentIntent` via Stripe utilizing the off-session SEPA Mandate on file.
- [ ] Generates Order ID linking tracking numbers.
**Tech Notes / Implementation Guidance:**
- Mark database status as `Processing_Payment` until the Stripe Webhook explicitly returns `payment_intent.succeeded` for SEPA clearance (can take days). Let the store user know it is "Placed successfully".

#### T-26-06 `[WIRE]` Connect Cart/Confirmation flows
**Description:**
Wire checkout APIs dynamically evaluating success.
**Acceptance Criteria:**
- [ ] "Checkout" button locks (grey/spinner) explicitly to prevent double tapping logic while API triggers Stripe `PaymentIntent`.
- [ ] Navigate away explicitly flushes local cart context entirely.
**Tech Notes / Implementation Guidance:**
- Handle Stripe `RequiresAction` cleanly via the Mobile Frontend SDK in case SCA (Strong Customer Authentication) unexpectedly requires device intervention.
