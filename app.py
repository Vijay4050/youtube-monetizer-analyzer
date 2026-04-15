import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="YouTube Monetization Analyzer", layout="wide")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv(r"D:/Viki/Guvi DS/Capstone Projects/youtube-monetization/notebook/youtube_data2.csv")

# -----------------------------
# Model (ONLY watch_time_minutes)
# -----------------------------
X = df[['watch_time_minutes']]
y = df['ad_revenue_usd']

model = LinearRegression()
model.fit(X, y)

# -----------------------------
# Title
# -----------------------------
st.title("📊 YouTube Monetization Analyzer")

st.markdown("""
### 🚀 Core Insight:
👉 Revenue is almost entirely driven by **Watch Time**
""")

# =============================
# 1️⃣ Revenue Estimation Tool
# =============================
st.header("1️⃣ Revenue Estimation Tool")

watch_time = st.slider("Select Watch Time (minutes)", 0, 10000, 1000)

pred = model.predict([[watch_time]])[0]

st.metric("Estimated Revenue", f"${pred:.2f}")

st.divider()

# =============================
# 2️⃣ Watch Time Sensitivity
# =============================
st.header("2️⃣ Watch Time Sensitivity Simulator")

range_vals = np.arange(0, 10000, 500)
preds = model.predict(range_vals.reshape(-1, 1))

sim_df = pd.DataFrame({
    "Watch Time": range_vals,
    "Revenue": preds
})

st.line_chart(sim_df.set_index("Watch Time"))

st.caption("📈 Revenue increases linearly with watch time")

st.divider()

# =============================
# 3️⃣ Benchmarking
# =============================
st.header("3️⃣ Content Performance Benchmarking")

col1, col2 = st.columns(2)

with col1:
    wt1 = st.number_input("Scenario A Watch Time", value=2000)

with col2:
    wt2 = st.number_input("Scenario B Watch Time", value=5000)

rev1 = model.predict([[wt1]])[0]
rev2 = model.predict([[wt2]])[0]

col1.metric("Revenue A", f"${rev1:.2f}")
col2.metric("Revenue B", f"${rev2:.2f}")

if rev1 > rev2:
    st.success("Scenario A performs better 🚀")
elif rev2 > rev1:
    st.success("Scenario B performs better 🚀")

st.divider()

# =============================
# 4️⃣ Creator Decision Support
# =============================
st.header("4️⃣ Creator Decision Support")

st.info("""
### 🎯 Key Takeaways:

- Watch Time is the **primary driver of revenue**
- Other features have negligible impact
- Increasing watch time directly increases earnings

### 📌 Strategy:

- Improve audience retention
- Focus on engaging content
- Optimize video hooks

👉 **Maximize Watch Time = Maximize Revenue**
""")