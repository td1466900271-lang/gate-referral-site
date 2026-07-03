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

DATE = "2026-07-03"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-03-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-03-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-03-en.svg",
    "ru": "/daily/images/market-brief-2026-07-03-ru.svg",
}

META = {
    "zh-cn": {
        "title": "AI 硬件链继续出清，资金转向平台变现与 Crypto beta",
        "desc": "2026-07-03 GateAffiliate 每日市场日报：AI 硬件链继续洗筹，MU、SNDK、DRAM、SKHX 与 TSM 承压，META 算力变现和 Crypto beta 成为资金轮动重点。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "AI 硬件链继续出清，资金转向平台变现与 Crypto beta。",
        "summary": "今天的核心不是全面 risk-off，而是结构性切换：AI 硬件链继续高成交换手下跌，MU、SNDK、DRAM 与 SKHX 承压；资金更愿意追踪 META 算力变现叙事、平台股防御和局部 crypto beta。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "AI 硬體鏈繼續出清，資金轉向平台變現與 Crypto beta",
        "desc": "2026-07-03 GateAffiliate 每日市場日報：AI 硬體鏈繼續洗籌，MU、SNDK、DRAM、SKHX 與 TSM 承壓，META 算力變現和 Crypto beta 成為資金輪動重點。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "AI 硬體鏈繼續出清，資金轉向平台變現與 Crypto beta。",
        "summary": "今天的核心不是全面 risk-off，而是結構性切換：AI 硬體鏈繼續高成交換手下跌，MU、SNDK、DRAM 與 SKHX 承壓；資金更願意追蹤 META 算力變現敘事、平台股防禦和局部 crypto beta。",
        "tag": "最新",
    },
    "en": {
        "title": "AI hardware keeps clearing as capital rotates to platform monetization and crypto beta",
        "desc": "2026-07-03 GateAffiliate daily market brief: AI hardware continues to wash out, with MU, SNDK, DRAM, SKHX and TSM under pressure while META compute monetization and crypto beta lead the rotation.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "AI hardware keeps clearing as capital rotates to platform monetization and crypto beta.",
        "summary": "This is not a broad risk-off tape. It is a structural rotation: crowded AI hardware keeps falling on heavy volume, with MU, SNDK, DRAM and SKHX under pressure, while capital favors META's compute-monetization story, platform defensiveness and selected crypto beta.",
        "tag": "Latest",
    },
    "ru": {
        "title": "AI hardware продолжает очищение, капитал уходит в монетизацию платформ и crypto beta",
        "desc": "Ежедневный обзор GateAffiliate за 2026-07-03: AI hardware продолжает снижаться; MU, SNDK, DRAM, SKHX и TSM под давлением, а META compute monetization и crypto beta ведут ротацию.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "AI hardware продолжает очищение, капитал уходит в монетизацию платформ и crypto beta.",
        "summary": "Это не широкий risk-off, а структурная ротация: перегретый AI hardware падает на высоких объемах, MU, SNDK, DRAM и SKHX остаются под давлением, а капитал выбирает историю монетизации compute у META, защитные платформы и отдельный crypto beta.",
        "tag": "Свежий",
    },
}

