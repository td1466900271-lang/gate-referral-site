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

DATE = "2026-07-07"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-07-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-07-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-07-en.svg",
    "ru": "/daily/images/market-brief-2026-07-07-ru.svg",
}

META = {
    "zh-cn": {
        "title": "机构看多与永续去风险分歧，存储链仍是短线核心矛盾",
        "desc": "2026-07-07 GateAffiliate 每日市场日报：AI 硬件链中期逻辑未破，但 TraderXYZ / Hyperliquid 上 MU、SKHX、SNDK、DRAM 高成交下跌，机构对 Micron 的多头观点与衍生品去风险形成分歧。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "机构看多与永续去风险分歧，存储链仍是短线核心矛盾。",
        "summary": "AI 硬件链中期逻辑没有破坏，但今天不能只看正股和机构乐观。TraderXYZ / Hyperliquid 上 MU、SKHX、SNDK、DRAM 同时高成交下跌，说明存储链仍在去杠杆；TSMC 早盘偏强，但 2500 新台币仍是关键确认位。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "機構看多與永續去風險分歧，記憶體鏈仍是短線核心矛盾",
        "desc": "2026-07-07 GateAffiliate 每日市場日報：AI 硬體鏈中期邏輯未破，但 TraderXYZ / Hyperliquid 上 MU、SKHX、SNDK、DRAM 高成交下跌，機構對 Micron 的多頭觀點與衍生品去風險形成分歧。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "機構看多與永續去風險分歧，記憶體鏈仍是短線核心矛盾。",
        "summary": "AI 硬體鏈中期邏輯沒有破壞，但今天不能只看正股和機構樂觀。TraderXYZ / Hyperliquid 上 MU、SKHX、SNDK、DRAM 同時高成交下跌，說明記憶體鏈仍在去槓桿；TSMC 早盤偏強，但 2500 新台幣仍是關鍵確認位。",
        "tag": "最新",
    },
    "en": {
        "title": "Institutional optimism clashes with perpetual de-risking across the memory chain",
        "desc": "2026-07-07 GateAffiliate daily market brief: AI hardware's medium-term thesis is intact, but MU, SKHX, SNDK and DRAM are still falling on heavy TraderXYZ / Hyperliquid volume as Micron bulls and derivatives de-risking diverge.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "Institutional optimism clashes with perpetual de-risking across the memory chain.",
        "summary": "AI hardware's medium-term thesis is not broken, but today's signal is split. Cash-equity and institutional views are more constructive, while TraderXYZ / Hyperliquid still shows high-volume downside in MU, SKHX, SNDK and DRAM. TSMC is firmer early, but NT$2500 remains the key confirmation level.",
        "tag": "Latest",
    },
    "ru": {
        "title": "Оптимизм институтов расходится со снижением риска в перпетуалах цепочки памяти",
        "desc": "Ежедневный обзор GateAffiliate за 2026-07-07: среднесрочная логика аппаратной AI-цепочки не сломана, но MU, SKHX, SNDK и DRAM падают на высоком объеме TraderXYZ / Hyperliquid, создавая разрыв между мнением институционалов и деривативами.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "Оптимизм институтов расходится со снижением риска в перпетуалах цепочки памяти.",
        "summary": "Среднесрочная логика аппаратной AI-цепочки не сломана, но сигнал дня разделен. Акции и институциональные оценки выглядят конструктивнее, а TraderXYZ / Hyperliquid все еще показывает высокий объем снижения по MU, SKHX, SNDK и DRAM. TSMC сильнее утром, но NT$2500 остается ключевым уровнем подтверждения.",
        "tag": "Свежий",
    },
}

