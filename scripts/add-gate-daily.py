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

DATE = "2026-07-14"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-14-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-14-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-14-en.svg",
    "ru": "/daily/images/market-brief-2026-07-14-ru.svg",
}

META = {
    "zh-cn": {
        "title": "能源冲击取代 AI 需求成为首要变量",
        "desc": "2026-07-14 GateAffiliate 每日市场日报：霍尔木兹海峡风险推升油价和利率，台股盘中普遍去风险，存储链继续承压。台积电 7 月 16 日法说将验证 AI 需求、资本开支和毛利率。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "能源冲击取代 AI 需求，成为市场首要变量。",
        "summary": "油价跳涨与利率上行压缩科技股估值，台股盘中跌约 2.8%，存储链继续去风险。AI 产业逻辑尚未反转，但资金已进入验证回报与估值的阶段。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "能源衝擊取代 AI 需求成為首要變量",
        "desc": "2026-07-14 GateAffiliate 每日市場日報：霍爾木茲海峽風險推高油價和利率，台股盤中普遍去風險，記憶體鏈繼續承壓。台積電 7 月 16 日法說將驗證 AI 需求、資本開支和毛利率。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "能源衝擊取代 AI 需求，成為市場首要變量。",
        "summary": "油價跳漲與利率上行壓縮科技股估值，台股盤中跌約 2.8%，記憶體鏈繼續去風險。AI 產業邏輯尚未反轉，但資金已進入驗證回報與估值的階段。",
        "tag": "最新",
    },
    "en": {
        "title": "Energy shock replaces AI demand as the market's primary variable",
        "desc": "2026-07-14 GateAffiliate daily market brief: Strait of Hormuz risk lifts oil and yields, Taiwan equities de-risk broadly and memory remains under pressure. TSMC's July 16 call will test AI demand, capex and margins.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "Energy shock replaces AI demand as the market's primary variable.",
        "summary": "The oil surge and higher yields are compressing technology valuations. Taiwan equities fell about 2.8% intraday and memory continues to de-risk. AI fundamentals have not reversed, but markets have entered a return-and-valuation test.",
        "tag": "Latest",
    },
    "ru": {
        "title": "Энергетический шок стал главной переменной рынка",
        "desc": "Ежедневный обзор GateAffiliate за 2026-07-14: риск в Ормузском проливе повышает цены на нефть и доходности, тайваньский рынок снижает риск, а память остается под давлением. Отчет TSMC 16 июля проверит AI-спрос, капзатраты и маржу.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "Энергетический шок стал главной переменной рынка.",
        "summary": "Скачок нефти и рост доходностей сжимают оценки технологий. Тайваньский рынок падал примерно на 2,8%, а память продолжает снижать риск. AI-фундамент не сломан, но рынок теперь проверяет отдачу и оценки.",
        "tag": "Свежий",
    },
}

