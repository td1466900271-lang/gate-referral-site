#!/usr/bin/env python3
from pathlib import Path
import html
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parents[1]
IMPORT_SCRIPT = ROOT / "scripts" / "import-market-briefs.py"
SPEC = importlib.util.spec_from_file_location("import_market_briefs", IMPORT_SCRIPT)
import_market_briefs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(import_market_briefs)

BASE_URL = import_market_briefs.BASE_URL
CODE = import_market_briefs.CODE
LANG_META = import_market_briefs.LANG_META
STYLE_VERSION = import_market_briefs.STYLE_VERSION
T2S = import_market_briefs.T2S
alternates = import_market_briefs.alternates
brief_cta = import_market_briefs.brief_cta
daily_slug = import_market_briefs.daily_slug
footer = import_market_briefs.footer
header = import_market_briefs.header
write = import_market_briefs.write

DATE = "2026-07-01"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGE = "/daily/images/latest-market-brief.jpg"

META = {
    "zh-cn": {
        "title": "AI 半导体二次确认继续推进，TSM 与设备链成为核心信号",
        "desc": "2026-07-01 GateAffiliate 每日市场日报：AI 半导体二次确认、TSM 台股修复、设备链走强、MU 高位换手、Crypto 偏弱与宏观约束。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "AI 半导体二次确认继续推进，TSM 与设备链成为核心信号。",
        "summary": "TSM、AMD、AMAT、ASML 与半导体 ETF 延续修复，资金从 MU 财报验证扩散到先进制程、设备链和 AI 供应链；但 MU 高位换手、DRAM 转弱、Crypto 偏弱，说明不是无差别 risk-on。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "AI 半導體二次確認繼續推進，TSM 與設備鏈成為核心信號",
        "desc": "2026-07-01 GateAffiliate 每日市場日報：AI 半導體二次確認、TSM 台股修復、設備鏈走強、MU 高位換手、Crypto 偏弱與宏觀約束。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "AI 半導體二次確認繼續推進，TSM 與設備鏈成為核心信號。",
        "summary": "TSM、AMD、AMAT、ASML 與半導體 ETF 延續修復，資金從 MU 財報驗證擴散到先進製程、設備鏈和 AI 供應鏈；但 MU 高位換手、DRAM 轉弱、Crypto 偏弱，說明不是無差別 risk-on。",
        "tag": "最新",
    },
    "en": {
        "title": "AI semiconductor second confirmation continues as TSM and equipment lead",
        "desc": "2026-07-01 GateAffiliate daily market brief: AI semiconductor confirmation, TSM Taiwan repair, equipment strength, MU high-level churn, weak crypto and macro valuation limits.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "AI semiconductor second confirmation continues, with TSM and equipment as the key signals.",
        "summary": "TSM, AMD, AMAT, ASML and semiconductor ETFs continued to recover. The trade is spreading from MU's memory proof into advanced process, equipment and the broader AI supply chain, but MU churn, weaker DRAM and soft crypto show this is selective risk-taking rather than a broad risk-on move.",
        "tag": "Latest",
    },
    "ru": {
        "title": "Второе подтверждение AI-полупроводников продолжается: в центре TSM и оборудование",
        "desc": "Ежедневный обзор GateAffiliate за 2026-07-01: подтверждение AI-полупроводников, восстановление TSM на Тайване, сила оборудования, высокая смена рук в MU, слабая крипта и макро-ограничения.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "Второе подтверждение AI-полупроводников продолжается: ключевые сигналы дают TSM и оборудование.",
        "summary": "TSM, AMD, AMAT, ASML и полупроводниковые ETF продолжили восстановление. Сделка расширяется от подтверждения MU в памяти к передовым техпроцессам, оборудованию и всей AI-цепочке, но высокая смена рук в MU, слабый DRAM и мягкая крипта показывают, что это выборочный, а не широкий risk-on.",
        "tag": "Свежий",
    },
}

