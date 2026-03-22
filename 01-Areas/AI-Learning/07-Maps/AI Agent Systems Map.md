---
title: AI Agent Systems Map
type: map
status: learning
tags:
  - ai/map
  - ai/agent
created: 2026-03-18
updated: 2026-03-22
---

# AI Agent Systems Map

```mermaid
flowchart TD
  A["Agent"] --> B["AI Assistant"]
  A --> C["Coding Agents"]
  B --> D["OpenClaw"]
  C --> D

  D --> D1["Gateway / Control Plane"]
  D --> D2["Channels / Messaging Surfaces"]
  D --> D3["Typed Tools"]
  D --> D4["Sessions / Memory"]
  D --> D5["Canvas / Browser / Nodes / Cron"]
  D --> D6["Local-first / Self-hosted"]

  D3 --> E["browser / exec / process / web / canvas / nodes"]
  D4 --> F["Markdown memory + session source of truth"]
  D2 --> G["WhatsApp / Telegram / Discord / iMessage"]
  D1 --> H["always-on assistant runtime"]
```

## 怎么读这张图

- `Agent` 是抽象能力层：模型 + 工具 + 状态 +执行循环
- `AI Assistant` 是产品层：面向用户的任务完成入口
- `Coding Agents` 是高价值垂直场景：代码理解、修改、测试、反馈循环
- `OpenClaw` 值得学的地方，是它把 agent/assistant/coding-agent 推进到了“系统运行层”

## 推荐顺序

1. [[../06-Topics/Agent|Agent]]
2. [[../06-Topics/AI Assistant|AI Assistant]]
3. [[../06-Topics/Coding Agents|Coding Agents]]
4. [[../06-Topics/OpenClaw|OpenClaw]]
5. [[../06-Topics/OpenClaw 工作原理与架构|OpenClaw 工作原理与架构]]
6. [[../06-Topics/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
7. [[OpenClaw Architecture Map]]
8. [[OpenClaw 准自进化工作流图]]

## 关联

- [[../06-Topics/AI Topics Index|AI Topics Index]]
- [[../06-Topics/Agent|Agent]]
- [[../06-Topics/AI Assistant|AI Assistant]]
- [[../06-Topics/Coding Agents|Coding Agents]]
- [[../06-Topics/OpenClaw 工作原理与架构|OpenClaw 工作原理与架构]]
- [[../06-Topics/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
- [[../06-Topics/OpenClaw、ChatGPT 与 Claude Code 的定位差异|OpenClaw、ChatGPT 与 Claude Code 的定位差异]]
- [[OpenClaw Architecture Map]]
- [[OpenClaw 准自进化工作流图]]
- [[AI Ecosystem Map]]
