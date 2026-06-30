# GateAffiliate Site

Gate affiliate 返佣自然流量网站，邀请码：`VLYQB1HXUW`。

## 语言结构

- 简体中文：`/`
- 繁体中文：`/zh-hant/`
- English：`/en/`
- Русский：`/ru/`

日报也同步为四种语言，例如：

- `/daily/2026-06-29/`
- `/zh-hant/daily/2026-06-29/`
- `/en/daily/2026-06-29/`
- `/ru/daily/2026-06-29/`

## 本地预览

```bash
npm start
```

然后打开 `http://localhost:4173`。

## 每天更新日报

1. 四种语言都要新增对应日期页面。
2. 简体中文放在 `daily/YYYY-MM-DD/`。
3. 繁体中文放在 `zh-hant/daily/YYYY-MM-DD/`。
4. 英文放在 `en/daily/YYYY-MM-DD/`。
5. 俄语放在 `ru/daily/YYYY-MM-DD/`。
6. 同步更新四种语言的日报目录和 `sitemap.xml`。
7. 提交并推送到 GitHub，GitHub Pages 会自动部署。

当前项目保留了 `scripts/import-market-briefs.py`，可从参考站批量重新生成四语言历史日报。

首次运行迁移脚本前安装依赖：

```bash
python3 -m pip install -r requirements.txt
```

## 重要说明

页面里的注册按钮指向 Gate 官方注册入口，并带有邀请码参数。奖励、返佣、affiliate 资格和活动门槛以 Gate 官方页面当前规则为准。