CONCISE_SECTIONS = {
    "zh-cn": [
        ("核心结论", [
            "今天市场的主线是 AI 硬件链继续出清。MU、SNDK、DRAM、SKHX 跌幅和成交额都偏高，说明这不是低量回调，而是拥挤交易在高位重新定价。",
            "但这也不是全市场 risk-off。SP500 附近持平，BTC、ETH、SOL 和 HYPE 修复，资金并没有离开所有风险资产，而是从 AI 硬件扩产链转向平台变现、指数防御和局部 crypto beta。",
        ]),
        ("关键市场结构", [
            "TSM 中期仍是 AI 先进制程核心资产，但台股 2330 未能站稳 2500，盘中回到 2425/2430 附近，短线从突破确认变成 2415-2500 区间消化。",
            "MU 财报验证的中期逻辑没有被推翻，但永续价格逼近 1000 一线，已经进入关键防守区。若 1000-1050 不能止跌，记忆体交易还会继续降温。",
            "META 算力云化 / 出租过剩算力仍是今天最重要的 AI 变量。市场开始奖励“AI CapEx 如何变成收入”，而不是继续无差别奖励“谁继续买 GPU / 扩产”。",
        ]),
        ("交易框架", [
            "中期仍看好 AI 瓶颈资产，包括 TSM、HBM/DRAM、先进封装和设备链；短线则要等待 MU 守住 1000-1050、TSM 重回 2500、SKHX / SNDK / DRAM 停止高成交下跌。",
            "META 叙事对平台股偏利好，但对 GPU 租赁、neocloud 和部分硬件链可能是压力，因为可出租算力供给增加会让市场重新审视租赁价格和 CapEx 回报率。",
            "Crypto 的修复说明风险偏好仍在，但不能直接推导 AI 硬件马上反弹。当前更像资金在不同风险资产之间轮动，而不是同一条 AI 硬件主线全面回归。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "今天市場的主線是 AI 硬體鏈繼續出清。MU、SNDK、DRAM、SKHX 跌幅和成交額都偏高，說明這不是低量回調，而是擁擠交易在高位重新定價。",
            "但這也不是全市場 risk-off。SP500 附近持平，BTC、ETH、SOL 和 HYPE 修復，資金並沒有離開所有風險資產，而是從 AI 硬體擴產鏈轉向平台變現、指數防禦和局部 crypto beta。",
        ]),
        ("關鍵市場結構", [
            "TSM 中期仍是 AI 先進製程核心資產，但台股 2330 未能站穩 2500，盤中回到 2425/2430 附近，短線從突破確認變成 2415-2500 區間消化。",
            "MU 財報驗證的中期邏輯沒有被推翻，但永續價格逼近 1000 一線，已經進入關鍵防守區。若 1000-1050 不能止跌，記憶體交易還會繼續降溫。",
            "META 算力雲化 / 出租過剩算力仍是今天最重要的 AI 變量。市場開始獎勵「AI CapEx 如何變成收入」，而不是繼續無差別獎勵「誰繼續買 GPU / 擴產」。",
        ]),
        ("交易框架", [
            "中期仍看好 AI 瓶頸資產，包括 TSM、HBM/DRAM、先進封裝和設備鏈；短線則要等待 MU 守住 1000-1050、TSM 重回 2500、SKHX / SNDK / DRAM 停止高成交下跌。",
            "META 敘事對平台股偏利好，但對 GPU 租賃、neocloud 和部分硬體鏈可能是壓力，因為可出租算力供給增加會讓市場重新審視租賃價格和 CapEx 回報率。",
            "Crypto 的修復說明風險偏好仍在，但不能直接推導 AI 硬體馬上反彈。當前更像資金在不同風險資產之間輪動，而不是同一條 AI 硬體主線全面回歸。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "The main story is another clearing round in AI hardware. MU, SNDK, DRAM and SKHX are falling with heavy turnover, which looks more like crowded-position repricing than a quiet pullback.",
            "This is not broad risk-off. SP500 exposure is roughly stable, while BTC, ETH, SOL and HYPE improved. Capital is rotating out of the AI hardware buildout trade and into platform monetization, index defensiveness and selective crypto beta.",
        ]),
        ("Market Structure", [
            "TSM remains a core AI advanced-node asset, but 2330.TW failed to hold NT$2500 and moved back near 2425/2430 intraday. The short-term setup has shifted from breakout confirmation to digestion inside the 2415-2500 zone.",
            "Micron's medium-term demand thesis is not broken, but MU perpetuals near 1000 are now in a key defense area. If 1000-1050 fails to stabilize, the memory trade can keep cooling.",
            "META's compute-cloud and excess-capacity monetization story remains the key AI variable. The market is rewarding how AI CapEx becomes revenue, not simply who keeps buying GPUs or expanding capacity.",
        ]),
        ("Trading Frame", [
            "Medium term, AI bottleneck assets still matter: TSM, HBM/DRAM, advanced packaging and equipment remain strategic. Short term, the market needs MU to hold 1000-1050, TSM to reclaim 2500, and SKHX / SNDK / DRAM to stop falling on heavy volume.",
            "META is constructive for platform names, but it can pressure GPU rental, neocloud and parts of the hardware chain if more rentable compute supply causes investors to revisit rental prices and CapEx returns.",
            "Crypto strength shows risk appetite is still alive, but it does not automatically mean AI hardware is ready to rebound. This is rotation across risk assets, not a clean return to the same hardware-led AI trade.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Главная тема дня — очередная чистка в AI hardware. MU, SNDK, DRAM и SKHX падают при высоком обороте, поэтому это больше похоже на переоценку перегретого позиционирования, а не на тихий откат.",
            "Это не широкий risk-off. SP500 остается около нуля, BTC, ETH, SOL и HYPE восстанавливаются. Капитал уходит из сделки AI buildout в монетизацию платформ, защиту через индексы и выборочный crypto beta.",
        ]),
        ("Структура Рынка", [
            "TSM остается ключевым активом advanced nodes для AI, но 2330.TW не удержала NT$2500 и вернулась к 2425/2430 intraday. Краткосрочно это уже не breakout, а переваривание в зоне 2415-2500.",
            "Среднесрочная логика спроса на Micron не сломана, но MU perpetual около 1000 входит в ключевую зону защиты. Если 1000-1050 не удержится, memory trade может охлаждаться дальше.",
            "История META про compute cloud и монетизацию избыточных мощностей остается главным AI-фактором. Рынок награждает путь от AI CapEx к выручке, а не просто покупку GPU и расширение capacity.",
        ]),
        ("Торговая Рамка", [
            "Среднесрочно активы узких мест AI остаются важными: TSM, HBM/DRAM, advanced packaging и оборудование. Краткосрочно нужно увидеть, что MU держит 1000-1050, TSM возвращает 2500, а SKHX / SNDK / DRAM перестают падать на высоком обороте.",
            "META позитивна для платформ, но может давить на GPU rental, neocloud и часть hardware-цепочки, если рост доступной compute supply заставит рынок пересмотреть цены аренды и окупаемость CapEx.",
            "Сила крипты показывает, что аппетит к риску жив, но это не значит, что AI hardware сразу готов к отскоку. Сейчас это ротация между риск-активами, а не чистое возвращение к hardware-led AI trade.",
        ]),
    ],
}

