
# project-specific status mappings
DEFAULT_STATUS_MAP = {
    'Done': 'Done',
    'Completed': 'Done',
    'In Testing (Staging)': 'Testing',
    'Ready To Test': 'Testing',
    'In Progress': 'In Progress',
    'Inprogress': 'In Progress',
    'To Do': 'Pending',
    'New': 'Pending',
    'Bug': 'Pending'
}

# Project Definitions
PROJECTS = {
    "Kaptrain": {
        "status_map": DEFAULT_STATUS_MAP,
        "title_prop": "Task name",
        "features": {
            "Sign In & Profile": ["signin", "sign in", "login", "register", "profile", "otp", "auth", "connexion", "profil", "inscription", "masuk", "daftar"],
            "Coach/Athlete Invitation": ["invite", "invitation", "undangan"],
            "Sports & Records": ["sport", "record", "index mes", "sélection", "olahraga"],
            "Wellness Tracking": ["wellness", "check-in", "weight", "daily check", "bien-être", "suivi", "sehat", "harian", "berat"],
            "Training Programs": ["program", "training", "exercise", "workout", "session", "entraînement", "séance", "latihan", "urutan", "jadwal"],
            "Messenger & Notifications": ["chat", "message", "messenger", "notification", "pesan", "ngobrol", "notif"],
            "Mobile Widgets": ["widget"],
            "Subscriptions & Payments": ["subscription", "payment", "stripe", "price", "billing", "abonnement", "paiement", "langganan", "bayar", "tagihan"],
            "Athlete Management (CMS)": ["athlete details", "athlete list", "cms athlete", "liste", "daftar atlet", "cms"]
        }
    },
    "NFA": {
        "status_map": {
            'Done': 'Done',
            'Ready To Test': 'Testing',
            'Inprogress': 'In Progress',
            'New': 'Pending'
        },
        "title_prop": "Title",
        "features": {
            # NFA uses 'Epic' property usually, but we can fallback to title keywords
            "General": ["nfa"]
        },
        "use_epic_prop": True # Flag to prioritize Epic property over keywords
    }
}
