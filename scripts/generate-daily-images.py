#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-01"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-01-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "AI 半导体再次确认",
        "subtitle": "TSM 与设备链领涨，记忆体进入换手而非破坏。",
        "cards": [("TSM 台股", "NT$2490", "观察 2500"), ("MU", "1130-1150", "关键支撑区"), ("SMH / SOXX", "+3.8% / +4.1%", "广度改善")],
        "box1": ("3 个关键观察", ["1. TSM 能否站稳 NT$2500？", "2. MU 能否守住 1130-1150？", "3. AMAT / ASML 是否确认 AI CapEx？"]),
        "box2": ("交易框架", ["选择性强势，不是全面 risk-on。", "等待确认，不追情绪高点。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：AI 瓶颈资产中期仍偏强，但短线不适合无差别追涨。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-01-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "AI 半導體再次確認",
        "subtitle": "TSM 與設備鏈領漲，記憶體進入換手而非破壞。",
        "cards": [("TSM 台股", "NT$2490", "觀察 2500"), ("MU", "1130-1150", "關鍵支撐區"), ("SMH / SOXX", "+3.8% / +4.1%", "廣度改善")],
        "box1": ("3 個關鍵觀察", ["1. TSM 能否站穩 NT$2500？", "2. MU 能否守住 1130-1150？", "3. AMAT / ASML 是否確認 AI CapEx？"]),
        "box2": ("交易框架", ["選擇性強勢，不是全面 risk-on。", "等待確認，不追情緒高點。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：AI 瓶頸資產中期仍偏強，但短線不適合無差別追漲。",
    },
    "en": {
        "file": "market-brief-2026-07-01-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "AI semis confirm again",
        "subtitle": "TSM and equipment lead; memory is rotating, not breaking.",
        "cards": [("TSM TW", "NT$2490", "watch 2500"), ("MU", "1130-1150", "support zone"), ("SMH / SOXX", "+3.8% / +4.1%", "breadth improves")],
        "box1": ("3 key checks", ["1. Can TSM hold above NT$2500?", "2. Does MU keep 1130-1150 support?", "3. Do AMAT / ASML confirm AI CapEx?"]),
        "box2": ("Framework", ["Selective strength, not broad risk-on.", "Wait for confirmation.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: AI bottleneck assets remain constructive, but chasing is not the base case.",
    },
    "ru": {
        "file": "market-brief-2026-07-01-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "AI-чипы подтверждаются",
        "subtitle": "TSM и оборудование лидируют; память ротируется, а не ломается.",
        "cards": [("TSM TW", "NT$2490", "уровень 2500"), ("MU", "1130-1150", "зона поддержки"), ("SMH / SOXX", "+3.8% / +4.1%", "ширина лучше")],
        "box1": ("3 ключевых сигнала", ["1. Удержит ли TSM NT$2500?", "2. Удержит ли MU 1130-1150?", "3. Подтвердят ли AMAT / ASML AI CapEx?"]),
        "box2": ("Рамка", ["Выборочная сила, не широкий risk-on.", "Ждать подтверждения.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: AI bottleneck assets конструктивны, но погоня за ростом не базовый сценарий.",
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
