# utils/translations.py
# ============================================================
# TRANSLATION DICTIONARY — TH / EN
# ============================================================

TRANSLATIONS = {
    "th": {
        # App
        "app_title": "FULL-STACK AI TRADING SYSTEM",
        "app_subtitle": "ระบบวิเคราะห์การลงทุนอัจฉริยะ",
        "phase_badge": "⚡ เฟส 2 — ข้อมูลจริง LIVE",
        "last_update": "อัพเดทล่าสุด",
        "disclaimer": "⚠️ เพื่อการศึกษาเท่านั้น — ไม่ใช่คำแนะนำการลงทุน",

        # Navigation
        "nav_dashboard": "📊 แดชบอร์ด",
        "nav_signals": "⚡ สัญญาณ AI",
        "nav_portfolio": "💼 พอร์ตจำลอง",
        "nav_learn": "🎓 เรียนรู้",

        # Market
        "market_overview": "ภาพรวมตลาด",
        "btc_label": "Bitcoin",
        "gold_label": "ทองคำ",
        "signal_buy": "สะสมได้",
        "signal_wait": "รอดูก่อน",
        "signal_sell": "ระวังความเสี่ยง",
        "ai_confidence": "ความมั่นใจ AI",
        "support": "แนวรับ",
        "resistance": "แนวต้าน",
        "rsi_label": "RSI",
        "change_24h": "เปลี่ยนแปลง 24ชม.",

        # Macro
        "macro_title": "ปัจจัยเศรษฐกิจโลก",
        "dxy_label": "ดัชนีดอลลาร์ (DXY)",
        "fed_label": "อัตราดอกเบี้ย Fed",
        "cpi_label": "เงินเฟ้อ (CPI)",
        "geo_label": "ความเสี่ยงภูมิรัฐศาสตร์",

        # On-chain
        "onchain_title": "On-Chain Intelligence",
        "whale_flow": "Whale Flow",
        "exchange_flow": "Exchange Flow",
        "fear_greed": "Fear & Greed",
        "accumulating": "กำลังสะสม 🐋",
        "outflow": "เงินออก (Bullish) 📤",
        "extreme_fear": "กลัวสุดขีด 😱",

        # Signals
        "why_title": "เหตุผลของ AI",
        "risk_title": "ความเสี่ยงที่ต้องระวัง",
        "short_term": "ระยะสั้น (1 สัปดาห์)",
        "mid_term": "ระยะกลาง (1-3 เดือน)",

        # Portfolio
        "paper_title": "พอร์ตจำลอง — ไม่มีความเสี่ยงจริง",
        "paper_balance": "ยอดเงินจำลอง",
        "paper_pnl": "กำไร/ขาดทุน",
        "paper_desc": "ทดลองเทรดด้วยเงินสมมติ เรียนรู้โดยไม่เสี่ยงเงินจริง",
        "allocation": "การจัดสรรพอร์ต",
        "cash": "เงินสด",

        # Learn
        "learn_title": "เรียนรู้กับ AI Trading System",
        "learn_q1": "Bitcoin คืออะไร?",
        "learn_q2": "ทำไม Gold ถึงปลอดภัยกว่า?",
        "learn_q3": "DXY มีผลต่อตลาดยังไง?",
        "learn_q4": "ควรแบ่งเงินลงทุนยังไง?",
        "learn_q5": "RSI คืออะไร ดูยังไง?",
        "learn_q6": "Whale คือใคร ทำไมต้องสนใจ?",
        "key_concepts": "แนวคิดสำคัญ",
    },
    "en": {
        # App
        "app_title": "FULL-STACK AI TRADING SYSTEM",
        "app_subtitle": "Intelligent Investment Analysis System",
        "phase_badge": "⚡ Phase 2 — Live Data Mode",
        "last_update": "Last Updated",
        "disclaimer": "⚠️ For educational purposes only — Not financial advice",

        # Navigation
        "nav_dashboard": "📊 Dashboard",
        "nav_signals": "⚡ AI Signals",
        "nav_portfolio": "💼 Paper Portfolio",
        "nav_learn": "🎓 Learn",

        # Market
        "market_overview": "Market Overview",
        "btc_label": "Bitcoin",
        "gold_label": "Gold",
        "signal_buy": "Accumulate",
        "signal_wait": "Wait & Watch",
        "signal_sell": "High Risk",
        "ai_confidence": "AI Confidence",
        "support": "Support",
        "resistance": "Resistance",
        "rsi_label": "RSI",
        "change_24h": "24h Change",

        # Macro
        "macro_title": "Global Macro Factors",
        "dxy_label": "Dollar Index (DXY)",
        "fed_label": "Fed Funds Rate",
        "cpi_label": "Inflation (CPI)",
        "geo_label": "Geopolitical Risk",

        # On-chain
        "onchain_title": "On-Chain Intelligence",
        "whale_flow": "Whale Flow",
        "exchange_flow": "Exchange Flow",
        "fear_greed": "Fear & Greed",
        "accumulating": "Accumulating 🐋",
        "outflow": "Outflow (Bullish) 📤",
        "extreme_fear": "Extreme Fear 😱",

        # Signals
        "why_title": "AI Reasoning",
        "risk_title": "Risks to Watch",
        "short_term": "Short-Term (1 Week)",
        "mid_term": "Mid-Term (1-3 Months)",

        # Portfolio
        "paper_title": "Paper Portfolio — Zero Real Risk",
        "paper_balance": "Simulated Balance",
        "paper_pnl": "Profit / Loss",
        "paper_desc": "Practice trading with virtual money. Learn without risking real capital.",
        "allocation": "Portfolio Allocation",
        "cash": "Cash",

        # Learn
        "learn_title": "Learn with AI Trading System",
        "learn_q1": "What is Bitcoin?",
        "learn_q2": "Why is Gold safer?",
        "learn_q3": "How does DXY affect markets?",
        "learn_q4": "How to allocate investments?",
        "learn_q5": "What is RSI and how to read it?",
        "learn_q6": "Who are Whales and why do they matter?",
        "key_concepts": "Key Concepts",
    }
}

