#!/usr/bin/env python3
from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://gateaffiliate.com"
CODE = "VLYQB1HXUW"
TODAY = "2026-07-01"

LANGS = {
    "zh-cn": {"prefix": "", "html": "zh-CN", "home": "/", "daily": "/daily/"},
    "zh-hant": {"prefix": "/zh-hant", "html": "zh-Hant", "home": "/zh-hant/", "daily": "/zh-hant/daily/"},
    "en": {"prefix": "/en", "html": "en", "home": "/en/", "daily": "/en/daily/"},
    "ru": {"prefix": "/ru", "html": "ru", "home": "/ru/", "daily": "/ru/daily/"},
}

HOME_GUIDES = {
    "zh-cn": {
        "heading": "交易前快速检查",
        "copy": "把邀请码、官方入口、账户安全和市场背景放在同一条流程里，减少注册和交易前的遗漏。",
        "cards": [
            ("Gate 邀请码", f"注册时确认 {CODE} 是否已经填入。", "/#invite"),
            ("注册步骤", "从官方入口开户，并完成基础安全设置。", "/#steps"),
            ("市场日报", "查看 BTC、ETH、AI 半导体和宏观风险变化。", "/daily/"),
            ("常见问题", "先确认奖励、返佣和账户资格的边界。", "/#faq"),
        ],
    },
    "zh-hant": {
        "heading": "交易前快速檢查",
        "copy": "把邀請碼、官方入口、帳戶安全和市場背景放在同一條流程裡，減少註冊和交易前的遺漏。",
        "cards": [
            ("Gate 邀請碼", f"註冊時確認 {CODE} 是否已經填入。", "/zh-hant/#invite"),
            ("註冊步驟", "從官方入口開戶，並完成基礎安全設定。", "/zh-hant/#steps"),
            ("市場日報", "查看 BTC、ETH、AI 半導體和宏觀風險變化。", "/zh-hant/daily/"),
            ("常見問題", "先確認獎勵、返佣和帳戶資格的邊界。", "/zh-hant/#faq"),
        ],
    },
    "en": {
        "heading": "Quick Check Before Trading",
        "copy": "Keep the invite code, official entry, account security, and daily market context in one clean flow.",
        "cards": [
            ("Gate invite code", f"Confirm {CODE} is entered during signup.", "/en/#invite"),
            ("How to register", "Open Gate from the official path and secure the account.", "/en/#steps"),
            ("Daily briefs", "Review BTC, ETH, AI semiconductors, and macro risk.", "/en/daily/"),
            ("FAQ", "Check the limits around rewards, rebates, and eligibility.", "/en/#faq"),
        ],
    },
    "ru": {
        "heading": "Быстрая Проверка Перед Торговлей",
        "copy": "Инвайт-код, официальный вход, безопасность аккаунта и рыночный контекст собраны в один простой маршрут.",
        "cards": [
            ("Инвайт-код Gate", f"Проверьте, что {CODE} указан при регистрации.", "/ru/#invite"),
            ("Регистрация", "Откройте Gate через официальный путь и защитите аккаунт.", "/ru/#steps"),
            ("Ежедневные обзоры", "Следите за BTC, ETH, AI-полупроводниками и макро-рисками.", "/ru/daily/"),
            ("FAQ", "Проверьте ограничения по бонусам, rebate и eligibility.", "/ru/#faq"),
        ],
    },
}

RELATED = {
    "zh-cn": ("继续阅读", [("注册邀请码", "/#invite"), ("日报目录", "/daily/"), ("常见问题", "/#faq")]),
    "zh-hant": ("繼續閱讀", [("註冊邀請碼", "/zh-hant/#invite"), ("日報目錄", "/zh-hant/daily/"), ("常見問題", "/zh-hant/#faq")]),
    "en": ("Continue Reading", [("Invite code", "/en/#invite"), ("Brief archive", "/en/daily/"), ("FAQ", "/en/#faq")]),
    "ru": ("Продолжить Чтение", [("Инвайт-код", "/ru/#invite"), ("Архив обзоров", "/ru/daily/"), ("FAQ", "/ru/#faq")]),
}

KEYWORDS = {
    "zh-cn": f"Gate 邀请码, Gate affiliate, Gate 返佣, Gate 40% 返佣, Gate 14400U 奖励, Gate 注册, GateAffiliate, {CODE}, 每日市场日报",
    "zh-hant": f"Gate 邀請碼, Gate affiliate, Gate 返佣, Gate 40% 返佣, Gate 14400U 獎勵, Gate 註冊, GateAffiliate, {CODE}, 每日市場日報",
    "en": f"Gate invite code, Gate affiliate, Gate referral code, Gate 40% rebate, Gate 14400U rewards, Gate registration, GateAffiliate, {CODE}, daily market brief",
    "ru": f"Gate инвайт-код, Gate affiliate, Gate referral code, Gate rebate 40%, Gate бонусы 14400U, регистрация Gate, GateAffiliate, {CODE}, ежедневный обзор рынка",
}


