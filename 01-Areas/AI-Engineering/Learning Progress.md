---
title: Learning Progress
type: progress
status: active
domain: AI-Engineering
current_topic: AI infra and inference serving systems
last_completed: Expanded the engineering path with a complete first-pass branch for GPU cloud, serving runtimes, disaggregated serving, and inference data planes
next_up: Decide whether to deepen by benchmark methodology, runtime comparison cases, or infra control-plane examples
updated: 2026-03-25
---

# Learning Progress

## Current

- current_topic: AI infra / inference serving / serving data plane
- current_goal: turn the old seed-level inference notes into a readable engineering branch that explains where runtime, cloud substrate, routing, and data planes now split apart

## Completed

- Built the core AI engineering path across training, evaluation, inference, deployment, and agent runtime topics
- Added runtime, tool calling, session/memory, planning loop, approval gate, reliability, and long-running operations topics
- Added the action-surface branch: `MCP 与 CLI 模式`, `App Server 与 Rich Agent Protocols`, `Computer Use Runtime and Safety`
- Added the harness branch: `Harness Engineering`, `Eval Harness 与 Regression Suites`, and `Harness Feedback Loop Map`
- Added the governance branch: `Agent Evaluation and Reliability`, `Task Success and Failure Recovery`, `Cost, Latency, and Safety Tradeoffs`
- Added the completion branch: `长期运行 Agent 的记忆系统`, `Agent Security、Sandbox 与 Approval Architecture`, and `A2A 与 Multi-Agent Coordination`
- Added the platform-design layer: `Agent SDK 设计`, `Tool Gateway、MCP Servers 与 SDK Tools`, `飞书与 Lark 作为 Agent Channel Adapter`, and `Agent 平台架构（LangGraph、Langfuse、ADK）`
- Added the delivery-doc layer under `06-Projects`: PRD, architecture doc, API/data model, roadmap, and Cursor implementation pack
- Upgraded the inference branch from seeds into a coherent slice: `Infrastructure (GPU-TPU)`, `Inference Optimization`, `Serving and Scaling`, `KV Cache、Prefill-Decode 与 Continuous Batching`, `Disaggregated Serving 与推理数据面`, `SGLang`, `TensorRT-LLM`, and a richer `Inference and Serving Map`

## Next

- next_up: deepen either by runtime comparison benchmarks, infra control-plane cases, or enterprise serving patterns
- why_this_next: the engineering branch now explains what the layers are, so the next highest-value move is to make the tradeoffs more case-driven and comparative

## Weak Points

- We still need more concrete case notes for benchmark methodology, routing failures, GPU cloud operating models, and data-plane control towers
- Rich inference cost-measurement and evaluation methods are still thinner than the topology layer
- Production examples for mixed-runtime serving and vendor-neutral data-plane operations can still be expanded later

## Resume Note

- Restart from `Topics Index`, then read the inference line as one chain: `Infrastructure -> Inference Optimization -> Serving and Scaling -> KV Cache / Prefill-Decode / Continuous Batching -> Disaggregated Serving`, then continue into `vLLM -> SGLang -> TensorRT-LLM -> Inference and Serving Map`.
