#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-22"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-22-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "硬件反弹有量，等待 Alphabet 验证",
        "subtitle": "存储与 AI 硬件获资金回补，台湾指数强于台积电；高油价和收益率继续约束估值扩张。",
        "cards": [("MU", "+12.2%", "存储领涨"), ("TAIEX / TSMC", "+1.9 / -0.4", "百分比变化"), ("Brent / US10Y", "91.0 / 4.63", "美元 / 收益率百分比")],
        "box1": ("3 个关键观察", ["1. 存储高成交能否延续？", "2. TSMC 能否重新跑赢指数？", "3. Brent 与收益率是否继续上行？"]),
        "box2": ("Alphabet 验证", ["Cloud 增速与 AI 资本开支。", "Gemini 变现与自由现金流。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：AI 硬件短线偏强，全面风险重启仍需云收入、利润率与现金回报证明。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-22-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "硬體反彈有量，等待 Alphabet 驗證",
        "subtitle": "記憶體與 AI 硬體獲資金回補，台灣指數強於台積電；高油價和殖利率繼續約束估值擴張。",
        "cards": [("MU", "+12.2%", "記憶體領漲"), ("TAIEX / TSMC", "+1.9 / -0.4", "百分比變化"), ("Brent / US10Y", "91.0 / 4.63", "美元 / 殖利率百分比")],
        "box1": ("3 個關鍵觀察", ["1. 記憶體高成交能否延續？", "2. TSMC 能否重新跑贏指數？", "3. Brent 與殖利率是否續升？"]),
        "box2": ("Alphabet 驗證", ["Cloud 增速與 AI 資本開支。", "Gemini 變現與自由現金流。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：AI 硬體短線偏強，全面風險重啟仍需雲端收入、利潤率與現金回報證明。",
    },
    "en": {
        "file": "market-brief-2026-07-22-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "Hardware rebounds on volume; Alphabet tests it",
        "subtitle": "Memory and AI hardware attract fresh buying as Taiwan beats TSMC; elevated oil and yields still constrain valuation expansion.",
        "cards": [("MU", "+12.2%", "memory leads"), ("TAIEX / TSMC", "+1.9 / -0.4", "change, percent"), ("Brent / US10Y", "91.0 / 4.63", "USD / yield %")],
        "box1": ("3 key checks", ["1. Does high memory volume persist?", "2. Can TSMC regain index leadership?", "3. Do Brent and yields keep rising?"]),
        "box2": ("Alphabet Test", ["Cloud growth and AI capex.", "Gemini monetization and free cash flow.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: AI hardware is tactically firm, but broad risk needs proof from cloud revenue, margin and cash returns.",
    },
    "ru": {
        "file": "market-brief-2026-07-22-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "AI-оборудование растет: тест Alphabet",
        "subtitle": "Память и AI привлекают покупки, индекс Тайваня сильнее TSMC; дорогая нефть и доходности ограничивают оценки.",
        "cards": [("MU", "+12.2%", "память лидирует"), ("TAIEX / TSMC", "+1.9 / -0.4", "изменение, %"), ("Brent / US10Y", "91.0 / 4.63", "USD / доходность %")],
        "box1": ("3 ключевых сигнала", ["1. Сохранится ли оборот памяти?", "2. Вернет ли TSMC лидерство?", "3. Продолжат ли расти нефть и ставки?"]),
        "box2": ("Проверка Alphabet", ["Рост Cloud и AI-капзатраты.", "Монетизация Gemini и денежный поток.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: AI-оборудование сильно краткосрочно, но широкий риск требует роста облака, маржи и денежной отдачи.",
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
