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

counts = {}
for page in all_results:
    status_prop = page['properties'].get('Status', {})
    if 'select' in status_prop and status_prop['select']:
        name = status_prop['select']['name']
    else:
        name = "No Status"
    counts[name] = counts.get(name, 0) + 1

total = len(all_results)
print(f"Total tasks: {total}")
print(json.dumps(counts, indent=2))

# Feature mapping
feature_mapping = {
    "Sign In & Registration": ["sign in", "registration", "login", "onboarding auth"],
    "Coach/Athlete Invitation": ["invite", "invitation"],
    "Sports (Master/Selection)": ["sports"],
    "Records": ["record"],
    "Injuries": ["injuries", "muscle", "human body"],
    "Subscriptions": ["subscription", "abonnements", "free trial", "upgrade plan"],
    "Wellness Tracking": ["wellness", "daily check-in", "weight tracking"],
    "Chat Feature": ["chat", "messaging", "messenger"],
    "Mobile Widgets": ["widget", "stats"],
    "Training Programs": ["training", "program", "session", "cycle"],
    "Agenda -> Timer": ["agenda", "stopwatch", "timer"],
    "Dual Language": ["french", "english", "language", "translation"],
    "Step Count": ["step"]
}

feat_results = {feature: {"Done": 0, "Not Done": 0} for feature in feature_mapping}

for page in all_results:
    title = ""
    title_list = page['properties'].get('Task name', {}).get('title', [])
    if title_list:
        title = title_list[0].get('plain_text', "").lower()
    
    status_prop = page['properties'].get('Status', {})
    if 'select' in status_prop and status_prop['select']:
        status_name = status_prop['select']['name']
    else:
        status_name = "To Do"
    
    is_done = (status_name == "Done")
    
    for feature, keywords in feature_mapping.items():
        if any(kw in title for kw in keywords):
            if is_done:
                feat_results[feature]["Done"] += 1
            else:
                feat_results[feature]["Not Done"] += 1

print("\nFeature Breakdown:")
print(json.dumps(feat_results, indent=2))
