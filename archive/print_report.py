import json

input_path = r'C:\Users\Lenovo\.gemini\antigravity\brain\d6e32ee7-d0e4-4f49-9c04-7543ff2db268\.system_generated\steps\184\output.txt'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

features = {}
for task in data['results']:
    p = task['properties']
    epic = p['Epic']['select']['name'] if p.get('Epic') and p['Epic'].get('select') else 'Uncategorized'
    layer = p['Task Layer']['select']['name'] if p.get('Task Layer') and p['Task Layer'].get('select') else 'Unknown'
    status = p['Status']['select']['name'] if p.get('Status') and p['Status'].get('select') else 'New'
    
    if epic not in features:
        features[epic] = {
            'FE': {'t': 0, 'ip': 0, 'rt': 0},
            'BE': {'t': 0, 'ip': 0, 'rt': 0},
            'WIRED': {'t': 0, 'ip': 0, 'rt': 0}
        }
    
    if layer in features[epic]:
        features[epic][layer]['t'] += 1
        if status == 'Inprogress':
            features[epic][layer]['ip'] += 1
        elif status == 'Ready To Test':
            features[epic][layer]['rt'] += 1

for epic in sorted(features.keys()):
    layers = features[epic]
    line = f"• **{epic}**:"
    for l in ['FE', 'BE', 'WIRED']:
        d = layers[l]
        ip = round(d['ip'] / d['t'] * 100) if d['t'] > 0 else 0
        rt = round(d['rt'] / d['t'] * 100) if d['t'] > 0 else 0
        line += f" | {l}: IP: {ip}% - RT: {rt}%"
    print(line)
