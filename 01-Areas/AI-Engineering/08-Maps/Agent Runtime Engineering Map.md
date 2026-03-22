---
title: Agent Runtime Engineering Map
type: map
status: seed
tags:
  - ai/maps
created: 2026-03-22
updated: 2026-03-22
---

# Agent Runtime Engineering Map

```mermaid
flowchart TD
  A["Agent Runtime Architecture"] --> A1["Tool Calling and Action Execution"]
  A --> B["Session and Memory Design"]
  A --> A2["Planning Loops and State Machines"]
  A --> A3["Human-in-the-Loop and Approval Gates"]
  A --> A4["Agent Evaluation and Reliability"]
  A --> C["Long-Running Agent Operations"]
  A --> D["Serving and Scaling"]
  A --> E["Security and Privacy"]

  B --> B1["session boundary"]
  B --> B2["durable memory"]
  B --> B3["identity / isolation"]

  C --> C1["heartbeat"]
  C --> C2["cron"]
  C --> C3["hooks / retries / escalation"]

  D --> D1["service orchestration"]
  E --> E1["permissions / audit / guardrails"]

  F["System Cases"] --> G["OpenClaw"]
  F --> H["Claude Code"]
```

## 怎么读这张图

- `Agent Runtime Architecture` 是总骨架
- `Tool Calling and Action Execution` 解决动作层如何真正执行
- `Session and Memory Design` 解决连续性与持久性
- `Planning Loops and State Machines` 解决控制循环如何稳定
- `Human-in-the-Loop and Approval Gates` 解决风险治理
- `Long-Running Agent Operations` 解决长期运行、主动触发和治理
- 这些主题再和 serving、安全、成本交叉，才构成真实 agent 系统

## 关联

- [[../07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[../07-Topics/Tool Calling and Action Execution|Tool Calling and Action Execution]]
- [[../07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../07-Topics/Planning Loops and State Machines|Planning Loops and State Machines]]
- [[../07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
- [[../07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
- [[../07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]
- [[Agent Evaluation and Governance Map]]
- [[../07-Topics/Serving and Scaling|Serving and Scaling]]
- [[../07-Topics/Security and Privacy|Security and Privacy]]
- [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]
