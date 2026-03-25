import json

input_path = r'C:\Users\Lenovo\.gemini\antigravity\brain\d6e32ee7-d0e4-4f49-9c04-7543ff2db268\.system_generated\steps\32\output.txt'
output_path = r'd:\Github\Gemini Gems\project-manager\descriptive_report.txt'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

results = data['results']
features = {}

for task in results:
    props = task['properties']
    epic = props['Epic']['select']['name'] if props.get('Epic') and props['Epic'].get('select') else 'Uncategorized'
    layer = props['Task Layer']['select']['name'] if props.get('Task Layer') and props['Task Layer'].get('select') else 'Unknown'
    status = props['Status']['select']['name'] if props.get('Status') and props['Status'].get('select') else 'New'
    
    if epic not in features:
        features[epic] = {'FE': {'t':0, 'i':0}, 'BE': {'t':0, 'i':0}, 'WIRED': {'t':0, 'i':0}}
    
    if layer in features[epic]:
        features[epic][layer]['t'] += 1
        if status == 'Inprogress':
            features[epic][layer]['i'] += 1

with open(output_path, 'w', encoding='utf-8') as f:
    for epic in sorted(features.keys()):
        layers = features[epic]
        
        def get_pct(l):
            d = layers[l]
            return round(d['i'] / d['t'] * 100) if d['t'] > 0 else 0
            
        fe = get_pct('FE')
        be = get_pct('BE')
        wired = get_pct('WIRED')
        
        f.write(f"• {epic}: FE In Progress: {fe}% | BE In Progress: {be}% | Wired In Progress: {wired}%\n")

print("Done")
