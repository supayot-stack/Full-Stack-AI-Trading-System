# app.py
# ============================================================
# FULL-STACK AI TRADING SYSTEM — Main Application
# Dark Premium Bloomberg-Style Dashboard
# Phase 1: Learning Mode (Mock Data, No Real Money)
# ============================================================

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from utils.translations import TRANSLATIONS, LEARN_ANSWERS
from services.market_data import (
    get_btc_data, get_gold_data, get_macro_data,
    get_onchain_data, get_sparkline_data, format_volume
)
from components.ui_styles import (
    BLOOMBERG_CSS, header_html, asset_card_html,
    macro_card_html, comparison_table_html
)

# ── PAGE CONFIG ──────────────────────────────────────────────
st.set_page_config(
    page_title="Full-Stack AI Trading System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",  # always start expanded
)

# ── INJECT CSS ───────────────────────────────────────────────
st.markdown(BLOOMBERG_CSS, unsafe_allow_html=True)

# ── SESSION STATE ────────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "th"
if "learn_answer" not in st.session_state:
    st.session_state.learn_answer = None
if "selected_q" not in st.session_state:
    st.session_state.selected_q = None

# ── DATA ─────────────────────────────────────────────────────
lang = st.session_state.lang
t = TRANSLATIONS[lang]
btc = get_btc_data()
gold = get_gold_data()
macro = get_macro_data()
onchain = get_onchain_data()
timestamp = datetime.now().strftime("%d %b %Y  %H:%M:%S")

# ── HEADER ───────────────────────────────────────────────────
st.markdown(header_html(t, lang, timestamp), unsafe_allow_html=True)



