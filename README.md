# 🛡️ FULL-STACK AI TRADING SYSTEM
> Dark Premium Bloomberg-Style AI Investment Dashboard

![Phase](https://img.shields.io/badge/Phase-1%20Learning%20Mode-gold)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red)
![Python](https://img.shields.io/badge/Python-3.10+-blue)

---

## 📌 Overview

Full-Stack AI Trading System เป็นระบบวิเคราะห์การลงทุนอัจฉริยะ สำหรับ BTC/USD และ XAU/USD (ทองคำ)
ออกแบบสำหรับผู้เริ่มต้นที่ต้องการเรียนรู้การลงทุนโดยมี AI เป็นผู้ช่วย

**Phase 1 — Learning Mode (ปลอดภัย 100%)**
- ข้อมูลจำลอง — ไม่มีการเชื่อมต่อ Exchange จริง
- Paper Trading — ทดลองเทรดด้วยเงินสมมติ
- AI อธิบายทุก Signal เป็นภาษาคนธรรมดา

---

## 🗂️ Project Structure

```
full-stack-ai-trading-system/
├── app.py                    # Main Streamlit App
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── config.toml           # Dark Premium Theme
├── components/
│   └── ui_styles.py          # Bloomberg CSS & HTML Components
├── services/
│   └── market_data.py        # Data Layer (Mock → Real API in Phase 2)
└── utils/
    └── translations.py       # TH/EN Dictionary
```

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/full-stack-ai-trading-system.git
cd full-stack-ai-trading-system

# 2. Install
pip install -r requirements.txt

# 3. Run
streamlit run app.py
```

---

## ☁️ Deploy to Streamlit Cloud (Free)

1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set **Main file path** = `app.py`
5. Click **Deploy** ✅

---

## 🗺️ Roadmap

| Phase | Status | Features |
|-------|--------|----------|
| Phase 1 | ✅ Current | Dashboard, AI Signals, Paper Trading, Learn |
| Phase 2 | 🔜 Next | Real Price API, Live On-chain, News Sentiment |
| Phase 3 | 🔜 Future | Live Paper Trading Engine, Backtesting |
| Phase 4 | 🔜 Future | Risk Management + Live Execution (after validation) |

---

## ⚠️ Disclaimer

เพื่อการศึกษาเท่านั้น ไม่ใช่คำแนะนำการลงทุน
For educational purposes only. Not financial advice.
