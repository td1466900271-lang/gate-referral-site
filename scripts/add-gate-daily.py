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

DATE = "2026-07-15"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-15-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-15-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-15-en.svg",
    "ru": "/daily/images/market-brief-2026-07-15-ru.svg",
}

META = {
    "zh-cn": {
        "title": "台股与存储链强力修复，半导体进入关键验证窗口",
        "desc": "2026-07-15 GateAffiliate 每日市场日报：台股反弹约 2.2%，存储链剧烈修复。美国 6 月 CPI 降温提供宏观缓冲，但高油价与拥挤仓位仍带来风险。ASML 业绩和台积电法说将验证反弹成色。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "台股与存储链强力修复，半导体进入关键验证窗口。",
        "summary": "低 CPI 支持风险资产反弹，台股与存储链强力修复；但油价仍高、半导体仓位拥挤。未来 24 小时的 ASML 业绩和台积电法说将决定修复能否转化为盈利上修。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "台股與記憶體鏈強力修復，半導體進入關鍵驗證窗口",
        "desc": "2026-07-15 GateAffiliate 每日市場日報：台股反彈約 2.2%，記憶體鏈劇烈修復。美國 6 月 CPI 降溫提供宏觀緩衝，但高油價與擁擠倉位仍帶來風險。ASML 業績和台積電法說將驗證反彈成色。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "台股與記憶體鏈強力修復，半導體進入關鍵驗證窗口。",
        "summary": "低 CPI 支持風險資產反彈，台股與記憶體鏈強力修復；但油價仍高、半導體倉位擁擠。未來 24 小時的 ASML 業績和台積電法說將決定修復能否轉化為盈利上修。",
        "tag": "最新",
    },
    "en": {
        "title": "Taiwan and memory stage a powerful rebound into a key semiconductor test",
        "desc": "2026-07-15 GateAffiliate daily market brief: Taiwan equities rebound about 2.2% and memory contracts surge. Cooler June CPI provides macro relief, but elevated oil and crowded semiconductor positioning remain risks. ASML results and TSMC's call will test the rebound.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "Taiwan and memory stage a powerful rebound into a key semiconductor test.",
        "summary": "Cooler CPI supports a forceful rebound in Taiwan and memory, but oil remains elevated and semiconductor positioning is crowded. ASML results and TSMC's July 16 call will decide whether technical repair becomes an earnings upgrade.",
        "tag": "Latest",
    },
    "ru": {
        "title": "Тайвань и память сильно отскакивают перед ключевой проверкой чипов",
        "desc": "Ежедневный обзор GateAffiliate за 2026-07-15: тайваньский рынок отскакивает примерно на 2,2%, а контракты на память резко растут. Низкий CPI дает передышку, но нефть и перегретые позиции остаются рисками. Отчеты ASML и TSMC проверят отскок.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "Тайвань и память сильно отскакивают перед ключевой проверкой чипов.",
        "summary": "Низкий CPI поддерживает сильный отскок Тайваня и памяти, но нефть остается дорогой, а позиции в чипах перегреты. Отчет ASML и звонок TSMC 16 июля покажут, станет ли техническое восстановление ростом прибыли.",
        "tag": "Свежий",
    },
}

