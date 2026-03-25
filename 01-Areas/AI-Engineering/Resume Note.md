---
title: Resume Note
type: resume
status: active
domain: AI-Engineering
updated: 2026-03-25
---

# Resume Note

## Last Session

- We extended `AI-Engineering` with a new agent-focused slice around `Harness Engineering` and the real boundary between `MCP` and `CLI` execution modes.

## What I Actually Understand Now

- Agent engineering is not just runtime architecture; it also depends on how context is assembled and how actions are surfaced
- `CLI` and `MCP` are not the same kind of abstraction: one is closer to direct execution, the other to protocolized integration
- Modern agent quality increasingly depends on harness design: environment, feedback loop, evals, approvals, and legibility
- The engineering path from prompt to context to tool integration is now explicitly connected in the vault

## What Still Feels Fuzzy

- Rich app-server style task protocols still need more concrete case notes
- Remote MCP trust boundaries and policy patterns still need more examples
- We still need more side-by-side project cases for shell-heavy, MCP-heavy, and mixed architectures

## Restart Here

- Read: [[./README|README]], [[07-Topics/Topics Index|Topics Index]], [[07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]], [[07-Topics/Tool Calling and Action Execution|Tool Calling and Action Execution]], [[07-Topics/Session and Memory Design|Session and Memory Design]], [[07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]], [[07-Topics/Harness Engineering|Harness Engineering]]
- Then continue to: [[08-Maps/Agent Context and Integration Engineering Map|Agent Context and Integration Engineering Map]], [[08-Maps/Agent Runtime Engineering Map|Agent Runtime Engineering Map]], [[08-Maps/Agent Evaluation and Governance Map|Agent Evaluation and Governance Map]]
