import json

input_path = r'C:\Users\Lenovo\.gemini\antigravity\brain\d6e32ee7-d0e4-4f49-9c04-7543ff2db268\.system_generated\steps\32\output.txt'

with open(input_path, 'r') as f:
    data = json.load(f)

results = data['results']
features = {}

for task in results:
    props = task['properties']
    epic = props['Epic']['select']['name'] if props.get('Epic') and props['Epic'].get('select') else 'Uncategorized'
    layer = props['Task Layer']['select']['name'] if props.get('Task Layer') and props['Task Layer'].get('select') else 'Unknown'
    status = props['Status']['select']['name'] if props.get('Status') and props['Status'].get('select') else 'New'
    
    if epic not in features:
        features[epic] = {
            'FE': {'total': 0, 'inprogress': 0},
            'BE': {'total': 0, 'inprogress': 0},
            'WIRED': {'total': 0, 'inprogress': 0}
        }
    
    if layer in features[epic]:
        features[epic][layer]['total'] += 1
        if status == 'Inprogress':
            features[epic][layer]['inprogress'] += 1

print("--- NFA FEATURE PROGRESS BREAKDOWN ---")
for epic, layers in sorted(features.items()):
    parts = []
    for layer in ['FE', 'BE', 'WIRED']:
        d = layers[layer]
        pct = round((d['inprogress'] / d['total'] * 100)) if d['total'] > 0 else 0
        parts.append(f"{layer} In Progress: {pct}%")
    print(f"• {epic}: {' | '.join(parts)}")
