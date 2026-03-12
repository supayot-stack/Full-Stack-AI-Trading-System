# components/ui_styles.py
# ============================================================
# DARK PREMIUM BLOOMBERG-STYLE UI — CSS & HTML Components
# ============================================================

BLOOMBERG_CSS = """
<style>
/* ── FONTS ── */
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500;600;700&family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&display=swap');

/* ── ROOT VARIABLES ── */
:root {
    --gold:        #C9A84C;
    --gold-dim:    #8B6914;
    --gold-glow:   rgba(201,168,76,0.15);
    --gold-light:  #E8C96A;
    --bg-0:        #050608;
    --bg-1:        #0A0C12;
    --bg-2:        #0F1219;
    --bg-3:        #141720;
    --border:      rgba(201,168,76,0.12);
    --border-bright: rgba(201,168,76,0.3);
    --text-1:      #E8E0D0;
    --text-2:      #A89880;
    --text-3:      #5C5040;
    --green:       #00C853;
    --green-dim:   rgba(0,200,83,0.12);
    --red:         #FF3D3D;
    --red-dim:     rgba(255,61,61,0.12);
    --yellow:      #FFB300;
    --yellow-dim:  rgba(255,179,0,0.12);
    --blue:        #2196F3;
    --blue-dim:    rgba(33,150,243,0.12);
    --font-mono:   'IBM Plex Mono', monospace;
    --font-th:     'IBM Plex Sans Thai', sans-serif;
}

/* ── GLOBAL RESET ── */
* { box-sizing: border-box; }

.stApp {
    background: var(--bg-0) !important;
    font-family: var(--font-mono) !important;
}

/* ── HIDE STREAMLIT CHROME ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.stDeployButton { display: none; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: var(--bg-1) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-1) !important; }

/* ── SELECTBOX & RADIO ── */
.stSelectbox label, .stRadio label { color: var(--text-2) !important; font-size: 11px !important; letter-spacing: 1px; text-transform: uppercase; }
.stSelectbox > div > div { background: var(--bg-2) !important; border: 1px solid var(--border) !important; color: var(--gold) !important; }

/* ── METRIC ── */
[data-testid="metric-container"] {
    background: var(--bg-2);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 16px !important;
}
[data-testid="metric-container"] label { color: var(--text-3) !important; font-size: 10px !important; letter-spacing: 2px; text-transform: uppercase; }
[data-testid="metric-container"] [data-testid="stMetricValue"] { color: var(--gold) !important; font-family: var(--font-mono) !important; font-size: 22px !important; font-weight: 700; }
[data-testid="metric-container"] [data-testid="stMetricDelta"] { font-size: 12px !important; }

/* ── BUTTON ── */
.stButton > button {
    background: transparent !important;
    border: 1px solid var(--border) !important;
    color: var(--text-2) !important;
    font-family: var(--font-mono) !important;
    font-size: 11px !important;
    letter-spacing: 1px;
    border-radius: 2px !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    border-color: var(--gold) !important;
    color: var(--gold) !important;
    background: var(--gold-glow) !important;
}

/* ── EXPANDER ── */
.streamlit-expanderHeader {
    background: var(--bg-2) !important;
    border: 1px solid var(--border) !important;
    color: var(--text-2) !important;
    font-size: 11px !important;
    letter-spacing: 1px;
}

/* ── DIVIDER ── */
hr { border-color: var(--border) !important; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: var(--bg-0); }
::-webkit-scrollbar-thumb { background: var(--gold-dim); border-radius: 2px; }

/* ── BLOOMBERG TICKER BAR ── */
.ticker-bar {
    background: var(--bg-1);
    border-bottom: 1px solid var(--border);
    padding: 6px 24px;
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--text-3);
    letter-spacing: 0.5px;
    overflow: hidden;
    white-space: nowrap;
}
.ticker-item { display: inline-block; margin-right: 32px; }
.ticker-up { color: var(--green); }
.ticker-down { color: var(--red); }
.ticker-neutral { color: var(--gold); }

/* ── HEADER BAR ── */
.bloomberg-header {
    background: var(--bg-1);
    border-bottom: 2px solid var(--gold-dim);
    padding: 14px 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

/* ── CARD ── */
.bberg-card {
    background: var(--bg-2);
    border: 1px solid var(--border);
    border-radius: 2px;
    padding: 20px;
    position: relative;
    overflow: hidden;
}
.bberg-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--gold-dim), transparent);
}
.bberg-card-gold {
    background: linear-gradient(135deg, rgba(201,168,76,0.05), var(--bg-2));
    border: 1px solid var(--border-bright);
}
.bberg-card-green {
    background: linear-gradient(135deg, rgba(0,200,83,0.05), var(--bg-2));
    border: 1px solid rgba(0,200,83,0.2);
}
.bberg-card-red {
    background: linear-gradient(135deg, rgba(255,61,61,0.05), var(--bg-2));
    border: 1px solid rgba(255,61,61,0.15);
}

/* ── PRICE DISPLAY ── */
.price-main {
    font-family: var(--font-mono);
    font-size: 36px;
    font-weight: 700;
    color: var(--text-1);
    letter-spacing: -1px;
    line-height: 1;
}
.price-up { color: var(--green) !important; }
.price-down { color: var(--red) !important; }
.price-change {
    font-size: 13px;
    font-weight: 600;
    margin-left: 8px;
}

/* ── SIGNAL BADGE ── */
.signal-buy {
    display: inline-block;
    padding: 4px 14px;
    background: var(--green-dim);
    border: 1px solid var(--green);
    color: var(--green);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    border-radius: 2px;
}
.signal-wait {
    display: inline-block;
    padding: 4px 14px;
    background: var(--yellow-dim);
    border: 1px solid var(--yellow);
    color: var(--yellow);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    border-radius: 2px;
}
.signal-sell {
    display: inline-block;
    padding: 4px 14px;
    background: var(--red-dim);
    border: 1px solid var(--red);
    color: var(--red);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    border-radius: 2px;
}

/* ── LABEL ── */
.section-label {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--text-3);
    margin-bottom: 12px;
    padding-bottom: 6px;
    border-bottom: 1px solid var(--border);
}
.gold-label { color: var(--gold) !important; }

/* ── PROGRESS BAR ── */
.conf-bar-wrap {
    height: 3px;
    background: var(--bg-3);
    border-radius: 1px;
    overflow: hidden;
    margin-top: 6px;
}
.conf-bar-fill-gold {
    height: 100%;
    background: linear-gradient(90deg, var(--gold-dim), var(--gold));
    border-radius: 1px;
    transition: width 1s ease;
}
.conf-bar-fill-green {
    height: 100%;
    background: linear-gradient(90deg, #007B33, var(--green));
    border-radius: 1px;
    transition: width 1s ease;
}

/* ── MACRO BADGE ── */
.macro-card {
    padding: 14px 16px;
    border-radius: 2px;
    border: 1px solid;
}
.macro-negative { background: var(--red-dim); border-color: rgba(255,61,61,0.2) !important; }
.macro-neutral  { background: var(--blue-dim); border-color: rgba(33,150,243,0.2) !important; }
.macro-watch    { background: var(--yellow-dim); border-color: rgba(255,179,0,0.2) !important; }
.macro-positive { background: var(--green-dim); border-color: rgba(0,200,83,0.2) !important; }

.macro-label { font-size: 9px; letter-spacing: 2px; text-transform: uppercase; color: var(--text-3); margin-bottom: 6px; }
.macro-value { font-size: 18px; font-weight: 700; color: var(--text-1); font-family: var(--font-mono); }
.macro-trend-neg { color: var(--red); font-size: 10px; margin-top: 3px; }
.macro-trend-neu { color: var(--blue); font-size: 10px; margin-top: 3px; }
.macro-trend-wat { color: var(--yellow); font-size: 10px; margin-top: 3px; }

/* ── ONCHAIN ── */
.onchain-card {
    background: var(--bg-2);
    border: 1px solid var(--border);
    border-radius: 2px;
    padding: 16px;
    text-align: center;
}
.fear-number {
    font-size: 52px;
    font-weight: 900;
    color: var(--red);
    line-height: 1;
    font-family: var(--font-mono);
}
.fear-label { font-size: 10px; color: var(--red); letter-spacing: 2px; text-transform: uppercase; margin-top: 4px; }

/* ── REASON LIST ── */
.reason-item {
    font-size: 12px;
    color: var(--text-2);
    padding: 8px 0;
    border-bottom: 1px solid var(--border);
    line-height: 1.6;
    font-family: var(--font-th);
}
.reason-item:last-child { border-bottom: none; }
.reason-dot { color: var(--gold); margin-right: 8px; }

.risk-item {
    font-size: 12px;
    color: #CC8800;
    padding: 6px 0;
    border-bottom: 1px solid rgba(255,179,0,0.08);
    line-height: 1.5;
    font-family: var(--font-th);
}

/* ── TABLE ── */
.bloomberg-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
}
.bloomberg-table th {
    background: var(--bg-3);
    color: var(--text-3);
    font-size: 9px;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 10px 14px;
    text-align: left;
    border-bottom: 1px solid var(--border);
}
.bloomberg-table td {
    padding: 10px 14px;
    border-bottom: 1px solid rgba(201,168,76,0.04);
    color: var(--text-2);
    font-family: var(--font-mono);
}
.bloomberg-table tr:hover td { background: rgba(201,168,76,0.03); }
.td-btc { color: #6699FF !important; }
.td-gold { color: var(--gold) !important; }

/* ── LEARN ── */
.learn-btn-card {
    background: var(--bg-2);
    border: 1px solid var(--border);
    border-radius: 2px;
    padding: 14px 16px;
    cursor: pointer;
    color: var(--text-2);
    font-size: 12px;
    font-family: var(--font-th);
    transition: all 0.2s;
    margin-bottom: 8px;
}
.learn-btn-card:hover { border-color: var(--gold); color: var(--gold); }

.answer-box {
    background: linear-gradient(135deg, rgba(201,168,76,0.04), var(--bg-2));
    border: 1px solid var(--border-bright);
    border-radius: 2px;
    padding: 20px;
    font-size: 13px;
    color: var(--text-2);
    line-height: 1.8;
    font-family: var(--font-th);
    margin-top: 12px;
}

/* ── PHASE BADGE ── */
.phase-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(201,168,76,0.08);
    border: 1px solid var(--border-bright);
    border-radius: 2px;
    padding: 8px 16px;
    font-size: 11px;
    color: var(--gold);
    letter-spacing: 1px;
}

/* ── PAPER PORTFOLIO ── */
.paper-card {
    background: linear-gradient(135deg, rgba(0,200,83,0.05), var(--bg-2));
    border: 1px solid rgba(0,200,83,0.2);
    border-radius: 2px;
    padding: 20px;
    position: relative;
}
.paper-card::before {
    content: '◆ PAPER TRADING MODE — NO REAL MONEY AT RISK';
    position: absolute;
    top: 8px; right: 12px;
    font-size: 9px;
    letter-spacing: 2px;
    color: var(--green);
    opacity: 0.6;
}

/* ── PULSE DOT ── */
.pulse-dot {
    display: inline-block;
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--green);
    margin-right: 6px;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(1.3); }
}

/* ── CROSS HAIR LINES ── */
.crosshair-h {
    border-top: 1px dashed var(--border);
    margin: 16px 0;
}

/* ── STAT ROW ── */
.stat-row { display: flex; gap: 24px; flex-wrap: wrap; }
.stat-item { }
.stat-label { font-size: 9px; color: var(--text-3); letter-spacing: 2px; text-transform: uppercase; }
.stat-value { font-size: 20px; font-weight: 700; color: var(--text-1); font-family: var(--font-mono); margin-top: 2px; }
.stat-value-green { color: var(--green) !important; }
.stat-value-gold { color: var(--gold) !important; }

/* ── CONCEPT CARD ── */
.concept-card {
    background: var(--bg-2);
    border: 1px solid var(--border);
    border-radius: 2px;
    padding: 16px;
}
.concept-icon { font-size: 22px; margin-bottom: 8px; }
.concept-title { font-size: 13px; font-weight: 700; color: var(--gold); margin-bottom: 6px; }
.concept-desc { font-size: 11px; color: var(--text-3); line-height: 1.6; font-family: var(--font-th); }

/* ── TICKER MARQUEE ── */
@keyframes marquee {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}
.marquee-track { animation: marquee 30s linear infinite; display: inline-block; white-space: nowrap; }
.marquee-track:hover { animation-play-state: paused; }

</style>
"""


