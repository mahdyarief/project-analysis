import json

# Absolute path to the raw tasks from Notion
input_path = r'C:\Users\Lenovo\.gemini\antigravity\brain\d6e32ee7-d0e4-4f49-9c04-7543ff2db268\.system_generated\steps\32\output.txt'

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
        features[epic] = {'FE': {'t': 0, 'i': 0}, 'BE': {'t': 0, 'i': 0}, 'WIRED': {'t': 0, 'i': 0}}
    
    if layer in features[epic]:
        features[epic][layer]['t'] += 1
        if status == 'Inprogress':
            features[epic][layer]['i'] += 1

# Extract pure numbers first to avoid logic in f-strings
report = []
for epic in sorted(features.keys()):
    layers = features[epic]
    
    def calc(layer_name):
        d = layers[layer_name]
        return round(d['i'] / d['t'] * 100) if d['t'] > 0 else 0
    
    report.append({
        'feature': epic,
        'FE': calc('FE'),
        'BE': calc('BE'),
        'WIRED': calc('WIRED')
    })

# Final clean print
for r in report:
    print(f"REPORT_LINE|{r['feature']}|FE:{r['FE']}%|BE:{r['BE']}%|WIRED:{r['WIRED']}%")
