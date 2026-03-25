import json

input_path = r'C:\Users\Lenovo\.gemini\antigravity\brain\d6e32ee7-d0e4-4f49-9c04-7543ff2db268\.system_generated\steps\289\output.txt'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for task in data['results']:
    p = task['properties']
    layer = p['Task Layer']['select']['name'] if p.get('Task Layer') and p['Task Layer'].get('select') else 'Unknown'
    if layer == 'FE':
        epic = p['Epic']['select']['name'] if p.get('Epic') and p['Epic'].get('select') else 'Un'
        status = p['Status']['select']['name'] if p.get('Status') and p['Status'].get('select') else 'New'
        title = p['Title']['title'][0]['plain_text'] if p.get('Title') and p['Title'].get('title') else 'No Name'
        print(f"[{epic}] | {status} | {title}")
