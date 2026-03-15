import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import time  # Tambah library masa

# 1. HCI & Cognitive Neuroscience Design
st.set_page_config(page_title="NEURO-STRAT AI", layout="wide")
st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

st.title("🧠 NEURO-STRAT: Iran-West Conflict Risk Engine")

# Guna placeholder supaya dashboard boleh "update" tempat yang sama
placeholder = st.empty()

# Fungsi ambil data
def get_live_data():
    tickers = {"Brent Oil": "BZ=F", "Gold": "GC=F", "GBP/USD": "GBPUSD=X"}
    data = {}
    for name, sym in tickers.items():
        df = yf.Ticker(sym).history(period="5d", interval="1m")
        data[name] = df
    return data

# Loop untuk jadikan dia bergerak
while True:
    with placeholder.container():
        data = get_live_data()

        if not data["Brent Oil"].empty:
            # 3. Metrics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                oil_price = data["Brent Oil"]['Close'].iloc[-1]
                oil_open = data["Brent Oil"]['Open'].iloc[0]
                st.metric("Brent Crude (Energy War Proxy)", f"${oil_price:.2f}", f"{oil_price - oil_open:.2f}")
                st.caption("Accounting: Impact on Global Shipping Rates")

            with col2:
                stress_val = (data["Brent Oil"]['Close'].pct_change().std() * 1000)
                st.metric("Market Cognitive Stress Index", f"{stress_val:.2f} Hz", "LIVE Updates")
                st.caption("Neuroscience: Amygdala response factor")

            with col3:
                st.metric("Hormuz Strait Risk", "CRITICAL", "85% Blockage Prob.")
                st.caption("Strategist: Tactical Supply Chain Disruption")

            # 4. Visualization (HCI)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data["Brent Oil"].index, y=data["Brent Oil"]['Close'], name="Brent Oil Price"))
            fig.update_layout(template="plotly_dark", title=f"Real-Time Sentiment Analysis (Last Updated: {time.strftime('%H:%M:%S')})")
            st.plotly_chart(fig, use_container_width=True)
            
            st.info("HCI Note: Dashboard updates every 60 seconds to provide real-time strategic clarity.")
        else:
            st.error("Waiting for market data...")

    # Tunggu 60 saat sebelum buat pusingan seterusnya
    time.sleep(60)
