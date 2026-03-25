---
title: Resume Note
type: resume
status: active
domain: AI-Engineering
updated: 2026-03-25
---

# Resume Note

## Last Session

- We extended `AI-Engineering` with a new agent-focused slice around `Harness Engineering`, then pushed further into `Computer Use`, `App Server`, and `Eval Harness` as the next quality-control layer.

## What I Actually Understand Now

- Agent engineering is not just runtime architecture; it also depends on how context is assembled and how actions are surfaced
- `CLI` and `MCP` are not the same kind of abstraction: one is closer to direct execution, the other to protocolized integration
- `Computer Use` is a third major action surface: powerful, but slower and riskier because it operates through real UI loops
- `App Server` / rich protocols become important when the system must expose tasks, approvals, events, and artifacts to multiple clients
- Modern agent quality increasingly depends on harness design: environment, feedback loop, evals, approvals, and legibility
- Eval harnesses and regression suites are now framed as the quality loop inside harness engineering, not as optional afterthoughts
- The engineering path from prompt to context to tool integration to eval harness is now explicitly connected in the vault

## What Still Feels Fuzzy

- Rich app-server style task protocols still need more concrete case notes
- Remote MCP trust boundaries and policy patterns still need more examples
- We still need more side-by-side project cases for shell-heavy, browser-heavy, MCP-heavy, and mixed architectures
- Concrete trace-grading and continuous-eval case notes are still thinner than the abstract harness layer

## Restart Here

- Read: [[./README|README]], [[07-Topics/Topics Index|Topics Index]], [[07-Topics/Tool Calling and Action Execution|Tool Calling and Action Execution]], [[07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]], [[07-Topics/App Server 与 Rich Agent Protocols|App Server 与 Rich Agent Protocols]], [[07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]], [[07-Topics/Harness Engineering|Harness Engineering]], [[07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]
- Then continue to: [[08-Maps/Agent Action Surfaces and Protocols Map|Agent Action Surfaces and Protocols Map]], [[08-Maps/Agent Context and Integration Engineering Map|Agent Context and Integration Engineering Map]], [[08-Maps/Harness Feedback Loop Map|Harness Feedback Loop Map]], [[08-Maps/Agent Runtime Engineering Map|Agent Runtime Engineering Map]], [[08-Maps/Agent Evaluation and Governance Map|Agent Evaluation and Governance Map]]
