---
title: Learning Progress
type: progress
status: active
domain: AI
current_topic: MLOps, LLMOps, and feedback-driven AI engineering
last_completed: Turned the AI graph from infra-first expansion into a reusable MLOps / LLMOps slice spanning topics, systems, engineering lifecycle, and observability
next_up: Decide whether to deepen by MLOps case studies, agent/LLM evaluation templates, or vendor comparison under enterprise constraints
updated: 2026-03-26
---

# Learning Progress

## Current

- current_topic: MLOps / LLMOps / AgentOps observability
- current_goal: connect experiments, evals, prompt versioning, registry, deployment, online feedback, and tracing into one lifecycle instead of treating them as isolated tools

## Completed

- Built the 4-area AI structure: `AI-Foundations`, `AI-Learning`, `AI-Engineering`, `AI-Applications`
- Filled `AI-Foundations` with a beginner-to-modern learning path
- Expanded `AI-Learning/06-Topics` into a modern AI concept chain
- Split `AI-Learning` into cleaner `Models` and `Systems` layers
- Added the major agent systems line: `ChatGPT Agent`, `Claude Code`, `Codex`, `Cursor`, `Devin`, `Manus`, `OpenClaw`
- Added the major capability line: `提示词工程`, `上下文工程`, `Tool Use`, `Browser Agents 与 Computer Use`, `Agent Memory`, `Planning and Control`, `Multi-Agent Systems`, `A2A（Agent-to-Agent）与协作协议`
- Added the major agent platform line: `Agent 平台`, `Google Agent Development Kit（ADK）`, `LangGraph`, `Langfuse`
- Added the engineering line around `MCP / CLI`, `Harness`, `Eval Harness`, `Security`, `Long-Running Ops`, `Agent SDK`, `Tool Gateway`, and channel adapters
- Built a six-month global frontier news slice with a recap note, timeline note, frontier map, and new company nodes for `Mistral AI` and `Cohere`
- Distilled that news slice into durable topic notes: `AI Coding Workbench`, `Sovereign AI`, `OCR 与 Document AI`
- Added the AI infra / inference branch: `AI 基础设施与 GPU Cloud`, `Inference Serving`, `NVIDIA`, `CoreWeave`, `Groq`, `Fireworks AI`, `NVIDIA Dynamo`, `CoreWeave Cloud`, `GroqCloud`, `Fireworks Inference Cloud`, and the `AI Infra 与推理服务生态图`
- Added the first-pass MLOps / LLMOps branch: `MLOps 与 LLMOps`, `MLflow`, `Weights & Biases Platform`, `Arize Phoenix`, `Promptfoo`, and the `MLOps 与 LLMOps 生态图`

## Next

- next_up: deepen either by MLOps case studies, evaluation templates, or enterprise vendor tradeoffs between open-source and managed LLMOps stacks
- why_this_next: the graph now has the lifecycle skeleton, so the next highest-value move is to make the tradeoffs more operational and case-driven

## Weak Points

- People coverage is still thinner than company/system/topic coverage
- MLOps / LLMOps now has a strong first-pass topology, but still needs richer case studies and rollout patterns
- Enterprise policy, privacy, and self-hosting tradeoffs across MLflow / Langfuse / Phoenix / W&B can still be expanded later
- We still need more explicit templates for evaluation cadence and release-gate governance

## Open Questions

- Whether the long-term control point sits in experiment/registry systems or in trace/eval/feedback systems
- How much of LLMOps will converge on OpenTelemetry-native observability
- Whether prompt registry becomes as central as model registry for enterprise teams
- How strongly AgentOps will separate from general LLMOps as action surfaces and approvals get richer

## Resume Note

- The AI graph now has a usable MLOps / LLMOps branch. Restart from `AI Topics Index`, then read `MLOps 与 LLMOps`, `MLOps 与 LLMOps 生态图`, and the four system notes before going deeper into the AI-Engineering lifecycle pages.
