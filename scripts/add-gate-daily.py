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

DATE = "2026-07-20"
SOURCE = ROOT / "content" / "daily" / DATE / "zh-cn.txt"
IMAGES = {
    "zh-cn": "/daily/images/market-brief-2026-07-20-zh-cn.svg",
    "zh-hant": "/daily/images/market-brief-2026-07-20-zh-hant.svg",
    "en": "/daily/images/market-brief-2026-07-20-en.svg",
    "ru": "/daily/images/market-brief-2026-07-20-ru.svg",
}

META = {
    "zh-cn": {
        "title": "台股超跌修复，AI 交易转向云资本开支与能源验证",
        "desc": "2026-07-20 GateAffiliate 每日市场日报：台积电反弹但台股尚未确认反转，AI 基本面仍强，周末永续成交偏低，油价与云厂商资本开支成为本周关键。",
        "eyebrow": f"全球市场日报 · {DATE}",
        "h1": "台股超跌修复，AI 交易转向云资本开支与能源验证。",
        "summary": "台积电反弹约 2%，但大规模换手后的趋势反转尚未确认。AI 需求仍强，市场本周将用云资本开支、现金回报与高油价重新检验估值。",
        "tag": "最新",
    },
    "zh-hant": {
        "title": "台股超跌修復，AI 交易轉向雲端資本開支與能源驗證",
        "desc": "2026-07-20 GateAffiliate 每日市場日報：台積電反彈但台股尚未確認反轉，AI 基本面仍強，週末永續成交偏低，油價與雲端資本開支成為本週關鍵。",
        "eyebrow": f"全球市場日報 · {DATE}",
        "h1": "台股超跌修復，AI 交易轉向雲端資本開支與能源驗證。",
        "summary": "台積電反彈約 2%，但大規模換手後的趨勢反轉尚未確認。AI 需求仍強，市場本週將以雲端資本開支、現金回報與高油價重新檢驗估值。",
        "tag": "最新",
    },
    "en": {
        "title": "Taiwan steadies as AI trades face cloud-capex and energy tests",
        "desc": "GateAffiliate's 2026-07-20 market brief: TSMC rebounds but Taiwan has not confirmed a reversal; AI fundamentals remain firm while thin weekend perpetual volume, oil and cloud capex shape the week.",
        "eyebrow": f"Global market brief · {DATE}",
        "h1": "Taiwan steadies as AI trades face cloud-capex and energy tests.",
        "summary": "TSMC rebounds about 2%, but heavy turnover leaves the trend reversal unconfirmed. Strong AI demand now faces a weekly test from cloud capex, cash returns and elevated oil prices.",
        "tag": "Latest",
    },
    "ru": {
        "title": "Тайвань стабилизируется: AI проверят облачные капзатраты и нефть",
        "desc": "Обзор GateAffiliate за 2026-07-20: TSMC отскакивает, но разворот Тайваня не подтвержден; фундамент AI силен, а низкий объем выходных, нефть и облачные капзатраты определяют неделю.",
        "eyebrow": f"Глобальный обзор · {DATE}",
        "h1": "Тайвань стабилизируется: AI проверят облачные капзатраты и нефть.",
        "summary": "TSMC отскакивает примерно на 2%, но разворот после крупного оборота еще не подтвержден. Сильный AI-спрос теперь проверят облачные капзатраты, денежная отдача и дорогая нефть.",
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

SOURCE_URLS = [
    ("tsmc-q2", "https://investor.tsmc.com/english/quarterly-results/2026/q2"),
    ("twse", "https://mis.twse.com.tw/stock/index.jsp"),
    ("taipei-times", "https://www.taipeitimes.com/News/front/archives/2026/07/18/2003860942"),
    ("ap-global", "https://apnews.com/article/65449e9565fba441a617f9517e097f5a"),
    ("reuters-global", "https://www.investing.com/news/economy-news/asian-shares-slump-on-chipmaker-drag-bonds-cheer-cooler-inflation-4794608"),
    ("ubs-volatility", "https://www.ubs.com/global/en/wealthmanagement/insights/chief-investment-office/house-view/daily/2026/latest-06072026.html"),
    ("week-ahead", "https://au.marketscreener.com/news/week-ahead-for-fx-bonds-u-s-european-pmi-data-ecb-decision-in-focus-ce7f51dade8dff20"),
    ("dbs-week", "https://www.dbs.com.tw/personal/aics/templatedata/article/generic/data/en/GR/072026/260717_insights_week_ahead.xml"),
    ("imf-weo", "https://www.imf.org/-/media/files/publications/weo/2026/update/july/english/text.pdf"),
    ("hyperliquid-api", "https://api.hyperliquid.xyz/info"),
    ("hyperliquid-docs", "https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals"),
    ("man-group", "https://www.man.com/insights/views-from-the-floor-2026-14-july"),
]

SOURCE_LABELS = {
    "zh-cn": {
        "bls-cpi": "美国劳工统计局：2026 年 6 月 CPI",
        "bls-ppi": "美国劳工统计局：2026 年 6 月 PPI",
        "tsmc-q2": "TSMC 2026 年第二季度业绩",
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
        "zh-cn": ("2300 / 缩量企稳", "美股正股与 ETF 验证", "Brent 90 美元关口", "42000-43000 区间承接", "云资本开支与现金回报"),
        "zh-hant": ("2300 / 縮量企穩", "美股現貨與 ETF 驗證", "Brent 90 美元關口", "42000-43000 區間承接", "雲端資本開支與現金回報"),
        "en": ("2300 / lower-volume stabilization", "U.S. cash and ETF validation", "Brent near $90", "support across 42000-43000", "cloud capex and cash returns"),
        "ru": ("2300 / стабилизация на меньшем объеме", "проверка спотом США и ETF", "Brent у $90", "поддержка 42000-43000", "облачные капзатраты и денежная отдача"),
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
        "zh-cn": ("台积电强财报后下跌，AI 科技进入资本回报再定价", "上一篇市场日报。", "归档"),
        "zh-hant": ("台積電強財報後下跌，AI 科技進入資本回報再定價", "上一篇市場日報。", "歸檔"),
        "en": ("TSMC falls after a stellar report as AI tech reprices capital returns", "Previous market brief.", "Archive"),
        "ru": ("TSMC падает после сильного отчета: AI-сектор переоценивает отдачу капитала", "Предыдущий обзор рынка.", "Архив"),
    }[lang]
    return f'''<section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">
      <a class="history-link" href="{daily_slug(lang, DATE)}"><span class="history-date">{DATE}</span><span><span class="history-title">{html.escape(latest["title"])}</span><span class="history-summary">{html.escape(latest["summary"])}</span></span><span class="history-tag">{latest["tag"]}</span></a>
      <a class="history-link" href="{daily_slug(lang, "2026-07-17")}"><span class="history-date">2026-07-17</span><span><span class="history-title">{html.escape(previous[0])}</span><span class="history-summary">{html.escape(previous[1])}</span></span><span class="history-tag">{html.escape(previous[2])}</span></a>
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
