#!/usr/bin/env python3
from pathlib import Path
import html
import json
import re
import shutil

from opencc import OpenCC

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "hyperliquid-referral-site" / "market-briefing"
BASE_URL = "https://gateaffiliate.com"
CODE = "VLYQB1HXUW"
STYLE_VERSION = "20260630-gate-blue"
T2S = OpenCC("t2s")

DATES = sorted([p.name for p in SOURCE.iterdir() if p.is_dir() and re.match(r"2026-\d\d-\d\d$", p.name)])
LANGS = ("zh-cn", "zh-hant", "en", "ru")

LANG_META = {
    "zh-cn": {
        "html": "zh-CN",
        "label": "简体中文",
        "short": "简",
        "home": "/",
        "daily": "/daily/",
        "nav": ("邀请码", "注册步骤", "每日市场日报", "FAQ", "使用邀请码注册"),
        "footer": "GateAffiliate 市场内容仅供信息参考，不构成投资建议。",
        "daily_title": "GateAffiliate 每日市场日报 | BTC、ETH 与热门交易观察",
        "daily_desc": "GateAffiliate 每日市场日报目录，覆盖 BTC、ETH、AI 半导体、宏观、热门交易情绪与 Gate 用户关注的市场变化。",
        "daily_h1": "GateAffiliate 每日市场日报",
        "daily_copy": f"这里整理每日市场主线、宏观风险、热门资产与交易情绪，帮助 Gate 用户在注册和交易前快速了解市场背景。邀请码：{CODE}。",
        "history": "历史日报",
        "history_copy": "按日期查看历史市场观察，快速回顾不同交易日的主题、风险和关键数据。",
        "latest": "阅读最新日报",
    },
    "zh-hant": {
        "html": "zh-Hant",
        "label": "繁體中文",
        "short": "繁",
        "home": "/zh-hant/",
        "daily": "/zh-hant/daily/",
        "nav": ("邀請碼", "註冊步驟", "每日市場日報", "FAQ", "使用邀請碼註冊"),
        "footer": "GateAffiliate 市場內容僅供資訊參考，不構成投資建議。",
        "daily_title": "GateAffiliate 每日市場日報 | BTC、ETH 與熱門交易觀察",
        "daily_desc": "GateAffiliate 每日市場日報目錄，覆蓋 BTC、ETH、AI 半導體、宏觀、熱門交易情緒與 Gate 用戶關注的市場變化。",
        "daily_h1": "GateAffiliate 每日市場日報",
        "daily_copy": f"這裡整理每日市場主線、宏觀風險、熱門資產與交易情緒，幫助 Gate 用戶在註冊和交易前快速了解市場背景。邀請碼：{CODE}。",
        "history": "歷史日報",
        "history_copy": "按日期查看歷史市場觀察，快速回顧不同交易日的主題、風險和關鍵數據。",
        "latest": "閱讀最新日報",
    },
    "en": {
        "html": "en",
        "label": "English",
        "short": "EN",
        "home": "/en/",
        "daily": "/en/daily/",
        "nav": ("Invite Code", "How to Join", "Daily Briefs", "FAQ", "Join with Code"),
        "footer": "GateAffiliate market commentary is for information only and is not financial advice.",
        "daily_title": "GateAffiliate Daily Market Briefs | BTC, ETH and Market Updates",
        "daily_desc": "GateAffiliate daily market brief archive covering BTC, ETH, AI semiconductors, macro risk, trading sentiment, and market changes Gate users follow.",
        "daily_h1": "GateAffiliate Daily Market Briefs",
        "daily_copy": f"This archive keeps daily market themes, macro risk, hot assets, and trading sentiment in one place so Gate users can get context before registering or trading. Invite code: {CODE}.",
        "history": "Brief Archive",
        "history_copy": "Browse previous market briefs by date and review key themes, risks, and data points from each trading day.",
        "latest": "Read Latest Brief",
    },
    "ru": {
        "html": "ru",
        "label": "Русский",
        "short": "RU",
        "home": "/ru/",
        "daily": "/ru/daily/",
        "nav": ("Инвайт-код", "Регистрация", "Обзоры", "FAQ", "Регистрация с кодом"),
        "footer": "Материалы GateAffiliate предназначены только для информации и не являются инвестиционной рекомендацией.",
        "daily_title": "GateAffiliate Ежедневные обзоры рынка | BTC, ETH и рыночные обновления",
        "daily_desc": "Архив ежедневных обзоров GateAffiliate по BTC, ETH, AI-полупроводникам, макро-рискам, рыночным настроениям и важным изменениям рынка.",
        "daily_h1": "GateAffiliate Ежедневные обзоры рынка",
        "daily_copy": f"Здесь собраны ежедневные рыночные темы, макро-риски, популярные активы и торговые настроения, чтобы пользователи Gate могли получить контекст перед регистрацией или торговлей. Инвайт-код: {CODE}.",
        "history": "Архив обзоров",
        "history_copy": "Просматривайте предыдущие обзоры по датам и быстро возвращайтесь к ключевым темам, рискам и данным каждого торгового дня.",
        "latest": "Читать свежий обзор",
    },
}

