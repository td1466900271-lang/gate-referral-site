#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-03"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-03-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "AI 硬件链继续出清",
        "subtitle": "资金从硬件扩产转向平台变现、指数防御与局部 crypto beta。",
        "cards": [("MU", "1000-1050", "关键防守区"), ("TSM 台股", "2415-2500", "区间消化"), ("BTC / ETH", "修复", "风险偏好仍在")],
        "box1": ("3 个关键观察", ["1. MU 能否守住 1000-1050？", "2. TSM 能否重回 NT$2500？", "3. SKHX / SNDK / DRAM 是否止跌？"]),
        "box2": ("交易框架", ["硬件链继续洗筹。", "META 变现叙事更关键。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：不是全面避险，而是 AI 硬件拥挤交易继续降温。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-03-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "AI 硬體鏈繼續出清",
        "subtitle": "資金從硬體擴產轉向平台變現、指數防禦與局部 crypto beta。",
        "cards": [("MU", "1000-1050", "關鍵防守區"), ("TSM 台股", "2415-2500", "區間消化"), ("BTC / ETH", "修復", "風險偏好仍在")],
        "box1": ("3 個關鍵觀察", ["1. MU 能否守住 1000-1050？", "2. TSM 能否重回 NT$2500？", "3. SKHX / SNDK / DRAM 是否止跌？"]),
        "box2": ("交易框架", ["硬體鏈繼續洗籌。", "META 變現敘事更關鍵。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：不是全面避險，而是 AI 硬體擁擠交易繼續降溫。",
    },
    "en": {
        "file": "market-brief-2026-07-03-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "AI hardware keeps clearing",
        "subtitle": "Capital rotates from hardware buildout to platform monetization and selective crypto beta.",
        "cards": [("MU", "1000-1050", "key defense"), ("TSM TW", "2415-2500", "digestion zone"), ("BTC / ETH", "rebound", "risk appetite alive")],
        "box1": ("3 key checks", ["1. Can MU hold 1000-1050?", "2. Can TSM reclaim NT$2500?", "3. Do SKHX / SNDK / DRAM stop falling?"]),
        "box2": ("Framework", ["Hardware is still washing out.", "META monetization matters more.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: not broad risk-off; crowded AI hardware is still cooling.",
    },
    "ru": {
        "file": "market-brief-2026-07-03-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "AI hardware продолжает чистку",
        "subtitle": "Капитал уходит из hardware buildout в монетизацию платформ и выборочный crypto beta.",
        "cards": [("MU", "1000-1050", "ключевая защита"), ("TSM TW", "2415-2500", "зона переваривания"), ("BTC / ETH", "отскок", "аппетит к риску")],
        "box1": ("3 ключевых сигнала", ["1. Удержит ли MU 1000-1050?", "2. Вернет ли TSM NT$2500?", "3. Остановят ли падение SKHX / SNDK / DRAM?"]),
        "box2": ("Рамка", ["Hardware продолжает чистку.", "Монетизация META важнее.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: это не широкий risk-off; перегретый AI hardware продолжает остывать.",
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
