---
title: OpenClaw
type: system
status: learning
tags:
  - ai/topic
  - ai/system
  - ai/agent
  - ai/assistant
  - ai/openclaw
created: 2026-03-18
updated: 2026-03-22
---

# OpenClaw

## 这个主题是什么

`OpenClaw` 是一个自托管 `self-hosted` 的个人 AI assistant / agent gateway。你可以把它理解成：它不是单纯的聊天产品，也不只是一个“会调工具的 prompt”，而是一套长期在线、跨消息渠道、带工具、带会话、带记忆、带自动化的 agent 运行时系统。

官方 GitHub README 把它描述为“你运行在自己设备上的 personal AI assistant”，而官方文档强调它通过一个长期运行的 `Gateway` 连接 WhatsApp、Telegram、Discord、iMessage 等消息渠道，并把这些入口接到 AI agent 上。

## 为什么它值得学

如果你已经理解了 `Agent`、`AI Assistant`、`Coding Agents` 这些概念，那么 `OpenClaw` 值得学的地方在于：它把这些概念推进到了“真正可运行的系统层”。

它让你看到：

- agent 不只是模型调用循环，而是一个长期在线的 control plane
- assistant 不只是聊天界面，而是跨渠道、跨设备的工作入口
- coding agent 不只是 IDE 插件，而可以嵌入更大的消息与自动化系统中
- 真正的 agent 系统必须处理会话、记忆、工具权限、设备能力和远程接入

## 如果你想继续挖“它到底怎么跑起来”

建议直接接着看：

- [[OpenClaw 工作原理与架构]]
- [[OpenClaw 的准自进化工作流]]
- [[OpenClaw、ChatGPT 与 Claude Code 的定位差异]]
- [[../07-Maps/OpenClaw Architecture Map|OpenClaw Architecture Map]]
- [[../07-Maps/OpenClaw 准自进化工作流图|OpenClaw 准自进化工作流图]]

这两页会把它拆到：

- `Gateway` 为什么像 control plane
- `workspace + memory + sessions` 为什么是系统基础设施
- `heartbeat / hooks / cron` 为什么让它更像长期在线 agent runtime
- 你听到的“自进化”在官方语境里最接近什么
- 它和 `ChatGPT`、`Claude Code` 这些更熟悉的产品到底差在哪

如果你想把这些问题继续抽象成工程知识，而不是只停留在 `OpenClaw` 这个具体系统上，再读：