def header_html(t: dict, lang: str, timestamp: str) -> str:
    return f"""
<div style="background:#0A0C12; border-bottom:2px solid #3D2D0A; padding:0; margin-bottom:0;">
    <!-- TICKER BAR -->
    <div style="background:#070809; border-bottom:1px solid rgba(201,168,76,0.1); padding:5px 24px; overflow:hidden;">
        <div class="marquee-track">
            <span class="ticker-item" style="font-size:10px; font-family:'IBM Plex Mono',monospace; color:#5C5040; letter-spacing:0.5px;">
                <span class="ticker-neutral">BTC/USD</span> <span class="ticker-up">$70,760 ▲2.34%</span> &nbsp;│&nbsp;
                <span class="ticker-neutral">XAU/USD</span> <span class="ticker-down">$5,145 ▼0.87%</span> &nbsp;│&nbsp;
                <span class="ticker-neutral">DXY</span> <span class="ticker-up">98.9 ▲0.3%</span> &nbsp;│&nbsp;
                <span class="ticker-neutral">FED RATE</span> <span style="color:#A89880;">3.625%</span> &nbsp;│&nbsp;
                <span class="ticker-neutral">CPI</span> <span class="ticker-down">2.4% ⚠</span> &nbsp;│&nbsp;
                <span class="ticker-neutral">FEAR&GREED</span> <span class="ticker-down">13 — EXTREME FEAR</span> &nbsp;│&nbsp;
                <span class="ticker-neutral">BTC/USD</span> <span class="ticker-up">$70,760 ▲2.34%</span> &nbsp;│&nbsp;
                <span class="ticker-neutral">XAU/USD</span> <span class="ticker-down">$5,145 ▼0.87%</span> &nbsp;│&nbsp;
                <span class="ticker-neutral">DXY</span> <span class="ticker-up">98.9 ▲0.3%</span> &nbsp;│&nbsp;
                <span class="ticker-neutral">FED RATE</span> <span style="color:#A89880;">3.625%</span> &nbsp;│&nbsp;
                <span class="ticker-neutral">GEOPOLITICAL RISK</span> <span class="ticker-down">HIGH — MIDDLE EAST</span>
            </span>
        </div>
    </div>
    <!-- MAIN HEADER -->
    <div style="padding:16px 28px; display:flex; align-items:center; justify-content:space-between;">
        <div style="display:flex; align-items:center; gap:16px;">
            <div style="width:36px; height:36px; background:linear-gradient(135deg,#C9A84C,#8B6914); display:flex; align-items:center; justify-content:center; font-size:18px;">🛡</div>
            <div>
                <div style="font-family:'IBM Plex Mono',monospace; font-size:16px; font-weight:700; color:#E8E0D0; letter-spacing:3px;">FULL-STACK AI TRADING SYSTEM</div>
                <div style="font-size:9px; color:#5C5040; letter-spacing:2px; text-transform:uppercase;">{t.get('app_subtitle','')}</div>
            </div>
        </div>
        <div style="text-align:right;">
            <div class="phase-badge">{t.get('phase_badge','')}</div>
            <div style="font-size:9px; color:#3D3020; margin-top:6px; letter-spacing:1px;">
                <span class="pulse-dot"></span>{t.get('last_update','')}: {timestamp}
            </div>
        </div>
    </div>
</div>
"""


