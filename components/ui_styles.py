# components/ui_styles.py
# ============================================================
# DARK PREMIUM BLOOMBERG-STYLE UI — CSS & HTML Components
# Phase 2: Real data, NO << button, clean sidebar
# ============================================================

BLOOMBERG_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500;600;700&family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&display=swap');

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
    --font-mono:   'IBM Plex Mono', monospace;
    --font-th:     'IBM Plex Sans Thai', sans-serif;
}

* { box-sizing: border-box; }

.stApp {
    background: var(--bg-0) !important;
    font-family: var(--font-mono) !important;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.stDeployButton { display: none; }

/* ── HIDE << COLLAPSE ARROW ── */
[data-testid="stSidebarCollapseButton"],
button[data-testid="collapsedControl"],
[data-testid="stSidebarCollapsedControl"] {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
}

[data-testid="stSidebar"] {
    background: var(--bg-1) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-1) !important; }

.stSelectbox label, .stRadio label { color: var(--text-2) !important; font-size: 11px !important; letter-spacing: 1px; text-transform: uppercase; }
.stSelectbox > div > div { background: var(--bg-2) !important; border: 1px solid var(--border) !important; color: var(--gold) !important; }

[data-testid="metric-container"] {
    background: var(--bg-2);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 16px !important;
}
[data-testid="metric-container"] label { color: var(--text-3) !important; font-size: 10px !important; letter-spacing: 2px; text-transform: uppercase; }
[data-testid="metric-container"] [data-testid="stMetricValue"] { color: var(--gold) !important; font-family: var(--font-mono) !important; font-size: 22px !important; font-weight: 700; }

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

.streamlit-expanderHeader {
    background: var(--bg-2) !important;
    border: 1px solid var(--border) !important;
    color: var(--text-2) !important;
    font-size: 11px !important;
    letter-spacing: 1px;
}

hr { border-color: var(--border) !important; }