SOURCE_URLS = [
    ("businessinsider-meta", "https://www.businessinsider.com/meta-stock-cloud-computing-ai-compute-tech-stocks-data-centers-2026-7"),
    ("marketwatch-meta", "https://www.marketwatch.com/story/is-meta-giving-up-on-cutting-edge-ai-wall-street-is-divided-over-potential-cloud-pivot-7c5ffc5d"),
    ("ibd-meta-micron", "https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-meta-jumps-spacex-micron-tesla-deliveries-jobs-report/"),
    ("micron-q3", "https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-record-results-third-quarter"),
    ("goldman-capex", "https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out"),
    ("bea-pce", "https://www.bea.gov/news/2026/personal-income-and-outlays-may-2026"),
    ("tomshardware-tsmc", "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-is-reportedly-hiking-prices-for-all-advanced-nodes-accounting-for-74-percent-of-the-companys-wafer-business-nvidia-amd-apple-qualcomm-and-others-will-face-higher-wafer-costs"),
    ("twse", "https://mis.twse.com.tw/stock/index.jsp"),
    ("traderxyz-api", "https://api.hyperliquid.xyz/info"),
]

SOURCE_LABELS = {
    "zh-cn": {
        "businessinsider-meta": "Business Insider：Meta AI 算力云计划",
        "marketwatch-meta": "MarketWatch：华尔街讨论 Meta 云转向",
        "ibd-meta-micron": "IBD：Meta 上涨与 Micron、硬件链回落",
        "micron-q3": "Micron FY2026 Q3 官方财报",
        "goldman-capex": "Goldman Sachs AI 资本开支框架",
        "bea-pce": "BEA 个人收入与支出数据",
        "tomshardware-tsmc": "Tom's Hardware：TSMC 先进节点价格报道",
        "twse": "TWSE 实时行情",
        "traderxyz-api": "TraderXYZ / Hyperliquid 数据接口",
    },
    "zh-hant": {
        "businessinsider-meta": "Business Insider：Meta AI 算力雲計劃",
        "marketwatch-meta": "MarketWatch：華爾街討論 Meta 雲轉向",
        "ibd-meta-micron": "IBD：Meta 上漲與 Micron、硬體鏈回落",
        "micron-q3": "Micron FY2026 Q3 官方財報",
        "goldman-capex": "Goldman Sachs AI 資本開支框架",
        "bea-pce": "BEA 個人收入與支出數據",
        "tomshardware-tsmc": "Tom's Hardware：TSMC 先進節點價格報導",
        "twse": "TWSE 即時行情",
        "traderxyz-api": "TraderXYZ / Hyperliquid 數據接口",
    },
    "en": {
        "businessinsider-meta": "Business Insider: Meta AI compute cloud plan",
        "marketwatch-meta": "MarketWatch: Wall Street debates Meta cloud pivot",
        "ibd-meta-micron": "IBD: Meta jump and Micron hardware-chain pressure",
        "micron-q3": "Micron FY2026 Q3 earnings release",
        "goldman-capex": "Goldman Sachs AI CapEx framework",
        "bea-pce": "BEA Personal Income and Outlays",
        "tomshardware-tsmc": "Tom's Hardware: TSMC advanced-node pricing report",
        "twse": "TWSE real-time quotes",
        "traderxyz-api": "TraderXYZ / Hyperliquid data API",
    },
    "ru": {
        "businessinsider-meta": "Business Insider: план Meta по AI compute cloud",
        "marketwatch-meta": "MarketWatch: дискуссия Wall Street о cloud-повороте Meta",
        "ibd-meta-micron": "IBD: рост Meta и давление на Micron/hardware",
        "micron-q3": "Официальный отчет Micron за FY2026 Q3",
        "goldman-capex": "Goldman Sachs: рамка AI-капзатрат",
        "bea-pce": "BEA: личные доходы и расходы",
        "tomshardware-tsmc": "Tom's Hardware: цены TSMC на advanced nodes",
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
        "zh-cn": ("1000-1050 防守区", "2415-2500 消化区", "算力变现", "记忆体链压力", "crypto beta"),
        "zh-hant": ("1000-1050 防守區", "2415-2500 消化區", "算力變現", "記憶體鏈壓力", "crypto beta"),
        "en": ("1000-1050 defense", "2415-2500 digestion", "compute monetization", "memory-chain pressure", "crypto beta"),
        "ru": ("защита 1000-1050", "зона 2415-2500", "монетизация compute", "давление memory-chain", "crypto beta"),
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
              <div class="brief-item"><strong>MU</strong><span>{watch_labels[0]}</span></div>
              <div class="brief-item"><strong>TSM</strong><span>{watch_labels[1]}</span></div>
              <div class="brief-item"><strong>META</strong><span>{watch_labels[2]}</span></div>
              <div class="brief-item"><strong>SKHX / SNDK / DRAM</strong><span>{watch_labels[3]}</span></div>
              <div class="brief-item"><strong>BTC / ETH / SOL / HYPE</strong><span>{watch_labels[4]}</span></div>
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
      <a class="history-link" href="{daily_slug(lang, "2026-07-02")}"><span class="history-date">2026-07-02</span><span><span class="history-title">AI compute monetization / hardware stress test</span><span class="history-summary">Previous market brief.</span></span><span class="history-tag">Archive</span></a>
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
    text = re.sub(
        r'(<div class="hero-actions"><a class="button button-primary" href=")[^"]+(">)',
        rf'\1{daily_slug(lang, DATE)}\2',
        text,
        count=1,
    )
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
