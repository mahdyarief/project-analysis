
from .notion import NotionTask
from ..config.definitions import PROJECTS, DEFAULT_STATUS_MAP
from collections import defaultdict

class ProjectProcessor:
    def __init__(self, project_name):
        self.config = PROJECTS.get(project_name, {
            "status_map": DEFAULT_STATUS_MAP,
            "title_prop": "Task name",
            "features": {}
        })
        self.project_name = project_name


    def process_tasks(self, raw_results):
        processed = []
        for raw in raw_results:
            task = NotionTask(raw)
            title = task.get_text(self.config['title_prop'])
            status = task.get_status_normalized(self.config['status_map'])
            layer = task.get_select('Task Layer')
            
            # Map Feature/Epic
            feature = "Miscellaneous"
            
            # Special logic for NFA Epic property
            if self.config.get('use_epic_prop'):
                epic = task.get_select('Epic')
                if epic and epic != "To Do":
                    feature = epic
            
            # Keyword fallback/override
            if feature == "Miscellaneous":
                title_lower = title.lower()
                for feat, keywords in self.config.get('features', {}).items():
                    if any(kw in title_lower for kw in keywords):
                        feature = feat
                        break
            
            processed.append({
                "title": title,
                "status": status,
                "feature": feature,
                "layer": layer,
                "tags": task.get_multi_select('Tags')
            })
        return processed

    def get_aggregated_stats(self, processed_tasks):
        stats = defaultdict(lambda: {"Done": 0, "Testing": 0, "In Progress": 0, "Pending": 0, "Tasks": [], "Layers": defaultdict(lambda: {"total": 0, "Done": 0, "Testing": 0, "In Progress": 0, "Pending": 0})})
        total_counts = {"Done": 0, "Testing": 0, "In Progress": 0, "Pending": 0}
        
        for t in processed_tasks:
            feat = t['feature']
            stat = t['status']
            layer = t['layer']
            
            stats[feat][stat] += 1
            stats[feat]["Tasks"].append(t['title'])
            stats[feat]["Layers"][layer]["total"] += 1
            stats[feat]["Layers"][layer][stat] += 1
            
            total_counts[stat] += 1
            
        return stats, total_counts
