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

DATE = "2026-07-02"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-02-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-02-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-02-en.svg",
    "ru": "/daily/images/market-brief-2026-07-02-ru.svg",
}

META = {
    "zh-cn": {
        "title": "AI 交易切向算力变现，半导体硬件链进入压力测试",
        "desc": "2026-07-02 GateAffiliate 每日市场日报：Meta 算力变现叙事走强，MU、TSM、SNDK、DRAM 和半导体 ETF 回落，Crypto 风险偏好修复但信号分化。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "AI 交易切向算力变现，半导体硬件链进入压力测试。",
        "summary": "今天的主线不是 AI 全面上涨，而是风格切换：半导体硬件链回落，META 因 AI 算力变现叙事大涨。资金开始追问 AI CapEx 能否转成收入，MU、SNDK、DRAM 与 TSM 则进入高位消化。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "AI 交易切向算力變現，半導體硬體鏈進入壓力測試",
        "desc": "2026-07-02 GateAffiliate 每日市場日報：Meta 算力變現敘事走強，MU、TSM、SNDK、DRAM 和半導體 ETF 回落，Crypto 風險偏好修復但信號分化。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "AI 交易切向算力變現，半導體硬體鏈進入壓力測試。",
        "summary": "今天的主線不是 AI 全面上漲，而是風格切換：半導體硬體鏈回落，META 因 AI 算力變現敘事大漲。資金開始追問 AI CapEx 能否轉成收入，MU、SNDK、DRAM 與 TSM 則進入高位消化。",
        "tag": "最新",
    },
    "en": {
        "title": "AI trade rotates toward compute monetization as hardware enters a stress test",
        "desc": "2026-07-02 GateAffiliate daily market brief: Meta's AI compute monetization narrative strengthens while MU, TSM, SNDK, DRAM and semiconductor ETFs pull back.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "AI trade rotates toward compute monetization as hardware enters a stress test.",
        "summary": "The market is no longer simply buying all AI exposure. Semiconductor hardware sold off, while META surged on the idea that excess AI compute can be monetized. Capital is now asking whether AI CapEx can become revenue, while MU, SNDK, DRAM and TSM digest crowded positioning.",
        "tag": "Latest",
    },
    "ru": {
        "title": "AI-сделка смещается к монетизации вычислений, а hardware проходит стресс-тест",
        "desc": "Ежедневный обзор GateAffiliate за 2026-07-02: нарратив монетизации AI-вычислений Meta усиливается, а MU, TSM, SNDK, DRAM и ETF полупроводников снижаются.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "AI-сделка смещается к монетизации вычислений, а hardware проходит стресс-тест.",
        "summary": "Рынок больше не покупает весь AI одинаково. Полупроводниковый hardware снижается, а META резко выросла на идее монетизации избыточных AI-вычислений. Теперь капитал проверяет, может ли AI CapEx превращаться в выручку, пока MU, SNDK, DRAM и TSM переваривают перегретое позиционирование.",
        "tag": "Свежий",
    },
}

