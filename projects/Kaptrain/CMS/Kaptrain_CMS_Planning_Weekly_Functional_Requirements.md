# Kaptrain CMS – Planning (Weekly) – Functional Requirements

## CMS – FR-050 View Weekly Planning (Week View)

**Description**  
Allow Coaches to view an athlete’s planning in a weekly calendar layout.


**Actor**  
Coach


**Priority**  
High


**Acceptance Criteria**
- Coach can open an athlete’s Planning page and see the week layout by default (or via the “Semaine/Week” tab).
- The week header shows the current week range and allows navigation to previous/next week.
- Each day column displays planned sessions for that day (including type/sport and key tags).
- An empty day provides an entry point to add a new session (e.g., “+ Séance / Add a session”).

---

## CMS – FR-051 Select a Target Week via Date Picker

**Description**  
Allow Coaches to jump to a specific week using a calendar date picker.


**Actor**  
Coach


**Priority**  
Medium


**Acceptance Criteria**
- Coach can open the date picker from the week header.
- Selecting a date navigates the planning view to the week that contains the selected date.
- The selected week range updates accordingly.

---

## CMS – FR-052 Publish This Week

**Description**  
Allow Coaches to publish all sessions planned for the currently displayed week.


**Actor**  
Coach


**Priority**  
High


**Acceptance Criteria**
- Coach can trigger publishing for the current week via “Publish this week”.
- If publishing succeeds, sessions in the week are marked as published/available to the athlete.
- If publishing fails, the system shows an error message and no partial publish state is applied (transactional behavior or clear partial-state messaging).

---

## CMS – FR-053 Publish the Current Month from Week View

**Description**  
Allow Coaches to publish the current month directly from the week view publish menu.


**Actor**  
Coach


**Priority**  
Low


**Acceptance Criteria**
- Coach can open the publish dropdown/menu from the week view.
- Coach can choose an action to publish the current month.
- The system confirms completion or shows a failure message.

---

## CMS – FR-054 Enable Multiple Selection Mode in Week View

**Description**  
Allow Coaches to select multiple sessions (and/or days) for bulk actions such as copy/paste or delete.


**Actor**  
Coach


**Priority**  
Medium


**Acceptance Criteria**
- Coach can activate multiple-selection mode from the week view toolbar.
- Selected items are visually highlighted and can be toggled on/off.
- The toolbar reflects the available bulk actions for the current selection.

---

## CMS – FR-055 Copy Selected Sessions

**Description**  
Allow Coaches to copy selected sessions in order to paste them into another week.


**Actor**  
Coach


**Priority**  
Medium


**Acceptance Criteria**
- Coach can copy one or more selected sessions.
- Copy action stores the copied sessions in a temporary clipboard (within the CMS session).
- The UI indicates that content is ready to be pasted (e.g., paste icon becomes available).

---

## CMS – FR-056 Paste Copied Sessions with Confirmation

**Description**  
Allow Coaches to paste previously copied sessions into a target week and confirm the operation.


**Actor**  
Coach


**Priority**  
High


**Acceptance Criteria**
- Coach can trigger paste into a target week.
- The system displays a confirmation modal specifying the destination week range.
- Coach can cancel or confirm the paste operation.
- Upon confirmation, copied sessions are created in the destination week with their structure preserved.
- Modal provides an option “Do not display this message again”; when enabled, subsequent pastes skip confirmation for this coach (until reset).

---

## CMS – FR-057 Open Session Details Panel

**Description**  
Allow Coaches to view detailed information of a session in a side panel from the week view.


**Actor**  
Coach


**Priority**  
High


**Acceptance Criteria**
- Clicking a session opens a right-side details panel.
- The panel displays: session type/sport, session title/description, date, duration, and overall rating (if available).
- The panel displays end-of-session notes and athlete notes when present.
- The panel displays training blocks and their content in a readable format.
- Coach can close the panel without losing context.

---

## CMS – FR-058 Edit Session from Details Panel

**Description**  
Allow Coaches to start editing a session from the session details panel.


**Actor**  
Coach


**Priority**  
High


**Acceptance Criteria**
- Details panel provides an “Edit” action.
- Selecting “Edit” opens the session in edit mode (drawer/panel) with current values pre-filled.
- Coach can save changes and see updates reflected immediately in the week view.

---

## CMS – FR-059 Delete Session with Confirmation

**Description**  
Allow Coaches to delete an existing session from the planning view.


**Actor**  
Coach


**Priority**  
High


**Acceptance Criteria**
- Coach can initiate deletion from the session details panel (trash icon/action).
- The system displays a confirmation modal before deleting.
- Coach can cancel or confirm deletion.
- Upon confirmation, the session is permanently removed from the planning schedule and disappears from the week view.

---

## CMS – FR-060 Duplicate Session

**Description**  
Allow Coaches to duplicate an existing session to speed up planning.


**Actor**  
Coach


**Priority**  
Medium


**Acceptance Criteria**
- Coach can initiate duplication from the session details panel (duplicate/copy icon).
- A new session is created with the same content as the original session (training blocks, linked exercises/videos, metadata).
- The duplicated session is placed in a sensible default date (same day) or prompts the coach to choose a target date/week if required by product rules.
- The new session is visible immediately in the planning view.

