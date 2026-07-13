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

DATE = "2026-07-13"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-13-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-13-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-13-en.svg",
    "ru": "/daily/images/market-brief-2026-07-13-ru.svg",
}

META = {
    "zh-cn": {
        "title": "台积电现货偏强，周末存储链回吐与原油走强并存",
        "desc": "2026-07-13 GateAffiliate 每日市场日报：台股现货和台积电强于周末存储链情绪，但 TraderXYZ 显示 SKHX、MU、DRAM、SNDK 回吐，原油走强。AI 资本开支仍上修，但油价、利率和筹码减仓压低估值容错率。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "台积电现货偏强，周末存储链回吐与原油走强并存。",
        "summary": "台积电盘中约 2445-2475 新台币，台股现货强于周末存储链情绪。但周末 TraderXYZ 显示存储链回吐、原油走强，AI 资本开支仍上修，市场却开始要求现金回报和更低拥挤度。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "台積電現貨偏強，週末記憶體鏈回吐與原油走強並存",
        "desc": "2026-07-13 GateAffiliate 每日市場日報：台股現貨和台積電強於週末記憶體鏈情緒，但 TraderXYZ 顯示 SKHX、MU、DRAM、SNDK 回吐，原油走強。AI 資本開支仍上修，但油價、利率和籌碼減倉壓低估值容錯率。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "台積電現貨偏強，週末記憶體鏈回吐與原油走強並存。",
        "summary": "台積電盤中約 2445-2475 新台幣，台股現貨強於週末記憶體鏈情緒。但週末 TraderXYZ 顯示記憶體鏈回吐、原油走強，AI 資本開支仍上修，市場卻開始要求現金回報和更低擁擠度。",
        "tag": "最新",
    },
    "en": {
        "title": "TSMC cash strength contrasts with weekend memory giveback and firmer oil",
        "desc": "2026-07-13 GateAffiliate daily market brief: Taiwan cash equities and TSMC were stronger than weekend memory sentiment, while TraderXYZ showed SKHX, MU, DRAM and SNDK giving back and oil moving higher. AI capex is still rising, but oil, rates and hedge fund de-risking reduce valuation tolerance.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "TSMC cash strength contrasts with weekend memory giveback and firmer oil.",
        "summary": "TSMC traded around NT$2445-2475 and Taiwan cash equities looked stronger than weekend memory sentiment. But TraderXYZ showed memory giveback and firmer oil, while AI capex is still rising and investors are demanding cash return and cleaner positioning.",
        "tag": "Latest",
    },
    "ru": {
        "title": "TSMC силен на наличном рынке, но память откатывается, а нефть растет",
        "desc": "Ежедневный обзор GateAffiliate за 2026-07-13: тайваньский наличный рынок и TSMC выглядят сильнее настроений по памяти на выходных, но TraderXYZ показывает откат SKHX, MU, DRAM и SNDK и рост нефти. AI-капзатраты растут, но нефть, ставки и сокращение позиций снижают терпимость к оценкам.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "TSMC силен на наличном рынке, но память откатывается, а нефть растет.",
        "summary": "TSMC торговалась около NT$2445-2475, а тайваньский наличный рынок выглядел сильнее настроений по памяти на выходных. Но TraderXYZ показывает откат памяти и рост нефти; AI-капзатраты все еще растут, а рынок требует денежной отдачи и менее перегретых позиций.",
        "tag": "Свежий",
    },
}