CONCISE_SECTIONS = {
    "zh-cn": [
        ("核心结论", [
            "市场正在进行强力技术修复，但尚未确认风险完全解除。台湾加权指数盘中反弹约 2.2%，台积电回到 2450 附近，存储链出现 8%-24% 的剧烈修复，显示空头回补与抄底资金同时涌入。",
            "美国 6 月总体 CPI 环比下降 0.4%，核心 CPI 环比持平，为科技股估值提供缓冲。但该数据未包含 7 月油价冲击，WTI 与 Brent 仍约为 79.2 和 84.2 美元，宏观风险尚未出清。",
        ]),
        ("半导体修复与拥挤度", [
            "TraderXYZ 中 SKHX 涨 21.33%、SKHY 涨 24.41%、DRAM 涨 11.65%，MU 和 SNDK 也反弹超过 8%。存储中期供需仍强，但如此剧烈的反弹同时包含空头回补、杠杆清算和流动性溢价。",
            "NVDA 和 AMD 约涨 4%，修复稳健但弱于存储。美国银行调查显示“做多全球半导体”仍是最拥挤交易之一，基本面与筹码风险都处于高位。",
            "ASML 结果与台积电法说是未来 24 小时的关键验证。市场需要设备订单、先进制程利用率、先进封装产能与毛利率将交易修复转化为盈利上修。",
        ]),
        ("交易框架", [
            "台股关注 45500 上方能否稳定，台积电能否维持 2450 附近，并观察反弹是否继续扩散到其他电子、金融与传统板块。",
            "美股开盘后比较 SKHY、MU、SNDK 与 NVDA、AMD。若存储冲高回落而 GPU 链稳定，说明拥挤交易仍在消化；同时需要正股成交、SOXX / SMH 和期权波动率确认。",
            "低 CPI 利好估值，但油价再次上冲会抵消这一利好。台积电法说后应以盈利预期是否上修为判断标准，不以单日股价涨跌代替基本面结论。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "市場正在進行強力技術修復，但尚未確認風險完全解除。台灣加權指數盤中反彈約 2.2%，台積電回到 2450 附近，記憶體鏈出現 8%-24% 的劇烈修復，顯示空頭回補與抄底資金同時湧入。",
            "美國 6 月總體 CPI 環比下降 0.4%，核心 CPI 環比持平，為科技股估值提供緩衝。但該數據未包含 7 月油價衝擊，WTI 與 Brent 仍約為 79.2 和 84.2 美元，宏觀風險尚未出清。",
        ]),
        ("半導體修復與擁擠度", [
            "TraderXYZ 中 SKHX 漲 21.33%、SKHY 漲 24.41%、DRAM 漲 11.65%，MU 和 SNDK 也反彈超過 8%。記憶體中期供需仍強，但如此劇烈的反彈同時包含空頭回補、槓桿清算和流動性溢價。",
            "NVDA 和 AMD 約漲 4%，修復穩健但弱於記憶體。美國銀行調查顯示「做多全球半導體」仍是最擁擠交易之一，基本面與籌碼風險都處於高位。",
            "ASML 結果與台積電法說是未來 24 小時的關鍵驗證。市場需要設備訂單、先進製程利用率、先進封裝產能與毛利率將交易修復轉化為盈利上修。",
        ]),
        ("交易框架", [
            "台股關注 45500 上方能否穩定，台積電能否維持 2450 附近，並觀察反彈是否繼續擴散到其他電子、金融與傳統板塊。",
            "美股開盤後比較 SKHY、MU、SNDK 與 NVDA、AMD。若記憶體衝高回落而 GPU 鏈穩定，說明擁擠交易仍在消化；同時需要正股成交、SOXX / SMH 和期權波動率確認。",
            "低 CPI 利好估值，但油價再次上衝會抵消這一利好。台積電法說後應以盈利預期是否上修為判斷標準，不以單日股價漲跌代替基本面結論。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "Markets are staging a powerful technical repair, but risk is not fully cleared. Taiwan's benchmark rebounded about 2.2%, TSMC returned toward NT$2450 and TraderXYZ memory contracts gained roughly 8%-24%, reflecting both dip buying and aggressive short covering.",
            "U.S. June headline CPI fell 0.4% month over month and core CPI was flat, giving technology valuations macro relief. But the report predates July's oil shock; WTI and Brent remain near $79.2 and $84.2, so the inflation risk has not disappeared.",
        ]),
        ("Semiconductor Rebound and Crowding", [
            "SKHX rose 21.33%, SKHY 24.41% and DRAM 11.65%, while MU and SNDK gained more than 8%. Medium-term memory supply and demand remain firm, but moves this large also contain short covering, leverage liquidations and a liquidity premium.",
            "NVDA and AMD gained about 4%, a steadier but smaller rebound than memory. Bank of America's survey still identifies long global semiconductors as one of the most crowded trades, leaving fundamentals and positioning risk high at the same time.",
            "ASML's results and TSMC's call are the next 24-hour test. Equipment orders, advanced-node utilization, packaging capacity and margins must turn trading repair into earnings upgrades.",
        ]),
        ("Trading Frame", [
            "Watch whether Taiwan can hold above 45500, whether TSMC stays near 2450 and whether the rebound keeps broadening beyond the main index weight.",
            "At the U.S. open, compare SKHY, MU and SNDK with NVDA and AMD. If memory fades while GPUs hold, crowding is still being digested; confirm with cash-equity volume, SOXX / SMH and options volatility.",
            "Cool CPI supports valuation, but another oil surge would offset that benefit. After TSMC's call, judge the move by earnings revisions rather than one day's share-price reaction.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Рынок показывает сильное техническое восстановление, но риск еще не исчез. Тайваньский индекс отскочил примерно на 2,2%, TSMC вернулась к NT$2450, а контракты на память выросли на 8%-24%, что отражает покупки на падении и закрытие шортов.",
            "Общий CPI США за июнь снизился на 0,4% к месяцу, а базовый CPI не изменился, дав передышку оценкам технологий. Но эти данные еще не отражают июльский скачок нефти; WTI и Brent остаются около $79,2 и $84,2.",
        ]),
        ("Отскок и Перегрев Чипов", [
            "На TraderXYZ SKHX вырос на 21,33%, SKHY на 24,41%, DRAM на 11,65%, а MU и SNDK более чем на 8%. Среднесрочный баланс памяти силен, но такой скачок также включает закрытие шортов, ликвидации и премию за ликвидность.",
            "NVDA и AMD прибавили около 4%, показав более спокойное восстановление. Опрос Bank of America по-прежнему называет длинную позицию в глобальных полупроводниках одной из самых перегретых сделок.",
            "Результаты ASML и звонок TSMC станут проверкой ближайших 24 часов. Заказы на оборудование, загрузка передовых техпроцессов, упаковка и маржа должны превратить технический отскок в повышение прибыли.",
        ]),
        ("Рамка Наблюдения", [
            "На Тайване важно удержаться выше 45500, TSMC около 2450, а также продолжение расширения отскока за пределы главной акции индекса.",
            "На открытии США сравните SKHY, MU и SNDK с NVDA и AMD. Если память ослабнет, а GPU удержатся, перегрев еще не устранен; нужно подтверждение объемом акций, SOXX / SMH и волатильностью опционов.",
            "Низкий CPI помогает оценкам, но новый скачок нефти его нейтрализует. После звонка TSMC оценивайте движение по пересмотру прогнозов прибыли, а не по одному дню цены.",
        ]),
    ],
}

