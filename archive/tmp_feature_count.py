import json

with open("C:/Users/Lenovo/.gemini/antigravity/brain/5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce/.system_generated/steps/66/output.txt", "r", encoding="utf-8") as f:
    data = json.load(f)

# Keywords to map tasks to requested features
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

results = {feature: {"Done": 0, "Not Done": 0} for feature in feature_mapping}

for page in data['results']:
    title = ""
    title_list = page['properties'].get('Task name', {}).get('title', [])
    if title_list:
        title = title_list[0].get('plain_text', "").lower()
    
    status_obj = page['properties'].get('Status', {}).get('select', {})
    status_name = status_obj.get('name', 'Unknown') if status_obj else 'Empty'
    is_done = (status_name == "Done")
    
    # Simple keyword matching
    for feature, keywords in feature_mapping.items():
        if any(kw in title for kw in keywords):
            if is_done:
                results[feature]["Done"] += 1
            else:
                results[feature]["Not Done"] += 1

print(json.dumps(results, indent=2))
