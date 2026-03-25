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

    all_tasks = []
    for f in task_files:
        if not os.path.exists(f): continue
        with open(f, 'r', encoding='utf-8') as file:
            data = json.load(file)
            all_tasks.extend(data.get('results', []))

    # Feature Mapping Config
    FEAT_MAP = {
        "Account Sign In & Registration": ["Onboarding", "Login", "OTP", "Password", "Sign", "Registration", "athlete profile"],
        "Sports (Master & Selection)": ["Sport", "Master sport"],
        "Athlete Wellness Tracking": ["Wellness", "Daily Check", "Weight", "Sleep", "Tracking"],
        "Subscriptions (Master & Payments)": ["Abonnement", "Payment", "Free Trial", "Subscription"],
        "Coach & Athlete Connection": ["Invitation", "Coach", "Athlete", "Connexion"],
        "Records (Master & Selection)": ["Mes Record", "My record", "Record"],
        "Injuries": ["Injure", "Muscle-map", "Blessure"],
        "Chat feature": ["Chat", "Messaging", "Message"],
        "Training Programs": ["Programmation", "Programme", "Session", "Séance", "Exercice", "Block forms"],
        "Agenda \u2192 Timer": ["Agenda", "Timer", "Stopwatch", "Chronometer"],
        "All mobile widgets": ["Widget"],
        "Dual language": ["Language", "French", "English", "Translati"],
        "Step count": ["Step Count", "Steps"]
    }

    feature_stats = {name: {"total": 0, "done": 0, "testing": 0} for name in FEAT_MAP}
    uncategorized = 0

    for task in all_tasks:
        props = task.get('properties', {})
        task_name_obj = props.get('Task name', {}).get('title', []) or []
        task_name = task_name_obj[0].get('plain_text', '').lower() if task_name_obj else ''
        
        status_name = (props.get('Status', {}).get('select', {}) or {}).get('name', 'To Do')
        is_done = (status_name == 'Done')
        is_testing = ('Testing' in status_name) or (status_name == 'Review Needed')

        found = False
        for feat, keywords in FEAT_MAP.items():
            if any(k.lower() in task_name for k in keywords):
                feature_stats[feat]["total"] += 1
                if is_done: feature_stats[feat]["done"] += 1
                elif is_testing: feature_stats[feat]["testing"] += 1
                found = True
                # Break if prioritizing first match? No, let's just break on first.
                break
        if not found:
            uncategorized += 1

    # Output Report
    print("🚀 KAPTRAIN FEATURE STATUS BREAKDOWN (18-03-2026)")
    
    # Sections as requested
    completed_feats = [
        "Account Sign In & Registration",
        "Sports (Master & Selection)",
        "Athlete Wellness Tracking",
        "Subscriptions (Master & Payments)",
        "Coach & Athlete Connection",
        "Records (Master & Selection)",
        "Injuries"
    ]
    
    finalizing_feats = [
        "Chat feature",
        "Training Programs",
        "Agenda \u2192 Timer",
        "All mobile widgets",
        "Dual language",
        "Step count"
    ]

    print("\n✅ Features completed (available for testing now)")
    for feat in completed_feats:
        stats = feature_stats[feat]
        total = stats["total"]
        if total > 0:
            done_p = (stats["done"] / total) * 100
            test_p = (stats["testing"] / total) * 100
            print(f"* {feat}: Done: {done_p:.0f}% | Testing: {test_p:.0f}%")
        else:
            print(f"* {feat}: No tasks identified")

    print("\n🚧 Features currently being finalized")
    for feat in finalizing_feats:
        stats = feature_stats[feat]
        total = stats["total"]
        if total > 0:
            done_p = (stats["done"] / total) * 100
            test_p = (stats["testing"] / total) * 100
            print(f"* {feat}: Done: {done_p:.0f}% | Testing: {test_p:.0f}%")
        else:
            print(f"* {feat}: No tasks identified")

if __name__ == "__main__":
    analyze()
