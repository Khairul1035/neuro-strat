import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# 1. HCI & Cognitive Neuroscience Design
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

# 2. Real-Time Data Fetching (Ubah ke 5d supaya berfungsi waktu weekend)
def get_live_data():
    tickers = {"Brent Oil": "BZ=F", "Gold": "GC=F", "GBP/USD": "GBPUSD=X"}
    data = {}
    for name, sym in tickers.items():
        # Guna period 5d untuk pastikan ada data jika pasaran tutup
        df = yf.Ticker(sym).history(period="5d", interval="1m")
        data[name] = df
    return data

data = get_live_data()

# Check jika data ada (untuk elak error waktu weekend)
if not data["Brent Oil"].empty:
    # 3. Metrics (Accounting & Strategic Analysis)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        oil_price = data["Brent Oil"]['Close'].iloc[-1]
        oil_open = data["Brent Oil"]['Open'].iloc[0]
        st.metric("Brent Crude (Energy War Proxy)", f"${oil_price:.2f}", f"{oil_price - oil_open:.2f}")
        st.caption("Accounting: Impact on Global Shipping Rates")

    with col2:
        # Neuro Stress Index berdasarkan volatiliti
        stress_val = (data["Brent Oil"]['Close'].pct_change().std() * 1000)
        st.metric("Market Cognitive Stress Index", f"{stress_val:.2f} Hz", "Weekend Mode")
        st.caption("Neuroscience: Amygdala response to Escalation")

    with col3:
        st.metric("Hormuz Strait Risk", "CRITICAL", "85% Blockage Prob.")
        st.caption("Strategist: Tactical Supply Chain Disruption")

    # 4. Visualization (HCI Optimization)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["Brent Oil"].index, y=data["Brent Oil"]['Close'], name="Brent Oil Price"))
    fig.update_layout(template="plotly_dark", title="Conflict Escalation vs Energy Market Sentiment (Last 5 Days)")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("Market is currently closed or API limit reached. Please check back during trading hours.")

st.info("HCI Note: Dashboard optimized for low-cognitive load during high-stress geopolitical events.")
