import pandas as pd
from tabulate import tabulate

# Load anomaly-labeled data
df = pd.read_csv("data/cost_with_anomalies.csv", parse_dates=["date"])

# Keep only flagged anomalies
anomalies = df[df["anomaly"] == -1].copy()
anomalies["Anomaly"] = "❌"
anomalies["Cost ($)"] = anomalies["cost"].round(2)
anomalies["Date"] = anomalies["date"].dt.strftime("%Y-%m-%d")

# Format for table
table = anomalies[["Date", "Cost ($)", "Anomaly"]]

if table.empty:
    print("✅ No anomalies detected. All costs look normal.")
else:
    print("💥 Anomalies Detected in Cloud Spend:\n")
    print(tabulate(table, headers="keys", tablefmt="fancy_grid"))
