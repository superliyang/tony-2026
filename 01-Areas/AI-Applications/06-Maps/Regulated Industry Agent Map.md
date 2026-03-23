---
title: Regulated Industry Agent Map
type: map
status: learning
tags:
  - ai/maps
  - ai/applications
  - ai/regulation
created: 2026-03-23
updated: 2026-03-23
---

# Regulated Industry Agent Map

```mermaid
graph TD
    A["Regulated Industries"] --> B["Financial Services"]
    A --> C["Healthcare"]
    A --> D["Legal and Compliance"]

    B --> B1["Value: advisor productivity, knowledge access, multilingual support"]
    B --> B2["Need: evals, privacy, auditable outputs"]
    B --> B3["Case: Morgan Stanley"]

    C --> C1["Value: documentation relief, claims ops, evidence retrieval"]
    C --> C2["Need: HIPAA, access control, clinician oversight"]
    C --> C3["Case: Oscar, OpenAI for Healthcare"]

    D --> D1["Value: drafting, citation, contract comparison"]
    D --> D2["Need: source grounding, reviewability, low hallucination"]
    D --> D3["Case: Harvey"]

    B2 --> E["Common Governance Requirements"]
    C2 --> E
    D2 --> E

    E --> E1["Single Source of Truth"]
    E --> E2["Human Approval Gates"]
    E --> E3["Task-Level Evals"]
    E --> E4["Auditability and Evidence"]
```

## 怎么看这张图

- 这张图不是讲行业大小，而是讲“高监管行业里，agent 为什么难，又为什么值”
- 三个行业的共同点是：价值高，但治理要求更高
- 越进入真实生产环境，越要把 eval、审批、证据和审计能力前置

## 关联

- [[../01-Industries/Financial Services Agents|Financial Services Agents]]
- [[../01-Industries/Healthcare Agents|Healthcare Agents]]
- [[../01-Industries/Legal and Compliance Agents|Legal and Compliance Agents]]
- [[Agent Industry Value Map]]
