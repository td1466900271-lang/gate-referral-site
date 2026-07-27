#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-27"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-27-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "油价回落，等待云财报接力",
        "subtitle": "风险环境边际缓和，台积电相对抗跌；低成交反弹仍需四大科技公司的资本回报共同确认。",
        "cards": [("Brent / WTI", "-5.2 / -5.4", "亚洲时段百分比"), ("TSMC", "2350-2355", "接近前收"), ("TraderXYZ", "$1.48B", "前十成交偏低")],
        "box1": ("3 个关键观察", ["1. Brent 能否稳定低于 90 美元？", "2. TSMC 能否守住 2330-2350？", "3. 云厂能否兑现自由现金流？"]),
        "box2": ("本周框架", ["Microsoft / Meta 云增速与资本开支。", "Amazon AWS 与 Apple 盈利质量。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：风险缓和不等于解除，AI 行情将由云收入、资本开支和现金回报共同决定。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-27-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "油價回落，等待雲端財報接力",
        "subtitle": "風險環境邊際緩和，台積電相對抗跌；低成交反彈仍需四大科技公司的資本回報共同確認。",
        "cards": [("Brent / WTI", "-5.2 / -5.4", "亞洲時段百分比"), ("TSMC", "2350-2355", "接近前收"), ("TraderXYZ", "$1.48B", "前十成交偏低")],
        "box1": ("3 個關鍵觀察", ["1. Brent 能否穩定低於 90 美元？", "2. TSMC 能否守住 2330-2350？", "3. 雲端業者能否兌現自由現金流？"]),
        "box2": ("本週框架", ["Microsoft / Meta 雲端增速與資本開支。", "Amazon AWS 與 Apple 盈利品質。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：風險緩和不等於解除，AI 行情將由雲端收入、資本開支和現金回報共同決定。",
    },
    "en": {
        "file": "market-brief-2026-07-27-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "Oil eases; cloud earnings must take over",
        "subtitle": "Risk conditions improve and TSMC stays resilient, but a thin rebound still needs capital-return proof from four technology mega-caps.",
        "cards": [("Brent / WTI", "-5.2 / -5.4", "Asia-session percent"), ("TSMC", "2350-2355", "near prior close"), ("TraderXYZ", "$1.48B", "thin top-ten volume")],
        "box1": ("3 key checks", ["1. Can Brent stay below $90?", "2. Can TSMC hold 2330-2350?", "3. Can cloud capex deliver free cash flow?"]),
        "box2": ("Weekly Frame", ["Microsoft / Meta cloud growth and capex.", "Amazon AWS and Apple earnings quality.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: risk relief is not resolution; cloud revenue, capex and cash returns will decide the AI trade.",
    },
    "ru": {
        "file": "market-brief-2026-07-27-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "Нефть падает, эстафета у облаков",
        "subtitle": "Риск снижается, TSMC устойчива; тонкий отскок должны подтвердить денежные результаты четырех гигантов.",
        "cards": [("Brent / WTI", "-5.2 / -5.4", "проценты в Азии"), ("TSMC", "2350-2355", "около прошлого закрытия"), ("TraderXYZ", "$1.48B", "низкий оборот десятки")],
        "box1": ("3 ключевых сигнала", ["1. Удержится ли Brent ниже $90?", "2. Удержит ли TSMC зону 2330-2350?", "3. Дадут ли облака свободный поток?"]),
        "box2": ("Рамка Недели", ["Рост облака и капзатраты Microsoft / Meta.", "AWS Amazon и качество прибыли Apple.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: ослабление риска не равно его снятию; AI определят облачная выручка, капзатраты и денежная отдача.",
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
