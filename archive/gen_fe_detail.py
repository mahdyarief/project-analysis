import json

input_path = r'C:\Users\Lenovo\.gemini\antigravity\brain\d6e32ee7-d0e4-4f49-9c04-7543ff2db268\.system_generated\steps\289\output.txt'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

fe_tasks = {'Inprogress': [], 'New': []}

for task in data['results']:
    p = task['properties']
    layer = p['Task Layer']['select']['name'] if p.get('Task Layer') and p['Task Layer'].get('select') else 'Unknown'
    
    if layer == 'FE':
        status = p['Status']['select']['name'] if p.get('Status') and p['Status'].get('select') else 'New'
        if status in ['Inprogress', 'New']:
            epic = p['Epic']['select']['name'] if p.get('Epic') and p['Epic'].get('select') else 'Uncategorized'
            title = p['Title']['title'][0]['plain_text'] if p.get('Title') and p['Title'].get('title') else 'No Name'
            fe_tasks[status].append(f"• **{epic}**: {title}")

with open('fe_status_detail.txt', 'w', encoding='utf-8') as f:
    f.write("### 🚧 Frontend (FE) - Tasks Still In Progress\n")
    if fe_tasks['Inprogress']:
        for t in sorted(fe_tasks['Inprogress']):
            f.write(f"{t}\n")
    else:
        f.write("No tasks currently In Progress.\n")
        
    f.write("\n### 📋 Frontend (FE) - New Tasks (Backlog)\n")
    if fe_tasks['New']:
        for t in sorted(fe_tasks['New']):
            f.write(f"{t}\n")
    else:
        f.write("No new tasks in backlog.\n")
