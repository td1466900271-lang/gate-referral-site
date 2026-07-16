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

DATE = "2026-07-16"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-16-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-16-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-16-en.svg",
    "ru": "/daily/images/market-brief-2026-07-16-ru.svg",
}

META = {
    "zh-cn": {
        "title": "ASML 上调指引，存储链再度去杠杆",
        "desc": "2026-07-16 GateAffiliate 每日市场日报：ASML 二季度收入、毛利率和指引强劲，确认 AI 设备需求。台股在台积电法说前持平，存储链却再度双位数下跌，显示产业景气与拥挤交易继续分化。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "ASML 上调指引，存储链再度去杠杆。",
        "summary": "ASML 强劲财报确认 AI 设备需求仍在加速，但存储合约普遍下跌 10%-14%。台股在台积电法说前保持观望，市场更重视订单、毛利率和资本开支回报的真实兑现。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "ASML 上調指引，記憶體鏈再度去槓桿",
        "desc": "2026-07-16 GateAffiliate 每日市場日報：ASML 二季度收入、毛利率和指引強勁，確認 AI 設備需求。台股在台積電法說前持平，記憶體鏈卻再度雙位數下跌，顯示產業景氣與擁擠交易繼續分化。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "ASML 上調指引，記憶體鏈再度去槓桿。",
        "summary": "ASML 強勁財報確認 AI 設備需求仍在加速，但記憶體合約普遍下跌 10%-14%。台股在台積電法說前保持觀望，市場更重視訂單、毛利率和資本開支回報的真實兌現。",
        "tag": "最新",
    },
    "en": {
        "title": "ASML raises guidance as memory de-leverages again",
        "desc": "2026-07-16 GateAffiliate daily market brief: ASML posts strong revenue, margin and guidance, confirming AI equipment demand. Taiwan trades flat before TSMC's call while memory contracts fall 10%-14%, showing continued divergence between industry strength and crowded positioning.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "ASML raises guidance as memory de-leverages again.",
        "summary": "ASML's strong report confirms accelerating AI equipment demand, but memory contracts are down 10%-14%. Taiwan is cautious before TSMC's call, and markets are prioritizing real order, margin and capex-return delivery.",
        "tag": "Latest",
    },
    "ru": {
        "title": "ASML повышает прогноз, а память снова снижает плечо",
        "desc": "Ежедневный обзор GateAffiliate за 2026-07-16: ASML показывает сильную выручку, маржу и прогноз, подтверждая спрос на AI-оборудование. Тайвань стабилен перед звонком TSMC, а контракты на память падают на 10%-14%.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "ASML повышает прогноз, а память снова снижает плечо.",
        "summary": "Сильный отчет ASML подтверждает ускорение спроса на AI-оборудование, но память падает на 10%-14%. Перед звонком TSMC рынок ждет реальной отдачи в заказах, марже и капзатратах.",
        "tag": "Свежий",
    },
}