CONCISE_SECTIONS = {
    "zh-cn": [
        ("核心结论", [
            "今天的重点不是“AI 硬件链继续上涨”，而是正股市场和机构观点偏乐观，但 TraderXYZ / Hyperliquid 的存储链永续仍在明显去风险。",
            "中期逻辑没有破坏：TSMC、HBM、DRAM、先进封装、GPU / AI 服务器仍是未来几个季度的重要主线。但短线不能忽视 MU、SKHX、SNDK、DRAM 同时高成交下跌带来的波动风险。",
        ]),
        ("关键市场结构", [
            "TSMC 早盘参考买卖盘约 2470 / 2475，高于前收 2460，但这还不能等同全天突破确认。2500 新台币仍是最关键压力位，只有站稳并配合成交，才更像有效突破。",
            "TraderXYZ / Hyperliquid 上 SKHX、MU、SNDK、DRAM 同时进入高成交下跌名单，说明衍生品端仍在对存储链减仓或对冲。这更像拥挤交易后的去杠杆，而不是行业中期逻辑被推翻。",
            "机构端出现明显分歧。UBS 对 Micron 仍然偏多，把近期回调视为买点；但永续合约端显示 MU 跌破 1000 附近后仍有卖压。这个分歧本身就是今天最重要的信号。",
        ]),
        ("交易框架", [
            "AI 硬件链仍维持中期多头框架，但短线降低追涨冲动。TSMC 要看 2500 是否有效站稳，不能把盘前或早盘集合竞价直接当作全天趋势确认。",
            "存储链重点看 MU 是否重新站回 1000-1050，以及 SK Hynix / Samsung 是否释放 DRAM / HBM 价格或供应端的积极信息。若正股修复且永续止跌，多头才算重新接管。",
            "对机构明显看多、但衍生品明显看空的标的，不急于只站一边。更好的确认方式是等待正股成交、期权、ETF 和 TraderXYZ 信号相互验证。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "今天的重點不是「AI 硬體鏈繼續上漲」，而是正股市場和機構觀點偏樂觀，但 TraderXYZ / Hyperliquid 的記憶體鏈永續仍在明顯去風險。",
            "中期邏輯沒有破壞：TSMC、HBM、DRAM、先進封裝、GPU / AI 伺服器仍是未來幾個季度的重要主線。但短線不能忽視 MU、SKHX、SNDK、DRAM 同時高成交下跌帶來的波動風險。",
        ]),
        ("關鍵市場結構", [
            "TSMC 早盤參考買賣盤約 2470 / 2475，高於前收 2460，但這還不能等同全天突破確認。2500 新台幣仍是最關鍵壓力位，只有站穩並配合成交，才更像有效突破。",
            "TraderXYZ / Hyperliquid 上 SKHX、MU、SNDK、DRAM 同時進入高成交下跌名單，說明衍生品端仍在對記憶體鏈減倉或對沖。這更像擁擠交易後的去槓桿，而不是產業中期邏輯被推翻。",
            "機構端出現明顯分歧。UBS 對 Micron 仍然偏多，把近期回調視為買點；但永續合約端顯示 MU 跌破 1000 附近後仍有賣壓。這個分歧本身就是今天最重要的信號。",
        ]),
        ("交易框架", [
            "AI 硬體鏈仍維持中期多頭框架，但短線降低追漲衝動。TSMC 要看 2500 是否有效站穩，不能把盤前或早盤集合競價直接當作全天趨勢確認。",
            "記憶體鏈重點看 MU 是否重新站回 1000-1050，以及 SK Hynix / Samsung 是否釋放 DRAM / HBM 價格或供應端的積極資訊。若正股修復且永續止跌，多頭才算重新接管。",
            "對機構明顯看多、但衍生品明顯看空的標的，不急於只站一邊。更好的確認方式是等待正股成交、期權、ETF 和 TraderXYZ 信號相互驗證。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "Today's main signal is not simply that AI hardware is rising. Cash equities and institutional views look constructive, but TraderXYZ / Hyperliquid memory-chain perpetuals are still clearly de-risking.",
            "The medium-term thesis is intact: TSMC, HBM, DRAM, advanced packaging, GPUs and AI servers remain important themes for the next several quarters. Short term, however, MU, SKHX, SNDK and DRAM falling together on heavy volume is a real volatility warning.",
        ]),
        ("Market Structure", [
            "TSMC's early reference bid / ask near 2470 / 2475 is above the prior 2460 close, but that is not a full-session breakout confirmation. NT$2500 remains the key resistance level; it needs to hold with volume.",
            "On TraderXYZ / Hyperliquid, SKHX, MU, SNDK and DRAM all appear in high-volume downside flow. That points to continued memory-chain hedging or position reduction, more like post-crowding deleveraging than a broken industry thesis.",
            "The institutional split matters. UBS remains constructive on Micron and treats the pullback as a buying opportunity, while perpetual markets still show selling pressure after MU moved below the 1000 area.",
        ]),
        ("Trading Frame", [
            "Keep the medium-term bullish AI hardware framework, but reduce short-term chase risk. TSMC needs to confirm above NT$2500; early-session strength alone is not enough.",
            "For the memory chain, watch whether MU can reclaim 1000-1050 and whether SK Hynix / Samsung bring supportive DRAM / HBM pricing or supply signals. Bulls regain control only if cash equities recover and perpetuals stop falling.",
            "When institutions are clearly bullish but derivatives are clearly defensive, do not rely on one side alone. Confirmation should come from cash equity volume, options, ETFs and TraderXYZ signals lining up.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Главный сигнал дня не в том, что аппаратная AI-цепочка просто растет. Акции и институциональные оценки выглядят конструктивно, но перпетуалы цепочки памяти на TraderXYZ / Hyperliquid все еще явно снижают риск.",
            "Среднесрочная логика не сломана: TSMC, HBM, DRAM, передовая упаковка, GPU и AI-серверы остаются важными темами следующих кварталов. Но краткосрочно одновременное падение MU, SKHX, SNDK и DRAM на высоком объеме — реальное предупреждение о волатильности.",
        ]),
        ("Структура Рынка", [
            "Ранний ориентир TSMC около 2470 / 2475 выше предыдущего закрытия 2460, но это еще не подтверждение пробоя на весь день. NT$2500 остается ключевым сопротивлением: нужен удержанный уровень и объем.",
            "На TraderXYZ / Hyperliquid SKHX, MU, SNDK и DRAM одновременно находятся среди высокооборотных снижений. Это указывает на хеджирование или сокращение позиций в цепочке памяти, а не обязательно на слом среднесрочной отраслевой логики.",
            "Расхождение институтов важно. UBS сохраняет позитивный взгляд на Micron и считает откат возможностью для покупки, тогда как рынок перпетуалов показывает давление продавцов после ухода MU ниже зоны 1000.",
        ]),
        ("Торговая Рамка", [
            "Среднесрочно сохраняется бычья рамка по аппаратной AI-цепочке, но краткосрочно лучше снизить погоню за ростом. TSMC должна подтвердить уровень выше NT$2500; одной ранней силы недостаточно.",
            "По цепочке памяти важно, сможет ли MU вернуть 1000-1050 и появятся ли от SK Hynix / Samsung позитивные сигналы по DRAM / HBM. Быки возвращают контроль только если акции восстанавливаются, а перпетуалы перестают падать.",
            "Когда институты явно смотрят вверх, а деривативы явно защищаются, не стоит полагаться только на одну сторону. Подтверждение лучше ждать от объема в акциях, опционов, ETF и сигналов TraderXYZ одновременно.",
        ]),
    ],
}

