# Workflow Definition & QA Standards

## 🔄 Kanban Column Transitions

The Jira board must strictly adhere to the following 5 columns. Do not add custom columns like "Code Review" or "Blocked" (use Jira Labels/Flags for blockers).

1. **Backlog (To Refine)**: Un-estimated tasks or Epics slated for Sprint 3+.
2. **To Do (Ready for Dev)**: Fully estimated, scoped, and groomed tasks for the active Sprint. A developer picks from the top of this list.
3. **In Progress**: Developer is actively coding branch `feat/NFA-[ID]`.
4. **QA (Ready to Test)**: Code is merged to the `staging` environment. The feature is actively accessible by a non-technical tester.
5. **Done**: Approved by QA and Product. Feature works in production.

---

## ✅ Definition of Done (DoD)

A task only moves to **Done** if ALL of the following apply:
*   The code accomplishes all checked Acceptances Criteria outlined in the Jira task.
*   The PR has been approved by at least 1 other engineer.
*   The feature branch has been deployed to the Staging server.
*   The UX strictly complies with the constraints outlined in `00_figma_analysis.md` (e.g. Account icon stays top right).
*   The feature passes basic manual "Happy Path" testing by QA without throwing 500 API errors.

---

## 🐛 Defect / Bug Management

If a task is in QA and fails testing:
1. Do **not** drag the ticket back to "In Progress".
2. Create a Sub-Bug ticket linking back to the parent task.
3. The parent task remains in "QA" until the Sub-Bug is resolved and closed by the original engineer.