CONCISE_SECTIONS = {
    "zh-cn": [
        ("核心结论", [
            "能源冲击已超过 AI 需求，成为今日首要变量。霍尔木兹海峡运输风险推高 WTI 与 Brent，通胀预期和债券收益率随之上行，高估值科技股首先承压。",
            "台股是广泛的系统性去风险，不是台积电单一个股的调整。加权指数盘中约 44115，跌幅约 2.8%；台积电运行于 2390-2430，相对大盘仍有韧性，但还不能视为调整结束。",
        ]),
        ("半导体内部分化", [
            "存储链仍是回撤中心。TraderXYZ 中 SKHX 跌 7.64%、SNDK 跌 9.22%、DRAM 跌 3.04%，而 MU 跌幅较小。这更像资金减持前期涨幅较大的拥挤品种，并未单日否定 HBM / DRAM 中期供需。",
            "NVDA 和 AMD 的表现好于部分存储与网络芯片，说明市场主要在处理估值、筹码与能源成本，还没有 AI 核心需求直接反转的证据。",
            "AI 资本开支仍在增长，但股价逻辑已从“订单增长”转向“现金回报”。供应链景气与股票回报需要分开判断。",
        ]),
        ("交易框架", [
            "首先看 WTI 和 Brent 能否回落至跳涨前区域。油价维持高位时，不宜仅因科技股跌幅扩大就判断宏观压力已经出清。",
            "台股关注 44000 点承接和台积电 2390-2400 区间。美股开盘后，用 MU、SKHY、SNDK 与 NVDA、AMD 的相对强弱判断是否仅为存储去拥挤。",
            "7 月 16 日台积电法说是近期核心验证：重点跟踪全年营收增速、资本开支、CoWoS / 先进封装产能、2nm / 3nm 进展、毛利率与海外厂成本。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "能源衝擊已超越 AI 需求，成為今日首要變量。霍爾木茲海峽運輸風險推高 WTI 與 Brent，通膨預期和債券收益率隨之上行，高估值科技股首先承壓。",
            "台股是廣泛的系統性去風險，不是台積電單一個股的調整。加權指數盤中約 44115，跌幅約 2.8%；台積電運行於 2390-2430，相對大盤仍有韌性，但還不能視為調整結束。",
        ]),
        ("半導體內部分化", [
            "記憶體鏈仍是回撤中心。TraderXYZ 中 SKHX 跌 7.64%、SNDK 跌 9.22%、DRAM 跌 3.04%，而 MU 跌幅較小。這更像資金減持前期漲幅較大的擁擠品種，並未單日否定 HBM / DRAM 中期供需。",
            "NVDA 和 AMD 的表現好於部分記憶體與網路芯片，說明市場主要在處理估值、籌碼與能源成本，還沒有 AI 核心需求直接反轉的證據。",
            "AI 資本開支仍在增長，但股價邏輯已從「訂單增長」轉向「現金回報」。供應鏈景氣與股票回報需要分開判斷。",
        ]),
        ("交易框架", [
            "首先看 WTI 和 Brent 能否回落至跳漲前區域。油價維持高位時，不宜僅因科技股跌幅擴大就判斷宏觀壓力已經出清。",
            "台股關注 44000 點承接和台積電 2390-2400 區間。美股開盤後，用 MU、SKHY、SNDK 與 NVDA、AMD 的相對強弱判斷是否僅為記憶體去擁擠。",
            "7 月 16 日台積電法說是近期核心驗證：重點跟蹤全年營收增速、資本開支、CoWoS / 先進封裝產能、2nm / 3nm 進展、毛利率與海外廠成本。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "Energy has overtaken AI demand as today's primary variable. Strait of Hormuz risk pushed WTI and Brent sharply higher, lifting inflation expectations and bond yields and putting the most pressure on long-duration technology valuations.",
            "Taiwan's decline is broad systemic de-risking rather than a TSMC-only event. The Taiwan Weighted Index traded near 44115, down about 2.8%, while TSMC held a 2390-2430 range. Relative resilience is visible, but it does not confirm the correction is over.",
        ]),
        ("Semiconductor Split", [
            "Memory remains the center of the drawdown. On TraderXYZ, SKHX fell 7.64%, SNDK 9.22% and DRAM 3.04%, while MU lost much less. The pattern points to de-crowding in the biggest prior winners rather than one-day proof that HBM and DRAM fundamentals have reversed.",
            "NVDA and AMD held up better than parts of memory and networking, suggesting the market is repricing valuation, positioning and energy costs rather than directly rejecting core AI demand.",
            "AI capex is still rising, but the equity test has shifted from order growth to cash return. Supply-chain momentum and stock returns now need to be judged separately.",
        ]),
        ("Trading Frame", [
            "First watch whether WTI and Brent can retrace toward their pre-jump levels. If oil stays elevated, a large technology drawdown alone does not mean the macro pressure has cleared.",
            "In Taiwan, watch support near 44000 and TSMC's 2390-2400 area. At the U.S. open, compare MU, SKHY and SNDK with NVDA and AMD to test whether this is mainly memory de-crowding.",
            "TSMC's July 16 earnings call is the next major validation point. Focus on full-year revenue growth, capex, CoWoS and advanced packaging capacity, 2nm / 3nm progress, gross margin and overseas-fab costs.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Энергетический шок обогнал AI-спрос и стал главной переменной дня. Риск в Ормузском проливе резко поднял WTI и Brent, а с ними инфляционные ожидания и доходности, давя на дорогие технологии.",
            "Снижение на Тайване носит системный характер, а не ограничивается TSMC. Taiwan Weighted Index был около 44115, снижаясь примерно на 2,8%, а TSMC держалась в диапазоне 2390-2430. Относительная устойчивость видна, но коррекция еще не подтверждена как завершенная.",
        ]),
        ("Расхождение Полупроводников", [
            "Память остается центром снижения. На TraderXYZ SKHX потерял 7,64%, SNDK 9,22%, DRAM 3,04%, а MU снизился гораздо меньше. Это похоже на снижение перегрева в прежних лидерах, а не на однодневное опровержение фундамента HBM / DRAM.",
            "NVDA и AMD держались лучше части памяти и сетевых чипов. Рынок скорее переоценивает стоимость, позиции и энергозатраты, чем отвергает базовый AI-спрос.",
            "AI-капзатраты все еще растут, но проверка акций сместилась от роста заказов к денежной отдаче. Динамику цепочки поставок и доходность акций теперь нужно оценивать отдельно.",
        ]),
        ("Рамка Наблюдения", [
            "Сначала нужно понять, смогут ли WTI и Brent вернуться к уровням до скачка. Если нефть остается дорогой, сильное падение технологий само по себе не означает, что макрориск исчез.",
            "На Тайване важна поддержка около 44000 и зона TSMC 2390-2400. На открытии США сравните MU, SKHY и SNDK с NVDA и AMD, чтобы проверить, связано ли движение преимущественно с охлаждением памяти.",
            "Отчет TSMC 16 июля станет следующей ключевой проверкой. В центре внимания: рост выручки, капзатраты, мощности CoWoS и передовой упаковки, прогресс 2nm / 3nm, валовая маржа и затраты зарубежных фабрик.",
        ]),
    ],
}

