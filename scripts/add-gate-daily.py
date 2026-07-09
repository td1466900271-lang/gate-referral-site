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

DATE = "2026-07-09"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-09-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-09-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-09-en.svg",
    "ru": "/daily/images/market-brief-2026-07-09-ru.svg",
}

META = {
    "zh-cn": {
        "title": "AI 半导体转向龙头抱团，存储链去拥挤与油价压力并存",
        "desc": "2026-07-09 GateAffiliate 每日市场日报：AI 半导体没有崩，但从全链条 beta 转向龙头抱团、存储链去拥挤和能源冲击压估值。TSMC 2400-2420 支撑与 2500 压力、NVDA 相对强弱、MU / SKHX / DRAM 走势和油价成为核心观察。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "AI 半导体转向龙头抱团，存储链去拥挤与油价压力并存。",
        "summary": "AI 硬件链中期逻辑仍在，但市场已经不再无差别买入半导体。TSMC 仍在 2500 下方高位消化，NVDA 相对强，AMD / INTC / MRVL 偏弱；存储链没有崩，但 SKHX、DRAM、SMSN 仍在去拥挤，油价上行继续压制科技股估值。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "AI 半導體轉向龍頭抱團，記憶體鏈去擁擠與油價壓力並存",
        "desc": "2026-07-09 GateAffiliate 每日市場日報：AI 半導體沒有崩，但從全鏈條 beta 轉向龍頭抱團、記憶體鏈去擁擠和能源衝擊壓估值。TSMC 2400-2420 支撐與 2500 壓力、NVDA 相對強弱、MU / SKHX / DRAM 走勢和油價成為核心觀察。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "AI 半導體轉向龍頭抱團，記憶體鏈去擁擠與油價壓力並存。",
        "summary": "AI 硬體鏈中期邏輯仍在，但市場已經不再無差別買入半導體。TSMC 仍在 2500 下方高位消化，NVDA 相對強，AMD / INTC / MRVL 偏弱；記憶體鏈沒有崩，但 SKHX、DRAM、SMSN 仍在去擁擠，油價上行繼續壓制科技股估值。",
        "tag": "最新",
    },
    "en": {
        "title": "AI semis shift to leader concentration as memory de-crowding and oil pressure rise",
        "desc": "2026-07-09 GateAffiliate daily market brief: AI semiconductors have not broken, but the trade has shifted from full-chain beta to leader concentration, memory-chain de-crowding, and energy-driven valuation pressure. TSMC 2400-2420 support and 2500 resistance, NVDA relative strength, MU / SKHX / DRAM and oil are the key checks.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "AI semis shift to leader concentration as memory de-crowding and oil pressure rise.",
        "summary": "The medium-term AI hardware thesis remains intact, but the market is no longer buying all semis equally. TSMC is digesting below NT$2500, NVDA remains relatively strong, AMD / INTC / MRVL are weaker, memory is de-crowding rather than collapsing, and higher oil keeps pressure on tech valuations.",
        "tag": "Latest",
    },
    "ru": {
        "title": "AI-полупроводники переходят к лидерам, а память и нефть давят на оценки",
        "desc": "Ежедневный обзор GateAffiliate за 2026-07-09: AI-полупроводники не сломались, но сделка перешла от широкого beta к концентрации в лидерах, снижению перегрева цепочки памяти и давлению нефти на оценки. В фокусе TSMC 2400-2420 и 2500, относительная сила NVDA, MU / SKHX / DRAM и нефть.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "AI-полупроводники переходят к лидерам, а память и нефть давят на оценки.",
        "summary": "Среднесрочная логика аппаратной AI-цепочки сохраняется, но рынок больше не покупает все полупроводники одинаково. TSMC переваривает движение ниже NT$2500, NVDA остается относительно сильной, AMD / INTC / MRVL слабее, цепочка памяти снижает перегрев, а рост нефти давит на оценки техсектора.",
        "tag": "Свежий",
    },
}