CONCISE_SECTIONS = {
    "zh-cn": [
        ("核心结论", [
            "台股现货强于周末存储链情绪。台积电盘中约 2445-2475 新台币，高于前收 2415；台湾加权指数约 45696，说明先进制程与 AI 代工龙头仍是台湾市场主要支撑。",
            "周末风险结构是“存储回吐、原油走强”。SKHX、DRAM、SMSN、SNDK 等合约普遍下跌，WTI 和 Brent 反而上涨。这更像拥挤交易降温与地缘风险溢价回归，还不足以单独证明存储基本面反转。",
        ]),
        ("关键市场结构", [
            "台积电官网在数据截点仍未显示 6 月营收，1-5 月累计营收约 1.962 万亿新台币，同比增长 30.0%。因此今天的上涨更多是市场对 AI / 先进制程景气的定价，还不是新增月营收确认。",
            "AI 资本开支尚未见顶。摩根士丹利与摩根资管都上调超大规模云厂商资本开支预期，供应链收入景气仍强；但市场已经开始要求现金回报，估值容错率下降。",
            "筹码层面在降温。高盛主经纪数据显示，对冲基金已连续第四周净卖出科技硬件和半导体。基本面向上与资金减仓可以同时发生，所以波动会继续偏大。",
        ]),
        ("交易框架", [
            "短线观察台积电能否在放量情况下维持 2445-2475 区间上方强势，而不是只靠早盘跳空。2500 新台币仍是关键压力，下一次月营收和法说会是验证点。",
            "美股开盘重点比较 MU、SK Hynix ADR、SNDK 与 NVDA / AMD 的相对强弱；如果存储跌幅快速收窄，周末价格更可能只是低流动性扰动。",
            "同时监控 WTI、10 年期美债收益率和 SOXX / SMH。油价与收益率同步上行时，不宜仅凭产业利好追逐高估值；中期优先选择订单、产能和盈利上修可验证的环节。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "台股現貨強於週末記憶體鏈情緒。台積電盤中約 2445-2475 新台幣，高於前收 2415；台灣加權指數約 45696，說明先進製程與 AI 代工龍頭仍是台灣市場主要支撐。",
            "週末風險結構是「記憶體回吐、原油走強」。SKHX、DRAM、SMSN、SNDK 等合約普遍下跌，WTI 和 Brent 反而上漲。這更像擁擠交易降溫與地緣風險溢價回歸，還不足以單獨證明記憶體基本面反轉。",
        ]),
        ("關鍵市場結構", [
            "台積電官網在數據截點仍未顯示 6 月營收，1-5 月累計營收約 1.962 萬億新台幣，同比增長 30.0%。因此今天的上漲更多是市場對 AI / 先進製程景氣的定價，還不是新增月營收確認。",
            "AI 資本開支尚未見頂。摩根士丹利與摩根資管都上調超大規模雲廠商資本開支預期，供應鏈收入景氣仍強；但市場已經開始要求現金回報，估值容錯率下降。",
            "籌碼層面在降溫。高盛主經紀數據顯示，對沖基金已連續第四週淨賣出科技硬體和半導體。基本面向上與資金減倉可以同時發生，所以波動會繼續偏大。",
        ]),
        ("交易框架", [
            "短線觀察台積電能否在放量情況下維持 2445-2475 區間上方強勢，而不是只靠早盤跳空。2500 新台幣仍是關鍵壓力，下一次月營收和法說會是驗證點。",
            "美股開盤重點比較 MU、SK Hynix ADR、SNDK 與 NVDA / AMD 的相對強弱；如果記憶體跌幅快速收窄，週末價格更可能只是低流動性擾動。",
            "同時監控 WTI、10 年期美債收益率和 SOXX / SMH。油價與收益率同步上行時，不宜僅憑產業利好追逐高估值；中期優先選擇訂單、產能和盈利上修可驗證的環節。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "Taiwan cash equities are stronger than weekend memory sentiment. TSMC traded around NT$2445-2475, above the prior NT$2415 close, and the Taiwan Weighted Index was near 45696, keeping advanced-node and AI foundry leadership as the local market's main support.",
            "The weekend risk structure is memory giveback plus stronger oil. SKHX, DRAM, SMSN and SNDK contracts fell, while WTI and Brent rose. That looks more like crowding cooling and geopolitical risk premium returning than proof that memory fundamentals have reversed.",
        ]),
        ("Market Structure", [
            "TSMC had still not posted June revenue at the data cutoff. January-May cumulative revenue was about NT$1.962 trillion, up 30.0% year over year, so today's strength is more pricing of AI and advanced-node optimism than confirmation from new monthly revenue.",
            "AI capex has not peaked. Morgan Stanley and J.P. Morgan Asset Management both point to higher hyperscaler spending expectations, which keeps supply-chain revenue momentum strong, but the market is starting to demand cash return and lower valuation tolerance.",
            "Positioning is cooling. Goldman prime brokerage data shows hedge funds net sold technology hardware and semiconductors for a fourth straight week. Fundamentals can rise while capital de-risks, so volatility can stay elevated.",
        ]),
        ("Trading Frame", [
            "Watch whether TSMC can hold strength above the 2445-2475 area on volume rather than only an opening gap. NT$2500 remains the key resistance, while the next monthly revenue update and earnings call are the real validation points.",
            "At the U.S. open, compare MU, SK Hynix ADR and SNDK against NVDA / AMD. If memory losses narrow quickly, the weekend move was more likely a low-liquidity disturbance.",
            "Also watch WTI, the U.S. 10-year yield and SOXX / SMH. When oil and yields rise together, do not chase high valuations on industry news alone; medium term, prioritize segments where orders, capacity and earnings revisions are verifiable.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Тайваньский наличный рынок сильнее, чем настроения по памяти на выходных. TSMC торговалась около NT$2445-2475, выше предыдущего закрытия NT$2415, а Taiwan Weighted Index был около 45696; передовые техпроцессы и AI-заказы остаются главной опорой рынка.",
            "Риск на выходных выглядит как откат памяти плюс рост нефти. SKHX, DRAM, SMSN и SNDK снизились, а WTI и Brent выросли. Это больше похоже на охлаждение перегретой сделки и возврат геополитической премии, чем на доказательство разворота фундаментальных факторов памяти.",
        ]),
        ("Структура Рынка", [
            "На момент среза данных TSMC еще не показала июньскую выручку. За январь-май накопленная выручка была около NT$1.962 трлн, плюс 30.0% год к году, поэтому сегодняшний рост скорее отражает ожидания по AI и передовым техпроцессам, а не новое подтверждение месячной выручкой.",
            "AI-капзатраты еще не достигли пика. Morgan Stanley и J.P. Morgan Asset Management указывают на повышение ожиданий расходов крупных облачных компаний, поэтому выручка цепочки поставок остается сильной; но рынок уже требует денежной отдачи и снижает терпимость к оценкам.",
            "Позиционирование охлаждается. Данные Goldman prime brokerage показывают, что хедж-фонды четвертую неделю подряд нетто-продавали технологическое оборудование и полупроводники. Фундаментальные показатели могут улучшаться одновременно с сокращением позиций, поэтому волатильность останется высокой.",
        ]),
        ("Торговая Рамка", [
            "Краткосрочно важно, сможет ли TSMC удержать силу выше зоны 2445-2475 на объеме, а не только за счет утреннего гэпа. NT$2500 остается ключевым сопротивлением, а следующая месячная выручка и отчетный звонок будут настоящими проверками.",
            "На открытии США нужно сравнить MU, SK Hynix ADR и SNDK с NVDA / AMD. Если падение памяти быстро сократится, движение выходных скорее было низколиквидным шумом.",
            "Также важно следить за WTI, доходностью 10-летних облигаций США и SOXX / SMH. Когда нефть и доходности растут вместе, не стоит гнаться за высокой оценкой только из-за отраслевых новостей; среднесрочно лучше выбирать сегменты, где заказы, мощности и прибыль можно проверить.",
        ]),
    ],
}

