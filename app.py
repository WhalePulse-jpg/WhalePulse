import streamlit as st
import yfinance as yf
import time
import pandas as pd
import numpy as np
import random

st.set_page_config(page_title="WhalePulse AI | Elite Access", layout="wide")

# --- CSS PRO (LOOK 0.1%) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [data-testid="stAppViewContainer"] { background-color: #010208 !important; font-family: 'Inter', sans-serif; color: white; }
    .nav-container { display: flex; justify-content: space-between; align-items: center; padding: 12px 35px; background: rgba(255,255,255,0.03); border-radius: 50px; border: 1px solid rgba(0, 209, 255, 0.15); margin-bottom: 30px; }
    @keyframes pulse-blue { 0% { box-shadow: 0 0 0 0 rgba(0, 209, 255, 0.7); } 70% { box-shadow: 0 0 0 10px rgba(0, 209, 255, 0); } 100% { box-shadow: 0 0 0 0 rgba(0, 209, 255, 0); } }
    .wallet-btn { border: 1px solid #00d1ff; padding: 6px 20px; border-radius: 25px; color: #00d1ff; font-size: 11px; font-weight: bold; animation: pulse-blue 2s infinite; background: transparent; }
    .hero-title { font-size: 80px !important; font-weight: 900; line-height: 0.85; text-shadow: 0 0 30px rgba(0, 209, 255, 0.4); }
    .alert-card { background: linear-gradient(180deg, rgba(255, 0, 0, 0.15) 0%, rgba(0, 0, 0, 0.9) 100%); border: 1px solid rgba(255, 50, 50, 0.4); border-radius: 18px; padding: 25px; text-align: center; }
    .sentiment-badge { padding: 2px 8px; border-radius: 10px; font-size: 9px; font-weight: bold; margin-left: 5px; vertical-align: middle; }
    .ticker-bar { position: fixed; bottom: 0; left: 0; width: 100%; background: #000; border-top: 1px solid #00d1ff; padding: 15px; color: #00d1ff; font-family: monospace; z-index: 1000; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTEUR DE DONNÉES ---
@st.cache_data(ttl=2)
def get_wealth():
    targets = {
        "Elon Musk": {"ticker": "TSLA", "shares": 411000000},
        "Jeff Bezos": {"ticker": "AMZN", "shares": 930000000},
        "Bernard Arnault": {"ticker": "MC.PA", "shares": 233000000},
        "Mark Zuckerberg": {"ticker": "META", "shares": 350000000},
        "CZ Binance": {"ticker": "BNB-USD", "shares": 65000000}
    }
    results = {}
    for name, info in targets.items():
        try:
            stock = yf.Ticker(info["ticker"])
            price = stock.fast_info['last_price']
            # On simule un sentiment AI basé sur le dernier chiffre du prix (pour le fun)
            sentiment = "🟢 BULLISH" if price % 2 == 0 else "🔴 BEARISH"
            results[name] = {"price": price, "total": price * info["shares"], "sentiment": sentiment}
        except:
            results[name] = {"price": 0, "total": 0, "sentiment": "⚪ NEUTRAL"}
    return results

@st.cache_data(ttl=60)
def get_crypto_history(ticker="BTC-USD"):
    try:
        df = yf.download(ticker, period="1d", interval="15m", progress=False)
        return df['Close']
    except:
        return pd.DataFrame(np.random.randn(20, 1))

data = get_wealth()
btc_price_history = get_crypto_history()

# --- ALERTES IA ---
alerts = ["BTC VOLATILITY DETECTED", "ELON MUSK SENTIMENT: STABLE", "UNUSUAL WHALE ACTIVITY ON META"]
current_alert = random.choice(alerts)

# --- NAVIGATION ---
st.markdown(f'<div class="nav-container"><div style="font-weight: 900; color: #00d1ff; font-size: 22px;">📈 WhalePulse.ai</div><div class="wallet-btn">CONNECT WALLET</div></div>', unsafe_allow_html=True)

col_left, col_mid, col_right = st.columns([1.6, 2, 1.2])

with col_left:
    st.markdown('<p class="hero-title">FEEL THE<br>RHYTHM OF<br>THE 0.1%.</p>', unsafe_allow_html=True)
    st.write("Real-time Billionaire Wealth Tracking with AI Sentiment Analysis.")

with col_mid:
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1000&auto=format&fit=crop", use_container_width=True)

with col_right:
    st.markdown(f'<div class="alert-card"><p style="color:#ff3232; font-size:12px; font-weight:bold;">● AI PULSE ALERT</p><p style="font-size:11px; color:white;">{current_alert}</p>', unsafe_allow_html=True)
    st.line_chart(btc_price_history, height=120, use_container_width=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/ed/Elon_Musk_Royal_Society.jpg", width=150)
    
    # --- AJOUT DU SENTIMENT DANS LA METRIC ---
    sentiment_color = "#00ff00" if "BULLISH" in data['Elon Musk']['sentiment'] else "#ff3232"
    st.markdown(f'<p style="font-size:12px; margin-bottom:0px;">SENTIMENT: <span style="color:{sentiment_color}; font-weight:bold;">{data["Elon Musk"]["sentiment"]}</span></p>', unsafe_allow_html=True)
    st.metric("ELON MUSK", f"{data['Elon Musk']['total']:,.0f} $", "-$3.2B", delta_color="inverse")
    st.button("ENTER THE TERMINAL", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- TICKER DYNAMIQUE AVEC SENTIMENT ---
ticker_html = '<div class="ticker-bar">'
for name, info in data.items():
    color = "#00ff00" if "BULLISH" in info['sentiment'] else "#ff3232"
    ticker_html += f' || {name.upper()}: {info["price"]:.2f}$ <span style="color:{color}; font-size:10px;">[{info["sentiment"]}]</span>'
ticker_html += ' || WHALEPULSE AI CONNECTED...</div>'
st.markdown(ticker_html, unsafe_allow_html=True)

time.sleep(5)
st.rerun()