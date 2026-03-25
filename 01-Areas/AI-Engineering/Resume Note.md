---
title: Resume Note
type: resume
status: active
domain: AI-Engineering
updated: 2026-03-25
---

# Resume Note

## Last Session

- We closed the first-pass agent engineering branch by adding the missing layers around long-term memory systems, security / sandbox / approval architecture, and A2A coordination.

## What I Actually Understand Now

- Agent engineering is not just runtime architecture; it is runtime + action surfaces + harness + eval + memory + trust boundaries
- `CLI`、`MCP`、`Computer Use` are different action surfaces, not one debate with one winner
- `App Server / Rich Protocols` expose tasks, sessions, events, approvals, and artifacts to clients
- `Harness Engineering` is the workbench layer that gathers environment, policies, feedback loops, and observability
- `Eval Harness` and `Regression Suites` are the quality loop inside that workbench
- Long-running memory systems are about thread state, durable memory, compaction, and correction, not just retrieval
- `A2A` and `Multi-Agent` are related but distinct: one is cross-boundary interoperability, the other is system structure
- Security is a first-class architecture layer: sandbox, permission modes, approvals, watch mode, allowlists, auditability, and recovery all sit here

## What Still Feels Fuzzy

- We still need more real project cases for remote MCP trust, A2A rollout, browser-heavy automation, and app-server control planes
- Security-heavy enterprise patterns are still more abstract than case-driven
- Trace-grading and continuous-eval examples can still be richer later

## Restart Here

- Read: [[./README|README]], [[07-Topics/Topics Index|Topics Index]], [[07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]], [[07-Topics/App Server 与 Rich Agent Protocols|App Server 与 Rich Agent Protocols]], [[07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]], [[07-Topics/Harness Engineering|Harness Engineering]], [[07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]], [[07-Topics/长期运行 Agent 的记忆系统|长期运行 Agent 的记忆系统]], [[07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]], [[07-Topics/A2A 与 Multi-Agent Coordination|A2A 与 Multi-Agent Coordination]]
- Then continue to: [[08-Maps/Agent Action Surfaces and Protocols Map|Agent Action Surfaces and Protocols Map]], [[08-Maps/Agent Context and Integration Engineering Map|Agent Context and Integration Engineering Map]], [[08-Maps/Harness Feedback Loop Map|Harness Feedback Loop Map]], [[08-Maps/Agent 协作、记忆与信任边界图|Agent 协作、记忆与信任边界图]], [[08-Maps/Agent Evaluation and Governance Map|Agent Evaluation and Governance Map]]