EN_SECTIONS = [
    ("Main View", [
        "AI semiconductor second confirmation is still progressing. U.S. TSM, AMD, AMAT, ASML, SMH and SOXX all strengthened, while Taiwan's market and TSM continued to repair intraday.",
        "This is not broad, indiscriminate risk-on. MU still has high TraderXYZ turnover but is slightly lower, DRAM is weaker, CRCL fell sharply, and BTC/ETH are soft. Capital is choosing assets that can convert AI CapEx into earnings.",
    ]),
    ("Key Market Data", [
        "U.S. cash data is from the 2026-06-30 close. Taiwan and TraderXYZ / Hyperliquid data are from around 2026-07-01 10:59 CST.",
        "SPY 746.77 +0.74%, QQQ 736.40 +1.63%, SMH 655.89 +3.80%, SOXX 640.76 +4.15%. TSM ADR 477.57 +4.84%, MU 1154.29 +0.53%, NVDA 200.09 +2.53%, AMD 580.91 +7.64%, AMAT 723.00 +4.19%, ASML 1989.44 +5.59%, SNDK 2273.73 +10.75%.",
        "Taiwan Weighted traded near 47,045.32, up about 1.99%. TSM 2330 bid/ask was around NT$2485 / NT$2490, with an intraday high near NT$2495. A sustained move above NT$2500 would reconfirm TSM as the core anchor of the Asian AI supply chain.",
    ]),
    ("TraderXYZ / Hyperliquid Flows", [
        "Top 24h notional flows included SKHX about $435M, XYZ100 about $314M, SP500 about $261M, SPCX about $258M, MU about $197M, SNDK about $171M, SILVER about $164M, DRAM about $86.22M, CL about $76.53M and CRCL about $72.52M.",
        "MU remains top five but is slightly lower, which points to high-level churn rather than a clean second leg higher. SNDK is much stronger than DRAM, suggesting rotation inside the memory chain toward data-center storage capacity.",
    ]),
    ("Crypto and Macro", [
        "BTC traded near 59,060, ETH near 1,585.6, SOL near 74.774 and HYPE near 65.37. Crypto is not confirming a broad liquidity-driven risk-on move today.",
        "May PCE at 4.1% YoY and core PCE at 3.4% keep the Fed from turning dovish quickly. AI hardware needs earnings delivery more than simple multiple expansion.",
    ]),
    ("Institutional Frame", [
        "Micron's FY2026 Q3 results remain the core fundamental anchor: revenue $41.456B, non-GAAP EPS $25.11 and gross margin near 84.6%, with Q4 guidance around $50B revenue and non-GAAP EPS near $31.",
        "Wedbush, BNP Paribas and Morgan Stanley remain supportive on the AI memory cycle and MU's improving visibility. Goldman Sachs' AI CapEx framework keeps the bigger point in focus: AI infrastructure is a multi-year build-out across data centers, power, cooling, memory, networking and packaging.",
        "Reported TSMC advanced-node price increases strengthen TSM's pricing power, but may pressure downstream customers such as Nvidia, AMD, Apple, Qualcomm and Broadcom.",
    ]),
    ("Contrarian View", [
        "The strongest signal today is not MU alone. TSM, AMD, AMAT, ASML, SNDK and semiconductor ETFs show that AI is being repriced across the supply chain.",
        "MU sideways action is not automatically bearish. If key levels hold, heavy turnover can be a healthy handoff rather than the end of the theme.",
        "Weak crypto means this is not a broad liquidity rally. The real signal is in semiconductor ETFs, TSM, equipment and SNDK.",
    ]),
    ("Watchlist", [
        "TSM: whether 2330.TW can break and hold NT$2500.",
        "MU: whether the 1130-1150 zone keeps attracting buyers.",
        "SNDK / DRAM: whether storage strength continues while DRAM lags.",
        "Equipment chain: AMAT, ASML, LRCX and KLAC are the quality check for AI CapEx diffusion.",
        "Macro: Fed comments, Treasury yields and oil remain the valuation ceiling.",
    ]),
    ("Conclusion", [
        "My view: AI semiconductor second confirmation is becoming higher quality. Last week MU validated memory tightness; now TSM, equipment, AMD, SNDK and semiconductor ETFs are repairing together. This looks like a systemic repricing of the AI CapEx chain, not only a single-company earnings trade.",
        "I would still avoid calling it a risk-free chase. MU is sideways, DRAM is weaker, crypto is not helping, and PCE remains high. The better framework is medium-term constructive on AI bottleneck assets, short-term confirmation through TSM NT$2500 and MU 1130-1150, with macro risk kept in view.",
    ]),
]

