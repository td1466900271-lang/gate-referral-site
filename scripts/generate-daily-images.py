#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-08-18"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-08-18-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "消费转弱，存储与设备逆势走强",
        "subtitle": "油价突破90美元、长债收益率升至4.72%；AI资金从平台股转向存储与设备瓶颈。",
        "cards": [("S&P 500", "-0.5%", "消费与利率承压"), ("TAIEX / TSMC", "-1.0 / -0.8", "亚洲午间变化，%"), ("TraderXYZ", "$2.88B", "前十工作日成交")],
        "box1": ("3 个关键观察", ["1. TSMC 2375 能否形成承接？", "2. Brent 能否回到 90 美元下方？", "3. MU / AMAT 能否继续跑赢？"]),
        "box2": ("风险框架", ["弱消费正转化为盈利风险。", "油价与长端利率同步上行。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：AI资本开支未见顶，但市场开始奖励存储与设备瓶颈，并重新审视平台公司的现金回报。",
    },
    "zh-hant": {
        "file": "market-brief-2026-08-18-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "消費轉弱，記憶體與設備逆勢走強",
        "subtitle": "油價突破90美元、長債殖利率升至4.72%；AI資金從平台股轉向記憶體與設備瓶頸。",
        "cards": [("S&P 500", "-0.5%", "消費與利率承壓"), ("TAIEX / TSMC", "-1.0 / -0.8", "亞洲午間變化，%"), ("TraderXYZ", "$2.88B", "前十工作日成交")],
        "box1": ("3 個關鍵觀察", ["1. TSMC 2375 能否形成承接？", "2. Brent 能否回到 90 美元下方？", "3. MU / AMAT 能否繼續跑贏？"]),
        "box2": ("風險框架", ["弱消費正轉化為盈利風險。", "油價與長端殖利率同步上行。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：AI資本開支未見頂，但市場開始獎勵記憶體與設備瓶頸，並重新審視平台公司的現金回報。",
    },
    "en": {
        "file": "market-brief-2026-08-18-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "Weak consumption shifts AI capital to bottlenecks",
        "title_size": 46,
        "subtitle": "Oil clears $90 and the 10-year reaches 4.72% as AI capital rotates from platforms toward memory and equipment.",
        "cards": [("S&P 500", "-0.5%", "demand-rate pressure"), ("TAIEX / TSMC", "-1.0 / -0.8", "Asia midday change, %"), ("TraderXYZ", "$2.88B", "weekday top-ten volume")],
        "box1": ("3 key checks", ["1. Can TSMC hold TWD 2375?", "2. Can Brent fall back below $90?", "3. Do MU / AMAT keep outperforming?"]),
        "box2": ("Risk Frame", ["Weak consumption now threatens earnings.", "Oil and long yields rise together.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: AI capex remains intact, but markets reward memory and equipment while reassessing platform cash returns.",
        "bottom_width": 78,
    },
    "ru": {
        "file": "market-brief-2026-08-18-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "Слабый спрос ведет AI к узким местам",
        "title_size": 42,
        "subtitle": "Нефть выше $90, ставка США 4,72%; капитал идет от платформ к памяти и оборудованию.",
        "subtitle_width": 56,
        "cards": [("S&P 500", "-0.5%", "давление ставок"), ("TAIEX / TSMC", "-1.0 / -0.8", "Азия в полдень, %"), ("TraderXYZ", "$2.88B", "оборот топ-10")],
        "box1": ("3 ключевых сигнала", ["1. Удержит ли TSMC уровень 2375?", "2. Вернется ли Brent ниже $90?", "3. Сохранят ли MU / AMAT лидерство?"]),
        "box2": ("Рамка риска", ["Слабый спрос угрожает прибыли.", "Нефть и длинные ставки растут вместе.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: капзатраты AI сильны, но рынок выбирает память и оборудование и проверяет денежную отдачу платформ.",
        "bottom_width": 62,
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
