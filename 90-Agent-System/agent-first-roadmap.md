---
title: Agent First Knowledge Automation Roadmap
type: system-roadmap
status: active
updated: 2026-05-23
---

# Agent First Knowledge Automation Roadmap

## 目标状态

这套系统的目标不是“用户想到主题后让 AI 整理”，而是：

1. Agent 每天 / 每周自动巡检外部世界
2. 自动发现值得学习的主题
3. 自动放入候选池和 Review Queue
4. 汇总推送到飞书
5. 用户在飞书里选择候选内容去向
6. Curator Agent 在人工确认后半自动合入正式专题

正式知识区 `01-Areas/` 仍然保持人工确认边界。自动化默认只写入 `00-Agent-Inbox/` 和 `90-Agent-System/`。

## 当前已实现

- RSS / URL 采集：`scripts/collect_sources.py`
- 规则分类与重要性评分：`scripts/classify_items.py`
- DeepSeek 语义分析：`scripts/semantic_analyze.py`
- Daily Digest：`scripts/generate_digest.py --mode daily`
- Weekly Digest：`scripts/generate_digest.py --mode weekly`
- Candidate Notes：`scripts/generate_candidates.py`
- Study Queue：`scripts/generate_study_queue.py`
- Review Queue：`scripts/review_queue.py`
- Curator Merge Plan：`scripts/curator_merge_plan.py`
- Vault Health Report：`scripts/check_vault.py`
- Automation Ops Run：`scripts/agent_ops.py`
- 飞书 Webhook 主动推送：`scripts/notify_feishu.py`
- 飞书 WebSocket Bot 交互入口：`scripts/feishu_bot_ws.py`
- GitHub Actions 定时运行脚手架：`.github/workflows/`

## 能力分层

### 1. 调度层

当前主力：

- 本地手动命令
- GitHub Actions
- macOS `launchd` 本地服务：`scripts/launchd_agent.sh`
- 多轮自动化巡检：`scripts/agent_ops.py`

后续可视化调度层：

- `n8n`：适合可视化流程、失败记录、跨服务集成
- `Windmill`：适合把 Python / TypeScript 脚本产品化为 workflow、webhook、内部工具
- `Activepieces`：适合 AI-first / no-code 工作流

第一阶段仍以 Python 脚本为主，避免过早把核心逻辑散进平台节点里。

### 2. 信息源层

当前主力：

- OpenAI / Anthropic / AWS / Cloudflare / Flink RSS
- 弱 URL 抓取
- GitHub Releases：LangGraph / LiteLLM / OpenCode
- arXiv AI agent 查询
- CISA 安全情报 RSS

后续增强：

- GitHub Trending
- OWASP / Security advisories
- 手动收藏 URL Inbox
- PDF / OCR / Screenshot 来源

### 3. AI 分析层

当前主力：

- 规则分类
- 规则重要性评分
- DeepSeek 语义分析增强

后续增强：

- OpenAI 语义分类备选 provider
- 候选内容和现有 vault 的关系判断
- 向量检索已有笔记
- 自动识别“该进哪个专题 / 哪张地图 / 哪个 playbook”

### 4. 结构化产物层

当前主力：

- Daily Digest
- Weekly Digest
- Candidate Notes
- Study Queue
- Review Queue
- AI Triage Report
- Curator Merge Plan
- Vault Health Report

后续增强：

- Topic Opportunity Report
- Source Quality Report
- Learning Debt Report
- Curator Merge Execution

### 5. 人工决策层

当前主力：

- 飞书命令 `/review`
- 飞书命令 `/decide <编号> study|ignore|keep|merge`
- 飞书命令 `合入计划`
- 飞书命令 `巡检` / `真实巡检`

状态含义：

- `pending-review`：候选池等待人工判断
- `queued-for-study`：进入学习队列
- `discarded`：忽略
- `ready-to-merge`：准备交给 Curator Agent 半自动合入

### 6. 正式合入层

当前边界：

- 不自动修改 `01-Areas/`

后续 Curator Agent 合入时必须：

- 读取相关专题 `专题总览.md`
- 判断是否更新 `学习进度.md`
- 判断是否更新 `恢复笔记.md`
- 判断是否更新地图索引 / 主题索引
- 运行 `check_vault.py`
- 生成 Git commit / PR

## 推荐下一步

1. 观察 `agent_ops.py` 多轮巡检报告，沉淀失败趋势和质量指标。
2. 观察 DeepSeek 语义分析一周，调优 prompt 和 Review Queue 策略。
3. 增加 GitHub Trending / Security Advisory / 手动收藏 URL Inbox。
4. 实现 `ready-to-merge` 候选的 Curator Merge Execution，但默认仍需人工确认。
5. 稳定两周后，再评估是否把调度层迁移到 n8n 或 Windmill。
