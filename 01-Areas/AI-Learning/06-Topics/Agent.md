---
title: Agent
type: topic
status: draft
tags:
  - ai/topic
  - ai/agent
created: 2026-03-01
updated: 2026-03-18
---

# Agent

## 这个主题是什么

`Agent` 关注模型如何结合工具、记忆、规划与执行，完成多步任务。

## 为什么重要

- 它把模型从回答问题推进到执行工作
- 也是 AI 产品和自动化工作流的关键方向

## 你先要抓住什么

- agent 不等于“一个更聪明的聊天机器人”
- agent 的核心在于：给定目标后，系统能否自己拆任务、调用工具、根据结果继续推进
- 一个 agent 通常由模型、工具、状态、执行循环和约束机制共同组成

## 常见组成

- 模型：负责理解目标、生成计划、决定下一步
- 工具：搜索、代码执行、数据库、浏览器、API
- 记忆：保存任务上下文或历史结果
- 控制层：限制权限、管理循环、处理失败

## 关键问题

- agent 什么时候比普通 prompt 更有价值
- 为什么很多 agent demo 看起来厉害，但真实生产中很难稳定
- tool use、reasoning、memory 各自扮演什么角色

## 当前关联模型 / 产品

- [[ChatGPT]]
- [[OpenAI API]]
- [[Claude Code]]
- [[DeepSeek API]]
- [[OpenClaw]]

## 作为系统案例

- `OpenClaw` 很适合拿来理解“agent 从概念走向长期运行系统”这一层
- 它强调 gateway、channels、tools、sessions 和 memory，而不只是一个 tool loop demo
- 如果你想继续拆系统层，进入 [[OpenClaw 工作原理与架构]]

## 相关

- [[RAG]]
- [[Coding Agents]]
- [[Developer Tools]]
- [[Reasoning Models]]
- [[OpenClaw]]
- [[OpenClaw 工作原理与架构]]
