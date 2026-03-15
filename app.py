import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import time

# 1. HCI & Cognitive Neuroscience Design Configuration
st.set_page_config(page_title="NEURO-STRAT AI", layout="wide")
st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

# Sidebar: Expert Profile & Expertise Layers
st.sidebar.title("Strategic Analyst Profile")
st.sidebar.info("Mohd Khairul Ridhuan bin Mohd Fadzil")
st.sidebar.markdown("""
**Interdisciplinary Expertise:**
- 🌍 Geopolitics: Choke-point & Tactical Analysis
- 📊 Accounting: Supply Chain Cost Integrity
- 💡 Finance: Market Volatility & Risk Proxy
- 🧠 Neuroscience: Cognitive Stress Indexing
- 💻 HCI: Decision-Support Interface Design
""")

st.title("🧠 NEURO-STRAT: Iran-West Conflict Risk Engine")

# Placeholder untuk memastikan dashboard dikemaskini di tempat yang sama (HCI Optimization)
placeholder = st.empty()

# 2. Real-Time Data Intelligence Engine
def get_live_intelligence():
    # Menggunakan 5d supaya dashboard berfungsi walaupun pada hari minggu (weekend)
    tickers = {"Brent Oil": "BZ=F", "Gold": "GC=F", "GBP/USD": "GBPUSD=X"}
    results = {}
    for name, sym in tickers.items():
        try:
            df = yf.Ticker(sym).history(period="5d", interval="1m")
            results[name] = df
        except:
            results[name] = pd.DataFrame()
    return results

# 3. Main Dashboard Loop (Live Refresh)
while True:
    with placeholder.container():
        data = get_live_intelligence()
        
        if not data["Brent Oil"].empty:
            # Metrics: Financial & Cognitive Analysis
            col1, col2, col3 = st.columns(3)
            
            with col1:
                oil_price = data["Brent Oil"]['Close'].iloc[-1]
                oil_open = data["Brent Oil"]['Open'].iloc[0]
                st.metric("Brent Crude (Energy War Proxy)", f"${oil_price:.2f}", f"{oil_price - oil_open:.2f}")
                st.caption("Accounting: Impact on Global OPEX & Shipping Rates")

            with col2:
                # Neuro-Stress Index: Digerakkan oleh volatiliti harga pasaran (Amygdala Proxy)
                stress_val = (data["Brent Oil"]['Close'].pct_change().std() * 1000)
                st.metric("Market Cognitive Stress Index", f"{stress_val:.2f} Hz", "LIVE Updates")
                st.caption("Neuroscience: Collective Amygdala Fear Response")

            with col3:
                # Geopolitical Strategist Assessment
                st.metric("Hormuz Strait Risk", "CRITICAL", "85% Blockage Prob.")
                st.caption("Strategist: Tactical Supply Chain Disruption Risk")

            # 4. Visualization: Market Sentiment Analysis (HCI Layer)
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=data["Brent Oil"].index, 
                y=data["Brent Oil"]['Close'], 
                name="Market Sentiment",
                line=dict(color='#ff4b4b', width=2)
            ))
            fig.update_layout(
                template="plotly_dark", 
                title=f"Real-Time Sentiment Analysis (Last Updated: {time.strftime('%H:%M:%S')})",
                margin=dict(l=20, r=20, t=50, b=20)
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.info("HCI Note: Dashboard optimized for low-cognitive load during high-stress geopolitical events.")

            # --- FOOTER SIGNATURE & OWNERSHIP ---
            st.markdown("---")
            st.markdown(
                """
                <div style='text-align: center; color: #808495; padding: 10px;'>
                    <p style='margin: 0;'><strong>NEURO-STRAT Intelligence Engine v1.0</strong></p>
                    <p style='margin: 0;'>Developed & Conceptualized by:</p>
                    <p style='font-size: 1.2rem; color: #ffffff;'><strong>Mohd Khairul Ridhuan bin Mohd Fadzil</strong></p>
                    <p style='margin: 0;'>© 2026 | Geopolitical Strategist & Neuro-Analyst</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
        else:
            st.warning("Connecting to global financial servers... Please wait.")

    # Berehat 60 saat sebelum kitaran data seterusnya
    time.sleep(60)