CONCISE_SECTIONS = {
    "zh-cn": [
        ("核心结论", [
            "ASML 确认 AI 设备需求仍在加速。二季度收入 93.26 亿欧元、毛利率 54.0%、净利润 29.18 亿欧元，并将 2026 年收入指引上调至 430 亿-450 亿欧元。设备龙头的订单与产能规划支持 AI 资本开支主线。",
            "台股在台积电法说前接近平盘，而存储链再次双位数回撤。SP500 合约小幅上涨，说明这更像高拥挤行业的内部去杠杆，而非整个美股的系统性风险。",
        ]),
        ("产业景气与交易分化", [
            "存储链波动再度扩大：SKHX 跌 13.90%、SKHY 跌 11.01%、DRAM 跌 11.05%、MU 跌 10.15%、SNDK 跌 11.59%。NVDA 仅小幅回落，说明抛压集中在前期更拥挤的存储交易。",
            "美国 CPI 与 PPI 连续降温，为科技股估值提供缓冲；但 WTI 仍接近 79 美元，7 月能源冲击尚未进入这些数据。台湾与韩国等能源进口市场仍对油价、汇率和利率路径敏感。",
            "ASML 计划 2027 年将低 NA EUV 和浸没式 DUV 产能各提高约 30%。这提高长期需求可见度，也带来 2027-2028 年若云厂商回报或存储价格转弱时的供给过剩尾部风险。",
        ]),
        ("交易框架", [
            "台积电法说优先看全年美元收入增速、毛利率和资本开支的组合，其次看 2nm / 3nm 利用率、CoWoS 扩产与海外厂成本。资本开支上调但毛利率下修，会加剧产业链内部回报分化。",
            "美股开盘后观察 ASML 财报反应，并用 MU、SKHY、SNDK 正股、SOXX / SMH 与期权市场验证 TraderXYZ 跌幅。若现货跌幅明显较小，永续合约中包含较高的杠杆与流动性折价。",
            "继续监控 Brent 油价与美债收益率。存储链维持中期积极、短期谨慎，以订单、价格、成交量和期权偏度共同确认。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "ASML 確認 AI 設備需求仍在加速。二季度收入 93.26 億歐元、毛利率 54.0%、淨利潤 29.18 億歐元，並將 2026 年收入指引上調至 430 億-450 億歐元。設備龍頭的訂單與產能規劃支持 AI 資本開支主線。",
            "台股在台積電法說前接近平盤，而記憶體鏈再次雙位數回撤。SP500 合約小幅上漲，說明這更像高擁擠行業的內部去槓桿，而非整個美股的系統性風險。",
        ]),
        ("產業景氣與交易分化", [
            "記憶體鏈波動再度擴大：SKHX 跌 13.90%、SKHY 跌 11.01%、DRAM 跌 11.05%、MU 跌 10.15%、SNDK 跌 11.59%。NVDA 僅小幅回落，說明拋壓集中在前期更擁擠的記憶體交易。",
            "美國 CPI 與 PPI 連續降溫，為科技股估值提供緩衝；但 WTI 仍接近 79 美元，7 月能源衝擊尚未進入這些數據。台灣與韓國等能源進口市場仍對油價、匯率和利率路徑敏感。",
            "ASML 計劃 2027 年將低 NA EUV 和浸沒式 DUV 產能各提高約 30%。這提高長期需求可見度，也帶來 2027-2028 年若雲廠商回報或記憶體價格轉弱時的供給過剩尾部風險。",
        ]),
        ("交易框架", [
            "台積電法說優先看全年美元收入增速、毛利率和資本開支的組合，其次看 2nm / 3nm 利用率、CoWoS 擴產與海外廠成本。資本開支上調但毛利率下修，會加劇產業鏈內部回報分化。",
            "美股開盤後觀察 ASML 財報反應，並用 MU、SKHY、SNDK 正股、SOXX / SMH 與期權市場驗證 TraderXYZ 跌幅。若現貨跌幅明顯較小，永續合約中包含較高的槓桿與流動性折價。",
            "繼續監控 Brent 油價與美債收益率。記憶體鏈維持中期積極、短期謹慎，以訂單、價格、成交量和期權偏度共同確認。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "ASML confirms AI equipment demand is still accelerating. Second-quarter revenue reached EUR9.326 billion, gross margin 54.0% and net income EUR2.918 billion, while 2026 revenue guidance rose to EUR43-45 billion. Equipment orders and capacity plans support the AI capex cycle.",
            "Taiwan is nearly flat before TSMC's call while memory contracts suffer another double-digit drawdown. With the SP500 contract slightly positive, this looks like internal de-leveraging in an overcrowded sector rather than system-wide U.S. equity risk.",
        ]),
        ("Industry Strength, Trading Weakness", [
            "Memory volatility widened again: SKHX fell 13.90%, SKHY 11.01%, DRAM 11.05%, MU 10.15% and SNDK 11.59%. NVDA eased only modestly, concentrating the selling in the previously more crowded memory trade.",
            "U.S. CPI and PPI both cooled, supporting technology valuations, but WTI remains near $79 and July's energy shock is absent from those releases. Energy-importing markets such as Taiwan and Korea remain sensitive to oil, currencies and policy rates.",
            "ASML plans to raise both low-NA EUV and immersion DUV capacity by about 30% in 2027. That improves demand visibility but creates a tail risk of excess supply in 2027-2028 if cloud returns or memory prices weaken.",
        ]),
        ("Trading Frame", [
            "For TSMC's call, prioritize the combination of full-year U.S.-dollar revenue growth, gross margin and capex, followed by 2nm / 3nm utilization, CoWoS expansion and overseas-fab costs. Higher capex with lower margin would deepen return dispersion across the chain.",
            "At the U.S. open, watch ASML's earnings reaction and validate TraderXYZ through MU, SKHY and SNDK cash shares, SOXX / SMH and options. Much smaller cash losses would imply leverage and liquidity discounts in perpetuals.",
            "Keep watching Brent and U.S. yields. Stay constructive on memory medium term but cautious short term, using orders, pricing, volume and options skew together for confirmation.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "ASML подтверждает, что спрос на AI-оборудование ускоряется. Выручка во втором квартале составила EUR9,326 млрд, валовая маржа 54,0%, чистая прибыль EUR2,918 млрд, а прогноз выручки 2026 повышен до EUR43-45 млрд.",
            "Тайвань почти не меняется перед звонком TSMC, а память снова падает двузначными темпами. Положительный SP500 указывает на внутреннее снижение плеча в перегретом секторе, а не на системный риск всего рынка США.",
        ]),
        ("Сила Отрасли и Слабость Торговли", [
            "Волатильность памяти снова расширилась: SKHX потерял 13,90%, SKHY 11,01%, DRAM 11,05%, MU 10,15% и SNDK 11,59%. NVDA снизилась лишь незначительно, поэтому продажи сосредоточены в более перегретой памяти.",
            "CPI и PPI США снизились, поддерживая оценки технологий, но WTI остается около $79. Июльский энергетический шок еще не входит в эти данные, а Тайвань и Корея чувствительны к нефти, валютам и ставкам.",
            "ASML планирует в 2027 году нарастить мощности low-NA EUV и иммерсионного DUV примерно на 30%. Это улучшает видимость спроса, но создает риск избытка в 2027-2028 годах, если отдача облаков или цены памяти ослабнут.",
        ]),
        ("Рамка Наблюдения", [
            "На звонке TSMC сначала важна связка роста долларовой выручки, валовой маржи и капзатрат, затем загрузка 2nm / 3nm, CoWoS и затраты зарубежных фабрик. Рост капзатрат при падении маржи усилит различия в отдаче.",
            "На открытии США нужно следить за реакцией ASML и проверять TraderXYZ через MU, SKHY, SNDK, SOXX / SMH и опционы. Гораздо меньшее падение спота будет означать дисконт за плечо и ликвидность в перпетуалах.",
            "Следите за Brent и доходностями США. По памяти среднесрочный взгляд остается позитивным, а краткосрочный осторожным; нужно совместное подтверждение заказами, ценами, объемом и скью опционов.",
        ]),
    ],
}