CONCISE_SECTIONS = {
    "zh-cn": [
        ("核心结论", [
            "今天最重要的变化是 AI 交易的定价焦点从硬件建设切到算力变现。SMH、SOXX、TSM ADR、MU、AMD、AMAT、ASML 同步回落，说明硬件链正在做压力测试；但 META 大涨，说明市场开始奖励能够把 AI CapEx 转成云收入、租赁收入或平台现金流的公司。",
            "这不是 AI 主题结束，而是 AI 主题从“谁卖铲子”切换到“谁能提升算力利用率”。短线对半导体硬件链要更严格，尤其是 MU、SNDK、DRAM 和 SKHX 这种高拥挤度方向。",
        ]),
        ("关键市场结构", [
            "美股指数本身没有崩：SPY 和 QQQ 小幅上涨，但半导体 ETF 跌幅明显，MU 跌超 10%，AMD 跌超 8%，TSM ADR 跌超 3%。这说明压力集中在 AI 硬件链，不是全市场风险偏好崩塌。",
            "台积电台股盘中回到 2460/2465 附近，昨天站上 2500 后没有继续突破。中期代工逻辑仍强，但短线从突破确认回到前高震荡，2440-2460 成为第一观察带。",
            "TraderXYZ / Hyperliquid 上 MU、SNDK、DRAM 同时大跌且成交额高，代表记忆体主线正在经历高位清洗；META 进入成交前十并上涨，是今天最清晰的风格切换信号。",
        ]),
        ("交易框架", [
            "中期仍看好 AI 瓶颈资产，包括 TSM、HBM/DRAM、先进封装和设备链，但短线不适合把强财报直接等同于股价继续单边上涨。MU 若守不住 1000-1050，记忆体交易还会继续降温。",
            "META 的上涨对平台股是利好，但对硬件链未必全是利好。若市场开始担心 GPU 租赁价格和算力供给过剩，部分硬件和云算力资产的估值会被重新审视。",
            "加密资产今天偏强，BTC、ETH、SOL 修复，但 HYPE 走弱且硬件链下跌，说明跨市场信号不一致。不能用加密反弹直接推导 AI 硬件马上修复。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "今天最重要的變化是 AI 交易的定價焦點從硬體建設切到算力變現。SMH、SOXX、TSM ADR、MU、AMD、AMAT、ASML 同步回落，說明硬體鏈正在做壓力測試；但 META 大漲，說明市場開始獎勵能把 AI CapEx 轉成雲收入、租賃收入或平台現金流的公司。",
            "這不是 AI 主題結束，而是 AI 主題從「誰賣鏟子」切換到「誰能提升算力利用率」。短線對半導體硬體鏈要更嚴格，尤其是 MU、SNDK、DRAM 和 SKHX 這種高擁擠度方向。",
        ]),
        ("關鍵市場結構", [
            "美股指數本身沒有崩：SPY 和 QQQ 小幅上漲，但半導體 ETF 跌幅明顯，MU 跌超 10%，AMD 跌超 8%，TSM ADR 跌超 3%。這說明壓力集中在 AI 硬體鏈，不是全市場風險偏好崩塌。",
            "台積電台股盤中回到 2460/2465 附近，昨天站上 2500 後沒有繼續突破。中期代工邏輯仍強，但短線從突破確認回到前高震盪，2440-2460 成為第一觀察帶。",
            "TraderXYZ / Hyperliquid 上 MU、SNDK、DRAM 同時大跌且成交額高，代表記憶體主線正在經歷高位清洗；META 進入成交前十並上漲，是今天最清晰的風格切換信號。",
        ]),
        ("交易框架", [
            "中期仍看好 AI 瓶頸資產，包括 TSM、HBM/DRAM、先進封裝和設備鏈，但短線不適合把強財報直接等同於股價繼續單邊上漲。MU 若守不住 1000-1050，記憶體交易還會繼續降溫。",
            "META 的上漲對平台股是利好，但對硬體鏈未必全是利好。若市場開始擔心 GPU 租賃價格和算力供給過剩，部分硬體和雲算力資產的估值會被重新審視。",
            "加密資產今天偏強，BTC、ETH、SOL 修復，但 HYPE 走弱且硬體鏈下跌，說明跨市場信號不一致。不能用加密反彈直接推導 AI 硬體馬上修復。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "The most important shift is that the AI trade is moving from hardware buildout toward compute monetization. SMH, SOXX, TSM ADR, MU, AMD, AMAT and ASML fell together, while META surged on the idea that excess AI compute can become cloud or infrastructure revenue.",
            "This does not mean the AI theme is over. It means the market is moving from rewarding the sellers of shovels to rewarding companies that can raise utilization and returns on AI CapEx. Short term, crowded hardware winners need stricter risk rules.",
        ]),
        ("Market Structure", [
            "The broad tape did not break: SPY and QQQ were slightly higher. The pressure was concentrated in AI hardware, with MU down more than 10%, AMD down more than 8%, TSM ADR down more than 3%, and semiconductor ETFs sharply lower.",
            "TSM 2330.TW moved back near 2460/2465 after failing to extend above NT$2500. The medium-term foundry thesis is intact, but the short-term setup has moved from breakout confirmation back into resistance digestion.",
            "On TraderXYZ / Hyperliquid, MU, SNDK and DRAM fell together on heavy notional volume. That is a clear memory-chain washout. META entering the top flow list while rising is the cleanest style-rotation signal today.",
        ]),
        ("Trading Frame", [
            "Medium term, AI bottleneck assets still matter: TSM, HBM/DRAM, advanced packaging and equipment remain strategic. Short term, strong earnings are not enough when positioning is crowded; MU needs to hold 1000-1050 to stop the memory trade from cooling further.",
            "META strength is positive for platform monetization, but it can be mixed for hardware. If investors worry about GPU rental prices or excess compute supply, some hardware and neocloud valuations may need to reset.",
            "Crypto improved, with BTC, ETH and SOL firmer, but HYPE weakened and AI hardware sold off. Cross-asset signals are split, so a crypto bounce is not enough to call an immediate hardware rebound.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Главный сдвиг дня: AI-сделка переходит от темы строительства hardware к теме монетизации вычислений. SMH, SOXX, TSM ADR, MU, AMD, AMAT и ASML снижались вместе, а META резко выросла на идее, что избыточные AI-вычисления можно превратить в облачную или инфраструктурную выручку.",
            "Это не конец AI-темы. Это переход от награды продавцам оборудования к награде компаниям, которые могут повысить загрузку инфраструктуры и окупаемость AI CapEx. Краткосрочно для перегретых hardware-победителей нужны более строгие правила риска.",
        ]),
        ("Структура Рынка", [
            "Широкий рынок не сломался: SPY и QQQ немного выросли. Давление было сосредоточено в AI hardware: MU упала более чем на 10%, AMD более чем на 8%, TSM ADR более чем на 3%, а ETF полупроводников заметно снизились.",
            "TSM 2330.TW вернулась к зоне 2460/2465 после неудачной попытки продолжить движение выше NT$2500. Среднесрочная логика foundry остается сильной, но краткосрочно это снова зона сопротивления и переваривания.",
            "На TraderXYZ / Hyperliquid MU, SNDK и DRAM падали вместе при высоком обороте. Это явная чистка в цепочке памяти. META в топе потоков и с ростом — самый чистый сигнал ротации стиля.",
        ]),
        ("Торговая Рамка", [
            "Среднесрочно активы узких мест AI остаются важными: TSM, HBM/DRAM, advanced packaging и оборудование. Но краткосрочно сильной отчетности недостаточно, если позиционирование перегрето; MU нужно удержать 1000-1050, чтобы остановить дальнейшее охлаждение memory trade.",
            "Рост META позитивен для платформенной монетизации, но для hardware сигнал смешанный. Если инвесторы начнут опасаться цен аренды GPU и избытка вычислительных мощностей, часть hardware и neocloud-оценок может быть пересмотрена.",
            "Крипта улучшилась: BTC, ETH и SOL сильнее, но HYPE слабее, а AI hardware падает. Межрыночные сигналы расходятся, поэтому отскок крипты сам по себе не подтверждает немедленное восстановление hardware.",
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
        "zh-cn": ("1000-1050 支撑", "2440-2500 区间", "算力变现", "记忆体压力", "风险偏好"),
        "zh-hant": ("1000-1050 支撐", "2440-2500 區間", "算力變現", "記憶體壓力", "風險偏好"),
        "en": ("1000-1050 support", "2440-2500 range", "compute monetization", "memory pressure", "risk appetite"),
        "ru": ("поддержка 1000-1050", "диапазон 2440-2500", "монетизация compute", "давление памяти", "аппетит к риску"),
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
              <div class="brief-item"><strong>SNDK / DRAM</strong><span>{watch_labels[3]}</span></div>
              <div class="brief-item"><strong>BTC / ETH</strong><span>{watch_labels[4]}</span></div>
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
      <a class="history-link" href="{daily_slug(lang, "2026-07-01")}"><span class="history-date">2026-07-01</span><span><span class="history-title">AI semiconductor confirmation / TSM / equipment</span><span class="history-summary">Previous market brief.</span></span><span class="history-tag">Archive</span></a>
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
    text = re.sub(r'href="' + re.escape(daily_slug(lang, "2026-07-01")) + r'"', f'href="{daily_slug(lang, DATE)}"', text, count=1)
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
