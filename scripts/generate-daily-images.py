#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-16"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-16-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "ASML 强指引，存储去杠杆",
        "subtitle": "设备需求与存储交易继续分化，台积电法说将验证资本开支回报。",
        "cards": [("ASML", "EUR43-45B", "2026 收入指引"), ("SKHX / SKHY", "-13.9% / -11.0%", "存储去杠杆"), ("TSMC", "2420-2455", "法说前观望")],
        "box1": ("3 个关键观察", ["1. TSMC 毛利率与资本开支？", "2. 存储现货是否确认跌幅？", "3. 油价是否抵消通胀降温？"]),
        "box2": ("产业框架", ["ASML 订单与产能强。", "存储中期积极、短期谨慎。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：产业需求仍强，股票交易更重视订单、毛利率与回报兑现。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-16-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "ASML 強指引，記憶體去槓桿",
        "subtitle": "設備需求與記憶體交易繼續分化，台積電法說將驗證資本開支回報。",
        "cards": [("ASML", "EUR43-45B", "2026 收入指引"), ("SKHX / SKHY", "-13.9% / -11.0%", "記憶體去槓桿"), ("TSMC", "2420-2455", "法說前觀望")],
        "box1": ("3 個關鍵觀察", ["1. TSMC 毛利率與資本開支？", "2. 記憶體現貨是否確認跌幅？", "3. 油價是否抵消通膨降溫？"]),
        "box2": ("產業框架", ["ASML 訂單與產能強。", "記憶體中期積極、短期謹慎。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：產業需求仍強，股票交易更重視訂單、毛利率與回報兌現。",
    },
    "en": {
        "file": "market-brief-2026-07-16-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "ASML strong, memory de-leverages",
        "subtitle": "Equipment demand and memory trading diverge as TSMC's call tests the return on AI capex.",
        "cards": [("ASML", "EUR43-45B", "2026 revenue guide"), ("SKHX / SKHY", "-13.9% / -11.0%", "memory de-leveraging"), ("TSMC", "2420-2455", "pre-call caution")],
        "box1": ("3 key checks", ["1. TSMC margin and capex?", "2. Does cash memory confirm losses?", "3. Does oil offset disinflation?"]),
        "box2": ("Industry Frame", ["ASML orders and capacity are strong.", "Memory: constructive, near-term cautious.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: industry demand is firm, while equities demand real delivery in orders, margin and returns.",
    },
    "ru": {
        "file": "market-brief-2026-07-16-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "ASML силен, память снижает плечо",
        "subtitle": "Спрос на оборудование и торговля памятью расходятся; звонок TSMC проверит отдачу AI-капзатрат.",
        "cards": [("ASML", "EUR43-45B", "прогноз выручки 2026"), ("SKHX / SKHY", "-13.9% / -11.0%", "снижение плеча памяти"), ("TSMC", "2420-2455", "осторожность перед звонком")],
        "box1": ("3 ключевых сигнала", ["1. Маржа и капзатраты TSMC?", "2. Подтвердит ли спот падение памяти?", "3. Нейтрализует ли нефть дезинфляцию?"]),
        "box2": ("Отраслевая Рамка", ["ASML: сильные заказы и мощности.", "Память: срок позитивен, краткосрочно осторожно.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: спрос силен, но акциям нужна реальная отдача в заказах, марже и доходности.",
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
