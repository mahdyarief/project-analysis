import json

# Path to the latest Notion query output
input_path = r'C:\Users\Lenovo\.gemini\antigravity\brain\d6e32ee7-d0e4-4f49-9c04-7543ff2db268\.system_generated\steps\289\output.txt'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Focus on FE Tasks
epic_details = {}

for task in data['results']:
    p = task['properties']
    layer_obj = p.get('Task Layer')
    layer = layer_obj['select']['name'] if layer_obj and layer_obj.get('select') else 'Unknown'
    
    if layer != 'FE':
        continue
    
    epic_obj = p.get('Epic')
    epic = epic_obj['select']['name'] if epic_obj and epic_obj.get('select') else 'Uncategorized'
    
    status_obj = p.get('Status')
    status = status_obj['select']['name'] if status_obj and status_obj.get('select') else 'New'
    
    title_obj = p.get('Title')
    task_name = 'Unnamed Task'
    if title_obj and title_obj.get('title'):
        task_name = title_obj['title'][0]['plain_text']
    
    if epic not in epic_details:
        epic_details[epic] = {'inprogress': [], 'new': [], 'ready': []}
    
    if status == 'Inprogress':
        epic_details[epic]['inprogress'].append(task_name)
    elif status == 'New':
        epic_details[epic]['new'].append(task_name)
    elif status == 'Ready To Test':
        epic_details[epic]['ready'].append(task_name)

# Result printing
print("--- FRONTEND (FE) STATUS BREAKDOWN ---")
for epic in sorted(epic_details.keys()):
    info = epic_details[epic]
    print(f"\n• {epic}")
    
    if info['inprogress']:
        print("  🚧 In Progress:")
        for t in info['inprogress']: print(f"    - {t}")
    
    if info['new']:
        print("  📋 New / Backlog:")
        for t in info['new']: print(f"    - {t}")
        
    if not info['inprogress'] and not info['new']:
        print("  ✅ All tasks are Ready To Test or Done.")
