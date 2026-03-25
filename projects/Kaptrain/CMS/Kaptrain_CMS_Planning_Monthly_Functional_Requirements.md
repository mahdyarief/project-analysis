# Kaptrain CMS – Planning (Monthly) – Functional Requirements

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

