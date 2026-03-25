import json

with open("C:/Users/Lenovo/.gemini/antigravity/brain/5e5c5e31-7cbb-4e52-92fc-fb8a2f33bdce/.system_generated/steps/223/output.txt", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Has more: {data.get('has_more')}")
print(f"Next cursor: {data.get('next_cursor')}")
