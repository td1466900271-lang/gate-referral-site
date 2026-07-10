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

DATE = "2026-07-10"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-10-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-10-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-10-en.svg",
    "ru": "/daily/images/market-brief-2026-07-10-ru.svg",
}

META = {
    "zh-cn": {
        "title": "AI 硬件链从防守切回修复，存储链高成交反弹",
        "desc": "2026-07-10 GateAffiliate 每日市场日报：AI 硬件链从防守切回修复，SKHX、MU、SNDK、DRAM 高成交上涨，Micron 美国投资计划和 SK Hynix 上市强化 AI 存储叙事，油价回落缓和科技股估值压力。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "AI 硬件链从防守切回修复，存储链高成交反弹。",
        "summary": "今天市场从昨天的防守切回 AI 硬件链修复。SKHX、MU、SNDK、DRAM 高成交上涨，油价回落减轻估值压力，Micron 投资计划和 SK Hynix 美国上市让资金重新交易 AI 存储周期。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "AI 硬體鏈從防守切回修復，記憶體鏈高成交反彈",
        "desc": "2026-07-10 GateAffiliate 每日市場日報：AI 硬體鏈從防守切回修復，SKHX、MU、SNDK、DRAM 高成交上漲，Micron 美國投資計畫和 SK Hynix 上市強化 AI 記憶體敘事，油價回落緩和科技股估值壓力。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "AI 硬體鏈從防守切回修復，記憶體鏈高成交反彈。",
        "summary": "今天市場從昨天的防守切回 AI 硬體鏈修復。SKHX、MU、SNDK、DRAM 高成交上漲，油價回落減輕估值壓力，Micron 投資計畫和 SK Hynix 美國上市讓資金重新交易 AI 記憶體周期。",
        "tag": "最新",
    },
    "en": {
        "title": "AI hardware rotates back into repair as memory rebounds on high volume",
        "desc": "2026-07-10 GateAffiliate daily market brief: AI hardware rotated from defense back into repair. SKHX, MU, SNDK and DRAM rose on high volume, Micron's U.S. investment plan and SK Hynix's U.S. listing strengthened the AI memory story, and lower oil eased valuation pressure.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "AI hardware rotates back into repair as memory rebounds on high volume.",
        "summary": "The market moved from defense back into AI hardware repair. SKHX, MU, SNDK and DRAM rose on high volume, lower oil eased valuation pressure, and Micron plus SK Hynix catalysts brought capital back to the AI memory cycle.",
        "tag": "Latest",
    },
    "ru": {
        "title": "AI-оборудование возвращается к восстановлению, память растет на высоких объемах",
        "desc": "Ежедневный обзор GateAffiliate за 2026-07-10: AI-оборудование перешло от защиты к восстановлению. SKHX, MU, SNDK и DRAM выросли на высоких объемах, план инвестиций Micron в США и листинг SK Hynix поддержали тему AI-памяти, а снижение нефти сняло часть давления с оценок.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "AI-оборудование возвращается к восстановлению, память растет на высоких объемах.",
        "summary": "Рынок перешел от защиты к восстановлению AI-оборудования. SKHX, MU, SNDK и DRAM выросли на высоких объемах, снижение нефти смягчило давление на оценки, а события вокруг Micron и SK Hynix вернули спрос к циклу AI-памяти.",
        "tag": "Свежий",
    },
}