HOME = {
    "zh-cn": {
        "title": "GateAffiliate 返佣邀请码 VLYQB1HXUW | Gate Affiliate Program",
        "desc": "GateAffiliate 返佣站：使用 Gate 邀请码 VLYQB1HXUW 注册，查看 Gate affiliate program、返佣规则说明、注册步骤和每日市场日报。",
        "eyebrow": f"GateAffiliate 邀请码：{CODE}",
        "h1": "使用 Gate affiliate 邀请码，开启更清晰的交易入口。",
        "copy": f"复制邀请码 {CODE}，通过 Gate 官方注册入口开通账户。这里整理注册步骤、返佣权益、账户安全和每日市场观察，帮助你更从容地开始使用 Gate。",
        "open": "打开 Gate 注册",
        "copy_code": "复制邀请码",
        "stats": [("VLYQB1HXUW", "注册时填写的邀请码"), ("Affiliate", "关注 Gate 返佣权益"), ("每日市场", "跟踪交易情绪与风险")],
        "bonus_h2": "注册前先复制 Gate affiliate 邀请码。",
        "bonus_p": f"如果 Gate 注册页没有自动带入邀请码，请手动填写 {CODE}。新用户奖励、返佣比例、任务券、affiliate 资格和活动门槛会随官方活动变化，实际权益请以 Gate 当前页面显示为准。",
        "steps_h2": "Gate affiliate 注册步骤",
        "steps_p": "保持流程简单，重点是确认官方域名、填写邀请码、完成账户安全设置。",
        "steps": [("打开官方注册页", "从本站按钮跳转到 Gate 官方页面，检查浏览器地址栏，确认不是仿冒网站。"), ("填写邀请码", "注册时输入或粘贴邀请码，提交前再确认一次。"), ("完成安全设置", "启用双重验证，设置资金密码，并只在自己理解风险的前提下使用现货、合约或理财功能。")],
        "seo_h2": "Gate 交易权益与账户指南",
        "seo_p": "在注册前了解邀请码、返佣资格、账户安全和市场信息，能帮助你更好地判断是否适合使用 Gate 的相关交易产品。",
        "latest_h2": "最新 GateAffiliate 市场日报",
        "latest_p": "每日市场日报覆盖 BTC、ETH、热门板块、宏观变量和交易情绪，方便你在交易前快速了解当天市场背景。",
        "faq_h2": "常见问题",
        "faq_p": "注册前建议先把这些细节确认好。",
        "faq": [("GateAffiliate 邀请码是多少？", f"邀请码是 {CODE}。如果注册链接没有自动带入，请手动复制填写。"), ("奖励和返佣一定能拿到吗？", "不承诺。不同地区、账户状态、活动周期、交易产品和 KYC 情况都可能影响资格，最终以 Gate 官方页面和账户内显示为准。"), ("注册后怎么确认邀请码和权益？", "完成注册后，可以到 Gate 账户内与邀请、奖励或 affiliate 相关的页面查看状态。如果页面没有显示，请以 Gate 账户内当前提示和官方规则为准。")],
    },
    "zh-hant": {},
    "en": {
        "title": "GateAffiliate Referral Code VLYQB1HXUW | Gate Affiliate Program",
        "desc": "GateAffiliate rebate site: use Gate invite code VLYQB1HXUW, review Gate affiliate program notes, joining steps, and daily market briefs.",
        "eyebrow": f"GateAffiliate invite code: {CODE}",
        "h1": "Use the Gate affiliate invite code and start with a clearer trading entry.",
        "copy": f"Copy invite code {CODE} and open a Gate account through the official registration path. This page keeps the signup flow, rebate notes, account security basics, and daily market context in one place.",
        "open": "Open Gate registration",
        "copy_code": "Copy invite code",
        "stats": [("VLYQB1HXUW", "Invite code to use at signup"), ("Affiliate", "Follow Gate rebate benefits"), ("Daily market", "Track sentiment and risk")],
        "bonus_h2": "Copy the Gate affiliate invite code before signup.",
        "bonus_p": f"If Gate does not auto-fill the invite code, enter {CODE} manually. New-user rewards, rebate rates, task coupons, affiliate eligibility, and campaign rules can change, so the current Gate page controls the final terms.",
        "steps_h2": "How to join with the Gate affiliate code",
        "steps_p": "Keep the flow simple: verify the official domain, enter the invite code, and secure the account.",
        "steps": [("Open the official registration page", "Use the button on this site and check the browser address bar before entering any account details."), ("Enter the invite code", "Paste the code during registration and confirm it before submitting."), ("Secure the account", "Enable two-factor authentication, set fund security controls, and only use trading products you understand.")],
        "seo_h2": "Gate trading benefits and account guide",
        "seo_p": "Before signing up, review the invite code, rebate eligibility, account security basics, and market information so you can decide whether Gate products fit your needs.",
        "latest_h2": "Latest GateAffiliate Market Brief",
        "latest_p": "Daily market briefs cover BTC, ETH, hot sectors, macro variables, and trading sentiment so you can get context before trading.",
        "faq_h2": "FAQ",
        "faq_p": "Check these points before registering.",
        "faq": [("What is the GateAffiliate invite code?", f"The invite code is {CODE}. If the signup page does not auto-fill it, copy and enter it manually."), ("Are rewards and rebates guaranteed?", "No. Region, account status, campaign dates, trading product, and KYC status may affect eligibility. Gate's current official page and account display are final."), ("How do I confirm the invite code after signup?", "After creating your account, check Gate's invite, rewards, or affiliate-related account pages. If the code or rewards do not appear, follow the current instructions shown inside your Gate account.")],
    },
    "ru": {
        "title": "GateAffiliate реферальный код VLYQB1HXUW | Gate Affiliate Program",
        "desc": "GateAffiliate сайт для rebate: используйте инвайт-код Gate VLYQB1HXUW, смотрите условия affiliate program, шаги регистрации и ежедневные обзоры рынка.",
        "eyebrow": f"GateAffiliate инвайт-код: {CODE}",
        "h1": "Используйте Gate affiliate инвайт-код и начните с понятного входа.",
        "copy": f"Скопируйте инвайт-код {CODE} и откройте аккаунт Gate через официальный путь регистрации. Здесь собраны шаги регистрации, заметки о rebate, базовая безопасность аккаунта и ежедневный рыночный контекст.",
        "open": "Открыть регистрацию Gate",
        "copy_code": "Скопировать код",
        "stats": [("VLYQB1HXUW", "Код для регистрации"), ("Affiliate", "Условия Gate rebate"), ("Ежедневный рынок", "Настроения и риски")],
        "bonus_h2": "Скопируйте Gate affiliate код перед регистрацией.",
        "bonus_p": f"Если Gate не подставит код автоматически, введите {CODE} вручную. Бонусы, rebate-условия, купоны, affiliate-право и условия кампаний могут меняться; финальные условия определяются текущей страницей Gate.",
        "steps_h2": "Как зарегистрироваться с Gate affiliate кодом",
        "steps_p": "Проверьте официальный домен, введите инвайт-код и настройте безопасность аккаунта.",
        "steps": [("Откройте официальную страницу", "Используйте кнопку на сайте и проверьте адрес в браузере перед вводом данных."), ("Введите инвайт-код", "Вставьте код при регистрации и проверьте его перед отправкой формы."), ("Защитите аккаунт", "Включите 2FA, настройте защиту средств и используйте только понятные вам торговые продукты.")],
        "seo_h2": "Преимущества Gate и краткий гид по аккаунту",
        "seo_p": "Перед регистрацией проверьте инвайт-код, условия rebate, базовую безопасность аккаунта и рыночную информацию, чтобы понять, подходят ли вам продукты Gate.",
        "latest_h2": "Свежий обзор GateAffiliate",
        "latest_p": "Ежедневные обзоры охватывают BTC, ETH, популярные сектора, макро-факторы и рыночные настроения, чтобы дать контекст перед торговлей.",
        "faq_h2": "FAQ",
        "faq_p": "Проверьте эти пункты перед регистрацией.",
        "faq": [("Какой инвайт-код GateAffiliate?", f"Инвайт-код: {CODE}. Если он не подставился автоматически, скопируйте и введите его вручную."), ("Гарантированы ли бонусы и rebate?", "Нет. Регион, статус аккаунта, даты кампании, торговый продукт и KYC могут влиять на eligibility. Финальными являются текущие условия Gate."), ("Как проверить инвайт-код после регистрации?", "После создания аккаунта проверьте разделы Gate, связанные с приглашениями, наградами или affiliate. Если код или бонусы не отображаются, следуйте актуальным подсказкам внутри аккаунта Gate.")],
    },
}
HOME["zh-hant"] = {
    k: (T2S.convert(v) if False else v)
    for k, v in HOME["zh-cn"].items()
}
HOME["zh-hant"].update({
    "title": "GateAffiliate 返佣邀請碼 VLYQB1HXUW | Gate Affiliate Program",
    "desc": "GateAffiliate 返佣站：使用 Gate 邀請碼 VLYQB1HXUW 註冊，查看 Gate affiliate program、返佣規則說明、註冊步驟和每日市場日報。",
    "eyebrow": f"GateAffiliate 邀請碼：{CODE}",
    "h1": "使用 Gate affiliate 邀請碼，開啟更清晰的交易入口。",
    "copy": f"複製邀請碼 {CODE}，透過 Gate 官方註冊入口開通帳戶。這裡整理註冊步驟、返佣權益、帳戶安全和每日市場觀察，幫助你更從容地開始使用 Gate。",
    "open": "打開 Gate 註冊",
    "copy_code": "複製邀請碼",
    "stats": [("VLYQB1HXUW", "註冊時填寫的邀請碼"), ("Affiliate", "關注 Gate 返佣權益"), ("每日市場", "追蹤交易情緒與風險")],
    "bonus_h2": "註冊前先複製 Gate affiliate 邀請碼。",
    "bonus_p": f"如果 Gate 註冊頁沒有自動帶入邀請碼，請手動填寫 {CODE}。新用戶獎勵、返佣比例、任務券、affiliate 資格和活動門檻會隨官方活動變化，實際權益請以 Gate 當前頁面顯示為準。",
    "steps_h2": "Gate affiliate 註冊步驟",
    "steps_p": "保持流程簡單，重點是確認官方域名、填寫邀請碼、完成帳戶安全設定。",
    "steps": [("打開官方註冊頁", "從本站按鈕跳轉到 Gate 官方頁面，檢查瀏覽器地址欄，確認不是仿冒網站。"), ("填寫邀請碼", "註冊時輸入或貼上邀請碼，提交前再確認一次。"), ("完成安全設定", "啟用雙重驗證，設定資金密碼，並只在自己理解風險的前提下使用現貨、合約或理財功能。")],
    "seo_h2": "Gate 交易權益與帳戶指南",
    "seo_p": "在註冊前了解邀請碼、返佣資格、帳戶安全和市場資訊，能幫助你更好地判斷是否適合使用 Gate 的相關交易產品。",
    "latest_h2": "最新 GateAffiliate 市場日報",
    "latest_p": "每日市場日報覆蓋 BTC、ETH、熱門板塊、宏觀變量和交易情緒，方便你在交易前快速了解當天市場背景。",
    "faq_h2": "常見問題",
    "faq_p": "註冊前建議先把這些細節確認好。",
    "faq": [("GateAffiliate 邀請碼是多少？", f"邀請碼是 {CODE}。如果註冊連結沒有自動帶入，請手動複製填寫。"), ("獎勵和返佣一定能拿到嗎？", "不承諾。不同地區、帳戶狀態、活動週期、交易產品和 KYC 情況都可能影響資格，最終以 Gate 官方頁面和帳戶內顯示為準。"), ("註冊後怎麼確認邀請碼和權益？", "完成註冊後，可到 Gate 帳戶內與邀請、獎勵或 affiliate 相關的頁面查看狀態。如果頁面沒有顯示，請以 Gate 帳戶內當前提示和官方規則為準。")],
})

