#!/usr/bin/env python3
from pathlib import Path

required = [
    "index.html",
    "zh-hant/index.html",
    "en/index.html",
    "ru/index.html",
    "daily/index.html",
    "zh-hant/daily/index.html",
    "en/daily/index.html",
    "ru/daily/index.html",
    "daily/2026-07-02/index.html",
    "zh-hant/daily/2026-07-02/index.html",
    "en/daily/2026-07-02/index.html",
    "ru/daily/2026-07-02/index.html",
    "daily/2026-07-01/index.html",
    "zh-hant/daily/2026-07-01/index.html",
    "en/daily/2026-07-01/index.html",
    "ru/daily/2026-07-01/index.html",
    "daily/2026-06-29/index.html",
    "zh-hant/daily/2026-06-29/index.html",
    "en/daily/2026-06-29/index.html",
    "ru/daily/2026-06-29/index.html",
    "assets/styles.css",
    "assets/app.js",
    "sitemap.xml",
]

missing = [path for path in required if not Path(path).exists()]
htmls = list(Path(".").glob("**/*.html"))
broken = []

for path in htmls:
    text = path.read_text(encoding="utf-8", errors="ignore")
    checks = [
        "GateAffiliate",
        "VLYQB1HXUW",
        "/assets/styles.css?v=20260701-tg",
        'hreflang="zh-CN"',
        'hreflang="zh-Hant"',
        'hreflang="en"',
        'hreflang="ru"',
    ]
    if any(check not in text for check in checks):
        broken.append(str(path))

sitemap = Path("sitemap.xml").read_text(encoding="utf-8")
expected_urls = 76
if sitemap.count("<url>") != expected_urls:
    broken.append("sitemap.xml:url-count")

if missing or broken:
    print({"missing": missing, "broken": broken})
    raise SystemExit(1)

print(f"Checked {len(htmls)} HTML files and {expected_urls} sitemap URLs successfully.")