@keyframes marquee { from { transform: translateX(0); } to { transform: translateX(-50%); } }
.marquee-track { display: inline-flex; animation: marquee 40s linear infinite; white-space: nowrap; }
.ticker-up    { color: #00C853 !important; }
.ticker-down  { color: #FF3D3D !important; }
.ticker-neutral { color: var(--text-3) !important; }

@keyframes pulse-gold {
    0%,100% { box-shadow: 0 0 0 0 rgba(201,168,76,0.6); }
    50%      { box-shadow: 0 0 0 6px rgba(201,168,76,0); }
}
.pulse-dot {
    display: inline-block;
    width: 7px; height: 7px;
    background: var(--gold);
    border-radius: 50%;
    margin-right: 8px;
    animation: pulse-gold 2s ease-in-out infinite;
    vertical-align: middle;
}

.bberg-card {
    background: var(--bg-1);
    border: 1px solid var(--border);
    padding: 20px;
    position: relative;
}
.bberg-card-gold { border-top: 2px solid var(--gold); }

.section-label {
    font-size: 10px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--text-3);
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
}
.gold-label { color: var(--gold) !important; border-bottom-color: rgba(201,168,76,0.2) !important; }

.price-main {
    font-size: 46px;
    font-weight: 700;
    letter-spacing: -1px;
    color: var(--text-1);
    line-height: 1;
}
.price-change { font-size: 13px; }

.conf-bar-bg { background: var(--bg-3); height: 3px; width: 100%; margin-top: 12px; }
.conf-bar-fill-gold  { background: linear-gradient(90deg, var(--gold), var(--gold-light)); height: 3px; }
.conf-bar-fill-green { background: linear-gradient(90deg, #00C853, #69F0AE); height: 3px; }

.signal-buy  { color: #00C853; border: 1px solid #00C853; background: var(--green-dim); padding: 4px 14px; font-size: 12px; letter-spacing: 2px; font-weight: 600; }
.signal-sell { color: #FF3D3D; border: 1px solid #FF3D3D; background: var(--red-dim);   padding: 4px 14px; font-size: 12px; letter-spacing: 2px; font-weight: 600; }
.signal-wait { color: var(--gold); border: 1px solid var(--gold); background: var(--gold-glow); padding: 4px 14px; font-size: 12px; letter-spacing: 2px; font-weight: 600; }

.phase-badge {
    display: inline-block;
    background: var(--gold-glow);
    border: 1px solid rgba(201,168,76,0.3);
    color: var(--gold);
    font-size: 11px;
    letter-spacing: 2px;
    padding: 4px 12px;
    font-weight: 600;
}

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--bg-0); }
::-webkit-scrollbar-thumb { background: var(--gold-dim); }
</style>
"""


def header_html(t: dict, lang: str, timestamp: str) -> str:
    return f"""
<div style="background:#0A0C12; border-bottom:2px solid #3D2D0A; padding:0; margin-bottom:0;">
    <div style="background:#070809; border-bottom:1px solid rgba(201,168,76,0.1); padding:5px 24px; overflow:hidden;">
        <div class="marquee-track">
            <span style="font-size:10px; font-family:'IBM Plex Mono',monospace; color:#5C5040; letter-spacing:0.5px;">
                <span class="ticker-neutral">BTC/USD</span>&nbsp;<span class="ticker-up">$70,760 ▲2.34%</span>&nbsp;&nbsp;│&nbsp;&nbsp;
                <span class="ticker-neutral">XAU/USD</span>&nbsp;<span class="ticker-down">$3,100 ▼0.25%</span>&nbsp;&nbsp;│&nbsp;&nbsp;
                <span class="ticker-neutral">DXY</span>&nbsp;<span class="ticker-up">98.9 ▲0.3%</span>&nbsp;&nbsp;│&nbsp;&nbsp;
                <span class="ticker-neutral">FED RATE</span>&nbsp;<span style="color:#A89880;">3.625%</span>&nbsp;&nbsp;│&nbsp;&nbsp;
                <span class="ticker-neutral">CPI</span>&nbsp;<span class="ticker-down">2.4% ⚠</span>&nbsp;&nbsp;│&nbsp;&nbsp;
                <span class="ticker-neutral">FEAR&amp;GREED</span>&nbsp;<span class="ticker-down">18 — EXTREME FEAR</span>&nbsp;&nbsp;│&nbsp;&nbsp;
                <span class="ticker-neutral">BTC/USD</span>&nbsp;<span class="ticker-up">$70,760 ▲2.34%</span>&nbsp;&nbsp;│&nbsp;&nbsp;
                <span class="ticker-neutral">XAU/USD</span>&nbsp;<span class="ticker-down">$3,100 ▼0.25%</span>&nbsp;&nbsp;│&nbsp;&nbsp;
                <span class="ticker-neutral">GEOPOLITICAL RISK</span>&nbsp;<span class="ticker-down">HIGH — MIDDLE EAST</span>
            </span>
        </div>
    </div>
    <div style="padding:16px 28px; display:flex; align-items:center; justify-content:space-between;">
        <div style="display:flex; align-items:center; gap:16px;">
            <div style="width:36px; height:36px; background:linear-gradient(135deg,#C9A84C,#8B6914);
                        display:flex; align-items:center; justify-content:center; font-size:18px;">🛡</div>
            <div>
                <div style="font-family:'IBM Plex Mono',monospace; font-size:16px; font-weight:700;
                            color:#E8E0D0; letter-spacing:3px;">FULL-STACK AI TRADING SYSTEM</div>
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


def macro_card_html(label: str, value: str, trend: str, color: str = "gold") -> str:
    colors = {
        "gold":  ("#3D2D0A", "#C9A84C"),
        "blue":  ("#0A1628", "#2196F3"),
        "olive": ("#1A1A0A", "#8B8B00"),
        "red":   ("#2A0A0A", "#CC3333"),
    }
    bg, accent = colors.get(color, colors["gold"])
    return f"""
<div style="background:#0A0C12; border:1px solid rgba(201,168,76,0.08);
            border-left:3px solid {accent}; padding:18px 20px; height:100%;">
    <div style="font-size:9px; letter-spacing:3px; text-transform:uppercase;
                color:#5C5040; margin-bottom:10px;">{label}</div>
    <div style="font-family:'IBM Plex Mono',monospace; font-size:24px; font-weight:700;
                color:#E8E0D0; letter-spacing:1px;">{value}</div>
    <div style="font-size:11px; color:#5C5040; margin-top:6px; letter-spacing:1px;">{trend}</div>
</div>
"""


def asset_card_html(asset, signal_label: str, t: dict, color: str = "gold") -> str:
    change_color = "#00C853" if asset.change_24h >= 0 else "#FF3D3D"
    change_arrow = "▲" if asset.change_24h >= 0 else "▼"
    signal_cls = f"signal-{asset.signal}"
    bar_class = "conf-bar-fill-gold" if color == "gold" else "conf-bar-fill-green"
    border_top = "#C9A84C" if color == "gold" else "#00C853"

    source_dot = ""
    if hasattr(asset, 'data_source'):
        if asset.data_source == "live":
            source_dot = '<span style="font-size:9px;color:#00C853;letter-spacing:1px;"> ● LIVE</span>'
        else:
            source_dot = '<span style="font-size:9px;color:#5C5040;letter-spacing:1px;"> ○ MOCK</span>'

    return f"""
<div style="background:#0A0C12; border:1px solid rgba(201,168,76,0.08);
            border-top:2px solid {border_top}; padding:20px; height:100%;">
    <div style="font-size:10px; letter-spacing:3px; text-transform:uppercase; color:#5C5040;
                margin-bottom:14px; display:flex; align-items:center; justify-content:space-between;">
        <span>{'₿ BTC/USD' if asset.symbol == 'BTC' else '◈ XAU/USD'}</span>
        {source_dot}
    </div>
    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px;">
        <div>
            <div class="price-main">${asset.price:,.0f}</div>
            <div style="margin-top:5px;">
                <span class="price-change" style="color:{change_color};">{change_arrow} {abs(asset.change_24h):.2f}%</span>
                <span style="font-size:10px; color:#3D3020; margin-left:8px;">24H</span>
            </div>
        </div>
        <div class="{signal_cls}">{signal_label}</div>
    </div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-bottom:14px;">
        <div>
            <div style="font-size:9px; color:#5C5040; letter-spacing:2px; text-transform:uppercase;">{t.get('support','SUPPORT')}</div>
            <div style="font-family:'IBM Plex Mono',monospace; font-size:14px; color:#A89880; margin-top:3px;">${asset.support:,.0f}</div>
        </div>
        <div>
            <div style="font-size:9px; color:#5C5040; letter-spacing:2px; text-transform:uppercase;">{t.get('resistance','RESIST')}</div>
            <div style="font-family:'IBM Plex Mono',monospace; font-size:14px; color:#A89880; margin-top:3px;">${asset.resistance:,.0f}</div>
        </div>
        <div>
            <div style="font-size:9px; color:#5C5040; letter-spacing:2px; text-transform:uppercase;">RSI</div>
            <div style="font-family:'IBM Plex Mono',monospace; font-size:14px; color:#A89880; margin-top:3px;">{asset.rsi}</div>
        </div>
    </div>
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:5px;">
        <div style="font-size:9px; color:#5C5040; letter-spacing:2px; text-transform:uppercase;">{t.get('ai_confidence','AI CONFIDENCE')}</div>
        <div style="font-size:12px; font-weight:700; color:{border_top};">{asset.confidence}%</div>
    </div>
    <div class="conf-bar-bg"><div class="{bar_class}" style="width:{asset.confidence}%;"></div></div>
</div>
"""


def comparison_table_html(btc, gold, t: dict, lang: str) -> str:
    rows = [
        (t.get('price','Price'),        f"${btc.price:,.0f}",      f"${gold.price:,.0f}"),
        ("24H",                          f"{btc.change_24h:+.2f}%", f"{gold.change_24h:+.2f}%"),
        ("RSI",                          str(btc.rsi),              str(gold.rsi)),
        (t.get('signal','Signal'),       btc.signal.upper(),        gold.signal.upper()),
        (t.get('ai_confidence','Conf.'), f"{btc.confidence}%",      f"{gold.confidence}%"),
        (t.get('support','Support'),     f"${btc.support:,.0f}",    f"${gold.support:,.0f}"),
        (t.get('resistance','Resist.'),  f"${btc.resistance:,.0f}", f"${gold.resistance:,.0f}"),
    ]
    rows_html = ""
    for label, b, g in rows:
        rows_html += f"""
        <tr>
            <td style="font-size:10px;color:#5C5040;letter-spacing:2px;text-transform:uppercase;
                       padding:10px 0;border-bottom:1px solid rgba(201,168,76,0.06);">{label}</td>
            <td style="font-family:'IBM Plex Mono',monospace;font-size:14px;color:#C9A84C;
                       text-align:right;padding:10px 0;border-bottom:1px solid rgba(201,168,76,0.06);">{b}</td>
            <td style="font-family:'IBM Plex Mono',monospace;font-size:14px;color:#00C853;
                       text-align:right;padding:10px 0;border-bottom:1px solid rgba(201,168,76,0.06);">{g}</td>
        </tr>"""
    return f"""
<div style="background:#0A0C12;border:1px solid rgba(201,168,76,0.08);border-top:2px solid #C9A84C;padding:20px;">
    <table style="width:100%;border-collapse:collapse;">
        <thead><tr>
            <th style="font-size:9px;color:#5C5040;letter-spacing:3px;text-align:left;padding-bottom:12px;text-transform:uppercase;"></th>
            <th style="font-family:'IBM Plex Mono',monospace;font-size:12px;color:#C9A84C;text-align:right;letter-spacing:2px;padding-bottom:12px;">₿ BTC</th>
            <th style="font-family:'IBM Plex Mono',monospace;font-size:12px;color:#00C853;text-align:right;letter-spacing:2px;padding-bottom:12px;">◈ GOLD</th>
        </tr></thead>
        <tbody>{rows_html}</tbody>
    </table>
</div>
"""