RU_BRIEFS = {
    "2026-06-29": {
        "title": "AI-память остается главной аппаратной темой, но сделке нужно второе подтверждение.",
        "summary": "MU остается одним из главных потоков на TraderXYZ, TSM восстанавливается на Тайване, а высокий PCE ограничивает расширение оценок техсектора.",
        "suffix": "AI-память, MU, восстановление TSM и потоки TraderXYZ",
    },
    "2026-06-01": {
        "title": "AI-инфраструктура остается сильной, пока TSM подтверждается на Тайване.",
        "summary": "Тайваньский рынок подтверждает TSM, по MU важна защита прибыли, а HYPE поддерживает аппетит к риску.",
        "suffix": "Сила TSM на Тайване, правила по MU и HYPE",
    },
    "2026-05-30": {
        "title": "AI-полупроводники остаются в тренде, но победителям нужны более строгие правила.",
        "summary": "MU ведет HBM-направление, TSM и NVDA остывают, а HYPE остается сильным перед выходными.",
        "suffix": "MU, TSM, NVDA и ротация AI-полупроводников",
    },
    "2026-05-29": {
        "title": "AI-полупроводники сохраняют тренд, но главным становится расхождение на высоких уровнях.",
        "summary": "TSM и NVDA растут, MU торгуется с высокой волатильностью, а HYPE остается сильным.",
        "suffix": "TSM, MU, NVDA и риск-аппетит HYPE",
    },
    "2026-05-28": {
        "title": "AI-полупроводники не закончились, но рынок покупает уверенность, а не все подряд.",
        "summary": "TSM и MU лидируют, NVDA остывает, а слабость BTC и ETH показывает выборочный риск-аппетит.",
        "suffix": "TSM, MU, AI-полупроводники и риск BTC",
    },
    "2026-05-27": {
        "title": "AI-полупроводники подтверждаются, но лидерство шире, чем NVDA.",
        "summary": "TSM, MU, AMAT и азиатские цепочки поставок подтверждают расширение AI capex.",
        "suffix": "AI-полупроводники, TSM, MU и перпы",
    },
    "2026-05-26": {
        "title": "AI-полупроводники не сломались, рынок перешел к подтверждению на высоких уровнях.",
        "summary": "Тайвань откатывается от максимумов, Корея держится, а перпы продолжают закладывать премию AI.",
        "suffix": "Фандинг BTC, открытый интерес и AI-полупроводники",
    },
    "2026-05-25": {
        "title": "TSM ведет восстановление AI-полупроводников, пока рынок США закрыт.",
        "summary": "Тайваньский cash-рынок и перпы оценивают восстановление, но нужно подтверждение США.",
        "suffix": "TSM ведет восстановление AI",
    },
    "2026-05-23": {
        "title": "NVIDIA подтверждает спрос на AI, но дисциплина оценок важнее.",
        "summary": "Сильный прогноз, сдержанная реакция NVDA, устойчивые chip ETF и макро-ограничения.",
        "suffix": "NVIDIA, спрос на AI и дисциплина оценок",
    },
    "2026-05-22": {
        "title": "Высокий диапазон и структурные возможности: полупроводники расходятся, BTC нейтрален.",
        "summary": "Расхождение полупроводников, нейтральное плечо BTC, повышенные нефть и золото.",
        "suffix": "Диапазон рынка, BTC и структурные возможности",
    },
    "2026-05-21": {
        "title": "Восстановительный отскок сохраняется, но риск жесткой политики остается.",
        "summary": "Нефть и доходности остыли, а оценки AI остаются чувствительными к ставкам.",
        "suffix": "Восстановительный отскок и риск политики",
    },
}