def lang_from_path(path):
    rel = "/" + path.relative_to(ROOT).as_posix()
    if rel.startswith("/zh-hant/"):
        return "zh-hant"
    if rel.startswith("/en/"):
        return "en"
    if rel.startswith("/ru/"):
        return "ru"
    return "zh-cn"


def url_path(path):
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def title_of(text):
    match = re.search(r"<title>(.*?)</title>", text, re.S)
    return html.unescape(match.group(1).strip()) if match else "GateAffiliate"


def desc_of(text):
    match = re.search(r'<meta name="description" content="([^"]*)"', text)
    return html.unescape(match.group(1).strip()) if match else ""


def og_image_of(text):
    match = re.search(r'<meta property="og:image" content="([^"]*)"', text)
    return match.group(1) if match else f"{BASE_URL}/assets/hero.png"


def remove_old(text):
    text = re.sub(r"\n?    <!-- seo-enhance:start -->.*?<!-- seo-enhance:end -->\n?", "\n", text, flags=re.S)
    text = re.sub(r"\n?      <!-- seo-guides:start -->.*?<!-- seo-guides:end -->\n?", "\n", text, flags=re.S)
    text = re.sub(r"\n?      <!-- seo-related:start -->.*?<!-- seo-related:end -->\n?", "\n", text, flags=re.S)
    text = re.sub(r'\n?\s*<meta name="keywords" content="[^"]*">', "", text)
    text = re.sub(r'\n?\s*<meta name="author" content="[^"]*">', "", text)
    text = re.sub(r'\n?\s*<meta name="format-detection" content="[^"]*">', "", text)
    text = re.sub(r'\n?\s*<meta property="og:url" content="[^"]*">', "", text)
    text = re.sub(r'\n?\s*<meta property="og:locale" content="[^"]*">', "", text)
    text = re.sub(r'\n?\s*<meta name="twitter:title" content="[^"]*">', "", text)
    text = re.sub(r'\n?\s*<meta name="twitter:description" content="[^"]*">', "", text)
    text = re.sub(r'\n?\s*<meta name="twitter:image" content="[^"]*">', "", text)
    return text


def breadcrumb_schema(path_value, title):
    parts = [("GateAffiliate", "/")]
    if "/daily/" in path_value:
        lang = "zh-cn"
        for key, data in LANGS.items():
            if path_value.startswith(data["prefix"] + "/") or path_value == data["home"]:
                lang = key
        daily_name = {"zh-cn": "每日市场日报", "zh-hant": "每日市場日報", "en": "Daily Briefs", "ru": "Ежедневные обзоры"}[lang]
        parts.append((daily_name, LANGS[lang]["daily"]))
        date = re.search(r"/daily/(\d{4}-\d{2}-\d{2})/", path_value)
        if date:
            parts.append((date.group(1), path_value))
    elif path_value != "/":
        parts.append((title.split("|")[0].strip(), path_value))
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": name, "item": f"{BASE_URL}{loc}"}
            for i, (name, loc) in enumerate(parts, 1)
        ],
    }


