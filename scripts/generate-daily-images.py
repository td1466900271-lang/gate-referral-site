#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-14"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-14-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "能源冲击压制科技估值",
        "subtitle": "油价与利率同步上行，台股系统性去风险，存储链仍是回撤中心。",
        "cards": [("TAIEX", "-2.8%", "广泛去风险"), ("TSMC", "2390-2430", "相对韧性"), ("WTI / Brent", "+6.9% / +6.2%", "能源冲击")],
        "box1": ("3 个关键观察", ["1. 油价能否回落？", "2. 台股 44000 点能否承接？", "3. 存储是否继续弱于 GPU？"]),
        "box2": ("验证框架", ["7 月 16 日 TSMC 法说。", "关注资本开支与毛利率。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：AI 产业逻辑未反转，但市场已进入现金回报与估值验证阶段。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-14-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "能源衝擊壓制科技估值",
        "subtitle": "油價與利率同步上行，台股系統性去風險，記憶體鏈仍是回撤中心。",
        "cards": [("TAIEX", "-2.8%", "廣泛去風險"), ("TSMC", "2390-2430", "相對韌性"), ("WTI / Brent", "+6.9% / +6.2%", "能源衝擊")],
        "box1": ("3 個關鍵觀察", ["1. 油價能否回落？", "2. 台股 44000 點能否承接？", "3. 記憶體是否繼續弱於 GPU？"]),
        "box2": ("驗證框架", ["7 月 16 日 TSMC 法說。", "關注資本開支與毛利率。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：AI 產業邏輯未反轉，但市場已進入現金回報與估值驗證階段。",
    },
    "en": {
        "file": "market-brief-2026-07-14-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "Energy shock hits tech valuations",
        "subtitle": "Oil and yields rise together as Taiwan equities de-risk broadly and memory remains at the center of the drawdown.",
        "cards": [("TAIEX", "-2.8%", "broad de-risking"), ("TSMC", "2390-2430", "relative resilience"), ("WTI / Brent", "+6.9% / +6.2%", "energy shock")],
        "box1": ("3 key checks", ["1. Can oil retrace?", "2. Does TAIEX hold 44000?", "3. Does memory stay weaker than GPU?"]),
        "box2": ("Validation", ["TSMC reports on July 16.", "Watch capex and gross margin.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: AI fundamentals remain intact, but markets are testing cash returns and valuation discipline.",
    },
    "ru": {
        "file": "market-brief-2026-07-14-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "Энергошок давит на оценки технологий",
        "subtitle": "Нефть и доходности растут, тайваньский рынок снижает риск, а память остается центром падения.",
        "cards": [("TAIEX", "-2.8%", "общее снижение риска"), ("TSMC", "2390-2430", "относительная устойчивость"), ("WTI / Brent", "+6.9% / +6.2%", "энергетический шок")],
        "box1": ("3 ключевых сигнала", ["1. Откатится ли нефть?", "2. Удержит ли TAIEX 44000?", "3. Будет ли память слабее GPU?"]),
        "box2": ("Проверка", ["Отчет TSMC 16 июля.", "Следите за капзатратами и маржой.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: AI-фундамент сохраняется, но рынок проверяет денежную отдачу и дисциплину оценок.",
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
