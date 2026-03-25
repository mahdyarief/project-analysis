import json

# Path to the latest Notion query output
input_path = r'C:\Users\Lenovo\.gemini\antigravity\brain\d6e32ee7-d0e4-4f49-9c04-7543ff2db268\.system_generated\steps\289\output.txt'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Group by Epic and Task Layer with specific status splits
features = {}
for task in data['results']:
    p = task['properties']
    
    # Extract Epic
    epic_obj = p.get('Epic')
    epic = epic_obj['select']['name'] if epic_obj and epic_obj.get('select') else 'Uncategorized'
    
    # Extract Layer
    layer_obj = p.get('Task Layer')
    layer = layer_obj['select']['name'] if layer_obj and layer_obj.get('select') else 'Unknown'
    
    # Extract Status
    status_obj = p.get('Status')
    status = status_obj['select']['name'] if status_obj and status_obj.get('select') else 'New'
    
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

# Write to final report file
report_file = 'nfa_recheck_split.txt'
with open(report_file, 'w', encoding='utf-8') as f:
    for epic in sorted(features.keys()):
        layers = features[epic]
        
        layer_parts = []
        for l in ['FE', 'BE', 'WIRED']:
            d = layers[l]
            ip = round(d['ip'] / d['t'] * 100) if d['t'] > 0 else 0
            rt = round(d['rt'] / d['t'] * 100) if d['t'] > 0 else 0
            layer_parts.append(f"{l}: [IP: {ip}% | Ready: {rt}%]")
        
        f.write(f"• {epic}: {' | '.join(layer_parts)}\n")

print(f"Update completed. Results in {report_file}")
