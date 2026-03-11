# Sprint 1: "The Walking Skeleton" - Detailed Features

## Feature 1: Setup Postgres Database Schema (Admin, HO, Store Users)
**Description:** Establish the primary relational structure mapping a Super Admin to Head Offices, and Head Offices to individual Stores. 
**Acceptance Criteria:**
- [x] ORM configured.
- [x] Migrations generated successfully for Enum Roles.
- [x] Database strictly enforces referential integrity on deletes.
**Tech Notes:** Consider Prisma or TypeORM for explicit typing schemas matching TS.

## Feature 2: Setup JWT Auth Service & Role Guards
**Description:** API endpoints and middleware specifically verifying JWT payloads against Admin, HO, or Store Enum constraints.
**Acceptance Criteria:**
- [x] Unauthorized access returns rigid 401/403 payloads.
- [x] JWT expires and has a refresh mechanism.
- [x] Middleware correctly decodes `role` property in token payload.
**Tech Notes:** Fastify JWT or passport.js. 

## Feature 3: SendGrid OTP Login System (Mobile User Target)
**Description:** Instead of passwords, Mobile users input their email. The API generates a random 6 digit numeric code, sends it via SendGrid to the requested email, and caches it in Redis awaiting the verification hook.
**Acceptance Criteria:**
- [x] Valid 6-digit Code generated and cached (Redis/DB) with 5-min TTL.
- [x] SendGrid API returns 2xx success block.
- [x] Verifying correct code issues long-lived Session Token.
**Tech Notes:** Implement tight rate-limiting (`express-rate-limit`) on the verification route to prevent OTP brute-forcing. 

## Feature 4: Admin Web Login Portal
**Description:** Develop the React.js view for Admin login containing valid email/password fields, visual show/hide mechanics on the password via an eye icon, and distinct field-level error messages.
**Acceptance Criteria:**
- [x] "Login" button remains `disabled` computationally unless both fields pass basic regex validation.
- [x] Visual validation error toast notification if 401 returns from API.
- [x] Successful login immediately rewrites user to `/dashboard` route.
**Tech Notes:** React Hook Form combined with Zod schema validation maps perfectly to these requirements.

---
**(Subset generated for brevity, following the exact deep-dive methodology for all 67 SP of Sprint 1 tasks...)**
