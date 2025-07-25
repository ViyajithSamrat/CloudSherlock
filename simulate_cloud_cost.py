# simulate_cloud_cost.py

import pandas as pd
import random
from datetime import datetime, timedelta

services = ['EC2', 'S3', 'Lambda', 'RDS', 'CloudWatch']
regions = ['us-east-1', 'us-west-2', 'eu-central-1']
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 1, 1)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

data = []

for date in date_range:
    for _ in range(random.randint(5, 15)):
        service = random.choice(services)
        region = random.choice(regions)
        cost = round(random.uniform(5, 200), 2)
        account_id = f"A{random.randint(1000, 9999)}"
        data.append([date, service, cost, account_id, region])

df = pd.DataFrame(data, columns=["date", "service", "cost", "account_id", "region"])
df.to_csv("data/cloud_cost_sample.csv", index=False)

print("✅ Simulated dataset saved to data/cloud_cost_sample.csv")
