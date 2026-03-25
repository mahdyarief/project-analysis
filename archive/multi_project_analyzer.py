import json
import csv
import os
from datetime import datetime

# Load Kaptrain data (from previous steps, assuming they are in these files or I'll re-read)
# I'll re-read the files generated in previous turns if they exist, or just use the current task results.
# For simplicity, I'll read from the .system_generated/steps directory where I saved them.
KAPTRAIN_FILES = [
    r'C:\Users\Lenovo\.gemini\antigravity\brain\5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce\.system_generated\steps\66\output.txt',
    r'C:\Users\Lenovo\.gemini\antigravity\brain\5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce\.system_generated\steps\223\output.txt'
]
NFA_FILES = [
    r'C:\Users\Lenovo\.gemini\antigravity\brain\5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce\.system_generated\steps\324\output.txt'
]

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data.get('results', [])

all_kaptrain_tasks = []
for f in KAPTRAIN_FILES:
    all_kaptrain_tasks.extend(load_json(f))

all_nfa_tasks = []
for f in NFA_FILES:
    all_nfa_tasks.extend(load_json(f))

# Define status mapping
# Unified Statuses: Done, Testing, In Progress, Pending/Backlog
STATUS_MAP = {
    # Kaptrain
    'Done': 'Done',
    'In Testing (Staging)': 'Testing',
    'In Progress': 'In Progress',
    'To Do': 'Pending',
    'Bug': 'Pending',
    # NFA
    'Ready To Test': 'Testing',
    'Inprogress': 'In Progress',
    'New': 'Pending'
}

def get_status(task):
    status_obj = task['properties'].get('Status', {}).get('select', {})
    if not status_obj:
        return 'Pending'
    name = status_obj.get('name', 'Pending')
    return STATUS_MAP.get(name, 'Pending')

# Multilingual Feature Keywords (EN, FR, ID)
KAPTRAIN_FEATURE_KEYWORDS = {
    "Sign In & Profile": ["signin", "sign in", "login", "register", "profile", "otp", "auth", "connexion", "profil", "inscription", "masuk", "daftar"],
    "Coach/Athlete Invitation": ["invite", "invitation", "undangan"],
    "Sports & Records": ["sport", "record", "index mes", "sélection", "olahraga"],
    "Wellness Tracking": ["wellness", "check-in", "weight", "daily check", "bien-être", "suivi", "sehat", "harian", "berat"],
    "Training Programs": ["program", "training", "exercise", "workout", "session", "entraînement", "séance", "latihan", "urutan", "jadwal"],
    "Messenger & Notifications": ["chat", "message", "messenger", "notification", "pesan", "ngobrol", "notif"],
    "Mobile Widgets": ["widget"],
    "Subscriptions & Payments": ["subscription", "payment", "stripe", "price", "billing", "abonnement", "paiement", "langganan", "bayar", "tagihan"],
    "Athlete Management (CMS)": ["athlete details", "athlete list", "cms athlete", "liste", "daftar atlet"]
}

def map_kaptrain_feature(title):
    title_lower = title.lower()
    for feature, keywords in KAPTRAIN_FEATURE_KEYWORDS.items():
        if any(kw in title_lower for kw in keywords):
            return feature
    return "UI, CMS & System Core"

# Process Kaptrain
kaptrain_report = {}
for task in all_kaptrain_tasks:
    title = task['properties']['Task name']['title'][0]['text']['content']
    status = get_status(task)
    feature = map_kaptrain_feature(title)
    
    if feature not in kaptrain_report:
        kaptrain_report[feature] = {"Done": 0, "Testing": 0, "In Progress": 0, "Pending": 0, "Tasks": []}
    
    kaptrain_report[feature][status] += 1
    kaptrain_report[feature]["Tasks"].append(title)

# Process NFA
nfa_report = {}
for task in all_nfa_tasks:
    title = task['properties']['Title']['title'][0]['text']['content']
    status = get_status(task)
    epic_obj = task['properties'].get('Epic', {}).get('select', {})
    epic = epic_obj.get('name', 'Uncategorized') if epic_obj else 'Uncategorized'
    
    if epic not in nfa_report:
        nfa_report[epic] = {"Done": 0, "Testing": 0, "In Progress": 0, "Pending": 0, "Tasks": []}
    
    nfa_report[epic][status] += 1
    nfa_report[epic]["Tasks"].append(title)

# Generate CSV
today = datetime.now().strftime("%Y-%m-%d")
csv_filename = f"d:/Github/Gemini Gems/project-manager/daily-reports/reports/{today}_multi_project_feature_report.csv"

with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Project", "Feature Module", "Done", "Testing", "In Progress", "Pending", "Description"])
    
    # Kaptrain rows
    for feature, counts in kaptrain_report.items():
        desc = ", ".join(counts["Tasks"][:3]) + ("..." if len(counts["Tasks"]) > 3 else "")
        writer.writerow(["Kaptrain", feature, counts["Done"], counts["Testing"], counts["In Progress"], counts["Pending"], desc])
    
    # NFA rows
    for epic, counts in nfa_report.items():
        desc = ", ".join(counts["Tasks"][:3]) + ("..." if len(counts["Tasks"]) > 3 else "")
        writer.writerow(["NFA", epic, counts["Done"], counts["Testing"], counts["In Progress"], counts["Pending"], desc])

print(f"CSV Report generated: {csv_filename}")

# Print summary for Markdown
print("\n--- MULTI-PROJECT SUMMARY ---")
print(f"Kaptrain: {len(all_kaptrain_tasks)} tasks")
print(f"NFA: {len(all_nfa_tasks)} tasks")
