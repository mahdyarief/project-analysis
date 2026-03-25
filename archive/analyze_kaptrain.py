import json
import os
import sys
from collections import defaultdict

# Set encoding to utf-8 for Windows console
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def analyze_kaptrain_interactive_report():
    filepaths = [
        r'C:\Users\Lenovo\.gemini\antigravity\brain\5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce\.system_generated\steps\533\output.txt',
        r'C:\Users\Lenovo\.gemini\antigravity\brain\5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce\.system_generated\steps\567\output.txt'
    ]
    
    REPORT_FEATURES = {
        "Sign In & Reg": ["login", "register", "signin", "otp", "auth", "inscription", "connexion"],
        "Coach/Ath Invitation": ["invite", "invitation"],
        "Sports (Master)": ["sport", "favoris"],
        "Records": ["record", "index mes"],
        "Injuries": ["injury", "injuries", "muscle-map", "blessure"],
        "Subscriptions": ["subscription", "billing", "abonnement", "free trial", "stripe", "paiement", "pay", "billing"],
        "Wellness Tracking": ["wellness", "check-in", "tracking", "suivi", "weight", "sleep"],
        "Chat Feature": ["chat", "message", "messenger"],
        "Mobile Widgets": ["widget"],
        "Training Programs": ["program", "training", "exercise", "workout", "session", "bibliothèque", "training block", "entrainement", "séance"],
        "Agenda -> Timer": ["timer", "stopwatch", "agenda"],
        "Dual Language": ["translation", "dual language", "english", "french", "fr/en", "translate"],
        "Step Count": ["step count", "widget steps", "daily steps", "steps"]
    }

    def map_feature(title):
        title_lower = title.lower()
        if any(kw in title_lower for kw in ["step count", "widget steps", "daily steps", "steps"]):
            return "Step Count"
        for feature, keywords in REPORT_FEATURES.items():
            if any(kw in title_lower for kw in keywords):
                return feature
        return "System Core & UI"

    all_results = []
    for filepath in filepaths:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                all_results.extend(data.get('results', []))
    
    # Detailed stats collection
    status_counts = {"Done": 0, "Testing": 0, "Pending": 0}
    feature_stats = defaultdict(lambda: {"Done": 0, "Testing": 0, "Pending": 0, "Details": []})
    
    for page in all_results:
        props = page.get('properties', {})
        title = props.get('Task name', {}).get('title', [{}])[0].get('plain_text', 'No Title')
        status_name = props.get('Status', {}).get('select', {}).get('name', 'To Do')
        
        feature = map_feature(title)
        
        if status_name == 'Done':
            norm = "Done"
        elif "Testing" in status_name:
            norm = "Testing"
        else:
            norm = "Pending"
            
        status_counts[norm] += 1
        feature_stats[feature][norm] += 1
        if len(feature_stats[feature]["Details"]) < 2:
            feature_stats[feature]["Details"].append(title)

    total_tasks = sum(status_counts.values())
    pct_done = (status_counts["Done"] / total_tasks * 100) if total_tasks > 0 else 0
    pct_testing = (status_counts["Testing"] / total_tasks * 100) if total_tasks > 0 else 0
    pct_pending = (status_counts["Pending"] / total_tasks * 100) if total_tasks > 0 else 0

    # Output Interactive Report
    print("🚀 KAPTRAIN PROJECT PULSE")
    print(f"Date: 16 March 2026 | Total Scope: {total_tasks} Tasks")
    
    print(f"\n📈 OVERALL PERFORMANCE")
    print(f"- ✅ **Done**: {pct_done:.1f}% ({status_counts['Done']} tasks)")
    print(f"- 🧪 **Testing**: {pct_testing:.1f}% ({status_counts['Testing']} tasks)")
    print(f"- ⏳ **Pending**: {pct_pending:.1f}% ({status_counts['Pending']} tasks)")

    print(f"\n🎯 FEATURE BREAKDOWN")
    
    def get_bar(d, t, p):
        total = d + t + p
        if total == 0: return "[░░░░░░░░░░]"
        d_count = int((d/total) * 10)
        t_count = int((t/total) * 10)
        p_count = 10 - d_count - t_count
        return f"[{'█' * d_count}{'▓' * t_count}{'░' * p_count}]"

    all_features = ["Sign In & Reg", "Coach/Ath Invitation", "Sports (Master)", "Records", "Injuries", "Subscriptions", "Wellness Tracking", 
                    "Chat Feature", "Mobile Widgets", "Training Programs", "Agenda -> Timer", "Dual Language", "Step Count"]

    for feat in all_features:
        s = feature_stats[feat]
        total = s['Done'] + s['Testing'] + s['Pending']
        if total == 0: continue
        
        bar = get_bar(s['Done'], s['Testing'], s['Pending'])
        done_pct = int((s['Done']/total)*100)
        
        print(f"\n**{feat}** {bar} {done_pct}%")
        print(f"  • Status: {s['Done']} Done | {s['Testing']} Testing | {s['Pending']} Pending")
        desc = ", ".join(s['Details'])
        print(f"  • Focus: {desc}")

if __name__ == "__main__":
    analyze_kaptrain_interactive_report()
