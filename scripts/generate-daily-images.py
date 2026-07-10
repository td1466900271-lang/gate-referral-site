#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-07-10"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-07-10-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "AI 硬件链修复，存储领涨",
        "subtitle": "市场从防守切回修复，存储链高成交反弹，油价回落缓和估值压力。",
        "cards": [("MU", "+4.6%", "1000 附近确认"), ("SNDK / DRAM", "+10.4% / +4.8%", "存储修复"), ("CL / Brent", "-2.7% / -2.8%", "油价回落")],
        "box1": ("3 个关键观察", ["1. MU 能否站稳 1000-1050？", "2. TSMC 6 月营收是否验证？", "3. 存储链高成交上涨能否延续？"]),
        "box2": ("交易框架", ["中期 AI 主线仍在。", "短线从防守转修复。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：AI 硬件链重新修复，存储链主动反弹，油价回落给科技估值减压。",
    },
    "zh-hant": {
        "file": "market-brief-2026-07-10-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "AI 硬體鏈修復，記憶體領漲",
        "subtitle": "市場從防守切回修復，記憶體鏈高成交反彈，油價回落緩和估值壓力。",
        "cards": [("MU", "+4.6%", "1000 附近確認"), ("SNDK / DRAM", "+10.4% / +4.8%", "記憶體修復"), ("CL / Brent", "-2.7% / -2.8%", "油價回落")],
        "box1": ("3 個關鍵觀察", ["1. MU 能否站穩 1000-1050？", "2. TSMC 6 月營收是否驗證？", "3. 記憶體鏈高成交上漲能否延續？"]),
        "box2": ("交易框架", ["中期 AI 主線仍在。", "短線從防守轉修復。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：AI 硬體鏈重新修復，記憶體鏈主動反彈，油價回落給科技估值減壓。",
    },
    "en": {
        "file": "market-brief-2026-07-10-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "AI hardware repairs, memory leads",
        "subtitle": "The market rotated from defense to repair as memory rebounded on high volume and lower oil eased valuation pressure.",
        "cards": [("MU", "+4.6%", "1000 area check"), ("SNDK / DRAM", "+10.4% / +4.8%", "memory repair"), ("CL / Brent", "-2.7% / -2.8%", "oil pullback")],
        "box1": ("3 key checks", ["1. Can MU hold 1000-1050?", "2. Does TSMC June revenue confirm?", "3. Does memory volume follow through?"]),
        "box2": ("Framework", ["Medium-term AI remains intact.", "Short term shifted to repair.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: AI hardware is repairing, memory is leading, and lower oil relieves pressure on tech valuations.",
    },
    "ru": {
        "file": "market-brief-2026-07-10-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "AI-сектор восстанавливается, память лидирует",
        "subtitle": "Рынок перешел от защиты к восстановлению: память растет на объеме, а снижение нефти облегчает оценки.",
        "cards": [("MU", "+4.6%", "проверка зоны 1000"), ("SNDK / DRAM", "+10.4% / +4.8%", "восстановление памяти"), ("CL / Brent", "-2.7% / -2.8%", "снижение нефти")],
        "box1": ("3 ключевых сигнала", ["1. Удержит ли MU 1000-1050?", "2. Подтвердит ли TSMC июньскую выручку?", "3. Продлится ли рост памяти на объеме?"]),
        "box2": ("Рамка", ["Среднесрочный AI-тренд жив.", "Краткосрочно рынок чинится.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: AI-оборудование восстанавливается, память лидирует, а снижение нефти снимает давление с оценок.",
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