SOURCE_URLS = [
    ("tsmc-q2", "https://investor.tsmc.com/english/quarterly-results/2026/q2"),
    ("tsmc-monthly", "https://investor.tsmc.com/english/monthly-revenue/2026"),
    ("twse", "https://mis.twse.com.tw/stock/index.jsp"),
    ("hyperliquid-api", "https://api.hyperliquid.xyz/info"),
    ("hyperliquid-docs", "https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals"),
    ("reuters-gulf", "https://au.investing.com/news/commodities-news/shares-slip-in-asia-as-oil-jumps-on-gulf-attacks-4528787"),
    ("reuters-stocks", "https://au.marketscreener.com/news/wall-street-slips-as-iran-tensions-hit-sentiment-chipmakers-drop-ce7f5edcdb88f327"),
    ("ap-oil", "https://apnews.com/article/2d6744b09c68b5473d0bc8584b89e60e"),
    ("morgan-stanley", "https://www.morganstanley.com/Themes/outlooks"),
    ("jpmorgan-ai", "https://am.jpmorgan.com/se/en/asset-management/adv/insights/market-insights/investment-outlook/technology-and-ai/"),
    ("amundi", "https://research-center.amundi.com/article/global-investment-views-july-2026"),
]

SOURCE_LABELS = {
    "zh-cn": {
        "tsmc-q2": "TSMC 2026 年第二季度业绩",
        "tsmc-monthly": "TSMC 2026 月营收",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文档",
        "reuters-gulf": "Reuters：海湾冲突升级与油价上涨",
        "reuters-stocks": "Reuters：伊朗局势压制美股与芯片股",
        "ap-oil": "AP：油价跳涨、AI 股票下跌",
        "morgan-stanley": "摩根士丹利 2026 年中展望",
        "jpmorgan-ai": "摩根资管：AI 需求与资本开支",
        "amundi": "Amundi 2026 年 7 月全球投资观点",
    },
    "zh-hant": {
        "tsmc-q2": "TSMC 2026 年第二季度業績",
        "tsmc-monthly": "TSMC 2026 月營收",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文件",
        "reuters-gulf": "Reuters：海灣衝突升級與油價上漲",
        "reuters-stocks": "Reuters：伊朗局勢壓制美股與芯片股",
        "ap-oil": "AP：油價跳漲、AI 股票下跌",
        "morgan-stanley": "摩根士丹利 2026 年中展望",
        "jpmorgan-ai": "摩根資管：AI 需求與資本開支",
        "amundi": "Amundi 2026 年 7 月全球投資觀點",
    },
    "en": {
        "tsmc-q2": "TSMC 2026 second-quarter results",
        "tsmc-monthly": "TSMC 2026 monthly revenue",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs docs",
        "reuters-gulf": "Reuters: Gulf conflict escalation and higher oil",
        "reuters-stocks": "Reuters: Iran tension weighs on U.S. stocks and chips",
        "ap-oil": "AP: oil jumps and AI stocks fall",
        "morgan-stanley": "Morgan Stanley 2026 midyear outlook",
        "jpmorgan-ai": "J.P. Morgan Asset Management: AI demand and capex",
        "amundi": "Amundi July 2026 global investment views",
    },
    "ru": {
        "tsmc-q2": "TSMC: результаты второго квартала 2026",
        "tsmc-monthly": "TSMC: месячная выручка 2026",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Документация Hyperliquid HIP-3 / metaAndAssetCtxs",
        "reuters-gulf": "Reuters: эскалация в Заливе и рост нефти",
        "reuters-stocks": "Reuters: напряженность вокруг Ирана давит на чипы",
        "ap-oil": "AP: нефть скачет, AI-акции падают",
        "morgan-stanley": "Morgan Stanley: обзор середины 2026 года",
        "jpmorgan-ai": "J.P. Morgan Asset Management: спрос AI и капзатраты",
        "amundi": "Amundi: глобальные инвестиционные взгляды за июль 2026",
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
        "zh-cn": ("2390-2430 / 7 月 16 日法说", "SKHX、MU、DRAM、SNDK 去风险", "油价与 10 年美债", "44000 点承接 / ETF 资金流", "资本开支与现金回报"),
        "zh-hant": ("2390-2430 / 7 月 16 日法說", "SKHX、MU、DRAM、SNDK 去風險", "油價與 10 年美債", "44000 點承接 / ETF 資金流", "資本開支與現金回報"),
        "en": ("2390-2430 / July 16 earnings", "SKHX, MU, DRAM, SNDK de-risking", "oil and U.S. 10-year yield", "44000 support / ETF flows", "capex and cash return"),
        "ru": ("2390-2430 / отчет 16 июля", "снижение риска SKHX, MU, DRAM, SNDK", "нефть и 10-летняя доходность США", "поддержка 44000 / потоки ETF", "капзатраты и денежная отдача"),
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
              <div class="brief-item"><strong>TAIEX / SOXX / SMH</strong><span>{watch_labels[3]}</span></div>
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
        "zh-cn": ("台积电现货偏强，周末存储链回吐与原油走强并存", "上一篇市场日报。", "归档"),
        "zh-hant": ("台積電現貨偏強，週末記憶體鏈回吐與原油走強並存", "上一篇市場日報。", "歸檔"),
        "en": ("TSMC cash strength contrasts with weekend memory giveback and firmer oil", "Previous market brief.", "Archive"),
        "ru": ("TSMC силен, но память откатывается, а нефть растет", "Предыдущий обзор рынка.", "Архив"),
    }[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-07-13")}"><span class="history-date">2026-07-13</span><span><span class="history-title">{html.escape(previous[0])}</span><span class="history-summary">{html.escape(previous[1])}</span></span><span class="history-tag">{html.escape(previous[2])}</span></a>
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
