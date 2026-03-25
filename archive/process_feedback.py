import json
import os

def process_feedback():
    filepath = r'C:\Users\Lenovo\.gemini\antigravity\brain\5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce\.system_generated\steps\420\output.txt'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    results = data.get('results', [])
    report = {
        'Status': {},
        'Category': {},
        'Type': {},
        'Items': []
    }

    for page in results:
        props = page['properties']
        
        # Title
        title = ""
        if props.get('Nom', {}).get('title'):
            title = props['Nom']['title'][0]['text']['content']
        if not title: continue # Skip empty titles

        # Status
        status = props.get('Status', {}).get('select', {}).get('name', 'Unknown') if props.get('Status', {}).get('select') else 'Unknown'
        
        # Category
        category = props.get('Category', {}).get('select', {}).get('name', 'Unknown') if props.get('Category', {}).get('select') else 'Unknown'
        
        # Type
        item_type = props.get('Type', {}).get('select', {}).get('name', 'Unknown') if props.get('Type', {}).get('select') else 'Unknown'
        
        # Description
        desc = ""
        if props.get('Description', {}).get('rich_text'):
            desc = props['Description']['rich_text'][0]['text']['content']

        report['Status'][status] = report['Status'].get(status, 0) + 1
        report['Category'][category] = report['Category'].get(category, 0) + 1
        report['Type'][item_type] = report['Type'].get(item_type, 0) + 1
        
        report['Items'].append({
            'title': title,
            'status': status,
            'category': category,
            'type': item_type,
            'desc': desc
        })

    # Sort items by status (New first)
    report['Items'].sort(key=lambda x: x['status'] != 'New')

    # Group by themes for a nice Markdown report
    themes = {
        "Wellness & Graphics": [],
        "Exercises & Library": [],
        "UI & Aesthetic (Figma Alignment)": [],
        "CMS Functional": [],
        "Other": []
    }

    for item in report['Items']:
        t = item['title'].lower() + " " + item['desc'].lower()
        if 'wellness' in t or 'curve' in t or 'graph' in t or 'sleep' in t:
            themes["Wellness & Graphics"].append(item)
        elif 'exercice' in t or 'exercise' in t or 'library' in t or 'photo' in t or 'muscle' in t:
            themes["Exercises & Library"].append(item)
        elif 'figma' in t or 'misalignment' in t or 'space' in t or 'menu' in t or 'logo' in t:
            themes["UI & Aesthetic (Figma Alignment)"].append(item)
        elif 'cms' in item['type'] or 'button' in t or 'translate' in t or 'validate' in t:
            themes["CMS Functional"].append(item)
        else:
            themes["Other"].append(item)

    # Print summary
    print(f"# Feedback Status Report - {os.path.basename(filepath)}")
    print("\n## Distribution")
    print(f"- **Total Items**: {len(report['Items'])}")
    print(f"- **Status**: {report['Status']}")
    print(f"- **Category**: {report['Category']}")
    print(f"- **Type**: {report['Type']}")

    print("\n## Theme Breakdown")
    for theme, items in themes.items():
        if not items: continue
        print(f"\n### {theme}")
        for item in items:
            status_emoji = "🟢" if item['status'] == 'Done' else "🟡" if item['status'] == 'Need confirm' else "🔴"
            print(f"- {status_emoji} **{item['title']}** [{item['category']} | {item['type']}]")
            if item['desc']:
                print(f"  > _{item['desc'].strip()}_")

if __name__ == "__main__":
    process_feedback()
