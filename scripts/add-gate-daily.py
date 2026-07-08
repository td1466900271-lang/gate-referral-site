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

DATE = "2026-07-08"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-08-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-08-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-08-en.svg",
    "ru": "/daily/images/market-brief-2026-07-08-ru.svg",
}

META = {
    "zh-cn": {
        "title": "AI 半导体进入验证交易，TSMC 与存储链成为关键确认",
        "desc": "2026-07-08 GateAffiliate 每日市场日报：AI 半导体从普涨交易进入验证交易，市场开始检验估值、存储周期和 AI CapEx 回报。TSMC 2500、7 月营收与法说会，MU、SKHX、DRAM、SNDK 修复持续性成为核心观察。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "AI 半导体进入验证交易，TSMC 与存储链成为关键确认。",
        "summary": "资金没有放弃 AI 硬件链，但已经从普涨交易切到验证交易。TSMC 仍是核心资产，却没有重新拿下 2500；存储链在 TraderXYZ 上出现修复，但 AMD、MRVL、INTC 仍弱，说明半导体内部正在再平衡。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "AI 半導體進入驗證交易，TSMC 與記憶體鏈成為關鍵確認",
        "desc": "2026-07-08 GateAffiliate 每日市場日報：AI 半導體從普漲交易進入驗證交易，市場開始檢驗估值、記憶體週期和 AI CapEx 回報。TSMC 2500、7 月營收與法說會，MU、SKHX、DRAM、SNDK 修復持續性成為核心觀察。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "AI 半導體進入驗證交易，TSMC 與記憶體鏈成為關鍵確認。",
        "summary": "資金沒有放棄 AI 硬體鏈，但已經從普漲交易切到驗證交易。TSMC 仍是核心資產，卻沒有重新拿下 2500；記憶體鏈在 TraderXYZ 上出現修復，但 AMD、MRVL、INTC 仍弱，說明半導體內部正在再平衡。",
        "tag": "最新",
    },
    "en": {
        "title": "AI semiconductors enter a verification trade as TSMC and memory become key tests",
        "desc": "2026-07-08 GateAffiliate daily market brief: AI semiconductors move from a broad rally into a verification trade. Valuation, memory-cycle durability and AI CapEx returns are being tested, with TSMC 2500, July revenue, the July 16 call, and MU / SKHX / DRAM / SNDK durability in focus.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "AI semiconductors enter a verification trade as TSMC and memory become key tests.",
        "summary": "Capital has not abandoned AI hardware, but the trade has shifted from broad buying to verification. TSMC remains a core asset but has not reclaimed NT$2500; memory names improved on TraderXYZ, while AMD, MRVL and INTC remain weak, showing internal semiconductor rebalancing.",
        "tag": "Latest",
    },
    "ru": {
        "title": "AI-полупроводники переходят к проверке, TSMC и цепочка памяти становятся ключевыми тестами",
        "desc": "Ежедневный обзор GateAffiliate за 2026-07-08: AI-полупроводники переходят от широкого роста к проверке оценок, цикла памяти и отдачи AI CapEx. В фокусе TSMC 2500, июльская выручка, звонок 16 июля и устойчивость MU / SKHX / DRAM / SNDK.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "AI-полупроводники переходят к проверке, TSMC и цепочка памяти становятся ключевыми тестами.",
        "summary": "Капитал не отказался от аппаратной AI-цепочки, но сделка перешла от широких покупок к проверке. TSMC остается ключевым активом, но не вернула NT$2500; цепочка памяти улучшилась на TraderXYZ, тогда как AMD, MRVL и INTC остаются слабыми, показывая внутреннюю ребалансировку сектора.",
        "tag": "Свежий",
    },
}

