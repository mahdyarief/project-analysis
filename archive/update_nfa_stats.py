import json

input_path = r'C:\Users\Lenovo\.gemini\antigravity\brain\d6e32ee7-d0e4-4f49-9c04-7543ff2db268\.system_generated\steps\184\output.txt'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

results = data['results']

# Data structures
epics = {}
layers = {
    'FE': {'total': 0, 'inprogress': 0, 'ready_to_test': 0, 'done': 0},
    'BE': {'total': 0, 'inprogress': 0, 'ready_to_test': 0, 'done': 0},
    'WIRED': {'total': 0, 'inprogress': 0, 'ready_to_test': 0, 'done': 0}
}

for task in results:
    props = task['properties']
    
    epic = props['Epic']['select']['name'] if props.get('Epic') and props['Epic'].get('select') else 'Uncategorized'
    layer = props['Task Layer']['select']['name'] if props.get('Task Layer') and props['Task Layer'].get('select') else 'Unknown'
    status = props['Status']['select']['name'] if props.get('Status') and props['Status'].get('select') else 'New'
    sp = (props['Story Points']['number'] or 0) if props.get('Story Points') else 0
    
    # Process Epics
    if epic not in epics:
        epics[epic] = {'total': 0, 'inprogress': 0, 'ready_to_test': 0, 'done': 0, 'sp_total': 0}
    
    epics[epic]['total'] += 1
    epics[epic]['sp_total'] += sp
    if status == 'Inprogress': epics[epic]['inprogress'] += 1
    elif status == 'Ready To Test': epics[epic]['ready_to_test'] += 1
    elif status == 'Done': epics[epic]['done'] += 1
    
    # Process Layers
    if layer in layers:
        layers[layer]['total'] += 1
        if status == 'Inprogress': layers[layer]['inprogress'] += 1
        elif status == 'Ready To Test': layers[layer]['ready_to_test'] += 1
        elif status == 'Done': layers[layer]['done'] += 1

# Output for report generation
final_data = {
    'epics': epics,
    'layers': layers,
    'total_stats': {
        'tasks': len(results),
        'inprogress': sum(e['inprogress'] for e in epics.values()),
        'ready_to_test': sum(e['ready_to_test'] for e in epics.values()),
        'done': sum(e['done'] for e in epics.values()),
        'sp': sum(e['sp_total'] for e in epics.values())
    }
}

print(json.dumps(final_data))
