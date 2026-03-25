import json
import csv

files = [
    "C:/Users/Lenovo/.gemini/antigravity/brain/5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce/.system_generated/steps/66/output.txt",
    "C:/Users/Lenovo/.gemini/antigravity/brain/5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce/.system_generated/steps/223/output.txt"
]

all_tasks = []
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        all_tasks.extend(data.get('results', []))

feature_mapping = {
    "Sign In & Registration": ["sign in", "registration", "login", "auth", "otp", "password", "onboarding", "verification"],
    "Coach/Athlete Invitation": ["invite", "invitation"],
    "Sports (Master/Selection)": ["sports"],
    "Records": ["record"],
    "Injuries & Muscle Map": ["injuries", "muscle", "human body"],
    "Subscriptions & Payments": ["subscription", "abonnements", "free trial", "upgrade", "payment"],
    "Wellness Tracking": ["wellness", "daily check-in", "weight tracking", "sleep", "nutrition"],
    "Chat Feature": ["chat", "messaging", "messenger"],
    "Mobile Widgets": ["widget", "stats"],
    "Training Programs": ["training", "program", "session", "cycle", "planification", "exercices"],
    "Agenda & Timer": ["agenda", "stopwatch", "timer"],
    "Dual Language": ["language", "translation", "french", "english"],
    "Step Count": ["step"]
}

# Structure to hold counts and representative task names
# { "Feature": {"Done": 0, "Testing": 0, "InProgress": 0, "Tasks": []} }
results = {f: {"Done": 0, "Testing": 0, "InProgress": 0, "Tasks": []} for f in feature_mapping}
results["UI & System Core"] = {"Done": 0, "Testing": 0, "InProgress": 0, "Tasks": []}

for task in all_tasks:
    # Extract Title
    title_list = task['properties'].get('Task name', {}).get('title', [])
    raw_title = title_list[0].get('plain_text', "") if title_list else "Untitled"
    clean_title = raw_title.lower()
    
    # Extract Status
    status_prop = task['properties'].get('Status', {})
    status_name = status_prop['select']['name'] if status_prop.get('select') else "To Do"
    
    # Match Feature
    matched = False
    for feature, keywords in feature_mapping.items():
        if any(kw in clean_title for kw in keywords):
            # Update Counts
            if status_name == "Done": results[feature]["Done"] += 1
            elif status_name == "In Testing (Staging)": results[feature]["Testing"] += 1
            elif status_name == "In Progress": results[feature]["InProgress"] += 1
            
            # Store first few titles for description
            if len(results[feature]["Tasks"]) < 3:
                results[feature]["Tasks"].append(raw_title)
            matched = True
            break
            
    if not matched:
        if status_name == "Done": results["UI & System Core"]["Done"] += 1
        elif status_name == "In Testing (Staging)": results["UI & System Core"]["Testing"] += 1
        elif status_name == "In Progress": results["UI & System Core"]["InProgress"] += 1
        if len(results["UI & System Core"]["Tasks"]) < 3:
            results["UI & System Core"]["Tasks"].append(raw_title)

# Generate CSV
output_path = "d:/Github/Gemini Gems/project-manager/kaptrain_feature_report.csv"
with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Feature Module", "Done", "Testing", "In Progress", "Short Description"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for feat, data in results.items():
        # Create Description
        desc_preview = ", ".join(data["Tasks"])
        if len(desc_preview) > 80: desc_preview = desc_preview[:77] + "..."
        if not desc_preview: desc_preview = "General module tasks"
        
        writer.writerow({
            "Feature Module": feat,
            "Done": data["Done"],
            "Testing": data["Testing"],
            "In Progress": data["InProgress"],
            "Short Description": desc_preview
        })

print(f"CSV report generated at {output_path}")
