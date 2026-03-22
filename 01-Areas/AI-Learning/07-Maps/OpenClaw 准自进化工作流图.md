---
title: OpenClaw 准自进化工作流图
type: map
status: learning
tags:
  - ai/map
  - ai/openclaw
  - ai/automation
  - ai/memory
created: 2026-03-22
updated: 2026-03-22
---

# OpenClaw 准自进化工作流图

```mermaid
flowchart TD
  A["User Message / External Event"] --> B["Gateway Session"]
  H["Heartbeat"] --> B
  I["Cron Job"] --> B

  B --> C["Agent Runtime"]
  C --> D["Workspace Files"]
  C --> E["Memory Files"]
  C --> F["Typed Tools"]

  D --> D1["AGENTS.md / SOUL.md / TOOLS.md"]
  D --> D2["BOOT.md / HEARTBEAT.md"]
  E --> E1["MEMORY.md"]
  E --> E2["memory/YYYY-MM-DD.md"]

  C --> G["Action / Reply / File Update"]
  G --> E
  G --> D

  J["Hooks"] --> E
  J --> D
  B --> J

  D --> K["Next Turn Reads Updated Context"]
  E --> K
  K --> B
```

## 怎么读这张图

- heartbeat 和 cron 都可以唤醒一次新的 agent turn
- 每次 turn 都不是从零开始，而是读入已经变化过的 workspace 与 memory
- hooks 会在某些事件上自动补充状态
- agent 后续行为之所以“越来越像会自我调整”，关键不在模型变了，而在上下文文件变了

## 这张图最想说明什么

OpenClaw 最接近“自进化”的地方，不是神秘的内核成长，而是：

- 可以持续写
- 可以持续读
- 可以持续触发
- 可以在下次运行里利用上次沉淀

## 关联

- [[../09-Systems/OpenClaw|OpenClaw]]
- [[../09-Systems/OpenClaw|OpenClaw]]
- [[../09-Systems/OpenClaw 工作原理与架构|OpenClaw 工作原理与架构]]
- [[../09-Systems/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
- [[OpenClaw Architecture Map]]
