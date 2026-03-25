---
title: Harness Engineering
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/harness
created: 2026-03-25
updated: 2026-03-25
---

# Harness Engineering

## 为什么这个词最近变热

`Harness Engineering` 是 agent / coding agent 时代更工程化的一种说法。

它强调：真正决定 agent 质量的，不只是 prompt，也不只是 tool call，而是围绕 agent 搭起来的整套工作台：

- 任务边界
- 代码仓库或业务环境
- 工具与协议
- 反馈回路
- 评测与回归
- 审批与策略
- 可读性与可调试性

## 可以把 harness 理解成什么

最直白地说，`harness` 就是 agent 被放进去工作的受控环境。

在 coding agent 里，它往往包括：

- repo / branch / diff 作为系统真实上下文
- shell、API、browser、MCP server 等动作面
- task object、session、approval、logs
- 测试、lint、eval 和回归检查
- 人类可以介入、审查、重试和回放的反馈机制

## 为什么 prompt engineering 不够了

如果 agent 已经要：

- 读代码
- 改文件
- 运行命令
- 调外部工具
- 生成 diff
- 提交任务结果

那系统好坏往往不再主要取决于 prompt，而是取决于 harness 是否：

- 可观察
- 可限制
- 可复现
- 可评估
- 可恢复

## 和 context engineering 的关系

- `Context Engineering` 更关注模型看到什么
- `Harness Engineering` 更关注模型如何在一个完整工作台中被引导、被约束、被反馈

可以简单理解成：

- prompt 是一层文本控制
- context 是一层信息装配
- harness 是一层系统环境与反馈回路

## 一个成熟 harness 往往包含什么

- `environment`：仓库、文件、任务、工作目录、外部系统
- `tool surface`：CLI、browser、API、MCP
- `control plane`：session、task、approval、budget、timeouts
- `feedback loop`：tests、evals、review、retry、rollback
- `regression control`：trace grading、suite、promotion gate
- `legibility`：logs、artifacts、trace、diff、decision history

## 为什么这对 coding agents 特别重要

coding agent 的难点不只是“会写代码”，而是：

- 有没有稳定的 repo context
- 改动是不是可检查
- 是否能自动跑验证
- agent 的行为是否足够可读，方便人类 review
- session 和 task object 是否足够清晰

这些都更接近 harness 问题。

## 为什么 MCP 和 CLI 都只是 harness 的一部分

`MCP` 和 `CLI` 经常被争成二选一，但从 harness 视角看，它们只是动作面的两种接法：

- `CLI` 更直接
- `MCP` 更协议化
- 更复杂的 task / diff / approval / app server，又是另一层协议或 runtime 结构

所以真正的工程问题不是“押宝哪一个词”，而是：

- 你的 agent 需要多强的动作能力
- 需要多清晰的边界
- 需要多强的可观测与治理

## 什么时候你已经进入 harness engineering

- 你在设计 agent app server 或 task protocol
- 你在搭 repo-aware execution environment
- 你在做 regression harness、eval harness、review loop
- 你在限制动作权限和审批门槛
- 你在思考 session / diff / artifact 怎么沉淀

## 推荐继续往下读

- [[MCP 与 CLI 模式]]
- [[Tool Calling and Action Execution]]
- [[Planning Loops and State Machines]]
- [[Human-in-the-Loop and Approval Gates]]
- [[Agent Evaluation and Reliability]]
- [[Eval Harness 与 Regression Suites]]
- [[../../AI-Learning/06-Topics/上下文工程|上下文工程]]

## 系统案例

- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
- [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]

## 相关

- [[Agent Runtime Architecture]]
- [[MCP 与 CLI 模式]]
- [[Tool Calling and Action Execution]]
- [[Session and Memory Design]]
- [[Long-Running Agent Operations]]
- [[Eval Harness 与 Regression Suites]]
- [[../08-Maps/Agent Context and Integration Engineering Map|Agent Context and Integration Engineering Map]]
- [[../08-Maps/Harness Feedback Loop Map|Harness Feedback Loop Map]]
