#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-20"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-20-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "台股修复，等待云资本开支验证",
        "subtitle": "台积电超跌反弹但趋势未确认，低成交永续仅显示恐慌缓和，高油价继续约束科技估值。",
        "cards": [("TSMC", "2330-2335", "反弹约 2%"), ("TraderXYZ", "$1.35B", "前十低成交"), ("Brent", "$88.2", "能源压力上升")],
        "box1": ("3 个关键观察", ["1. TSMC 能否守住 2300？", "2. SOXX / SMH 是否止跌？", "3. Brent 是否突破 90 美元？"]),
        "box2": ("本周框架", ["Alphabet 云资本开支与收入。", "订单、利润率与现金回报优先。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：技术修复不等于反转，AI 交易进入云资本开支与能源双重验证。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-20-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "台股修復，等待雲端資本開支驗證",
        "subtitle": "台積電超跌反彈但趨勢未確認，低成交永續僅顯示恐慌緩和，高油價繼續約束科技估值。",
        "cards": [("TSMC", "2330-2335", "反彈約 2%"), ("TraderXYZ", "$1.35B", "前十低成交"), ("Brent", "$88.2", "能源壓力上升")],
        "box1": ("3 個關鍵觀察", ["1. TSMC 能否守住 2300？", "2. SOXX / SMH 是否止跌？", "3. Brent 是否突破 90 美元？"]),
        "box2": ("本週框架", ["Alphabet 雲端資本開支與收入。", "訂單、利潤率與現金回報優先。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：技術修復不等於反轉，AI 交易進入雲端資本開支與能源雙重驗證。",
    },
    "en": {
        "file": "market-brief-2026-07-20-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "Taiwan repairs as cloud capex faces a test",
        "subtitle": "TSMC rebounds without confirming a reversal; thin perpetual volume shows calmer fear while high oil restrains tech valuations.",
        "cards": [("TSMC", "2330-2335", "about 2% rebound"), ("TraderXYZ", "$1.35B", "thin top-ten volume"), ("Brent", "$88.2", "higher energy risk")],
        "box1": ("3 key checks", ["1. Can TSMC hold 2300?", "2. Can SOXX / SMH stabilize?", "3. Does Brent break $90?"]),
        "box2": ("Weekly Frame", ["Alphabet cloud capex and revenue.", "Prioritize orders, margin and cash returns.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: technical repair is not a reversal; AI now faces cloud-capex and energy tests.",
    },
    "ru": {
        "file": "market-brief-2026-07-20-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "Тайвань отскакивает: проверка облаков",
        "subtitle": "TSMC растет без подтверждения разворота; тонкий объем снижает страх, а дорогая нефть давит на оценки технологий.",
        "cards": [("TSMC", "2330-2335", "отскок около 2%"), ("TraderXYZ", "$1.35B", "низкий оборот"), ("Brent", "$88.2", "рост энергориска")],
        "box1": ("3 ключевых сигнала", ["1. Удержит ли TSMC уровень 2300?", "2. Стабилизируются ли SOXX / SMH?", "3. Пробьет ли Brent отметку $90?"]),
        "box2": ("Рамка Недели", ["Облачные капзатраты и выручка Alphabet.", "Важнее заказы, маржа и денежная отдача.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: технический отскок не равен развороту; AI проверят облачные капзатраты и энергия.",
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