SOURCE_URLS = [
    ("bls-cpi", "https://www.bls.gov/news.release/cpi.htm"),
    ("bls-ppi", "https://www.bls.gov/news.release/archives/ppi_07152026.htm"),
    ("tsmc-q2", "https://investor.tsmc.com/english/quarterly-results/2026/q2"),
    ("tsmc-monthly", "https://investor.tsmc.com/english/monthly-revenue/2026"),
    ("asml-q2", "https://www.asml.com/en/investors/financial-results/q2-2026"),
    ("asml-release", "https://ourbrand.asml.com/asset/c8dbf3fc-4c5e-4406-83f6-27694b138245/Press-Release-Financial-Results-Q2-2026.pdf"),
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
        "bls-ppi": "美国劳工统计局：2026 年 6 月 PPI",
        "tsmc-q2": "TSMC 2026 年第二季度业绩",
        "tsmc-monthly": "TSMC 2026 月营收",
        "asml-q2": "ASML 2026 年第二季度业绩",
        "asml-release": "ASML 第二季度官方新闻稿",
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
        "bls-ppi": "美國勞工統計局：2026 年 6 月 PPI",
        "tsmc-q2": "TSMC 2026 年第二季度業績",
        "tsmc-monthly": "TSMC 2026 月營收",
        "asml-q2": "ASML 2026 年第二季度業績",
        "asml-release": "ASML 第二季度官方新聞稿",
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
        "bls-ppi": "U.S. BLS: June 2026 PPI",
        "tsmc-q2": "TSMC 2026 second-quarter results",
        "tsmc-monthly": "TSMC 2026 monthly revenue",
        "asml-q2": "ASML 2026 second-quarter results",
        "asml-release": "ASML second-quarter press release",
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
        "bls-ppi": "BLS США: PPI за июнь 2026",
        "tsmc-q2": "TSMC: результаты второго квартала 2026",
        "tsmc-monthly": "TSMC: месячная выручка 2026",
        "asml-q2": "ASML: результаты второго квартала 2026",
        "asml-release": "ASML: официальный пресс-релиз за второй квартал",
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
        "zh-cn": ("2420-2455 / 法说指引", "SKHX、SKHY、DRAM、MU 去杠杆", "CPI / PPI 降温，油价仍高", "正股 / ETF / 期权确认", "ASML 产能 / TSMC 毛利率"),
        "zh-hant": ("2420-2455 / 法說指引", "SKHX、SKHY、DRAM、MU 去槓桿", "CPI / PPI 降溫，油價仍高", "正股 / ETF / 期權確認", "ASML 產能 / TSMC 毛利率"),
        "en": ("2420-2455 / guidance", "SKHX, SKHY, DRAM, MU de-leveraging", "cool CPI / PPI, elevated oil", "cash / ETF / options confirmation", "ASML capacity / TSMC margin"),
        "ru": ("2420-2455 / прогноз", "снижение плеча SKHX, SKHY, DRAM, MU", "слабые CPI / PPI, дорогая нефть", "спот / ETF / опционы", "мощности ASML / маржа TSMC"),
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
        "zh-cn": ("台股与存储链强力修复，半导体进入关键验证窗口", "上一篇市场日报。", "归档"),
        "zh-hant": ("台股與記憶體鏈強力修復，半導體進入關鍵驗證窗口", "上一篇市場日報。", "歸檔"),
        "en": ("Taiwan and memory stage a powerful rebound into a key semiconductor test", "Previous market brief.", "Archive"),
        "ru": ("Тайвань и память сильно отскакивают перед ключевой проверкой", "Предыдущий обзор рынка.", "Архив"),
    }[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-07-15")}"><span class="history-date">2026-07-15</span><span><span class="history-title">{html.escape(previous[0])}</span><span class="history-summary">{html.escape(previous[1])}</span></span><span class="history-tag">{html.escape(previous[2])}</span></a>
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
