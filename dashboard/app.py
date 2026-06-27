import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    layout="wide"
)

st.title("📊 Mutual Fund Analytics Dashboard")

# ----------------------------
# Load Data
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
csv_file = BASE_DIR / "data" / "processed" / "combined_mutual_funds.csv"

df = pd.read_csv(csv_file)

# Convert date safely
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# ----------------------------
# Sidebar
# ----------------------------
funds = st.sidebar.multiselect(
    "Select Funds",
    options=sorted(df["fund"].unique()),
    default=sorted(df["fund"].unique())
)

filtered = df[df["fund"].isin(funds)].copy()

# ----------------------------
# KPI Section
# ----------------------------
st.subheader("📌 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Total Funds", filtered["fund"].nunique())

latest_nav = filtered.sort_values("date")["nav"].iloc[-1]
col2.metric("Latest NAV", f"{latest_nav:.2f}")

col3.metric("Average NAV", f"{filtered['nav'].mean():.2f}")

# ----------------------------
# Dataset Preview
# ----------------------------
st.subheader("Dataset Preview")

preview = filtered.copy()
preview["date"] = preview["date"].dt.strftime("%Y-%m-%d")

st.dataframe(preview.head())

# ----------------------------
# Summary Statistics
# ----------------------------
st.subheader("Summary Statistics")

summary = filtered[["nav"]].describe()

st.dataframe(summary)

# ----------------------------
# NAV Trend
# ----------------------------
st.subheader("📈 NAV Trend")

fig, ax = plt.subplots(figsize=(12,5))

for fund in funds:
    temp = filtered[filtered["fund"] == fund].sort_values("date")
    ax.plot(temp["date"], temp["nav"], label=fund)

ax.set_xlabel("Date")
ax.set_ylabel("NAV")
ax.set_title("NAV Trend")
ax.legend()

st.pyplot(fig)

# ----------------------------
# Latest NAV
# ----------------------------
st.subheader("Latest NAV")

latest = (
    filtered.sort_values("date")
    .groupby("fund")
    .tail(1)[["fund","date","nav"]]
    .copy()
)

latest["date"] = latest["date"].dt.strftime("%Y-%m-%d")

st.dataframe(latest)

# ----------------------------
# Download Filtered Data
# ----------------------------
st.subheader("Download Data")

download_df = filtered.copy()
download_df["date"] = download_df["date"].dt.strftime("%Y-%m-%d")

csv = download_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered CSV",
    data=csv,
    file_name="filtered_mutual_funds.csv",
    mime="text/csv",
)