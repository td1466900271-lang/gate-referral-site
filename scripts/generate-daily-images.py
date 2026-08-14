#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-08-14"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-08-14-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "通胀降温，AI资金转向存储链",
        "subtitle": "美股再创新高，台股冲高回落；MU、SNDK与DRAM升温，零售销售检验软着陆。",
        "cards": [("S&P 500", "+0.7%", "再创历史新高"), ("TAIEX / TSMC", "-0.1 / -0.4", "亚洲午间变化，%"), ("TraderXYZ", "$3.07B", "前十成交增 38%")],
        "box1": ("3 个关键观察", ["1. TSMC 能否守住 2435-2440？", "2. 零售与预期是否支持软着陆？", "3. 存储涨幅能否获现货确认？"]),
        "box2": ("风险框架", ["通胀降温缓解短期政策压力。", "高估值与杠杆风险仍在。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：AI瓶颈向HBM与存储扩散，但消费、核心PCE与美股现货成交仍需继续确认。",
    },
    "zh-hant": {
        "file": "market-brief-2026-08-14-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "通膨降溫，AI資金轉向記憶體鏈",
        "subtitle": "美股再創新高，台股衝高回落；MU、SNDK與DRAM升溫，零售銷售檢驗軟著陸。",
        "cards": [("S&P 500", "+0.7%", "再創歷史新高"), ("TAIEX / TSMC", "-0.1 / -0.4", "亞洲午間變化，%"), ("TraderXYZ", "$3.07B", "前十成交增 38%")],
        "box1": ("3 個關鍵觀察", ["1. TSMC 能否守住 2435-2440？", "2. 零售與預期是否支持軟著陸？", "3. 記憶體漲幅能否獲現貨確認？"]),
        "box2": ("風險框架", ["通膨降溫緩解短期政策壓力。", "高估值與槓桿風險仍在。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：AI瓶頸向HBM與記憶體擴散，但消費、核心PCE與美股現貨成交仍需繼續確認。",
    },
    "en": {
        "file": "market-brief-2026-08-14-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "Cooling inflation shifts AI capital to memory",
        "title_size": 46,
        "subtitle": "U.S. stocks hit a record as Taiwan fades; MU, SNDK and DRAM heat up before the retail-sales test.",
        "cards": [("S&P 500", "+0.7%", "new record close"), ("TAIEX / TSMC", "-0.1 / -0.4", "Asia midday change, %"), ("TraderXYZ", "$3.07B", "top-ten volume, +38%")],
        "box1": ("3 key checks", ["1. Can TSMC hold 2435-2440?", "2. Do retail sales support a soft landing?", "3. Does cash confirm the memory rally?"]),
        "box2": ("Risk Frame", ["Cooling inflation eases policy pressure.", "Valuation and leverage risks remain.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: AI bottlenecks spread into HBM and memory, but consumption, core PCE and cash volume still need to confirm.",
        "bottom_width": 78,
    },
    "ru": {
        "file": "market-brief-2026-08-14-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "Инфляция остыла, капитал идет в память",
        "title_size": 42,
        "subtitle": "Акции США обновили рекорд, Тайвань откатился; MU, SNDK и DRAM растут перед данными продаж.",
        "subtitle_width": 56,
        "cards": [("S&P 500", "+0.7%", "новый рекорд"), ("TAIEX / TSMC", "-0.1 / -0.4", "Азия в полдень, %"), ("TraderXYZ", "$3.07B", "оборот топ-10, +38%")],
        "box1": ("3 ключевых сигнала", ["1. Удержит ли TSMC 2435-2440?", "2. Поддержат ли продажи мягкую посадку?", "3. Подтвердит ли рынок рост памяти?"]),
        "box2": ("Рамка риска", ["Слабая инфляция снижает давление ставок.", "Риски оценки и плеча сохраняются.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: дефицит AI идет в HBM и память, но спрос, базовый PCE и оборот акций должны подтвердить тренд.",
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