CONCISE_SECTIONS = {
    "zh-cn": [
        ("核心结论", [
            "今天市场主线是 AI 半导体从“普涨交易”进入“验证交易”。资金没有放弃 AI 硬件链，但开始追问估值是否过热、存储周期是否接近高点、云厂商 AI CapEx 能否继续兑现成利润。",
            "中期主线仍然是 AI 算力、HBM、DRAM、先进制程、先进封装和数据中心基础设施。短线风险在于交易过于拥挤，市场已经不满足于“利润很好”，而是要求“未来继续更好”。",
        ]),
        ("关键市场结构", [
            "TSMC 今日盘中在 2420-2455 新台币区间震荡，没有明显走弱，也没有重新拿下 2500。真正更重要的窗口是 7 月 10 日 6 月营收，以及 7 月 16 日二季度业绩与法说会。",
            "美股半导体 7 月 7 日明显回撤，SOXX 自 6 月底高点回落，MarketWatch 强调高飞芯片股开始失去动能。这不是 AI 产业链结束，而是估值重估。",
            "TraderXYZ 数据更微妙：SKHX、MU、SNDK、DRAM 转为修复，但 AMD、MRVL、INTC、SPCX 偏弱。衍生品资金不是全面看空半导体，而是在半导体内部做结构切换。",
        ]),
        ("交易框架", [
            "对 AI 硬件链保持中期多头框架，但短线不要把每一次反弹都理解为新一轮主升。TSMC 以 2500 新台币为强弱确认点，确认前更像高位震荡。",
            "存储链重点看 MU、SKHX、DRAM 的高成交反弹能否延续。如果反弹放量且正股同步修复，说明前一轮恐慌可能只是拥挤交易出清。",
            "接下来一周最重要的不是口号，而是数据：TSMC 月营收、法说会、Samsung / SK Hynix 指引、Micron 价格预期、云厂商资本开支更新。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "今天市場主線是 AI 半導體從「普漲交易」進入「驗證交易」。資金沒有放棄 AI 硬體鏈，但開始追問估值是否過熱、記憶體週期是否接近高點、雲廠商 AI CapEx 能否繼續兌現成利潤。",
            "中期主線仍然是 AI 算力、HBM、DRAM、先進製程、先進封裝和資料中心基礎設施。短線風險在於交易過於擁擠，市場已經不滿足於「利潤很好」，而是要求「未來繼續更好」。",
        ]),
        ("關鍵市場結構", [
            "TSMC 今日盤中在 2420-2455 新台幣區間震盪，沒有明顯走弱，也沒有重新拿下 2500。真正更重要的窗口是 7 月 10 日 6 月營收，以及 7 月 16 日二季度業績與法說會。",
            "美股半導體 7 月 7 日明顯回撤，SOXX 自 6 月底高點回落，MarketWatch 強調高飛晶片股開始失去動能。這不是 AI 產業鏈結束，而是估值重估。",
            "TraderXYZ 數據更微妙：SKHX、MU、SNDK、DRAM 轉為修復，但 AMD、MRVL、INTC、SPCX 偏弱。衍生品資金不是全面看空半導體，而是在半導體內部做結構切換。",
        ]),
        ("交易框架", [
            "對 AI 硬體鏈保持中期多頭框架，但短線不要把每一次反彈都理解為新一輪主升。TSMC 以 2500 新台幣為強弱確認點，確認前更像高位震盪。",
            "記憶體鏈重點看 MU、SKHX、DRAM 的高成交反彈能否延續。如果反彈放量且正股同步修復，說明前一輪恐慌可能只是擁擠交易出清。",
            "接下來一週最重要的不是口號，而是數據：TSMC 月營收、法說會、Samsung / SK Hynix 指引、Micron 價格預期、雲廠商資本開支更新。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "The main shift is that AI semiconductors have moved from a broad rally into a verification trade. Capital has not abandoned AI hardware, but it is now testing valuation heat, memory-cycle durability and whether cloud AI CapEx can keep turning into profit.",
            "The medium-term theme remains AI compute, HBM, DRAM, advanced nodes, advanced packaging and data-center infrastructure. The short-term risk is crowding: the market no longer accepts strong current profit alone; it wants stronger forward proof.",
        ]),
        ("Market Structure", [
            "TSMC traded in a NT$2420-2455 range intraday: not weak, but not a reclaim of NT$2500 either. The more important windows are July 10 monthly revenue and the July 16 earnings call.",
            "U.S. semiconductors pulled back sharply on July 7, with SOXX off from late-June highs and MarketWatch highlighting that highflying chip stocks are losing momentum. This is valuation reset, not the end of the AI supply chain.",
            "TraderXYZ is more nuanced: SKHX, MU, SNDK and DRAM improved, while AMD, MRVL, INTC and SPCX stayed weak. Derivatives flow is not broadly bearish on semis; it is rotating within the sector.",
        ]),
        ("Trading Frame", [
            "Keep a medium-term bullish AI hardware framework, but do not treat every bounce as a new impulse leg. For TSMC, NT$2500 is still the confirmation point; below it, the setup is more high-level digestion.",
            "For memory, watch whether MU, SKHX and DRAM can extend their high-volume rebound. If perpetuals recover and cash equities confirm, the previous selloff may have been crowded-position clearing.",
            "The next week is about data, not slogans: TSMC monthly revenue, the earnings call, Samsung / SK Hynix guidance, Micron pricing expectations and cloud capex updates.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Главный сдвиг дня: AI-полупроводники переходят от широкого роста к проверке. Капитал не отказался от аппаратной AI-цепочки, но теперь проверяет перегретость оценок, устойчивость цикла памяти и способность облачного AI CapEx превращаться в прибыль.",
            "Среднесрочная тема остается прежней: AI-вычисления, HBM, DRAM, передовые техпроцессы, передовая упаковка и инфраструктура дата-центров. Краткосрочный риск — перегретое позиционирование: рынку уже мало сильной текущей прибыли, нужны более сильные будущие подтверждения.",
        ]),
        ("Структура Рынка", [
            "TSMC торговалась внутри дня в диапазоне NT$2420-2455: это не слабость, но и не возврат выше NT$2500. Более важные окна — месячная выручка 10 июля и звонок по отчетности 16 июля.",
            "Американские полупроводники заметно откатились 7 июля, SOXX снизился от максимумов конца июня, а MarketWatch подчеркнул потерю импульса у сильных chip stocks. Это переоценка, а не конец AI-цепочки поставок.",
            "Данные TraderXYZ более тонкие: SKHX, MU, SNDK и DRAM улучшились, тогда как AMD, MRVL, INTC и SPCX остались слабыми. Потоки деривативов не являются тотально медвежьими по сектору, они показывают внутреннюю ротацию.",
        ]),
        ("Торговая Рамка", [
            "Среднесрочно сохраняется бычья рамка по аппаратной AI-цепочке, но не каждый отскок стоит считать новым импульсом. Для TSMC уровень NT$2500 остается точкой подтверждения; ниже него это скорее переваривание на высоких уровнях.",
            "По цепочке памяти важно, смогут ли MU, SKHX и DRAM продолжить высокооборотный отскок. Если перпетуалы восстанавливаются, а акции подтверждают движение, прежняя распродажа могла быть чисткой перегретых позиций.",
            "Следующая неделя — про данные, а не лозунги: месячная выручка TSMC, звонок по отчетности, прогнозы Samsung / SK Hynix, ожидания цен Micron и обновления по облачному CapEx.",
        ]),
    ],
}

