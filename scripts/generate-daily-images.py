#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-17"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-17-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "强财报后的资本回报再定价",
        "subtitle": "台积电需求与利润创新高，但高资本开支、毛利率边际回落和拥挤仓位推动 AI 科技去风险。",
        "cards": [("TSMC", "$40.2B", "二季度美元收入"), ("TAIEX / TSMC", "-5.2% / -5.1%", "广泛去风险"), ("CapEx", "$60-64B", "2026 资本开支")],
        "box1": ("3 个关键观察", ["1. TSMC 2340-2350 能否守稳？", "2. SOXX / SMH 成交是否确认？", "3. 油价、利率与美元是否共振？"]),
        "box2": ("估值框架", ["AI 需求仍强，估值容错下降。", "重点转向毛利率与自由现金流。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：产业景气仍强，市场正在重新评估资本开支与回报兑现。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-17-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "強財報後的資本回報再定價",
        "subtitle": "台積電需求與利潤創新高，但高資本開支、毛利率邊際回落和擁擠部位推動 AI 科技去風險。",
        "cards": [("TSMC", "$40.2B", "第二季度美元收入"), ("TAIEX / TSMC", "-5.2% / -5.1%", "廣泛去風險"), ("CapEx", "$60-64B", "2026 資本開支")],
        "box1": ("3 個關鍵觀察", ["1. TSMC 2340-2350 能否守穩？", "2. SOXX / SMH 成交是否確認？", "3. 油價、利率與美元是否共振？"]),
        "box2": ("估值框架", ["AI 需求仍強，估值容錯下降。", "重點轉向毛利率與自由現金流。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：產業景氣仍強，市場正在重新評估資本開支與回報兌現。",
    },
    "en": {
        "file": "market-brief-2026-07-17-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "Capital returns repriced after strong results",
        "subtitle": "TSMC demand and profit hit records, but high capex, softer margin guidance and crowded positions drive AI tech de-risking.",
        "cards": [("TSMC", "$40.2B", "Q2 USD revenue"), ("TAIEX / TSMC", "-5.2% / -5.1%", "broad de-risking"), ("CapEx", "$60-64B", "2026 spending")],
        "box1": ("3 key checks", ["1. Can TSMC hold 2340-2350?", "2. Do SOXX / SMH volumes confirm?", "3. Do oil, yields and USD rise together?"]),
        "box2": ("Valuation Frame", ["AI demand is firm; valuation tolerance falls.", "Focus shifts to margin and free cash flow.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: industry demand remains strong while markets reprice capex and realized capital returns.",
    },
    "ru": {
        "file": "market-brief-2026-07-17-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "Сильный отчет, переоценка капитала",
        "subtitle": "Рекорды TSMC не остановили снижение: капзатраты, маржа и перегретые позиции давят на AI-технологии.",
        "cards": [("TSMC", "$40.2B", "выручка Q2"), ("TAIEX / TSMC", "-5.2% / -5.1%", "снижение риска"), ("Капзатраты", "$60-64B", "план на 2026")],
        "box1": ("3 ключевых сигнала", ["1. Удержит ли TSMC зону 2340-2350?", "2. Подтвердят ли объемы SOXX / SMH?", "3. Растут ли нефть, ставки и доллар вместе?"]),
        "box2": ("Рамка Оценки", ["Спрос на AI силен, запас оценки снижается.", "Фокус на марже и свободном денежном потоке.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: отраслевой спрос силен, но рынок переоценивает капзатраты и фактическую отдачу капитала.",
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