def asset_card_html(asset, signal_label: str, t: dict, color: str = "gold") -> str:
    change_color = "#00C853" if asset.change_24h >= 0 else "#FF3D3D"
    change_arrow = "▲" if asset.change_24h >= 0 else "▼"
    signal_class = f"signal-{asset.signal}"
    bar_class = "conf-bar-fill-gold" if color == "gold" else "conf-bar-fill-green"
    card_class = "bberg-card-gold" if color == "gold" else "bberg-card"

    return f"""
<div class="bberg-card {card_class}">
    <div class="section-label gold-label">{'₿ BTC/USD' if asset.symbol == 'BTC' else '◈ XAU/USD'}</div>
    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px;">
        <div>
            <div class="price-main">${asset.price:,.0f}</div>
            <div style="margin-top:4px;">
                <span class="price-change" style="color:{change_color};">{change_arrow} {abs(asset.change_24h):.2f}%</span>
                <span style="font-size:10px; color:#3D3020; margin-left:8px;">24H</span>
            </div>
        </div>
        <div style="text-align:right;">
            <span class="{signal_class}">{signal_label}</span>
        </div>
    </div>
    <div class="crosshair-h"></div>
    <div style="display:flex; gap:20px; margin-bottom:12px; flex-wrap:wrap;">
        <div><div class="stat-label">{t.get('support','S')}</div><div style="font-size:13px; color:#A89880; font-family:'IBM Plex Mono',monospace;">${asset.support:,.0f}</div></div>
        <div><div class="stat-label">{t.get('resistance','R')}</div><div style="font-size:13px; color:#A89880; font-family:'IBM Plex Mono',monospace;">${asset.resistance:,.0f}</div></div>
        <div><div class="stat-label">{t.get('rsi_label','RSI')}</div><div style="font-size:13px; color:#A89880; font-family:'IBM Plex Mono',monospace;">{asset.rsi:.1f}</div></div>
    </div>
    <div>
        <div style="display:flex; justify-content:space-between; font-size:9px; color:#3D3020; letter-spacing:1px; text-transform:uppercase; margin-bottom:4px;">
            <span>{t.get('ai_confidence','AI Confidence')}</span>
            <span style="color:#C9A84C; font-weight:700;">{asset.confidence}%</span>
        </div>
        <div class="conf-bar-wrap"><div class="{bar_class}" style="width:{asset.confidence}%;"></div></div>
    </div>
</div>
"""


