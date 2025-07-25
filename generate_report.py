import pandas as pd
from datetime import datetime
import os

report_path = "anomaly_report.csv"
output_file = f"CloudSherlock_Report_{datetime.now().date()}.html"

if not os.path.exists(report_path):
    print("❌ Anomaly report not found.")
    exit()

df = pd.read_csv(report_path)

html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>CloudSherlock Anomaly Report</title>
    <style>
        body {{ font-family: Arial; padding: 20px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; }}
        th {{ background-color: #4CAF50; color: white; }}
    </style>
</head>
<body>
    <h2>🚨 CloudSherlock - Anomaly Report</h2>
    <p>Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    {df.to_html(index=False)}
</body>
</html>
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ HTML report generated: {output_file}")