SOURCE_URLS = [
    ("twse", "https://mis.twse.com.tw/stock/index.jsp"),
    ("tsmc-calendar", "https://investor.tsmc.com/english/financial-calendar"),
    ("hyperliquid-api", "https://api.hyperliquid.xyz/info"),
    ("hyperliquid-docs", "https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals"),
    ("marketwatch-chip-luster", "https://www.marketwatch.com/story/why-highflying-chip-stocks-are-suddenly-losing-their-luster-f0659145"),
    ("marketwatch-micron-top", "https://www.marketwatch.com/story/microns-stock-falls-as-investors-wonder-if-the-memory-market-is-near-the-top-ab2d2feb"),
    ("barrons-market-movers", "https://www.barrons.com/articles/stock-market-movers-intel-corning-super-micro-5c6ee417"),
    ("businessinsider-samsung", "https://www.businessinsider.com/kospi-today-samsung-stock-price-earnings-report-hynix-ai-profits-2026-7"),
    ("wsj-sk-hynix", "https://www.wsj.com/tech/ai/why-sk-hynix-isnt-as-cheap-as-it-looks-f2f2af42"),
    ("marketwatch-yiu", "https://www.marketwatch.com/story/this-fund-manager-bought-nvidia-and-sk-hynix-and-sold-software-before-others-his-simple-message-on-ai-follow-the-money-c3d67bea"),
    ("goldman-capex", "https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out"),
]

