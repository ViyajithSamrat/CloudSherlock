import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/cloud_cost_sample.csv", parse_dates=["date"])
print(df.head())

daily = df.groupby("date")["cost"].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=daily, x="date", y="cost")
plt.title("Total Cloud Cost Over Time")
plt.grid(True)
plt.tight_layout()
plt.show()
