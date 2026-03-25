import json
import os
import sys

# Ensure UTF-8 output
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def analyze():
    task_files = [
        r'C:\Users\Lenovo\.gemini\antigravity\brain\5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce\.system_generated\steps\769\output.txt',
        r'C:\Users\Lenovo\.gemini\antigravity\brain\5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce\.system_generated\steps\810\output.txt',
        r'C:\Users\Lenovo\.gemini\antigravity\brain\5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce\.system_generated\steps\826\output.txt'
    ]
    feedback_file = r'C:\Users\Lenovo\.gemini\antigravity\brain\5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce\.system_generated\steps\774\output.txt'

    all_tasks = []
    for f in task_files:
        if not os.path.exists(f): continue
        with open(f, 'r', encoding='utf-8') as file:
            data = json.load(file)
            all_tasks.extend(data.get('results', []))

    all_feedback = []
    if os.path.exists(feedback_file):
        with open(feedback_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            all_feedback.extend(data.get('results', []))

    # Overall Summary
    total_tasks = len(all_tasks)
    status_summary = {} # status_name -> count
    cms_responsive_tasks = []

    for task in all_tasks:
        props = task.get('properties', {})
        status_obj = props.get('Status', {}).get('select', {}) or {}
        status = status_obj.get('name', 'To Do')
        status_summary[status] = status_summary.get(status, 0) + 1
        
        tags_obj = props.get('Tags', {}).get('multi_select', []) or []
        tags = [t['name'] for t in tags_obj]
        if 'CMS - Responsive' in tags:
            cms_responsive_tasks.append(task)

    # Feedback Analysis (Filtered)
    hp_active_feedback = []
    hp_done = 0
    hp_inprogress = 0
    hp_needconfirm = 0
    hp_bugs = 0
    hp_feature_adj = 0

    for fb in all_feedback:
        props = fb.get('properties', {})
        priority = (props.get('Priority', {}).get('select', {}) or {}).get('name', 'None')
        status = (props.get('Status', {}).get('select', {}) or {}).get('name', 'New')
        fb_type = (props.get('Feedback Type', {}).get('select', {}) or {}).get('name', 'Other')

        if priority == 'High' and status != 'New':
            hp_active_feedback.append(fb)
            if status == 'Done': hp_done += 1
            if status == 'In progress': hp_inprogress += 1
            if status == 'Need confirm': hp_needconfirm += 1
            
            if fb_type == 'Bug': hp_bugs += 1
            else: hp_feature_adj += 1

    total_hp_active = len(hp_active_feedback)
    hp_progress = (hp_done / total_hp_active * 100) if total_hp_active > 0 else 0

    # Output Report
    print("# Kaptrain Detailed Progress Status (18-03-2026)")
    
    # CMS Responsive (Brief)
    cms_count = len(cms_responsive_tasks)
    cms_done = sum(1 for t in cms_responsive_tasks if (t['properties'].get('Status', {}).get('select', {}) or {}).get('name') == 'Done')
    print(f"\n## 📱 CMS Responsive Progress")
    print(f"Total Tasks: {cms_count} | Done: {cms_done} | Active: {cms_count - cms_done}")
    print(f"Progress: {(cms_done/cms_count*100 if cms_count > 0 else 0):.1f}%")

    # High Priority Feedback (Detailed)
    print(f"\n## 🚩 High Priority Feedback (Excl. New Status)")
    print(f"Total Active High Priority: {total_hp_active}")
    print(f"- **Done**: {hp_done}")
    print(f"- **In Progress**: {hp_inprogress}")
    print(f"- **Need Confirm**: {hp_needconfirm}")
    print(f"- **Feedback Type (Bug)**: {hp_bugs}")
    print(f"- **Feedback Type (Feature Adjustment)**: {hp_feature_adj}")
    print(f"\n**High Priority Progress: {hp_progress:.1f}%**")

    if hp_active_feedback:
        print("\n### High Priority Items Breakdown:")
        for fb in hp_active_feedback:
            props = fb.get('properties', {})
            nom_obj = props.get('Nom', {}).get('title', []) or []
            name = nom_obj[0].get('plain_text', 'No Name') if nom_obj else 'No Name'
            stat = (props.get('Status', {}).get('select', {}) or {}).get('name', 'New')
            ftype = (props.get('Feedback Type', {}).get('select', {}) or {}).get('name', 'Other')
            print(f"- {name} [**{stat}**] Type: {ftype}")

if __name__ == "__main__":
    analyze()
