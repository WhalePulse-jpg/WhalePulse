import streamlit as st
import yfinance as yf
import time
import pandas as pd
import numpy as np

st.set_page_config(page_title="WhalePulse AI | Global Monitoring", layout="wide")

# --- CSS PRO (LOOK 0.1%) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [data-testid="stAppViewContainer"] { background-color: #010208 !important; font-family: 'Inter', sans-serif; color: white; }
    .nav-container { display: flex; justify-content: space-between; align-items: center; padding: 12px 35px; background: rgba(255,255,255,0.03); border-radius: 50px; border: 1px solid rgba(0, 209, 255, 0.15); margin-bottom: 30px; }
    .hero-title { font-size: 80px !important; font-weight: 900; line-height: 0.85; text-shadow: 0 0 30px rgba(0, 209, 255, 0.4); }
    .alert-card { background: linear-gradient(180deg, rgba(255, 0, 0, 0.15) 0%, rgba(0, 0, 0, 0.9) 100%); border: 1px solid rgba(255, 50, 50, 0.4); border-radius: 18px; padding: 25px; text-align: center; }
    .ticker-bar { position: fixed; bottom: 0; left: 0; width: 100%; background: #000; border-top: 1px solid #00d1ff; padding: 15px; color: #00d1ff; font-family: monospace; z-index: 1000; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
st.markdown("""
    <div class="nav-container">
        <div style="font-weight: 900; color: #00d1ff; font-size: 22px;">📈 WhalePulse.ai</div>
        <div style="color: #888; font-size: 11px; font-weight: bold; letter-spacing: 1.5px;">
            <span>LIVE TRACKER</span> &nbsp;&nbsp; <span>AI SENTIMENT</span> &nbsp;&nbsp; <span>PREDICTIONS</span>
        </div>
        <div style="border: 1px solid #00d1ff; padding: 6px 20px; border-radius: 25px; color: #00d1ff; font-size: 11px; font-weight: bold;">CONNECT WALLET</div>
    </div>
    """, unsafe_allow_html=True)

# --- MOTEUR DE DONNÉES ---
@st.cache_data(ttl=2)
def get_wealth():
    targets = {
        "Elon Musk": {"ticker": "TSLA", "shares": 411000000},
        "Jeff Bezos": {"ticker": "AMZN", "shares": 930000000},
        "Bernard Arnault": {"ticker": "MC.PA", "shares": 233000000}
    }
    results = {}
    for name, info in targets.items():
        stock = yf.Ticker(info["ticker"])
        price = stock.fast_info['last_price']
        results[name] = {"price": price, "total": price * info["shares"]}
    return results

data = get_wealth()

# --- LAYOUT ---
col_left, col_mid, col_right = st.columns([1.6, 2, 1.2])

with col_left:
    st.markdown('<p class="hero-title">FEEL THE<br>RHYTHM OF<br>THE 0.1%.</p>', unsafe_allow_html=True)
    st.write("Global Wealth Surveillance connected to Paris, New York, and Tokyo.")

with col_mid:
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1000&auto=format&fit=crop", use_container_width=True)

with col_right:
    st.markdown('<div class="alert-card"><p style="color:#ff3232; font-size:12px; font-weight:bold;">● AI PULSE ALERT</p>', unsafe_allow_html=True)
    st.line_chart(pd.DataFrame(np.random.randn(20, 1)), height=100, use_container_width=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/ed/Elon_Musk_Royal_Society.jpg", width=150)
    st.metric("ELON MUSK", f"{data['Elon Musk']['total']:,.0f} $", "-$3.2B Today", delta_color="inverse")
    st.button("ENTER THE TERMINAL", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- TICKER DYNAMIQUE ---
st.markdown(f"""
    <div class="ticker-bar">
        || ELON MUSK: {data['Elon Musk']['price']:.2f}$ ⚡ || 
        JEFF BEZOS: {data['Jeff Bezos']['price']:.2f}$ 📦 || 
        BERNARD ARNAULT: {data['Bernard Arnault']['price']:.2f}€ 💎 || 
        WHALEPULSE AI CONNECTED...
    </div>
    """, unsafe_allow_html=True)

time.sleep(2)
st.rerun()