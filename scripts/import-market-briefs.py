#!/usr/bin/env python3
from pathlib import Path
import html
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "hyperliquid-referral-site" / "market-briefing"
BASE_URL = "https://gate-referral-site.pages.dev"
CODE = "VLYQB1HXUW"
STYLE_VERSION = "20260630-gate-blue"

DATES = sorted([p.name for p in SOURCE.iterdir() if p.is_dir() and re.match(r"2026-\d\d-\d\d$", p.name)])


def read(path):
    return path.read_text(encoding="utf-8")


def meta(content, name):
    match = re.search(rf'<meta name="{re.escape(name)}" content="([^"]*)"', content)
    return html.unescape(match.group(1)) if match else ""


def title(content):
    match = re.search(r"<title>(.*?)</title>", content)
    return html.unescape(match.group(1)) if match else "GateAffiliate Daily Market Brief"


def extract_between(content, start_pat, end_pat):
    start = re.search(start_pat, content)
    end = re.search(end_pat, content)
    if not start or not end:
        raise ValueError("Cannot extract page body")
    return content[start.start():end.start()]


def rewrite_fragment(fragment):
    replacements = {
        "/market-briefing/images/": "/daily/images/",
        "/market-briefing/": "/daily/",
        "HLBESTCODE": CODE,
        "Use HLBESTCODE": f"Use {CODE}",
        "使用 HLBESTCODE": f"使用 {CODE}",
        "Join Hyperliquid": "Join Gate",
        "加入 Hyperliquid": "注册 Gate",
        "Open Hyperliquid": "Open Gate",
        "Hyperliquid referral": "Gate affiliate",
        "Hyperliquid Referral": "Gate Affiliate",
    }
    for old, new in replacements.items():
        fragment = fragment.replace(old, new)
    fragment = re.sub(r'href="/daily/(\d{4}-\d{2}-\d{2})/en/"', r'href="/daily/\1/en/"', fragment)
    fragment = re.sub(r'href="/daily/(\d{4}-\d{2}-\d{2})/"', r'href="/daily/\1/"', fragment)
    fragment = fragment.replace('href="/hype-market-brief/"', 'href="/daily/"')
    return fragment


def header(active="daily"):
    return f'''<header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">
          <span class="brand-mark"><img src="/assets/gate-logo.ico" alt="GateAffiliate logo"></span>
          <span>GateAffiliate</span>
        </a>
        <div class="nav-links">
          <a href="/#invite">邀请码</a>
          <a href="/#steps">注册步骤</a>
          <a href="/#seo">Affiliate SEO</a>
          <a href="/daily/">每日市场日报</a>
          <a href="/#faq">FAQ</a>
          <a class="button button-primary" data-invite href="#">使用邀请码注册</a>
        </div>
      </nav>
    </header>'''


def footer():
    return '''<footer>
      <div class="footer-inner">
        <span>GateAffiliate market commentary is for information only and is not financial advice.</span>
        <div class="footer-links">
          <a href="/">GateAffiliate</a>
          <a href="/daily/">Daily briefs</a>
          <a data-official href="#">Gate affiliate program</a>
        </div>
      </div>
    </footer>'''


def page(date, lang):
    src = SOURCE / date / ("en/index.html" if lang == "en" else "index.html")
    content = read(src)
    raw_title = title(content)
    raw_desc = meta(content, "description")
    page_title = raw_title.replace("Hyperliquid HYPE Market Brief", "GateAffiliate Daily Market Brief")
    page_title = page_title.replace("Hyperliquid HYPE 市場簡報", "GateAffiliate 每日市場日報")
    page_desc = raw_desc.replace("Hyperliquid HYPE market brief", "GateAffiliate daily market brief")
    page_desc = page_desc.replace("Hyperliquid HYPE 市場簡報", "GateAffiliate 每日市場日報")
    lang_attr = "en" if lang == "en" else "zh-Hant"
    slug = f"/daily/{date}/en/" if lang == "en" else f"/daily/{date}/"
    image_match = re.search(r'<meta property="og:image" content="https://hyperliquidreferral\.com/market-briefing/images/([^"]+)"', content)
    image = f"{BASE_URL}/daily/images/{image_match.group(1)}" if image_match else f"{BASE_URL}/assets/hero.png"
    hero_and_main = extract_between(content, r"<section class=\"hero\">", r"</main>")
    hero_and_main += "</main>"
    hero_and_main = rewrite_fragment(hero_and_main)
    hero_and_main = hero_and_main.replace("Hyperliquid HYPE Market Brief", "GateAffiliate Daily Market Brief")
    hero_and_main = hero_and_main.replace("Hyperliquid HYPE 市場簡報", "GateAffiliate 每日市場日報")
    schema = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": page_title,
        "description": page_desc,
        "datePublished": date,
        "dateModified": date,
        "author": {"@type": "Organization", "name": "GateAffiliate"},
        "publisher": {
            "@type": "Organization",
            "name": "GateAffiliate",
            "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/assets/gate-logo.ico"},
        },
        "image": image,
        "mainEntityOfPage": f"{BASE_URL}{slug}",
    }
    alternates = f'''<link rel="alternate" hreflang="zh-Hant" href="{BASE_URL}/daily/{date}/">
    <link rel="alternate" hreflang="en" href="{BASE_URL}/daily/{date}/en/">
    <link rel="alternate" hreflang="x-default" href="{BASE_URL}/daily/{date}/">'''
    return f'''<!doctype html>
<html lang="{lang_attr}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(page_title)}</title>
    <meta name="description" content="{html.escape(page_desc)}">
    <meta name="robots" content="index,follow,max-image-preview:large">
    <link rel="canonical" href="{BASE_URL}{slug}">
    {alternates}
    <meta property="og:type" content="article">
    <meta property="og:title" content="{html.escape(page_title)}">
    <meta property="og:description" content="{html.escape(page_desc)}">
    <meta property="og:image" content="{image}">
    <meta property="og:site_name" content="GateAffiliate">
    <meta property="og:url" content="{BASE_URL}{slug}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="theme-color" content="#07102b">
    <link rel="icon" href="/assets/gate-logo.ico" type="image/x-icon">
    <link rel="preload" as="image" href="{image.replace(BASE_URL, '')}">
    <link rel="stylesheet" href="/assets/styles.css?v={STYLE_VERSION}">
    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
  </head>
  <body>
    {header()}
    {hero_and_main}
    {footer()}
    <script src="/assets/app.js?v={STYLE_VERSION}"></script>
  </body>
</html>
'''


