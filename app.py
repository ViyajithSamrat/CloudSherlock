import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/cost_with_anomalies.csv", parse_dates=["date"])

st.set_page_config(page_title="CloudSherlock", layout="wide")
st.title("🔍 CloudSherlock: AI-Powered Cloud Cost Anomaly Detection")

# Overview
st.markdown("""
Track and detect anomalies in your cloud spend using AI.
Built with **Isolation Forest**, **Python**, and **Streamlit**.
""")

# KPIs
total_cost = df["cost"].sum()
num_anomalies = df[df["anomaly"] == -1].shape[0]
avg_cost = df["cost"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Cost", f"${total_cost:,.2f}")
col2.metric("🚨 Anomalies", num_anomalies)
col3.metric("📊 Avg Daily Cost", f"${avg_cost:,.2f}")

# Filter options
with st.sidebar:
    st.header("🔎 Filter")
    services = st.multiselect("Service", df["service"].unique(), default=df["service"].unique())
    region = st.selectbox("Region", df["region"].unique())

filtered = df[df["service"].isin(services) & (df["region"] == region)]

# Plot
fig = px.line(filtered.groupby("date")["cost"].sum().reset_index(),
              x="date", y="cost", title="📈 Daily Cloud Spend")
anomalies = df[df["anomaly"] == -1]
fig.add_scatter(x=anomalies["date"], y=anomalies["cost"],
                mode='markers', name="Anomaly", marker=dict(color='red', size=10))

st.plotly_chart(fig, use_container_width=True)

# Show raw data
with st.expander("📄 View Raw Anomalies"):
    st.dataframe(anomalies)
