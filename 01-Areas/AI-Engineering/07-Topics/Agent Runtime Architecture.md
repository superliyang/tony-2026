---
title: Agent Runtime Architecture
type: topic
status: seed
tags:
  - ai/engineering
  - ai/agent-runtime
created: 2026-03-22
updated: 2026-03-22
---

# Agent Runtime Architecture

## 为什么重要

- 它决定 agent 不是“会回答的模型”，而是“可持续运行的系统”
- 很多 agent demo 卡在能力演示层，真正落地时瓶颈往往在 runtime 设计

## 系统视角

`Agent Runtime` 解决的不是“模型聪不聪明”，而是：

- 一次任务如何被接住
- 状态如何延续
- 工具如何安全调用
- 多轮执行如何被约束
- 系统如何长期运行而不失控

如果把普通聊天产品看成 `request -> model -> response`，那么 agent runtime 更像：

- ingress
- session state
- planning / execution loop
- tool bus
- memory layer
- scheduling / automation
- policy / safety
- observability

## 关键问题

- runtime 的 source of truth 是什么
- agent 的执行循环和工具调用如何编排
- 状态、记忆、权限和自动化如何协同
- 多渠道、多客户端、多节点时如何保持一致性

## 核心模块

- 入口层：chat、API、消息渠道、事件源
- 会话层：session 边界、身份映射、上下文隔离
- 执行层：planner、executor、tool dispatcher
- 状态层：working state、durable state、checkpoints
- 安全层：权限、allow / deny、配额、人工接管
- 运维层：heartbeat、cron、hook、日志、审计

## 和普通 assistant 的差别

- assistant 更关心交互体验
- runtime 更关心系统行为能不能连续、可控、可恢复

也就是说，assistant 是产品外观，runtime 是系统骨架。

## 和 coding agent 的差别

- coding agent 是一个高价值垂直场景
- runtime 是更底层的执行平台

很多 coding agent 成功与否，最终也取决于 runtime 是否能处理：

- repo state
- command feedback
- file mutation
- retries
- guardrails

## 典型架构形态

- 单轮 agent：每次请求独立执行
- 会话型 agent：保留连续上下文
- 长期在线 agent：带 heartbeat / cron / hooks
- 多节点 agent：客户端、工作节点、渠道节点统一接入 control plane

## 真实系统里最难的地方

- session 边界不清，导致串话或状态污染
- tools 很强，但权限治理很弱
- 记忆能写入，但没有版本与纠错
- 自动化能力一上来，系统就变得 noisy 或不可预测
- agent “看起来很聪明”，但无法 debug 和审计

## 常见失败模式

- 一次错误写入污染长期 memory
- 多轮执行中上下文漂移，任务方向越来越偏
- 多客户端同时改状态，出现 source-of-truth 冲突
- 工具调用重试没有幂等设计，造成重复动作
- heartbeat / cron 缺少节流，导致低价值高成本循环

## 学习这页时最该记住什么

- agent runtime 是“系统设计问题”，不只是“prompt 设计问题”
- 真正成熟的 agent 产品，最终都要回答 session、memory、tooling、safety、ops 这几件事

## 相关主题

- [[Session and Memory Design]]
- [[Long-Running Agent Operations]]
- [[Serving and Scaling]]
- [[Security and Privacy]]

## 系统案例

- [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]
- [[../../AI-Learning/09-Systems/OpenClaw 工作原理与架构|OpenClaw 工作原理与架构]]
- [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