def daily_index():
    cards = []
    for date in reversed(DATES):
        zh = read(SOURCE / date / "index.html")
        en = read(SOURCE / date / "en" / "index.html")
        h1_match = re.search(r"<h1>(.*?)</h1>", zh)
        h1 = html.unescape(re.sub("<.*?>", "", h1_match.group(1))) if h1_match else f"{date} 市场日报"
        desc = meta(zh, "description").replace("Hyperliquid HYPE 市場簡報", "GateAffiliate 每日市場日報")
        en_desc = meta(en, "description").replace("Hyperliquid HYPE market brief", "GateAffiliate daily market brief")
        cards.append(f'''<a class="history-link" href="/daily/{date}/">
              <span class="history-date">{date}</span>
              <span>
                <span class="history-title">{html.escape(h1)}</span>
                <span class="history-summary">{html.escape(desc[:130])}</span>
              </span>
              <span class="history-tag">中文</span>
            </a>
            <a class="history-link" href="/daily/{date}/en/">
              <span class="history-date">{date}</span>
              <span>
                <span class="history-title">{html.escape(title(en).replace("Hyperliquid HYPE Market Brief", "GateAffiliate Daily Market Brief"))}</span>
                <span class="history-summary">{html.escape(en_desc[:130])}</span>
              </span>
              <span class="history-tag">EN</span>
            </a>''')
    return f'''<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>GateAffiliate 每日市场日报 | Gate 返佣自然流量内容库</title>
    <meta name="description" content="GateAffiliate 每日市场日报目录，覆盖 BTC、ETH、AI 半导体、宏观、热门交易情绪与 Gate affiliate 返佣站自然流量内容沉淀。">
    <meta name="robots" content="index,follow,max-image-preview:large">
    <link rel="canonical" href="{BASE_URL}/daily/">
    <meta property="og:type" content="website">
    <meta property="og:title" content="GateAffiliate 每日市场日报">
    <meta property="og:description" content="持续更新的 GateAffiliate 市场日报内容库，用于自然流量、内部链接和返佣转化。">
    <meta property="og:image" content="{BASE_URL}/assets/hero.png">
    <meta name="theme-color" content="#07102b">
    <link rel="stylesheet" href="/assets/styles.css?v={STYLE_VERSION}">
    <link rel="icon" href="/assets/gate-logo.ico" type="image/x-icon">
  </head>
  <body>
    {header()}
    <section class="hero">
      <div class="hero-inner">
        <span class="eyebrow">GateAffiliate daily market brief</span>
        <h1>GateAffiliate 每日市场日报内容库</h1>
        <p class="hero-copy">这里沉淀每日市场主线、宏观风险、热门资产与交易情绪。内容为 Gate affiliate 返佣站提供持续更新的自然流量入口，同时把读者引导到邀请码 {CODE}。</p>
        <div class="hero-actions">
          <a class="button button-primary" href="/daily/{DATES[-1]}/">阅读最新中文日报</a>
          <a class="button button-secondary" href="/daily/{DATES[-1]}/en/">Latest English brief</a>
        </div>
      </div>
    </section>
    <main>
      <section id="history">
        <div class="wrap">
          <div class="section-head">
            <h2>历史日报</h2>
            <p>已迁移参考站的历史日报内容，并统一为 GateAffiliate 蓝色视觉、内部链接和 SEO 结构。</p>
          </div>
          <div class="history-list">
            {''.join(cards)}
          </div>
        </div>
      </section>
    </main>
    {footer()}
    <script src="/assets/app.js?v={STYLE_VERSION}"></script>
  </body>
</html>
'''


def sitemap():
    urls = [
        ("/", "daily", "1.0"),
        ("/daily/", "daily", "0.9"),
    ]
    for date in DATES:
        urls.append((f"/daily/{date}/", "monthly", "0.75"))
        urls.append((f"/daily/{date}/en/", "monthly", "0.7"))
    body = "\n".join(
        f"  <url>\n    <loc>{BASE_URL}{loc}</loc>\n    <lastmod>2026-06-30</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{priority}</priority>\n  </url>"
        for loc, freq, priority in urls
    )
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
'''


def main():
    image_dest = ROOT / "daily" / "images"
    image_dest.mkdir(parents=True, exist_ok=True)
    for image in (SOURCE / "images").glob("*"):
        if image.is_file():
            shutil.copy2(image, image_dest / image.name)
    for date in DATES:
        zh_dir = ROOT / "daily" / date
        en_dir = zh_dir / "en"
        zh_dir.mkdir(parents=True, exist_ok=True)
        en_dir.mkdir(parents=True, exist_ok=True)
        (zh_dir / "index.html").write_text(page(date, "zh"), encoding="utf-8")
        (en_dir / "index.html").write_text(page(date, "en"), encoding="utf-8")
    (ROOT / "daily" / "index.html").write_text(daily_index(), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    print(f"Imported {len(DATES)} dates, {len(DATES) * 2} pages.")


if __name__ == "__main__":
    main()
