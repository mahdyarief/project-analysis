
import json

class NotionTask:
    """Helper to parse Notion task properties consistently."""
    def __init__(self, raw_data):
        self.raw = raw_data
        self.id = raw_data.get('id')
        self.properties = raw_data.get('properties', {})

    def get_text(self, prop_name):
        prop = self.properties.get(prop_name, {})
        prop_type = prop.get('type')
        if prop_type == 'title':
            titles = prop.get('title', [])
            return "".join([t.get('plain_text', '') for t in titles])
        if prop_type == 'rich_text':
            texts = prop.get('rich_text', [])
            return "".join([t.get('plain_text', '') for t in texts])
        return ""

    def get_select(self, prop_name):
        prop = self.properties.get(prop_name, {})
        if prop.get('type') == 'select':
            select = prop.get('select')
            return select.get('name') if select else "To Do"
        return "To Do"

    def get_multi_select(self, prop_name):
        prop = self.properties.get(prop_name, {})
        if prop.get('type') == 'multi_select':
            return [ms.get('name') for ms in prop.get('multi_select', [])]
        return []

    def get_status_normalized(self, status_map):
        """Maps project-specific status to internal: Done, Testing, In Progress, Pending."""
        raw_status = self.get_select('Status')
        # Handle cases where Status might be a 'status' type instead of 'select'
        if not raw_status or raw_status == "To Do":
            prop = self.properties.get('Status', {})
            if prop.get('type') == 'status':
                raw_status = prop.get('status', {}).get('name', 'To Do')
        
        return status_map.get(raw_status, 'Pending')
