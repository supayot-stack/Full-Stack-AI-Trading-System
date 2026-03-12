# services/market_data.py
# ============================================================
# MARKET DATA SERVICE — Phase 1 (Mock / Static Data)
# Phase 2 will replace with real API calls
# ============================================================

from dataclasses import dataclass
from typing import List
import random
import math
from datetime import datetime


@dataclass
class AssetData:
    symbol: str
    name: str
    price: float
    change_24h: float
    signal: str          # "buy" | "wait" | "sell"
    confidence: int      # 0-100
    support: float
    resistance: float
    rsi: float
    volume_24h: float
    market_cap: float
    reasons_th: List[str]
    reasons_en: List[str]
    risks_th: List[str]
    risks_en: List[str]
    short_term_th: str
    short_term_en: str
    mid_term_th: str
    mid_term_en: str


@dataclass
class MacroData:
    dxy: float
    dxy_trend: str
    fed_rate: str
    fed_trend: str
    cpi: str
    cpi_trend: str
    geo_risk: str


@dataclass
class OnChainData:
    whale_flow: str
    exchange_flow: str
    fear_greed: int
    exchange_outflow_btc: str
    whale_deposit_change: str


def get_btc_data() -> AssetData:
    return AssetData(
        symbol="BTC",
        name="Bitcoin",
        price=70_760,
        change_24h=+2.34,
        signal="wait",
        confidence=68,
        support=65_000,
        resistance=75_000,
        rsi=47.25,
        volume_24h=38_500_000_000,
        market_cap=1_390_000_000_000,
        reasons_th=[
            "RSI อยู่ที่ 47 — ไม่แพงเกินไป ไม่ถูกเกินไป อยู่ใน Zone ปกติ",
            "Whale กำลังย้ายเหรียญออกจาก Exchange (สัญญาณการสะสมระยะยาว)",
            "Fear & Greed = 13 (กลัวสุดขีด) — นักลงทุนระยะยาวมักซื้อในช่วงนี้",
            "ETF Outflow $1.8B แต่ BlackRock IBIT ยังมีเงินเข้าใน 5/6 สัปดาห์",
            "ต้องรอดูผล CPI วันนี้ก่อน ถ้าต่ำกว่าคาด BTC มีโอกาสขึ้นทดสอบ $75K",
        ],
        reasons_en=[
            "RSI at 47 — neither overbought nor oversold, in normal zone",
            "Whales moving coins off exchanges — long-term accumulation signal",
            "Fear & Greed = 13 (Extreme Fear) — historically a buy zone",
            "ETF Outflow $1.8B but BlackRock IBIT positive flow in 5/6 weeks",
            "Watch today's CPI — if below 2.4%, BTC may test $75K resistance",
        ],
        risks_th=[
            "ถ้า CPI สูงกว่า 2.5% → Dollar แข็ง → BTC อาจร่วงลงทดสอบ $65K",
            "Whale Ratio = 0.64 — Whale ควบคุม 64% ของ Inflow ทั้งหมด สัญญาณ Fragile",
            "สงครามตะวันออกกลางยังไม่จบ → ความผันผวนสูงได้ทุกเมื่อ",
            "ETF Outflow สะสม $6.18B ตั้งแต่ พ.ย. 2025 — Institutional ยังระมัดระวัง",
        ],
        risks_en=[
            "If CPI > 2.5% → Stronger dollar → BTC may test $65K support",
            "Whale Ratio = 0.64 — Whales control 64% of inflows, market fragile",
            "Middle East conflict unresolved → Volatility spike risk at any time",
            "Cumulative ETF Outflow $6.18B since Nov 2025 — institutions still cautious",
        ],
        short_term_th="คาด Consolidate ในกรอบ $65K-$75K รอผล CPI เป็น Catalyst",
        short_term_en="Expect consolidation $65K-$75K range, CPI as key catalyst",
        mid_term_th="ถ้า $65K ยังเป็น Support ได้ เป้าถัดไปคือ $78K-$80K ใน Q2 2026",
        mid_term_en="If $65K support holds, next target $78K-$80K in Q2 2026",
    )