- [[../../AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../../AI-Engineering/07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]

## 先抓住它的 6 个关键点

### 1. Gateway 是核心

官方架构文档里，`Gateway` 是单个长期运行的控制平面。它负责拥有消息渠道、维护 provider 连接、处理控制端客户端、以及接收节点能力。

你可以把它理解为：

- 聊天入口汇聚层
- agent 运行控制层
- 会话与状态事实来源 `source of truth`
- 设备能力与自动化的协调层

### 2. 它是“渠道化 assistant”而不只是网页聊天

`OpenClaw` 最大的产品差异之一是：它不是把 agent 限制在一个网页对话框里，而是把 agent 接到你已经在用的消息面上，例如 WhatsApp、Telegram、Discord、iMessage 等。

这意味着它更像“随时能被你叫到的 AI 助手”，而不是一个必须打开某个站点才存在的产品。

### 3. 工具系统是第一公民

官方 tools 文档强调，`OpenClaw` 暴露的是 typed、first-class tools，而不是老式 shell skill 的临时拼接。它内建的能力包括：

- `exec` / `process`
- `browser`
- `canvas`
- `nodes`
- `cron`
- `web_search` / `web_fetch`
- `sessions_*`
- `memory_*`

这说明它不是“一个大模型 + 一堆 prompt tricks”，而是把工具调用当成 agent runtime 的正式能力面。

### 4. 会话和记忆是系统能力，不是附属功能

官方 session 文档强调：会话状态由 gateway 持有，UI 客户端不能自己乱读本地文件当真相来源。

官方 memory 文档又说明：`OpenClaw` 的记忆默认就是 workspace 里的 Markdown 文件，例如：

- `MEMORY.md`
- `memory/YYYY-MM-DD.md`

同时它还提供 `memory_search` 和 `memory_get`。这很值得学，因为它代表了一种很实用的 agent 记忆观：

- durable memory 写入文件
- recall 通过工具做
- 模型“记住”的前提，是它真的把内容写下来了

### 5. 它把 agent 系统做成了“本地优先 + 可远程接入”

官方 onboarding 和架构文档都提到：你可以本地跑 gateway，也可以远程接入；可以通过 CLI、dashboard、app 和自动化系统连接它。

所以它很适合作为一个案例来理解：

- local-first AI assistant
- remote control plane
- agent runtime + ops
- personal agent infrastructure

### 6. 它特别适合拿来研究“Agent 产品化”

很多 agent 项目停在 demo 层：会拆任务、会调工具、会跑浏览器。

`OpenClaw` 更值得学的地方在于，它逼你思考产品与系统问题：

- 用户从哪里与 agent 交互
- 会话如何跨渠道延续
- 权限和安全如何控制
- 记忆怎么存、怎么检索
- 长期运行如何维护
- 自动化和 heartbeat / cron 如何接入

## 和 ChatGPT / 通用 assistant 的差别

一个很粗的理解方式是：

- `ChatGPT` 更像 cloud-hosted 通用 assistant
- `OpenClaw` 更像 self-hosted personal agent runtime

这不意味着它“更强”，而是它关心的问题不同：

- 更关心渠道与入口
- 更关心本地数据与控制权
- 更关心工具、设备、节点和自动化接入
- 更像一个“AI assistant operating system”而不是单个聊天产品

## 关于你可能听到的“自进化”

这里要说准一点：

- 按官方文档，`OpenClaw` 并没有把自己的核心机制正式命名成 `self-evolving agent`
- 更接近这个说法的，是它支持 agent 持续写入 memory、改 workspace 文件、再通过 `hooks`、`heartbeat`、`cron` 继续运行
- 所以更准确的理解是：它具备“可持续自运转 / 可配置自调整 / 准自我迭代工作流”的能力

如果你想系统搞懂这一点，继续读 [[OpenClaw 工作原理与架构]]。

如果你想专门看“这个循环是怎么形成的”，继续读 [[OpenClaw 的准自进化工作流]]。

## 从 AI Agent 学习角度，最值得研究的几个问题

1. 为什么 `Gateway` 这种 control-plane 架构对 agent 产品很重要
2. `OpenClaw` 为什么把会话和记忆看成基础设施，而不是产品细节
3. 工具 allow / deny、profile、节点权限这些机制，如何影响 agent 安全性
4. 为什么跨消息渠道的 assistant 比单一网页聊天更接近真实个人助理
5. `OpenClaw` 应该被理解成一个 agent、一个 assistant，还是一个 agent runtime 平台
6. 它和 `Coding Agents`、`Claude Code` 这类 developer-facing agent 的边界在哪里

## 你可以怎么学它

推荐顺序：

1. 先读 [[Agent]]
2. 再读 [[AI Assistant]]
3. 再读 [[Coding Agents]]
4. 然后进入 [[OpenClaw]]
5. 再读 [[OpenClaw 工作原理与架构]]
6. 再读 [[OpenClaw 的准自进化工作流]]
7. 最后回到 [[../07-Maps/AI Agent Systems Map|AI Agent Systems Map]] 看它在整个 agent 生态中的位置

## 关联

- [[Agent]]
- [[AI Assistant]]
- [[Coding Agents]]
- [[Developer Tools]]
- [[API Economy]]
- [[OpenClaw 工作原理与架构]]
- [[OpenClaw 的准自进化工作流]]
- [[OpenClaw、ChatGPT 与 Claude Code 的定位差异]]
- [[../07-Maps/AI Agent Systems Map|AI Agent Systems Map]]
- [[../07-Maps/OpenClaw Architecture Map|OpenClaw Architecture Map]]
- [[../07-Maps/OpenClaw 准自进化工作流图|OpenClaw 准自进化工作流图]]
- [[../../AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../../AI-Engineering/07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]

## 资料

- 官方 GitHub: [openclaw/openclaw](https://github.com/openclaw/openclaw)
- 官方文档首页: [OpenClaw Docs](https://docs.openclaw.ai/)
- 官方架构: [Gateway Architecture](https://docs.openclaw.ai/concepts/architecture)
- 官方工具文档: [Tools](https://docs.openclaw.ai/tools)
- 官方会话文档: [Session Management](https://docs.openclaw.ai/sessions)
- 官方记忆文档: [Memory](https://docs.openclaw.ai/concepts/memory)
- 官方 onboarding: [Onboarding (CLI)](https://docs.openclaw.ai/start/wizard)
