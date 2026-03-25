import json
import re

# Paths
stats_file = r'd:\Github\Gemini Gems\project-manager\stats_output.json'
report_path = r'C:\Users\Lenovo\.gemini\antigravity\brain\d6e32ee7-d0e4-4f49-9c04-7543ff2db268\nfa_project_summary.md'

with open(stats_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

epics = data['epics']
layers = data['layers']
total = data['total_stats']

# 1. Update Layer Table
# New header: | Layer | Total Tasks | In Progress % | Ready % | Tasks In-Progress |
layer_header = "| Layer | Total Tasks | In Progress % | Ready To Test % | Tasks In-Progress |"
layer_sep = "| :--- | :---: | :---: | :---: | :---: |"
layer_rows = []
for name in ['FE', 'BE', 'WIRED']:
    l = layers[name]
    ip_pct = round(l['inprogress'] / l['total'] * 100, 2) if l['total'] > 0 else 0
    rt_pct = round(l['ready_to_test'] / l['total'] * 100, 2) if l['total'] > 0 else 0
    layer_rows.append(f"| **{name}** | {l['total']} | **{ip_pct}%** | **{rt_pct}%** | {l['inprogress']} |")

layer_table = layer_header + "\n" + layer_sep + "\n" + "\n".join(layer_rows)

# 2. Update Feature Table
# New header: | Epic | Total Tasks | In Progress | Ready To Test | New | Story Points |
feature_header = "| Epic | Total Tasks | In Progress | Ready To Test | New | Story Points |"
feature_sep = "| :--- | :---: | :---: | :---: | :---: | :---: |"
epic_rows = []
for name in sorted(epics.keys()):
    e = epics[name]
    new_tasks = e['total'] - e['inprogress'] - e['ready_to_test'] - e['done']
    epic_rows.append(f"| **{name}** | {e['total']} | {e['inprogress']} | {e['ready_to_test']} | {new_tasks} | {e['sp_total']} |")

epic_rows.append(f"| **TOTAL** | **{total['tasks']}** | **{total['inprogress']}** | **{total['ready_to_test']}** | **{total['tasks'] - total['inprogress'] - total['ready_to_test']}** | **{total['sp']}** |")
feature_table = feature_header + "\n" + feature_sep + "\n" + "\n".join(epic_rows)

# Read the existing report
with open(report_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Layer Table
content = re.sub(r"\| Layer \|.*?\n\| :--- \|.*?\n(?:\|.*?\n)+", layer_table + "\n", content)

# Replace Feature Table
content = re.sub(r"\| Epic \|.*?\n\| :--- \|.*?\n(?:\|.*?\n)+", feature_table + "\n", content)

# Update Status and Key Achievements
if total['ready_to_test'] > 0:
    content = re.sub(r'Current Status: `.*?`', 'Current Status: `🧪 TESTING ENABLED`', content)
    achievement_update = f"*   **Key Achievement**: {total['ready_to_test']} tasks are now **Ready To Test**, starting the first verification cycle."
    content = re.sub(r'\*   \*\*Key Achievement\*\*: .*', achievement_update, content)

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Report updated successfully.")