RU_TEXT_REPLACEMENTS = [
    ("GateAffiliate daily market brief", "ежедневный обзор GateAffiliate"),
    ("GateAffiliate Daily Market Brief", "Ежедневный обзор GateAffiliate"),
    ("GateAffiliate daily market brief archive", "архив ежедневных обзоров GateAffiliate"),
    ("GateAffiliate invite code", "инвайт-код GateAffiliate"),
    ("GateAffiliate Invite Code", "Инвайт-код GateAffiliate"),
    ("Daily briefs", "Ежедневные обзоры"),
    ("Daily brief", "Ежедневный обзор"),
    ("Brief Archive", "Архив обзоров"),
    ("Archive", "Архив"),
    ("Latest", "Свежий"),
    ("Updated:", "Обновлено:"),
    ("Theme:", "Тема:"),
    ("Coverage:", "Охват:"),
    ("Read today's brief", "Читать сегодняшний обзор"),
    ("Read Latest Brief", "Читать свежий обзор"),
    ("Join Gate", "Регистрация Gate"),
    ("Use VLYQB1HXUW", f"Использовать {CODE}"),
    ("Copy code", "Скопировать код"),
    ("Copied", "Скопировано"),
    ("Gate affiliate program", "Программа Gate affiliate"),
    ("GateAffiliate Ежедневный обзор рынка", "Ежедневный обзор рынка GateAffiliate"),
    ("Global market brief", "Глобальный обзор рынка"),
    ("Global Market Brief", "Глобальный обзор рынка"),
    ("Top view", "Главный вывод"),
    ("Watchlist", "Список наблюдения"),
    ("Trader Watchlist", "Список наблюдения"),
    ("Framework", "Рамка действий"),
    ("Bottom line:", "Итог:"),
    ("Key Market Data", "Ключевые рыночные данные"),
    ("Sources:", "Источники:"),
    ("Data timestamps:", "Время данных:"),
    ("U.S. equities and AI semiconductors", "Акции США и AI-полупроводники"),
    ("Taiwan market and TSM", "Рынок Тайваня и TSM"),
    ("TraderXYZ / Hyperliquid top flows", "Крупнейшие потоки TraderXYZ / Hyperliquid"),
    ("Crypto risk context", "Криптовалютный риск-контекст"),
    ("Institutions and major messages", "Институциональный фон и ключевые сообщения"),
    ("Contrarian view", "Контрарный взгляд"),
    ("For a focused Hyperliquid ecosystem view, see the", "Для отдельного обзора экосистемы Hyperliquid смотрите"),
    ("HYPE market brief hub", "раздел рыночных обзоров"),
    ("for information only and is not financial advice", "предназначены только для информации и не являются инвестиционной рекомендацией"),
    ("AI memory remains the hardware theme, but the trade now needs second confirmation.", "AI-память остается главной аппаратной темой, но сделке теперь нужно второе подтверждение."),
    ("MU Memory Rotation, TSM Repair and TraderXYZ Flows", "Ротация MU в памяти, восстановление TSM и потоки TraderXYZ"),
    ("MU memory rotation, TSM Taiwan repair, TraderXYZ flows, DRAM and SNDK, PCE pressure, BTC/ETH and HYPE sentiment.", "Ротация MU в памяти, восстановление TSM на Тайване, потоки TraderXYZ, DRAM и SNDK, давление PCE, настроение BTC/ETH и HYPE."),
    ("MU memory rotation + TSM repair", "ротация MU в памяти + восстановление TSM"),
    ("MU earnings confirmed AI memory shortage, but the trade has moved from demand proof to durability confirmation. TSM is repairing in Taiwan, TraderXYZ still shows MU in top flows, and high PCE caps broad tech valuation expansion.", "Отчет MU подтвердил дефицит AI-памяти, но рынок перешел от доказательства спроса к проверке устойчивости. TSM восстанавливается на Тайване, TraderXYZ по-прежнему показывает MU среди главных потоков, а высокий PCE ограничивает расширение оценок техсектора."),
    ("MU earnings confirmed the AI memory bottleneck, but the market has moved from demand proof into sustainability proof. TSM is repairing in Taiwan, TraderXYZ still shows MU among top flows, and high PCE caps valuations.", "Отчет MU подтвердил узкое место в AI-памяти, но рынок перешел от доказательства спроса к проверке устойчивости. TSM восстанавливается на Тайване, TraderXYZ по-прежнему показывает MU среди главных потоков, а высокий PCE ограничивает оценки."),
    ("MU is still hot, but post-earnings trading is no longer a clean one-way chase.", "MU остается горячей темой, но после отчета это уже не чистая односторонняя погоня."),
    ("MU is still hot, but the post-earnings trade is no longer a clean one-way chase.", "MU остается горячей темой, но после отчета это уже не чистая односторонняя погоня."),
    ("AI memory remains valid as a medium-term theme. Short term, MU, DRAM and SNDK are in high-level turnover; TSM's Taiwan repair is constructive, but it still needs to reclaim 2400 TWD for confirmation.", "AI-память остается рабочей среднесрочной темой. Краткосрочно MU, DRAM и SNDK находятся в зоне высокой смены рук; восстановление TSM на Тайване конструктивно, но для подтверждения нужен возврат выше 2400 TWD."),
    ("AI memory remains valid as medium-term theme. Short term, MU, DRAM and SNDK are in high-level churn, while Taiwan TSM repair is constructive but still below NT$2400 confirmation.", "AI-память остается рабочей среднесрочной темой. Краткосрочно MU, DRAM и SNDK находятся в зоне высокой смены рук, а восстановление TSM на Тайване конструктивно, но все еще ниже подтверждения NT$2400."),
    ("1. MU needs second confirmation", "1. MU нужно второе подтверждение"),
    ("MU was still top five on TraderXYZ 24h notional flow, around $61.71M, but U.S. cash MU fell about 5.2% after earnings. Attention is high, but chasing strength is fading.", "MU все еще входит в топ-5 по 24-часовому обороту TraderXYZ, около $61,71 млн, но на рынке США акция упала примерно на 5,2% после отчета. Интерес высокий, но импульс догоняющей покупки слабеет."),
    ("MU was still top five on TraderXYZ with about $61.7M 24h notional and +2.0%, but U.S. cash MU fell about 5.2% after earnings. Attention remains high, while chase intensity has cooled.", "MU все еще входила в топ-5 TraderXYZ с 24-часовым оборотом около $61,7 млн и ростом 2,0%, но на рынке США акция упала примерно на 5,2% после отчета. Интерес остается высоким, но интенсивность догоняющей покупки снизилась."),
    ("2. TSM repair is positive but not acceleration", "2. Восстановление TSM позитивно, но это еще не ускорение"),
    ("Taiwan Weighted rose about 1.98%, and TSM 2330.TW traded around 2385/2390 TWD versus a prior 2340 close. The rebound is supportive, but trend confirmation needs a clean reclaim of 2400.", "Индекс Taiwan Weighted вырос примерно на 1,98%, а TSM 2330.TW торговалась около 2385/2390 TWD против предыдущего закрытия 2340. Отскок поддерживает картину, но для подтверждения тренда нужен уверенный возврат выше 2400."),
    ("Taiwan Weighted rose about 1.98%, and 2330.TW traded near NT$2385/2390 after a prior NT$2340 close. Trend acceleration needs a clean move back above NT$2400.", "Индекс Taiwan Weighted вырос примерно на 1,98%, а 2330.TW торговалась около NT$2385/2390 после предыдущего закрытия NT$2340. Для ускорения тренда нужен уверенный возврат выше NT$2400."),
    ("3. Memory chain is internally split", "3. Внутри цепочки памяти есть расхождение"),
    ("3. Memory chain is splitting internally", "3. Внутри цепочки памяти есть расхождение"),
    ("DRAM fell slightly on TraderXYZ, SNDK rose slightly, while U.S. spot SNDK and AMAT were clearly weaker. The theme remains, but selection has already started.", "DRAM немного снизился на TraderXYZ, SNDK слегка вырос, а на рынке США SNDK и AMAT заметно слабее. Тема остается, но отбор бумаг уже начался."),
    ("DRAM was slightly lower and SNDK slightly higher on TraderXYZ, while SNDK and AMAT sold off hard in U.S. cash. The memory thesis is alive, but now selective.", "DRAM был немного ниже, а SNDK немного выше на TraderXYZ, тогда как SNDK и AMAT резко снизились на рынке США. Тезис по памяти жив, но теперь требует отбора."),
    ("4. Macro remains the ceiling", "4. Макро остается потолком"),
    ("4. Macro keeps the ceiling", "4. Макро остается потолком"),
    ("U.S. PCE at 4.1% YoY and core PCE at 3.4% keep Fed easing difficult. This matters because AI hardware is long-duration growth: valuation expansion is harder when real rates stay high.", "PCE США на уровне 4,1% г/г и базовый PCE 3,4% осложняют смягчение ФРС. Это важно, потому что AI-оборудование относится к long-duration росту: при высоких реальных ставках расширение мультипликаторов сложнее."),
    ("U.S. PCE at 4.1% YoY and core PCE at 3.4% mean the Fed cannot pivot quickly. Strong earnings can support winners, but broad tech multiple expansion remains constrained.", "PCE США на уровне 4,1% г/г и базовый PCE 3,4% означают, что ФРС не может быстро перейти к смягчению. Сильные отчеты поддерживают победителей, но широкое расширение мультипликаторов техсектора остается ограниченным."),
    ("5. Crypto is not driving risk-on today", "5. Крипто сегодня не задает risk-on"),
    ("BTC and ETH were slightly lower to flat, while HYPE was flat near 61.86. Crypto is not providing a clean liquidity tailwind for AI beta today.", "BTC и ETH были слегка слабее или около нуля, HYPE держался около 61,86. Крипто сегодня не дает чистого ликвидностного попутного ветра для AI-беты."),
    ("These signals decide whether AI memory rotation remains healthy.", "Эти сигналы покажут, остается ли ротация в AI-памяти здоровой."),
    ("Can MU hold above 1140-1150 without more profit-taking?", "Сможет ли MU удержаться выше 1140-1150 без новой фиксации прибыли?"),
    ("Can MU hold the 1140-1150 zone after post-earnings profit-taking?", "Сможет ли MU удержать зону 1140-1150 после фиксации прибыли на отчете?"),
    ("Can TSM 2330.TW reclaim and hold NT$2400 with Taiwan tech breadth?", "Сможет ли TSM 2330.TW вернуть и удержать NT$2400 на фоне ширины тайваньского техсектора?"),
    ("Do AMAT, ASML and SNDK recover, confirming the MU read-through into capex?", "Восстановятся ли AMAT, ASML и SNDK, подтверждая перенос сигнала MU на capex?"),
    ("Do DRAM and SNDK regain TraderXYZ volume, or does memory heat keep fading?", "Вернут ли DRAM и SNDK объемы на TraderXYZ, или интерес к памяти продолжит остывать?"),
    ("Do Fed comments after high PCE pressure tech valuation multiples?", "Будут ли комментарии ФРС после высокого PCE давить на мультипликаторы техсектора?"),
    ("Stay constructive on AI bottleneck assets, but do not chase memory blindly. MU needs sideways digestion or renewed volume; TSM needs NT$2400; macro still limits broad tech beta.", "Сохраняйте конструктивный взгляд на активы с AI-дефицитом, но не догоняйте память вслепую. MU нужна боковая разгрузка или новый объем; TSM нужен уровень NT$2400; макро все еще ограничивает широкую технологическую бету."),
    ("U.S. cash from 2026-06-26 close; Taiwan and TraderXYZ/Hyperliquid around 2026-06-29 09:45 CST.", "рынок США по закрытию 2026-06-26; Тайвань и TraderXYZ/Hyperliquid около 2026-06-29 09:45 CST."),
    ("Top 24h notional flows included", "Крупнейшие 24-часовые номинальные потоки включали"),
    ("around $180M", "около $180 млн"),
    ("around $158M", "около $158 млн"),
    ("around $122M", "около $122 млн"),
    ("around $92.9M", "около $92,9 млн"),
    ("around $61.7M", "около $61,7 млн"),
    ("around $49.0M", "около $49,0 млн"),
    ("around $47.3M", "около $47,3 млн"),
    ("around $42.6M", "около $42,6 млн"),
    ("around $30.3M", "около $30,3 млн"),
    ("around $25.0M", "около $25,0 млн"),
    ("Crypto is broadly flat and does not provide a clean risk-on signal today.", "Крипто в целом около нуля и сегодня не дает чистого сигнала risk-on."),
    ("The strong MU report does not guarantee a one-way stock move.", "Сильный отчет MU не гарантирует одностороннего движения акции."),
    ("SPY was near 733.8 (-0.07%) and QQQ near 715.1 (-0.18%). SMH fell about 3.36% and SOXX about 4.55%. TSM ADR was near 429.5 (-1.25%), MU near 1150.1 (-5.2%), NVDA near 198.2 (+1.25%), AMAT near 617.1 (-7.6%), ASML near 1789.4 (-2.8%) and SNDK near 2134.0 (-8.6%).", "SPY был около 733,8 (-0,07%), QQQ около 715,1 (-0,18%). SMH снизился примерно на 3,36%, SOXX на 4,55%. TSM ADR был около 429,5 (-1,25%), MU около 1150,1 (-5,2%), NVDA около 198,2 (+1,25%), AMAT около 617,1 (-7,6%), ASML около 1789,4 (-2,8%), SNDK около 2134,0 (-8,6%)."),
    ("Taiwan Weighted traded near 45,452.66, up about 1.98%, with an intraday high near 45,456.16. TSM 2330.TW was around NT$2385/2390 versus a prior NT$2340 close, with intraday high NT$2390 and low NT$2330. This is repair, not yet a fresh acceleration signal.", "Taiwan Weighted торговался около 45 452,66, прибавляя примерно 1,98%, с внутридневным максимумом около 45 456,16. TSM 2330.TW была около NT$2385/2390 против предыдущего закрытия NT$2340, с максимумом NT$2390 и минимумом NT$2330. Это восстановление, но еще не новый сигнал ускорения."),
    ("MU staying top five is important, but turnover is lower than peak excitement.", "То, что MU остается в топ-5, важно, но оборот ниже пикового ажиотажа."),
    ("SKHX around $180M, XYZ100 around $158M, CL around $122M, SP500 around $92.9M, MU around $61.7M, DRAM around $49.0M, SILVER around $47.3M, Brent around $42.6M, SPCX around $30.3M and SNDK around $25.0M.", "SKHX около $180 млн, XYZ100 около $158 млн, CL около $122 млн, SP500 около $92,9 млн, MU около $61,7 млн, DRAM около $49,0 млн, SILVER около $47,3 млн, Brent около $42,6 млн, SPCX около $30,3 млн и SNDK около $25,0 млн."),
    ("BTC traded near 59,523 (-1.17%), ETH near 1,571.3 (-0.27%), SOL near 71.582 (+1.03%) and HYPE near 61.861 (flat).", "BTC торговался около 59 523 (-1,17%), ETH около 1 571,3 (-0,27%), SOL около 71,582 (+1,03%), а HYPE около 61,861 без выраженного изменения."),
    ("Micron FY2026 Q3 revenue was", "Выручка Micron за FY2026 Q3 составила"),
    ("with non-GAAP EPS of", "с non-GAAP EPS"),
    ("and gross margin near", "и валовой маржой около"),
    ("Q4 guidance points to revenue around", "Прогноз на Q4 указывает на выручку около"),
    ("gross margin near", "валовую маржу около"),
    ("and non-GAAP EPS around", "и non-GAAP EPS около"),
    ("commentary supports improving AI memory visibility", "комментарии поддерживают улучшение видимости по AI-памяти"),
    ("frames AI capex as a multi-year infrastructure cycle", "рассматривает AI capex как многолетний инфраструктурный цикл"),
    ("Micron FY2026 Q3 revenue was 41.456B with non-GAAP EPS of 25.11 and gross margin near 84.6%. Q4 guidance points to revenue around 50B, gross margin near 86% and non-GAAP EPS around 31. Wedbush, BNP Paribas and Morgan Stanley commentary supports improving AI memory visibility, while Goldman Sachs frames AI capex as a multi-year infrastructure cycle.", "Выручка Micron за FY2026 Q3 составила 41,456 млрд, non-GAAP EPS - 25,11, валовая маржа около 84,6%. Прогноз на Q4 указывает на выручку около 50 млрд, маржу около 86% и non-GAAP EPS около 31. Комментарии Wedbush, BNP Paribas и Morgan Stanley поддерживают улучшение видимости по AI-памяти, а Goldman Sachs рассматривает AI capex как многолетний инфраструктурный цикл."),
    ("Expectations are now higher, TSM repair still needs NT$2400 confirmation, AI capex beneficiaries are rotating, and high PCE keeps the Fed cautious.", "Ожидания теперь выше, восстановлению TSM все еще нужно подтверждение выше NT$2400, бенефициары AI capex ротируются, а высокий PCE удерживает ФРС в осторожном режиме."),
    ("AI memory stays alive, but MU enters second-confirmation mode", "AI-память остается в игре, но MU переходит в режим второго подтверждения"),
    ("MU remains top TraderXYZ flow, TSM rebounds in Taiwan, and high PCE caps broad tech valuation expansion.", "MU остается среди главных потоков TraderXYZ, TSM отскакивает на Тайване, а высокий PCE ограничивает широкое расширение оценок техсектора."),
    ("AI hardware stays strong while TSM confirms in Taiwan", "AI-оборудование остается сильным, пока TSM подтверждается на Тайване"),
    ("Taiwan cash confirms TSM, MU profit rules matter, and HYPE leads risk appetite.", "Тайваньский cash-рынок подтверждает TSM, по MU важны правила фиксации прибыли, а HYPE ведет риск-аппетит."),
    ("AI semis rotate at highs while HYPE stays firm", "AI-полупроводники ротируются на максимумах, пока HYPE держится уверенно"),
    ("MU leads HBM, TSM and NVDA cool, and HYPE remains strong.", "MU ведет HBM-направление, TSM и NVDA остывают, а HYPE остается сильным."),
    ("AI semis enter high-level dispersion", "AI-полупроводники входят в расхождение на высоких уровнях"),
    ("TSM and NVDA rise, MU churns at highs, and HYPE stays strong.", "TSM и NVDA растут, MU меняет руки на максимумах, а HYPE остается сильным."),
    ("AI semis rotate into certainty", "AI-полупроводники ротируются в сторону большей определенности"),
    ("TSM and MU lead while NVDA cools.", "TSM и MU лидируют, пока NVDA остывает."),
    ("AI semiconductors broaden beyond NVDA", "AI-полупроводники расширяют лидерство за пределы NVDA"),
    ("TSM, MU, AMAT and Asia supply chains confirm AI capex diffusion.", "TSM, MU, AMAT и азиатские цепочки поставок подтверждают расширение AI capex."),
    ("AI semiconductors enter high-level confirmation", "AI-полупроводники входят в фазу подтверждения на высоких уровнях"),
    ("Taiwan fades from highs, Korea stays firm, HL perps price AI premiums.", "Тайвань откатывается от максимумов, Корея держится, а перпы закладывают AI-премию."),
    ("TSM leads AI repair while U.S. markets are closed", "TSM ведет восстановление AI, пока рынки США закрыты"),
    ("Taiwan cash and HL perps price a recovery.", "Тайваньский cash-рынок и перпы закладывают восстановление."),
    ("NVIDIA validates AI demand, but valuation discipline matters", "NVIDIA подтверждает спрос на AI, но дисциплина оценок важнее"),
    ("Strong guidance, weaker NVDA reaction, firm chip ETFs and macro constraints.", "Сильный прогноз, слабая реакция NVDA, устойчивые chip ETF и макро-ограничения."),
    ("High-level range trading + structural opportunities", "Диапазон на высоких уровнях и структурные возможности"),
    ("Semiconductor divergence, neutral BTC leverage, elevated oil and gold.", "Расхождение полупроводников, нейтральное плечо BTC, повышенные нефть и золото."),
    ("Repair rally, but hawkish policy tail risk", "Восстановительный отскок, но остается риск жесткой политики"),
    ("Oil and yields cooled, while AI valuations stayed rate-sensitive.", "Нефть и доходности остыли, а оценки AI остались чувствительными к ставкам."),
    ("AI memory remains valid as medium-term theme. Short term, MU, DRAM and SNDK are in high-level churn, while Taiwan восстановление TSM is constructive but still below NT$2400 confirmation.", "AI-память остается рабочей среднесрочной темой. Краткосрочно MU, DRAM и SNDK находятся в зоне высокой смены рук, а восстановление TSM на Тайване конструктивно, но все еще ниже подтверждения NT$2400."),
    ("2. восстановление TSM is positive but not acceleration", "2. Восстановление TSM позитивно, но это еще не ускорение"),
    ("These signals decide whether AI ротация памяти remains healthy.", "Эти сигналы покажут, остается ли ротация в AI-памяти здоровой."),
    ("SPCX около $30,3 млн and SNDK около $25,0 млн.", "SPCX около $30,3 млн и SNDK около $25,0 млн."),
    ("Wedbush, BNP Paribas and Morgan Stanley комментарии поддерживают улучшение видимости по AI-памяти, while Goldman Sachs рассматривает AI capex как многолетний инфраструктурный цикл.", "Комментарии Wedbush, BNP Paribas и Morgan Stanley поддерживают улучшение видимости по AI-памяти, а Goldman Sachs рассматривает AI capex как многолетний инфраструктурный цикл."),
    ("Expectations are now higher, восстановление TSM still needs NT$2400 confirmation, AI capex beneficiaries are rotating, and high PCE keeps the Fed cautious.", "Ожидания теперь выше, восстановлению TSM все еще нужно подтверждение выше NT$2400, бенефициары AI capex ротируются, а высокий PCE удерживает ФРС в осторожном режиме."),
]


