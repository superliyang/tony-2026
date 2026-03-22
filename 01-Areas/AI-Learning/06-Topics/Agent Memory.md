---
title: Agent Memory
type: topic
status: draft
tags:
  - ai/topic
  - ai/agent
  - ai/memory
created: 2026-03-22
updated: 2026-03-22
---

# Agent Memory

## 这个主题是什么

`Agent Memory` 关注 agent 如何保留上下文、状态和长期信息，而不是每轮都像第一次见到任务一样重新开始。

## 为什么重要

- 没有记忆，agent 很难跨回合、跨任务、跨渠道保持连续性
- 很多“看起来聪明”的 agent，一旦任务变长、时间跨度变大，就会因为没有可持续记忆而崩掉
- 记忆问题本质上也是系统设计问题，不只是 prompt 问题

## 你先要抓住什么

- 记忆不等于“把所有历史都塞回上下文”
- agent memory 至少要区分：短期上下文、会话状态、长期事实、外部可检索记录
- 真实系统更常见的是“文件 / 数据库 / 向量库 / 事件日志”与模型协同，而不是模型自己神奇记住一切

## 常见层次

- working memory：当前这轮任务临时需要的信息
- session memory：一个会话内持续有效的状态
- durable memory：跨会话保留的长期记录
- retrieval memory：需要时再通过检索拉回来的外部记忆

## 真正难的地方

- 什么该记，什么不该记
- 记忆是事实库、偏好库，还是任务状态机的一部分
- 记忆写入是否可靠，可否被审计与修正
- 历史信息如何压缩，否则上下文成本会越来越高

## 为什么 OpenClaw 值得学

`OpenClaw` 很适合拿来理解 agent memory，因为它把 memory 设计成 workspace 中的可读写文件，并通过工具进行 recall。这是一种很实用的 memory 思路：

- durable memory 可见且可编辑
- recall 通过工具完成
- 模型并不“天然记住”，而是借助系统化记忆机制工作

## 典型系统案例

- [[../09-Systems/OpenClaw|OpenClaw]]
- [[../09-Systems/OpenClaw 工作原理与架构|OpenClaw 工作原理与架构]]
- [[../09-Systems/ChatGPT Agent|ChatGPT Agent]]

## 从工程角度继续往下读

- [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../../AI-Engineering/07-Topics/Planning Loops and State Machines|Planning Loops and State Machines]]
- [[../../AI-Engineering/07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]

## 相关

- [[Agent]]
- [[Tool Use]]
- [[Planning and Control]]
- [[Long Context]]
- [[RAG]]
- [[../07-Maps/AI Agent Capability Map|AI Agent Capability Map]]
