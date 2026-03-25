---
title: Agent Memory
type: topic
status: learning
tags:
  - ai/topic
  - ai/agent
  - ai/memory
created: 2026-03-22
updated: 2026-03-25
---

# Agent Memory

## 这个主题是什么

`Agent Memory` 关注 agent 如何在长任务、跨回合、跨会话甚至跨天的工作中保留状态、知识和经验，而不是每一轮都像从零开始。

## 为什么重要

- 没有记忆，agent 很难形成连续性
- 很多“看起来聪明”的 agent，一旦任务变长、跨度变大，就会因为没有可持续记忆而崩掉
- 记忆问题不只是 retrieval 问题，本质上也是系统边界问题

## 你先要抓住什么

- 记忆不等于把所有历史都塞回上下文
- 短期 thread state、长期 durable memory、可检索外部记录不是同一个东西
- 成熟系统通常会同时使用：session state、memory store、summary、trace 和外部检索

## 常见层次

- `working memory`：当前任务临时需要的信息
- `thread / session memory`：一个会话内持续有效的状态
- `semantic memory`：稳定事实、偏好、配置、知识
- `episodic memory`：过去任务和经验记录
- `procedural memory`：逐渐稳定化的做事方式和默认流程
- `retrieval memory`：需要时再从外部检索回来的记忆

## 真正难的地方

- 什么该记，什么不该记
- 这条内容是 thread state 还是 durable memory
- 写入是否可靠、可审计、可修正
- 历史如何压缩，否则上下文成本会失控
- 错误记忆如何撤销、过期、纠偏

## 两种很重要的写入方式

### `hot-path memory`

- 在执行过程中即时写入
- 好处是及时
- 问题是更容易污染系统，也更吃 latency

### `background memory`

- 先保留 trace / transcript
- 再在后台抽取、合并、纠偏
- 更适合长期运行 agent

## 为什么 OpenClaw 值得学

`OpenClaw` 很适合拿来理解 durable memory，因为它把 memory 放进 workspace 中，变成可读、可写、可编辑的系统对象，而不是把“记忆”神秘化。

## 为什么 LangGraph / LangMem 这类思路也重要

这类系统把 memory 明确拆成：

- 短期 thread/checkpoint
- 长期 store
- hot-path 写入
- background consolidation

这很能代表 agent 工程的实际方向。

## 学习这页最该记住什么

- 记忆不是“模型自己记住”
- 记忆是系统如何组织状态、事实、经验和恢复能力

## 典型系统案例

- [[../09-Systems/OpenClaw|OpenClaw]]
- [[../09-Systems/OpenClaw 工作原理与架构|OpenClaw 工作原理与架构]]
- [[../09-Systems/ChatGPT Agent|ChatGPT Agent]]

## 从工程角度继续往下读

- [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../../AI-Engineering/07-Topics/长期运行 Agent 的记忆系统|长期运行 Agent 的记忆系统]]
- [[../../AI-Engineering/07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]
- [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]

## 相关

- [[Agent]]
- [[Tool Use]]
- [[Planning and Control]]
- [[Long Context]]
- [[RAG]]
- [[A2A（Agent-to-Agent）与协作协议]]
- [[../07-Maps/AI Agent Capability Map|AI Agent Capability Map]]
