# Agent Knowledge Automation

## 目标

本目录用于管理知识库自动化系统。

第一版自动生成：

- Daily Digest
- Weekly Digest
- Candidate Notes
- Study Queue
- Vault Health Report

第一版不会自动修改 `01-Areas/`。

## 本地 dry-run

```bash
python scripts/knowledge_daily.py --dry-run
python scripts/knowledge_weekly.py --dry-run
```

`dry-run` 会把中间文件写入系统临时目录中的镜像路径，用于完整验证流水线；不会向仓库写入预览文件，也不会真实发送通知。

## 本地真实运行但不通知

```bash
python scripts/knowledge_daily.py --no-notify
python scripts/knowledge_weekly.py --no-notify
```

## 配置飞书通知

```bash
export FEISHU_WEBHOOK_URL="..."
export FEISHU_WEBHOOK_SECRET="..."
python scripts/knowledge_daily.py
```

同时需要在 `90-Agent-System/notification.yaml` 中将 `feishu.enabled` 设置为 `true`。

## 配置企业微信通知

```bash
export WECOM_WEBHOOK_URL="..."
python scripts/notify_wecom.py --file 00-Agent-Inbox/Daily-Digests/YYYY-MM-DD.md
```

同时需要在 `90-Agent-System/notification.yaml` 中将 `wecom.enabled` 设置为 `true`。

## GitHub Actions Secrets

- `FEISHU_WEBHOOK_URL`
- `FEISHU_WEBHOOK_SECRET`
- `WECOM_WEBHOOK_URL`
- `BARK_ENDPOINT`

## 输出目录

- `00-Agent-Inbox/Daily-Digests`
- `00-Agent-Inbox/Weekly-Digests`
- `00-Agent-Inbox/Candidates`
- `00-Agent-Inbox/Study-Queue`
- `90-Agent-System/reports`
- `90-Agent-System/logs`

## 安全边界

- 第一版不会自动修改 `01-Areas/`
- 所有外部信息只进入 Inbox
- 正式合入需要人工 review
- 不修改 `.obsidian/*`
- 不修改 `.p_obsidian/*`
- Webhook URL 只从环境变量读取，不写入仓库

## 可移植性

这套自动化是仓库内自包含的轻量系统。迁移到其他 Obsidian vault 时，通常需要带走：

- `00-Agent-Inbox/`
- `90-Agent-System/`
- `scripts/`
- `.github/workflows/`
- `requirements.txt`

然后按新 vault 的专题名调整 `90-Agent-System/topic-router.yaml` 和 `90-Agent-System/sources.yaml`。