def apply_ru_replacements(text):
    for old, new in RU_TEXT_REPLACEMENTS:
        text = text.replace(old, new)
    return text


def ru_brief_meta(date):
    return RU_BRIEFS.get(date, {})


def read(path):
    return path.read_text(encoding="utf-8")


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def meta(content, name):
    match = re.search(rf'<meta name="{re.escape(name)}" content="([^"]*)"', content)
    return html.unescape(match.group(1)) if match else ""


def title(content):
    match = re.search(r"<title>(.*?)</title>", content)
    return html.unescape(match.group(1)) if match else "GateAffiliate Daily Market Brief"


def h1(content):
    match = re.search(r"<h1>(.*?)</h1>", content)
    return html.unescape(re.sub("<.*?>", "", match.group(1))) if match else ""


def slug(lang, suffix=""):
    prefix = {
        "zh-cn": "",
        "zh-hant": "/zh-hant",
        "en": "/en",
        "ru": "/ru",
    }[lang]
    return f"{prefix}{suffix}"


def daily_slug(lang, date=None):
    base = slug(lang, "/daily/")
    return f"{base}{date}/" if date else base


def source_path(date, lang):
    if lang in ("zh-cn", "zh-hant"):
        return SOURCE / date / "index.html"
    return SOURCE / date / lang / "index.html"


