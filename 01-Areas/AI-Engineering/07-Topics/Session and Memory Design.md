---
title: Session and Memory Design
type: topic
status: seed
tags:
  - ai/engineering
  - ai/session
  - ai/memory
created: 2026-03-22
updated: 2026-03-22
---

# Session and Memory Design

## 为什么重要

- 这决定 agent 到底是“多轮连续工作”，还是“每次都像第一次见你”
- 很多 agent 的稳定性问题，本质上不是模型差，而是 session 和 memory 设计差

## 系统视角

要把这两个概念分开：

- `Session`：一次连续交互的边界和状态容器
- `Memory`：跨 session 持续保留的信息

如果这两层混在一起，系统通常会出现两种问题：

- 不该记住的也记住了
- 该长期保留的却丢了

## 核心问题

- session 边界按什么切
- 长期 memory 什么该写、什么不该写
- recall 什么时候靠上下文拼接，什么时候靠检索
- 用户、渠道、任务、群聊之间如何做隔离

## 推荐的状态分层

- request state：这一次请求的局部变量
- session state：这一段对话或任务的连续状态
- durable memory：长期事实、偏好、规则、历史结论
- derived memory：摘要、索引、embedding、cache

## Session 设计时要想清楚什么

- 这是不是同一个任务
- 这是不是同一个用户身份
- 群聊和私聊是否共享上下文
- 多渠道是否应该合并成一条 session
- agent 是否需要 task-level checkpoint

## Memory 设计时要想清楚什么

- 什么是事实，什么只是一次猜测
- 什么该 append-only，什么该可编辑
- 谁能改 memory
- memory 出错后如何纠偏
- recall 结果如何被审计和追踪

## 常见策略

- 短期上下文：直接随 session 传递
- 长期知识：写入 durable store
- 高频事实：做结构化索引
- 低置信度内容：先留在 working memory，不立刻升为长期记忆

## 真实系统里最难的点

- identity mapping：一个用户在不同渠道怎么认成同一个人
- memory pollution：错误结论写进长期存储
- summarization drift：总结越来越偏，原始上下文却被压扁
- over-recall：每次都拉太多旧信息，导致噪声和成本上升

## 常见失败模式

- 群聊 session 和私聊 session 串在一起
- 系统把一次错误推断写成用户长期偏好
- memory 只有写入，没有生命周期治理
- session 中断后无法恢复任务现场

## 学习这页时最该记住什么

- session 解决“连续性”
- memory 解决“持久性”
- 两者都不只是存储问题，而是边界治理问题

## 相关主题

- [[Agent Runtime Architecture]]
- [[Long-Running Agent Operations]]
- [[Data Pipelines]]

## 系统案例

- [[../../AI-Learning/09-Systems/OpenClaw 工作原理与架构|OpenClaw 工作原理与架构]]
- [[../../AI-Learning/09-Systems/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
