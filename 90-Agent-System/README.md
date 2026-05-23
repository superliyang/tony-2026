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
python scripts/agent_ops.py --rounds 2 --mode dry-run
```

`dry-run` 会把中间文件写入系统临时目录中的镜像路径，用于完整验证流水线；不会向仓库写入预览文件，也不会真实发送通知。

`agent_ops.py` 是完整链路巡检入口，会连续运行 Daily / Weekly / Review Queue / Merge Plan / Vault Health，并写入：

```text
90-Agent-System/reports/automation-ops-*.md
```

## 本地真实运行但不通知

```bash
python scripts/knowledge_daily.py --no-notify
python scripts/knowledge_weekly.py --no-notify
python scripts/agent_ops.py --rounds 1 --mode real
```

如果要验证主动推送，可以显式打开通知：

```bash
python scripts/agent_ops.py --rounds 1 --mode real --notify --notify-report
```

## 配置飞书通知

```bash
export FEISHU_WEBHOOK_URL="..."
export FEISHU_WEBHOOK_SECRET="..."
python scripts/knowledge_daily.py
```

同时需要在 `90-Agent-System/notification.yaml` 中将 `feishu.enabled` 设置为 `true`。

也可以把本地密钥放到 `90-Agent-System/.env.local`。该文件被 `.gitignore` 忽略，不会提交到仓库。

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
- `DEEPSEEK_API_KEY`

## AI 语义分析

规则分类会先运行；如果 `90-Agent-System/ai-analysis.yaml` 启用，并且本地或 GitHub Secrets 配置了 `DEEPSEEK_API_KEY`，系统会调用 DeepSeek 为高价值条目补充语义判断。

输出位置：

```text
90-Agent-System/logs/semantic-analysis-YYYY-MM-DD.json
90-Agent-System/logs/semantic-analysis-YYYY-WW.json
00-Agent-Inbox/Review-Queue/AI-Triage/YYYY-WW.md
```

语义分析会补充：

- `learning_value`
- `vault_relationship`
- `suggested_action`
- `reason`
- `confidence`

如果 DeepSeek API 失败，系统会记录 warning，并继续使用规则分类结果。

## 信息源类型

`90-Agent-System/sources.yaml` 当前支持：

- `rss`：RSS / Atom 信息源
- `url`：弱网页抓取
- `github_releases`：GitHub Releases API，配置 `repo: owner/name`

默认已接入：

- AI 官方博客
- AWS / Cloudflare / CISA 安全源
- arXiv AI agent 查询
- LangGraph / LiteLLM / OpenCode release 源

## 飞书 WebSocket Bot

Webhook 只适合主动推送日报/周报。若要接收飞书消息，需要创建飞书自建应用并启用机器人能力，然后使用长连接 WebSocket 事件订阅。

本地配置：

```bash
cp 90-Agent-System/.env.example 90-Agent-System/.env.local
```

在 `.env.local` 中填写：

```bash
FEISHU_APP_ID="..."
FEISHU_APP_SECRET="..."
```

然后把 `90-Agent-System/feishu-bot.yaml` 里的 `websocket_bot.enabled` 改成 `true`，运行：

```bash
scripts/bootstrap_agent_env.sh
scripts/run_feishu_bot.sh --dry-run
scripts/run_feishu_bot.sh
```

如果你想指定 Conda 或其他 Python：

```bash
PYTHON_BIN="$(which python3)" scripts/bootstrap_agent_env.sh
PYTHON_BIN="$(which python3)" scripts/run_feishu_bot.sh
```

也可以直接运行：

```bash
python scripts/feishu_bot_ws.py --dry-run
python scripts/feishu_bot_ws.py
```

## 一键本地服务

macOS 推荐使用 `launchd` 托管服务：

```bash
scripts/launchd_agent.sh doctor
scripts/launchd_agent.sh install
scripts/launchd_agent.sh status
scripts/launchd_agent.sh logs
```

这会安装三项服务：

- `com.tony2026.knowledge-feishu-bot`：飞书 WebSocket bot 常驻运行
- `com.tony2026.knowledge-daily`：每天 08:30 生成日报
- `com.tony2026.knowledge-weekly`：每周一 09:00 生成周报

常用管理命令：

```bash
scripts/launchd_agent.sh restart
scripts/launchd_agent.sh stop
scripts/launchd_agent.sh start
scripts/launchd_agent.sh uninstall
```

日志写入：

```text
90-Agent-System/logs/launchd/
```

如果 vault 放在 `~/Documents`、`~/Desktop` 或 `~/Downloads` 下，macOS 可能阻止 `launchd` 访问目录，日志里会出现 `Operation not permitted`。处理方式：

```bash
scripts/launchd_agent.sh privacy
```

然后在 Full Disk Access 中添加并启用：

- `/bin/bash`
- `/usr/bin/python3`

授权后重新运行：

```bash
scripts/launchd_agent.sh install
```

如果不想处理 macOS 隐私授权，也可以把 vault 移到 `~/Developer/tony2026` 这类非保护目录后重新安装服务。

第一版支持命令：

- `/ping`
- `/daily`
- `/weekly`
- `/health`
- `/review`
- `/decide <编号> study|ignore|keep|merge`
- `/run daily`
- `/run weekly`

也支持更短的自然语言命令：

- `日报`
- `周报`
- `健康`
- `候选`
- `1 学习`
- `2 忽略`
- `3 保留`
- `4 合入`
- `合入计划`
- `巡检`
- `真实巡检`
- `跑日报`
- `跑周报`

Review Queue 是这套 Agent First 工作流的人工决策入口：

- `/review`：列出当前最需要你决策的候选卡片，并生成 `00-Agent-Inbox/Review-Queue/YYYY-MM-DD.md`
- `/decide <编号> study`：把候选标记为 `queued-for-study`
- `/decide <编号> ignore`：把候选标记为 `discarded`
- `/decide <编号> keep`：继续保留 `pending-review`
- `/decide <编号> merge`：标记为 `ready-to-merge`，等待 Curator Agent 半自动合入

短命令等价写法：

- `1 学习` 等价于 `/decide 1 study`
- `2 忽略` 等价于 `/decide 2 ignore`
- `3 保留` 等价于 `/decide 3 keep`
- `4 合入` 等价于 `/decide 4 merge`

当候选被标记为 `ready-to-merge` 后，可以发送：

- `合入计划`
- `/merge-plan`

系统会生成 `00-Agent-Inbox/Review-Queue/Merge-Plans/YYYY-MM-DD.md`，列出目标专题、建议检查文件和人工确认点。第一版只生成计划，不自动修改 `01-Areas/`。

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
