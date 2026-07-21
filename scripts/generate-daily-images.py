#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-21"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-21-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "科技修复增强，等待云财报确认",
        "subtitle": "台湾市场广度改善、油价回落、存储成交恢复，但新趋势仍需美国现货和 Alphabet 基本面验证。",
        "cards": [("TAIEX / TSMC", "+3.8% / +3.0%", "广泛风险回补"), ("TraderXYZ", "$2.84B", "前十成交翻倍"), ("Brent", "$86.7", "回落约 1.7%")],
        "box1": ("3 个关键观察", ["1. TSMC 能否收稳 2380-2400？", "2. SOXX / SMH 是否放量？", "3. Brent 能否回到 85 美元下方？"]),
        "box2": ("云财报框架", ["Google Cloud 增速与 AI 资本开支。", "Gemini 商业化与搜索利润率。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：反弹强度与成交改善，阶段性底部仍需现货、期权和云财报共同确认。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-21-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "科技修復增強，等待雲端財報確認",
        "subtitle": "台灣市場廣度改善、油價回落、記憶體成交恢復，但新趨勢仍需美國現貨和 Alphabet 基本面驗證。",
        "cards": [("TAIEX / TSMC", "+3.8% / +3.0%", "廣泛風險回補"), ("TraderXYZ", "$2.84B", "前十成交翻倍"), ("Brent", "$86.7", "回落約 1.7%")],
        "box1": ("3 個關鍵觀察", ["1. TSMC 能否收穩 2380-2400？", "2. SOXX / SMH 是否放量？", "3. Brent 能否回到 85 美元下方？"]),
        "box2": ("雲端財報框架", ["Google Cloud 增速與 AI 資本開支。", "Gemini 商業化與搜尋利潤率。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：反彈強度與成交改善，階段性底部仍需現貨、期權和雲端財報共同確認。",
    },
    "en": {
        "file": "market-brief-2026-07-21-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "Tech repair strengthens; cloud results decide",
        "subtitle": "Taiwan breadth improves as oil falls and memory volume returns, but U.S. cash trading and Alphabet fundamentals must confirm the trend.",
        "cards": [("TAIEX / TSMC", "+3.8% / +3.0%", "broad risk buying"), ("TraderXYZ", "$2.84B", "top-ten volume doubles"), ("Brent", "$86.7", "down about 1.7%")],
        "box1": ("3 key checks", ["1. Can TSMC close at 2380-2400?", "2. Do SOXX / SMH volumes expand?", "3. Can Brent move below $85?"]),
        "box2": ("Cloud Results Frame", ["Google Cloud growth and AI capex.", "Gemini monetization and search margin.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: stronger price and volume help, but cash, options and cloud earnings must confirm a tactical bottom.",
    },
    "ru": {
        "file": "market-brief-2026-07-21-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "Отскок усилился: облака решат",
        "subtitle": "Тайвань растет, нефть снижается, оборот памяти вернулся; тренд подтвердят спот США и отчет Alphabet.",
        "cards": [("TAIEX / TSMC", "+3.8% / +3.0%", "широкий отскок"), ("TraderXYZ", "$2.84B", "оборот удвоился"), ("Brent", "$86.7", "снижение на 1.7%")],
        "box1": ("3 ключевых сигнала", ["1. Закроется ли TSMC на 2380-2400?", "2. Вырастут ли объемы SOXX / SMH?", "3. Опустится ли Brent ниже $85?"]),
        "box2": ("Рамка Облачного Отчета", ["Рост Google Cloud и AI-капзатраты.", "Монетизация Gemini и маржа поиска.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: цена и объем улучшились, но тактическое дно должны подтвердить спот, опционы и облачная отчетность.",
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
