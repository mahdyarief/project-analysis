
# 🛠️ Generalized Project Analyzer

This directory contains a generalized system for analyzing project progress from Notion data.

## 📂 Structure

- `run_analyzer.py`: The main entry point script.
- `core/`: Core logic engines.
  - `notion.py`: Handles property extraction from Notion JSON.
  - `processor.py`: Handles data normalization and feature mapping.
  - `generators.py`: Handles Markdown, CSV, and Text report generation.
- `config/`: Project-specific configurations.
  - `definitions.py`: Registry of project keywords, status maps, and title properties.

## 🚀 Usage

You can run the analyzer for any project defined in `config/definitions.py`.

```bash
python script/run_analyzer.py <ProjectName> --input <path_to_notion_json>
```

### Examples:

**For Kaptrain:**
```bash
python script/run_analyzer.py Kaptrain --input data.json --format all
```

**For NFA (includes Layer Grid):**
```bash
python script/run_analyzer.py NFA --input data.json --format md
```

### Options:
- `--input`: Path to the JSON file containing Notion results (required).
- `--format`: `md`, `csv`, or `all` (default: `md`).
- `--output_dir`: Where to save the reports (default: `result`).

## ⚙️ Adding a New Project

To support a new project, edit `script/config/definitions.py` and add a new entry to the `PROJECTS` dictionary:

```python
"MY_PROJECT": {
    "status_map": DEFAULT_STATUS_MAP,
    "title_prop": "Name", # Property name for the task title
    "features": {
        "Module A": ["keyword1", "keyword2"],
        ...
    }
}
```