LEARN_ANSWERS = {
    "th": {
        "Bitcoin คืออะไร?": """
**Bitcoin (BTC)** คือเงินดิจิทัลที่ไม่มีรัฐบาลหรือธนาคารใดควบคุม

🔑 **สิ่งที่ควรรู้:**
- มีจำนวนจำกัดเพียง **21 ล้านเหรียญ** ตลอดกาล (เหมือนทองคำดิจิทัล)
- ทำธุรกรรมได้ทั่วโลกโดยไม่ต้องผ่านธนาคาร
- ราคาผันผวนสูงมาก — สามารถขึ้น/ลงได้ **20-50% ในเดือนเดียว**

⚠️ **คำแนะนำ:** อย่าลงทุนเงินที่ขาดไม่ได้ เริ่มด้วยจำนวนน้อยก่อนเสมอ
        """,
        "ทำไม Gold ถึงปลอดภัยกว่า?": """
**ทองคำ** เป็น Safe Haven มากกว่า 5,000 ปี เมื่อโลกมีวิกฤต นักลงทุนวิ่งหาทอง

🔑 **เหตุผลที่ปลอดภัยกว่า BTC:**
- ธนาคารกลางทั่วโลกถือทองเป็นทุนสำรอง (~755 ตัน/ปี)
- ความผันผวนต่ำกว่า BTC ประมาณ **3-4 เท่า**
- มีมูลค่าจริงทางกายภาพ ไม่สามารถ "แฮก" ได้

📊 **ตัวเลขจริง:** ปี 2025 Gold ขึ้น +65% | BTC ขึ้น +120% แต่ลงได้เร็วกว่ามาก
        """,
        "DXY มีผลต่อตลาดยังไง?": """
**DXY (Dollar Index)** วัดความแข็งแกร่งของเงินดอลลาร์เทียบกับสกุลเงินหลัก

🔄 **ความสัมพันธ์:**
- DXY ขึ้น ➜ Gold/BTC **มักลง** (ดอลลาร์แข็ง = สินทรัพย์อื่นแพงขึ้นสำหรับต่างชาติ)
- DXY ลง ➜ Gold/BTC **มักขึ้น** (ดอลลาร์อ่อน = นักลงทุนหนีไปสินทรัพย์อื่น)

📌 **ปัจจุบัน DXY = 98.9 (สูง)** ➜ เป็นแรงกดดันต่อ Gold และ BTC ในระยะสั้น
        """,
        "ควรแบ่งเงินลงทุนยังไง?": """
**AI Trading System แนะนำสำหรับมือใหม่:**

| สัดส่วน | ประเภท | เหตุผล |
|---------|--------|--------|
| 70% | เงินสำรองฉุกเฉิน | ความปลอดภัยสูงสุด |
| 20% | ทองคำ / สินทรัพย์ปลอดภัย | Hedge ความเสี่ยง |
| 10% | BTC (ถ้ารับความเสี่ยงได้) | Upside โอกาส |

⚠️ **กฎทอง:** อย่าลงทุนเงินที่ขาดไม่ได้ และค่อยๆ เพิ่มสัดส่วนเมื่อเข้าใจมากขึ้น
        """,
        "RSI คืออะไร ดูยังไง?": """
**RSI (Relative Strength Index)** วัดว่าสินทรัพย์แพงหรือถูกเกินไป (0-100)

📊 **การอ่านค่า:**
- **RSI 0-30** = ถูกเกินไป (Oversold) ➜ อาจเป็นโอกาสซื้อ
- **RSI 30-70** = Zone ปกติ ➜ รอดูแนวโน้ม  
- **RSI 70-100** = แพงเกินไป (Overbought) ➜ ระวังการย่อตัว

📌 **ปัจจุบัน:** BTC RSI = 47 (ปกติ) | Gold RSI = 53 (ปกติ-บวก)
        """,
        "Whale คือใคร ทำไมต้องสนใจ?": """
**Whale** คือนักลงทุนที่ถือ Bitcoin จำนวนมาก (มักเกิน 1,000 BTC)

🐋 **ทำไมต้องสนใจ?**
- Whale ควบคุมเหรียญในตลาดจำนวนมาก การเคลื่อนไหวของพวกเขา **ขยับราคาได้จริง**
- ถ้า Whale ย้ายเหรียญออกจาก Exchange ➜ **Bullish** (เตรียมถือระยะยาว)
- ถ้า Whale ส่งเหรียญเข้า Exchange ➜ **Bearish** (อาจจะขาย)

📌 **ปัจจุบัน:** Whale Exchange Deposit ลดลง 18% MoM ➜ สัญญาณ Accumulation
        """,
    },
    "en": {
        "What is Bitcoin?": """
**Bitcoin (BTC)** is a decentralized digital currency not controlled by any government or bank.

🔑 **Key Facts:**
- Fixed supply of only **21 million coins** ever (digital gold)
- Global peer-to-peer transactions without banks
- Highly volatile — can move **20-50% in a single month**

⚠️ **Advice:** Never invest money you cannot afford to lose. Always start small.
        """,
        "Why is Gold safer?": """
**Gold** has been a safe-haven asset for 5,000+ years. During crises, investors flee to gold.

🔑 **Why safer than BTC:**
- Central banks hold gold as reserves (~755 tons/year globally)
- Approximately **3-4x less volatile** than BTC
- Physical intrinsic value — cannot be hacked

📊 **Real numbers:** 2025: Gold +65% | BTC +120% but much faster drawdowns
        """,
        "How does DXY affect markets?": """
**DXY (Dollar Index)** measures USD strength against major currencies.

🔄 **Relationship:**
- DXY rises ➜ Gold/BTC **often falls** (stronger dollar = assets more expensive for foreigners)
- DXY falls ➜ Gold/BTC **often rises** (weaker dollar = investors seek alternatives)

📌 **Current DXY = 98.9 (High)** ➜ Short-term headwind for both Gold and BTC
        """,
        "How to allocate investments?": """
**AI Trading System recommends for beginners:**

| Allocation | Type | Reason |
|-----------|------|--------|
| 70% | Emergency fund | Maximum safety |
| 20% | Gold / Safe assets | Risk hedge |
| 10% | BTC (if risk-tolerant) | Upside opportunity |

⚠️ **Golden Rule:** Never invest money you need. Gradually increase allocation as you learn more.
        """,
        "What is RSI and how to read it?": """
**RSI (Relative Strength Index)** measures if an asset is overpriced or underpriced (0-100).

📊 **Reading RSI:**
- **RSI 0-30** = Oversold ➜ Potential buying opportunity
- **RSI 30-70** = Normal zone ➜ Watch the trend
- **RSI 70-100** = Overbought ➜ Watch for correction

📌 **Current:** BTC RSI = 47 (Normal) | Gold RSI = 53 (Normal-Bullish)
        """,
        "Who are Whales and why do they matter?": """
**Whales** are investors holding large amounts of Bitcoin (usually 1,000+ BTC).

🐋 **Why they matter:**
- Whales control massive supply — their moves **genuinely move the market**
- Whales moving coins OFF exchanges ➜ **Bullish** (holding long-term)
- Whales sending coins TO exchanges ➜ **Bearish** (preparing to sell)

📌 **Current:** Whale Exchange Deposits down 18% MoM ➜ Accumulation signal
        """,
    }
}
