#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-23"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-23-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "AI 需求确认，资本回报开始分化",
        "subtitle": "Google Cloud 高增长且算力受限，但资本开支超过经营现金流，供应链受益与云厂估值压力并存。",
        "cards": [("Google Cloud", "+82%", "收入同比增长"), ("CapEx / OCF", "44.9 / 39.1", "十亿美元"), ("Free Cash Flow", "-5.86B", "季度转负")],
        "box1": ("3 个关键观察", ["1. GOOGL 能否收复盘后跌幅？", "2. TSMC 能否守住 2370？", "3. Brent 是否站稳 95 美元？"]),
        "box2": ("分化框架", ["上游订单与定价权受益。", "云厂需证明现金回报。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：AI 资本开支尚未见顶，投资重点从规模增长转向订单、利润率与自由现金流。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-23-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "AI 需求確認，資本回報開始分化",
        "subtitle": "Google Cloud 高增長且算力受限，但資本開支超過經營現金流，供應鏈受益與雲端業者估值壓力並存。",
        "cards": [("Google Cloud", "+82%", "收入年增"), ("CapEx / OCF", "44.9 / 39.1", "十億美元"), ("Free Cash Flow", "-5.86B", "季度轉負")],
        "box1": ("3 個關鍵觀察", ["1. GOOGL 能否收復盤後跌幅？", "2. TSMC 能否守住 2370？", "3. Brent 是否站穩 95 美元？"]),
        "box2": ("分化框架", ["上游訂單與定價權受益。", "雲端業者需證明現金回報。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：AI 資本開支尚未見頂，投資重點從規模增長轉向訂單、利潤率與自由現金流。",
    },
    "en": {
        "file": "market-brief-2026-07-23-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "AI demand confirmed; capital returns diverge",
        "subtitle": "Google Cloud surges as compute stays constrained, but capex exceeds operating cash flow, splitting supplier upside from hyperscaler valuation pressure.",
        "cards": [("Google Cloud", "+82%", "year-on-year growth"), ("CapEx / OCF", "44.9 / 39.1", "USD billions"), ("Free Cash Flow", "-5.86B", "quarter turns negative")],
        "box1": ("3 key checks", ["1. Can GOOGL recover its post-call loss?", "2. Can TSMC hold 2370?", "3. Does Brent hold above $95?"]),
        "box2": ("Divergence Frame", ["Upstream orders and pricing benefit.", "Cloud buyers must prove cash returns.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: AI capex has not peaked; focus shifts from spending scale to orders, margin and free cash flow.",
    },
    "ru": {
        "file": "market-brief-2026-07-23-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "AI-спрос силен, капитал под давлением",
        "subtitle": "Google Cloud растет, но капзатраты выше денежного потока: поставщики и облачные оценки расходятся.",
        "cards": [("Google Cloud", "+82%", "рост год к году"), ("Капзатраты / OCF", "44.9 / 39.1", "миллиарды USD"), ("Свободный Поток", "-5.86B", "отрицательный квартал")],
        "box1": ("3 ключевых сигнала", ["1. Вернет ли GOOGL падение после отчета?", "2. Удержит ли TSMC уровень 2370?", "3. Удержится ли Brent выше $95?"]),
        "box2": ("Рамка Расхождения", ["Заказы и ценовая сила помогают поставщикам.", "Облака должны доказать денежную отдачу.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: пик AI-капзатрат не пройден; фокус смещается к заказам, марже и свободному денежному потоку.",
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