SOURCE_URLS = [
    ("tsmc-monthly", "https://investor.tsmc.com/english/monthly-revenue/2026"),
    ("tsmc-calendar", "https://investor.tsmc.com/english/financial-calendar"),
    ("twse", "https://mis.twse.com.tw/stock/index.jsp"),
    ("hyperliquid-api", "https://api.hyperliquid.xyz/info"),
    ("hyperliquid-docs", "https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals"),
    ("morgan-stanley", "https://www.morganstanley.com/Themes/outlooks"),
    ("jpmorgan-ai", "https://am.jpmorgan.com/se/en/asset-management/adv/insights/market-insights/investment-outlook/technology-and-ai/"),
    ("amundi", "https://research-center.amundi.com/article/global-investment-views-july-2026"),
    ("investing-chip-flows", "https://www.investing.com/news/stock-market-news/hedge-funds-dumped-chip-stocks-for-a-fourth-week-as-ai-shares-sold-off-4776190"),
]

SOURCE_LABELS = {
    "zh-cn": {
        "tsmc-monthly": "TSMC 2026 月营收",
        "tsmc-calendar": "TSMC 投资人日历",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文档",
        "morgan-stanley": "摩根士丹利 2026 年中展望",
        "jpmorgan-ai": "摩根资管：AI 需求与资本开支",
        "amundi": "Amundi 2026 年 7 月全球投资观点",
        "investing-chip-flows": "Reuters / Investing：对冲基金连续减持芯片股",
    },
    "zh-hant": {
        "tsmc-monthly": "TSMC 2026 月營收",
        "tsmc-calendar": "TSMC 投資人日曆",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文件",
        "morgan-stanley": "摩根士丹利 2026 年中展望",
        "jpmorgan-ai": "摩根資管：AI 需求與資本開支",
        "amundi": "Amundi 2026 年 7 月全球投資觀點",
        "investing-chip-flows": "Reuters / Investing：對沖基金連續減持芯片股",
    },
    "en": {
        "tsmc-monthly": "TSMC 2026 monthly revenue",
        "tsmc-calendar": "TSMC investor calendar",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs docs",
        "morgan-stanley": "Morgan Stanley 2026 midyear outlook",
        "jpmorgan-ai": "J.P. Morgan Asset Management: AI demand and capex",
        "amundi": "Amundi July 2026 global investment views",
        "investing-chip-flows": "Reuters / Investing: hedge funds cut chip stocks",
    },
    "ru": {
        "tsmc-monthly": "TSMC: месячная выручка 2026",
        "tsmc-calendar": "TSMC: календарь для инвесторов",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Документация Hyperliquid HIP-3 / metaAndAssetCtxs",
        "morgan-stanley": "Morgan Stanley: обзор середины 2026 года",
        "jpmorgan-ai": "J.P. Morgan Asset Management: спрос AI и капзатраты",
        "amundi": "Amundi: глобальные инвестиционные взгляды за июль 2026",
        "investing-chip-flows": "Reuters / Investing: хедж-фонды сокращают чиповые акции",
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
        "zh-cn": ("2445-2475 强弱 / 2500 压力", "SKHX、MU、DRAM、SNDK 回吐", "油价与 10 年美债", "ETF 资金流确认", "资本开支与现金回报"),
        "zh-hant": ("2445-2475 強弱 / 2500 壓力", "SKHX、MU、DRAM、SNDK 回吐", "油價與 10 年美債", "ETF 資金流確認", "資本開支與現金回報"),
        "en": ("2445-2475 strength / 2500 resistance", "SKHX, MU, DRAM, SNDK giveback", "oil and U.S. 10-year yield", "ETF flow confirmation", "capex and cash return"),
        "ru": ("сила 2445-2475 / сопротивление 2500", "откат SKHX, MU, DRAM, SNDK", "нефть и доходность США 10 лет", "подтверждение потоками ETF", "капзатраты и денежная отдача"),
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
              <div class="brief-item"><strong>TSMC</strong><span>{watch_labels[0]}</span></div>
              <div class="brief-item"><strong>SKHX / MU / DRAM / SNDK</strong><span>{watch_labels[1]}</span></div>
              <div class="brief-item"><strong>WTI / Brent / US10Y</strong><span>{watch_labels[2]}</span></div>
              <div class="brief-item"><strong>SOXX / SMH</strong><span>{watch_labels[3]}</span></div>
              <div class="brief-item"><strong>AI CapEx</strong><span>{watch_labels[4]}</span></div>
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
        "zh-cn": ("AI 硬件链从防守切回修复，存储链高成交反弹", "上一篇市场日报。", "归档"),
        "zh-hant": ("AI 硬體鏈從防守切回修復，記憶體鏈高成交反彈", "上一篇市場日報。", "歸檔"),
        "en": ("AI hardware rotates back into repair as memory rebounds on high volume", "Previous market brief.", "Archive"),
        "ru": ("AI-оборудование возвращается к восстановлению, память растет на высоких объемах", "Предыдущий обзор рынка.", "Архив"),
    }[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-07-10")}"><span class="history-date">2026-07-10</span><span><span class="history-title">{html.escape(previous[0])}</span><span class="history-summary">{html.escape(previous[1])}</span></span><span class="history-tag">{html.escape(previous[2])}</span></a>
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