def source_content(date, lang):
    content = read(source_path(date, lang))
    return T2S.convert(content) if lang == "zh-cn" else content


def localize_title(text, lang):
    text = text.replace("Hyperliquid HYPE Market Brief", "GateAffiliate Daily Market Brief")
    text = text.replace("Hyperliquid HYPE 市場簡報", "GateAffiliate 每日市場日報")
    text = text.replace("Hyperliquid HYPE 市场简报", "GateAffiliate 每日市场日报")
    if lang == "zh-cn":
        text = T2S.convert(text).replace("每日市場日報", "每日市场日报")
    if lang == "ru":
        text = text.replace("GateAffiliate Daily Market Brief", "GateAffiliate Ежедневный обзор рынка")
        text = apply_ru_replacements(text)
    return text


def localize_desc(text, lang):
    text = text.replace("Hyperliquid HYPE market brief", "GateAffiliate daily market brief")
    text = text.replace("Hyperliquid HYPE 市場簡報", "GateAffiliate 每日市場日報")
    text = text.replace("Hyperliquid HYPE 市场简报", "GateAffiliate 每日市场日报")
    if lang == "zh-cn":
        text = T2S.convert(text).replace("每日市場日報", "每日市场日报")
    if lang == "ru":
        text = apply_ru_replacements(text)
    return text


def extract_between(content, start_pat, end_pat):
    start = re.search(start_pat, content)
    end = re.search(end_pat, content)
    if not start or not end:
        raise ValueError("Cannot extract page body")
    return content[start.start():end.start()] + "</main>"


def lang_switch(current_lang, current_path_by_lang):
    links = []
    for lang in LANGS:
        meta = LANG_META[lang]
        current = ' aria-current="true"' if lang == current_lang else ""
        links.append(f'<a{current} href="{current_path_by_lang[lang]}">{meta["short"]}</a>')
    return f'<div class="lang-switch" aria-label="Language">{"".join(links)}</div>'


def header(lang, current_path_by_lang=None):
    m = LANG_META[lang]
    nav = m["nav"]
    current_path_by_lang = current_path_by_lang or {l: LANG_META[l]["home"] for l in LANGS}
    return f'''<header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="{m["home"]}">
          <span class="brand-mark"><img src="/assets/gate-logo.ico" alt="GateAffiliate logo"></span>
          <span>GateAffiliate</span>
        </a>
        <div class="nav-links">
          <a href="{m["home"]}#invite">{nav[0]}</a>
          <a href="{m["home"]}#steps">{nav[1]}</a>
          <a href="{m["daily"]}">{nav[2]}</a>
          <a href="{m["home"]}#faq">{nav[3]}</a>
          <a class="button button-primary" data-invite href="#">{nav[4]}</a>
        </div>
        {lang_switch(lang, current_path_by_lang)}
      </nav>
    </header>'''


def footer(lang):
    m = LANG_META[lang]
    labels = {
        "zh-cn": ("每日市场日报", "Gate 官方活动"),
        "zh-hant": ("每日市場日報", "Gate 官方活動"),
        "en": ("Daily briefs", "Gate affiliate program"),
        "ru": ("Ежедневные обзоры", "Программа Gate affiliate"),
    }[lang]
    return f'''<footer>
      <div class="footer-inner">
        <span>{m["footer"]}</span>
        <div class="footer-links">
          <a href="{m["home"]}">GateAffiliate</a>
          <a href="{m["daily"]}">{labels[0]}</a>
          <a data-official href="#">{labels[1]}</a>
        </div>
      </div>
    </footer>'''


def alternates(path_by_lang, x_default):
    lines = []
    for lang in LANGS:
        hreflang = {"zh-cn": "zh-CN", "zh-hant": "zh-Hant", "en": "en", "ru": "ru"}[lang]
        lines.append(f'<link rel="alternate" hreflang="{hreflang}" href="{BASE_URL}{path_by_lang[lang]}">')
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}{x_default}">')
    return "\n    ".join(lines)


