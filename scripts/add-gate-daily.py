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

DATE = "2026-07-17"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-17-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-17-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-17-en.svg",
    "ru": "/daily/images/market-brief-2026-07-17-ru.svg",
}

META = {
    "zh-cn": {
        "title": "台积电强财报后下跌，AI 科技进入资本回报再定价",
        "desc": "2026-07-17 GateAffiliate 每日市场日报：台积电收入、利润与全年指引强劲，但资本开支上调、毛利率边际回落与拥挤仓位引发 AI 科技广泛去风险。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "台积电强财报后下跌，AI 科技进入资本回报再定价。",
        "summary": "台积电证明 AI 需求仍极其强劲，但市场已从收入叙事转向自由现金流、毛利率与资本回报率。台股、GPU、存储与网络芯片同步去风险。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "台積電強財報後下跌，AI 科技進入資本回報再定價",
        "desc": "2026-07-17 GateAffiliate 每日市場日報：台積電收入、利潤與全年指引強勁，但資本開支上調、毛利率邊際回落與擁擠倉位引發 AI 科技廣泛去風險。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "台積電強財報後下跌，AI 科技進入資本回報再定價。",
        "summary": "台積電證明 AI 需求仍極其強勁，但市場已從收入敘事轉向自由現金流、毛利率與資本回報率。台股、GPU、記憶體與網路芯片同步去風險。",
        "tag": "最新",
    },
    "en": {
        "title": "TSMC falls after a stellar report as AI tech reprices capital returns",
        "desc": "2026-07-17 GateAffiliate daily market brief: TSMC delivers strong revenue, profit and guidance, but higher capex, softer sequential margin guidance and crowded positioning trigger broad de-risking across AI technology.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "TSMC falls after a stellar report as AI tech reprices capital returns.",
        "summary": "TSMC confirms exceptionally strong AI demand, but markets have shifted from revenue growth to free cash flow, margin and return on capital. Taiwan, GPUs, memory and networking chips are de-risking together.",
        "tag": "Latest",
    },
    "ru": {
        "title": "TSMC падает после сильного отчета: AI-сектор переоценивает отдачу капитала",
        "desc": "Ежедневный обзор GateAffiliate за 2026-07-17: TSMC показывает сильную выручку, прибыль и прогноз, но рост капзатрат, снижение прогноза маржи и перегретые позиции вызывают общее снижение риска в AI-технологиях.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "TSMC падает после сильного отчета: AI-сектор переоценивает отдачу капитала.",
        "summary": "TSMC подтверждает исключительно сильный AI-спрос, но рынок уже смотрит на свободный денежный поток, маржу и отдачу капитала. Тайвань, GPU, память и сетевые чипы снижают риск вместе.",
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

CONCISE_SECTIONS.update({
    "zh-cn": [
        ("核心结论", [
            "台积电二季度美元收入 402 亿、毛利率 67.7%、净利润 7066 亿新台币，并将全年美元收入增速上调至略高于 40%。这证明 AI 需求没有见顶，但仅仅超预期已不足以推动估值继续扩张。",
            "股价下跌的核心是资本回报再定价。2026 年资本开支上调至 600 亿-640 亿美元，三季度毛利率指引 65%-67% 低于二季度。市场开始要求扩产转化为自由现金流，而不再只奖励收入增长。",
        ]),
        ("AI 科技广泛去风险", [
            "台湾加权指数盘中跌约 5.2%，台积电跌约 5.1%。TraderXYZ 中纳指、GPU、存储、网络芯片和韩国 ETF 同步下跌，前一交易日费城半导体指数也跌 4.3%，风险已从单一行业扩散。",
            "存储仍是最拥挤和波动最大的环节，SNDK、DRAM、SKHY、MU 普遍大跌；MRVL、AMD 和 INTC 也明显承压。产业需求仍强，但高估值、高仓位与高资本开支同时放大回撤。",
            "ASML 与台积电共同确认设备和先进制程资本开支仍在上行。这提高订单可见度，也使 2027-2028 年供需、折旧、融资成本和资本回报率成为新的估值核心。",
        ]),
        ("观察框架", [
            "台股先看 43000 点附近承接与台积电 2340-2350 区域，重点观察收盘是否脱离日内低点。",
            "美股开盘后用 TSM、NVDA、AMD、MU、SKHY、SNDK 及 SOXX / SMH 成交量验证。若盈利预期上修而估值下跌，更像估值压缩；若毛利率和自由现金流预期下调，需要更谨慎。",
            "继续监控油价、美债收益率与美元。三者同步上行时，高估值科技股压力最大。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "台積電二季度美元收入 402 億、毛利率 67.7%、淨利潤 7066 億新台幣，並將全年美元收入增速上調至略高於 40%。這證明 AI 需求沒有見頂，但僅僅超預期已不足以推動估值繼續擴張。",
            "股價下跌的核心是資本回報再定價。2026 年資本開支上調至 600 億-640 億美元，三季度毛利率指引 65%-67% 低於二季度。市場開始要求擴產轉化為自由現金流。",
        ]),
        ("AI 科技廣泛去風險", [
            "台灣加權指數盤中跌約 5.2%，台積電跌約 5.1%。TraderXYZ 中納指、GPU、記憶體、網路芯片和韓國 ETF 同步下跌，風險已從單一行業擴散。",
            "記憶體仍是最擁擠和波動最大的環節，MRVL、AMD 和 INTC 也明顯承壓。產業需求仍強，但高估值、高倉位與高資本開支同時放大回撤。",
            "ASML 與台積電共同確認資本開支仍在上行，也使 2027-2028 年供需、折舊、融資成本和資本回報率成為新的估值核心。",
        ]),
        ("觀察框架", [
            "台股先看 43000 點附近承接與台積電 2340-2350 區域，重點觀察收盤是否脫離日內低點。",
            "美股開盤後用 TSM、NVDA、AMD、MU、SKHY、SNDK 及 SOXX / SMH 成交量驗證。若盈利預期上修而估值下跌，更像估值壓縮；若毛利率和自由現金流預期下調，需要更謹慎。",
            "繼續監控油價、美債收益率與美元。三者同步上行時，高估值科技股壓力最大。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "TSMC delivered $40.2 billion in second-quarter revenue, a 67.7% gross margin and NT$706.6 billion in net income, while lifting full-year U.S.-dollar revenue growth to slightly above 40%. AI demand is not peaking, but beating expectations alone no longer expands valuation.",
            "The selloff is a repricing of capital returns. 2026 capex rose to $60-64 billion while third-quarter gross-margin guidance of 65%-67% is below the second quarter. Investors now want expansion to translate into free cash flow.",
        ]),
        ("Broad AI Tech De-risking", [
            "Taiwan's index fell about 5.2% intraday and TSMC about 5.1%. Nasdaq, GPUs, memory, networking chips and Korea exposure fell together on TraderXYZ, consistent with a 4.3% prior-session drop in the Philadelphia Semiconductor Index.",
            "Memory remains the most crowded and volatile segment, while MRVL, AMD and INTC also face heavy pressure. Strong demand now coexists with high valuation, heavy positioning and elevated capex.",
            "ASML and TSMC both confirm that advanced-node capex is rising. That improves order visibility but makes 2027-2028 supply, depreciation, financing costs and return on capital the new valuation debate.",
        ]),
        ("Watch Frame", [
            "Watch Taiwan near 43000 and TSMC at 2340-2350, especially whether the close moves away from intraday lows.",
            "At the U.S. open, validate through TSM, NVDA, AMD, MU, SKHY, SNDK and SOXX / SMH volume. Higher earnings with lower multiples suggests valuation compression; falling margin or free-cash-flow estimates require more caution.",
            "Keep monitoring oil, U.S. yields and the dollar. When all three rise together, high-valuation technology faces the greatest pressure.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "TSMC показала $40,2 млрд выручки, валовую маржу 67,7% и NT$706,6 млрд чистой прибыли, повысив прогноз роста долларовой выручки до чуть выше 40%. AI-спрос не достиг пика, но одного сюрприза уже недостаточно для роста оценки.",
            "Падение отражает переоценку отдачи капитала. Капзатраты 2026 повышены до $60-64 млрд, а прогноз маржи 65%-67% ниже второго кварта. Рынок требует, чтобы расширение давало свободный денежный поток.",
        ]),
        ("Широкое Снижение Риска AI", [
            "Индекс Тайваня падал примерно на 5,2%, TSMC на 5,1%. Nasdaq, GPU, память, сетевые чипы и Корея снижаются вместе, а индекс чипов Филадельфии ранее потерял 4,3%.",
            "Память остается самым перегретым и волатильным сегментом; MRVL, AMD и INTC также под давлением. Сильный спрос сочетается с высокой оценкой, позициями и капзатратами.",
            "ASML и TSMC подтверждают рост капзатрат. Это улучшает видимость заказов, но делает спрос, амортизацию, стоимость финансирования и отдачу капитала в 2027-2028 годах центром оценки.",
        ]),
        ("Рамка Наблюдения", [
            "Следите за поддержкой Тайваня около 43000 и TSMC в зоне 2340-2350, особенно за уходом от дневных минимумов к закрытию.",
            "На открытии США проверяйте TSM, NVDA, AMD, MU, SKHY, SNDK и объемы SOXX / SMH. Рост прибыли при падении мультипликаторов означает сжатие оценки; снижение прогнозов маржи и денежного потока требует большей осторожности.",
            "Следите за нефтью, доходностями США и долларом. Когда все три растут, дорогие технологии находятся под максимальным давлением.",
        ]),
    ],
})

SOURCE_URLS = [
    ("tsmc-q2", "https://investor.tsmc.com/english/quarterly-results/2026/q2"),
    ("reuters-tsmc", "https://www.investing.com/news/stock-market-news/tsmc-q2-profit-jumps-77-to-record-far-surpasses-expectations-4794649"),
    ("ap-tsmc-us", "https://apnews.com/article/taiwan-tsmc-chipmaking-ai-arizona-fab-ba05b1b952257d371acb9d070e7914ff"),
    ("sec-tsmc", "https://www.sec.gov/Archives/edgar/data/1046179/000104617926000447/tsm-revenue20260713.htm"),
    ("reuters-chips", "https://sa.marketscreener.com/news/chipmakers-put-pressure-on-equity-indexes-globally-oil-dips-ce7f5ed3dc89f327"),
    ("asml-q2", "https://www.asml.com/en/investors/financial-results/q2-2026"),
    ("twse", "https://mis.twse.com.tw/stock/index.jsp"),
    ("bls-cpi", "https://www.bls.gov/news.release/cpi.htm"),
    ("bls-ppi", "https://www.bls.gov/news.release/archives/ppi_07152026.htm"),
    ("hyperliquid-api", "https://api.hyperliquid.xyz/info"),
    ("hyperliquid-docs", "https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals"),
    ("man-group", "https://www.man.com/insights/views-from-the-floor-2026-14-july"),
]

SOURCE_LABELS = {
    "zh-cn": {
        "bls-cpi": "美国劳工统计局：2026 年 6 月 CPI",
        "bls-ppi": "美国劳工统计局：2026 年 6 月 PPI",
        "tsmc-q2": "TSMC 2026 年第二季度业绩",
        "reuters-tsmc": "Reuters：TSMC 第二季度利润创新高",
        "ap-tsmc-us": "AP：TSMC 美国投资与扩产计划",
        "sec-tsmc": "SEC：TSMC 2026 年 6 月营收报告",
        "reuters-chips": "Reuters：全球芯片股回撤与风险重估",
        "asml-q2": "ASML 2026 年第二季度业绩",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文档",
        "man-group": "Man Group：半导体交易进入选择阶段",
    },
    "zh-hant": {
        "bls-cpi": "美國勞工統計局：2026 年 6 月 CPI",
        "bls-ppi": "美國勞工統計局：2026 年 6 月 PPI",
        "tsmc-q2": "TSMC 2026 年第二季度業績",
        "reuters-tsmc": "Reuters：TSMC 第二季度利潤創新高",
        "ap-tsmc-us": "AP：TSMC 美國投資與擴產計畫",
        "sec-tsmc": "SEC：TSMC 2026 年 6 月營收報告",
        "reuters-chips": "Reuters：全球晶片股回落與風險重估",
        "asml-q2": "ASML 2026 年第二季度業績",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs 文件",
        "man-group": "Man Group：半導體交易進入選擇階段",
    },
    "en": {
        "bls-cpi": "U.S. BLS: June 2026 CPI",
        "bls-ppi": "U.S. BLS: June 2026 PPI",
        "tsmc-q2": "TSMC 2026 second-quarter results",
        "reuters-tsmc": "Reuters: TSMC second-quarter profit hits a record",
        "ap-tsmc-us": "AP: TSMC's U.S. investment and expansion",
        "sec-tsmc": "SEC: TSMC June 2026 revenue filing",
        "reuters-chips": "Reuters: global chip selloff and risk repricing",
        "asml-q2": "ASML 2026 second-quarter results",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Hyperliquid HIP-3 / metaAndAssetCtxs docs",
        "man-group": "Man Group: semiconductors enter a selection phase",
    },
    "ru": {
        "bls-cpi": "BLS США: CPI за июнь 2026",
        "bls-ppi": "BLS США: PPI за июнь 2026",
        "tsmc-q2": "TSMC: результаты второго квартала 2026",
        "reuters-tsmc": "Reuters: рекордная прибыль TSMC за второй квартал",
        "ap-tsmc-us": "AP: инвестиции и расширение TSMC в США",
        "sec-tsmc": "SEC: отчет TSMC о выручке за июнь 2026",
        "reuters-chips": "Reuters: глобальная распродажа чипов и переоценка риска",
        "asml-q2": "ASML: результаты второго квартала 2026",
        "twse": "Taiwan Stock Exchange",
        "hyperliquid-api": "Hyperliquid Info API",
        "hyperliquid-docs": "Документация Hyperliquid HIP-3 / metaAndAssetCtxs",
        "man-group": "Man Group: полупроводники входят в фазу отбора",
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
        "zh-cn": ("2340-2350 / 毛利率与资本开支", "广泛科技去风险", "油价 / 美债收益率 / 美元", "美股正股与 ETF 确认", "资本回报与自由现金流"),
        "zh-hant": ("2340-2350 / 毛利率與資本開支", "廣泛科技去風險", "油價 / 美債殖利率 / 美元", "美股現貨與 ETF 確認", "資本回報與自由現金流"),
        "en": ("2340-2350 / margin and capex", "broad tech de-risking", "oil / Treasury yields / dollar", "U.S. cash and ETF confirmation", "capital returns and free cash flow"),
        "ru": ("2340-2350 / маржа и капзатраты", "широкое снижение риска в технологиях", "нефть / доходности США / доллар", "подтверждение спотом США и ETF", "отдача капитала и свободный денежный поток"),
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
              <div class="brief-item"><strong>NVDA / AMD / MU / SNDK</strong><span>{watch_labels[1]}</span></div>
              <div class="brief-item"><strong>WTI / US10Y / USD</strong><span>{watch_labels[2]}</span></div>
              <div class="brief-item"><strong>TAIEX / SOXX / SMH</strong><span>{watch_labels[3]}</span></div>
              <div class="brief-item"><strong>TSMC CapEx / Margin</strong><span>{watch_labels[4]}</span></div>
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
        "zh-cn": ("ASML 上调指引，存储链再度去杠杆", "上一篇市场日报。", "归档"),
        "zh-hant": ("ASML 上調指引，記憶體鏈再度去槓桿", "上一篇市場日報。", "歸檔"),
        "en": ("ASML raises guidance as memory de-leverages again", "Previous market brief.", "Archive"),
        "ru": ("ASML повышает прогноз, а память снова снижает плечо", "Предыдущий обзор рынка.", "Архив"),
    }[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-07-16")}"><span class="history-date">2026-07-16</span><span><span class="history-title">{html.escape(previous[0])}</span><span class="history-summary">{html.escape(previous[1])}</span></span><span class="history-tag">{html.escape(previous[2])}</span></a>
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
