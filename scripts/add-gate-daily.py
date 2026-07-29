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

DATE = "2026-07-29"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-29-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-29-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-29-en.svg",
    "ru": "/daily/images/market-brief-2026-07-29-ru.svg",
}

META = {
    "zh-cn": {
        "title": "亚洲芯片二次去杠杆，强业绩也难阻估值收缩",
        "desc": "2026-07-29 GateAffiliate 每日市场日报：KOSPI 与台湾芯片继续去杠杆，SK 海力士创纪录业绩仍低于极高预期；Fed、Microsoft 与 Meta 将验证 AI 资本回报。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "亚洲芯片二次去杠杆，强业绩也难阻估值收缩。",
        "summary": "KOSPI 午间再跌约 8.2%、台湾指数跌约 4.9%。SK 海力士收入与利润创新高仍未满足极高预期，市场焦点已转向估值、杠杆与 AI 投资回报。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "亞洲晶片二次去槓桿，強業績也難阻估值收縮",
        "desc": "2026-07-29 GateAffiliate 每日市場日報：KOSPI 與台灣晶片繼續去槓桿，SK 海力士創紀錄業績仍低於極高預期；Fed、Microsoft 與 Meta 將驗證 AI 資本回報。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "亞洲晶片二次去槓桿，強業績也難阻估值收縮。",
        "summary": "KOSPI 午間再跌約 8.2%、台灣指數跌約 4.9%。SK 海力士收入與利潤創新高仍未滿足極高預期，市場焦點已轉向估值、槓桿與 AI 投資回報。",
        "tag": "最新",
    },
    "en": {
        "title": "Asian chips enter a second de-leveraging wave despite record results",
        "desc": "GateAffiliate's 2026-07-29 brief: KOSPI and Taiwan chips keep de-leveraging as record SK Hynix results miss extreme expectations; the Fed, Microsoft and Meta now test returns on AI capital.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "Asian chips enter a second de-leveraging wave despite record results.",
        "summary": "KOSPI falls another 8.2% and Taiwan about 4.9%. Record SK Hynix revenue and profit still miss extreme expectations, shifting the market toward valuation, leverage and returns on AI investment.",
        "tag": "Latest",
    },
    "ru": {
        "title": "Вторая волна снижения плеча в чипах Азии несмотря на рекорды",
        "desc": "Обзор GateAffiliate за 2026-07-29: KOSPI и чипы Тайваня продолжают снижать плечо, а рекорд SK Hynix не достигает крайних ожиданий; ФРС, Microsoft и Meta проверят отдачу AI-капитала.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "Вторая волна снижения плеча в чипах Азии несмотря на рекорды.",
        "summary": "KOSPI теряет еще 8,2%, Тайвань около 4,9%. Рекордные выручка и прибыль SK Hynix не достигают крайних ожиданий, поэтому рынок пересматривает оценки, плечо и отдачу AI-инвестиций.",
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

CONCISE_SECTIONS.update({
    "zh-cn": [
        ("核心结论", [
            "周末宏观环境边际改善，但只能定义为风险缓和。Brent 从上周五 96.78 美元进一步回落至约 91.73 美元，美债收益率下降、美股期货反弹；红海与霍尔木兹运输风险仍在，单日油价下跌不等于风险解除。",
            "本周决定 AI 行情的关键从需求转向资本回报。Microsoft、Meta、Amazon 与 Apple 集中披露财报；Alphabet 已经证明 Cloud 需求极强，却因资本开支超过经营现金流而遭遇估值下调。",
        ]),
        ("台积电抗跌，存储地区轮动", [
            "台湾指数盘中跌约 0.9%，台积电却在 2350-2355、接近前收并从低位回升，显示资金仍认可先进制程基本面，同时继续卖出高波动中小型科技股。只有重新站稳 2400 并持续跑赢大盘，才能确认估值重定价结束。",
            "存储链出现地区分化：上周五 MU 跌约 6.9%，今天 MU、SNDK 与 DRAM 温和上涨，SK 海力士相关合约下跌；CXMT 上海上市首日因稀缺性与低发行定价大涨，但不能据此推导 HBM 或全球存储基本面一天改变。",
            "TraderXYZ 前十名义成交约 14.81 亿美元，较上周工作日高峰下降约 58%，且 CXMT 事件占据大量成交。指数和原油方向仍有参考价值，单一个股尤其是 CXMT 与低成交 TSM 不适合作为精确定价。",
        ]),
        ("本周验证框架", [
            "Microsoft 与 Meta 重点看云增速、AI 收入、资本开支和自由现金流；Amazon 看 AWS 与约 2000 亿美元资本开支回报，Apple 则需要在接近高估值时交出几乎无瑕疵的结果。",
            "Intel 超预期却下跌，进一步说明需求增长不等于自由现金流转正。AI 上游仍偏多，但优先选择有技术壁垒、订单可见度与议价能力的先进制程、封装、存储和光互连。",
            "短线观察 Brent 能否稳定低于 90 美元、10 年期收益率能否守在 4.7%下方，以及台积电能否守住 2330-2350。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "週末宏觀環境邊際改善，但只能定義為風險緩和。Brent 從上週五 96.78 美元進一步回落至約 91.73 美元，美債殖利率下降、美股期貨反彈；紅海與霍爾木茲運輸風險仍在，單日油價下跌不等於風險解除。",
            "本週決定 AI 行情的關鍵從需求轉向資本回報。Microsoft、Meta、Amazon 與 Apple 集中披露財報；Alphabet 已經證明 Cloud 需求極強，卻因資本開支超過經營現金流而遭遇估值下調。",
        ]),
        ("台積電抗跌，記憶體地區輪動", [
            "台灣指數盤中跌約 0.9%，台積電卻在 2350-2355、接近前收並從低位回升，顯示資金仍認可先進製程基本面，同時繼續賣出高波動中小型科技股。只有重新站穩 2400 並持續跑贏大盤，才能確認估值重定價結束。",
            "記憶體鏈出現地區分化：上週五 MU 跌約 6.9%，今天 MU、SNDK 與 DRAM 溫和上漲，SK 海力士相關合約下跌；CXMT 上海上市首日因稀缺性與低發行定價大漲，但不能據此推導 HBM 或全球記憶體基本面一天改變。",
            "TraderXYZ 前十名義成交約 14.81 億美元，較上週工作日高峰下降約 58%，且 CXMT 事件佔據大量成交。指數和原油方向仍有參考價值，單一個股尤其是 CXMT 與低成交 TSM 不適合作為精確定價。",
        ]),
        ("本週驗證框架", [
            "Microsoft 與 Meta 重點看雲端增速、AI 收入、資本開支和自由現金流；Amazon 看 AWS 與約 2000 億美元資本開支回報，Apple 則需要在接近高估值時交出幾乎無瑕疵的結果。",
            "Intel 超預期卻下跌，進一步說明需求增長不等於自由現金流轉正。AI 上游仍偏多，但優先選擇有技術壁壘、訂單可見度與議價能力的先進製程、封裝、記憶體和光互連。",
            "短線觀察 Brent 能否穩定低於 90 美元、10 年期殖利率能否守在 4.7%下方，以及台積電能否守住 2330-2350。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "The weekend macro backdrop improves at the margin, but this is risk relief rather than risk resolution. Brent falls from Friday's $96.78 settlement toward $91.73, Treasury yields ease and U.S. futures rebound, while Red Sea and Hormuz shipping risks remain active.",
            "This week's AI question shifts from demand to capital returns. Microsoft, Meta, Amazon and Apple report in a cluster; Alphabet already proved Cloud demand is powerful, yet suffered valuation pressure because capex exceeded operating cash flow.",
        ]),
        ("TSMC Resilience, Regional Memory Rotation", [
            "Taiwan's index falls about 0.9% while TSMC trades near 2350-2355, close to its prior finish after recovering from the low. Investors still favor advanced-node fundamentals while selling volatile smaller technology. A sustained move above 2400 is needed to end the repricing debate.",
            "Memory diverges by region: MU fell about 6.9% Friday, while MU, SNDK and DRAM rise modestly today and SK Hynix-linked contracts fall. CXMT's Shanghai debut surges on scarcity and IPO pricing, but does not mean HBM or global memory fundamentals changed overnight.",
            "TraderXYZ top-ten notional volume is about $1.481 billion, down roughly 58% from last week's workday peak, with CXMT absorbing substantial activity. Index and oil direction remain useful; CXMT and thin TSM contracts do not offer precise fair value.",
        ]),
        ("Weekly Validation Frame", [
            "For Microsoft and Meta, prioritize cloud growth, AI revenue, capex and free cash flow. Amazon must validate AWS and roughly $200 billion of spending, while Apple needs a near-flawless print close to peak valuation.",
            "Intel beating expectations but falling reinforces that demand growth is not free-cash-flow conversion. Stay constructive upstream, favoring advanced nodes, packaging, memory and optics with technical barriers, visible orders and pricing power.",
            "Near-term checks are Brent sustainably below $90, the U.S. 10-year below 4.7% and TSMC holding 2330-2350.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "Макрофон выходных улучшился, но это ослабление риска, а не его исчезновение. Brent снижается с пятничных $96,78 к $91,73, доходности падают, фьючерсы США растут, однако риски перевозок в Красном море и Ормузском проливе сохраняются.",
            "Главный вопрос AI этой недели смещается от спроса к отдаче капитала. Microsoft, Meta, Amazon и Apple публикуют отчеты; Alphabet уже доказала силу Cloud, но получила снижение оценки из-за капзатрат выше операционного потока.",
        ]),
        ("Устойчивость TSMC и Региональная Ротация Памяти", [
            "Индекс Тайваня падает примерно на 0,9%, а TSMC держится у 2350-2355, около прошлого закрытия после восстановления от минимума. Рынок сохраняет доверие к передовым техпроцессам, продавая более волатильные малые технологии. Для завершения переоценки нужен устойчивый уровень выше 2400.",
            "Память расходится по регионам: MU потеряла 6,9% в пятницу, сегодня MU, SNDK и DRAM умеренно растут, а контракты SK Hynix падают. Взлет CXMT на дебюте отражает дефицит и цену IPO, но не означает мгновенной смены фундаментала HBM и мировой памяти.",
            "Оборот первой десятки TraderXYZ около $1,481 млрд, на 58% ниже рабочего пика прошлой недели; CXMT забирает значительную долю. Индексы и нефть полезны для направления, но CXMT и тонкий TSM не дают точной справедливой цены.",
        ]),
        ("Рамка Проверки Недели", [
            "У Microsoft и Meta важны рост облака, AI-выручка, капзатраты и свободный поток. Amazon должна подтвердить AWS и около $200 млрд расходов, Apple — показать почти безупречный отчет при высокой оценке.",
            "Падение Intel после сильного отчета показывает: рост спроса не равен свободному потоку. Вверх по цепочке приоритет у техпроцессов, упаковки, памяти и оптики с барьерами, заказами и ценовой силой.",
            "Краткосрочные ориентиры: Brent устойчиво ниже $90, доходность США ниже 4,7% и TSMC выше 2330-2350.",
        ]),
    ],
})

CONCISE_SECTIONS.update({
    "zh-cn": [
        ("核心结论", [
            "亚洲 AI 与半导体资产发生区域性去杠杆。韩国 KOSPI 收跌约 7.4%，Samsung 与 SK 海力士分别跌约 9.2%和 10%；台湾指数跌约 4.65%，日经盘中也一度跌约 4%。这已超出单一个股调整。",
            "油价和收益率回落仍未救起芯片股。Brent 结算跌至 85.87 美元、10 年期美债收益率降至约 4.65%，半导体却继续下跌，说明抛售核心已从宏观通胀转向估值、竞争、杠杆和 AI 资本回报。",
        ]),
        ("CXMT 是触发因素，不是全部解释", [
            "CXMT 上市融资与中国半导体进展提高了通用 DRAM 的长期竞争折价，但不能直接推导其已追平 HBM、先进封装、良率和国际客户认证。韩国极端跌幅还受到指数集中、融资交易和程序卖出的放大。",
            "台积电收跌约 2.98%，明显小于台湾指数约 4.65%的跌幅。CXMT 对先进逻辑制程与代工生态的直接冲击有限；今天更像系统性流动性去杠杆，而非台积电基本面同步崩塌。",
            "TraderXYZ 前十名义成交约 44.74 亿美元，较昨日增加约 202%，存储、指数与韩国相关资产同步下跌，方向可信度显著提高；具体跌幅仍可能被永续杠杆和清算放大。",
        ]),
        ("风险控制与验证条件", [
            "短线先观察台积电今日低点 2270 与台湾外资流向。只有重新站上 2350-2400，KOSPI 停止触发交易限制、TraderXYZ 成交回落且跌幅收窄，恐慌才更接近稳定。",
            "今晚用美国正股、SOXX / SMH、费城半导体指数与期权成交确认亚洲信号。若美股没有同步放量下跌，亚洲存在过度反应；若同步放量，风险可能延续至 Fed 与财报日。",
            "Microsoft 与 Meta 必须证明 AI 收入增速可以覆盖资本开支。美联储基准情景仍是鹰派暂停，但若意外加息或后续 PCE 偏高，高估值科技仍有第二轮压力。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "亞洲 AI 與半導體資產發生區域性去槓桿。韓國 KOSPI 收跌約 7.4%，Samsung 與 SK 海力士分別跌約 9.2%和 10%；台灣指數跌約 4.65%，日經盤中也一度跌約 4%。這已超出單一個股調整。",
            "油價和殖利率回落仍未救起晶片股。Brent 結算跌至 85.87 美元、10 年期美債殖利率降至約 4.65%，半導體卻繼續下跌，說明拋售核心已從宏觀通膨轉向估值、競爭、槓桿和 AI 資本回報。",
        ]),
        ("CXMT 是觸發因素，不是全部解釋", [
            "CXMT 上市融資與中國半導體進展提高了通用 DRAM 的長期競爭折價，但不能直接推導其已追平 HBM、先進封裝、良率和國際客戶認證。韓國極端跌幅還受到指數集中、融資交易和程式賣出的放大。",
            "台積電收跌約 2.98%，明顯小於台灣指數約 4.65%的跌幅。CXMT 對先進邏輯製程與代工生態的直接衝擊有限；今天更像系統性流動性去槓桿，而非台積電基本面同步崩塌。",
            "TraderXYZ 前十名義成交約 44.74 億美元，較昨日增加約 202%，記憶體、指數與韓國相關資產同步下跌，方向可信度顯著提高；具體跌幅仍可能被永續槓桿和清算放大。",
        ]),
        ("風險控制與驗證條件", [
            "短線先觀察台積電今日低點 2270 與台灣外資流向。只有重新站上 2350-2400，KOSPI 停止觸發交易限制、TraderXYZ 成交回落且跌幅收窄，恐慌才更接近穩定。",
            "今晚以美國現貨、SOXX / SMH、費城半導體指數與期權成交確認亞洲訊號。若美股沒有同步放量下跌，亞洲存在過度反應；若同步放量，風險可能延續至 Fed 與財報日。",
            "Microsoft 與 Meta 必須證明 AI 收入增速可以覆蓋資本開支。聯準會基準情景仍是鷹派暫停，但若意外升息或後續 PCE 偏高，高估值科技仍有第二輪壓力。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "Asian AI and semiconductor assets enter a regional de-leveraging event. Korea's KOSPI falls about 7.4%, Samsung roughly 9.2% and SK Hynix 10%; Taiwan drops about 4.65% and Japan loses roughly 4% intraday. This is broader than a single-stock correction.",
            "Lower oil and yields fail to rescue chip shares. Brent settles near $85.87 and the U.S. 10-year eases to about 4.65%, yet semiconductors keep falling, moving the selloff from macro inflation toward valuation, competition, leverage and AI capital returns.",
        ]),
        ("CXMT Is a Trigger, Not the Whole Explanation", [
            "CXMT's listing and China's semiconductor progress increase the long-term discount on commodity DRAM, but do not establish parity in HBM, advanced packaging, yield or international qualification. Korea's extreme move also reflects index concentration, margin trading and program selling.",
            "TSMC closes down about 2.98%, materially less than Taiwan's 4.65% decline. CXMT has limited direct impact on advanced logic and the foundry ecosystem; today's move looks more like systemic liquidity de-leveraging than a matching collapse in TSMC fundamentals.",
            "TraderXYZ top-ten notional volume reaches about $4.474 billion, up roughly 202% from yesterday. Memory, indices and Korea-linked assets fall together, making direction more credible, while perpetual leverage and liquidations still exaggerate magnitude.",
        ]),
        ("Risk Control and Confirmation", [
            "Watch TSMC's 2270 low and Taiwan foreign flows first. Stabilization needs TSMC back above 2350-2400, KOSPI no longer triggering trading limits, and TraderXYZ volume and losses narrowing together.",
            "Use U.S. cash shares, SOXX / SMH, the Philadelphia Semiconductor Index and options volume tonight. A lack of matching U.S. volume would imply Asian overreaction; synchronized heavy selling would extend risk into the Fed and earnings dates.",
            "Microsoft and Meta must show AI revenue growth can cover capex. The Fed baseline remains a hawkish hold, but a surprise hike or firm PCE would create a second valuation shock for expensive technology.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "AI и полупроводники Азии входят в региональное снижение плеча. KOSPI падает примерно на 7,4%, Samsung на 9,2%, SK Hynix на 10%; Тайвань теряет 4,65%, Япония внутри дня около 4%. Это шире коррекции одной акции.",
            "Снижение нефти и доходностей не спасает чипы. Brent закрывается около $85,87, доходность США снижается к 4,65%, но полупроводники продолжают падать: фокус сместился с инфляции к оценке, конкуренции, плечу и отдаче AI-капитала.",
        ]),
        ("CXMT — Триггер, но не Полное Объяснение", [
            "Листинг CXMT и прогресс Китая повышают долгосрочный дисконт обычной DRAM, но не доказывают равенство в HBM, упаковке, выходе годных и международной сертификации. Экстремум Кореи усилили концентрация индекса, маржинальные позиции и программные продажи.",
            "TSMC закрывается на 2,98% ниже, заметно лучше падения Тайваня на 4,65%. CXMT мало влияет напрямую на передовую логику и экосистему фабрик; движение больше похоже на системное снижение ликвидности, чем на обвал фундаментала TSMC.",
            "Оборот первой десятки TraderXYZ достигает $4,474 млрд, на 202% выше вчерашнего. Память, индексы и корейские активы падают вместе, поэтому направление надежнее, но плечо и ликвидации преувеличивают масштаб.",
        ]),
        ("Контроль Риска и Подтверждение", [
            "Сначала следите за минимумом TSMC 2270 и иностранными потоками Тайваня. Для стабилизации нужны возврат выше 2350-2400, прекращение торговых ограничений KOSPI и одновременное снижение оборота и потерь TraderXYZ.",
            "Сегодня США должны подтвердить сигнал через акции, SOXX / SMH, индекс Филадельфии и опционы. Без синхронного объема Азия могла переоценить риск; тяжелые продажи продлят давление до ФРС и отчетов.",
            "Microsoft и Meta должны показать, что рост AI-выручки покрывает капзатраты. Базовый сценарий ФРС — жесткая пауза, но неожиданное повышение или сильный PCE создадут второй удар по оценкам технологий.",
        ]),
    ],
})

CONCISE_SECTIONS.update({
    "zh-cn": [
        ("核心结论", [
            "亚洲 AI 硬件进入第二阶段去杠杆。KOSPI 在前一日暴跌后午间再跌约 8.2%，台湾指数跌约 4.9%；这已从情绪冲击升级为盈利预期、估值与杠杆同步收缩。",
            "SK 海力士收入和营业利润均创新高，但利润仍低于极高共识约 5.4%。AI 需求没有消失，真正变化是强增长已不足以支撑此前的极端估值。",
        ]),
        ("先进代工与存储需要分开判断", [
            "台积电约跌 4.2%，小于韩国两大存储厂，但尚未形成真正相对强势。CXMT 扩产首先影响通用 DRAM 与成熟制程，台积电在先进逻辑、CoWoS 和客户验证上的护城河更深。",
            "TraderXYZ 前十名义成交约 60.28 亿美元，韩国、MU、SNDK 与亚洲现货方向一致，边际情绪可信；永续价格仍会被杠杆、清算和跨时段流动性放大，不能替代主市场定价。",
            "两日极端下跌更像高估值、指数集中、杠杆 ETF 与预期下修共同触发的流动性事件，而不是 CXMT 单一消息或 AI 终端需求突然归零。",
        ]),
        ("今晚的验证节点", [
            "美联储主流预期维持 3.50%-3.75%，但油价反弹保留收紧尾部风险。Microsoft 与 Meta 的关键不只是资本开支，而是 Azure、广告效率、利润率与自由现金流能否证明 AI 投入正在产生回报。",
            "反转需要韩国停止流动性踩踏、MU / SNDK / SOXX 放量止跌、台积电守住 2185 并重新站回 2280。若油价再上 90 美元，或云厂上调资本开支却下调现金流，估值压力可能延续。",
        ]),
    ],
    "zh-hant": [
        ("核心結論", [
            "亞洲 AI 硬體進入第二階段去槓桿。KOSPI 在前一日暴跌後午間再跌約 8.2%，台灣指數跌約 4.9%；這已從情緒衝擊升級為盈利預期、估值與槓桿同步收縮。",
            "SK 海力士收入和營業利潤均創新高，但利潤仍低於極高共識約 5.4%。AI 需求沒有消失，真正變化是強增長已不足以支撐此前的極端估值。",
        ]),
        ("先進代工與記憶體需要分開判斷", [
            "台積電約跌 4.2%，小於韓國兩大記憶體廠，但尚未形成真正相對強勢。CXMT 擴產首先影響通用 DRAM 與成熟製程，台積電在先進邏輯、CoWoS 和客戶驗證上的護城河更深。",
            "TraderXYZ 前十名義成交約 60.28 億美元，韓國、MU、SNDK 與亞洲現貨方向一致，邊際情緒可信；永續價格仍會被槓桿、清算和跨時段流動性放大，不能替代主市場定價。",
            "兩日極端下跌更像高估值、指數集中、槓桿 ETF 與預期下修共同觸發的流動性事件，而不是 CXMT 單一消息或 AI 終端需求突然歸零。",
        ]),
        ("今晚的驗證節點", [
            "聯準會主流預期維持 3.50%-3.75%，但油價反彈保留收緊尾部風險。Microsoft 與 Meta 的關鍵不只是資本開支，而是 Azure、廣告效率、利潤率與自由現金流能否證明 AI 投入正在產生回報。",
            "反轉需要韓國停止流動性踩踏、MU / SNDK / SOXX 放量止跌、台積電守住 2185 並重新站回 2280。若油價再上 90 美元，或雲端業者上調資本開支卻下調現金流，估值壓力可能延續。",
        ]),
    ],
    "en": [
        ("Core Takeaway", [
            "Asian AI hardware enters a second de-leveraging phase. After the prior session's collapse, KOSPI loses another 8.2% around midday and Taiwan falls about 4.9%, turning an emotional shock into a simultaneous contraction in earnings expectations, valuation and leverage.",
            "SK Hynix posts record revenue and operating profit, yet profit misses an exceptionally high consensus by roughly 5.4%. AI demand has not disappeared; the change is that strong growth no longer supports the previous extreme valuation.",
        ]),
        ("Separate Advanced Foundry From Memory", [
            "TSMC falls about 4.2%, less than Korea's major memory makers but not yet true relative strength. CXMT capacity is most relevant to commodity DRAM and mature nodes, while TSMC retains deeper advantages in advanced logic, CoWoS and customer qualification.",
            "TraderXYZ top-ten notional reaches about $6.028 billion. Korea, MU, SNDK and Asian cash markets agree on direction, improving the sentiment signal; leverage, liquidations and cross-session liquidity still exaggerate perpetual prices.",
            "The two-day decline looks like a liquidity event driven by high valuation, index concentration, leveraged ETFs and estimate cuts, not a single CXMT headline or a sudden disappearance of end demand for AI.",
        ]),
        ("Tonight's Confirmation", [
            "Consensus expects the Fed to hold at 3.50%-3.75%, while rebounding oil preserves a tightening tail risk. For Microsoft and Meta, the test is whether Azure, advertising efficiency, margins and free cash flow can prove AI capex is producing returns.",
            "A turn requires Korean liquidity to stabilize, MU / SNDK / SOXX to stop falling on volume, and TSMC to hold 2185 before reclaiming 2280. Oil above $90 or higher cloud capex paired with weaker cash flow would extend valuation pressure.",
        ]),
    ],
    "ru": [
        ("Главный Вывод", [
            "AI-оборудование Азии входит во вторую фазу снижения плеча. После вчерашнего обвала KOSPI теряет еще около 8,2%, Тайвань около 4,9%: эмоциональный шок превращается в одновременное сжатие ожиданий прибыли, оценок и плеча.",
            "SK Hynix показывает рекордные выручку и операционную прибыль, но прибыль примерно на 5,4% ниже крайне высокого консенсуса. Спрос на AI не исчез; сильного роста теперь недостаточно для прежних экстремальных оценок.",
        ]),
        ("Передовые Фабрики и Память Нельзя Смешивать", [
            "TSMC падает примерно на 4,2%, меньше крупных производителей памяти Кореи, но это еще не настоящая относительная сила. CXMT прежде всего влияет на обычную DRAM и зрелые узлы; преимущества TSMC глубже в передовой логике, CoWoS и сертификации клиентов.",
            "Оборот первой десятки TraderXYZ достигает около $6,028 млрд. Корея, MU, SNDK и азиатский спот подтверждают направление, но плечо, ликвидации и межсессионная ликвидность по-прежнему преувеличивают цены перпетуалов.",
            "Двухдневное падение больше похоже на событие ликвидности из-за высоких оценок, концентрации индексов, ETF с плечом и снижения прогнозов, а не на одну новость CXMT или исчезновение спроса на AI.",
        ]),
        ("Проверка Сегодня Вечером", [
            "Консенсус ждет ставку ФРС 3,50%-3,75% без изменений, но рост нефти сохраняет риск ужесточения. Microsoft и Meta должны показать, что Azure, эффективность рекламы, маржа и денежный поток подтверждают отдачу AI-капзатрат.",
            "Для разворота нужны стабилизация Кореи, остановка MU / SNDK / SOXX на объеме и удержание TSMC 2185 с возвратом к 2280. Нефть выше $90 или рост капзатрат при слабом потоке продлят давление на оценки.",
        ]),
    ],
})

SOURCE_URLS = [
    ("ap-asia-0729", "https://apnews.com/article/b8bfaf782877957bbaa7196b70a4d725"),
    ("ap-us-0728", "https://apnews.com/article/wall-street-stocks-dow-nasdaq-d2a114bce818cab6ee9583f4815cb89a"),
    ("skhynix-q2", "https://news.skhynix.com/en/q2-2026-business-results/"),
    ("skhynix-sec", "https://www.sec.gov/Archives/edgar/data/2120882/000119312526303983/d19380d6k.htm"),
    ("reuters-asia-0729", "https://au.investing.com/news/stock-market-news/samsung-sk-hynix-slide-amid-nvidia-financing-worries-china-competition-4555278"),
    ("reuters-fed-0729", "https://www.investing.com/news/economy-news/growing-number-of-brokerages-see-july-fed-decision-as-a-close-call-4813379"),
    ("morgan-stanley", "https://www.morganstanley.com/insights/articles/market-risks-portfolio-positioning-July-2026"),
    ("msft-date", "https://news.microsoft.com/source/2026/07/08/microsoft-announces-quarterly-earnings-release-date-68/"),
    ("meta-q2", "https://investor.atmeta.com/investor-events/event-details/2026/Q2-2026-Earnings-Call/default.aspx"),
    ("hyperliquid-api", "https://api.hyperliquid.xyz/info"),
    ("twse", "https://mis.twse.com.tw/stock/index.jsp"),
]

SOURCE_LABELS = {
    "zh-cn": {
        "bls-cpi": "美国劳工统计局：2026 年 6 月 CPI",
        "bls-ppi": "美国劳工统计局：2026 年 6 月 PPI",
        "tsmc-q2": "TSMC 2026 年第二季度业绩",
        "ap-asia-0729": "AP：7 月 29 日亚洲芯片与韩国市场",
        "ap-us-0728": "AP：7 月 28 日美股收盘",
        "skhynix-q2": "SK 海力士：2026 年第二季度业绩",
        "skhynix-sec": "SEC：SK 海力士第二季度公告",
        "reuters-asia-0729": "Reuters：亚洲芯片抛售与中国竞争",
        "reuters-fed-0729": "Reuters：7 月 Fed 决议预期",
        "morgan-stanley": "Morgan Stanley：市场风险与仓位建议",
        "meta-q2": "Meta：2026 年第二季度电话会",
        "ap-us-0727": "AP：7 月 27 日美股、油价与美债",
        "reuters-us-0727": "Reuters：7 月 27 日美股、芯片指数与 Fed 定价",
        "ap-asia-0728": "AP：7 月 28 日韩国、台湾与亚洲市场",
        "reuters-korea": "Reuters：KOSPI、SK 海力士、Samsung 与 CXMT",
        "ap-cxmt": "AP：CXMT 上市",
        "goldman-outlook": "Goldman Sachs：美国年中宏观与 Fed 展望",
        "apollo-week": "Apollo：本周市场波动风险",
        "msft-ir": "Microsoft 投资者关系",
        "ap-market-0724": "AP：7 月 24 日美股、原油与美债市场",
        "reuters-asia-0727": "Reuters：7 月 27 日亚洲市场、油价与央行预期",
        "reuters-week": "Reuters：本周美联储与科技财报风险",
        "reuters-bonds": "Reuters：全球债券收益率、关税与原油",
        "intel-q2": "Intel 2026 年第二季度财报摘要",
        "reuters-intel": "Reuters：Intel 财报与 14A 投资",
        "reuters-cxmt": "Reuters：CXMT 上市与 IPO 数据",
        "sse-cxmt": "上海证券交易所：CXMT IPO 信息",
        "sp-msft-meta": "S&P Global：Microsoft 与 Meta 财报前瞻",
        "msft-date": "Microsoft：季度财报发布日期",
        "sp-credit": "S&P Global Ratings：大型云厂资本开支与信用风险",
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
        "ap-asia-0729": "AP：7 月 29 日亞洲晶片與韓國市場",
        "ap-us-0728": "AP：7 月 28 日美股收盤",
        "skhynix-q2": "SK 海力士：2026 年第二季度業績",
        "skhynix-sec": "SEC：SK 海力士第二季度公告",
        "reuters-asia-0729": "Reuters：亞洲晶片拋售與中國競爭",
        "reuters-fed-0729": "Reuters：7 月 Fed 決議預期",
        "morgan-stanley": "Morgan Stanley：市場風險與部位建議",
        "meta-q2": "Meta：2026 年第二季度電話會",
        "ap-us-0727": "AP：7 月 27 日美股、油價與美債",
        "reuters-us-0727": "Reuters：7 月 27 日美股、晶片指數與 Fed 定價",
        "ap-asia-0728": "AP：7 月 28 日韓國、台灣與亞洲市場",
        "reuters-korea": "Reuters：KOSPI、SK 海力士、Samsung 與 CXMT",
        "ap-cxmt": "AP：CXMT 上市",
        "goldman-outlook": "Goldman Sachs：美國年中宏觀與 Fed 展望",
        "apollo-week": "Apollo：本週市場波動風險",
        "msft-ir": "Microsoft 投資者關係",
        "ap-market-0724": "AP：7 月 24 日美股、原油與美債市場",
        "reuters-asia-0727": "Reuters：7 月 27 日亞洲市場、油價與央行預期",
        "reuters-week": "Reuters：本週聯準會與科技財報風險",
        "reuters-bonds": "Reuters：全球債券殖利率、關稅與原油",
        "intel-q2": "Intel 2026 年第二季度財報摘要",
        "reuters-intel": "Reuters：Intel 財報與 14A 投資",
        "reuters-cxmt": "Reuters：CXMT 上市與 IPO 數據",
        "sse-cxmt": "上海證券交易所：CXMT IPO 資訊",
        "sp-msft-meta": "S&P Global：Microsoft 與 Meta 財報前瞻",
        "msft-date": "Microsoft：季度財報發布日期",
        "sp-credit": "S&P Global Ratings：大型雲端業者資本開支與信用風險",
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
        "ap-asia-0729": "AP: July 29 Asian chips and Korean markets",
        "ap-us-0728": "AP: July 28 U.S. market close",
        "skhynix-q2": "SK Hynix: Q2 2026 business results",
        "skhynix-sec": "SEC: SK Hynix second-quarter filing",
        "reuters-asia-0729": "Reuters: Asian chip selloff and China competition",
        "reuters-fed-0729": "Reuters: expectations for the July Fed decision",
        "morgan-stanley": "Morgan Stanley: market risks and positioning",
        "meta-q2": "Meta: Q2 2026 earnings call",
        "ap-us-0727": "AP: July 27 U.S. stocks, oil and Treasuries",
        "reuters-us-0727": "Reuters: July 27 U.S. stocks, chips and Fed pricing",
        "ap-asia-0728": "AP: July 28 Korea, Taiwan and Asian markets",
        "reuters-korea": "Reuters: KOSPI, SK Hynix, Samsung and CXMT",
        "ap-cxmt": "AP: CXMT listing",
        "goldman-outlook": "Goldman Sachs: U.S. midyear macro and Fed outlook",
        "apollo-week": "Apollo: this week's market-volatility risks",
        "msft-ir": "Microsoft investor relations",
        "ap-market-0724": "AP: July 24 stocks, oil and Treasury markets",
        "reuters-asia-0727": "Reuters: July 27 Asia, oil and central-bank outlook",
        "reuters-week": "Reuters: Fed decision and technology earnings risks",
        "reuters-bonds": "Reuters: global yields, tariffs and oil",
        "intel-q2": "Intel Q2 2026 earnings summary",
        "reuters-intel": "Reuters: Intel earnings and 14A investment",
        "reuters-cxmt": "Reuters: CXMT listing and IPO data",
        "sse-cxmt": "Shanghai Stock Exchange: CXMT IPO information",
        "sp-msft-meta": "S&P Global: Microsoft and Meta earnings previews",
        "msft-date": "Microsoft: quarterly earnings release date",
        "sp-credit": "S&P Global Ratings: hyperscaler capex and credit risk",
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
        "ap-asia-0729": "AP: чипы Азии и рынок Кореи 29 июля",
        "ap-us-0728": "AP: закрытие рынка США 28 июля",
        "skhynix-q2": "SK Hynix: результаты второго квартала 2026",
        "skhynix-sec": "SEC: квартальный отчет SK Hynix",
        "reuters-asia-0729": "Reuters: распродажа чипов Азии и конкуренция Китая",
        "reuters-fed-0729": "Reuters: ожидания решения ФРС в июле",
        "morgan-stanley": "Morgan Stanley: риски рынка и позиции",
        "meta-q2": "Meta: отчетная конференция за второй квартал 2026",
        "ap-us-0727": "AP: акции США, нефть и облигации 27 июля",
        "reuters-us-0727": "Reuters: акции США, чипы и ожидания ФРС 27 июля",
        "ap-asia-0728": "AP: Корея, Тайвань и рынки Азии 28 июля",
        "reuters-korea": "Reuters: KOSPI, SK Hynix, Samsung и CXMT",
        "ap-cxmt": "AP: листинг CXMT",
        "goldman-outlook": "Goldman Sachs: прогноз США и ФРС на середину года",
        "apollo-week": "Apollo: риски волатильности этой недели",
        "msft-ir": "Microsoft: информация для инвесторов",
        "ap-market-0724": "AP: акции, нефть и облигации США 24 июля",
        "reuters-asia-0727": "Reuters: Азия, нефть и ожидания центробанков 27 июля",
        "reuters-week": "Reuters: решение ФРС и риски отчетов технологий",
        "reuters-bonds": "Reuters: мировые доходности, тарифы и нефть",
        "intel-q2": "Intel: итоги второго квартала 2026",
        "reuters-intel": "Reuters: отчет Intel и инвестиции в 14A",
        "reuters-cxmt": "Reuters: листинг CXMT и данные IPO",
        "sse-cxmt": "Шанхайская биржа: информация об IPO CXMT",
        "sp-msft-meta": "S&P Global: прогноз отчетов Microsoft и Meta",
        "msft-date": "Microsoft: дата публикации квартального отчета",
        "sp-credit": "S&P Global Ratings: капзатраты облаков и кредитный риск",
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
        "zh-cn": ("2185 支撑 / 2280 修复", "美国现货与期权止跌确认", "Fed 决议与油价反弹", "韩国踩踏与 SOXX 验证", "AI 收入能否覆盖资本开支"),
        "zh-hant": ("2185 支撐 / 2280 修復", "美國現貨與期權止跌確認", "Fed 決議與油價反彈", "韓國踩踏與 SOXX 驗證", "AI 收入能否覆蓋資本開支"),
        "en": ("2185 support / 2280 repair", "U.S. cash and options stabilization", "Fed decision and oil rebound", "Korean stress vs SOXX confirmation", "whether AI revenue covers capex"),
        "ru": ("поддержка 2185 / возврат 2280", "стабилизация акций и опционов США", "решение ФРС и рост нефти", "стресс Кореи и проверка SOXX", "покрывает ли AI-выручка капзатраты"),
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
              <div class="brief-item"><strong>MSFT / META / AMZN / AAPL</strong><span>{watch_labels[4]}</span></div>
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
        "zh-cn": ("亚洲半导体全面去杠杆，台积电相对抗跌", "上一篇市场日报。", "归档"),
        "zh-hant": ("亞洲半導體全面去槓桿，台積電相對抗跌", "上一篇市場日報。", "歸檔"),
        "en": ("Asian semiconductors de-leverage as TSMC shows relative resilience", "Previous market brief.", "Archive"),
        "ru": ("Полупроводники Азии снижают плечо, TSMC устойчивее рынка", "Предыдущий обзор рынка.", "Архив"),
    }[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-07-28")}"><span class="history-date">2026-07-28</span><span><span class="history-title">{html.escape(previous[0])}</span><span class="history-summary">{html.escape(previous[1])}</span></span><span class="history-tag">{html.escape(previous[2])}</span></a>
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