CONCISE_SECTIONS = {
    "zh-cn": [
        ("核心结论", [
            "今天市场主线从“防守”切回“AI 硬件链修复”，尤其是存储链明显反弹。AI 半导体并没有结束，但资金正在从恐慌回撤切回到有数据、有订单、有资本开支支撑的环节。",
            "存储链是最强修复方向。TraderXYZ 上 SKHX、MU、SNDK、DRAM 都是高成交上涨，说明昨天的高波动更像拥挤交易出清，而不是基本面被证伪。",
        ]),
        ("关键市场结构", [
            "Micron 的长期美国投资计划强化了 AI 存储周期叙事，BofA 继续给出买入观点；SK Hynix 美国上市需求强，也说明全球资金仍愿意为 AI 存储核心资产付费。",
            "TSMC 仍处在数据验证窗口。6 月营收和 7 月 16 日法说会是下一步确认，2500 新台币仍是关键突破位置；如果只是符合预期，短线可能继续高位震荡。",
            "油价回落是科技股修复的助推器。CL 和 BRENTOIL 转跌后，通胀和利率压力短线缓和，半导体 ETF 与高弹性 AI 标的更容易修复。",
        ]),
        ("交易框架", [
            "对 AI 硬件链继续维持中期多头框架，但不要把一天大涨直接当作趋势恢复。存储链可以从“防守观察”上调为“修复观察”，重点看 MU 1000-1050 和 DRAM / SKHX / SNDK 是否延续强势。",
            "如果 AMD、MRVL、META 和存储链继续强于单一 NVDA 抱团，说明 AI 交易扩散更健康；如果冲高回落，仍要把它看作高波动修复。",
            "Burry 对 AI 交易的警告需要保留在框架里：AI 需求强和供应商估值合理是两件事，后续市场会更关注客户现金流、资本开支回报和业绩兑现。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "今天市場主線從「防守」切回「AI 硬體鏈修復」，尤其是記憶體鏈明顯反彈。AI 半導體並沒有結束，但資金正在從恐慌回撤切回到有數據、有訂單、有資本開支支撐的環節。",
            "記憶體鏈是最強修復方向。TraderXYZ 上 SKHX、MU、SNDK、DRAM 都是高成交上漲，說明昨天的高波動更像擁擠交易出清，而不是基本面被證偽。",
        ]),
        ("關鍵市場結構", [
            "Micron 的長期美國投資計畫強化了 AI 記憶體周期敘事，BofA 繼續給出買入觀點；SK Hynix 美國上市需求強，也說明全球資金仍願意為 AI 記憶體核心資產付費。",
            "TSMC 仍處在數據驗證窗口。6 月營收和 7 月 16 日法說會是下一步確認，2500 新台幣仍是關鍵突破位置；如果只是符合預期，短線可能繼續高位震盪。",
            "油價回落是科技股修復的助推器。CL 和 BRENTOIL 轉跌後，通膨和利率壓力短線緩和，半導體 ETF 與高彈性 AI 標的更容易修復。",
        ]),
        ("交易框架", [
            "對 AI 硬體鏈繼續維持中期多頭框架，但不要把一天大漲直接當作趨勢恢復。記憶體鏈可以從「防守觀察」上調為「修復觀察」，重點看 MU 1000-1050 和 DRAM / SKHX / SNDK 是否延續強勢。",
            "如果 AMD、MRVL、META 和記憶體鏈繼續強於單一 NVDA 抱團，說明 AI 交易擴散更健康；如果衝高回落，仍要把它看作高波動修復。",
            "Burry 對 AI 交易的警告需要保留在框架裡：AI 需求強和供應商估值合理是兩件事，後續市場會更關注客戶現金流、資本開支回報和業績兌現。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "The market's main line rotated from defense back into AI hardware repair, led by a clear rebound in the memory chain. AI semiconductors have not ended, but capital is moving from panic de-risking back toward areas with data, orders and capex support.",
            "Memory is the strongest repair direction. On TraderXYZ, SKHX, MU, SNDK and DRAM all rose on high volume, suggesting the prior volatility looked more like crowding cleanup than a broken fundamental story.",
        ]),
        ("Market Structure", [
            "Micron's long-term U.S. investment plan reinforced the AI memory cycle narrative, while BofA kept a bullish view. Strong demand for SK Hynix's U.S. listing also showed that global capital still assigns a premium to core AI memory assets.",
            "TSMC remains in a verification window. June revenue and the July 16 earnings call are the next checks, and NT$2500 remains the key resistance. If the data merely meets expectations, high-level consolidation may continue.",
            "Lower oil helped the tech repair. As CL and BRENTOIL turned lower, short-term inflation and rate pressure eased, making semiconductor ETFs and high-beta AI names easier to repair.",
        ]),
        ("Trading Frame", [
            "Keep a medium-term bullish framework for AI hardware, but do not treat one strong session as full trend restoration. Memory moves from defensive watch to repair watch, with MU 1000-1050 and DRAM / SKHX / SNDK follow-through as the key checks.",
            "If AMD, MRVL, META and memory continue to outperform a single-name NVDA cluster, the AI trade is broadening in a healthier way. If the move fades after a gap higher, it is still only high-volatility repair.",
            "Burry's warning on the AI trade belongs in the framework: strong AI demand and reasonable supplier valuations are separate questions. The market will increasingly watch customer cash flow, capex returns and earnings delivery.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Главная линия рынка перешла от защиты к восстановлению AI-оборудования, особенно за счет явного отскока цепочки памяти. AI-полупроводники не завершили цикл, но капитал возвращается из панического снижения риска в сегменты с данными, заказами и капитальными расходами.",
            "Память стала самым сильным направлением восстановления. На TraderXYZ SKHX, MU, SNDK и DRAM выросли на высоких объемах, что больше похоже на очистку перегретых позиций, а не на слом фундаментальной истории.",
        ]),
        ("Структура Рынка", [
            "Долгосрочный инвестиционный план Micron в США усилил историю AI-памяти, а BofA сохранил позитивный взгляд. Сильный спрос на листинг SK Hynix в США также показывает, что глобальный капитал готов платить премию за ключевые активы AI-памяти.",
            "TSMC остается в окне проверки данных. Июньская выручка и звонок 16 июля являются следующими подтверждениями, а NT$2500 остается ключевым сопротивлением. Если данные лишь совпадут с ожиданиями, возможна дальнейшая консолидация наверху.",
            "Снижение нефти помогло восстановлению техсектора. Когда CL и BRENTOIL развернулись вниз, краткосрочное давление инфляции и ставок ослабло, а ETF на полупроводники и более волатильные AI-активы получили пространство для отскока.",
        ]),
        ("Торговая Рамка", [
            "Среднесрочная бычья рамка по AI-оборудованию сохраняется, но один сильный день не означает полного восстановления тренда. Память можно перевести из защитного наблюдения в режим наблюдения за восстановлением: важны MU 1000-1050 и продолжение силы DRAM / SKHX / SNDK.",
            "Если AMD, MRVL, META и цепочка памяти продолжают выглядеть сильнее одиночной концентрации в NVDA, значит AI-сделка расширяется более здорово. Если рост быстро погаснет, это все еще восстановление с высокой волатильностью.",
            "Предупреждение Burry по AI-сделке стоит оставить в рамке: сильный спрос на AI и разумные оценки поставщиков — разные вопросы. Рынок все больше будет смотреть на денежный поток клиентов, отдачу от капитальных расходов и выполнение прогнозов.",
        ]),
    ],
}

