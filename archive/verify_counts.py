import json

with open("C:/Users/Lenovo/.gemini/antigravity/brain/5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce/.system_generated/steps/66/output.txt", "r", encoding="utf-8") as f:
    data = json.load(f)

counts = {}
for page in data.get('results', []):
    status_prop = page['properties'].get('Status', {})
    if 'select' in status_prop and status_prop['select']:
        name = status_prop['select']['name']
    else:
        name = "No Status"
    counts[name] = counts.get(name, 0) + 1

total = sum(counts.values())
print(f"Total pages in file: {total}")
print(json.dumps(counts, indent=2))
