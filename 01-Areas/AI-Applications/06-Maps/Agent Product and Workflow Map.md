---
title: Agent Product and Workflow Map
type: map
status: learning
tags:
  - ai/maps
  - ai/applications
created: 2026-03-22
updated: 2026-03-22
---

# Agent Product and Workflow Map

```mermaid
graph TD
    A["Products"] --> B["ChatGPT Agent"]
    A --> C["Claude Code"]
    A --> D["Cursor"]
    A --> E["Codex"]
    A --> F["OpenClaw"]

    B --> W1["Research Workflow"]
    B --> W3["Enterprise Operations Workflow"]
    B --> W5["Customer Support Triage Workflow"]

    C --> W2["Coding Agent Workflow"]
    D --> W2
    E --> W2

    F --> W1
    F --> W4["Personal Assistant Workflow"]

    W1 --> G["Research / Analysis Use Cases"]
    W2 --> H["Software Engineering Use Cases"]
    W3 --> I["Enterprise Ops Use Cases"]
    W4 --> J["Personal Assistant Use Cases"]
    W5 --> K["Customer Support Use Cases"]
```

## 怎么看这张图

- 先看一个产品更自然地落到哪类 workflow
- 再看 workflow 对应的是哪类应用价值
- 这样可以避免只按“产品名字”学习，而忽略真正的使用路径

## 关联

- [[../02-Products/Products Index|Products Index]]
- [[../03-Workflows/Workflows Index|Workflows Index]]
- [[Agent Application Landscape Map]]
