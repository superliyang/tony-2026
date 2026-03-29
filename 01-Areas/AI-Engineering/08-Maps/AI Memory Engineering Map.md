---
title: AI Memory Engineering Map
type: map
status: learning
tags:
  - ai/map
  - ai/memory
  - ai/engineering
created: 2026-03-29
updated: 2026-03-29
---

# AI Memory Engineering Map

```mermaid
flowchart TD
  S["[[../07-Topics/Session and Memory Design|Session and Memory Design]]"] --> A["[[../07-Topics/记忆架构：State、Memory、Artifact 与 Context|记忆架构：State、Memory、Artifact 与 Context]]"]
  S --> L["[[../07-Topics/长期运行 Agent 的记忆系统|长期运行 Agent 的记忆系统]]"]
  A --> W["[[../07-Topics/记忆写入、召回、压缩与 Consolidation|记忆写入、召回、压缩与 Consolidation]]"]
  W --> E["[[../07-Topics/记忆评测、污染、遗忘与纠偏|记忆评测、污染、遗忘与纠偏]]"]
  E --> P["[[../07-Topics/Learnings、Promotion 与 Skill Extraction Pipeline|Learnings、Promotion 与 Skill Extraction Pipeline]]"]
  L --> F["[[../07-Topics/Plugin、Memory 与 Background Task 失效模式|Plugin、Memory 与 Background Task 失效模式]]"]
  E --> R["[[../07-Topics/Task Success and Failure Recovery|Task Success and Failure Recovery]]"]
  E --> G["[[../07-Topics/Runtime 发布门槛、灰度与 Blast Radius 控制|Runtime 发布门槛、灰度与 Blast Radius 控制]]"]

  subgraph systems["系统样本"]
    OA["[[../../AI-Learning/09-Systems/OpenClaw 的分层记忆设计|OpenClaw 的分层记忆设计]]"]
    LM["[[../../AI-Learning/09-Systems/LangMem|LangMem]]"]
    LG["[[../../AI-Learning/09-Systems/LangGraph|LangGraph]]"]
    CC["[[../../AI-Learning/09-Systems/Claude Code|Claude Code]]"]
    ADK["[[../../AI-Learning/09-Systems/Google Agent Development Kit（ADK）|Google Agent Development Kit（ADK）]]"]
  end

  OA --> A
  OA --> P
  LM --> W
  LG --> S
  CC --> L
  ADK --> A
```

## 怎么读

- 从 `Session and Memory Design` 开始，先把 state / memory 边界划清
- 再读 `记忆架构` 与 `写入/召回/压缩`
- 然后看 `Learnings、Promotion 与 Skill Extraction Pipeline`，理解什么时候该从 memory 进入 durable rules 和 skills
- 最后读 `评测、污染、遗忘与纠偏`，建立长期运行判断力

## 关联

- [[地图索引]]
- [[../../AI-Learning/07-Maps/AI 记忆设计图|AI 记忆设计图]]
- [[../../AI-Learning/07-Maps/AI 记忆学习导航.base|AI 记忆学习导航（Base）]]
