#!/usr/bin/env python3
from pathlib import Path
import html
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily" / "images"
DATE = "2026-08-10"
CODE = "VLYQB1HXUW"

IMAGES = {
    "zh-cn": {
        "file": "market-brief-2026-08-10-zh-cn.svg",
        "tag": f"{DATE} · 全球市场日报",
        "title": "弱就业推升风险偏好，AI内部重排",
        "subtitle": "美债收益率回落支持科技股，但CPI与消费将检验软着陆；台积电营收等待确认。",
        "cards": [("S&P 500", "+0.6%", "再创历史新高"), ("TAIEX / TSMC", "+1.6 / +0.8", "亚洲午间变化"), ("TraderXYZ", "$0.97B", "周末前十成交")],
        "box1": ("3 个关键观察", ["1. TSMC 7月营收是否超预期？", "2. CPI 与零售能否支持软着陆？", "3. MU / AMD 能否跟上 SOXX？"]),
        "box2": ("风险框架", ["弱就业降低短期加息压力。", "坏数据利好不能无限外推。", f"GateAffiliate · 邀请码 {CODE}"]),
        "bottom": "核心：AI需求未见顶，但盈利扩散、通胀与消费将决定高估值资产能否继续上行。",
    },
    "zh-hant": {
        "file": "market-brief-2026-08-10-zh-hant.svg",
        "tag": f"{DATE} · 全球市場日報",
        "title": "弱就業推升風險偏好，AI內部重排",
        "subtitle": "美債殖利率回落支持科技股，但CPI與消費將檢驗軟著陸；台積電營收等待確認。",
        "cards": [("S&P 500", "+0.6%", "再創歷史新高"), ("TAIEX / TSMC", "+1.6 / +0.8", "亞洲午間變化"), ("TraderXYZ", "$0.97B", "週末前十成交")],
        "box1": ("3 個關鍵觀察", ["1. TSMC 7月營收是否超預期？", "2. CPI 與零售能否支持軟著陸？", "3. MU / AMD 能否跟上 SOXX？"]),
        "box2": ("風險框架", ["弱就業降低短期升息壓力。", "壞數據利好不能無限外推。", f"GateAffiliate · 邀請碼 {CODE}"]),
        "bottom": "核心：AI需求未見頂，但盈利擴散、通膨與消費將決定高估值資產能否繼續上行。",
    },
    "en": {
        "file": "market-brief-2026-08-10-en.svg",
        "tag": f"{DATE} · Global Market Brief",
        "title": "Weak jobs lift risk as AI leadership resets",
        "title_size": 46,
        "subtitle": "Lower yields support tech, but CPI and consumption will test the soft landing as TSMC revenue awaits confirmation.",
        "cards": [("S&P 500", "+0.6%", "new record close"), ("TAIEX / TSMC", "+1.6 / +0.8", "Asia midday change, %"), ("TraderXYZ", "$0.97B", "weekend top-ten volume")],
        "box1": ("3 key checks", ["1. Does TSMC July revenue beat?", "2. Can CPI and retail support landing?", "3. Do MU / AMD catch up to SOXX?"]),
        "box2": ("Risk Frame", ["Weak jobs lower near-term hike pressure.", "Bad-news rallies cannot run forever.", f"GateAffiliate · invite code {CODE}"]),
        "bottom": "Bottom line: AI demand remains firm, but earnings breadth, inflation and consumption will decide the next valuation leg.",
        "bottom_width": 78,
    },
    "ru": {
        "file": "market-brief-2026-08-10-ru.svg",
        "tag": f"{DATE} · Обзор рынка",
        "title": "Слабая занятость поддержала риск",
        "title_size": 42,
        "subtitle": "Снижение ставок помогает технологиям, но CPI и спрос проверят мягкую посадку; отчет TSMC еще впереди.",
        "subtitle_width": 42,
        "cards": [("S&P 500", "+0.6%", "новый рекорд"), ("TAIEX / TSMC", "+1.6 / +0.8", "изменение в Азии, %"), ("TraderXYZ", "$0.97B", "оборот выходных")],
        "box1": ("3 ключевых сигнала", ["1. Удивит ли выручка TSMC за июль?", "2. Поддержат ли CPI и продажи посадку?", "3. Догонят ли MU / AMD индекс SOXX?"]),
        "box2": ("Рамка риска", ["Слабая занятость снижает риск ставки.", "Плохие данные не всегда полезны акциям.", f"GateAffiliate · код {CODE}"]),
        "bottom": "Итог: спрос AI силен, но широта прибыли, инфляция и потребление решат следующий этап оценки.",
        "bottom_width": 45,
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
