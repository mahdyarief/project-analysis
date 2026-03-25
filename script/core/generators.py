
import csv
import os
from datetime import datetime

class ReportGenerator:
    def __init__(self, project_name):
        self.project_name = project_name
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")


    def generate_markdown(self, stats, totals):
        total_tasks = sum(totals.values())
        done_pct = (totals["Done"] / total_tasks * 100) if total_tasks > 0 else 0
        test_pct = (totals["Testing"] / total_tasks * 100) if total_tasks > 0 else 0
        
        lines = [
            f"# 🚀 {self.project_name.upper()} Project Pulse",
            f"*Generated on: {self.timestamp}*",
            "",
            "## 📈 OVERALL PERFORMANCE",
            f"- ✅ **Done**: {done_pct:.1f}% ({totals['Done']} tasks)",
            f"- 🧪 **Testing**: {test_pct:.1f}% ({totals['Testing']} tasks)",
            f"- ⏳ **In Progress/Pending**: {totals['In Progress'] + totals['Pending']} tasks",
            "",
            "## 🧱 DEVELOPMENT LAYERS",
            self.generate_layer_grid(stats),
            "",
            "## 🎯 FEATURE BREAKDOWN",
            ""
        ]

        def get_bar(d, t, p):
            tot = d + t + p
            if tot == 0: return "[░░░░░░░░░░]"
            d_count = int((d/tot) * 10)
            t_count = int((t/tot) * 10)
            p_count = 10 - d_count - t_count
            return f"[{'█' * d_count}{'▓' * t_count}{'░' * p_count}]"

        # Sorted by completion %
        sorted_features = sorted(
            stats.items(), 
            key=lambda x: (x[1]['Done'] / (sum(v for k,v in x[1].items() if k not in ['Tasks', 'Layers']) or 1)), 
            reverse=True
        )

        for feat, counts in sorted_features:
            total_feat = sum(counts[k] for k in ["Done", "Testing", "In Progress", "Pending"])
            if total_feat == 0: continue
            
            bar = get_bar(counts['Done'], counts['Testing'], counts['In Progress'] + counts['Pending'])
            pct = int((counts['Done']/total_feat)*100)
            
            lines.append(f"### {feat} {bar} {pct}%")
            lines.append(f"  • Status: {counts['Done']} Done | {counts['Testing']} Testing | {counts['In Progress'] + counts['Pending']} Pending")
            focus = ", ".join(counts['Tasks'][:3])
            lines.append(f"  • Recent Tasks: {focus}...")
            lines.append("")

        return "\n".join(lines)

    def generate_layer_grid(self, stats):
        """Generates a table showing progress across layers (FE, BE, WIRED) for each feature."""
        layers = ["FE", "BE", "WIRED"]
        header = "| Feature | " + " | ".join(layers) + " |"
        sep = "| :--- | " + " | ".join([":---:"] * len(layers)) + " |"
        rows = [header, sep]
        
        for feat, counts in sorted(stats.items()):
            row = [f"**{feat}**"]
            for layer in layers:
                l_stats = counts["Layers"].get(layer, {"total": 0, "Done": 0})
                if l_stats["total"] > 0:
                    pct = int((l_stats["Done"] / l_stats["total"]) * 100)
                    row.append(f"{pct}%")
                else:
                    row.append("-")
            rows.append("| " + " | ".join(row) + " |")
        
        return "\n".join(rows)

    def save_csv(self, stats, output_path):
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Feature", "Done", "Testing", "In Progress", "Pending", "Sample Tasks"])
            for feat, counts in stats.items():
                writer.writerow([
                    feat, 
                    counts["Done"], 
                    counts["Testing"], 
                    counts["In Progress"], 
                    counts["Pending"], 
                    "; ".join(counts["Tasks"][:5])
                ])
        print(f"✅ CSV Report saved to: {output_path}")