# ── SIDEBAR ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style="padding:16px 8px 8px; border-bottom:1px solid rgba(201,168,76,0.1); margin-bottom:16px;">
        <div style="font-size:9px; letter-spacing:3px; color:#5C5040; text-transform:uppercase; margin-bottom:8px;">LANGUAGE / ภาษา</div>
    </div>
    """, unsafe_allow_html=True)

    lang_choice = st.radio("", ["🇹🇭  ภาษาไทย", "🇺🇸  English"], label_visibility="collapsed")
    st.session_state.lang = "th" if "ไทย" in lang_choice else "en"
    lang = st.session_state.lang
    t = TRANSLATIONS[lang]

    st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="border-top:1px solid rgba(201,168,76,0.1); padding-top:16px;">
        <div style="font-size:9px; letter-spacing:3px; color:#5C5040; text-transform:uppercase; margin-bottom:16px;">NAVIGATION</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "",
        [t["nav_dashboard"], t["nav_signals"], t["nav_portfolio"], t["nav_learn"]],
        label_visibility="collapsed"
    )

    st.markdown('<div style="height:32px;"></div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="border-top:1px solid rgba(201,168,76,0.08); padding-top:16px;">
        <div style="font-size:9px; letter-spacing:2px; color:#3D2D0A; text-transform:uppercase; margin-bottom:8px;">SYSTEM STATUS</div>
        <div style="font-size:10px; color:#3D3020;">
            <span class="pulse-dot" style="width:6px;height:6px;"></span> LIVE FEED ACTIVE<br>
            <span style="margin-left:14px; color:#3D2D0A;">Phase 1 — Mock Data</span>
        </div>
    </div>
    <div style="margin-top:16px; font-size:9px; color:#3D2D0A; line-height:1.6;">
        {t['disclaimer']}
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# PAGE: DASHBOARD
# ═══════════════════════════════════════════════════════════
if t["nav_dashboard"] in page:
    st.markdown('<div style="padding:24px 28px 0;">', unsafe_allow_html=True)

    # ── MACRO ROW ──
    st.markdown(f'<div class="section-label">{t["macro_title"]}</div>', unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(macro_card_html(t["dxy_label"], str(macro.dxy), macro.dxy_trend, "negative"), unsafe_allow_html=True)
    with m2:
        st.markdown(macro_card_html(t["fed_label"], macro.fed_rate, macro.fed_trend, "neutral"), unsafe_allow_html=True)
    with m3:
        st.markdown(macro_card_html(t["cpi_label"], macro.cpi, macro.cpi_trend, "watch"), unsafe_allow_html=True)
    with m4:
        st.markdown(macro_card_html(t["geo_label"], macro.geo_risk, "IRAN/ISRAEL WAR", "negative"), unsafe_allow_html=True)

    st.markdown('<div style="height:24px;"></div>', unsafe_allow_html=True)

    # ── ASSET CARDS + CHARTS ──
    st.markdown(f'<div class="section-label">{t["market_overview"]}</div>', unsafe_allow_html=True)

    signal_map = {
        "buy": t["signal_buy"],
        "wait": t["signal_wait"],
        "sell": t["signal_sell"]
    }

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(asset_card_html(btc, signal_map[btc.signal], t, "blue"), unsafe_allow_html=True)
        # BTC Sparkline
        btc_spark = get_sparkline_data(btc.price, 60, 0.025)
        fig_btc = go.Figure()
        fig_btc.add_trace(go.Scatter(
            y=btc_spark, mode='lines',
            line=dict(color='#6699FF', width=1.5),
            fill='tozeroy',
            fillcolor='rgba(102,153,255,0.06)',
            hovertemplate='$%{y:,.0f}<extra></extra>'
        ))
        fig_btc.update_layout(
            height=80, margin=dict(l=0, r=0, t=4, b=0),
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False, xaxis=dict(visible=False), yaxis=dict(visible=False)
        )
        st.plotly_chart(fig_btc, use_container_width=True, config={"displayModeBar": False})

    with col2:
        st.markdown(asset_card_html(gold, signal_map[gold.signal], t, "gold"), unsafe_allow_html=True)
        # Gold Sparkline
        gold_spark = get_sparkline_data(gold.price, 60, 0.012)
        fig_gold = go.Figure()
        fig_gold.add_trace(go.Scatter(
            y=gold_spark, mode='lines',
            line=dict(color='#C9A84C', width=1.5),
            fill='tozeroy',
            fillcolor='rgba(201,168,76,0.06)',
            hovertemplate='$%{y:,.0f}<extra></extra>'
        ))
        fig_gold.update_layout(
            height=80, margin=dict(l=0, r=0, t=4, b=0),
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False, xaxis=dict(visible=False), yaxis=dict(visible=False)
        )
        st.plotly_chart(fig_gold, use_container_width=True, config={"displayModeBar": False})

    st.markdown('<div style="height:24px;"></div>', unsafe_allow_html=True)

    # ── ON-CHAIN ──
    st.markdown(f'<div class="section-label">{t["onchain_title"]}</div>', unsafe_allow_html=True)
    oc1, oc2, oc3, oc4 = st.columns(4)

    with oc1:
        st.markdown(f"""
        <div class="onchain-card">
            <div class="macro-label">🐋 {t['whale_flow']}</div>
            <div style="font-size:16px; font-weight:700; color:#C9A84C; margin:6px 0;">{t['accumulating']}</div>
            <div style="font-size:10px; color:#5C5040;">Deposit -18% MoM</div>
        </div>
        """, unsafe_allow_html=True)

    with oc2:
        st.markdown(f"""
        <div class="onchain-card">
            <div class="macro-label">📤 {t['exchange_flow']}</div>
            <div style="font-size:16px; font-weight:700; color:#00C853; margin:6px 0;">{t['outflow']}</div>
            <div style="font-size:10px; color:#5C5040;">32,000 BTC ออก</div>
        </div>
        """, unsafe_allow_html=True)

    with oc3:
        st.markdown(f"""
        <div class="onchain-card" style="text-align:center;">
            <div class="macro-label">😱 {t['fear_greed']}</div>
            <div class="fear-number">{onchain.fear_greed}</div>
            <div class="fear-label">{t['extreme_fear']}</div>
        </div>
        """, unsafe_allow_html=True)

    with oc4:
        # Fear & Greed Gauge
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=onchain.fear_greed,
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [0, 100], 'tickcolor': '#3D3020', 'tickfont': {'size': 8, 'color': '#3D3020'}},
                'bar': {'color': '#FF3D3D', 'thickness': 0.3},
                'bgcolor': '#0A0C12',
                'borderwidth': 0,
                'steps': [
                    {'range': [0, 25], 'color': 'rgba(255,61,61,0.15)'},
                    {'range': [25, 50], 'color': 'rgba(255,179,0,0.1)'},
                    {'range': [50, 75], 'color': 'rgba(201,168,76,0.08)'},
                    {'range': [75, 100], 'color': 'rgba(0,200,83,0.12)'},
                ],
                'threshold': {'line': {'color': '#C9A84C', 'width': 1}, 'thickness': 0.75, 'value': onchain.fear_greed}
            },
            number={'font': {'color': '#FF3D3D', 'size': 28, 'family': 'IBM Plex Mono'}}
        ))
        fig_gauge.update_layout(
            height=120, margin=dict(l=10, r=10, t=10, b=0),
            paper_bgcolor='rgba(0,0,0,0)', font={'color': '#5C5040'}
        )
        st.plotly_chart(fig_gauge, use_container_width=True, config={"displayModeBar": False})

    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# PAGE: AI SIGNALS
# ═══════════════════════════════════════════════════════════
elif t["nav_signals"] in page:
    st.markdown('<div style="padding:24px 28px 0;">', unsafe_allow_html=True)

    reasons_key = "reasons_th" if lang == "th" else "reasons_en"
    risks_key = "risks_th" if lang == "th" else "risks_en"
    short_key = "short_term_th" if lang == "th" else "short_term_en"
    mid_key = "mid_term_th" if lang == "th" else "mid_term_en"

    col1, col2 = st.columns(2)

    with col1:
        reasons = getattr(btc, reasons_key)
        risks = getattr(btc, risks_key)
        reasons_html = "".join(f'<div class="reason-item"><span class="reason-dot">▸</span>{r}</div>' for r in reasons)
        risks_html = "".join(f'<div class="risk-item">⚠ {r}</div>' for r in risks)
        st.markdown(f"""
        <div class="bberg-card">
            <div class="section-label gold-label">₿ BITCOIN — BTC/USD</div>
            <div style="margin-bottom:16px;">
                <span class="signal-{btc.signal}" style="margin-right:8px;">
                    {TRANSLATIONS[lang]['signal_' + btc.signal]}
                </span>
                <span style="font-size:11px; color:#5C5040; font-family:'IBM Plex Mono',monospace;">
                    CONFIDENCE: {btc.confidence}%
                </span>
            </div>
            <div style="font-size:9px; letter-spacing:2px; color:#5C5040; text-transform:uppercase; margin-bottom:10px;">
                💡 {t['why_title']}
            </div>
            {reasons_html}
            <div style="height:16px;"></div>
            <div style="font-size:9px; letter-spacing:2px; color:#FF3D3D; text-transform:uppercase; margin-bottom:8px;">
                ⚠ {t['risk_title']}
            </div>
            {risks_html}
            <div class="crosshair-h"></div>
            <div style="font-size:9px; color:#5C5040; letter-spacing:1px; text-transform:uppercase; margin-bottom:6px;">{t['short_term']}</div>
            <div style="font-size:12px; color:#A89880; font-family:'IBM Plex Sans Thai',sans-serif; margin-bottom:12px;">{getattr(btc, short_key)}</div>
            <div style="font-size:9px; color:#5C5040; letter-spacing:1px; text-transform:uppercase; margin-bottom:6px;">{t['mid_term']}</div>
            <div style="font-size:12px; color:#A89880; font-family:'IBM Plex Sans Thai',sans-serif;">{getattr(btc, mid_key)}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        reasons = getattr(gold, reasons_key)
        risks = getattr(gold, risks_key)
        reasons_html = "".join(f'<div class="reason-item"><span class="reason-dot">▸</span>{r}</div>' for r in reasons)
        risks_html = "".join(f'<div class="risk-item">⚠ {r}</div>' for r in risks)
        st.markdown(f"""
        <div class="bberg-card bberg-card-gold">
            <div class="section-label gold-label">◈ GOLD — XAU/USD</div>
            <div style="margin-bottom:16px;">
                <span class="signal-{gold.signal}" style="margin-right:8px;">
                    {TRANSLATIONS[lang]['signal_' + gold.signal]}
                </span>
                <span style="font-size:11px; color:#5C5040; font-family:'IBM Plex Mono',monospace;">
                    CONFIDENCE: {gold.confidence}%
                </span>
            </div>
            <div style="font-size:9px; letter-spacing:2px; color:#5C5040; text-transform:uppercase; margin-bottom:10px;">
                💡 {t['why_title']}
            </div>
            {reasons_html}
            <div style="height:16px;"></div>
            <div style="font-size:9px; letter-spacing:2px; color:#FF3D3D; text-transform:uppercase; margin-bottom:8px;">
                ⚠ {t['risk_title']}
            </div>
            {risks_html}
            <div class="crosshair-h"></div>
            <div style="font-size:9px; color:#5C5040; letter-spacing:1px; text-transform:uppercase; margin-bottom:6px;">{t['short_term']}</div>
            <div style="font-size:12px; color:#A89880; font-family:'IBM Plex Sans Thai',sans-serif; margin-bottom:12px;">{getattr(gold, short_key)}</div>
            <div style="font-size:9px; color:#5C5040; letter-spacing:1px; text-transform:uppercase; margin-bottom:6px;">{t['mid_term']}</div>
            <div style="font-size:12px; color:#A89880; font-family:'IBM Plex Sans Thai',sans-serif;">{getattr(gold, mid_key)}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div style="height:24px;"></div>', unsafe_allow_html=True)

    # ── COMPARISON TABLE ──
    st.markdown(f'<div class="section-label">⚖ COMPARISON MATRIX</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="bberg-card">{comparison_table_html(lang)}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# PAGE: PAPER PORTFOLIO
# ═══════════════════════════════════════════════════════════
elif t["nav_portfolio"] in page:
    st.markdown('<div style="padding:24px 28px 0;">', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="paper-card" style="margin-bottom:24px;">
        <div class="section-label" style="color:#00C853;">◈ {t['paper_title']}</div>
        <div style="font-size:11px; color:#5C5040; margin-bottom:20px; font-family:'IBM Plex Sans Thai',sans-serif;">{t['paper_desc']}</div>
        <div class="stat-row">
            <div class="stat-item">
                <div class="stat-label">{t['paper_balance']}</div>
                <div class="stat-value stat-value-gold">฿100,000</div>
            </div>
            <div class="stat-item">
                <div class="stat-label">{t['paper_pnl']}</div>
                <div class="stat-value stat-value-green">+฿3,240 (+3.24%)</div>
            </div>
            <div class="stat-item">
                <div class="stat-label">POSITIONS</div>
                <div class="stat-value" style="color:#A89880;">2 OPEN</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        # Portfolio Donut
        st.markdown(f'<div class="section-label">{t["allocation"]}</div>', unsafe_allow_html=True)
        fig_pie = go.Figure(go.Pie(
            labels=["BTC", "GOLD", t["cash"]],
            values=[15, 25, 60],
            hole=0.65,
            marker=dict(colors=['#6699FF', '#C9A84C', '#3D3020'], line=dict(color='#050608', width=2)),
            textfont=dict(family='IBM Plex Mono', size=11, color='#A89880'),
            textposition='outside',
        ))
        fig_pie.update_layout(
            height=280, margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            showlegend=True,
            legend=dict(font=dict(color='#5C5040', size=10, family='IBM Plex Mono'), bgcolor='rgba(0,0,0,0)'),
            annotations=[dict(text='PORT', x=0.5, y=0.5, font=dict(size=12, color='#5C5040', family='IBM Plex Mono'), showarrow=False)]
        )
        st.plotly_chart(fig_pie, use_container_width=True, config={"displayModeBar": False})

    with col2:
        # P&L Chart
        st.markdown(f'<div class="section-label">SIMULATED P&L — 30 DAYS</div>', unsafe_allow_html=True)
        import random
        random.seed(42)
        pnl_data = [100000]
        for _ in range(29):
            pnl_data.append(pnl_data[-1] * (1 + random.gauss(0.002, 0.015)))

        fig_pnl = go.Figure()
        fig_pnl.add_trace(go.Scatter(
            y=pnl_data,
            mode='lines',
            line=dict(color='#00C853', width=2),
            fill='tozeroy',
            fillcolor='rgba(0,200,83,0.05)',
        ))
        fig_pnl.update_layout(
            height=280, margin=dict(l=0, r=0, t=8, b=0),
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False,
            xaxis=dict(visible=False),
            yaxis=dict(tickfont=dict(size=9, color='#3D3020', family='IBM Plex Mono'), gridcolor='rgba(201,168,76,0.05)', tickformat='$,.0f')
        )
        st.plotly_chart(fig_pnl, use_container_width=True, config={"displayModeBar": False})

    # ── POSITIONS TABLE ──
    st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">OPEN POSITIONS</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="bberg-card">
        <table class="bloomberg-table">
            <thead>
                <tr><th>ASSET</th><th>ENTRY</th><th>CURRENT</th><th>SIZE</th><th>P&L</th><th>STATUS</th></tr>
            </thead>
            <tbody>
                <tr>
                    <td class="td-gold">XAU/USD</td>
                    <td style="color:#5C5040;">$5,080</td>
                    <td class="td-gold">$5,145</td>
                    <td style="color:#A89880;">฿25,000</td>
                    <td class="ticker-up">+฿319 (+1.28%)</td>
                    <td><span class="signal-buy">HOLD</span></td>
                </tr>
                <tr>
                    <td class="td-btc">BTC/USD</td>
                    <td style="color:#5C5040;">$68,200</td>
                    <td class="td-btc">$70,760</td>
                    <td style="color:#A89880;">฿15,000</td>
                    <td class="ticker-up">+฿563 (+3.75%)</td>
                    <td><span class="signal-wait">WATCH</span></td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# PAGE: LEARN
# ═══════════════════════════════════════════════════════════
elif t["nav_learn"] in page:
    st.markdown('<div style="padding:24px 28px 0;">', unsafe_allow_html=True)
    st.markdown(f'<div class="section-label gold-label">🎓 {t["learn_title"]}</div>', unsafe_allow_html=True)

    questions = [t[f"learn_q{i}"] for i in range(1, 7)]
    answers = LEARN_ANSWERS[lang]

    cols = st.columns(2)
    for i, q in enumerate(questions):
        with cols[i % 2]:
            if st.button(f"❯  {q}", key=f"q_{i}", use_container_width=True):
                st.session_state.learn_answer = answers.get(q, "")
                st.session_state.selected_q = q

    if st.session_state.learn_answer:
        st.markdown(f"""
        <div style="font-size:9px; letter-spacing:2px; color:#C9A84C; text-transform:uppercase; margin-bottom:8px; margin-top:16px;">
            🤖 AI GUARDIAN — {st.session_state.selected_q}
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f'<div class="answer-box">', unsafe_allow_html=True)
        st.markdown(st.session_state.learn_answer)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="height:24px;"></div>', unsafe_allow_html=True)

    # ── KEY CONCEPTS ──
    st.markdown(f'<div class="section-label">{t["key_concepts"]}</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    concepts = [
        ("📉", "RSI", "วัดว่าสินทรัพย์แพงหรือถูกเกินไป\n0-30 = ถูก | 70-100 = แพง" if lang == "th" else "Measures overbought/oversold\n0-30 = Cheap | 70-100 = Expensive"),
        ("🐋", "WHALE", "นักลงทุนรายใหญ่ที่มีพลังขยับตลาดได้\nWale ออก Exchange = สัญญาณบวก" if lang == "th" else "Large holders who can move markets\nWhale leaves exchange = Bullish"),
        ("💰", "DXY", "ดัชนีความแข็งของดอลลาร์\nDXY ขึ้น = Gold/BTC มักลง" if lang == "th" else "US Dollar strength index\nDXY rises = Gold/BTC often falls"),
        ("🏦", "CENTRAL BANK", "ธนาคารกลางซื้อทอง ~755 ตัน/ปี\nสร้าง Structural Demand ระยะยาว" if lang == "th" else "Central banks buying ~755 tons/year\nCreates long-term structural demand"),
        ("😱", "FEAR & GREED", "วัด Sentiment ตลาด 0-100\n< 25 = กลัวมาก = โอกาสซื้อ" if lang == "th" else "Market sentiment index 0-100\n< 25 = Extreme Fear = Buy zone"),
        ("📊", "CORRELATION", "วัดว่า 2 สินทรัพย์เดินตามกันแค่ไหน\nBTC+Gold ปัจจุบัน: 0.18 (ต่าง)" if lang == "th" else "Measures how 2 assets move together\nBTC+Gold currently: 0.18 (diverging)"),
    ]
    for i, (icon, title, desc) in enumerate(concepts):
        with [c1, c2, c3][i % 3]:
            st.markdown(f"""
            <div class="concept-card" style="margin-bottom:12px;">
                <div class="concept-icon">{icon}</div>
                <div class="concept-title">{title}</div>
                <div class="concept-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
