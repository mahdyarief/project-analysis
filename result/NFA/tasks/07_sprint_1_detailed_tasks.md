# NFA — Detailed Task Specifications (Sprint 1)

> **Purpose:** To provide engineers with detailed implementation guidance, encompassing the task description, testable acceptance criteria, and specific tech notes (Item 2) required for execution.

---

## EPIC-01 · Authentication & Access Control

### STORY-01 · Admin Panel Login

#### T-01-01 `[FE]` Build Admin Login UI
**Description:**
Build the Admin Panel login screen with Email and Password inputs. This is the entry gate for Super Admins.
**Acceptance Criteria:**
- [ ] Renders exactly per Figma design with correct typography and spacing.
- [ ] Email field has client-side validation (must be valid format).
- [ ] Password field has client-side validation (cannot be empty).
- [ ] "Sign In" button is disabled while processing.
- [ ] Displays clear error text if API returns invalid credentials/server error.
**Tech Notes / Implementation Guidance:**
- Use `react-hook-form` and `zod` for form validation.
- DO NOT include a "Forgot Password" link (per Figma decisions).
- Use local state for the loading spinner on the submit button.

#### T-01-02 `[BE]` POST /auth/admin/login
**Description:**
Create an API endpoint to validate Admin credentials and issue secure session tokens.
**Acceptance Criteria:**
- [ ] Accepts `email` and `password` payload.
- [ ] Returns `401 Unauthorized` for incorrect credentials with generic error message.
- [ ] Returns `200 OK` with short-lived JWT (access token) and HttpOnly Refresh token on success.
- [ ] User role in JWT payload must explicitly define `role: 'SUPER_ADMIN'`.
**Tech Notes / Implementation Guidance:**
- Passwords must be hashed using `bcrypt` (salt rounds = 10 or 12).
- Enforce rate limiting on this endpoint (e.g., max 5 requests per minute per IP) to prevent brute force.

#### T-01-03 `[WIRE]` Connect Admin Login API
**Description:**
Wire the Frontend login UI directly to the Backend API. Handle token storage and application routing.
**Acceptance Criteria:**
- [ ] On successful login, the application router navigates to `/admin/head-offices`.
- [ ] JWT access token is securely stored in memory or secure storage (not localStorage).
- [ ] Interceptor is set up to automatically attach the `Authorization: Bearer <token>` to future requests.
- [ ] 401s from the API correctly trigger the FE error toast/state.
**Tech Notes / Implementation Guidance:**
- Create an Axios instance with request/response interceptors to handle token injection and token refresh logic automatically.

---

### STORY-02 · Head Office Login

#### T-02-01 `[FE]` Build HO Login UI
**Description:**
Build the login screen for Head Office managers.
**Acceptance Criteria:**
- [ ] Renders per Figma spec for Head Office app.
- [ ] Email/Password inputs have validation rules.
- [ ] Includes a working "Forgot Password" link navigating to the reset flow.
**Tech Notes / Implementation Guidance:**
- Form should mimic T-01-01 structure. Use shared UI components (buttons, inputs) if a monorepo design system exists.

#### T-02-02 `[FE]` Build HO Forgot Password UI
**Description:**
Build the Forgot Password flow allowing an HO manager to request a password reset email.
**Acceptance Criteria:**
- [ ] Screen 1: Input email address + "Send Reset Link" button.
- [ ] Screen 2: "Check your email" confirmation screen.
- [ ] Screen 3 (Link destination): Enter New Password + Confirm New Password inputs.
**Tech Notes / Implementation Guidance:**
- The new password form will read a reset token from the URL query params (`?token=xyz`).

#### T-02-03 `[BE]` POST /auth/ho/login
**Description:**
Head Office login endpoint.
**Acceptance Criteria:**
- [ ] Validates email + password against the HO Users table.
- [ ] Returns JWT (with HO context ID in payload) and HttpOnly Refresh Token.
**Tech Notes / Implementation Guidance:**
- Ensure the JWT payload contains `ho_id` so the BE knows which tenant environment this user belongs to on subsequent requests.

#### T-02-04 `[BE]` POST /auth/ho/forgot-password & T-02-05 `[BE]` POST /auth/ho/reset-password
**Description:**
Generate reset tokens and update user passwords.
**Acceptance Criteria:**
- [ ] `forgot-password`: Generates secure token, saves to DB with 15-min expiration, successfully triggers transactional email.
- [ ] `reset-password`: Validates token, hashes new password, updates DB, invalidates token immediately.
**Tech Notes / Implementation Guidance:**
- Use cryptographic random bytes for the token.
- Do not confirm if an email exists on the `forgot-password` endpoint (prevents email enumeration — return a generic success message regardless).

#### T-02-06 `[WIRE]` Connect HO Auth Flows end-to-end
**Description:**
Connect HO login and forgot password UI to their respective APIs.
**Acceptance Criteria:**
- [ ] Login success redirects to `/ho/dashboard`.
- [ ] Password reset flow fully functional end-to-end (submit email → simulated email → reset password form → success toast).
**Tech Notes / Implementation Guidance:**
- Verify token injection wrapper is fully functioning for the HO tenant environment.

---

### STORY-03 · Mobile App Login (OTP)

#### T-03-01 `[FE]` Build Mobile Email Input Screen
**Description:**
First screen of the mobile app: passwordless email collection.
**Acceptance Criteria:**
- [ ] Clean UI per Figma. Email keyboard layout is forced (includes `@` key).
- [ ] Validates email format before allowing submission.
**Tech Notes / Implementation Guidance:**
- Use `keyboardType="email-address"` in React Native / Flutter text fields.

