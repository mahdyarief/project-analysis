# 📁 Result Folder — Standard Structure

This folder contains Project Manager outputs, grouped **by project name**.

---

## 📂 Folder Layout

```
result/
└── {PROJECT_NAME}/
    ├── 00_project_overview.md          ← Project summary, scope, tech stack assumptions
    ├── 00_figma_analysis.md            ← [If Figma exists] Extracted design constraints and UX rules
    ├── 01_epic_list.md                 ← All Epics with description and business value
    ├── 02_backlog_tasks.md             ← Full task list (FE / BE / Wiring) with Story Points
    ├── 03_sprint_plan.md               ← Sprint 1 & Sprint 2 breakdown with rationale
    ├── 04_dependencies_and_risks.md    ← Dependency map, blockers, risks
    ├── 05_workflow_definition.md       ← Kanban workflow, Definition of Done, QA criteria
    ├── 06_jira_import_ready.csv        ← Native Jira bulk-upload CSV file (Epic, Summary, Priority, SP)
    └── tasks/
        ├── 07_sprint_1_detailed_tasks.md ← Deep dive implementation guide + Acceptance criteria
        └── 08_sprint_2_detailed_tasks.md ← Deep dive implementation guide + Acceptance criteria
```

---

## 📋 Standard File Descriptions

| File | Purpose |
|------|---------|
| `00_project_overview.md` | High-level understanding: what the product is, who uses it, key assumptions, open questions |
| `00_figma_analysis.md` | Figma specific findings, UI/UX constraints, design rules, and a **deep page-by-page feature breakdown** extracted directly from the master UI files |
| `01_epic_list.md` | Epics only — grouped by domain. Each epic has a short description and scope |
| `02_backlog_tasks.md` | All user stories/tasks split into **Frontend**, **Backend**, **Wiring/Integration** layers with SP estimates |
| `03_sprint_plan.md` | Sprint 1 (Foundation) and Sprint 2 (Value Delivery) with velocity targets and goals |
| `04_dependencies_and_risks.md` | Explicit dependencies between tasks, risk register, potential blockers per sprint |
| `05_workflow_definition.md` | How tasks flow through Kanban, what "Ready for QA" means, Definition of Done |
| `06_jira_import_ready.csv` | Raw CSV file format engineered specifically for Jira bulk-issue import |
| `tasks/..._detailed_tasks.md` | Deeply granular execution specs per task containing descriptions, testing AC, and Tech Notes (Item 2) |

---

## 🏷️ Task Layer Convention

Every task is tagged with one of three **layers**:

| Tag | Layer | Description |
|-----|-------|-------------|
| `[FE]` | Frontend | UI screens, components, UX states, forms, navigation |
| `[BE]` | Backend | API endpoints, business logic, DB models, integrations |
| `[WIRE]` | Wiring | Connecting FE ↔ BE: API contracts, auth tokens, data binding |

---

## 📐 Story Point Scale (Fibonacci)

| Points | Complexity |
|--------|-----------|
| 1 | Trivial — static page, label change |
| 2 | Simple — single form, basic CRUD display |
| 3 | Small — form with validation + API call |
| 5 | Medium — feature with multiple states, moderate API work |
| 8 | Large — complex integration, multi-step flow |
| 13 | X-Large — third-party integration + complex logic |

---

## 🗂️ Projects Index

| Project | Status | Apps |
|---------|--------|------|
| [NFA](./NFA/) | ✅ Analyzed | Admin Panel, Head Office, Mobile App |
