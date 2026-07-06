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

DATE = "2026-07-06"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-06-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-06-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-06-en.svg",
    "ru": "/daily/images/market-brief-2026-07-06-ru.svg",
}

META = {
    "zh-cn": {
        "title": "TSM 重新测试 2500，AI 硬件链进入关键防守期",
        "desc": "2026-07-06 GateAffiliate 每日市场日报：AI 硬件链仍在清洗后的关键防守期，TSM 重新测试 2500，MU 1000-1050 成为记忆体链核心观察区，Crypto beta 维持风险偏好。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "TSM 重新测试 2500，AI 硬件链进入关键防守期。",
        "summary": "AI 硬件链仍在清洗后的防守阶段，但台积电重新触及 2500 给出边际修复信号。MU 仍在 1000 附近高成交换手，SKHX、DRAM、SNDK 还没完全止跌；Crypto 偏强说明风险偏好没坏，但不能直接等同半导体修复。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "TSM 重新測試 2500，AI 硬體鏈進入關鍵防守期",
        "desc": "2026-07-06 GateAffiliate 每日市場日報：AI 硬體鏈仍在清洗後的關鍵防守期，TSM 重新測試 2500，MU 1000-1050 成為記憶體鏈核心觀察區，Crypto beta 維持風險偏好。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "TSM 重新測試 2500，AI 硬體鏈進入關鍵防守期。",
        "summary": "AI 硬體鏈仍在清洗後的防守階段，但台積電重新觸及 2500 給出邊際修復信號。MU 仍在 1000 附近高成交換手，SKHX、DRAM、SNDK 還沒完全止跌；Crypto 偏強說明風險偏好沒壞，但不能直接等同半導體修復。",
        "tag": "最新",
    },
    "en": {
        "title": "TSM retests 2500 as AI hardware enters a key defense phase",
        "desc": "2026-07-06 GateAffiliate daily market brief: AI hardware remains in a post-washout defense phase, TSM retests NT$2500, MU 1000-1050 is the key memory-chain level, and crypto beta keeps risk appetite alive.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "TSM retests 2500 as AI hardware enters a key defense phase.",
        "summary": "AI hardware is still defending after the washout, but TSM retesting NT$2500 is a marginal repair signal. MU is still changing hands near 1000, while SKHX, DRAM and SNDK have not fully stabilized. Crypto is firm, but that does not automatically confirm a semiconductor rebound.",
        "tag": "Latest",
    },
    "ru": {
        "title": "TSM снова тестирует 2500, аппаратная AI-цепочка входит в фазу защиты",
        "desc": "Ежедневный обзор GateAffiliate за 2026-07-06: аппаратная AI-цепочка остается в фазе защиты после чистки, TSM тестирует NT$2500, зона MU 1000-1050 важна для цепочки памяти, а крипто-бета поддерживает риск-аппетит.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "TSM снова тестирует 2500, аппаратная AI-цепочка входит в фазу защиты.",
        "summary": "Аппаратная AI-цепочка все еще защищается после чистки, но повторный тест TSM NT$2500 дает сигнал частичного восстановления. MU торгуется около 1000 с высоким оборотом, а SKHX, DRAM и SNDK еще не стабилизировались полностью. Крипторынок сильнее, но это не подтверждает автоматический отскок полупроводников.",
        "tag": "Свежий",
    },
}

