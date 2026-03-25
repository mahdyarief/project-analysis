
import json
import sys
import os
import argparse

# Allow importing from the script directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from script.core.processor import ProjectProcessor
from script.core.generators import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description="Analyze Notion Project Data")
    parser.add_argument("project", help="Project name (e.g., Kaptrain, NFA)")
    parser.add_argument("--input", help="Path to JSON data file", required=True)
    parser.add_argument("--format", choices=["md", "csv", "all"], default="md", help="Output format")
    parser.add_argument("--output_dir", default="result", help="Directory to save results")
    
    args = parser.parse_args()

    project_name = args.project
    input_file = args.input
    
    if not os.path.exists(input_file):
        print(f"❌ Error: Input file {input_file} not found.")
        return

    print(f"🔍 Analyzing {project_name}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            # Notion API results are usually in 'results' key or the list itself
            raw_results = data.get('results', []) if isinstance(data, dict) else data
        except Exception as e:
            print(f"❌ Error parsing JSON: {e}")
            return

    processor = ProjectProcessor(project_name)
    processed_tasks = processor.process_tasks(raw_results)
    stats, totals = processor.get_aggregated_stats(processed_tasks)

    generator = ReportGenerator(project_name)
    
    os.makedirs(args.output_dir, exist_ok=True)
    
    if args.format in ["md", "all"]:
        report_md = generator.generate_markdown(stats, totals)
        output_file = os.path.join(args.output_dir, f"{project_name}_progress_report.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(report_md)
        print(f"✅ Markdown Report saved to: {output_file}")
        # Also print to stdout for quick viewing
        print("\n--- REPORT SUMMARY ---")
        print(report_md)

    if args.format in ["csv", "all"]:
        output_file = os.path.join(args.output_dir, f"{project_name}_feature_stats.csv")
        generator.save_csv(stats, output_file)

if __name__ == "__main__":
    main()
