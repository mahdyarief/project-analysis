# Backlog Tasks: FE / BE / WIRED Breakdown

This backlog applies the **Trimmed Triad Model** to ensure clear technical boundaries.

| Epic | Task Name | Layer | Summary | Est. |
|------|-----------|-------|---------|------|
| **WE** | [BE] Wellness Score Formula | **BE** | Implement average score calculation logic based on the 5 variables in Supabase. | 3 |
| **WE** | [FE] Multi-Curve Graph UI | **FE** | Build the Recharts/Chart.js component with support for toggling max 2 curves. | 5 |
| **WE** | [WIRED] Dynamic Wellness Data | **WIRED** | Map the calculated average score and individual metrics from BE to the FE chart. | 2 |
| **EMI** | [BE] Muscle Mapping Schema | **BE** | Ensure DB supports primary/secondary muscle tags per exercise. | 2 |
| **EMI** | [FE] Human Body Interaction | **FE** | Implement SVG human body with hover states and single/double click detection. | 8 |
| **EMI** | [WIRED] Muscle Selection Bridge | **WIRED** | Send selected muscle IDs to the backend and handle loading/feedback states. | 3 |
| **UXP** | [FE] Avatar Cropper Modal | **FE** | Build the modal using `react-easy-crop` or similar for zoom/pan functionality. | 5 |
| **UXP** | [BE] Media Storage Logic | **BE** | Setup Supabase Storage buckets and update user table with the cropped URL. | 2 |
| **UXP** | [WIRED] Avatar Upload Flow | **WIRED** | Handle the blob generation on FE and push to BE storage with optimistic update. | 3 |
| **I18N** | [BE] Translation API Pipeline | **BE** | Integrate DeepL or OpenAI API to handle FR ➔ EN text transformations. | 5 |
| **I18N** | [FE] Manual Override Textbox | **FE** | UI for the translation results where users can manually edit the output. | 3 |
| **I18N** | [WIRED] One-Click Translate | **WIRED** | Connect the "English" button to the BE pipeline and return the draft translation. | 2 |
| **RHM** | [BE] Record Hierarchy DB | **BE** | Create the relational structure for Sport -> Category -> Title -> Unit. | 5 |
| **RHM** | [FE] Multi-Step Record Form | **FE** | Build the dynamic dropdowns for selecting the 4 layers of record data. | 5 |
| **RHM** | [WIRED] Record Entry Wiring | **WIRED** | Validation logic and submitting the complex record object to the database. | 3 |
| **FSM** | [BE] Stripe Proration Logic | **BE** | Webhook handlers for mid-cycle plan changes (license increments). | 8 |
| **FSM** | [FE] Subscription Change Confirmation| **FE** | Verification modal showing price difference and license availability. | 3 |
| **FSM** | [WIRED] Checkout & Plan Sync | **WIRED** | Triggering Stripe checkout sessions and updating user state upon success. | 5 |
