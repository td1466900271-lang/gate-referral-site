#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-09"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-09-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "龙头抱团 + 能源压估值",
        "subtitle": "AI 半导体未崩，但全链条 beta 已转向龙头抱团与存储链去拥挤。",
        "cards": [("TSM 台股", "2430-2460", "2500 压力"), ("NVDA", "+3.0%", "相对强"), ("CL / Brent", "+3%~4%", "油价压力")],
        "box1": ("3 个关键观察", ["1. TSMC 能否守住 2400-2420？", "2. MU 能否重新站上 950-1000？", "3. CL / BRENTOIL 是否继续推升利率压力？"]),
        "box2": ("交易框架", ["中期 AI 主线仍在。", "短线不是全链条普涨。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：资金抱团确定性龙头，存储链降拥挤，油价上行压制科技估值。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-09-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "龍頭抱團 + 能源壓估值",
        "subtitle": "AI 半導體未崩，但全鏈條 beta 已轉向龍頭抱團與記憶體鏈去擁擠。",
        "cards": [("TSM 台股", "2430-2460", "2500 壓力"), ("NVDA", "+3.0%", "相對強"), ("CL / Brent", "+3%~4%", "油價壓力")],
        "box1": ("3 個關鍵觀察", ["1. TSMC 能否守住 2400-2420？", "2. MU 能否重新站上 950-1000？", "3. CL / BRENTOIL 是否繼續推升利率壓力？"]),
        "box2": ("交易框架", ["中期 AI 主線仍在。", "短線不是全鏈條普漲。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：資金抱團確定性龍頭，記憶體鏈降擁擠，油價上行壓制科技估值。",
    },
    "en": {
        "file": "market-brief-2026-07-09-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "Leaders cluster as oil pressures valuations",
        "subtitle": "AI semis are not broken, but full-chain beta has shifted to leaders and memory de-crowding.",
        "cards": [("TSM TW", "2430-2460", "2500 resistance"), ("NVDA", "+3.0%", "relative strength"), ("CL / Brent", "+3%~4%", "oil pressure")],
        "box1": ("3 key checks", ["1. Can TSMC hold 2400-2420?", "2. Can MU reclaim 950-1000?", "3. Do CL / BRENTOIL keep lifting rate pressure?"]),
        "box2": ("Framework", ["Medium-term AI remains intact.", "Short term is not full-chain beta.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: capital is clustering around certainty, memory is de-crowding, and oil pressures tech valuations.",
    },
    "ru": {
        "file": "market-brief-2026-07-09-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "Лидеры в фокусе, нефть давит",
        "subtitle": "AI-сектор не сломан, но широкий beta перешел к лидерам и снижению перегрева памяти.",
        "cards": [("TSM TW", "2430-2460", "сопротивление 2500"), ("NVDA", "+3.0%", "относительная сила"), ("CL / Brent", "+3%~4%", "давление нефти")],
        "box1": ("3 ключевых сигнала", ["1. Удержит ли TSMC 2400-2420?", "2. Вернет ли MU 950-1000?", "3. Продолжит ли нефть давить на ставки?"]),
        "box2": ("Рамка", ["Среднесрочный AI-тренд жив.", "Краткосрочно это не широкий beta.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: капитал выбирает лидеров, цепочка памяти снижает перегрев, а нефть давит на оценки.",
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
