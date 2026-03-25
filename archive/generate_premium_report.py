import os
import json
import requests
from datetime import datetime
from collections import defaultdict

# Configuration
DATABASE_ID = "325aadf8-73ee-8138-96d8-000b189181fe" # Tasks Status 16-3-2026

# Note: This script is intended to be run within an environment where 
# the 'mcp_notion_API-query-data-source' tool is available or by 
# the agent using that tool to provide data.

def generate_report(tasks):
    print(f"--- Processing {len(tasks)} tasks from Notion ---")

def extract_property(properties, name):
    prop = properties.get(name, {})
    type = prop.get("type")
    
    if type == "title":
        titles = prop.get("title", [])
        return "".join([t.get("plain_text", "") for t in titles])
    elif type == "select":
        select = prop.get("select")
        return select.get("name") if select else None
    elif type == "multi_select":
        return [ms.get("name") for ms in prop.get("multi_select", [])]
    elif type == "status":
        status = prop.get("status")
        return status.get("name") if status else None
    return None

def generate_report_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    tasks = data.get('results', []) if isinstance(data, dict) else data
    return generate_report(tasks)
def generate_report(tasks):
    # Mapping keywords to categories based on user requested list
    categories = {
        "Account Sign In & Registration": ["login", "sign in", "register", "otp", "email", "auth", "authent", "onboarding", "sign-up", "sign-in"],
        "Coach & Athlete Connection & Invitation": ["invitation", "invite", "confirm", "athlete", "coach"],
        "Sports (Master & Selection)": ["sports", "exercice", "bibliothèque", "library", "sport list"],
        "Records (Master, Selection & Input)": ["record", "mes record", "profile"],
        "Injuries": ["injuries", "muscle-map", "muscle map", "human body", "muscles"],
        "Subscriptions (Master & Payments)": ["subscriptions", "abonnements", "free trial", "upgrade plan", "succès (admin)", "subscription page"],
        "Athlete Wellness Tracking": ["wellness", "sleep", "bien-être", "activity dashboard"],
        "Chat feature": ["chat", "messaging", "message page"],
        "All mobile widgets": ["widget", "volume d’entraînement", "statistics"],
        "Training Programs": ["training", "programs", "session", "cycle", "programmation", "planification", "planner", "library training"],
        "Agenda -> Timer": ["agenda", "timer", "stopwatch", "chronomètre"],
        "Dual language": ["language", "translation", "fr/en", "français", "french", "english"],
        "Step count": ["step count", "steps", "pas quotidiens"],
    }

    # Grouping by Tags (Feature Mapping)
    # If no tags, we use "Uncategorized"
    features = defaultdict(lambda: {"total": 0, "done": 0, "testing": 0, "pending": 0, "latest_done": []})

    for task in tasks:
        props = task.get("properties", {})
        title = extract_property(props, "Task name").lower()
        status = extract_property(props, "Status")
        tags = [t.lower() for t in extract_property(props, "Tags")] if extract_property(props, "Tags") else []
        
        # Determine categories for this task
        matched_categories = []
        for cat, keywords in categories.items():
            if any(kw in title for kw in keywords) or any(kw in " ".join(tags) for kw in keywords):
                matched_categories.append(cat)
        
        if not matched_categories:
            matched_categories = ["Uncategorized"]

        for cat_name in matched_categories:
            features[cat_name]["total"] += 1
            if status == "Done":
                features[cat_name]["done"] += 1
                if len(features[cat_name]["latest_done"]) < 3:
                    features[cat_name]["latest_done"].append(title)
            elif status == "In Testing (Staging)":
                features[cat_name]["testing"] += 1
            else:
                features[cat_name]["pending"] += 1

    # Format the report
    report_lines = []
    report_lines.append(f"# Project Progress Report - {datetime.now().strftime('%d %B %Y')}\n")

    # Finalized Features (100% Done)
    finalized = {k: v for k, v in features.items() if v["done"] == v["total"] and v["total"] > 0}
    if finalized:
        report_lines.append("## ✅ COMPLETED & VERIFIED")
        for name, stats in finalized.items():
            report_lines.append(f"### {name} | 100%")
            report_lines.append(f"**Details**: {', '.join(stats['latest_done'][:2]) if stats['latest_done'] else 'All tasks verified.'}")
            report_lines.append(f"**Tasks**: {stats['done']} Done / {stats['pending']} Pending\n")

    # In Progress Features
    ongoing = {k: v for k, v in features.items() if v["done"] < v["total"]}
    if ongoing:
        report_lines.append("## 🚧 CORE FEATURES (IN STAGING)")
        for name, stats in ongoing.items():
            done_pct = round((stats["done"] / stats["total"]) * 100)
            test_pct = round((stats["testing"] / stats["total"]) * 100)
            
            line = f"### {name} | Done: {done_pct}%"
            if test_pct > 0:
                line += f" | Testing: {test_pct}%"
            report_lines.append(line)
            
            report_lines.append(f"**Details**: Tasks include {', '.join(stats['latest_done'][:2]) if stats['latest_done'] else 'various ongoing updates.'}")
            report_lines.append(f"**Tasks**: {stats['done']} Done / {stats['pending']} Pending\n")

    output_content = "\n".join(report_lines)
    
    with open("premium_progress_report.md", "w", encoding="utf-8") as f:
        f.write(output_content)
    
    print("Report generated: premium_progress_report.md")
    return output_content

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        generate_report_from_file(sys.argv[1])
    else:
        print("Usage: python generate_premium_report.py <json_data_file>")
