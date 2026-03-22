---
title: Multi-Agent Systems
type: topic
status: draft
tags:
  - ai/topic
  - ai/agent
  - ai/multi-agent
created: 2026-03-22
updated: 2026-03-22
---

# Multi-Agent Systems

## 这个主题是什么

`Multi-Agent Systems` 关注多个 agent 如何分工、协作、交接和聚合，而不是把所有事情都交给一个单体 agent。

## 为什么重要

- 单 agent 很容易在复杂任务中变成巨大的黑盒
- 多 agent 系统更接近真实组织：研究、执行、评审、汇总可以分角色处理
- 但它也会把协调、冲突、状态共享和治理问题明显放大

## 你先要抓住什么

- multi-agent 不是“多开几个模型实例”
- 真正关键的是角色边界、任务切分、共享状态和结果聚合
- 并不是 agent 越多越好；很多任务一个主 agent + 少量专职 agent 就够了

## 常见角色

- planner：拆任务、分配子任务
- worker：执行具体动作
- reviewer：检查结果、找错误、补测试
- coordinator：汇总结果、决定是否继续下一轮

## 真正难的地方

- scope overlap：多个 agent 改到同一块
- hidden dependency：子任务之间暗含依赖
- coordination overhead：调度成本反而超过收益
- context divergence：各 agent 的假设逐渐不一致

## 什么时候值得用

- 任务天然可拆分
- 子任务边界清楚
- 需要并行吞吐
- 需要把“执行”和“评审”显式分离

## 从工程角度继续往下读

- [[../../AI-Engineering/07-Topics/Delegation and Task-Oriented Agents|Delegation and Task-Oriented Agents]]
- [[../../AI-Engineering/07-Topics/Background Agents|Background Agents]]
- [[../../AI-Engineering/07-Topics/Multi-Agent Coding Workflow|Multi-Agent Coding Workflow]]

## 相关

- [[Agent]]
- [[Planning and Control]]
- [[Coding Agents]]
- [[AI Assistant]]
- [[../09-Systems/Devin|Devin]]
- [[../09-Systems/Codex|Codex]]
- [[../07-Maps/AI Agent Capability Map|AI Agent Capability Map]]