CONCISE_SECTIONS = {
    "zh-cn": [
        ("核心结论", [
            "AI 半导体没有崩，但交易结构已经从“全链条 beta”转成“龙头抱团 + 存储链去拥挤 + 能源冲击压估值”。中期主线仍在，短线风险还没有释放完。",
            "TSMC、Nvidia、HBM、DRAM、先进封装仍是核心方向，但市场不再无差别买入半导体。NVDA 相对强，AMD / INTC / MRVL 相对弱，说明资金继续向最确定的 AI 算力龙头集中。",
        ]),
        ("关键市场结构", [
            "TSMC 今日盘中在 2430-2460 新台币区间，低于前收 2465，属于高位消化偏弱，不是突破形态。2500 仍是压力位，只要 2400-2420 没有有效跌破，中期结构仍未破坏。",
            "TraderXYZ 给出防守信号：SKHX、DRAM、SMSN 下跌，MU 基本持平，SNDK 小幅上涨。存储链不是单边崩盘，但资金仍在降低拥挤度。",
            "油价是今天重要宏观变量。CL 和 BRENTOIL 同时上涨并进入高成交榜，说明市场在交易能源和地缘风险；这会提高通胀粘性和利率压力，对科技股估值不友好。",
        ]),
        ("交易框架", [
            "对 AI 硬件链保持中期多头框架，但短线继续降低追涨冲动。TSMC 等 6 月营收和法说会验证，技术上先看 2400-2420 支撑和 2500 压力。",
            "存储链不要只看“跌了很多”，更要看 HBM / DRAM 价格、正股成交、ETF 资金流和 TraderXYZ 高成交方向是否同步改善。",
            "如果只有 NVDA 强、其他半导体弱，说明市场不是全面风险偏好回升，而是抱团确定性。油价如果继续上行，科技股估值会承压，短线仓位和节奏都应更保守。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "AI 半導體沒有崩，但交易結構已經從「全鏈條 beta」轉成「龍頭抱團 + 記憶體鏈去擁擠 + 能源衝擊壓估值」。中期主線仍在，短線風險還沒有釋放完。",
            "TSMC、Nvidia、HBM、DRAM、先進封裝仍是核心方向，但市場不再無差別買入半導體。NVDA 相對強，AMD / INTC / MRVL 相對弱，說明資金繼續向最確定的 AI 算力龍頭集中。",
        ]),
        ("關鍵市場結構", [
            "TSMC 今日盤中在 2430-2460 新台幣區間，低於前收 2465，屬於高位消化偏弱，不是突破形態。2500 仍是壓力位，只要 2400-2420 沒有有效跌破，中期結構仍未破壞。",
            "TraderXYZ 給出防守信號：SKHX、DRAM、SMSN 下跌，MU 基本持平，SNDK 小幅上漲。記憶體鏈不是單邊崩盤，但資金仍在降低擁擠度。",
            "油價是今天重要宏觀變量。CL 和 BRENTOIL 同時上漲並進入高成交榜，說明市場在交易能源和地緣風險；這會提高通膨黏性和利率壓力，對科技股估值不友好。",
        ]),
        ("交易框架", [
            "對 AI 硬體鏈保持中期多頭框架，但短線繼續降低追漲衝動。TSMC 等 6 月營收和法說會驗證，技術上先看 2400-2420 支撐和 2500 壓力。",
            "記憶體鏈不要只看「跌了很多」，更要看 HBM / DRAM 價格、正股成交、ETF 資金流和 TraderXYZ 高成交方向是否同步改善。",
            "如果只有 NVDA 強、其他半導體弱，說明市場不是全面風險偏好回升，而是抱團確定性。油價如果繼續上行，科技股估值會承壓，短線倉位和節奏都應更保守。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "AI semiconductors have not broken, but the structure has shifted from full-chain beta into leader concentration, memory-chain de-crowding and energy-driven valuation pressure. The medium-term theme is intact, but short-term risk has not fully cleared.",
            "TSMC, Nvidia, HBM, DRAM and advanced packaging remain core directions. But the market is no longer buying semiconductors indiscriminately: NVDA is relatively strong, while AMD / INTC / MRVL are weaker, showing capital clustering around the most certain AI compute leader.",
        ]),
        ("Market Structure", [
            "TSMC traded around NT$2430-2460, below the prior NT$2465 close. That is high-level digestion with a weak tilt, not a breakout. NT$2500 is still resistance, while the 2400-2420 area is the support that matters.",
            "TraderXYZ is defensive: SKHX, DRAM and SMSN fell, MU was roughly flat, and SNDK rose slightly. The memory chain is not collapsing, but capital is still reducing crowding.",
            "Oil is a major macro input today. CL and BRENTOIL both rose and entered the high-volume list, showing that energy and geopolitical risk are being traded. That adds inflation stickiness and rate pressure, which is unfriendly to tech valuations.",
        ]),
        ("Trading Frame", [
            "Keep the medium-term bullish AI hardware framework, but continue to reduce short-term chase risk. For TSMC, wait for June revenue and the earnings call; technically, watch 2400-2420 support and 2500 resistance.",
            "For memory, do not only look at how far prices have fallen. Watch HBM / DRAM pricing, cash-equity volume, ETF flows and whether TraderXYZ high-volume direction improves together.",
            "If only NVDA is strong while the rest of semis are weak, that is not broad risk appetite returning; it is a certainty trade. If oil keeps rising, tech valuations stay pressured, so position size and timing should be more conservative.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "AI-полупроводники не сломались, но структура сделки сместилась от широкого beta к концентрации в лидерах, снижению перегрева цепочки памяти и давлению нефти на оценки. Среднесрочная тема жива, но краткосрочный риск еще не снят.",
            "TSMC, Nvidia, HBM, DRAM и передовая упаковка остаются ключевыми направлениями. Но рынок больше не покупает полупроводники без разбора: NVDA относительно сильна, а AMD / INTC / MRVL слабее, что показывает концентрацию капитала в самом очевидном лидере AI-вычислений.",
        ]),
        ("Структура Рынка", [
            "TSMC торговалась около NT$2430-2460, ниже предыдущего закрытия NT$2465. Это высокоуровневое переваривание со слабым уклоном, а не пробой. NT$2500 остается сопротивлением, а зона 2400-2420 — ключевой поддержкой.",
            "TraderXYZ дает защитный сигнал: SKHX, DRAM и SMSN снизились, MU почти не изменилась, SNDK немного выросла. Цепочка памяти не рушится, но капитал продолжает снижать перегретость позиций.",
            "Нефть сегодня важный макро-фактор. CL и BRENTOIL одновременно выросли и вошли в список высоких объемов, показывая торговлю энергетическим и геополитическим риском. Это усиливает инфляционную липкость и давление ставок, что плохо для оценок техсектора.",
        ]),
        ("Торговая Рамка", [
            "Среднесрочно сохраняется бычья рамка по аппаратной AI-цепочке, но краткосрочно лучше меньше гнаться за ростом. По TSMC нужно ждать июньской выручки и звонка по отчетности; технически важны поддержка 2400-2420 и сопротивление 2500.",
            "По цепочке памяти недостаточно смотреть только на размер падения. Важны цены HBM / DRAM, объемы в акциях, потоки ETF и то, улучшается ли высокооборотное направление на TraderXYZ.",
            "Если сильна только NVDA, а остальные полупроводники слабы, это не широкий возврат риск-аппетита, а сделка на определенность. Если нефть продолжит расти, оценки техсектора останутся под давлением, поэтому размер позиции и тайминг должны быть осторожнее.",
        ]),
    ],
}

