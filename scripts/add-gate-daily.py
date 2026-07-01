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
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-01-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-01-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-01-en.svg",
    "ru": "/daily/images/market-brief-2026-07-01-ru.svg",
}

META = {
    "zh-cn": {
        "title": "AI 半导体二次确认继续推进，TSM 与设备链成为核心信号",
        "desc": "2026-07-01 GateAffiliate 每日市场日报：AI 半导体二次确认、TSM 台股修复、设备链走强、MU 高位换手、Crypto 偏弱与宏观约束。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "AI 半导体二次确认继续推进，TSM 与设备链成为核心信号。",
        "summary": "TSM、AMD、AMAT、ASML 与半导体 ETF 延续修复，资金从 MU 财报验证扩散到先进制程、设备链和 AI 供应链；但 MU 高位换手、DRAM 转弱、加密资产偏弱，说明不是无差别风险偏好升温。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "AI 半導體二次確認繼續推進，TSM 與設備鏈成為核心信號",
        "desc": "2026-07-01 GateAffiliate 每日市場日報：AI 半導體二次確認、TSM 台股修復、設備鏈走強、MU 高位換手、Crypto 偏弱與宏觀約束。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "AI 半導體二次確認繼續推進，TSM 與設備鏈成為核心信號。",
        "summary": "TSM、AMD、AMAT、ASML 與半導體 ETF 延續修復，資金從 MU 財報驗證擴散到先進製程、設備鏈和 AI 供應鏈；但 MU 高位換手、DRAM 轉弱、加密資產偏弱，說明不是無差別風險偏好升溫。",
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
        "summary": "TSM, AMD, AMAT, ASML и полупроводниковые ETF продолжили восстановление. Сделка расширяется от подтверждения MU в памяти к передовым техпроцессам, оборудованию и всей AI-цепочке, но высокая смена рук в MU, слабый DRAM и мягкая крипта показывают, что это выборочный, а не широкий рост аппетита к риску.",
        "tag": "Свежий",
    },
}

CONCISE_SECTIONS = {
    "zh-cn": [
        ("核心结论", [
            "今天的主线不是全面风险偏好升温，而是 AI 半导体内部的二次确认。TSM、AMD、AMAT、ASML 与半导体 ETF 同步修复，说明资金从 MU 的记忆体验证扩散到设备链、先进制程和 AI 供应链。",
            "但 MU 高位换手、DRAM 偏弱、BTC/ETH 走软，提示短线仍要避免无差别追涨。",
        ]),
        ("三条观察线", [
            "TSM 2330.TW 能否站稳 NT$2500，是亚洲 AI 供应链确认度的关键。",
            "MU 需要守住 1130-1150 区间，否则高位换手会变成利润回吐。",
            "设备链 AMAT、ASML、LRCX、KLAC 的持续性，决定 AI CapEx 是否继续向上扩散。",
        ]),
        ("交易框架", [
            "中期仍偏向 AI 瓶颈资产，但短线更适合等确认，而不是在情绪高点追单。",
            "加密资产没有同步走强，说明这轮强势更偏产业逻辑，不是全市场流动性行情。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "今天的主線不是全面風險偏好升溫，而是 AI 半導體內部的二次確認。TSM、AMD、AMAT、ASML 與半導體 ETF 同步修復，說明資金從 MU 的記憶體驗證擴散到設備鏈、先進製程和 AI 供應鏈。",
            "但 MU 高位換手、DRAM 偏弱、BTC/ETH 走軟，提示短線仍要避免無差別追漲。",
        ]),
        ("三條觀察線", [
            "TSM 2330.TW 能否站穩 NT$2500，是亞洲 AI 供應鏈確認度的關鍵。",
            "MU 需要守住 1130-1150 區間，否則高位換手會變成利潤回吐。",
            "設備鏈 AMAT、ASML、LRCX、KLAC 的持續性，決定 AI CapEx 是否繼續向上擴散。",
        ]),
        ("交易框架", [
            "中期仍偏向 AI 瓶頸資產，但短線更適合等確認，而不是在情緒高點追單。",
            "加密資產沒有同步走強，說明這輪強勢更偏產業邏輯，不是全市場流動性行情。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "This is not a broad risk-on move. It is a second confirmation inside AI semiconductors: TSM, AMD, AMAT, ASML and semi ETFs are recovering together.",
            "The signal has moved from MU memory validation into equipment, advanced process and the wider AI supply chain.",
        ]),
        ("Three Lines To Watch", [
            "TSM 2330.TW above NT$2500 would strengthen the Asian AI supply-chain confirmation.",
            "MU needs the 1130-1150 zone to hold; otherwise high turnover can become profit-taking.",
            "AMAT, ASML, LRCX and KLAC decide whether AI CapEx diffusion is still broadening.",
        ]),
        ("Trading Frame", [
            "Medium term, AI bottleneck assets remain constructive. Short term, confirmation matters more than chasing.",
            "Crypto weakness means this is an industry-led move, not a simple liquidity rally.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Это не широкий рост аппетита к риску, а второе подтверждение внутри AI-полупроводников: TSM, AMD, AMAT, ASML и полупроводниковые ETF восстанавливаются вместе.",
            "Сигнал расширился от памяти MU к оборудованию, передовым техпроцессам и более широкой AI-цепочке.",
        ]),
        ("Три Линии Для Наблюдения", [
            "TSM 2330.TW выше NT$2500 усилит подтверждение азиатской AI-цепочки.",
            "MU нужно удержать 1130-1150; иначе высокий оборот может перейти в фиксацию прибыли.",
            "AMAT, ASML, LRCX и KLAC покажут, продолжает ли AI CapEx расширяться.",
        ]),
        ("Торговая Рамка", [
            "Среднесрочно активы узких мест AI остаются конструктивными. Краткосрочно важнее подтверждение, чем погоня за движением.",
            "Слабая крипта означает, что это отраслевое движение, а не простой рост на ликвидности.",
        ]),
    ],
}

