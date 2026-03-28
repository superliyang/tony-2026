---
title: Codex
type: system
status: learning
tags:
  - ai/system
  - ai/agent
  - ai/product
  - ai/coding-agent
  - organization/openai
created: 2026-03-22
updated: 2026-03-28
---

# Codex

## 简介

`Codex` 在当前 OpenAI 官方语境里，不再只是早期的代码模型名字，也是一套面向软件工程的 `coding agent` 系统与产品面。

现在它已经至少有几层：

- `Codex` cloud task agent
- `Codex CLI`
- IDE extension
- `Codex app`
- `Codex harness / App Server`
- API 侧的 `shell`、`local_shell`、`computer_use`、`remote_mcp`

## 为什么重要

- 它代表了 `coding agent` 从“IDE 里配对写代码”继续走向“可委托、可并行、可后台运行”的方向
- 它把 OpenAI 的 agent 竞争点推进到了 `skills + automations + app server + connectors`
- 它特别适合拿来理解 `Harness Engineering` 为什么正在成为平台分水岭

## 官方定位里最值得记住的点

- OpenAI 把它定义成面向软件工程任务的 `agent`
- `Codex app` 被定位成 `command center for agents`
- app / CLI / IDE extension / cloud 共用配置与会话能力
- app 里直接强调了 `skills`、worktrees、automations、background work
- OpenAI 还公开了 `Harness Engineering` 与 `App Server` 文章，说明它背后不只是 tool use，而是 richer runtime surface

## 关键能力面

### 1. 多入口

Codex 已经不是单点入口，而是：

- CLI
- IDE extension
- app
- cloud tasks

### 2. Skills

`Codex app` 官方文章明确说：

- app 包含 skills library
- skills bundle instructions、resources、scripts
- 既可以显式调用，也可以自动按任务触发

这说明 OpenAI 已经把 `skills` 做成了一等产品能力。

### 3. Automations

官方文章也明确提到：

- 正在建设 `Automations`
- 支持 cloud-based triggers
- 支持 background continuous work

这意味着 Codex 不只是“你打开终端时才工作”，而是在走向持续运行工作流。

### 4. Shell / Local Shell / Computer Use / Remote MCP

OpenAI 平台文档已经把这些动作面拆开：

- `shell`
- `local_shell`
- `computer_use`
- `remote_mcp`

这非常典型地体现了 harness 视角：

- 不同任务需要不同动作面
- action surface 不是单一 function call

### 5. App Server

OpenAI 专门公开了如何构建 `Codex harness` 的 `App Server`。

这说明 Codex 的关键不只是模型能力，而是：

- task / thread / event
- artifact / diff
- approvals
- reconnect / resume
- multi-agent supervision

## 它最值得学的地方

如果用一句话总结：

`Codex` 最值得学的，不只是“会写代码”，而是“OpenAI 如何把 coding harness 做成 multi-agent product”。

## 它和 Claude Code 的差异

- `Claude Code` 更偏 terminal-first、repo-local loop、commands / hooks / subagents
- `Codex` 更偏 cloud task operator、app-level supervision、skills / automations / app server

## 它和 OpenClaw 的差异

- `Codex` 主要解决软件工程任务委托
- `OpenClaw` 更像自托管 personal agent runtime

## 什么时候优先研究它

- 你想看 OpenAI 对 multi-agent coding 的产品答案
- 你想研究 `skills + automations + app server` 如何一起工作
- 你想研究 apps/connectors 和 coding harness 如何衔接

## 推荐继续往下读

- [[Claude Code]]
- [[OpenClaw]]
- [[Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/App Server 与 Rich Agent Protocols|App Server 与 Rich Agent Protocols]]
- [[../../AI-Engineering/07-Topics/技能、插件、应用与自动化：Harness 的扩展面|技能、插件、应用与自动化：Harness 的扩展面]]

## 相关

- [[ChatGPT Agent]]
- [[OpenAI API]]
- [[Claude Code]]
- [[Cursor]]
- [[Devin]]
- [[AI Coding Agent Systems 对比：Claude Code、Codex、Cursor、Devin]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/App Server 与 Rich Agent Protocols|App Server 与 Rich Agent Protocols]]

## 官方资料

- [Codex](https://openai.com/codex/)
- [Introducing Codex](https://openai.com/index/introducing-codex/)
- [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [Codex GA](https://openai.com/index/codex-now-generally-available/)
- [Harness Engineering](https://openai.com/index/harness-engineering/)
- [Unlocking the Codex harness: how we built the App Server](https://openai.com/index/unlocking-the-codex-harness/)
- [Shell](https://platform.openai.com/docs/guides/tools-shell)
- [Local shell](https://platform.openai.com/docs/guides/tools-local-shell)
- [Computer use](https://platform.openai.com/docs/guides/tools-computer-use)
- [Building MCP servers for ChatGPT and API integrations](https://platform.openai.com/docs/mcp/)