def rewrite_fragment(fragment, lang):
    fragment = fragment.replace("/market-briefing/images/", "/daily/images/")
    fragment = fragment.replace("HLBESTCODE", CODE)
    fragment = fragment.replace("Use HLBESTCODE", f"Use {CODE}")
    fragment = fragment.replace("使用 HLBESTCODE", f"使用 {CODE}")
    fragment = fragment.replace("Join Hyperliquid", "Join Gate")
    fragment = fragment.replace("加入 Hyperliquid", "注册 Gate")
    fragment = fragment.replace("Hyperliquid HYPE Market Brief", "GateAffiliate Daily Market Brief")
    fragment = fragment.replace("Hyperliquid HYPE 市場簡報", "GateAffiliate 每日市場日報")
    fragment = fragment.replace("Hyperliquid HYPE 市场简报", "GateAffiliate 每日市场日报")
    fragment = fragment.replace('href="/hype-market-brief/"', f'href="{LANG_META[lang]["daily"]}"')
    fragment = fragment.replace('href="/zh/market-briefing/"', f'href="{LANG_META["zh-hant"]["daily"]}"')
    fragment = fragment.replace('href="/ru/market-briefing/"', f'href="{LANG_META["ru"]["daily"]}"')
    fragment = fragment.replace('href="/market-briefing/"', f'href="{LANG_META["en"]["daily"]}"')
    fragment = re.sub(r'href="/market-briefing/(\d{4}-\d{2}-\d{2})/en/"', lambda m: f'href="{daily_slug("en", m.group(1))}"', fragment)
    fragment = re.sub(r'href="/market-briefing/(\d{4}-\d{2}-\d{2})/ru/"', lambda m: f'href="{daily_slug("ru", m.group(1))}"', fragment)
    fragment = re.sub(r'href="/market-briefing/(\d{4}-\d{2}-\d{2})/"', lambda m: f'href="{daily_slug(lang if lang in ("zh-cn", "zh-hant") else "zh-hant", m.group(1))}"', fragment)
    if lang == "zh-cn":
        fragment = T2S.convert(fragment)
    if lang == "ru":
        fragment = apply_ru_replacements(fragment)
    return fragment


def brief_cta(lang):
    text = {
        "zh-cn": ("使用 GateAffiliate 邀请码注册", f"复制邀请码 {CODE}，通过 Gate 官方入口注册。奖励、返佣和 affiliate 资格以 Gate 当前页面显示为准。", "打开 Gate 注册", "复制邀请码", "已复制", "GateAffiliate 邀请码"),
        "zh-hant": ("使用 GateAffiliate 邀請碼註冊", f"複製邀請碼 {CODE}，透過 Gate 官方入口註冊。獎勵、返佣和 affiliate 資格以 Gate 當前頁面顯示為準。", "打開 Gate 註冊", "複製邀請碼", "已複製", "GateAffiliate 邀請碼"),
        "en": ("Join with the GateAffiliate invite code", f"Copy invite code {CODE} and register through the official Gate entry. Rewards, rebates, and affiliate eligibility follow Gate's current terms.", "Open Gate registration", "Copy code", "Copied", "GateAffiliate invite code"),
        "ru": ("Регистрация с инвайт-кодом GateAffiliate", f"Скопируйте инвайт-код {CODE} и зарегистрируйтесь через официальный вход Gate. Бонусы, rebate и affiliate eligibility зависят от текущих условий Gate.", "Открыть регистрацию Gate", "Скопировать код", "Скопировано", "Инвайт-код GateAffiliate"),
    }[lang]
    return f'''<section class="bonus-band">
        <div class="wrap reward">
          <div>
            <span class="eyebrow">GateAffiliate</span>
            <h2>{text[0]}</h2>
            <p>{text[1]}</p>
            <div class="hero-actions">
              <a class="button button-primary" data-invite href="#">{text[2]}</a>
              <button class="button button-secondary" data-copy-code data-copied="{text[4]}">{text[3]}</button>
            </div>
          </div>
          <div class="reward-amount"><b>{CODE}</b><span>{text[5]}</span></div>
        </div>
      </section>'''


def page(date, lang):
    content = source_content(date, lang)
    page_title = localize_title(title(content), lang)
    page_desc = localize_desc(meta(content, "description"), lang)
    if lang == "ru" and ru_brief_meta(date):
        brief = ru_brief_meta(date)
        page_title = f"Ежедневный обзор рынка GateAffiliate {date} | {brief['suffix']}"
        page_desc = f"{date} GateAffiliate: {brief['summary']}"
    page_path = daily_slug(lang, date)
    path_by_lang = {l: daily_slug(l, date) for l in LANGS}
    image_match = re.search(r'<meta property="og:image" content="https://hyperliquidreferral\.com/market-briefing/images/([^"]+)"', content)
    image = f"{BASE_URL}/daily/images/{image_match.group(1)}" if image_match else f"{BASE_URL}/assets/hero.png"
    body = rewrite_fragment(extract_between(content, r"<section class=\"hero\">", r"</main>"), lang)
    body = body.replace("</main>", brief_cta(lang) + "</main>")
    schema = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": page_title,
        "description": page_desc,
        "datePublished": date,
        "dateModified": date,
        "author": {"@type": "Organization", "name": "GateAffiliate"},
        "publisher": {"@type": "Organization", "name": "GateAffiliate", "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/assets/gate-logo.ico"}},
        "image": image,
        "mainEntityOfPage": f"{BASE_URL}{page_path}",
    }
    return f'''<!doctype html>
<html lang="{LANG_META[lang]["html"]}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(page_title)}</title>
    <meta name="description" content="{html.escape(page_desc)}">
    <meta name="robots" content="index,follow,max-image-preview:large">
    <link rel="canonical" href="{BASE_URL}{page_path}">
    {alternates(path_by_lang, path_by_lang["zh-cn"])}
    <meta property="og:type" content="article">
    <meta property="og:title" content="{html.escape(page_title)}">
    <meta property="og:description" content="{html.escape(page_desc)}">
    <meta property="og:image" content="{image}">
    <meta property="og:site_name" content="GateAffiliate">
    <meta property="og:url" content="{BASE_URL}{page_path}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="theme-color" content="#07102b">
    <link rel="icon" href="/assets/gate-logo.ico" type="image/x-icon">
    <link rel="preload" as="image" href="{image.replace(BASE_URL, '')}">
    <link rel="stylesheet" href="/assets/styles.css?v={STYLE_VERSION}">
    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
  </head>
  <body>
    {header(lang, path_by_lang)}
    {body}
    {footer(lang)}
    <script src="/assets/app.js?v={STYLE_VERSION}"></script>
  </body>
</html>
'''


