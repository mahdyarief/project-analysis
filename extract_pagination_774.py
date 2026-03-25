import json

file_path = r'C:\Users\Lenovo\.gemini\antigravity\brain\5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce\.system_generated\steps\774\output.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Count: {len(data['results'])}")
print(f"Has More: {data['has_more']}")
print(f"Next Cursor: {data['next_cursor']}")
