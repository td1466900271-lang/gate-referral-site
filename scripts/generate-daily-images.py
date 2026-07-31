#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-31"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-31-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "业绩验证触发亚洲芯片抢筹",
        "subtitle": "TSMC 与云厂确认需求强劲，但极端涨幅包含空头回补。",
        "cards": [("KOSPI", "+17.9%", "历史最大单日涨幅"), ("TAIEX / TSMC", "+8.0 / +10.0", "百分比变化"), ("TraderXYZ", "$6.24B", "前十名义成交")],
        "box1": ("3 个关键观察", ["1. 美国现货能否继续确认？", "2. TSMC 缺口与外资流向如何？", "3. 云厂资本开支能否兑现回报？"]),
        "box2": ("风险框架", ["方向可信，涨幅含空头回补。", "高利率仍压制极端估值。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：AI 需求仍强，单日暴涨仍需现货、盈利与现金流确认。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-31-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "業績驗證觸發亞洲晶片搶籌",
        "subtitle": "TSMC 與雲端業者確認需求強勁，但極端漲幅包含空頭回補。",
        "cards": [("KOSPI", "+17.9%", "歷史最大單日漲幅"), ("TAIEX / TSMC", "+8.0 / +10.0", "百分比變化"), ("TraderXYZ", "$6.24B", "前十名義成交")],
        "box1": ("3 個關鍵觀察", ["1. 美國現貨能否繼續確認？", "2. TSMC 缺口與外資流向如何？", "3. 雲端資本開支能否兌現回報？"]),
        "box2": ("風險框架", ["方向可信，漲幅含空頭回補。", "高利率仍壓制極端估值。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：AI 需求仍強，單日暴漲仍需現貨、盈利與現金流確認。",
    },
    "en": {
        "file": "market-brief-2026-07-31-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "Earnings revive demand for Asian chips",
        "title_size": 48,
        "subtitle": "TSMC and cloud data confirm firm demand, but 20%-30% gains also reflect short covering and a liquidity shock.",
        "cards": [("KOSPI", "+17.9%", "record daily gain"), ("TAIEX / TSMC", "+8.0 / +10.0", "change, %"), ("TraderXYZ", "$6.24B", "top-ten notional")],
        "box1": ("3 key checks", ["1. Does U.S. cash keep confirming?", "2. How do TSMC's gap and flows behave?", "3. Can cloud capex produce returns?"]),
        "box2": ("Risk Frame", ["Signal firm; short covering boosts it.", "High yields still cap valuations.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: AI demand is firm, but the surge needs confirmation from cash trading, earnings and free cash flow.",
        "bottom_width": 78,
    },
    "ru": {
        "file": "market-brief-2026-07-31-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "Отчеты вернули спрос на чипы Азии",
        "title_size": 44,
        "subtitle": "TSMC и облака подтверждают спрос; рост на 20%-30% усилен закрытием шортов.",
        "subtitle_width": 42,
        "cards": [("KOSPI", "+17.9%", "рекордный рост"), ("TAIEX / TSMC", "+8.0 / +10.0", "изменение, %"), ("TraderXYZ", "$6.24B", "оборот десятки")],
        "box1": ("3 ключевых сигнала", ["1. Подтвердят ли рост акции США?", "2. Что покажут гэп и потоки TSMC?", "3. Окупятся ли капзатраты облаков?"]),
        "box2": ("Рамка риска", ["Сигнал силен; шорты помогли.", "Ставки давят на оценки.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: спрос на AI силен, но рост должны подтвердить акции, прибыль и денежный поток.",
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