def get_gold_data() -> AssetData:
    return AssetData(
        symbol="XAU",
        name="Gold",
        price=5_145,
        change_24h=-0.87,
        signal="buy",
        confidence=74,
        support=5_052,
        resistance=5_261,
        rsi=53.0,
        volume_24h=198_000_000_000,
        market_cap=21_300_000_000_000,
        reasons_th=[
            "ธนาคารกลางทั่วโลกซื้อทองต่อเนื่อง ~755 ตัน/ปี (Structural Demand)",
            "สงครามตะวันออกกลางผลักดัน Safe-Haven Demand สูงขึ้นอย่างมีนัยสำคัญ",
            "RSI 53 — ยังมีพื้นที่ขึ้นต่อได้ ไม่ได้ Overbought",
            "De-dollarization trend — ประเทศ EM ลดการถือ USD เพิ่มทอง",
            "JP Morgan Target สิ้นปี 2026 ที่ $6,300 (upside +22% จากปัจจุบัน)",
        ],
        reasons_en=[
            "Central banks buying ~755 tons/year globally (structural demand)",
            "Middle East war driving significant safe-haven demand",
            "RSI 53 — still has upside room, not overbought",
            "De-dollarization trend — EM countries reducing USD, adding gold",
            "JP Morgan 2026 year-end target $6,300 (+22% upside from current)",
        ],
        risks_th=[
            "ถ้าสงครามยุติกะทันหัน → War Premium คายออก ราคาลงเร็ว $300-500",
            "Dollar แข็งตัวจาก CPI สูง → กดดัน Gold ระยะสั้น",
            "Gold ETF Outflow ถ้า Risk Appetite กลับมา → Rotation ออกจาก Gold",
            "ห่าง ATH ($5,595) แค่ 8% อาจมีแรงขายทำกำไร (Profit Taking)",
        ],
        risks_en=[
            "Sudden peace deal → War premium unwinds, quick $300-500 drop",
            "Strong CPI → Dollar strength pressures gold short-term",
            "Gold ETF outflows if risk appetite returns → Rotation out of gold",
            "Only 8% from ATH ($5,595), profit-taking pressure likely",
        ],
        short_term_th="ระวัง Volatility จาก CPI วันนี้ แนวรับ $5,052 ยังแข็งแกร่ง",
        short_term_en="Watch CPI volatility today, $5,052 support remains solid",
        mid_term_th="ถ้ายืนเหนือ $5,143 ได้ เป้า Retest ATH $5,595 และ $6,000+",
        mid_term_en="If holding above $5,143, targets ATH retest $5,595 then $6,000+",
    )


def get_macro_data() -> MacroData:
    return MacroData(
        dxy=98.9,
        dxy_trend="▲ Rising",
        fed_rate="3.50–3.75%",
        fed_trend="⏸ On Hold",
        cpi="2.4%",
        cpi_trend="👀 Watch Today",
        geo_risk="HIGH ⚠️",
    )


def get_onchain_data() -> OnChainData:
    return OnChainData(
        whale_flow="accumulating",
        exchange_flow="outflow",
        fear_greed=13,
        exchange_outflow_btc="32,000 BTC",
        whale_deposit_change="-18% MoM",
    )


def get_sparkline_data(base: float, periods: int = 30, volatility: float = 0.02) -> List[float]:
    """Generate realistic-looking sparkline price data."""
    data = [base]
    for i in range(periods - 1):
        change = random.gauss(0, volatility) + math.sin(i * 0.3) * 0.005
        new_price = data[-1] * (1 + change)
        data.append(new_price)
    return data


def format_price(price: float, symbol: str = "$") -> str:
    if price >= 1_000_000:
        return f"{symbol}{price/1_000_000:.2f}M"
    elif price >= 1_000:
        return f"{symbol}{price:,.0f}"
    return f"{symbol}{price:.2f}"


def format_volume(volume: float) -> str:
    if volume >= 1_000_000_000:
        return f"${volume/1_000_000_000:.1f}B"
    elif volume >= 1_000_000:
        return f"${volume/1_000_000:.0f}M"
    return f"${volume:,.0f}"
