import json

# Absolute path to the raw tasks from Notion (retrieved in step 184)
input_path = r'C:\Users\Lenovo\.gemini\antigravity\brain\d6e32ee7-d0e4-4f49-9c04-7543ff2db268\.system_generated\steps\184\output.txt'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Group by Epic and Task Layer
features = {}
for task in data['results']:
    p = task['properties']
    epic = p['Epic']['select']['name'] if p.get('Epic') and p['Epic'].get('select') else 'Uncategorized'
    layer = p['Task Layer']['select']['name'] if p.get('Task Layer') and p['Task Layer'].get('select') else 'Unknown'
    status = p['Status']['select']['name'] if p.get('Status') and p['Status'].get('select') else 'New'
    
    if epic not in features:
        features[epic] = {'FE': {'t': 0, 'p': 0}, 'BE': {'t': 0, 'p': 0}, 'WIRED': {'t': 0, 'p': 0}}
    
    if layer in features[epic]:
        features[epic][layer]['t'] += 1
        # Progress = anything that isn't 'New'
        if status in ['Inprogress', 'Ready To Test', 'Done']:
            features[epic][layer]['p'] += 1

# List to store formatted strings
report = []
for epic in sorted(features.keys()):
    layers = features[epic]
    
    def calc(layer_name):
        d = layers[layer_name]
        return round(d['p'] / d['t'] * 100) if d['t'] > 0 else 0
    
    fe = calc('FE')
    be = calc('BE')
    wired = calc('WIRED')
    
    report.append(f"• **{epic}**: FE: {fe}% | BE: {be}% | Wired: {wired}%")

print("\n".join(report))
