---
title: Resume Note
type: resume
status: active
domain: AI
updated: 2026-03-22
---

# Resume Note

## Last Session

- We studied: the AI learning system as a whole, and then opened a new branch around AI Agent systems
- We finished: the concept chain, representative model layer, most of the engineering stack/topics/entities, and then separated out a dedicated `Systems` layer for products/platforms/runtime cases

## What I Actually Understand Now

- AI is no longer organized as isolated notes; it is structured as a learning system with a clear path from foundations to modern topics to models to engineering
- The modern AI chain is now readable: foundation models, pretraining, transformer, multimodal, reasoning, long context, RAG, agent, assistant, coding agents
- `AI-Learning` is now cleaner topologically: `Topics` hold abstract themes, while `Systems` hold concrete products/platforms/runtime cases
- `OpenClaw` now gives a concrete case for understanding AI agent runtime systems: gateway, channels, tools, sessions, memory, and local-first assistant design
- The phrase "自进化" should be understood carefully here: in official docs it is closer to memory + workspace mutation + hooks + heartbeat + cron than a literal self-evolving core
- `OpenClaw` is now also mapped against `ChatGPT` and `Claude Code`, so its position in the AI agent landscape is easier to grasp
- The comparison line has widened further: `ChatGPT Agent`, `Claude Code`, `Codex`, `Cursor`, `Devin`, `Manus`, and `OpenClaw` now form a clearer product/runtime landscape
- The abstract capability layer is also clearer now: `Tool Use`, `Agent Memory`, `Planning and Control`, and `Multi-Agent Systems` separate “agent 是什么” from “具体系统长什么样”
- The coding-agent branch is now much more concrete: terminal-first, editor-first, cloud-first, and autonomous software-engineer styles are separated out
- Some of the most reusable engineering abstractions have now been pulled out into `AI-Engineering`: runtime architecture, tool calling, session/memory design, planning/state machines, approval gates, evaluation/reliability, and long-running agent operations
- AI engineering now has topic notes plus stack/framework/training entities

## What Still Feels Fuzzy

- The AI Agent branch still needs more ecosystem notes if we want a full comparative landscape
- Company/entity coverage has improved with `Anysphere` and `Cognition`, though people-layer coverage still trails the systems layer
- The relation between agent runtimes, coding agents, and assistant products still needs more side-by-side comparison
- We still need sharper notes about how these systems fit into real team workflows and governance
- More international / open-source agent systems may still need to be added
- Evaluation and deployment still need more concrete entity pages and project examples
- AI applications and real-world use-case notes still need to be expanded

## Restart Here

- Read: [[./README|README]], [[06-Topics/Agent|Agent]], [[06-Topics/Tool Use|Tool Use]], [[06-Topics/Agent Memory|Agent Memory]], [[06-Topics/Planning and Control|Planning and Control]], [[09-Systems/Systems Index|Systems Index]], [[09-Systems/Claude Code|Claude Code]], [[09-Systems/Codex|Codex]], [[09-Systems/Cursor|Cursor]], [[09-Systems/Devin|Devin]], [[09-Systems/Manus|Manus]], [[09-Systems/OpenClaw|OpenClaw]]
- Then continue to: [[07-Maps/AI Agent Capability Map|AI Agent Capability Map]], [[07-Maps/AI Agent Product Positioning Map|AI Agent Product Positioning Map]], [[07-Maps/AI Coding Agent Positioning Map|AI Coding Agent Positioning Map]], [[../AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]], [[../AI-Engineering/07-Topics/Tool Calling and Action Execution|Tool Calling and Action Execution]], [[../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]], [[../AI-Engineering/07-Topics/Task Success and Failure Recovery|Task Success and Failure Recovery]], [[../AI-Engineering/08-Maps/Agent Evaluation and Governance Map|Agent Evaluation and Governance Map]]

## Do Not Re-read Everything

- Skip: the full early setup work for folder creation and template creation
- Review only if stuck: [[../AI-Foundations/README|AI-Foundations]], [[06-Topics/Agent|Agent]], [[06-Topics/Coding Agents|Coding Agents]], [[07-Maps/OpenClaw Architecture Map|OpenClaw Architecture Map]], [[07-Maps/OpenClaw 准自进化工作流图|OpenClaw 准自进化工作流图]]
