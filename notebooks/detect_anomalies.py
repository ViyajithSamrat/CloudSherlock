import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

# Load CSV
df = pd.read_csv("data/cloud_cost_sample.csv", parse_dates=["date"])

# Group daily cost
daily_cost = df.groupby("date")["cost"].sum().reset_index()

# Fit Isolation Forest
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
daily_cost["anomaly"] = model.fit_predict(daily_cost[["cost"]])

# -1 = anomaly, 1 = normal
anomalies = daily_cost[daily_cost["anomaly"] == -1]

# Save output
daily_cost.to_csv("data/cost_with_anomalies.csv", index=False)
print("[✅] Saved labeled data → data/cost_with_anomalies.csv")

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_cost, x="date", y="cost", label="Cost")
sns.scatterplot(data=anomalies, x="date", y="cost", color="red", label="Anomaly", s=100)
plt.title("💥 Anomaly Detection in Cloud Costs")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