SOURCE_URLS = [
    ("tsmc-monthly", "https://investor.tsmc.com/english/monthly-revenue/2026"),
    ("tsmc-calendar", "https://investor.tsmc.com/english/financial-calendar"),
    ("twse", "https://mis.twse.com.tw/stock/index.jsp"),
    ("hyperliquid-api", "https://api.hyperliquid.xyz/info"),
    ("hyperliquid-docs", "https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals"),
    ("ibd-sk-hynix", "https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-nasdaq-micron-sandisk-jump-delta-taiwan-semi-sk-hynix/"),
    ("marketwatch-etf", "https://www.marketwatch.com/livecoverage/stock-market-today-dow-s-p-500-nasdaq-heightened-tensions-us-iran/card/etfs-focused-on-semiconductor-stocks-see-big-gains-as-micron-and-amd-surge-yvvbAsFSfW6ghxLFgk66"),
    ("barrons-micron", "https://www.barrons.com/articles/micron-stock-price-analyst-buy-spending-19ebab1a"),
    ("wsj-chip-trade", "https://www.wsj.com/finance/stocks/the-chip-trade-is-helping-wall-street-shake-off-latest-iran-strikes-54abbf62"),
    ("marketwatch-sk-hynix", "https://www.marketwatch.com/story/sk-hynix-is-about-to-hit-the-u-s-market-heres-what-to-know-about-the-deal-1c873fa4"),
    ("bi-micron", "https://www.businessinsider.com/micron-stock-price-us-chip-making-250-billion-trump-ai-2026-7"),
    ("bi-burry", "https://www.businessinsider.com/michael-burry-ai-trade-nvidia-short-hyperscalers-tech-stocks-nvda-2026-7"),
    ("goldman-capex", "https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out"),
]