RU_SECTIONS = [
    ("Главный Вывод", [
        "Второе подтверждение AI-полупроводников продолжается. В США укрепились TSM, AMD, AMAT, ASML, SMH и SOXX, а сегодня рынок Тайваня и TSM продолжили внутридневное восстановление.",
        "Это не широкий и безусловный risk-on. У MU все еще высокий оборот на TraderXYZ, но цена немного ниже; DRAM слабее, CRCL резко снизился, BTC/ETH мягкие. Капитал выбирает активы, которые реально могут конвертировать AI CapEx в прибыль.",
    ]),
    ("Ключевые Данные", [
        "Данные США относятся к закрытию 2026-06-30. Тайвань и TraderXYZ / Hyperliquid — около 2026-07-01 10:59 CST.",
        "SPY 746.77 +0.74%, QQQ 736.40 +1.63%, SMH 655.89 +3.80%, SOXX 640.76 +4.15%. TSM ADR 477.57 +4.84%, MU 1154.29 +0.53%, NVDA 200.09 +2.53%, AMD 580.91 +7.64%, AMAT 723.00 +4.19%, ASML 1989.44 +5.59%, SNDK 2273.73 +10.75%.",
        "Taiwan Weighted торговался около 47 045,32, рост около 1,99%. TSM 2330 стояла около NT$2485 / NT$2490, внутридневной максимум около NT$2495. Устойчивое движение выше NT$2500 снова подтвердит TSM как главный якорь азиатской AI-цепочки.",
    ]),
    ("Потоки TraderXYZ / Hyperliquid", [
        "В топ 24-часовых номинальных потоков вошли SKHX около $435 млн, XYZ100 около $314 млн, SP500 около $261 млн, SPCX около $258 млн, MU около $197 млн, SNDK около $171 млн, SILVER около $164 млн, DRAM около $86,22 млн, CL около $76,53 млн и CRCL около $72,52 млн.",
        "MU остается в топ-5, но немного снижается. Это больше похоже на высокую смену рук, чем на чистую вторую волну роста. SNDK заметно сильнее DRAM, что указывает на ротацию внутри памяти в сторону емкости хранения для дата-центров.",
    ]),
    ("Крипто И Макро", [
        "BTC около 59 060, ETH около 1 585,6, SOL около 74,774 и HYPE около 65,37. Крипто сегодня не подтверждает широкий ликвидностный risk-on.",
        "PCE за май 4,1% г/г и базовый PCE 3,4% не дают ФРС быстро стать мягкой. AI-оборудованию теперь важнее подтверждать прибыль, чем просто расширять мультипликаторы.",
    ]),
    ("Институциональный Фон", [
        "Отчет Micron за FY2026 Q3 остается ключевым фундаментальным якорем: выручка $41,456 млрд, non-GAAP EPS $25,11, валовая маржа около 84,6%; прогноз Q4 — выручка около $50 млрд и non-GAAP EPS около $31.",
        "Wedbush, BNP Paribas и Morgan Stanley по-прежнему поддерживают тезис AI-памяти и улучшения видимости MU. Рамка Goldman Sachs по AI CapEx напоминает: AI-инфраструктура — это многолетний цикл дата-центров, энергии, охлаждения, памяти, сетей и упаковки.",
        "Сообщения о повышении цен TSMC на передовые техпроцессы усиливают ценовую власть TSM, но могут давить на клиентов вроде Nvidia, AMD, Apple, Qualcomm и Broadcom.",
    ]),
    ("Контрарный Взгляд", [
        "Самый сильный сигнал сегодня — не только MU. TSM, AMD, AMAT, ASML, SNDK и полупроводниковые ETF показывают переоценку всей AI-цепочки.",
        "Боковое движение MU не обязательно медвежье. Пока ключевые уровни держатся, высокий оборот может быть здоровой сменой рук, а не концом темы.",
        "Слабая крипта означает, что это не широкий ликвидностный рост. Главный сигнал идет от ETF полупроводников, TSM, оборудования и SNDK.",
    ]),
    ("Что Смотреть", [
        "TSM: сможет ли 2330.TW пробить и удержать NT$2500.",
        "MU: будет ли зона 1130-1150 продолжать привлекать покупателей.",
        "SNDK / DRAM: продолжится ли сила хранения при отставании DRAM.",
        "Оборудование: AMAT, ASML, LRCX и KLAC проверяют качество распространения AI CapEx.",
        "Макро: комментарии ФРС, доходности и нефть остаются потолком для оценок.",
    ]),
    ("Заключение", [
        "Мой вывод: второе подтверждение AI-полупроводников становится качественнее. На прошлой неделе MU подтвердила дефицит памяти; теперь TSM, оборудование, AMD, SNDK и ETF восстанавливаются вместе. Это больше похоже на системную переоценку AI CapEx-цепочки, а не только на отчет одной компании.",
        "Но я не считаю это безрисковым окном для погони. MU боковая, DRAM слабее, крипто не помогает, PCE высокий. Более разумная рамка: среднесрочно конструктивно смотреть на AI bottleneck assets, краткосрочно ждать подтверждения TSM выше NT$2500 и удержания MU 1130-1150, не забывая о макро-риске.",
    ]),
]

