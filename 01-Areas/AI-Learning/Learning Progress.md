---
title: Learning Progress
type: progress
status: active
domain: AI
current_topic: Agent platform systems and stack design
last_completed: Closed the first-pass agent architecture and extended it into an agent platform slice with ADK, LangGraph, Langfuse, SDK design, tool gateways, and channel adapters
next_up: Use the new platform slice to connect abstract agent architecture with concrete runtime and platform design choices
updated: 2026-03-25
---

# Learning Progress

## Current

- current_topic: agent platform systems, SDK boundaries, and runtime stack choices
- current_goal: connect the completed agent architecture branch to the next layer: agent development frameworks, runtime selection, observability, and platform design

## Completed

- Built the 4-area AI structure: `AI-Foundations`, `AI-Learning`, `AI-Engineering`, `AI-Applications`
- Filled `AI-Foundations` with a beginner-to-modern learning path
- Expanded `AI-Learning/06-Topics` into a modern AI concept chain
- Split `AI-Learning` into cleaner `Models` and `Systems` layers
- Added the major agent systems line: `ChatGPT Agent`, `Claude Code`, `Codex`, `Cursor`, `Devin`, `Manus`, `OpenClaw`
- Added the major capability line: `提示词工程`, `上下文工程`, `Tool Use`, `Browser Agents 与 Computer Use`, `Agent Memory`, `Planning and Control`, `Multi-Agent Systems`, `A2A（Agent-to-Agent）与协作协议`
- Added a coherent action-surface line in `AI-Engineering`: `MCP 与 CLI 模式`, `App Server 与 Rich Agent Protocols`, `Computer Use Runtime and Safety`
- Added the harness line: `Harness Engineering`, `Eval Harness 与 Regression Suites`
- Added the long-running / governance line: `长期运行 Agent 的记忆系统`, `Long-Running Agent Operations`, `Agent Security、Sandbox 与 Approval Architecture`, `A2A 与 Multi-Agent Coordination`
- Added supporting maps so the branch can be resumed as a full architecture rather than isolated notes
- Expanded `AI-Applications` into a deep agent applications area with products, workflows, rollout, and industry slices
- Added the agent platform bridge: `Agent 平台`, `Google Agent Development Kit（ADK）`, `LangGraph`, `Langfuse`, and the platform ecosystem map

## Next

- next_up: read the platform branch from `Agent 平台` into `ADK / LangGraph / Langfuse` and then into the engineering architecture notes
- why_this_next: the agent branch is mature enough that the next highest-value move is not more hot-topic coverage but system design synthesis

## Weak Points

- We still need more project-level case notes around remote MCP, A2A adoption, browser-heavy agents, and security architectures if we want a richer case layer
- We can later deepen real production cases around ADK-native stacks, LangGraph deployment patterns, and Langfuse evaluation operations
- People/entity coverage still trails the topic/system layer
- Open-source and non-US agent ecosystems can still be expanded later

## Open Questions

- Which agent protocols will remain narrow implementation layers versus becoming durable ecosystem standards
- How quickly app-server style protocols will standardize relative to MCP
- Whether A2A will remain a collaboration niche or become common in enterprise agent stacks

## Resume Note

- The AI Agent branch is now structurally complete for a first pass. Restart from `AI Topics Index`, then read the line `Prompt -> Context -> Tool Use -> MCP / Browser -> Memory -> Multi-Agent / A2A -> Systems -> Harness -> Eval Harness -> Security / Long-Running Ops`, and then continue into `Agent 平台 -> ADK / LangGraph / Langfuse -> Agent SDK -> Tool Gateway -> Channel Adapter -> Platform Architecture`.
