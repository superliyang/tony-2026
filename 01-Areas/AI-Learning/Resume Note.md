---
title: Resume Note
type: resume
status: active
domain: AI
updated: 2026-03-25
---

# Resume Note

## Last Session

- We finished a first-pass closure of the AI Agent branch by adding the missing layers around `A2A`, long-term memory systems, harness feedback loops, and security / sandbox / approval boundaries.

## What I Actually Understand Now

- The AI Agent branch is no longer just a list of hot words; it now has a clear progression from `prompt` to `context` to `tool use` to `runtime` to `governance`
- `CLI`、`MCP`、`Browser / Computer Use` should be treated as different action surfaces rather than mutually exclusive camps
- `App Server / Rich Protocols` are a higher control layer for task/session/event/approval semantics, not just another tool protocol
- `Harness Engineering` is the workbench layer that gathers environment, tool surfaces, policies, feedback loops, and legibility
- `Eval Harness` and `Regression Suites` are the quality loop inside that workbench
- `Agent Memory` is really about thread state, durable memory, and retrieval policy, not magical model recall
- `Multi-Agent` and `A2A` are related but not identical: one is architecture, the other is cross-boundary interoperability
- Security is not an add-on; sandbox, permission modes, watch mode, approvals, and auditability are core architecture concerns

## What Still Feels Fuzzy

- Rich case notes for A2A adoption are still thinner than the abstract protocol layer
- Browser-heavy and security-heavy enterprise agent cases can still be expanded later
- Some vendor protocol boundaries may change as the ecosystem keeps moving quickly

## Restart Here

- Read: [[./README|README]], [[06-Topics/AI Topics Index|AI Topics Index]], [[06-Topics/Agent|Agent]], [[06-Topics/提示词工程|提示词工程]], [[06-Topics/上下文工程|上下文工程]], [[06-Topics/Tool Use|Tool Use]], [[06-Topics/MCP（Model Context Protocol）|MCP（Model Context Protocol）]], [[06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]], [[06-Topics/Agent Memory|Agent Memory]], [[06-Topics/Multi-Agent Systems|Multi-Agent Systems]], [[06-Topics/A2A（Agent-to-Agent）与协作协议|A2A（Agent-to-Agent）与协作协议]]
- Then continue to: [[07-Maps/AI Agent Capability Map|AI Agent Capability Map]], [[07-Maps/Agent Prompt-Context-Harness Map|Agent Prompt-Context-Harness Map]], [[../AI-Engineering/07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]], [[../AI-Engineering/07-Topics/App Server 与 Rich Agent Protocols|App Server 与 Rich Agent Protocols]], [[../AI-Engineering/07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]], [[../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]], [[../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]], [[../AI-Engineering/07-Topics/长期运行 Agent 的记忆系统|长期运行 Agent 的记忆系统]], [[../AI-Engineering/07-Topics/A2A 与 Multi-Agent Coordination|A2A 与 Multi-Agent Coordination]], [[../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]