SOURCE_URLS = [
    ("bls-cpi", "https://www.bls.gov/news.release/cpi.htm?lv=true"),
    ("tsmc-q2", "https://investor.tsmc.com/english/quarterly-results/2026/q2"),
    ("tsmc-monthly", "https://investor.tsmc.com/english/monthly-revenue/2026"),
    ("asml-q2", "https://www.asml.com/en/investors/financial-results/q2-2026"),
    ("twse", "https://mis.twse.com.tw/stock/index.jsp"),
    ("hyperliquid-api", "https://api.hyperliquid.xyz/info"),
    ("hyperliquid-docs", "https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals"),
    ("ap-oil", "https://apnews.com/article/2d6744b09c68b5473d0bc8584b89e60e"),
    ("ubs-ai", "https://www.ubs.com/us/en/wealth-management/insights/market-news/article.3534348.html"),
    ("man-group", "https://www.man.com/insights/views-from-the-floor-2026-14-july"),
    ("franklin-ai", "https://www.franklintempleton.com/articles/2026/clearbridge-investments/can-ai-capex-extend-the-semiconductor-cycle"),
]

SOURCE_LABELS = {
    "zh-cn": {
        "bls-cpi": "美国劳工统计局：2026 年 6 月 CPI",
        "tsmc-q2": "TSMC 2026 年第二季度业绩",
        "tsmc-monthly": "TSMC 2026 月营收",
        "asml-q2": "ASML 2026 年第二季度业绩",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文档",
        "ap-oil": "AP：油价跳涨、AI 股票下跌",
        "ubs-ai": "UBS：AI 资本开支与半导体选择",
        "man-group": "Man Group：半导体交易进入选择阶段",
        "franklin-ai": "Franklin Templeton：AI 资本开支与半导体周期",
    },
    "zh-hant": {
        "bls-cpi": "美國勞工統計局：2026 年 6 月 CPI",
        "tsmc-q2": "TSMC 2026 年第二季度業績",
        "tsmc-monthly": "TSMC 2026 月營收",
        "asml-q2": "ASML 2026 年第二季度業績",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文件",
        "ap-oil": "AP：油價跳漲、AI 股票下跌",
        "ubs-ai": "UBS：AI 資本開支與半導體選擇",
        "man-group": "Man Group：半導體交易進入選擇階段",
        "franklin-ai": "Franklin Templeton：AI 資本開支與半導體週期",
    },
    "en": {
        "bls-cpi": "U.S. BLS: June 2026 CPI",
        "tsmc-q2": "TSMC 2026 second-quarter results",
        "tsmc-monthly": "TSMC 2026 monthly revenue",
        "asml-q2": "ASML 2026 second-quarter results",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs docs",
        "ap-oil": "AP: oil jumps and AI stocks fall",
        "ubs-ai": "UBS: AI capex and semiconductor selection",
        "man-group": "Man Group: semiconductors enter a selection phase",
        "franklin-ai": "Franklin Templeton: AI capex and the chip cycle",
    },
    "ru": {
        "bls-cpi": "BLS США: CPI за июнь 2026",
        "tsmc-q2": "TSMC: результаты второго квартала 2026",
        "tsmc-monthly": "TSMC: месячная выручка 2026",
        "asml-q2": "ASML: результаты второго квартала 2026",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Документация Hyperliquid HIP-3 / metaAndAssetCtxs",
        "ap-oil": "AP: нефть скачет, AI-акции падают",
        "ubs-ai": "UBS: AI-капзатраты и выбор чипов",
        "man-group": "Man Group: полупроводники входят в фазу отбора",
        "franklin-ai": "Franklin Templeton: AI-капзатраты и цикл чипов",
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
        "zh-cn": ("2415-2460 / 法说验证", "SKHX、SKHY、DRAM、MU 强力修复", "6 月 CPI / 高油价", "45500 点承接 / ETF 确认", "ASML 订单 / TSMC 指引"),
        "zh-hant": ("2415-2460 / 法說驗證", "SKHX、SKHY、DRAM、MU 強力修復", "6 月 CPI / 高油價", "45500 點承接 / ETF 確認", "ASML 訂單 / TSMC 指引"),
        "en": ("2415-2460 / earnings test", "SKHX, SKHY, DRAM, MU rebound", "June CPI / elevated oil", "45500 support / ETF confirmation", "ASML orders / TSMC guidance"),
        "ru": ("2415-2460 / проверка отчетом", "отскок SKHX, SKHY, DRAM, MU", "CPI за июнь / дорогая нефть", "поддержка 45500 / ETF", "заказы ASML / прогноз TSMC"),
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
              <div class="brief-item"><strong>CPI / WTI / Brent</strong><span>{watch_labels[2]}</span></div>
              <div class="brief-item"><strong>TAIEX / SOXX / SMH</strong><span>{watch_labels[3]}</span></div>
              <div class="brief-item"><strong>ASML / TSMC</strong><span>{watch_labels[4]}</span></div>
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
        "zh-cn": ("能源冲击取代 AI 需求成为首要变量", "上一篇市场日报。", "归档"),
        "zh-hant": ("能源衝擊取代 AI 需求成為首要變量", "上一篇市場日報。", "歸檔"),
        "en": ("Energy shock replaces AI demand as the market's primary variable", "Previous market brief.", "Archive"),
        "ru": ("Энергетический шок стал главной переменной рынка", "Предыдущий обзор рынка.", "Архив"),
    }[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-07-14")}"><span class="history-date">2026-07-14</span><span><span class="history-title">{html.escape(previous[0])}</span><span class="history-summary">{html.escape(previous[1])}</span></span><span class="history-tag">{html.escape(previous[2])}</span></a>
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
