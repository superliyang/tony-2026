---
title: Agent Industry Value Map
type: map
status: learning
tags:
  - ai/maps
  - ai/applications
created: 2026-03-22
updated: 2026-03-22
---

# Agent Industry Value Map

```mermaid
graph TD
    A["Agent Applications"] --> B["Customer Support"]
    A --> C["Enterprise Operations"]
    A --> D["Software Engineering"]
    A --> E["Sales and Revenue"]

    B --> B1["Value: deflection, faster resolution, multilingual support"]
    B --> B2["Risk: wrong policy, bad actions, trust loss"]
    B --> B3["Cases: Klarna, Nubank, Salesforce, Decagon"]

    C --> C1["Value: workflow throughput, reusable analysis, auditability"]
    C --> C2["Risk: permissions, data leakage, silent drift"]
    C --> C3["Cases: OpenAI data agent, ServiceNow"]

    D --> D1["Value: faster drafts, review assist, shorter cycle time"]
    D --> D2["Risk: regressions, over-trust, hidden failure"]
    D --> D3["Cases: GitHub Copilot, Claude Code, Cursor, Codex"]

    E --> E1["Value: less admin work, faster follow-up, better pipeline visibility"]
    E --> E2["Risk: low trust, poor tone, bad CRM data"]
    E --> E3["Cases: Attention, Workato"]

    B2 --> F["Governance"]
    C2 --> F
    D2 --> F
    E2 --> F

    F --> F1["Approval Gates"]
    F --> F2["Evaluation"]
    F --> F3["Failure Recovery"]
    F --> F4["ROI and Adoption"]
```

## 怎么看这张图

- 左边看行业落地位置
- 中间看价值来源
- 右边看风险与代表案例
- 底部看无论落在哪个行业，都绕不开的治理要求

## 关联

- [[../01-Industries/Industries Index|Industries Index]]
- [[../04-Case-Studies/Case Studies Index|Case Studies Index]]
- [[../05-Topics/Agent Applications|Agent Applications]]
- [[Agent Application Landscape Map]]