SOURCE_URLS = [
    ("micron-q3", "https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-record-results-third-quarter"),
    ("micron-ir", "https://investors.micron.com/"),
    ("marketwatch-ives", "https://www.marketwatch.com/livecoverage/micron-earnings-stock-results-memory-guidance/card/micron-s-results-suggest-the-memory-chip-trade-is-in-the-early-stages-of-playing-out-says-analyst-goQl2ckFPUte8RwIXGIE"),
    ("goldman-capex", "https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out"),
    ("bea-pce", "https://www.bea.gov/news/2026/personal-income-and-outlays-may-2026"),
    ("twse", "https://mis.twse.com.tw/stock/index.jsp"),
    ("traderxyz-api", "https://api.hyperliquid.xyz/info"),
]

SOURCE_LABELS = {
    "zh-cn": {
        "micron-q3": "Micron FY2026 Q3 官方财报",
        "micron-ir": "Micron 投资者关系",
        "marketwatch-ives": "MarketWatch：Wedbush Daniel Ives 观点",
        "goldman-capex": "Goldman Sachs AI 资本开支框架",
        "bea-pce": "BEA 个人收入与支出数据",
        "twse": "TWSE 实时行情",
        "traderxyz-api": "TraderXYZ / Hyperliquid 数据接口",
    },
    "zh-hant": {
        "micron-q3": "Micron FY2026 Q3 官方財報",
        "micron-ir": "Micron 投資者關係",
        "marketwatch-ives": "MarketWatch：Wedbush Daniel Ives 觀點",
        "goldman-capex": "Goldman Sachs AI 資本開支框架",
        "bea-pce": "BEA 個人收入與支出數據",
        "twse": "TWSE 即時行情",
        "traderxyz-api": "TraderXYZ / Hyperliquid 數據接口",
    },
    "en": {
        "micron-q3": "Micron FY2026 Q3 earnings release",
        "micron-ir": "Micron Investor Relations",
        "marketwatch-ives": "MarketWatch: Wedbush Daniel Ives view",
        "goldman-capex": "Goldman Sachs AI CapEx framework",
        "bea-pce": "BEA Personal Income and Outlays",
        "twse": "TWSE real-time quotes",
        "traderxyz-api": "TraderXYZ / Hyperliquid data API",
    },
    "ru": {
        "micron-q3": "Официальный отчет Micron за FY2026 Q3",
        "micron-ir": "Micron Investor Relations",
        "marketwatch-ives": "MarketWatch: мнение Wedbush Daniel Ives",
        "goldman-capex": "Goldman Sachs: рамка AI-капзатрат",
        "bea-pce": "BEA: личные доходы и расходы",
        "twse": "TWSE: котировки в реальном времени",
        "traderxyz-api": "TraderXYZ / Hyperliquid API данных",
    },
}


def translated_sections(sections):
    return "\n".join(
        f"<h2>{html.escape(title)}</h2>" + "".join(f"<p>{html.escape(p)}</p>" for p in paragraphs)
        for title, paragraphs in sections
    )


def brief_body(lang):
    article = translated_sections(CONCISE_SECTIONS[lang])
    source_links = "".join(
        f'<li><a class="text-link" href="{url}">{html.escape(SOURCE_LABELS[lang][key])}</a></li>'
        for key, url in SOURCE_URLS
    )
    labels = {
        "zh-cn": ("今日总判断", "重点观察", "参考来源"),
        "zh-hant": ("今日總判斷", "重點觀察", "參考來源"),
        "en": ("Top View", "Watchlist", "Sources"),
        "ru": ("Главный Вывод", "Список Наблюдения", "Источники"),
    }[lang]
    watch_labels = {
        "zh-cn": ("记忆体轮动", "AI 资本开支", "风险偏好"),
        "zh-hant": ("記憶體輪動", "AI 資本開支", "風險偏好"),
        "en": ("memory rotation", "AI CapEx", "risk appetite"),
        "ru": ("ротация памяти", "AI-капзатраты", "аппетит к риску"),
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
            <img class="brief-hero-image" src="{IMAGES[lang]}" alt="{html.escape(META[lang]["title"])}">
            {article}
          </article>
          <aside class="card" id="watchlist">
            <h2>{labels[1]}</h2>
            <div class="brief-list">
              <div class="brief-item"><strong>TSM</strong><span>2500 TWD</span></div>
              <div class="brief-item"><strong>MU</strong><span>1130-1150</span></div>
              <div class="brief-item"><strong>SNDK / DRAM</strong><span>{watch_labels[0]}</span></div>
              <div class="brief-item"><strong>AMAT / ASML</strong><span>{watch_labels[1]}</span></div>
              <div class="brief-item"><strong>BTC / ETH</strong><span>{watch_labels[2]}</span></div>
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
        "image": f"{BASE_URL}{IMAGES[lang]}",
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
    <meta property="og:image" content="{BASE_URL}{IMAGES[lang]}">
    <meta property="og:site_name" content="GateAffiliate">
    <meta property="og:url" content="{BASE_URL}{path}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="theme-color" content="#07102b">
    <link rel="icon" href="/assets/gate-logo.ico" type="image/x-icon">
    <link rel="preload" as="image" href="{IMAGES[lang]}">
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