SOURCE_URLS = [
    ("twse", "https://mis.twse.com.tw/stock/index.jsp"),
    ("tsmc-monthly", "https://investor.tsmc.com/english/monthly-revenue/2026"),
    ("tsmc-calendar", "https://investor.tsmc.com/english/financial-calendar"),
    ("hyperliquid-api", "https://api.hyperliquid.xyz/info"),
    ("hyperliquid-docs", "https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals"),
    ("bi-sk-hynix", "https://www.businessinsider.com/kospi-sk-hynix-stock-price-adr-listing-samsung-chip-stocks-2026-7"),
    ("bi-memory-bear", "https://www.businessinsider.com/memory-stocks-bear-market-ai-sk-hynix-sndk-mu-wdc-2026-7"),
    ("ibd-market", "https://www.investors.com/market-trend/stock-market-today/dow-jones-sp500-nasdaq-trump-us-iran-ceasefire-micron-sandisk/"),
    ("marketwatch-yiu", "https://www.marketwatch.com/story/this-fund-manager-bought-nvidia-and-sk-hynix-and-sold-software-before-others-his-simple-message-on-ai-follow-the-money-c3d67bea"),
    ("goldman-capex", "https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out"),
]

SOURCE_LABELS = {
    "zh-cn": {
        "twse": "TWSE 实时行情",
        "tsmc-monthly": "TSMC 2026 月营收",
        "tsmc-calendar": "TSMC 投资人日历",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文档",
        "bi-sk-hynix": "Business Insider：SK Hynix 与韩国半导体回撤",
        "bi-memory-bear": "Business Insider：记忆体股票进入回撤区间",
        "ibd-market": "IBD：美股低位修复与宏观压力",
        "marketwatch-yiu": "MarketWatch：Stephen Yiu AI 基础设施观点",
        "goldman-capex": "Goldman Sachs AI 资本开支框架",
    },
    "zh-hant": {
        "twse": "TWSE 即時行情",
        "tsmc-monthly": "TSMC 2026 月營收",
        "tsmc-calendar": "TSMC 投資人日曆",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文件",
        "bi-sk-hynix": "Business Insider：SK Hynix 與韓國半導體回撤",
        "bi-memory-bear": "Business Insider：記憶體股票進入回撤區間",
        "ibd-market": "IBD：美股低位修復與宏觀壓力",
        "marketwatch-yiu": "MarketWatch：Stephen Yiu AI 基礎設施觀點",
        "goldman-capex": "Goldman Sachs AI 資本開支框架",
    },
    "en": {
        "twse": "TWSE real-time quotes",
        "tsmc-monthly": "TSMC 2026 monthly revenue",
        "tsmc-calendar": "TSMC investor calendar",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs docs",
        "bi-sk-hynix": "Business Insider: SK Hynix and Korea semiconductor pullback",
        "bi-memory-bear": "Business Insider: memory stocks enter pullback zone",
        "ibd-market": "IBD: market repair and macro pressure",
        "marketwatch-yiu": "MarketWatch: Stephen Yiu on AI infrastructure",
        "goldman-capex": "Goldman Sachs AI CapEx framework",
    },
    "ru": {
        "twse": "TWSE: котировки в реальном времени",
        "tsmc-monthly": "TSMC: месячная выручка 2026",
        "tsmc-calendar": "TSMC: календарь для инвесторов",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Документация Hyperliquid HIP-3 / metaAndAssetCtxs",
        "bi-sk-hynix": "Business Insider: SK Hynix и откат полупроводников Кореи",
        "bi-memory-bear": "Business Insider: акции памяти входят в зону отката",
        "ibd-market": "IBD: восстановление рынка и макро-давление",
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
        "zh-cn": ("950-1000 修复", "2400-2420 支撑 / 2500 压力", "抱团龙头验证", "去拥挤是否缓和", "能源冲击压估值"),
        "zh-hant": ("950-1000 修復", "2400-2420 支撐 / 2500 壓力", "抱團龍頭驗證", "去擁擠是否緩和", "能源衝擊壓估值"),
        "en": ("950-1000 recovery", "2400-2420 support / 2500 resistance", "leader concentration check", "de-crowding pressure", "energy pressure on valuations"),
        "ru": ("возврат к 950-1000", "поддержка 2400-2420 / сопротивление 2500", "проверка лидеров", "снижение перегрева", "энергия давит на оценки"),
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
        "zh-cn": ("AI 半导体进入验证交易，TSMC 与存储链成为关键确认", "上一篇市场日报。", "归档"),
        "zh-hant": ("AI 半導體進入驗證交易，TSMC 與記憶體鏈成為關鍵確認", "上一篇市場日報。", "歸檔"),
        "en": ("AI semiconductors enter a verification trade as TSMC and memory become key tests", "Previous market brief.", "Archive"),
        "ru": ("AI-полупроводники переходят к проверке, TSMC и цепочка памяти становятся ключевыми тестами", "Предыдущий обзор рынка.", "Архив"),
    }[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-07-08")}"><span class="history-date">2026-07-08</span><span><span class="history-title">{html.escape(previous[0])}</span><span class="history-summary">{html.escape(previous[1])}</span></span><span class="history-tag">{html.escape(previous[2])}</span></a>
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
