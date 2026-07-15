#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-15"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-15-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "半导体强力修复",
        "subtitle": "低 CPI 提供缓冲，台股与存储链反弹，但拥挤度与油价风险仍在。",
        "cards": [("TAIEX", "+2.2%", "广泛修复"), ("SKHX / SKHY", "+21% / +24%", "存储回补"), ("NVDA / AMD", "+4.4% / +3.9%", "GPU 稳健")],
        "box1": ("3 个关键观察", ["1. 台股能否稳住 45500？", "2. 存储反弹能否获得现货确认？", "3. 油价是否抵消 CPI 利好？"]),
        "box2": ("验证窗口", ["ASML 关注净订单。", "TSMC 关注指引与毛利率。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：技术修复强劲，但需要订单、成交与盈利上修完成确认。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-15-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "半導體強力修復",
        "subtitle": "低 CPI 提供緩衝，台股與記憶體鏈反彈，但擁擠度與油價風險仍在。",
        "cards": [("TAIEX", "+2.2%", "廣泛修復"), ("SKHX / SKHY", "+21% / +24%", "記憶體回補"), ("NVDA / AMD", "+4.4% / +3.9%", "GPU 穩健")],
        "box1": ("3 個關鍵觀察", ["1. 台股能否穩住 45500？", "2. 記憶體反彈能否獲得現貨確認？", "3. 油價是否抵消 CPI 利好？"]),
        "box2": ("驗證窗口", ["ASML 關注淨訂單。", "TSMC 關注指引與毛利率。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：技術修復強勁，但需要訂單、成交與盈利上修完成確認。",
    },
    "en": {
        "file": "market-brief-2026-07-15-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "Semiconductors rebound sharply",
        "subtitle": "Cooler CPI supports Taiwan and memory, but crowded positioning and elevated oil keep risk high.",
        "cards": [("TAIEX", "+2.2%", "broad repair"), ("SKHX / SKHY", "+21% / +24%", "memory covering"), ("NVDA / AMD", "+4.4% / +3.9%", "steady GPU")],
        "box1": ("3 key checks", ["1. Can TAIEX hold 45500?", "2. Does cash trading confirm memory?", "3. Does oil offset the CPI relief?"]),
        "box2": ("Validation Window", ["ASML: watch net bookings.", "TSMC: watch guidance and margin.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: technical repair is strong, but orders, volume and earnings upgrades must confirm it.",
    },
    "ru": {
        "file": "market-brief-2026-07-15-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "Чипы резко отскакивают",
        "subtitle": "Низкий CPI поддерживает Тайвань и память, но перегретые позиции и дорогая нефть сохраняют риск.",
        "cards": [("TAIEX", "+2.2%", "широкое восстановление"), ("SKHX / SKHY", "+21% / +24%", "закрытие в памяти"), ("NVDA / AMD", "+4.4% / +3.9%", "стабильные GPU")],
        "box1": ("3 ключевых сигнала", ["1. Удержит ли TAIEX 45500?", "2. Подтвердит ли спот отскок памяти?", "3. Нейтрализует ли нефть эффект CPI?"]),
        "box2": ("Окно Проверки", ["ASML: следите за заказами.", "TSMC: прогноз и маржа.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: отскок силен, но его должны подтвердить заказы, объем и прогнозы прибыли.",
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
