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

DATE = "2026-07-23"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-23-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-23-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-23-en.svg",
    "ru": "/daily/images/market-brief-2026-07-23-ru.svg",
}

META = {
    "zh-cn": {
        "title": "Alphabet 确认 AI 需求，云厂资本回报开始承压",
        "desc": "2026-07-23 GateAffiliate 每日市场日报：Alphabet Cloud 增长 82%并上调资本开支，但自由现金流转负；AI 供应链上涨、GOOGL 下跌，台股冲高回落且油价继续压制估值。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "Alphabet 确认 AI 需求，云厂资本回报开始承压。",
        "summary": "Google Cloud 增长 82%、算力仍受供给约束，但季度资本开支超过经营现金流，自由现金流转负。供应链受益与云厂估值压力正式分化。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "Alphabet 確認 AI 需求，雲端業者資本回報開始承壓",
        "desc": "2026-07-23 GateAffiliate 每日市場日報：Alphabet Cloud 增長 82%並上調資本開支，但自由現金流轉負；AI 供應鏈上漲、GOOGL 下跌，台股衝高回落且油價繼續壓制估值。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "Alphabet 確認 AI 需求，雲端業者資本回報開始承壓。",
        "summary": "Google Cloud 增長 82%、算力仍受供給約束，但季度資本開支超過經營現金流，自由現金流轉負。供應鏈受益與雲端業者估值壓力正式分化。",
        "tag": "最新",
    },
    "en": {
        "title": "Alphabet confirms AI demand as hyperscaler capital returns come under pressure",
        "desc": "GateAffiliate's 2026-07-23 brief: Alphabet Cloud grows 82% and capex rises, but free cash flow turns negative; AI suppliers gain while GOOGL falls, Taiwan fades and oil caps valuations.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "Alphabet confirms AI demand as hyperscaler capital returns come under pressure.",
        "summary": "Google Cloud grows 82% and compute remains supply constrained, but quarterly capex exceeds operating cash flow and free cash flow turns negative. Supplier upside now diverges from hyperscaler valuation pressure.",
        "tag": "Latest",
    },
    "ru": {
        "title": "Alphabet подтверждает AI-спрос, но отдача облачного капитала под давлением",
        "desc": "Обзор GateAffiliate за 2026-07-23: Cloud Alphabet растет на 82%, но свободный денежный поток становится отрицательным; поставщики AI растут, GOOGL падает, Тайвань слабеет, нефть ограничивает оценки.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "Alphabet подтверждает AI-спрос, но отдача облачного капитала под давлением.",
        "summary": "Google Cloud растет на 82%, вычисления ограничены предложением, но капзатраты превышают операционный поток, а свободный поток становится отрицательным. Поставщики и облачные оценки расходятся.",
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

CONCISE_SECTIONS.update({
    "zh-cn": [
        ("核心结论", [
            "台股出现超跌修复，但尚未确认趋势反转。台湾加权指数接近平盘，台积电较前收反弹约 1.7%-2.0%；上周五台积电跌 7.29%，台股成交约 1.213 万亿新台币，今天首先应视为大幅换手后的技术修复。",
            "AI 产业基本面仍强，股票却继续消化高估值与拥挤仓位。台积电利润增长 77%、上调全年收入指引，ASML 也提高收入与产能计划；市场焦点已转向资本开支能否产生足够毛利率、自由现金流与股东回报。",
        ]),
        ("低流动性修复与能源压力", [
            "周末 TraderXYZ 前十名义成交量约 13.5 亿美元，较上周五下降约 63%，且 SKHX 占约 39%。MU、SK 海力士与大盘合约小幅回升，只能说明恐慌缓和，不能证明芯片股已经见底。",
            "WTI 约 83.8 美元、Brent 约 88.2 美元。能源进口经济体与高耗电 AI 基础设施同时承受成本压力，油价将继续通过通胀、汇率和政策利率影响科技估值。",
            "本周验证点转向 Alphabet 的 AI 资本开支、云收入与商业化，同时关注 Tesla、ECB、欧美 PMI、中国 LPR 以及美联储会议前的利率定价。",
        ]),
        ("本周观察框架", [
            "台湾市场观察 42000-43000 点区间承接，以及台积电能否稳定在 2300 上方并出现缩量止跌。",
            "美股开盘后用 TSM、NVDA、AMD、MU、SKHY、SNDK 正股，SOXX / SMH 与期权隐含波动率验证低成交永续信号。",
            "重点监控 Brent 90 美元关口、美元与美债收益率。中期仍优先选择订单、产能和现金流可验证的企业，降低对只依靠估值扩张品种的容忍度。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "台股出現超跌修復，但尚未確認趨勢反轉。台灣加權指數接近平盤，台積電較前收反彈約 1.7%-2.0%；上週五台積電跌 7.29%，台股成交約 1.213 萬億新台幣，今天首先應視為大幅換手後的技術修復。",
            "AI 產業基本面仍強，股票卻繼續消化高估值與擁擠部位。台積電利潤增長 77%、上調全年收入指引，ASML 也提高收入與產能計畫；市場焦點已轉向資本開支能否產生足夠毛利率、自由現金流與股東回報。",
        ]),
        ("低流動性修復與能源壓力", [
            "週末 TraderXYZ 前十名義成交量約 13.5 億美元，較上週五下降約 63%，且 SKHX 佔約 39%。MU、SK 海力士與大盤合約小幅回升，只能說明恐慌緩和，不能證明晶片股已經見底。",
            "WTI 約 83.8 美元、Brent 約 88.2 美元。能源進口經濟體與高耗電 AI 基礎設施同時承受成本壓力，油價將繼續透過通膨、匯率和政策利率影響科技估值。",
            "本週驗證點轉向 Alphabet 的 AI 資本開支、雲端收入與商業化，同時關注 Tesla、ECB、歐美 PMI、中國 LPR 以及聯準會會議前的利率定價。",
        ]),
        ("本週觀察框架", [
            "台灣市場觀察 42000-43000 點區間承接，以及台積電能否穩定在 2300 上方並出現縮量止跌。",
            "美股開盤後以 TSM、NVDA、AMD、MU、SKHY、SNDK 現貨，SOXX / SMH 與期權隱含波動率驗證低成交永續訊號。",
            "重點監控 Brent 90 美元關口、美元與美債殖利率。中期仍優先選擇訂單、產能和現金流可驗證的企業，降低對只依靠估值擴張品種的容忍度。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "Taiwan is staging an oversold rebound, not a confirmed trend reversal. The index is nearly flat and TSMC is up roughly 1.7%-2.0%; after Friday's 7.29% TSMC drop and NT$1.213 trillion turnover, today's move is best treated as a technical repair after heavy rotation.",
            "AI fundamentals remain firm while equities digest high valuations and crowded positioning. TSMC grew profit 77% and raised revenue guidance, while ASML lifted its outlook and capacity plans. The debate has moved to whether capex can deliver margin, free cash flow and shareholder returns.",
        ]),
        ("Thin Repair, Higher Energy Risk", [
            "TraderXYZ top-ten notional volume was about $1.35 billion, down roughly 63% from Friday, with SKHX alone near 39%. Small gains in MU, SK Hynix and index contracts suggest fear is easing, but cannot establish a bottom in cash semiconductor shares.",
            "WTI is near $83.8 and Brent $88.2. Energy-importing economies and power-intensive AI infrastructure both face rising costs, leaving oil as a channel into inflation, currencies, policy rates and technology valuations.",
            "This week's test shifts to Alphabet's AI capex, cloud revenue and monetization, alongside Tesla, the ECB, U.S. and European PMIs, China's LPR and rate pricing ahead of the Federal Reserve meeting.",
        ]),
        ("Weekly Watch Frame", [
            "Watch support across 42000-43000 in Taiwan and whether TSMC can stabilize above 2300 on declining volume.",
            "At the U.S. open, validate thin perpetual signals through TSM, NVDA, AMD, MU, SKHY and SNDK cash shares, SOXX / SMH and implied volatility.",
            "Monitor Brent near $90, the dollar and Treasury yields. Medium term, favor companies with verifiable orders, capacity and cash flow while demanding more from valuation-dependent trades.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Тайвань показывает технический отскок, но разворот тренда не подтвержден. Индекс почти не меняется, TSMC растет примерно на 1,7%-2,0%; после падения TSMC на 7,29% и оборота NT$1,213 трлн в пятницу это прежде всего восстановление после крупной смены позиций.",
            "Фундамент AI остается сильным, а акции переваривают дорогую оценку и перегретые позиции. Прибыль TSMC выросла на 77%, прогноз выручки повышен, ASML также улучшила прогноз и план мощностей. Теперь рынок требует маржу, свободный денежный поток и отдачу акционерам.",
        ]),
        ("Тонкий Отскок и Энергетический Риск", [
            "Оборот первой десятки TraderXYZ составил около $1,35 млрд, на 63% меньше пятницы, а доля SKHX достигла 39%. Небольшой рост MU, SK Hynix и индексов говорит лишь об ослаблении страха, но не подтверждает дно акций чипов.",
            "WTI около $83,8, Brent $88,2. Импортеры энергии и энергоемкая AI-инфраструктура сталкиваются с ростом затрат; нефть продолжит влиять на инфляцию, валюты, ставки и оценки технологий.",
            "Проверка недели смещается к AI-капзатратам, облачной выручке и монетизации Alphabet, а также Tesla, ЕЦБ, PMI США и Европы, LPR Китая и ожиданиям перед заседанием ФРС.",
        ]),
        ("Рамка Наблюдения на Неделю", [
            "Следите за поддержкой Тайваня в диапазоне 42000-43000 и способностью TSMC удержаться выше 2300 при снижении объема.",
            "На открытии США проверяйте слабый сигнал перпетуалов через акции TSM, NVDA, AMD, MU, SKHY, SNDK, фонды SOXX / SMH и подразумеваемую волатильность.",
            "Контролируйте Brent у $90, доллар и доходности США. В среднесрочном горизонте приоритет у компаний с проверяемыми заказами, мощностями и денежным потоком.",
        ]),
    ],
})

CONCISE_SECTIONS.update({
    "zh-cn": [
        ("核心结论", [
            "台湾科技股进入第二天修复，强度与市场广度都明显改善。加权指数上涨约 3.8%并接近日内高位，台积电上涨约 3%；指数强于权重股，说明风险回补已扩散到其他电子、金融与传统行业。",
            "能源压力暂时缓和是反弹的重要条件。WTI 与 Brent 分别回落约 1.9%和 1.7%，存储、韩国市场与 AI 芯片合约同步回升，再次体现油价与高估值科技之间的负相关。",
        ]),
        ("反弹增强，但尚未确认新趋势", [
            "费城半导体指数周一反弹约 1.6%，但仍较 6 月高点低逾 20%。TraderXYZ 前十名义成交量回升至约 28.4 亿美元、较昨日翻倍，方向可信度改善，但仍需美国正股、ETF 与期权市场确认。",
            "存储链反弹最强：SKHX、SNDK、MU、DRAM 与三星相关合约普遍上涨约 5%-9%。这是阶段性底部的积极信号，也可能包含空头回补；若美股现货缩量冲高回落，仍要防杠杆溢价回吐。",
            "本周真正的基本面验证来自 Alphabet。Google Cloud 增速、AI 资本开支、Gemini 商业化、自研芯片效率与搜索利润率，将决定网络、ASIC、光模块、服务器和电力链的下一阶段定价。",
        ]),
        ("今日观察框架", [
            "台湾市场观察指数能否收在 43800-44000 上方，以及台积电能否站稳 2380 并靠近 2400 收盘。",
            "美股开盘后比较 MU、SKHY、SNDK、AMD、NVDA 正股与 TraderXYZ 涨幅，并观察 SOXX / SMH 成交量、市场广度和期权偏度。",
            "宏观关注 Brent 能否回到 85 美元下方、10 年期美债收益率能否回落，以及中东停火方案是否出现可验证进展。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "台灣科技股進入第二天修復，強度與市場廣度都明顯改善。加權指數上漲約 3.8%並接近日內高位，台積電上漲約 3%；指數強於權重股，說明風險回補已擴散到其他電子、金融與傳統行業。",
            "能源壓力暫時緩和是反彈的重要條件。WTI 與 Brent 分別回落約 1.9%和 1.7%，記憶體、韓國市場與 AI 晶片合約同步回升，再次體現油價與高估值科技之間的負相關。",
        ]),
        ("反彈增強，但尚未確認新趨勢", [
            "費城半導體指數週一反彈約 1.6%，但仍較 6 月高點低逾 20%。TraderXYZ 前十名義成交量回升至約 28.4 億美元、較昨日翻倍，方向可信度改善，但仍需美國現貨、ETF 與期權市場確認。",
            "記憶體鏈反彈最強：SKHX、SNDK、MU、DRAM 與三星相關合約普遍上漲約 5%-9%。這是階段性底部的積極訊號，也可能包含空頭回補；若美股現貨縮量衝高回落，仍要防槓桿溢價回吐。",
            "本週真正的基本面驗證來自 Alphabet。Google Cloud 增速、AI 資本開支、Gemini 商業化、自研晶片效率與搜尋利潤率，將決定網路、ASIC、光模組、伺服器和電力鏈的下一階段定價。",
        ]),
        ("今日觀察框架", [
            "台灣市場觀察指數能否收在 43800-44000 上方，以及台積電能否站穩 2380 並靠近 2400 收盤。",
            "美股開盤後比較 MU、SKHY、SNDK、AMD、NVDA 現貨與 TraderXYZ 漲幅，並觀察 SOXX / SMH 成交量、市場廣度和期權偏度。",
            "宏觀關注 Brent 能否回到 85 美元下方、10 年期美債殖利率能否回落，以及中東停火方案是否出現可驗證進展。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "Taiwan technology enters a stronger second day of repair with better breadth. The index rises about 3.8% near its intraday high and TSMC gains roughly 3%; the index outperforming its largest weight shows risk buying has spread beyond one stock.",
            "Temporary relief in energy is an important condition for the rebound. WTI and Brent fall about 1.9% and 1.7%, while memory, Korea and AI-chip contracts rise together, reinforcing the negative relationship between oil and high-valuation technology.",
        ]),
        ("A Stronger Rebound, Not Yet a New Trend", [
            "The Philadelphia Semiconductor Index rebounded about 1.6% Monday but remains more than 20% below its June high. TraderXYZ top-ten notional volume doubled to roughly $2.84 billion, improving directional confidence but still requiring confirmation from U.S. cash, ETFs and options.",
            "Memory leads with SKHX, SNDK, MU, DRAM and Samsung-linked contracts up roughly 5%-9%. That is constructive for a potential tactical bottom, but may include short covering; a low-volume fade in cash shares would expose leverage premium in perpetuals.",
            "Alphabet provides the week's real fundamental test. Google Cloud growth, AI capex, Gemini monetization, custom-chip efficiency and search margins will shape the next move in networking, ASICs, optics, servers and power infrastructure.",
        ]),
        ("Today's Watch Frame", [
            "Watch whether Taiwan closes above 43800-44000 and whether TSMC holds 2380 while approaching 2400 into the close.",
            "At the U.S. open, compare MU, SKHY, SNDK, AMD and NVDA cash moves with TraderXYZ, alongside SOXX / SMH volume, market breadth and options skew.",
            "Macro checks are Brent below $85, a retreat in the U.S. 10-year yield and verifiable progress toward a Middle East ceasefire.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Технологии Тайваня проводят второй, заметно более сильный день восстановления. Индекс растет примерно на 3,8% у дневного максимума, TSMC почти на 3%; опережение индекса показывает, что покупки распространились на другие отрасли.",
            "Временное ослабление энергетического давления поддерживает отскок. WTI и Brent падают примерно на 1,9% и 1,7%, а память, Корея и AI-чипы растут вместе, подтверждая обратную связь нефти и дорогих технологий.",
        ]),
        ("Отскок Сильнее, Новый Тренд не Подтвержден", [
            "Филадельфийский индекс чипов вырос в понедельник на 1,6%, но остается более чем на 20% ниже июньского пика. Оборот первой десятки TraderXYZ удвоился до $2,84 млрд, однако сигнал еще должны подтвердить акции, ETF и опционы США.",
            "Память лидирует: SKHX, SNDK, MU, DRAM и контракты Samsung растут примерно на 5%-9%. Это позитивно для тактического дна, но часть движения может быть закрытием шортов; слабый спот вернет премию плеча назад.",
            "Главная фундаментальная проверка недели — Alphabet. Рост Google Cloud, AI-капзатраты, монетизация Gemini, эффективность собственных чипов и маржа поиска зададут направление сетям, ASIC, оптике, серверам и энергетике.",
        ]),
        ("Рамка Наблюдения", [
            "Следите, закроется ли Тайвань выше 43800-44000 и удержит ли TSMC 2380 с движением к 2400.",
            "На открытии США сравните MU, SKHY, SNDK, AMD и NVDA с TraderXYZ, а также объем SOXX / SMH, ширину рынка и скью опционов.",
            "Макроориентиры: Brent ниже $85, снижение доходности 10-летних облигаций США и проверяемый прогресс к перемирию на Ближнем Востоке.",
        ]),
    ],
})

CONCISE_SECTIONS.update({
    "zh-cn": [
        ("核心结论", [
            "AI 硬件反弹获得成交支持。Micron 上涨 12.2%，Nvidia 上涨约 2%；TraderXYZ 前十成交中，MU、SK 海力士、SNDK 与 DRAM 占据四席，资金正在集中回补存储与 AI 硬件链。",
            "台湾市场出现指数强、台积电弱的分化。加权指数盘中上涨约 1.85%至 45050 附近，台积电却在 2400 附近略低于前收，并从 2445 回落；这更像广泛修复与板块轮动，而非单一权重股推动。",
        ]),
        ("反弹有基础，宏观仍有约束", [
            "Brent 上一交易日结算约 91.01 美元，10 年期美债收益率升至约 4.63%。股市上涨而原油与收益率同步走高，利好盈利上修明确的硬件股，却限制依赖远期现金流的高估值资产。",
            "存储仍是最强也最拥挤的交易。MU 合约再涨约 6.5%，SNDK、SKHY 与 DRAM 同步上行，前十名义成交约 28.2 亿美元；工作日成交提高信号价值，但仍不能替代美股正股、ETF 与期权定价。",
            "台积电长期需求没有破坏，但股价分化显示市场正在审视海外扩产成本、折旧和三季度 65%-67% 的毛利率指引。若资本开支继续上调而利润率回落，估值中枢仍需调整。",
        ]),
        ("Alphabet 财报验证", [
            "今晚重点依次是 Google Cloud 增速、AI 资本开支、Gemini 与搜索 AI 的变现、Cloud 利润率及自由现金流，而不只是营收是否达标。",
            "若 Cloud 保持高增长且利润率稳定，GPU、HBM、先进封装、光模块和数据中心电力链会获得更强基本面支持；若收入达标但自由现金流继续恶化，资本开支上调会被重估为回报周期拉长。",
            "未来 24 小时同时观察 Brent 能否站稳 90 美元、10 年期收益率是否靠近 4.7%，以及台积电能否重新跑赢台湾指数。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "AI 硬體反彈獲得成交支持。Micron 上漲 12.2%，Nvidia 上漲約 2%；TraderXYZ 前十成交中，MU、SK 海力士、SNDK 與 DRAM 佔據四席，資金正在集中回補記憶體與 AI 硬體鏈。",
            "台灣市場出現指數強、台積電弱的分化。加權指數盤中上漲約 1.85%至 45050 附近，台積電卻在 2400 附近略低於前收，並從 2445 回落；這更像廣泛修復與板塊輪動，而非單一權重股推動。",
        ]),
        ("反彈有基礎，宏觀仍有約束", [
            "Brent 上一交易日結算約 91.01 美元，10 年期美債殖利率升至約 4.63%。股市上漲而原油與殖利率同步走高，利好盈利上修明確的硬體股，卻限制依賴遠期現金流的高估值資產。",
            "記憶體仍是最強也最擁擠的交易。MU 合約再漲約 6.5%，SNDK、SKHY 與 DRAM 同步上行，前十名義成交約 28.2 億美元；工作日成交提高訊號價值，但仍不能替代美股現貨、ETF 與期權定價。",
            "台積電長期需求沒有破壞，但股價分化顯示市場正在審視海外擴產成本、折舊和三季度 65%-67% 的毛利率指引。若資本開支持續上調而利潤率回落，估值中樞仍需調整。",
        ]),
        ("Alphabet 財報驗證", [
            "今晚重點依次是 Google Cloud 增速、AI 資本開支、Gemini 與搜尋 AI 的變現、Cloud 利潤率及自由現金流，而不只是營收是否達標。",
            "若 Cloud 保持高增長且利潤率穩定，GPU、HBM、先進封裝、光模組和資料中心電力鏈會獲得更強基本面支持；若收入達標但自由現金流繼續惡化，資本開支上調會被重估為回報週期拉長。",
            "未來 24 小時同時觀察 Brent 能否站穩 90 美元、10 年期殖利率是否靠近 4.7%，以及台積電能否重新跑贏台灣指數。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "The AI hardware rebound has volume behind it. Micron rose 12.2% and Nvidia about 2%; MU, SK Hynix, SNDK and DRAM take four places in TraderXYZ's top ten, showing concentrated buying across memory and AI hardware.",
            "Taiwan shows a strong-index, weak-TSMC divergence. The index gains roughly 1.85% near 45050 while TSMC trades around 2400, slightly below its prior close after retreating from 2445. This is broad rotation rather than a one-stock rally.",
        ]),
        ("A Supported Rebound With Macro Constraints", [
            "Brent settled near $91.01 and the U.S. 10-year yield rose to about 4.63%. Equities rising alongside oil and yields favors hardware with visible earnings upgrades but constrains expensive assets dependent on distant cash flows.",
            "Memory remains both the strongest and most crowded trade. MU perpetuals add about 6.5% as SNDK, SKHY and DRAM rise, with top-ten notional volume near $2.82 billion. Weekday volume improves the signal but cannot replace cash, ETF and options price discovery.",
            "TSMC's long-term demand remains intact, yet its relative weakness shows investors are pricing overseas expansion, depreciation and third-quarter gross-margin guidance of 65%-67%. Higher capex with lower margins would still pressure valuation.",
        ]),
        ("Alphabet Earnings Test", [
            "Tonight's sequence is Google Cloud growth, AI capex, Gemini and search-AI monetization, Cloud margin and free cash flow, not simply whether revenue meets consensus.",
            "If Cloud stays fast and profitable, GPUs, HBM, advanced packaging, optics and data-center power gain stronger fundamental support. If revenue meets expectations while free cash flow worsens, higher capex will be repriced as a longer return cycle.",
            "Over the next 24 hours, also watch Brent above $90, the 10-year yield toward 4.7% and whether TSMC can regain leadership over Taiwan's index.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Отскок AI-оборудования подтверждается оборотом. Micron выросла на 12,2%, Nvidia примерно на 2%; MU, SK Hynix, SNDK и DRAM занимают четыре места в первой десятке TraderXYZ, показывая концентрацию покупок в памяти и AI-оборудовании.",
            "На Тайване сильный индекс расходится со слабой TSMC. Индекс растет примерно на 1,85% к 45050, а TSMC около 2400, чуть ниже прошлого закрытия после отката от 2445. Это широкая ротация, а не рост одной акции.",
        ]),
        ("Отскок Поддержан, Макроусловия Ограничивают", [
            "Brent закрылся около $91,01, доходность 10-летних облигаций США выросла до 4,63%. Одновременный рост акций, нефти и ставок помогает оборудованию с ростом прибыли, но ограничивает дорогие активы с далекими денежными потоками.",
            "Память остается самым сильным и перегретым сегментом. MU прибавляет 6,5%, SNDK, SKHY и DRAM также растут, а оборот первой десятки около $2,82 млрд. Рабочий день улучшает сигнал, но не заменяет акции, ETF и опционы.",
            "Долгосрочный спрос TSMC не нарушен, однако слабость акции отражает затраты зарубежного расширения, амортизацию и прогноз маржи 65%-67%. Рост капзатрат при снижении маржи продолжит давить на оценку.",
        ]),
        ("Проверка Отчетом Alphabet", [
            "Сегодня важны рост Google Cloud, AI-капзатраты, монетизация Gemini и AI-поиска, маржа Cloud и свободный денежный поток, а не только выполнение прогноза выручки.",
            "Сильный и прибыльный Cloud поддержит GPU, HBM, передовую упаковку, оптику и энергетику дата-центров. Если выручка выполнит прогноз, а денежный поток ухудшится, рост капзатрат будет означать более долгий цикл отдачи.",
            "В ближайшие сутки следите за Brent выше $90, доходностью к 4,7% и способностью TSMC снова опередить индекс Тайваня.",
        ]),
    ],
})

CONCISE_SECTIONS.update({
    "zh-cn": [
        ("核心结论", [
            "Alphabet 财报确认 AI 算力需求仍比预期更紧。Google Cloud 收入同比增长 82%，积压订单增至 5140 亿美元，公司明确表示算力仍受供给约束，并把 2026 年资本开支指引上调至 1950 亿-2050 亿美元。",
            "同一份财报也让资本回报压力正式进入报表。季度资本开支 449.24 亿美元，超过 390.69 亿美元经营现金流，自由现金流转为负 58.55 亿美元。供应链上涨而 GOOGL 下跌，准确反映需求利好与购买方估值压力的分化。",
        ]),
        ("供应链受益，云厂现金流承压", [
            "Cloud 营收 247.68 亿美元、利润率约 35.6%，搜索收入增长 17%，说明 AI 已贡献收入且暂未破坏搜索商业模式；但 GAAP 利润包含大额投资收益，核心盈利并没有表面数字那么强。",
            "TraderXYZ 前十名义成交约 35.15 亿美元，较昨日增加约 25%。MU、SK 海力士、SNDK、DRAM、AMD 与 Nvidia 上涨，GOOGL 跌约 4.7%，跨市场方向与财报逻辑一致。",
            "台湾指数早盘冲高后跌约 0.8%，台积电在 2375-2380、较前收低约 1%。Alphabet 上调资本开支强化先进制程与互连订单，但台积电仍受三季度毛利率、海外厂成本和高基数估值约束。",
        ]),
        ("风险阈值与下一验证", [
            "Brent 结算升至 94.07 美元，10 年期美债收益率约 4.65%。若 Brent 站稳 95 美元且收益率突破 4.7%，科技盈利上修可能继续被估值下调抵消。",
            "AI 上游维持结构性偏多，但优先选择订单、定价权与自由现金流兼备的存储、先进封装、光互连、电力和模拟芯片环节，避免只根据单日永续合约追价。",
            "未来 24 小时关注 Intel 的数据中心、18A、代工利用率与现金流，欧洲央行措辞，以及 Alphabet 正式交易能否收复盘后跌幅。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "Alphabet 財報確認 AI 算力需求仍比預期更緊。Google Cloud 收入年增 82%，積壓訂單增至 5140 億美元，公司明確表示算力仍受供給約束，並把 2026 年資本開支指引上調至 1950 億-2050 億美元。",
            "同一份財報也讓資本回報壓力正式進入報表。季度資本開支 449.24 億美元，超過 390.69 億美元經營現金流，自由現金流轉為負 58.55 億美元。供應鏈上漲而 GOOGL 下跌，準確反映需求利好與購買方估值壓力的分化。",
        ]),
        ("供應鏈受益，雲端業者現金流承壓", [
            "Cloud 營收 247.68 億美元、利潤率約 35.6%，搜尋收入增長 17%，說明 AI 已貢獻收入且暫未破壞搜尋商業模式；但 GAAP 利潤包含大額投資收益，核心盈利沒有表面數字那麼強。",
            "TraderXYZ 前十名義成交約 35.15 億美元，較昨日增加約 25%。MU、SK 海力士、SNDK、DRAM、AMD 與 Nvidia 上漲，GOOGL 跌約 4.7%，跨市場方向與財報邏輯一致。",
            "台灣指數早盤衝高後跌約 0.8%，台積電在 2375-2380、較前收低約 1%。Alphabet 上調資本開支強化先進製程與互連訂單，但台積電仍受三季度毛利率、海外廠成本和高基數估值約束。",
        ]),
        ("風險閾值與下一驗證", [
            "Brent 結算升至 94.07 美元，10 年期美債殖利率約 4.65%。若 Brent 站穩 95 美元且殖利率突破 4.7%，科技盈利上修可能繼續被估值下調抵消。",
            "AI 上游維持結構性偏多，但優先選擇訂單、定價權與自由現金流兼備的記憶體、先進封裝、光互連、電力和類比晶片環節，避免只根據單日永續合約追價。",
            "未來 24 小時關注 Intel 的資料中心、18A、代工利用率與現金流，歐洲央行措辭，以及 Alphabet 正式交易能否收復盤後跌幅。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "Alphabet confirms AI compute demand is tighter than expected. Google Cloud revenue grows 82%, backlog reaches $514 billion and management says compute remains supply constrained, while lifting 2026 capex guidance to $195-205 billion.",
            "The same report puts capital-return pressure directly into the accounts. Quarterly capex of $44.924 billion exceeds $39.069 billion of operating cash flow, turning free cash flow negative by $5.855 billion. Suppliers rise while GOOGL falls, capturing the demand-versus-buyer split.",
        ]),
        ("Supplier Upside, Hyperscaler Cash Pressure", [
            "Cloud revenue reaches $24.768 billion with roughly 35.6% margin, while search grows 17%, showing AI is monetizing without yet breaking search. Yet GAAP profit contains a large investment gain, so core earnings are less spectacular than the headline.",
            "TraderXYZ top-ten notional volume rises about 25% to $3.515 billion. MU, SK Hynix, SNDK, DRAM, AMD and Nvidia gain while GOOGL falls about 4.7%, a cross-market pattern consistent with the earnings logic.",
            "Taiwan fades from an early gain to about -0.8%, with TSMC at 2375-2380, roughly 1% below its prior close. Higher Alphabet capex supports advanced nodes and interconnect orders, but TSMC still faces margin, overseas-cost and valuation constraints.",
        ]),
        ("Risk Thresholds and Next Tests", [
            "Brent settles at $94.07 and the U.S. 10-year yield near 4.65%. If Brent holds $95 and yields break 4.7%, higher technology earnings can continue to be offset by multiple compression.",
            "Stay structurally constructive on AI suppliers, prioritizing memory, advanced packaging, optical interconnects, power and analog chips with visible orders, pricing power and free cash flow rather than chasing one-day perpetual moves.",
            "The next 24 hours bring Intel's data-center, 18A, foundry-utilization and cash-flow test, the ECB's policy language and whether Alphabet cash trading recovers its post-earnings decline.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Alphabet подтверждает, что спрос на AI-вычисления сильнее ожиданий. Выручка Google Cloud растет на 82%, портфель заказов достигает $514 млрд, мощности ограничены предложением, а прогноз капзатрат 2026 повышен до $195-205 млрд.",
            "Тот же отчет показывает давление на отдачу капитала. Капзатраты $44,924 млрд превышают операционный поток $39,069 млрд, свободный поток становится отрицательным на $5,855 млрд. Поставщики растут, GOOGL падает — спрос и оценка покупателя расходятся.",
        ]),
        ("Рост Поставщиков, Давление на Денежный Поток", [
            "Выручка Cloud достигает $24,768 млрд при марже около 35,6%, поиск растет на 17%: AI уже монетизируется и пока не разрушает поиск. Но GAAP-прибыль содержит крупный инвестиционный доход, поэтому базовая прибыль слабее заголовка.",
            "Оборот первой десятки TraderXYZ растет примерно на 25% до $3,515 млрд. MU, SK Hynix, SNDK, DRAM, AMD и Nvidia растут, а GOOGL падает на 4,7%, что соответствует логике отчета.",
            "Тайвань разворачивается от раннего роста к падению на 0,8%, TSMC торгуется 2375-2380, примерно на 1% ниже закрытия. Рост капзатрат Alphabet поддерживает заказы, но маржа, зарубежные затраты и оценка TSMC остаются ограничениями.",
        ]),
        ("Пороги Риска и Следующие Проверки", [
            "Brent закрывается на $94,07, доходность 10-летних облигаций США около 4,65%. Если Brent удержит $95, а доходность превысит 4,7%, рост прибыли технологий продолжит компенсироваться снижением мультипликаторов.",
            "Структурно позитивный взгляд на поставщиков AI сохраняется, но приоритет у памяти, упаковки, оптики, энергетики и аналоговых чипов с заказами, ценовой силой и свободным денежным потоком.",
            "В ближайшие сутки важны дата-центры, 18A, загрузка фабрик и денежный поток Intel, риторика ЕЦБ и способность Alphabet восстановиться после падения.",
        ]),
    ],
})

SOURCE_URLS = [
    ("alphabet-q2", "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf"),
    ("alphabet-call", "https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/"),
    ("reuters-alphabet", "https://www.reuters.com/business/google-quarterly-cloud-revenue-growth-beats-expectations-2026-07-22/"),
    ("ap-alphabet", "https://apnews.com/article/google-results-revenue-profit-ai-alphabet-f914606d842d4c6848019083d667fc3a"),
    ("ap-market-0722", "https://apnews.com/article/stocks-markets-iran-ai-trump-207dfa55d180fcc565420454178168c5"),
    ("tsmc-q2", "https://investor.tsmc.com/english/quarterly-results/2026/q2"),
    ("tesla-q2", "https://ir.tesla.com/press-release/tesla-releases-second-quarter-2026-financial-results"),
    ("ti-q2", "https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-07-22-ti-reports-second-quarter-2026-financial-results-and-shareholder-returns.html"),
    ("ibm-q2", "https://newsroom.ibm.com/2026-07-22-IBM-RELEASES-SECOND-QUARTER-RESULTS"),
    ("fed-mpr", "https://www.federalreserve.gov/monetarypolicy/2026-07-mpr-summary.htm"),
    ("goldman-ai", "https://www.goldmansachs.com/insights/articles/ai-investment-is-shifting-as-inference-enterprise-adoption-accelerate"),
    ("ubs-capex", "https://www.ubs.com/us/en/wealth-management/insights/market-news/article.3534348.html"),
    ("jpm-fed", "https://www.jpmorgan.com/insights/global-research/economy/fed-rate-cuts"),
    ("traderxyz", "https://traderxyz.com/"),
]

SOURCE_LABELS = {
    "zh-cn": {
        "bls-cpi": "美国劳工统计局：2026 年 6 月 CPI",
        "bls-ppi": "美国劳工统计局：2026 年 6 月 PPI",
        "tsmc-q2": "TSMC 2026 年第二季度业绩",
        "alphabet-q2": "Alphabet 2026 年第二季度官方财报",
        "alphabet-call": "Sundar Pichai：第二季度财报电话会发言",
        "reuters-alphabet": "Reuters：Alphabet 上调资本开支与 Cloud 增长",
        "ap-alphabet": "AP：Alphabet 第二季度财报",
        "ap-market-0722": "AP：7 月 22 日美股、油价与美债收益率",
        "tesla-q2": "Tesla 2026 年第二季度财报",
        "ti-q2": "Texas Instruments 2026 年第二季度业绩",
        "ibm-q2": "IBM 2026 年第二季度业绩",
        "fed-mpr": "美联储 2026 年 7 月货币政策报告",
        "goldman-ai": "Goldman Sachs AM：企业 AI 采用与算力约束",
        "ubs-capex": "UBS：AI 资本开支与回报风险",
        "jpm-fed": "J.P. Morgan：美联储政策展望",
        "ap-us-0721": "AP：7 月 21 日美股、芯片股与油价",
        "ap-asia-0722": "AP：7 月 22 日亚洲市场",
        "ig-alphabet": "IG：Alphabet 2026 年第二季度财报前瞻",
        "morningstar-alphabet": "Morningstar：Alphabet 财报前估值与基本面",
        "kiplinger-calendar": "Kiplinger：本周美股财报日历",
        "bofa-survey": "BofA：2026 年 7 月基金经理调查摘要",
        "traderxyz": "TraderXYZ 市场数据",
        "reuters-repair": "Reuters：7 月 20 日美股与芯片股修复",
        "ap-ai-oil": "AP：AI 股票企稳、油价与美债收益率上升",
        "reuters-bear": "Reuters：芯片指数进入技术性熊市",
        "reuters-macro": "Reuters：全球市场、中东冲突与油价",
        "focus-taiwan": "Focus Taiwan：7 月 17 日台股创纪录下跌",
        "taipei-times": "Taipei Times：7 月 17 日台股成交与下跌",
        "ap-global": "AP：全球 AI 股票抛售与油价上涨",
        "reuters-global": "Reuters：全球芯片股下跌",
        "ubs-volatility": "UBS：以分散和精选应对 AI 波动",
        "week-ahead": "本周全球央行与 PMI 前瞻",
        "dbs-week": "DBS：本周宏观前瞻",
        "imf-weo": "IMF：2026 年 7 月世界经济展望更新",
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
        "alphabet-q2": "Alphabet 2026 年第二季度官方財報",
        "alphabet-call": "Sundar Pichai：第二季度財報電話會發言",
        "reuters-alphabet": "Reuters：Alphabet 上調資本開支與 Cloud 增長",
        "ap-alphabet": "AP：Alphabet 第二季度財報",
        "ap-market-0722": "AP：7 月 22 日美股、油價與美債殖利率",
        "tesla-q2": "Tesla 2026 年第二季度財報",
        "ti-q2": "Texas Instruments 2026 年第二季度業績",
        "ibm-q2": "IBM 2026 年第二季度業績",
        "fed-mpr": "聯準會 2026 年 7 月貨幣政策報告",
        "goldman-ai": "Goldman Sachs AM：企業 AI 採用與算力約束",
        "ubs-capex": "UBS：AI 資本開支與回報風險",
        "jpm-fed": "J.P. Morgan：聯準會政策展望",
        "ap-us-0721": "AP：7 月 21 日美股、晶片股與油價",
        "ap-asia-0722": "AP：7 月 22 日亞洲市場",
        "ig-alphabet": "IG：Alphabet 2026 年第二季度財報前瞻",
        "morningstar-alphabet": "Morningstar：Alphabet 財報前估值與基本面",
        "kiplinger-calendar": "Kiplinger：本週美股財報日曆",
        "bofa-survey": "BofA：2026 年 7 月基金經理調查摘要",
        "traderxyz": "TraderXYZ 市場數據",
        "reuters-repair": "Reuters：7 月 20 日美股與晶片股修復",
        "ap-ai-oil": "AP：AI 股票企穩、油價與美債殖利率上升",
        "reuters-bear": "Reuters：晶片指數進入技術性熊市",
        "reuters-macro": "Reuters：全球市場、中東衝突與油價",
        "focus-taiwan": "Focus Taiwan：7 月 17 日台股創紀錄下跌",
        "taipei-times": "Taipei Times：7 月 17 日台股成交與下跌",
        "ap-global": "AP：全球 AI 股票拋售與油價上漲",
        "reuters-global": "Reuters：全球晶片股下跌",
        "ubs-volatility": "UBS：以分散和精選應對 AI 波動",
        "week-ahead": "本週全球央行與 PMI 前瞻",
        "dbs-week": "DBS：本週宏觀前瞻",
        "imf-weo": "IMF：2026 年 7 月世界經濟展望更新",
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
        "alphabet-q2": "Alphabet official Q2 2026 results",
        "alphabet-call": "Sundar Pichai: Q2 earnings-call remarks",
        "reuters-alphabet": "Reuters: Alphabet lifts capex as Cloud grows",
        "ap-alphabet": "AP: Alphabet second-quarter results",
        "ap-market-0722": "AP: July 22 stocks, oil and Treasury yields",
        "tesla-q2": "Tesla Q2 2026 results",
        "ti-q2": "Texas Instruments Q2 2026 results",
        "ibm-q2": "IBM Q2 2026 results",
        "fed-mpr": "Federal Reserve July 2026 Monetary Policy Report",
        "goldman-ai": "Goldman Sachs AM: enterprise AI and compute constraints",
        "ubs-capex": "UBS: AI capex and return risks",
        "jpm-fed": "J.P. Morgan: Federal Reserve policy outlook",
        "ap-us-0721": "AP: July 21 U.S. stocks, chips and oil",
        "ap-asia-0722": "AP: July 22 Asian markets",
        "ig-alphabet": "IG: Alphabet Q2 2026 earnings preview",
        "morningstar-alphabet": "Morningstar: Alphabet valuation before earnings",
        "kiplinger-calendar": "Kiplinger: weekly U.S. earnings calendar",
        "bofa-survey": "BofA: July 2026 fund manager survey summary",
        "traderxyz": "TraderXYZ market data",
        "reuters-repair": "Reuters: July 20 U.S. and chip-share repair",
        "ap-ai-oil": "AP: AI shares steady as oil and yields rise",
        "reuters-bear": "Reuters: chip index enters a technical bear market",
        "reuters-macro": "Reuters: global markets, Gulf conflict and oil",
        "focus-taiwan": "Focus Taiwan: record July 17 Taiwan decline",
        "taipei-times": "Taipei Times: July 17 Taiwan turnover and decline",
        "ap-global": "AP: global AI selloff and higher oil",
        "reuters-global": "Reuters: global chip shares decline",
        "ubs-volatility": "UBS: diversification and selection amid AI volatility",
        "week-ahead": "Week ahead: central banks and PMIs",
        "dbs-week": "DBS: weekly macro outlook",
        "imf-weo": "IMF: July 2026 World Economic Outlook update",
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
        "alphabet-q2": "Alphabet: официальный отчет за второй квартал 2026",
        "alphabet-call": "Sundar Pichai: комментарии к отчету за второй квартал",
        "reuters-alphabet": "Reuters: Alphabet повышает капзатраты на фоне роста Cloud",
        "ap-alphabet": "AP: результаты Alphabet за второй квартал",
        "ap-market-0722": "AP: акции, нефть и доходности 22 июля",
        "tesla-q2": "Tesla: результаты второго квартала 2026",
        "ti-q2": "Texas Instruments: результаты второго квартала 2026",
        "ibm-q2": "IBM: результаты второго квартала 2026",
        "fed-mpr": "ФРС: отчет о денежной политике, июль 2026",
        "goldman-ai": "Goldman Sachs AM: внедрение AI и дефицит вычислений",
        "ubs-capex": "UBS: AI-капзатраты и риски отдачи",
        "jpm-fed": "J.P. Morgan: прогноз политики ФРС",
        "ap-us-0721": "AP: акции США, чипы и нефть 21 июля",
        "ap-asia-0722": "AP: рынки Азии 22 июля",
        "ig-alphabet": "IG: прогноз отчета Alphabet за второй квартал 2026",
        "morningstar-alphabet": "Morningstar: оценка Alphabet перед отчетом",
        "kiplinger-calendar": "Kiplinger: календарь отчетов США на неделю",
        "bofa-survey": "BofA: опрос управляющих за июль 2026",
        "traderxyz": "Рыночные данные TraderXYZ",
        "reuters-repair": "Reuters: восстановление акций США и чипов 20 июля",
        "ap-ai-oil": "AP: AI-акции стабильны, нефть и доходности растут",
        "reuters-bear": "Reuters: индекс чипов входит в технический медвежий рынок",
        "reuters-macro": "Reuters: мировые рынки, конфликт в Персидском заливе и нефть",
        "focus-taiwan": "Focus Taiwan: рекордное падение Тайваня 17 июля",
        "taipei-times": "Taipei Times: оборот и падение Тайваня 17 июля",
        "ap-global": "AP: глобальная распродажа AI и рост нефти",
        "reuters-global": "Reuters: снижение мировых акций чипов",
        "ubs-volatility": "UBS: диверсификация при волатильности AI",
        "week-ahead": "Неделя впереди: центробанки и PMI",
        "dbs-week": "DBS: недельный макрообзор",
        "imf-weo": "IMF: обновление мирового прогноза, июль 2026",
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
        "zh-cn": ("2370-2400 / 毛利率约束", "供应链强于云厂", "Brent 95 / US10Y 4.7%", "冲高回落与收盘位置", "Cloud 利润与负自由现金流"),
        "zh-hant": ("2370-2400 / 毛利率約束", "供應鏈強於雲端業者", "Brent 95 / US10Y 4.7%", "衝高回落與收盤位置", "Cloud 利潤與負自由現金流"),
        "en": ("2370-2400 / margin constraint", "suppliers outperform hyperscalers", "Brent 95 / US10Y 4.7%", "failed rally and closing level", "Cloud profit and negative free cash flow"),
        "ru": ("2370-2400 / ограничение маржи", "поставщики сильнее облаков", "Brent 95 / US10Y 4,7%", "разворот роста и закрытие", "прибыль Cloud и отрицательный поток"),
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
              <div class="brief-item"><strong>GOOGL Cloud / CapEx</strong><span>{watch_labels[4]}</span></div>
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
        "zh-cn": ("AI 硬件反弹获成交确认，Alphabet 检验资本回报", "上一篇市场日报。", "归档"),
        "zh-hant": ("AI 硬體反彈獲成交確認，Alphabet 檢驗資本回報", "上一篇市場日報。", "歸檔"),
        "en": ("AI hardware rebound gains volume as Alphabet tests capital returns", "Previous market brief.", "Archive"),
        "ru": ("AI-оборудование растет на объеме: Alphabet проверит отдачу капитала", "Предыдущий обзор рынка.", "Архив"),
    }[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-07-22")}"><span class="history-date">2026-07-22</span><span><span class="history-title">{html.escape(previous[0])}</span><span class="history-summary">{html.escape(previous[1])}</span></span><span class="history-tag">{html.escape(previous[2])}</span></a>
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
