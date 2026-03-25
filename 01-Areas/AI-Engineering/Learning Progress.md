---
title: Learning Progress
type: progress
status: active
domain: AI-Engineering
current_topic: Agent architecture closure
last_completed: Closed the first-pass agent runtime branch with action surfaces, eval harnesses, long-term memory, security boundaries, and A2A coordination
next_up: Re-read the agent runtime branch as a coherent system and use future slices mainly for case expansion
updated: 2026-03-25
---

# Learning Progress

## Current

- current_topic: coordination, memory, trust boundaries, and quality loops
- current_goal: turn the agent runtime branch into a complete first-pass engineering architecture rather than a set of scattered debates

## Completed

- Built the core AI engineering path across training, evaluation, inference, deployment, and agent runtime topics
- Added runtime, tool calling, session/memory, planning loop, approval gate, reliability, and long-running operations topics
- Added the action-surface branch: `MCP 与 CLI 模式`, `App Server 与 Rich Agent Protocols`, `Computer Use Runtime and Safety`
- Added the harness branch: `Harness Engineering`, `Eval Harness 与 Regression Suites`, and `Harness Feedback Loop Map`
- Added the governance branch: `Agent Evaluation and Reliability`, `Task Success and Failure Recovery`, `Cost, Latency, and Safety Tradeoffs`
- Added the completion branch: `长期运行 Agent 的记忆系统`, `Agent Security、Sandbox 与 Approval Architecture`, and `A2A 与 Multi-Agent Coordination`
- Added maps that now connect runtime, action surfaces, trust boundaries, memory systems, and governance as one readable system

## Next

- next_up: use the current branch for synthesis and later case-study expansion rather than creating more abstract topics immediately
- why_this_next: the architecture is now broad enough that the best next step is deeper project cases, not more top-level fragmentation

## Weak Points

- We still need more concrete case notes for remote MCP, A2A adoption, browser-heavy agents, and security control towers
- Rich app-server protocol cases are still thinner than the abstraction layer
- Production-grade memory correction and trace-grading examples can still be expanded later

## Resume Note

- Restart from `Topics Index`, then read the agent path as one line: `Runtime -> Action Surfaces -> Harness -> Eval Harness -> Long-Term Memory -> Security / Approval -> A2A / Coordination -> Long-Running Ops`.
