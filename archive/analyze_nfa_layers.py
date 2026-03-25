import json

# Using absolute path for the input file
input_path = r'C:\Users\Lenovo\.gemini\antigravity\brain\d6e32ee7-d0e4-4f49-9c04-7543ff2db268\.system_generated\steps\32\output.txt'

with open(input_path, 'r') as f:
    data = json.load(f)

results = data['results']

layers = {
    'FE': {'total': 0, 'inprogress': 0, 'done': 0, 'new': 0},
    'BE': {'total': 0, 'inprogress': 0, 'done': 0, 'new': 0},
    'WIRED': {'total': 0, 'inprogress': 0, 'done': 0, 'new': 0}
}

for task in results:
    props = task['properties']
    layer = props['Task Layer']['select']['name'] if props.get('Task Layer') and props['Task Layer'].get('select') else 'Unknown'
    status = props['Status']['select']['name'] if props.get('Status') and props['Status'].get('select') else 'New'
    
    if layer in layers:
        layers[layer]['total'] += 1
        if status == 'Inprogress':
            layers[layer]['inprogress'] += 1
        elif status == 'Done':
            layers[layer]['done'] += 1
        elif status == 'New':
            layers[layer]['new'] += 1

# Calculate percentages
report = {}
for layer, counts in layers.items():
    if counts['total'] > 0:
        report[layer] = {
            'total': counts['total'],
            'inprogress_pct': round((counts['inprogress'] / counts['total']) * 100, 2),
            'done_pct': round((counts['done'] / counts['total']) * 100, 2),
            'new_pct': round((counts['new'] / counts['total']) * 100, 2),
            'inprogress_count': counts['inprogress']
        }

print(json.dumps(report, indent=2))
