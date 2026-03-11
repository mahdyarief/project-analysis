# 🤖 Project Management Automation Workspace

> **Status:** Production Ready
> **Purpose:** A fully automated AI-driven workspace that transforms raw requirements (PDFs, Figma designs, and Markdown briefs) into comprehensive Jira-ready engineering execution plans.

---

## 🏗️ Directory Structure

This repository is strictly partitioned into three distinct areas:

```
project-manager/
├── .agents/          ← The "Brain" (Workflows, Skills, and Agent Prompts)
├── projects/         ← The "Input" (Drop your raw client requirements here)
└── result/           ← The "Output" (Where the AI dumps the final Jira roadmaps)
```

## 🧠 Current Agent & Skills Architecture

The system is powered by the `pm-planner.agent`, enhanced by a suite of modular **Skills** and an automated playbook (**Workflow**).

### 1. Master Agent
* **`pm-planner.agent`**: Located in `.agents/skills/pm-planner.agent`. This is the core logic engine. It understands Agile methodologies, Fibonacci estimations, sprint velocity limits (~80 SP/Sprint), and risk mapping.

### 2. Available Skills (Autonomously Used)
| Skill | Directory | Description & Capabilities |
|-------|-----------|---------------------------|
| **PDF Mastery** | `.agents/skills/pdf-mastery/` | Automates the ingestion of standard PDF specification documents. Uses a Python script (`extract_pdfs.py`) via CLI to crawl a specific project folder and dump the text contents into JSON for the AI to read. |
| **Figma Integration** | `.agents/skills/figma-integration/` | If the AI detects a `figmaLink.md` file in a project folder, it utilizes the **Figma MCP Server** to autonomously read the live master design file. It extracts user stories, developer handoff comments, and frame configurations *before* writing any tasks to ensure design constraints are respected. |

### 3. Execution Workflow
* **`pm_project_kickoff.md`**: Located in `.agents/workflows/`. This is the strict Standard Operating Procedure (SOP). It forces the AI to execute standard discovery (PDF scripts + Figma MCP), sequentially generate the 9 standard PM deliverables, and compile a final native Jira `.csv` upload file.

---

## 🚀 How to Execute a New Project

To generate a complete technical roadmap for a new client application, follow these steps:

1. **Create the Input Folder:** Make a new folder in `projects/` (e.g., `projects/NEW_APP/`).
2. **Drop Requirements:** 
   - Add any PDF specification documents.
   - Add a `figmaLink.md` file containing the URL to the master Figma file (optional but recommended).
   - Add high-level briefs to `objective.md` or `requirement.md` inside that folder.
3. **Run the AI Command:** 
   Tell your AI Assistant: **`"/pm_project_kickoff targeting NEW_APP"`**
4. **Collect Results:** The AI will autonomously run all skills and output a perfectly formatted backlog inside the `result/NEW_APP/` directory, including a `06_jira_import_ready.csv` file you can drag directly into Jira.

---

*See `result/README.md` for a detailed breakdown of the exact deliverable file structure.*
