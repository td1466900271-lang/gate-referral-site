#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-08"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-08-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "AI 半导体验证交易",
        "subtitle": "资金仍在 AI 硬件链，但开始验证估值、存储周期与 CapEx 回报。",
        "cards": [("TSM 台股", "2420-2455", "2500 压力"), ("MU", "940.1", "900-950 观察"), ("SKHX / DRAM", "修复", "反弹需延续")],
        "box1": ("3 个关键观察", ["1. TSMC 7/10 营收与 7/16 法说会。", "2. MU 能否从 900-950 修复到 1000-1050？", "3. NVDA 是否继续强于 AMD / MRVL / INTC？"]),
        "box2": ("交易框架", ["从普涨切到验证。", "存储链修复不是全面解除风险。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：AI 主线未结束，但市场开始要求订单、利润和估值同时验证。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-08-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "AI 半導體驗證交易",
        "subtitle": "資金仍在 AI 硬體鏈，但開始驗證估值、記憶體週期與 CapEx 回報。",
        "cards": [("TSM 台股", "2420-2455", "2500 壓力"), ("MU", "940.1", "900-950 觀察"), ("SKHX / DRAM", "修復", "反彈需延續")],
        "box1": ("3 個關鍵觀察", ["1. TSMC 7/10 營收與 7/16 法說會。", "2. MU 能否從 900-950 修復到 1000-1050？", "3. NVDA 是否繼續強於 AMD / MRVL / INTC？"]),
        "box2": ("交易框架", ["從普漲切到驗證。", "記憶體鏈修復不是全面解除風險。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：AI 主線未結束，但市場開始要求訂單、利潤和估值同時驗證。",
    },
    "en": {
        "file": "market-brief-2026-07-08-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "AI semis enter verification",
        "subtitle": "Capital remains in AI hardware, but valuation, memory cycle and CapEx returns are being tested.",
        "cards": [("TSM TW", "2420-2455", "2500 resistance"), ("MU", "940.1", "watch 900-950"), ("SKHX / DRAM", "rebound", "needs follow-through")],
        "box1": ("3 key checks", ["1. TSMC July 10 revenue and July 16 call.", "2. Can MU recover from 900-950 to 1000-1050?", "3. Does NVDA stay stronger than AMD / MRVL / INTC?"]),
        "box2": ("Framework", ["Broad rally becomes verification.", "Memory repair is not full risk clearance.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: the AI trend is not over, but orders, profit and valuation now need confirmation.",
    },
    "ru": {
        "file": "market-brief-2026-07-08-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "AI-сектор входит в проверку",
        "subtitle": "Капитал остается в аппаратной AI-цепочке, но рынок проверяет оценки, цикл памяти и отдачу CapEx.",
        "cards": [("TSM TW", "2420-2455", "сопротивление 2500"), ("MU", "940.1", "зона 900-950"), ("SKHX / DRAM", "отскок", "нужно продолжение")],
        "box1": ("3 ключевых сигнала", ["1. Выручка TSMC 10 июля и звонок 16 июля.", "2. Вернет ли MU 1000-1050 после 900-950?", "3. Останется ли NVDA сильнее AMD / MRVL / INTC?"]),
        "box2": ("Рамка", ["Широкий рост стал проверкой.", "Ремонт памяти не снимает все риски.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: AI-тренд не завершен, но заказы, прибыль и оценки теперь требуют подтверждения.",
    },
}


def lines(text, width):
    return textwrap.wrap(text, width=width, break_long_words=False, replace_whitespace=False) or [text]


def text_line(x, y, value, size, fill="#d9ecff", weight="700", family="Inter, Arial, sans-serif"):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{family}" font-size="{size}" font-weight="{weight}">{html.escape(value)}</text>'


def paragraph(x, y, values, size, line_height, fill="#d9ecff", weight="700"):
    return "\n".join(text_line(x, y + i * line_height, value, size, fill, weight) for i, value in enumerate(values))


def svg(data):
    card_svg = []
    for i, (label, value, note) in enumerate(data["cards"]):
        x = 70 + i * 246
        card_svg.append(f'''<g transform="translate({x} 276)">
      <rect width="210" height="108" rx="8" fill="#081b3e" stroke="#2e78d8"/>
      {text_line(20, 35, label, 18, "#b9d4ff")}
      {text_line(20, 70, value, 31, "#45b7ff", "800")}
      {text_line(20, 94, note, 16, "#8bb4ed", "700")}
    </g>''')

    box1_title, box1_lines = data["box1"]
    box2_title, box2_lines = data["box2"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#07102b"/>
      <stop offset="0.56" stop-color="#0b2f74"/>
      <stop offset="1" stop-color="#061226"/>
    </linearGradient>
    <linearGradient id="line" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#1b7cff"/>
      <stop offset="1" stop-color="#66b7ff"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#010817" flood-opacity=".42"/>
    </filter>
  </defs>
  <rect width="1200" height="675" fill="url(#bg)"/>
  <path d="M860 0c-48 94-38 188 31 281 62 84 155 122 209 214 38 64 46 123 37 180h63V0z" fill="#0d51a3" opacity=".24"/>
  <path d="M0 520c112-52 203-78 290-80 122-3 186 42 292 16 110-27 147-117 258-132 112-15 176-5 360-106" fill="none" stroke="url(#line)" stroke-width="5" opacity=".82"/>
  <path d="M0 548c138-55 236-70 318-62 104 10 170 37 267 12 116-29 151-104 250-124 129-26 227-13 365-80" fill="none" stroke="#1b7cff" stroke-width="2" opacity=".3"/>

  <g transform="translate(70 48)">
    <rect width="346" height="42" rx="21" fill="#0f4389" stroke="#2491ff" opacity=".9"/>
    {text_line(23, 28, data["tag"], 18, "#d9ecff")}
  </g>

  {text_line(70, 154, data["title"], 54, "#f5f9ff", "800", "Inter, Arial, sans-serif")}
  {paragraph(70, 212, lines(data["subtitle"], 58), 25, 34, "#c8dcf8")}

  <g filter="url(#shadow)" font-family="Inter, Arial, sans-serif">
    {''.join(card_svg)}
  </g>

  <g transform="translate(70 430)" filter="url(#shadow)">
    <rect width="500" height="145" rx="9" fill="#081b3e" stroke="#264f99"/>
    {text_line(26, 42, box1_title, 25, "#f5f9ff", "800")}
    {paragraph(26, 78, box1_lines, 21, 32)}
  </g>

  <g transform="translate(620 430)" filter="url(#shadow)">
    <rect width="430" height="145" rx="9" fill="#081b3e" stroke="#264f99"/>
    {text_line(26, 42, box2_title, 25, "#f5f9ff", "800")}
    {paragraph(26, 78, box2_lines, 21, 32)}
  </g>

  {paragraph(70, 625, lines(data["bottom"], 88), 22, 28, "#45b7ff", "800")}
</svg>
'''


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for data in IMAGES.values():
        (OUT / data["file"]).write_text(svg(data), encoding="utf-8")
    print(f"Generated {len(IMAGES)} localized blue SVG daily images.")


if __name__ == "__main__":
    main()