SOURCE_LABELS = {
    "zh-cn": {
        "tsmc-monthly": "TSMC 2026 月营收",
        "tsmc-calendar": "TSMC 投资人日历",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文档",
        "ibd-sk-hynix": "IBD：SK Hynix 募资与 Micron、Sandisk 修复",
        "marketwatch-etf": "MarketWatch：半导体 ETF 与 Micron、AMD 走强",
        "barrons-micron": "Barron’s：Micron 投资计划与 BofA 买入观点",
        "wsj-chip-trade": "WSJ：芯片交易帮助市场消化地缘风险",
        "marketwatch-sk-hynix": "MarketWatch：SK Hynix 美国上市",
        "bi-micron": "Business Insider：Micron 美国芯片制造投资计划",
        "bi-burry": "Business Insider：Michael Burry AI 交易警告",
        "goldman-capex": "Goldman Sachs AI 资本开支框架",
    },
    "zh-hant": {
        "tsmc-monthly": "TSMC 2026 月營收",
        "tsmc-calendar": "TSMC 投資人日曆",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文件",
        "ibd-sk-hynix": "IBD：SK Hynix 募資與 Micron、Sandisk 修復",
        "marketwatch-etf": "MarketWatch：半導體 ETF 與 Micron、AMD 走強",
        "barrons-micron": "Barron’s：Micron 投資計畫與 BofA 買入觀點",
        "wsj-chip-trade": "WSJ：芯片交易幫助市場消化地緣風險",
        "marketwatch-sk-hynix": "MarketWatch：SK Hynix 美國上市",
        "bi-micron": "Business Insider：Micron 美國芯片製造投資計畫",
        "bi-burry": "Business Insider：Michael Burry AI 交易警告",
        "goldman-capex": "Goldman Sachs AI 資本開支框架",
    },
    "en": {
        "tsmc-monthly": "TSMC 2026 monthly revenue",
        "tsmc-calendar": "TSMC investor calendar",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs docs",
        "ibd-sk-hynix": "IBD: SK Hynix raise and Micron / Sandisk repair",
        "marketwatch-etf": "MarketWatch: semiconductor ETFs rise with Micron and AMD",
        "barrons-micron": "Barron’s: Micron spending plan and BofA buy view",
        "wsj-chip-trade": "WSJ: chip trade helps market absorb geopolitical risk",
        "marketwatch-sk-hynix": "MarketWatch: SK Hynix U.S. listing",
        "bi-micron": "Business Insider: Micron U.S. chipmaking investment plan",
        "bi-burry": "Business Insider: Michael Burry AI trade warning",
        "goldman-capex": "Goldman Sachs AI CapEx framework",
    },
    "ru": {
        "tsmc-monthly": "TSMC: месячная выручка 2026",
        "tsmc-calendar": "TSMC: календарь для инвесторов",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Документация Hyperliquid HIP-3 / metaAndAssetCtxs",
        "ibd-sk-hynix": "IBD: размещение SK Hynix и восстановление Micron / Sandisk",
        "marketwatch-etf": "MarketWatch: ETF на полупроводники растут вместе с Micron и AMD",
        "barrons-micron": "Barron’s: инвестиционный план Micron и мнение BofA",
        "wsj-chip-trade": "WSJ: чиповая сделка помогает рынку пройти геориск",
        "marketwatch-sk-hynix": "MarketWatch: листинг SK Hynix в США",
        "bi-micron": "Business Insider: инвестиционный план Micron в производстве чипов США",
        "bi-burry": "Business Insider: предупреждение Michael Burry по AI-сделке",
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
        "zh-cn": ("1000-1050 修复确认", "6 月营收 / 2500 压力", "AI 交易是否扩散", "高成交反弹延续", "油价回落支撑估值"),
        "zh-hant": ("1000-1050 修復確認", "6 月營收 / 2500 壓力", "AI 交易是否擴散", "高成交反彈延續", "油價回落支撐估值"),
        "en": ("1000-1050 repair check", "June revenue / 2500 resistance", "AI trade breadth", "high-volume rebound follow-through", "lower oil supports valuations"),
        "ru": ("проверка 1000-1050", "июньская выручка / сопротивление 2500", "ширина AI-сделки", "продолжение отскока на объеме", "снижение нефти поддерживает оценки"),
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
              <div class="brief-item"><strong>TSMC</strong><span>{watch_labels[1]}</span></div>
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
        "zh-cn": ("AI 半导体转向龙头抱团，存储链去拥挤与油价压力并存", "上一篇市场日报。", "归档"),
        "zh-hant": ("AI 半導體轉向龍頭抱團，記憶體鏈去擁擠與油價壓力並存", "上一篇市場日報。", "歸檔"),
        "en": ("AI semis shift to leader concentration as memory de-crowding and oil pressure rise", "Previous market brief.", "Archive"),
        "ru": ("AI-полупроводники переходят к лидерам, а память и нефть давят на оценки", "Предыдущий обзор рынка.", "Архив"),
    }[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-07-09")}"><span class="history-date">2026-07-09</span><span><span class="history-title">{html.escape(previous[0])}</span><span class="history-summary">{html.escape(previous[1])}</span></span><span class="history-tag">{html.escape(previous[2])}</span></a>
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
