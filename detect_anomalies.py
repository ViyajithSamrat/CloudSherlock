import pandas as pd
from sklearn.ensemble import IsolationForest
import os

csv_path = "billing_data.csv"
report_path = "anomaly_report.csv"

if not os.path.exists(csv_path):
    print("❌ billing_data.csv not found.")
    exit()

df = pd.read_csv(csv_path)

# Check if required columns exist
required_cols = {"service", "date", "cost"}
if not required_cols.issubset(df.columns):
    print("❌ Required columns missing in CSV.")
    exit()

model = IsolationForest(contamination=0.2, random_state=42)
df["anomaly"] = model.fit_predict(df[["cost"]])
anomalies = df[df["anomaly"] == -1]

if anomalies.empty:
    print("✅ No anomalies found.")
else:
    anomalies.to_csv(report_path, index=False)
    print(f"✅ Anomalies saved to {report_path}")