def head_block(path_value, lang, text):
    title = title_of(text)
    desc = desc_of(text)
    image = og_image_of(text)
    page_type = "CollectionPage" if path_value.endswith("/daily/") else "WebPage"
    if re.search(r"/daily/\d{4}-\d{2}-\d{2}/$", path_value):
        page_type = "Article"
    schemas = [
        {
            "@context": "https://schema.org",
            "@type": page_type,
            "name": title,
            "description": desc,
            "url": f"{BASE_URL}{path_value}",
            "inLanguage": LANGS[lang]["html"],
            "isPartOf": {"@type": "WebSite", "name": "GateAffiliate", "url": BASE_URL + "/"},
        },
        breadcrumb_schema(path_value, title),
    ]
    if path_value in ("/", "/zh-hant/", "/en/", "/ru/"):
        schemas.insert(
            0,
            {
                "@context": "https://schema.org",
                "@type": "Organization",
                "name": "GateAffiliate",
                "url": BASE_URL + "/",
                "logo": f"{BASE_URL}/assets/gate-logo.ico",
            },
        )
    meta = [
        '<!-- seo-enhance:start -->',
        f'<meta name="keywords" content="{html.escape(KEYWORDS[lang])}">',
        '<meta name="author" content="GateAffiliate">',
        '<meta name="format-detection" content="telephone=no">',
        f'<meta property="og:url" content="{BASE_URL}{path_value}">',
        f'<meta property="og:locale" content="{LANGS[lang]["html"].replace("-", "_")}">',
        f'<meta name="twitter:title" content="{html.escape(title)}">',
        f'<meta name="twitter:description" content="{html.escape(desc)}">',
        f'<meta name="twitter:image" content="{image}">',
    ]
    if path_value.endswith("/daily/"):
        items = []
        for i, href in enumerate(re.findall(r'<a class="history-link" href="([^"]+)"', text)[:12], 1):
            items.append({"@type": "ListItem", "position": i, "url": f"{BASE_URL}{href}"})
        schemas.append({"@context": "https://schema.org", "@type": "ItemList", "name": title, "itemListElement": items})
    meta.extend(f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>' for schema in schemas)
    meta.append("<!-- seo-enhance:end -->")
    return "\n    ".join(meta)


def guide_section(lang):
    data = HOME_GUIDES[lang]
    cards = "".join(
        f'<a class="guide-card" href="{href}"><strong>{html.escape(title)}</strong><span>{html.escape(copy)}</span></a>'
        for title, copy, href in data["cards"]
    )
    return f'''      <!-- seo-guides:start -->
      <section class="guide-section"><div class="wrap"><div class="section-head"><h2>{data["heading"]}</h2><p>{data["copy"]}</p></div><div class="guide-grid">{cards}</div></div></section>
      <!-- seo-guides:end -->
'''


def related_section(lang):
    heading, links = RELATED[lang]
    items = "".join(f'<a class="brief-pill" href="{href}">{html.escape(label)}</a>' for label, href in links)
    return f'''      <!-- seo-related:start -->
      <section class="related-links"><div class="wrap"><h2>{heading}</h2><div class="brief-meta">{items}</div></div></section>
      <!-- seo-related:end -->
'''


def enhance_html(path):
    text = remove_old(path.read_text(encoding="utf-8"))
    lang = lang_from_path(path)
    path_value = url_path(path)
    text = text.replace("</head>", f"    {head_block(path_value, lang, text)}\n  </head>", 1)
    text = re.sub(r"\n\s*\n\s*<!-- seo-enhance:start -->", "\n      <!-- seo-enhance:start -->", text)
    if path_value in ("/", "/zh-hant/", "/en/", "/ru/") and 'class="guide-section"' not in text:
        text = text.replace('      <section><div class="wrap latest-brief"', guide_section(lang) + '      <section><div class="wrap latest-brief"', 1)
    if re.search(r"/daily/\d{4}-\d{2}-\d{2}/$", path_value) and 'class="related-links"' not in text:
        text = text.replace('      <section class="bonus-band">', related_section(lang) + '      <section class="bonus-band">', 1)
    path.write_text(text, encoding="utf-8")


def alternate_group(path_value):
    date = re.search(r"/daily/(\d{4}-\d{2}-\d{2})/", path_value)
    if date:
        d = date.group(1)
        return {lang: f'{data["daily"]}{d}/' for lang, data in LANGS.items()}
    if path_value.endswith("/daily/"):
        return {lang: data["daily"] for lang, data in LANGS.items()}
    if path_value in [data["home"] for data in LANGS.values()]:
        return {lang: data["home"] for lang, data in LANGS.items()}
    return {}


def write_sitemap():
    paths = sorted(url_path(p) for p in ROOT.glob("**/index.html") if ".git" not in p.parts)
    home_order = {"/": 0, "/zh-hant/": 1, "/en/": 2, "/ru/": 3}
    paths.sort(key=lambda p: (0 if p in home_order else 1, home_order.get(p, 99), p))
    entries = []
    for path_value in paths:
        if "/daily/" in path_value and not re.search(r"/daily/\d{4}-\d{2}-\d{2}/$", path_value) and not path_value.endswith("/daily/"):
            continue
        lastmod = TODAY if path_value in ("/", "/daily/", "/zh-hant/", "/zh-hant/daily/", "/en/", "/en/daily/", "/ru/", "/ru/daily/") or TODAY in path_value else "2026-06-30"
        freq = "daily" if path_value in ("/", "/daily/", "/zh-hant/", "/zh-hant/daily/", "/en/", "/en/daily/", "/ru/", "/ru/daily/") else "monthly"
        priority = "1.0" if path_value == "/" else ("0.9" if path_value in [d["home"] for d in LANGS.values()] or path_value.endswith("/daily/") else "0.72")
        alts = alternate_group(path_value)
        alt_lines = ""
        if alts:
            alt_lines = "\n".join(
                f'    <xhtml:link rel="alternate" hreflang="{LANGS[lang]["html"]}" href="{BASE_URL}{href}" />'
                for lang, href in alts.items()
            )
            alt_lines += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE_URL}{alts["zh-cn"]}" />\n'
        entries.append(
            f"  <url>\n    <loc>{BASE_URL}{path_value}</loc>\n{alt_lines}    <lastmod>{lastmod}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{priority}</priority>\n  </url>"
        )
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    sitemap += "\n".join(entries)
    sitemap += "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")


def main():
    for path in ROOT.glob("**/index.html"):
        if ".git" not in path.parts:
            enhance_html(path)
    write_sitemap()
    print("Enhanced HTML metadata, internal links, structured data and sitemap alternates.")


if __name__ == "__main__":
    main()
