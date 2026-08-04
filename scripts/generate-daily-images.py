#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-08-04"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-08-04-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "美股修复，亚洲芯片仍在去拥挤",
        "subtitle": "油价回落推动美股接近新高，但台积电与存储合约承压；AI交易转向盈利兑现。",
        "cards": [("S&P 500", "+1.5%", "距历史高点约 0.1%"), ("TAIEX / TSMC", "-0.4 / -1.9", "亚洲午间变化"), ("TraderXYZ", "$3.70B", "前十成交增 148%")],
        "box1": ("3 个关键观察", ["1. TSMC 2300 能否承接？", "2. 存储卖压能否收敛？", "3. 油价与 JOLTS 如何定价？"]),
        "box2": ("风险框架", ["指数偏强，芯片内部分化。", "成交放大不等于全面看多。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：AI基础设施周期未结束，但高预期与高波动并存，超额收益更依赖盈利兑现。",
    },
    "zh-hant": {
        "file": "market-brief-2026-08-04-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "美股修復，亞洲晶片仍在去擁擠",
        "subtitle": "油價回落推動美股接近新高，但台積電與記憶體合約承壓；AI交易轉向盈利兌現。",
        "cards": [("S&P 500", "+1.5%", "距歷史高點約 0.1%"), ("TAIEX / TSMC", "-0.4 / -1.9", "亞洲午間變化"), ("TraderXYZ", "$3.70B", "前十成交增 148%")],
        "box1": ("3 個關鍵觀察", ["1. TSMC 2300 能否承接？", "2. 記憶體賣壓能否收斂？", "3. 油價與 JOLTS 如何定價？"]),
        "box2": ("風險框架", ["指數偏強，晶片內部分化。", "成交放大不等於全面看多。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：AI基礎設施週期未結束，但高預期與高波動並存，超額收益更依賴盈利兌現。",
    },
    "en": {
        "file": "market-brief-2026-08-04-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "U.S. rebounds; Asia chips remain crowded",
        "title_size": 46,
        "subtitle": "Lower oil lifts U.S. stocks near records, while TSMC and memory lag; AI leadership shifts toward proven earnings.",
        "cards": [("S&P 500", "+1.5%", "about 0.1% below record"), ("TAIEX / TSMC", "-0.4 / -1.9", "Asia midday change, %"), ("TraderXYZ", "$3.70B", "top-ten volume +148%")],
        "box1": ("3 key checks", ["1. Does TSMC hold 2300?", "2. Does memory selling ease?", "3. How do oil and JOLTS reprice?"]),
        "box2": ("Risk Frame", ["Indices firm; chips diverge inside.", "More volume is not broad bullishness.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: the AI infrastructure cycle continues, but high expectations and volatility make earnings delivery decisive.",
        "bottom_width": 78,
    },
    "ru": {
        "file": "market-brief-2026-08-04-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "США растут, чипы Азии под давлением",
        "title_size": 42,
        "subtitle": "Дешевая нефть поддержала США, но TSMC и память слабы; рынку нужна прибыль от AI.",
        "subtitle_width": 42,
        "cards": [("S&P 500", "+1.5%", "около 0,1% до рекорда"), ("TAIEX / TSMC", "-0.4 / -1.9", "изменение в Азии, %"), ("TraderXYZ", "$3.70B", "оборот +148%")],
        "box1": ("3 ключевых сигнала", ["1. Удержит ли TSMC уровень 2300?", "2. Ослабнет ли продажа памяти?", "3. Как нефть и JOLTS изменят ставки?"]),
        "box2": ("Рамка риска", ["Индексы сильны, чипы расходятся.", "Рост оборота не значит общий оптимизм.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: цикл AI продолжается, но высокая оценка и волатильность требуют реальной прибыли.",
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
