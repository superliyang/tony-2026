---
title: Delegation and Task-Oriented Agents
type: topic
status: seed
tags:
  - ai/engineering
  - ai/agent-runtime
  - ai/coding-agent
created: 2026-03-22
updated: 2026-03-22
---

# Delegation and Task-Oriented Agents

## 为什么重要

- agent 产品正在从“协作式问答”走向“任务委托式执行”
- 这会改变我们设计 prompt、任务边界、审批流和结果验收的方式

## 系统视角

`Delegation` 的核心不是把一句话丢给模型，而是把一个可执行任务正式交给系统：

- 目标要足够清晰
- 边界要可控
- 结果要可验收
- 失败要可回退

所以 task-oriented agent 通常要求：

- explicit task contract
- environment ownership
- intermediate progress
- result handoff
- acceptance criteria

## 协作式 agent 和委托式 agent 的差别

- 协作式 agent 更像 pair partner
- 委托式 agent 更像可管理的 worker

协作式更适合：

- 高频互动
- 连续修改
- 人类持续在回路中

委托式更适合：

- 目标清晰的子任务
- 可独立推进的工程工作
- 中途不需要频繁人工确认的任务

## 关键设计问题

- 什么样的任务适合委托，什么样的不适合
- 任务说明应该写到什么粒度
- agent 失败后如何恢复，而不是从头来过
- 如何让委托结果自然回到审查流、测试流和合并流

## 常见任务模式

- implementation task：实现一个明确功能
- investigation task：定位 bug、阅读代码、产出结论
- review task：做代码审查、风险识别、测试建议
- maintenance task：清理、重构、升级、修文档

## 真正难的地方

- 任务边界不清，agent 很容易“自己扩 scope”
- 要求太模糊时，agent 只能猜产品意图
- 缺少验收标准时，结果看起来完成，其实不满足预期
- 一旦把太多高风险动作自动化，委托就会变成失控

## 推荐治理方法

- 每个委托任务都尽量回答：目标、范围、限制、验收标准、输出形式
- 高风险任务保持 human-in-the-loop
- 委托型 agent 优先做“高上下文但低主观性”的工作
- 让测试、PR、diff、日志成为委托结果的标准回收形式

## 和 background agents 的关系

- `background agent` 解决“在哪里跑、怎么跑、如何异步交付”
- `delegation` 解决“什么任务该交、怎么交、交付标准是什么”

两者一起，才形成真正可用的任务代理系统。

## 学习这页时最该记住什么

- 委托不是“更高级的 prompt”，而是更明确的任务契约设计
- 任务型 agent 的上限，往往取决于任务边界与验收设计，而不是模型本身

## 系统案例

- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/Devin|Devin]]
- [[../../AI-Learning/09-Systems/Manus|Manus]]
- [[../../AI-Learning/09-Systems/ChatGPT Agent|ChatGPT Agent]]

## 官方资料

- [Codex cloud](https://developers.openai.com/codex/cloud)
- [Cursor](https://cursor.com/)
- [Introducing Devin](https://cognition.ai/blog/introducing-devin)
- [ChatGPT agent](https://help.openai.com/en/articles/11752874-chatgpt-agent)