SOURCES = [
    ("Micron FY2026 Q3 官方财报", "https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-record-results-third-quarter"),
    ("Micron Investor Relations", "https://investors.micron.com/"),
    ("MarketWatch: Wedbush Daniel Ives", "https://www.marketwatch.com/livecoverage/micron-earnings-stock-results-memory-guidance/card/micron-s-results-suggest-the-memory-chip-trade-is-in-the-early-stages-of-playing-out-says-analyst-goQl2ckFPUte8RwIXGIE"),
    ("Goldman Sachs AI CapEx framework", "https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out"),
    ("BEA Personal Income and Outlays", "https://www.bea.gov/news/2026/personal-income-and-outlays-may-2026"),
    ("TWSE 实时行情", "https://mis.twse.com.tw/stock/index.jsp"),
    ("TraderXYZ / Hyperliquid 数据接口", "https://api.hyperliquid.xyz/info"),
]


def paragraphs_from_source(lang):
    text = SOURCE.read_text(encoding="utf-8")
    if lang == "zh-hant":
        text = T2S.convert(text) if False else text
        text = __import__("opencc").OpenCC("s2t").convert(text)
    blocks = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    html_blocks = []
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        first = lines[0].lstrip("、")
        if len(lines) == 1 and (first.endswith("判断") or re.match(r"^[一二三四五六七八九十]+、", first)):
            html_blocks.append(f"<h2>{html.escape(first)}</h2>")
        elif len(lines) > 2 and all(("：" in line or line.startswith(("TSM", "MU", "SNDK", "设备链", "AMD", "CRCL", "TRAM", "宏观"))) for line in lines[1:]):
            html_blocks.append(f"<h2>{html.escape(first)}</h2><ul>" + "".join(f"<li>{html.escape(line)}</li>" for line in lines[1:]) + "</ul>")
        else:
            html_blocks.append("".join(f"<p>{html.escape(line)}</p>" for line in lines))
    return "\n".join(html_blocks)


def translated_sections(sections):
    return "\n".join(
        f"<h2>{html.escape(title)}</h2>" + "".join(f"<p>{html.escape(p)}</p>" for p in paragraphs)
        for title, paragraphs in sections
    )


def brief_body(lang):
    if lang in ("zh-cn", "zh-hant"):
        article = paragraphs_from_source(lang)
    elif lang == "en":
        article = translated_sections(EN_SECTIONS)
    else:
        article = translated_sections(RU_SECTIONS)
    source_links = "".join(f'<li><a class="text-link" href="{url}">{html.escape(label)}</a></li>' for label, url in SOURCES)
    labels = {
        "zh-cn": ("今日总判断", "重点观察", "参考来源"),
        "zh-hant": ("今日總判斷", "重點觀察", "參考來源"),
        "en": ("Top View", "Watchlist", "Sources"),
        "ru": ("Главный Вывод", "Список Наблюдения", "Источники"),
    }[lang]
    return f'''<section class="hero">
      <div class="hero-inner">
        <span class="eyebrow">{META[lang]["eyebrow"]}</span>
        <h1>{META[lang]["h1"]}</h1>
        <p class="hero-copy">{META[lang]["summary"]}</p>
        <div class="hero-actions">
          <a class="button button-primary" href="#brief">{labels[0]}</a>
          <a class="button button-secondary" data-invite href="#">VLYQB1HXUW</a>
        </div>
      </div>
    </section>
    <main id="brief">
      <section>
        <div class="wrap brief-layout">
          <article class="card brief-article">
            <span class="eyebrow">{labels[0]}</span>
            <img class="brief-hero-image" src="{IMAGE}" alt="{html.escape(META[lang]["title"])}">
            {article}
          </article>
          <aside class="card" id="watchlist">
            <h2>{labels[1]}</h2>
            <div class="brief-list">
              <div class="brief-item"><strong>TSM</strong><span>2500 TWD</span></div>
              <div class="brief-item"><strong>MU</strong><span>1130-1150</span></div>
              <div class="brief-item"><strong>SNDK / DRAM</strong><span>memory rotation</span></div>
              <div class="brief-item"><strong>AMAT / ASML</strong><span>AI CapEx</span></div>
              <div class="brief-item"><strong>BTC / ETH</strong><span>risk appetite</span></div>
            </div>
          </aside>
        </div>
      </section>
      <section class="faq">
        <div class="wrap">
          <div class="section-head"><h2>{labels[2]}</h2></div>
          <ul>{source_links}</ul>
        </div>
      </section>
      {history_section(lang)}
      {brief_cta(lang)}
    </main>'''