SOURCE_LABELS = {
    "zh-cn": {
        "twse": "TWSE 实时行情",
        "tsmc-calendar": "TSMC 投资人日历",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文档",
        "marketwatch-chip-luster": "MarketWatch：高飞芯片股降温",
        "marketwatch-micron-top": "MarketWatch：Micron 与存储周期疑问",
        "barrons-market-movers": "Barron's：市场异动与半导体观察",
        "businessinsider-samsung": "Business Insider：Samsung 业绩与韩国市场反应",
        "wsj-sk-hynix": "WSJ：SK Hynix 估值讨论",
        "marketwatch-yiu": "MarketWatch：Stephen Yiu AI 基础设施观点",
        "goldman-capex": "Goldman Sachs AI 资本开支框架",
    },
    "zh-hant": {
        "twse": "TWSE 即時行情",
        "tsmc-calendar": "TSMC 投資人日曆",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文件",
        "marketwatch-chip-luster": "MarketWatch：高飛晶片股降溫",
        "marketwatch-micron-top": "MarketWatch：Micron 與記憶體週期疑問",
        "barrons-market-movers": "Barron's：市場異動與半導體觀察",
        "businessinsider-samsung": "Business Insider：Samsung 業績與韓國市場反應",
        "wsj-sk-hynix": "WSJ：SK Hynix 估值討論",
        "marketwatch-yiu": "MarketWatch：Stephen Yiu AI 基礎設施觀點",
        "goldman-capex": "Goldman Sachs AI 資本開支框架",
    },
    "en": {
        "twse": "TWSE real-time quotes",
        "tsmc-calendar": "TSMC investor calendar",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs docs",
        "marketwatch-chip-luster": "MarketWatch: highflying chip stocks lose momentum",
        "marketwatch-micron-top": "MarketWatch: Micron and memory-cycle concerns",
        "barrons-market-movers": "Barron's: market movers and semiconductor watch",
        "businessinsider-samsung": "Business Insider: Samsung earnings and Korea market reaction",
        "wsj-sk-hynix": "WSJ: SK Hynix valuation discussion",
        "marketwatch-yiu": "MarketWatch: Stephen Yiu on AI infrastructure",
        "goldman-capex": "Goldman Sachs AI CapEx framework",
    },
    "ru": {
        "twse": "TWSE: котировки в реальном времени",
        "tsmc-calendar": "TSMC: календарь для инвесторов",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Документация Hyperliquid HIP-3 / metaAndAssetCtxs",
        "marketwatch-chip-luster": "MarketWatch: охлаждение сильных chip stocks",
        "marketwatch-micron-top": "MarketWatch: Micron и вопросы по циклу памяти",
        "barrons-market-movers": "Barron's: рыночные движения и полупроводники",
        "businessinsider-samsung": "Business Insider: отчет Samsung и реакция рынка Кореи",
        "wsj-sk-hynix": "WSJ: обсуждение оценки SK Hynix",
        "marketwatch-yiu": "MarketWatch: Stephen Yiu об AI-инфраструктуре",
        "goldman-capex": "Goldman Sachs: рамка AI-капзатрат",
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
        "zh-cn": ("900-950 / 1000-1050", "2500 与 7/10 营收", "相对强弱验证", "修复能否延续", "油价与通胀压力"),
        "zh-hant": ("900-950 / 1000-1050", "2500 與 7/10 營收", "相對強弱驗證", "修復能否延續", "油價與通膨壓力"),
        "en": ("900-950 / 1000-1050", "2500 and July 10 revenue", "relative strength check", "rebound durability", "oil and inflation pressure"),
        "ru": ("900-950 / 1000-1050", "2500 и выручка 10 июля", "проверка относительной силы", "устойчивость отскока", "нефть и инфляционное давление"),
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
              <div class="brief-item"><strong>NVDA / AMD / MRVL / INTC</strong><span>{watch_labels[2]}</span></div>
              <div class="brief-item"><strong>SKHX / SNDK / DRAM</strong><span>{watch_labels[3]}</span></div>
              <div class="brief-item"><strong>CL / BRENTOIL</strong><span>{watch_labels[4]}</span></div>
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
        "zh-cn": ("机构看多与永续去风险分歧，存储链仍是短线核心矛盾", "上一篇市场日报。", "归档"),
        "zh-hant": ("機構看多與永續去風險分歧，記憶體鏈仍是短線核心矛盾", "上一篇市場日報。", "歸檔"),
        "en": ("Institutional optimism clashes with perpetual de-risking across the memory chain", "Previous market brief.", "Archive"),
        "ru": ("Оптимизм институтов расходится со снижением риска в перпетуалах цепочки памяти", "Предыдущий обзор рынка.", "Архив"),
    }[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-07-07")}"><span class="history-date">2026-07-07</span><span><span class="history-title">{html.escape(previous[0])}</span><span class="history-summary">{html.escape(previous[1])}</span></span><span class="history-tag">{html.escape(previous[2])}</span></a>
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
