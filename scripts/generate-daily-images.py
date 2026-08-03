#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-08-03"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-08-03-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "AI资本开支仍强，市场转向回报验证",
        "subtitle": "台股指数强、台积电弱，存储追涨降温；资金重新审视盈利、现金流与估值。",
        "cards": [("TAIEX / TSMC", "+0.6 / -1.9", "百分比变化"), ("KOSPI", "-4.3%", "回吐极端反弹"), ("TraderXYZ", "$1.49B", "前十成交降 76%")],
        "box1": ("3 个关键观察", ["1. TSMC 能否收复 2400？", "2. MU 现货与期权是否企稳？", "3. 就业与收益率如何定价？"]),
        "box2": ("风险框架", ["AI 投入仍强，追涨拥挤度下降。", "收入与现金流决定估值。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：基础设施周期仍在扩张，但市场只奖励能够兑现收入、利润与现金流的投入。",
    },
    "zh-hant": {
        "file": "market-brief-2026-08-03-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "AI資本開支仍強，市場轉向回報驗證",
        "subtitle": "台股指數強、台積電弱，記憶體追漲降溫；資金重新審視盈利、現金流與估值。",
        "cards": [("TAIEX / TSMC", "+0.6 / -1.9", "百分比變化"), ("KOSPI", "-4.3%", "回吐極端反彈"), ("TraderXYZ", "$1.49B", "前十成交降 76%")],
        "box1": ("3 個關鍵觀察", ["1. TSMC 能否收復 2400？", "2. MU 現貨與期權是否企穩？", "3. 就業與殖利率如何定價？"]),
        "box2": ("風險框架", ["AI 投入仍強，追漲擁擠度下降。", "收入與現金流決定估值。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：基礎設施週期仍在擴張，但市場只獎勵能夠兌現收入、利潤與現金流的投入。",
    },
    "en": {
        "file": "market-brief-2026-08-03-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "AI capex grows; returns take center stage",
        "title_size": 46,
        "subtitle": "Taiwan's index rises as TSMC falls and memory momentum cools; profit, cash flow and valuation regain focus.",
        "cards": [("TAIEX / TSMC", "+0.6 / -1.9", "change, %"), ("KOSPI", "-4.3%", "rebound fades"), ("TraderXYZ", "$1.49B", "top-ten volume -76%")],
        "box1": ("3 key checks", ["1. Can TSMC reclaim 2400?", "2. Do MU cash and options stabilize?", "3. How do jobs and yields reprice?"]),
        "box2": ("Risk Frame", ["AI spending is firm; crowding cools.", "Revenue and cash flow set valuation.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: infrastructure still expands, but markets reward only capex that converts into revenue, profit and free cash flow.",
        "bottom_width": 78,
    },
    "ru": {
        "file": "market-brief-2026-08-03-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "AI-капзатраты растут; важна отдача",
        "title_size": 44,
        "subtitle": "Тайвань растет, TSMC падает, память остывает; рынок снова смотрит на прибыль.",
        "subtitle_width": 42,
        "cards": [("TAIEX / TSMC", "+0.6 / -1.9", "изменение, %"), ("KOSPI", "-4.3%", "отскок слабеет"), ("TraderXYZ", "$1.49B", "оборот -76%")],
        "box1": ("3 ключевых сигнала", ["1. Вернется ли TSMC выше 2400?", "2. Стабилизируются ли MU и опционы?", "3. Что покажут занятость и ставки?"]),
        "box2": ("Рамка риска", ["AI-расходы сильны; перегрев снижен.", "Выручка и поток задают оценку.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: цикл растет, но рынок награждает лишь капзатраты с выручкой, прибылью и потоком.",
        "bottom_width": 45,
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

  {text_line(70, 154, data["title"], data.get("title_size", 54), "#f5f9ff", "800", "Inter, Arial, sans-serif")}
  {paragraph(70, 212, lines(data["subtitle"], data.get("subtitle_width", 58)), 25, 34, "#c8dcf8")}

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

  {paragraph(70, 625, lines(data["bottom"], data.get("bottom_width", 88)), 22, 28, "#45b7ff", "800")}
</svg>
'''


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for data in IMAGES.values():
        (OUT / data["file"]).write_text(svg(data), encoding="utf-8")
    print(f"Generated {len(IMAGES)} localized blue SVG daily images.")


if __name__ == "__main__":
    main()