def home_page(lang):
    c = HOME[lang]
    m = LANG_META[lang]
    home_labels = {
        "zh-cn": ("Invite code", "Gate 官方活动", "Copy", "Copied", "Daily brief"),
        "zh-hant": ("Invite code", "Gate 官方活動", "Copy", "Copied", "Daily brief"),
        "en": ("Invite code", "Gate affiliate program", "Copy", "Copied", "Daily brief"),
        "ru": ("Инвайт-код", "Программа Gate affiliate", "Копировать", "Скопировано", "Ежедневный обзор"),
    }[lang]
    path_by_lang = {l: LANG_META[l]["home"] for l in LANGS}
    org_schema = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "GateAffiliate",
        "url": f"{BASE_URL}{m['home']}",
        "description": c["desc"],
        "inLanguage": m["html"],
    }
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]],
    }
    stats = "\n".join(f'<div class="trust-item"><strong>{s}</strong><span>{t}</span></div>' for s, t in c["stats"])
    steps = "\n".join(
        f'''<article class="card step">
              <div class="icon">{i:02d}</div>
              <h3>{h}</h3>
              <p>{p}</p>
              {f'<div class="code-box"><code>{CODE}</code><button class="mini-button" data-copy-code data-copied="{home_labels[3]}">{home_labels[2]}</button></div>' if i == 2 else ''}
            </article>'''
        for i, (h, p) in enumerate(c["steps"], 1)
    )
    faqs = "\n".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(c["faq"]))
    return f'''<!doctype html>
<html lang="{m["html"]}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(c["title"])}</title>
    <meta name="description" content="{html.escape(c["desc"])}">
    <meta name="robots" content="index,follow,max-image-preview:large">
    <link rel="canonical" href="{BASE_URL}{m["home"]}">
    {alternates(path_by_lang, path_by_lang["zh-cn"])}
    <meta property="og:type" content="website">
    <meta property="og:title" content="{html.escape(c["title"])}">
    <meta property="og:description" content="{html.escape(c["desc"])}">
    <meta property="og:image" content="{BASE_URL}/assets/hero.png">
    <meta property="og:site_name" content="GateAffiliate">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="theme-color" content="#07102b">
    <link rel="icon" href="/assets/gate-logo.ico" type="image/x-icon">
    <link rel="preload" as="image" href="/assets/hero.png">
    <link rel="stylesheet" href="/assets/styles.css?v={STYLE_VERSION}">
    <script type="application/ld+json">{json.dumps(org_schema, ensure_ascii=False)}</script>
    <script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False)}</script>
  </head>
  <body>
    {header(lang, path_by_lang)}
    <section class="hero">
      <div class="hero-inner">
        <span class="eyebrow">{c["eyebrow"]}</span>
        <h1>{c["h1"]}</h1>
        <p class="hero-copy">{c["copy"]}</p>
        <div class="hero-actions">
          <a class="button button-primary" data-invite href="#">{c["open"]}</a>
          <button class="button button-secondary" data-copy-code data-copied="{home_labels[3]}">{c["copy_code"]}</button>
        </div>
        <div class="trust-row">{stats}</div>
      </div>
    </section>
    <main>
      <section id="invite" class="bonus-band">
        <div class="wrap reward">
          <div><span class="eyebrow">{home_labels[0]}</span><h2>{c["bonus_h2"]}</h2><p>{c["bonus_p"]}</p>
            <div class="hero-actions"><a class="button button-primary" data-invite href="#">{c["open"]}</a><a class="button button-secondary" data-official href="#">{home_labels[1]}</a></div>
          </div>
          <div class="reward-amount"><b>{CODE}</b><span>{home_labels[0]}</span><button class="mini-button" data-copy-code data-copied="{home_labels[3]}">{home_labels[2]}</button></div>
        </div>
      </section>
      <section id="steps"><div class="wrap"><div class="section-head"><h2>{c["steps_h2"]}</h2><p>{c["steps_p"]}</p></div><div class="grid grid-3 steps">{steps}</div></div></section>
      <section><div class="wrap latest-brief"><div><span class="eyebrow">{home_labels[4]}</span><h2>{c["latest_h2"]}</h2><p>{c["latest_p"]}</p></div><a class="button button-secondary" href="{m["daily"]}">{m["nav"][2]}</a></div></section>
      <section id="faq" class="faq"><div class="wrap"><div class="section-head"><h2>{c["faq_h2"]}</h2><p>{c["faq_p"]}</p></div>{faqs}</div></section>
    </main>
    {footer(lang)}
    <script src="/assets/app.js?v={STYLE_VERSION}"></script>
  </body>
</html>
'''


def daily_index(lang):
    m = LANG_META[lang]
    path_by_lang = {l: daily_slug(l) for l in LANGS}
    eyebrow = {
        "zh-cn": "GateAffiliate 每日市场日报",
        "zh-hant": "GateAffiliate 每日市場日報",
        "en": "GateAffiliate daily market brief",
        "ru": "Ежедневный обзор GateAffiliate",
    }[lang]
    cards = []
    for date in reversed(DATES):
        content = source_content(date, lang)
        card_title = localize_title(h1(content) or title(content), lang)
        desc = localize_desc(meta(content, "description"), lang)
        if lang == "ru" and ru_brief_meta(date):
            brief = ru_brief_meta(date)
            card_title = brief["title"]
            desc = brief["summary"]
        cards.append(f'''<a class="history-link" href="{daily_slug(lang, date)}">
              <span class="history-date">{date}</span>
              <span><span class="history-title">{html.escape(card_title)}</span><span class="history-summary">{html.escape(desc[:140])}</span></span>
              <span class="history-tag">{m["short"]}</span>
            </a>''')
    return f'''<!doctype html>
<html lang="{m["html"]}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(m["daily_title"])}</title>
    <meta name="description" content="{html.escape(m["daily_desc"])}">
    <meta name="robots" content="index,follow,max-image-preview:large">
    <link rel="canonical" href="{BASE_URL}{m["daily"]}">
    {alternates(path_by_lang, path_by_lang["zh-cn"])}
    <meta property="og:type" content="website">
    <meta property="og:title" content="{html.escape(m["daily_title"])}">
    <meta property="og:description" content="{html.escape(m["daily_desc"])}">
    <meta property="og:image" content="{BASE_URL}/assets/hero.png">
    <meta name="theme-color" content="#07102b">
    <link rel="stylesheet" href="/assets/styles.css?v={STYLE_VERSION}">
    <link rel="icon" href="/assets/gate-logo.ico" type="image/x-icon">
  </head>
  <body>
    {header(lang, path_by_lang)}
    <section class="hero"><div class="hero-inner"><span class="eyebrow">{eyebrow}</span><h1>{m["daily_h1"]}</h1><p class="hero-copy">{m["daily_copy"]}</p><div class="hero-actions"><a class="button button-primary" href="{daily_slug(lang, DATES[-1])}">{m["latest"]}</a><a class="button button-secondary" data-invite href="#">{m["nav"][4]}</a></div></div></section>
    <main><section id="history"><div class="wrap"><div class="section-head"><h2>{m["history"]}</h2><p>{m["history_copy"]}</p></div><div class="history-list">{''.join(cards)}</div></div></section></main>
    {footer(lang)}
    <script src="/assets/app.js?v={STYLE_VERSION}"></script>
  </body>
</html>
'''


def sitemap():
    urls = []
    for lang in LANGS:
        urls.append((LANG_META[lang]["home"], "daily", "1.0" if lang == "zh-cn" else "0.9"))
        urls.append((LANG_META[lang]["daily"], "daily", "0.9"))
        for date in DATES:
            urls.append((daily_slug(lang, date), "monthly", "0.72"))
    body = "\n".join(
        f"  <url>\n    <loc>{BASE_URL}{loc}</loc>\n    <lastmod>2026-06-30</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{priority}</priority>\n  </url>"
        for loc, freq, priority in urls
    )
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
'''


def clean_generated():
    for folder in [ROOT / "zh-hant", ROOT / "en", ROOT / "ru"]:
        if folder.exists():
            shutil.rmtree(folder)
    for child in (ROOT / "daily").glob("2026-*"):
        if child.is_dir():
            shutil.rmtree(child)
    bad_daily_index_dir = ROOT / "daily" / "index.html"
    if bad_daily_index_dir.is_dir():
        shutil.rmtree(bad_daily_index_dir)


def main():
    clean_generated()
    image_dest = ROOT / "daily" / "images"
    image_dest.mkdir(parents=True, exist_ok=True)
    for image in (SOURCE / "images").glob("*"):
        if image.is_file():
            shutil.copy2(image, image_dest / image.name)
    for lang in LANGS:
        home_path = ROOT / slug(lang, "/index.html").lstrip("/")
        if lang == "zh-cn":
            home_path = ROOT / "index.html"
        write(home_path, home_page(lang))
        daily_index_path = ROOT / LANG_META[lang]["daily"].lstrip("/") / "index.html"
        write(daily_index_path, daily_index(lang))
        for date in DATES:
            write(ROOT / daily_slug(lang, date).lstrip("/") / "index.html", page(date, lang))
    write(ROOT / "sitemap.xml", sitemap())
    print(f"Imported {len(DATES)} dates in {len(LANGS)} languages: {len(DATES) * len(LANGS)} daily pages.")


if __name__ == "__main__":
    main()
