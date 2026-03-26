---
title: Learning Progress
type: progress
status: active
domain: AI-Engineering
current_topic: MLOps, LLMOps, and feedback-driven release engineering
last_completed: Expanded the engineering path with a complete first-pass branch for experiment tracking, evaluation, prompt/dataset governance, registry, online feedback, and LLM/agent observability
next_up: Decide whether to deepen by enterprise MLOps case studies, evaluation templates, or open-source vs managed platform tradeoffs
updated: 2026-03-26
---

# Learning Progress

## Current

- current_topic: MLOps / LLMOps / AgentOps observability
- current_goal: turn the older seed-level evaluation and registry notes into a readable engineering branch that explains how experiments, prompts, datasets, release gates, feedback loops, and production traces fit together

## Completed

- Built the core AI engineering path across training, evaluation, inference, deployment, and agent runtime topics
- Added runtime, tool calling, session/memory, planning loop, approval gate, reliability, and long-running operations topics
- Added the action-surface branch: `MCP 与 CLI 模式`, `App Server 与 Rich Agent Protocols`, `Computer Use Runtime and Safety`
- Added the harness branch: `Harness Engineering`, `Eval Harness 与 Regression Suites`, and `Harness Feedback Loop Map`
- Added the governance branch: `Agent Evaluation and Reliability`, `Task Success and Failure Recovery`, `Cost, Latency, and Safety Tradeoffs`
- Added the completion branch: `长期运行 Agent 的记忆系统`, `Agent Security、Sandbox 与 Approval Architecture`, and `A2A 与 Multi-Agent Coordination`
- Added the platform-design layer: `Agent SDK 设计`, `Tool Gateway、MCP Servers 与 SDK Tools`, `飞书与 Lark 作为 Agent Channel Adapter`, and `Agent 平台架构（LangGraph、Langfuse、ADK）`
- Upgraded the inference branch from seeds into a coherent slice: `Infrastructure (GPU-TPU)`, `Inference Optimization`, `Serving and Scaling`, `KV Cache、Prefill-Decode 与 Continuous Batching`, `Disaggregated Serving 与推理数据面`, `SGLang`, `TensorRT-LLM`, and a richer `Inference and Serving Map`
- Added the first MLOps / LLMOps slice: `Experiment Tracking`, `Evaluation and Benchmarks`, `Prompt Registry、Datasets 与 Evals`, `Model Registry and Deployment`, `Online Evals、Human Feedback 与 Annotation`, `LLMOps、AgentOps 与 Observability`, `Evaluation Index`, `Deployment Index`, and a richer `AI Engineering Stack Map`

## Next

- next_up: deepen either by enterprise case studies, evaluation / release templates, or open-source vs managed MLOps tradeoffs
- why_this_next: the engineering branch now explains the lifecycle shape, so the next highest-value move is to make the operational tradeoffs more concrete and reusable

## Weak Points

- We still need more concrete case notes for enterprise rollout, self-hosting choices, and governance rituals
- Rich evaluation templates and release-checklist templates are still thinner than the topology layer
- Production examples for annotation workflows and policy-heavy release gates can still be expanded later
- The lifecycle is now structurally strong, but still lighter on failure stories and rollout cases than on concepts

## Resume Note

- Restart from `Topics Index`, then read the MLOps line as one chain: `Experiment Tracking -> Evaluation and Benchmarks -> Prompt Registry / Datasets / Evals -> Model Registry and Deployment -> Online Evals / Human Feedback / Annotation -> LLMOps / AgentOps / Observability`, then continue into the system notes and `MLOps 与 LLMOps 工程图`.
