import json
import os

# Base directory for the project context
PROJECT_DIR = r"d:\Github\Gemini Gems\project-manager"
DATA_FILE = os.path.join(PROJECT_DIR, ".agent", "notion_cache.json")

def analyze():
    # Load cached data if it exists, or fall back to the system generated one for now
    # In a real scenario, this would be updated by the API call
    temp_data_path = r"C:\Users\Lenovo\.gemini\antigravity\brain\57141e69-efdf-4d2b-ad6f-42330500d127\.system_generated\steps\18\output.txt"
    
    if not os.path.exists(temp_data_path):
        print("Data source not found. Please sync Notion first.")
        return

    with open(temp_data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    tasks = data.get('results', [])

    categories = {
        "Sign In & Reg": ["login", "sign in", "register", "otp", "email verification", "auth", "authent", "verification", "onboarding", "sign-up", "sign-in"],
        "Coach/Ath Invitation": ["invitation", "invite", "confirm/refuse athlete"],
        "Sports (Master)": ["sports", "exercice", "bibliothèque", "library", "sport list"],
        "Records": ["record", "mes record"],
        "Injuries": ["injuries", "muscle-map", "muscle map", "human body", "muscles"],
        "Subscriptions": ["subscriptions", "abonnements", "free trial", "upgrade plan", "succès (admin)", "subscription page"],
        "Wellness Tracking": ["wellness", "sleep", "bien-être", "activity dashboard"],
        "Chat Feature": ["chat", "messaging", "message page"],
        "Mobile Widgets": ["widget", "volume d’entraînement", "daily steps", "steps", "sorting & customization", "statistics"],
        "Training Programs": ["training", "programs", "session", "cycle", "programmation", "planification", "planner", "library training"],
        "Agenda -> Timer": ["agenda", "timer", "stopwatch", "chronomètre"],
        "Dual Language": ["language", "translation", "fr/en", "français", "french", "english"],
        "Step Count": ["step count", "daily steps", "steps", "pas quotidiens"]
    }

    # Tracking results
    buckets = {cat: {"Done": 0, "Testing": 0, "Total": 0, "Details": []} for cat in categories}
    unmatched = []

    for page in tasks:
        name = page['properties']['Task name']['title'][0]['text']['content'].lower()
        status = page['properties']['Status']['select']['name'] if page['properties']['Status']['select'] else "To Do"
        
        # Determine logical "Section" (Details) - often found in tags
        tags = [t['name'].lower() for t in page['properties']['Tags']['multi_select']]
        
        matched_cat = None
        for cat, keywords in categories.items():
            if any(kw in name for kw in keywords) or any(kw in " ".join(tags) for kw in keywords):
                matched_cat = cat
                break
        
        if matched_cat:
            buckets[matched_cat]["Total"] += 1
            if status == "Done":
                buckets[matched_cat]["Done"] += 1
            else:
                buckets[matched_cat]["Testing"] += 1
            
            # Use the most descriptive detail if available
            if len(buckets[matched_cat]["Details"]) < 1:
                buckets[matched_cat]["ShortDesc"] = name.capitalize()
        else:
            unmatched.append((name, status))

    # Output formatting
    print("\n✅ COMPLETED & VERIFIED")
    for cat, stats in buckets.items():
        if stats["Total"] > 0 and stats["Done"] == stats["Total"]:
            done_pct = 100
            print(f"{cat} | {done_pct}%")
            print(f"Tasks: {stats['Done']} Done / {stats['Testing']} Pending")
            print("-" * 20)

    print("\n🚧 ACTIVE DEVELOPMENTS & TESTING")
    for cat, stats in buckets.items():
        if stats["Total"] > 0 and stats["Done"] < stats["Total"]:
            done_pct = int((stats["Done"] / stats["Total"]) * 100)
            test_pct = 100 - done_pct
            print(f"{cat} | Done: {done_pct}% | Testing: {test_pct}%")
            print(f"Tasks: {stats['Done']} Done / {stats['Testing']} Pending")
            print("-" * 20)

if __name__ == "__main__":
    analyze()