def macro_card_html(label: str, value: str, trend: str, impact: str) -> str:
    cls_map = {"negative": "macro-negative", "neutral": "macro-neutral", "watch": "macro-watch", "positive": "macro-positive"}
    trend_cls = {"negative": "macro-trend-neg", "neutral": "macro-trend-neu", "watch": "macro-trend-wat", "positive": "macro-trend-neu"}
    return f"""
<div class="macro-card {cls_map.get(impact, 'macro-neutral')}">
    <div class="macro-label">{label}</div>
    <div class="macro-value">{value}</div>
    <div class="{trend_cls.get(impact, 'macro-trend-neu')}">{trend}</div>
</div>
"""


def comparison_table_html(lang: str) -> str:
    rows = [
        ("Price", "$70,760", "$5,145"),
        ("Signal", "🟡 WAIT", "🟢 ACCUMULATE"),
        ("AI Confidence", "68%", "74%"),
        ("RSI (Daily)", "47.25 — NEUTRAL", "53.0 — BULLISH"),
        ("Volatility", "🔴 VERY HIGH", "🟡 MEDIUM"),
        ("From ATH", "-33%", "-8%"),
        ("Risk Profile", "HIGH RISK", "MEDIUM RISK"),
        ("Time Horizon", "TACTICAL", "STRATEGIC"),
        ("JPM Target", "$78K-$80K", "$6,300"),
    ]
    rows_html = "".join(
        f'<tr><td style="color:#5C5040;">{r[0]}</td>'
        f'<td class="td-btc">{r[1]}</td>'
        f'<td class="td-gold">{r[2]}</td></tr>'
        for r in rows
    )
    return f"""
<table class="bloomberg-table">
    <thead>
        <tr>
            <th>INDICATOR</th>
            <th>₿ BTC / USD</th>
            <th>◈ XAU / USD</th>
        </tr>
    </thead>
    <tbody>{rows_html}</tbody>
</table>
"""
