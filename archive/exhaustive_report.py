import json

files = [
    "C:/Users/Lenovo/.gemini/antigravity/brain/5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce/.system_generated/steps/66/output.txt",
    "C:/Users/Lenovo/.gemini/antigravity/brain/5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce/.system_generated/steps/223/output.txt"
]

all_results = []
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        all_results.extend(data.get('results', []))

feature_mapping = {
    "Sign In & Registration": ["sign in", "registration", "login", "onboarding auth", "otp", "email verification", "password", "reset profile"],
    "Coach/Athlete Invitation": ["invite", "invitation"],
    "Sports (Master/Selection)": ["sports"],
    "Records": ["record"],
    "Injuries": ["injuries", "muscle", "human body"],
    "Subscriptions": ["subscription", "abonnements", "free trial", "upgrade plan"],
    "Wellness Tracking": ["wellness", "daily check-in", "weight tracking", "sleep", "nutrition"],
    "Chat Feature": ["chat", "messaging", "messenger"],
    "Mobile Widgets": ["widget", "stats"],
    "Training Programs": ["training", "program", "session", "cycle", "planification", "exercices", "bibliothèque"],
    "Agenda -> Timer": ["agenda", "stopwatch", "timer"],
    "Dual Language": ["french", "english", "language", "translation"],
    "Step Count": ["step"]
}

# Advanced categorization and "Other" handling
groups = {f: {"Done": 0, "Testing": 0, "Other Pending": 0} for f in feature_mapping}
groups["UI, CMS & System Core"] = {"Done": 0, "Testing": 0, "Other Pending": 0}

for page in all_results:
    title_list = page['properties'].get('Task name', {}).get('title', [])
    title = title_list[0].get('plain_text', "").lower() if title_list else "untitled"
    
    status_prop = page['properties'].get('Status', {})
    status_name = status_prop['select']['name'] if (status_prop.get('select')) else "To Do"
    
    # State flags
    is_done = (status_name == "Done")
    is_testing = (status_name == "In Testing (Staging)")
    is_other_pending = (status_name in ["In Progress", "To Do", "Bug", "Review Needed"])

    matched = False
    for feature, keywords in feature_mapping.items():
        if any(kw in title for kw in keywords):
            if is_done: groups[feature]["Done"] += 1
            elif is_testing: groups[feature]["Testing"] += 1
            elif is_other_pending: groups[feature]["Other Pending"] += 1
            matched = True
            break
    
    if not matched:
        if is_done: groups["UI, CMS & System Core"]["Done"] += 1
        elif is_testing: groups["UI, CMS & System Core"]["Testing"] += 1
        elif is_other_pending: groups["UI, CMS & System Core"]["Other Pending"] += 1

print(json.dumps(groups, indent=2))

# Verifying totals
total_testing = sum(v["Testing"] for v in groups.values())
total_pending = sum(v["Testing"] + v["Other Pending"] for v in groups.values())
print(f"\nVerification: Total Testing = {total_testing}")
print(f"Verification: Total Pending (Not Done) = {total_pending}")