CONCISE_SECTIONS = {
    "zh-cn": [
        ("核心结论", [
            "AI 硬件链仍处在清洗后的关键防守期，但今天的边际变化更积极：台积电盘中重新测试 2500，说明亚洲 AI 核心资产开始出现承接。",
            "记忆体链还没有完全修复。MU 仍在 1000 附近高成交换手，SKHX 继续偏弱，DRAM 和 SNDK 的跌幅虽然收敛，但还缺少主动买盘回流。",
        ]),
        ("关键市场结构", [
            "TSM 比 MU 更强。台积电 2330 盘中高点触及 2500，随后回到 2470/2475 附近，短线判断从“前高失败”转为“关键压力位二次测试”。",
            "MU 1000-1050 是本周最重要的记忆体观察区。守住并横盘，第一轮清洗可能接近尾声；如果跌破 1000，技术盘和情绪盘可能继续退潮。",
            "Crypto 偏强，尤其 HYPE 表现突出，说明风险偏好没有全面崩坏。但股票永续里的 MU、SKHX 仍弱，所以不能把 crypto 反弹直接等同于 AI 半导体确认修复。",
        ]),
        ("交易框架", [
            "中期仍看好 AI 瓶颈资产，包括 TSM、MU、HBM/DRAM、先进封装和设备链；短线则要尊重价格，先看 TSM 是否站稳 2500、MU 是否守住 1000-1050。",
            "META 算力变现叙事仍在改变市场定价：平台股会被奖励收入化路径，硬件扩产链则需要证明 GPU 租赁价格、利用率和 CapEx 回报率。",
            "本周的确认条件很简单：MU 不破 1000、TSM 站稳 2500、SKHX / SNDK / DRAM 停止高成交下跌。满足前，维持中期看多、短线谨慎。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "AI 硬體鏈仍處在清洗後的關鍵防守期，但今天的邊際變化更積極：台積電盤中重新測試 2500，說明亞洲 AI 核心資產開始出現承接。",
            "記憶體鏈還沒有完全修復。MU 仍在 1000 附近高成交換手，SKHX 繼續偏弱，DRAM 和 SNDK 的跌幅雖然收斂，但還缺少主動買盤回流。",
        ]),
        ("關鍵市場結構", [
            "TSM 比 MU 更強。台積電 2330 盤中高點觸及 2500，隨後回到 2470/2475 附近，短線判斷從「前高失敗」轉為「關鍵壓力位二次測試」。",
            "MU 1000-1050 是本週最重要的記憶體觀察區。守住並橫盤，第一輪清洗可能接近尾聲；如果跌破 1000，技術盤和情緒盤可能繼續退潮。",
            "Crypto 偏強，尤其 HYPE 表現突出，說明風險偏好沒有全面崩壞。但股票永續裡的 MU、SKHX 仍弱，所以不能把 crypto 反彈直接等同於 AI 半導體確認修復。",
        ]),
        ("交易框架", [
            "中期仍看好 AI 瓶頸資產，包括 TSM、MU、HBM/DRAM、先進封裝和設備鏈；短線則要尊重價格，先看 TSM 是否站穩 2500、MU 是否守住 1000-1050。",
            "META 算力變現敘事仍在改變市場定價：平台股會被獎勵收入化路徑，硬體擴產鏈則需要證明 GPU 租賃價格、利用率和 CapEx 回報率。",
            "本週的確認條件很簡單：MU 不破 1000、TSM 站穩 2500、SKHX / SNDK / DRAM 停止高成交下跌。滿足前，維持中期看多、短線謹慎。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "AI hardware is still in a post-washout defense phase, but today's marginal signal is better: TSM retested NT$2500 intraday, showing some support for Asia's core AI asset.",
            "The memory chain is not fully repaired. MU is still changing hands near 1000 on heavy volume, SKHX remains weak, and DRAM / SNDK have only shown less downside pressure, not clear active buying.",
        ]),
        ("Market Structure", [
            "TSM is stronger than MU. 2330.TW touched NT$2500 intraday before easing back near 2470/2475, shifting the short-term setup from failed breakout to a second test of key resistance.",
            "MU 1000-1050 is the most important memory-chain zone this week. Holding and moving sideways would suggest the first washout is close to done; breaking 1000 could invite more technical selling.",
            "Crypto is firm, especially HYPE, which shows risk appetite has not collapsed. But MU and SKHX remain weak in equity perpetuals, so a crypto rebound is not the same as confirmed AI semiconductor repair.",
        ]),
        ("Trading Frame", [
            "Medium term, AI bottleneck assets still matter: TSM, MU, HBM/DRAM, advanced packaging and equipment. Short term, price comes first: TSM needs to hold 2500 and MU needs to defend 1000-1050.",
            "META's compute-monetization narrative continues to reshape pricing. Platforms get rewarded for revenue paths, while the hardware buildout chain must prove GPU rental pricing, utilization and CapEx returns.",
            "This week's confirmation checklist is simple: MU above 1000, TSM above 2500, and SKHX / SNDK / DRAM no longer falling on heavy volume. Until then, the stance is medium-term bullish but short-term cautious.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Аппаратная AI-цепочка все еще находится в фазе защиты после чистки, но сегодняшний маржинальный сигнал лучше: TSM внутри дня снова протестировала NT$2500, показывая поддержку ключевого AI-актива Азии.",
            "Цепочка памяти еще не восстановилась полностью. MU по-прежнему торгуется около 1000 на высоком объеме, SKHX остается слабой, а DRAM / SNDK пока показывают только снижение давления продаж, а не явный возврат покупателей.",
        ]),
        ("Структура Рынка", [
            "TSM сильнее MU. 2330.TW коснулась NT$2500 внутри дня, затем вернулась к 2470/2475, поэтому краткосрочная картина сместилась от неудачного прорыва к повторному тесту ключевого сопротивления.",
            "Зона MU 1000-1050 — главный уровень цепочки памяти на этой неделе. Удержание и боковик покажут, что первая чистка близка к завершению; пробой 1000 может запустить новые технические продажи.",
            "Крипторынок выглядит сильнее, особенно HYPE, что говорит о сохранении риск-аппетита. Но MU и SKHX в акционных перпетуалах остаются слабыми, поэтому отскок крипто не является подтверждением восстановления AI-полупроводников.",
        ]),
        ("Торговая Рамка", [
            "Среднесрочно активы узких мест AI остаются важными: TSM, MU, HBM/DRAM, advanced packaging и оборудование. Краткосрочно важнее цена: TSM нужно удержать 2500, а MU — зону 1000-1050.",
            "Нарратив META о монетизации вычислений продолжает менять оценку рынка. Платформы получают премию за путь к выручке, а аппаратная цепочка расширения должна доказать цены аренды GPU, загрузку и окупаемость CapEx.",
            "Чеклист недели простой: MU выше 1000, TSM выше 2500, SKHX / SNDK / DRAM больше не падают на высоком объеме. До этого позиция остается среднесрочно позитивной, но краткосрочно осторожной.",
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
        "businessinsider-meta": "Business Insider: план Meta по облаку AI-вычислений",
        "marketwatch-meta": "MarketWatch: дискуссия Уолл-стрит о cloud-повороте Meta",
        "ibd-meta-micron": "IBD: рост Meta и давление на Micron и аппаратную цепочку",
        "micron-q3": "Официальный отчет Micron за FY2026 Q3",
        "goldman-capex": "Goldman Sachs: рамка AI-капзатрат",
        "bea-pce": "BEA: личные доходы и расходы",
        "tomshardware-tsmc": "Tom's Hardware: цены TSMC на передовые техпроцессы",
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
        "zh-cn": ("1000-1050 防守区", "2500 二次测试", "算力变现", "等待止跌确认", "HYPE 相对强"),
        "zh-hant": ("1000-1050 防守區", "2500 二次測試", "算力變現", "等待止跌確認", "HYPE 相對強"),
        "en": ("1000-1050 defense", "2500 retest", "compute monetization", "waiting for stabilization", "HYPE relative strength"),
        "ru": ("защита 1000-1050", "повторный тест 2500", "монетизация вычислений", "ожидание стабилизации", "HYPE сильнее"),
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
    previous = {
        "zh-cn": ("AI 硬件链继续出清，资金转向平台变现与 Crypto beta", "上一篇市场日报。", "归档"),
        "zh-hant": ("AI 硬體鏈繼續出清，資金轉向平台變現與 Crypto beta", "上一篇市場日報。", "歸檔"),
        "en": ("AI hardware clearing / platform monetization / crypto beta", "Previous market brief.", "Archive"),
        "ru": ("Чистка AI-сектора / монетизация платформ / крипто-бета", "Предыдущий обзор рынка.", "Архив"),
    }[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-07-03")}"><span class="history-date">2026-07-03</span><span><span class="history-title">{html.escape(previous[0])}</span><span class="history-summary">{html.escape(previous[1])}</span></span><span class="history-tag">{html.escape(previous[2])}</span></a>
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