#### T-03-02 `[FE]` Build Mobile OTP Entry Screen
**Description:**
Screen allowing the user to enter the 6-digit code sent to their email.
**Acceptance Criteria:**
- [ ] 6 independent boxes for digit input (auto-advancing focus).
- [ ] 60-second countdown timer before "Resend" becomes active.
- [ ] Auto-submits when the 6th digit is typed.
**Tech Notes / Implementation Guidance:**
- Use a dedicated OTP input library (e.g., `@twotalltotems/react-native-otp-input` for RN) to handle auto-focus and clipboard paste.

#### T-03-03 `[BE]` POST /auth/mobile/request-otp
**Description:**
Generate and send 6-digit OTP code.
**Acceptance Criteria:**
- [ ] Verifies the email exists in the Stores database.
- [ ] Generates 6-digit number, saves to DB with 5-minute TTL.
- [ ] Invokes transactional email provider (SendGrid/AWS SES).
**Tech Notes / Implementation Guidance:**
- Rate limit this endpoint heavily to prevent abuse (e.g., 3 requests per 5 minutes per email).

#### T-03-04 `[BE]` POST /auth/mobile/verify-otp
**Description:**
Validate the OTP and issue mobile session tokens.
**Acceptance Criteria:**
- [ ] Validates OTP + email combination.
- [ ] Fails immediately on expired OTP or mismatched code.
- [ ] On success, returns standard JWT + refresh token.
**Tech Notes / Implementation Guidance:**
- Immediately delete or invalidate the OTP in the DB after correct usage to prevent replay attacks.

#### T-03-05 `[WIRE]` Connect Mobile OTP Flow & Routing
**Description:**
Connect the FE components to BE, and control post-login routing logic.
**Acceptance Criteria:**
- [ ] Requesting OTP moves user to next screen; timer engages.
- [ ] Typing wrong code shows a red visual error state + shake animation.
- [ ] On success -> store JWT in Secure Storage.
- [ ] Router evaluation: If user lacks an active SEPA mandate, route to SEPA Setup. If they have one, route to Catalogue.
**Tech Notes / Implementation Guidance:**
- The BE JWT payload or response shape must include a boolean `has_active_sepa`.
- Use React Native `EncryptedStorage` or `SecureStore` (Expo) for tokens.

---

### STORY-04 · Mobile App — First-Time SEPA Setup

#### T-04-01 `[FE]` Build SEPA Mandate Screen
**Description:**
Screen to collect IBAN securely using Stripe Elements/SDK.
**Acceptance Criteria:**
- [ ] Integrate Stripe SDK UI for IBAN collection (so raw IBAN doesn't hit our backend directly).
- [ ] Show SEPA direct debit legal text (Mandatory for compliance).
- [ ] Success/Loading/Failure UI states handled smoothly.
**Tech Notes / Implementation Guidance:**
- Use `@stripe/stripe-react-native` (or official package) specifically looking for `confirmSetupIntent` flow for SEPA Direct Debit.

#### T-04-02 `[BE]` POST /payments/sepa/setup (+ Webhooks)
**Description:**
Backend handling of Stripe SetupIntents.
**Acceptance Criteria:**
- [ ] Endpoint `/payments/sepa/setup` creates a Customer (if null) and returns an ephemeral `client_secret` to frontend.
- [ ] Webhook listener on `setup_intent.succeeded` updates internal database marking `has_active_sepa = true` for the store.
**Tech Notes / Implementation Guidance:**
- Pass the store's email and name to Stripe to prefill the mandate.
- Webhook endpoints must verify the Stripe signature to prevent spoofing.

#### T-04-03 `[WIRE]` Connect Stripe SDK Flow
**Description:**
Tie FE and BE Stripe components together into a blocking UX.
**Acceptance Criteria:**
- [ ] Frontend calls `/setup`, gets secret, launches Stripe SDK UI.
- [ ] Stripe SDK processes IBAN.
- [ ] On success, FE polls (or relies on socket) to ensure backend webhook cleared, then pushes user to the Catalogue.
**Tech Notes / Implementation Guidance:**
- Stripe test mode handles asynchronous responses immediately. Expose clear developer logs when webhooks arrive.

---

## EPIC-02 · Admin Panel — Network Management

### STORY-05 · Head Office List

#### T-05-01 `[FE]` Build HO List Page UI
**Description:**
Admin dashboard view showing all connected Head Offices.
**Acceptance Criteria:**
- [ ] Renders a paginated data table.
- [ ] Global search input field.
- [ ] "Country" select dropdown filter.
- [ ] Empty state ("No Head Offices found") + skeleton loaders for data fetching.
- [ ] Each row must have a "View Details" click access.
**Tech Notes / Implementation Guidance:**
- Use a robust table library like `@tanstack/react-table` for optimal rendering of large datasets.

#### T-05-02 `[BE]` GET /admin/head-offices
**Description:**
API providing the paginated HO list.
**Acceptance Criteria:**
- [ ] Accepts query params: `?page=1&limit=20&search=xyz&country=FR`.
- [ ] Returns properly formatted JSON with `data` array and `meta` (total items, total pages) object.
**Tech Notes / Implementation Guidance:**
- Ensure fuzzy searching is implemented efficiently on the DB (e.g., standard `ILIKE` on name/company fields for PostgreSQL).

#### T-05-03 `[WIRE]` Connect HO List + Implemented Debounce
**Description:**
Wire the frontend table to the API layer securely.
**Acceptance Criteria:**
- [ ] List populates with actual BE data.
- [ ] Typing in search has a 300ms–500ms debounce before firing the API call.
- [ ] Changing page/filter automatically updates the table state and URL query string (for link sharing).
**Tech Notes / Implementation Guidance:**
- Sync filters into URL parameters (e.g. `useSearchParams` in Next.js) so refreshing the page preserves filter states.
