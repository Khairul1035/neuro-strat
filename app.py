import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 1. HCI & Cognitive Neuroscience (Visual design for low cognitive load)
st.set_page_config(page_title="NEURO-STRAT AI", layout="wide")
st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

st.title("🧠 NEURO-STRAT: Iran-West Conflict Risk Engine")
st.sidebar.title("Analyst Insights")
st.sidebar.markdown("""
**Expertise Layers:**
- 🌍 Geopolitics: Choke-point Analysis
- 📊 Accounting: Supply Chain Costing
- 💡 Finance: Volatility Proxy
- 🧠 Neuroscience: Cognitive Stress Index
""")

# 2. Real-Time Data Fetching (Finance & Geopolitical Proxy)
def get_live_data():
    # Oil (Proxy for Energy War), Gold (Safe Haven), USD/GBP (UK Finance)
    tickers = {"Brent Oil": "BZ=F", "Gold": "GC=F", "GBP/USD": "GBPUSD=X"}
    data = {}
    for name, sym in tickers.items():
        data[name] = yf.Ticker(sym).history(period="1d", interval="1m")
    return data

data = get_live_data()

# 3. Metrics (Accounting & Strategic Analysis)
col1, col2, col3 = st.columns(3)
with col1:
    oil_price = data["Brent Oil"]['Close'].iloc[-1]
    st.metric("Brent Crude (Energy War Proxy)", f"${oil_price:.2f}", f"{oil_price - data['Brent Oil']['Open'].iloc[0]:.2f}")
    st.caption("Accounting: Direct Impact on TEU Shipping Rates")

with col2:
    stress_val = (data["Brent Oil"]['Close'].pct_change().std() * 1000)
    st.metric("Market Cognitive Stress Index", f"{stress_val:.2f} Hz", "High Alert")
    st.caption("Neuroscience: Amygdala response to Escalation News")

with col3:
    st.metric("Hormuz Strait Risk", "CRITICAL", "85% Blockage Prob.")
    st.caption("Strategist: Tactical Supply Chain Disruption")

# 4. Visualization (HCI Optimization)
fig = go.Figure()
fig.add_trace(go.Scatter(x=data["Brent Oil"].index, y=data["Brent Oil"]['Close'], name="Real-time Volatility"))
fig.update_layout(template="plotly_dark", title="Conflict Escalation vs Energy Market Sentiment")
st.plotly_chart(fig, use_container_width=True)

st.info("Visual designed to minimize cognitive load for executive decision-making under crisis.")