def history_section(lang):
    m = LANG_META[lang]
    latest = META[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-06-29")}"><span class="history-date">2026-06-29</span><span><span class="history-title">AI memory / MU / TSM</span><span class="history-summary">Previous market brief.</span></span><span class="history-tag">Archive</span></a>
    </div></div></section>'''


def page(lang):
    path = daily_slug(lang, DATE)
    path_by_lang = {l: daily_slug(l, DATE) for l in LANG_META}
    title_prefix = {
        "zh-cn": "GateAffiliate 每日市场日报",
        "zh-hant": "GateAffiliate 每日市場日報",
        "en": "GateAffiliate Daily Market Brief",
        "ru": "Ежедневный обзор рынка GateAffiliate",
    }[lang]
    schema = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": META[lang]["title"],
        "description": META[lang]["desc"],
        "datePublished": DATE,
        "dateModified": DATE,
        "author": {"@type": "Organization", "name": "GateAffiliate"},
        "publisher": {"@type": "Organization", "name": "GateAffiliate", "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/assets/gate-logo.ico"}},
        "image": f"{BASE_URL}{IMAGE}",
        "mainEntityOfPage": f"{BASE_URL}{path}",
    }
    return f'''<!doctype html>
<html lang="{LANG_META[lang]["html"]}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(title_prefix + " " + DATE + " | " + META[lang]["title"])}</title>
    <meta name="description" content="{html.escape(META[lang]["desc"])}">
    <meta name="robots" content="index,follow,max-image-preview:large">
    <link rel="canonical" href="{BASE_URL}{path}">
    {alternates(path_by_lang, path_by_lang["zh-cn"])}
    <meta property="og:type" content="article">
    <meta property="og:title" content="{html.escape(META[lang]["title"])}">
    <meta property="og:description" content="{html.escape(META[lang]["desc"])}">
    <meta property="og:image" content="{BASE_URL}{IMAGE}">
    <meta property="og:site_name" content="GateAffiliate">
    <meta property="og:url" content="{BASE_URL}{path}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="theme-color" content="#07102b">
    <link rel="icon" href="/assets/gate-logo.ico" type="image/x-icon">
    <link rel="preload" as="image" href="{IMAGE}">
    <link rel="stylesheet" href="/assets/styles.css?v={STYLE_VERSION}">
    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
  </head>
  <body>
    {header(lang, path_by_lang)}
    {brief_body(lang)}
    {footer(lang)}
    <script src="/assets/app.js?v={STYLE_VERSION}"></script>
  </body>
</html>
'''


def update_daily_index(lang):
    path = ROOT / LANG_META[lang]["daily"].lstrip("/") / "index.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace(daily_slug(lang, "2026-06-29"), daily_slug(lang, DATE), 1)
    card = f'''<a class="history-link" href="{daily_slug(lang, DATE)}">
              <span class="history-date">{DATE}</span>
              <span><span class="history-title">{html.escape(META[lang]["title"])}</span><span class="history-summary">{html.escape(META[lang]["summary"][:140])}</span></span>
              <span class="history-tag">{META[lang]["tag"]}</span>
            </a>'''
    text = re.sub(r'<a class="history-link" href="' + re.escape(daily_slug(lang, DATE)) + r'".*?</a>', "", text, flags=re.S)
    text = text.replace('<div class="history-list">', '<div class="history-list">' + card, 1)
    path.write_text(text, encoding="utf-8")


def update_sitemap():
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    for lang in LANG_META:
        loc = f"{BASE_URL}{daily_slug(lang, DATE)}"
        text = re.sub(rf"\s*<url>\s*<loc>{re.escape(loc)}</loc>.*?</url>", "", text, flags=re.S)
    entries = []
    for lang in LANG_META:
        entries.append(f"  <url>\n    <loc>{BASE_URL}{daily_slug(lang, DATE)}</loc>\n    <lastmod>{DATE}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.72</priority>\n  </url>")
    text = text.replace("</urlset>", "\n".join(entries) + "\n</urlset>")
    path.write_text(text, encoding="utf-8")


def main():
    if not SOURCE.exists():
        raise SystemExit(f"Missing {SOURCE}")
    for lang in LANG_META:
        write(ROOT / daily_slug(lang, DATE).lstrip("/") / "index.html", page(lang))
        update_daily_index(lang)
    update_sitemap()
    print(f"Added GateAffiliate daily brief {DATE} in {len(LANG_META)} languages.")


if __name__ == "__main__":
    main()