SOURCE_URLS = [
    ("twse", "https://mis.twse.com.tw/stock/index.jsp"),
    ("traderxyz-api", "https://api.hyperliquid.xyz/info"),
    ("barrons-micron", "https://www.barrons.com/articles/micron-stock-price-buy-833a9218"),
    ("marketwatch-micron", "https://www.marketwatch.com/story/microns-stock-gains-signaling-a-return-to-optimism-about-the-chip-sector-0b7f6a8c"),
    ("micron-q3", "https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-record-results-third-quarter"),
    ("goldman-capex", "https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out"),
    ("bea-pce", "https://www.bea.gov/news/2026/personal-income-and-outlays-may-2026"),
    ("tomshardware-tsmc", "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-is-reportedly-hiking-prices-for-all-advanced-nodes-accounting-for-74-percent-of-the-companys-wafer-business-nvidia-amd-apple-qualcomm-and-others-will-face-higher-wafer-costs"),
]

SOURCE_LABELS = {
    "zh-cn": {
        "twse": "TWSE 实时行情",
        "traderxyz-api": "TraderXYZ / Hyperliquid 数据接口",
        "barrons-micron": "Barron's：Micron 回调与买点讨论",
        "marketwatch-micron": "MarketWatch：Micron 与存储股乐观情绪",
        "micron-q3": "Micron FY2026 Q3 官方财报",
        "goldman-capex": "Goldman Sachs AI 资本开支框架",
        "bea-pce": "BEA 个人收入与支出数据",
        "tomshardware-tsmc": "Tom's Hardware：TSMC 先进节点价格报道",
    },
    "zh-hant": {
        "twse": "TWSE 即時行情",
        "traderxyz-api": "TraderXYZ / Hyperliquid 數據接口",
        "barrons-micron": "Barron's：Micron 回調與買點討論",
        "marketwatch-micron": "MarketWatch：Micron 與記憶體股樂觀情緒",
        "micron-q3": "Micron FY2026 Q3 官方財報",
        "goldman-capex": "Goldman Sachs AI 資本開支框架",
        "bea-pce": "BEA 個人收入與支出數據",
        "tomshardware-tsmc": "Tom's Hardware：TSMC 先進節點價格報導",
    },
    "en": {
        "twse": "TWSE real-time quotes",
        "traderxyz-api": "TraderXYZ / Hyperliquid data API",
        "barrons-micron": "Barron's: Micron pullback and buy-the-dip view",
        "marketwatch-micron": "MarketWatch: Micron and storage-stock optimism",
        "micron-q3": "Micron FY2026 Q3 earnings release",
        "goldman-capex": "Goldman Sachs AI CapEx framework",
        "bea-pce": "BEA Personal Income and Outlays",
        "tomshardware-tsmc": "Tom's Hardware: TSMC advanced-node pricing report",
    },
    "ru": {
        "twse": "TWSE: котировки в реальном времени",
        "traderxyz-api": "TraderXYZ / Hyperliquid API данных",
        "barrons-micron": "Barron's: откат Micron и идея покупки на снижении",
        "marketwatch-micron": "MarketWatch: Micron и оптимизм вокруг акций памяти",
        "micron-q3": "Официальный отчет Micron за FY2026 Q3",
        "goldman-capex": "Goldman Sachs: рамка AI-капзатрат",
        "bea-pce": "BEA: личные доходы и расходы",
        "tomshardware-tsmc": "Tom's Hardware: цены TSMC на передовые техпроцессы",
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
        "zh-cn": ("重回 1000-1050", "2500 确认位", "UBS 多头分歧", "高成交去风险", "正股/期权/ETF 验证"),
        "zh-hant": ("重回 1000-1050", "2500 確認位", "UBS 多頭分歧", "高成交去風險", "正股/期權/ETF 驗證"),
        "en": ("reclaim 1000-1050", "2500 confirmation", "UBS bull split", "high-volume de-risking", "cash/options/ETF check"),
        "ru": ("возврат к 1000-1050", "подтверждение 2500", "разрыв с UBS", "снижение риска на объеме", "проверка акций/опционов/ETF"),
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
              <div class="brief-item"><strong>UBS / Micron</strong><span>{watch_labels[2]}</span></div>
              <div class="brief-item"><strong>SKHX / SNDK / DRAM</strong><span>{watch_labels[3]}</span></div>
              <div class="brief-item"><strong>SPY / QQQ / SOXX</strong><span>{watch_labels[4]}</span></div>
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
        "zh-cn": ("TSM 重新测试 2500，AI 硬件链进入关键防守期", "上一篇市场日报。", "归档"),
        "zh-hant": ("TSM 重新測試 2500，AI 硬體鏈進入關鍵防守期", "上一篇市場日報。", "歸檔"),
        "en": ("TSM retests 2500 as AI hardware enters a key defense phase", "Previous market brief.", "Archive"),
        "ru": ("TSM снова тестирует 2500, аппаратная AI-цепочка входит в фазу защиты", "Предыдущий обзор рынка.", "Архив"),
    }[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-07-06")}"><span class="history-date">2026-07-06</span><span><span class="history-title">{html.escape(previous[0])}</span><span class="history-summary">{html.escape(previous[1])}</span></span><span class="history-tag">{html.escape(previous[2])}</span></a>
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
