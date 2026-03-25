---
title: Learning Progress
type: progress
status: active
domain: AI-Engineering
current_topic: Agent platform stack and SDK design
last_completed: Closed the first-pass agent runtime branch and extended it with platform architecture, SDK boundaries, tool gateways, channel adapters, and runtime stack decisions
next_up: Use the new platform slice to connect runtime theory to real platform design choices and later case studies
updated: 2026-03-25
---

# Learning Progress

## Current

- current_topic: SDK boundaries, tool gateways, channel adapters, and platform stack decisions
- current_goal: connect the completed runtime architecture branch to an actionable agent platform blueprint using LangGraph, Langfuse, ADK, and channel adapters

## Completed

- Built the core AI engineering path across training, evaluation, inference, deployment, and agent runtime topics
- Added runtime, tool calling, session/memory, planning loop, approval gate, reliability, and long-running operations topics
- Added the action-surface branch: `MCP 与 CLI 模式`, `App Server 与 Rich Agent Protocols`, `Computer Use Runtime and Safety`
- Added the harness branch: `Harness Engineering`, `Eval Harness 与 Regression Suites`, and `Harness Feedback Loop Map`
- Added the governance branch: `Agent Evaluation and Reliability`, `Task Success and Failure Recovery`, `Cost, Latency, and Safety Tradeoffs`
- Added the completion branch: `长期运行 Agent 的记忆系统`, `Agent Security、Sandbox 与 Approval Architecture`, and `A2A 与 Multi-Agent Coordination`
- Added maps that now connect runtime, action surfaces, trust boundaries, memory systems, and governance as one readable system
- Added the platform-design layer: `Agent SDK 设计`, `Tool Gateway、MCP Servers 与 SDK Tools`, `飞书 / Lark 作为 Agent Channel Adapter`, and `Agent 平台架构（LangGraph、Langfuse、ADK）`

## Next

- next_up: read the platform stack end-to-end and then expand later into deployment cases, Feishu interaction cases, and dual-runtime production patterns
- why_this_next: the architecture is now broad enough that the highest-value move is system synthesis and practical platform design, not more isolated abstractions

## Weak Points

- We still need more concrete case notes for remote MCP, A2A adoption, browser-heavy agents, and security control towers
- Rich app-server protocol cases are still thinner than the abstraction layer
- Production-grade memory correction and trace-grading examples can still be expanded later

## Resume Note

- Restart from `Topics Index`, then read the agent path as one line: `Runtime -> Action Surfaces -> Harness -> Eval Harness -> Long-Term Memory -> Security / Approval -> A2A / Coordination -> Long-Running Ops`, and then continue into `Agent SDK -> Tool Gateway -> Channel Adapter -> Platform Architecture`.
