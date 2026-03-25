# Kaptrain CMS – Planning (Coach) – Master Functional Requirements

This document consolidates all planning-related functional requirements for the Coach-facing CMS (Planning Notes, Weekly Planning, Monthly Planning, and Create Session).

---

## CMS – FR-045 Weekly Planning View

**Description**  
Allow Coaches to view and manage weekly and monthly planning for a selected athlete.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can access the planning view for a selected athlete.
- Coach can switch between weekly and monthly views.
- The system displays all planned sessions for the selected period.
- Planning data reflects the latest saved state.
- Coach can navigate between dates.

---

## CMS – FR-046 Create Planning Note

**Description**  
Allow Coaches to create a planning note spanning one or multiple dates.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can initiate the creation of a planning note.
- Coach must provide a note title.
- Coach must define a start date and end date.
- The system validates date ranges.
- Given valid input, the planning note is saved successfully.
- Newly created planning notes appear in the planning view.

---

## CMS – FR-047 View Planning Note Details

**Description**  
Allow Coaches to view details of an existing planning note.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can select a planning note from the planning view.
- The system displays the note title and date range.
- Planning note details are read-only by default.

---

## CMS – FR-048 Edit Planning Note

**Description**  
Allow Coaches to modify an existing planning note.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can initiate editing of a planning note.
- Coach can update the note title.
- Coach can update the date range.
- Given valid updates, the system saves changes successfully.
- Updated planning notes are reflected immediately.

---

## CMS – FR-049 Delete Planning Note

**Description**  
Allow Coaches to remove an existing planning note.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can initiate deletion of a planning note.
- The system requires confirmation before deletion.
- Upon confirmation, the planning note is removed from the planning view.

---

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

---

## CMS – FR-062 View Monthly Planning (Month View)

**Description**  
Allow Coaches to view an athlete’s planning in a monthly calendar layout.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can switch from Week view to Month view via the “Mois/Month” tab.
- The month view displays a standard calendar grid for the selected month.
- Each day cell shows planned sessions and a compact indicator when multiple sessions exist (e.g., “+2 sessions”).
- Coach can navigate to previous/next month and the calendar updates accordingly.

---

## CMS – FR-063 Publish the Current Month

**Description**  
Allow Coaches to publish all sessions planned for the currently selected month.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can trigger publishing for the current month via the month view publish menu.
- On success, all eligible sessions in the month are marked as published/available to the athlete.
- On failure, the system shows an error message and clarifies whether any partial publish occurred.

---

## CMS – FR-064 Publish Specific Days in the Month

**Description**  
Allow Coaches to publish sessions for a selected subset of days within a month.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can open a “Publish specific days” modal from the month view publish menu.
- The modal presents days of the selected month with multi-select capability.
- Coach can select one or more days and trigger “Publish the selected days”.
- Only sessions that fall on selected days are published.
- The system confirms completion and surfaces errors if publishing fails.

---

## CMS – FR-065 Open Day Details from Month View

**Description**  
Allow Coaches to drill into a specific day from the month view to review that day’s sessions.

**Actor**  
Coach

**Priority**  
Low

**Acceptance Criteria**

- Coach can click a day cell to view the list of sessions scheduled for that day (either inline expansion or via navigation to the relevant week/day).
- Coach can open a session from that day into the session details panel.
- Returning to the month view preserves the selected month context.

---

## CMS – FR-066 Open Create Session Panel

**Description**  
Allow Coaches to open the “Create a session” panel from planning (week or month) to create a new session for an athlete.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can click “Add a session” from the planning view.
- A side panel opens with a session creation form.
- Coach can close the panel to cancel creation; no session is created unless saved.

---

## CMS – FR-067 Assign Theme(s) and/or Sport(s) to the Session

**Description**  
Allow Coaches to categorize a session by selecting one or more themes and/or sports.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- The panel displays selectable theme chips and sport chips.
- Coach can select/deselect themes and sports.
- Coach can search for and add a sport not listed via “Search for a sport”.
- Selected themes/sports are persisted on save.

---

## CMS – FR-068 Set Session Date

**Description**  
Allow Coaches to define the session date using a date picker.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can set the session date from a date picker control.
- Default date is the day/slot from which the coach initiated creation (when applicable).
- Date is required to save the session.

---

## CMS – FR-069 Set Session Title

**Description**  
Allow Coaches to provide a title for the session.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can enter a session title.
- If left empty, the system either prevents saving or applies a sensible default (per product rules).
- Title is displayed in the planning calendar once saved.

---

## CMS – FR-070 Create and Manage Training Blocks

**Description**  
Allow Coaches to structure a session using one or more training blocks, each containing rich content.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can add a new training block (e.g., “Create a new block”).
- Each block has a title field and a rich-text area for instructions/content.
- Coach can use basic formatting (bold/italic/underline, lists) consistent with the editor controls.
- Coach can delete a block; deletion requires confirmation if the block contains content.
- Coach can reorder blocks (via drag handle or explicit controls) if supported by product rules.

---

## CMS – FR-071 Set Intensity Reference per Block

**Description**  
Allow Coaches to assign an intensity reference to a training block.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Each training block provides an “Intensity reference” selector (dropdown).
- Coach can select an intensity reference value from predefined options.
- Selected value is saved with the block and visible on subsequent edits.

---

## CMS – FR-072 Link Exercise Videos to the Session

**Description**  
Allow Coaches to associate one or more exercise videos with the session.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- Coach can open the “Link exercise videos” modal from the session panel.
- Modal supports searching exercises, filtering (e.g., via “Filter by”), and marking favorites.
- Coach can open an exercise detail view (“More details”) including video preview and target muscles.
- Coach can select one or more exercises and confirm to link them to the session.
- Linked exercises are listed under “Associated exercises” in the session panel.

---

## CMS – FR-073 Save a Training Block as a Template

**Description**  
Allow Coaches to save a training block as a reusable template from within a session.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can trigger “Save training block template” from a block action (e.g., star/save icon).
- A modal requests a template title and shows the block content preview.
- Coach can confirm to save the template.
- Saved template becomes available in “Training block models/templates”.

---

## CMS – FR-074 Insert a Training Block Template into the Session

**Description**  
Allow Coaches to insert one of their saved training block templates into a session.

**Actor**  
Coach

**Priority**  
Medium

**Acceptance Criteria**

- Coach can open the “Training block models/templates” list (e.g., “From my templates”).
- Templates can be searched and previewed.
- Coach can insert a template into the session; the inserted block appears in the session’s blocks list.
- Insertion does not modify the original template.

---

## CMS – FR-075 Save Session (Draft / Publish)

**Description**  
Allow Coaches to save a session, with support for saving without publishing and/or publishing depending on workflow.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- The session panel provides a primary save action (e.g., “Save session”).
- When supported, coach can “Save without publishing” and/or “Publish” the session.
- On save success, the session appears in the planning calendar on the chosen date.
- On save failure, the system shows an error and the coach’s inputs remain intact.

---

## CMS – FR-076 Validate Session Before Saving

**Description**  
Ensure the session creation form enforces required fields and prevents invalid data.

**Actor**  
Coach

**Priority**  
High

**Acceptance Criteria**

- System prevents saving if required fields are missing (at minimum: date; and other required fields per product rules).
- Inline validation messages are shown near the relevant fields.
- System prevents saving if training blocks contain invalid content (e.g., empty required titles if mandated).
