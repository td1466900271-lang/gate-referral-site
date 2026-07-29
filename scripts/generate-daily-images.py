#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-29"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-29-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "亚洲芯片二次去杠杆",
        "subtitle": "纪录业绩仍低于极高预期，市场从需求强弱转向估值、杠杆与 AI 资本回报。",
        "cards": [("KOSPI", "-8.2%", "连续流动性压力"), ("TAIEX / TSMC", "-4.9 / -4.2", "百分比变化"), ("TraderXYZ", "$6.03B", "前十名义成交")],
        "box1": ("3 个关键观察", ["1. TSMC 能否守住 2185？", "2. 韩国能否停止流动性踩踏？", "3. MSFT / META 能否验证回报？"]),
        "box2": ("风险框架", ["方向可信，永续跌幅被放大。", "Fed 与云财报决定下一节点。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：AI 需求未消失，但强业绩已不足以支撑极端估值；反转仍需现货、现金流与盈利确认。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-29-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "亞洲晶片二次去槓桿",
        "subtitle": "紀錄業績仍低於極高預期，市場從需求強弱轉向估值、槓桿與 AI 資本回報。",
        "cards": [("KOSPI", "-8.2%", "連續流動性壓力"), ("TAIEX / TSMC", "-4.9 / -4.2", "百分比變化"), ("TraderXYZ", "$6.03B", "前十名義成交")],
        "box1": ("3 個關鍵觀察", ["1. TSMC 能否守住 2185？", "2. 韓國能否停止流動性踩踏？", "3. MSFT / META 能否驗證回報？"]),
        "box2": ("風險框架", ["方向可信，永續跌幅被放大。", "Fed 與雲端財報決定下一節點。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：AI 需求未消失，但強業績已不足以支撐極端估值；反轉仍需現貨、現金流與盈利確認。",
    },
    "en": {
        "file": "market-brief-2026-07-29-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "Asian chips enter a second de-leveraging wave",
        "title_size": 48,
        "subtitle": "Record results still miss extreme expectations as markets reprice valuation, leverage and returns on AI capital.",
        "cards": [("KOSPI", "-8.2%", "liquidity stress"), ("TAIEX / TSMC", "-4.9 / -4.2", "change, %"), ("TraderXYZ", "$6.03B", "top-ten notional")],
        "box1": ("3 key checks", ["1. Can TSMC hold 2185?", "2. Can Korean liquidity stabilize?", "3. Can MSFT / META prove returns?"]),
        "box2": ("Risk Frame", ["Direction credible; perps amplify moves.", "Fed and cloud earnings set the next node.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: AI demand remains, but strong results no longer justify extreme valuations; cash trading and earnings must confirm a turn.",
        "bottom_width": 78,
    },
    "ru": {
        "file": "market-brief-2026-07-29-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "Вторая волна снижения плеча в Азии",
        "title_size": 44,
        "subtitle": "Рекордные итоги ниже ожиданий: рынок снижает оценки, плечо и отдачу AI.",
        "subtitle_width": 42,
        "cards": [("KOSPI", "-8.2%", "стресс ликвидности"), ("TAIEX / TSMC", "-4.9 / -4.2", "изменение, %"), ("TraderXYZ", "$6.03B", "оборот десятки")],
        "box1": ("3 ключевых сигнала", ["1. Удержит ли TSMC уровень 2185?", "2. Стабилизируется ли Корея?", "3. Докажут ли MSFT / META отдачу?"]),
        "box2": ("Рамка риска", ["Сигнал верен; плечо усиливает.", "ФРС и отчеты зададут шаг.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: спрос на AI есть, но оценки высоки. Разворот подтвердят акции и отчеты.",
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
