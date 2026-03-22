---
title: Agent Failure Cases and Deployment Pitfalls
type: topic
status: learning
tags:
  - ai/applications
  - ai/agent
  - ai/failure
created: 2026-03-22
updated: 2026-03-22
---

# Agent Failure Cases and Deployment Pitfalls

## 这个主题是什么

`Agent Failure Cases and Deployment Pitfalls` 关注的不是模型答错一两次，而是 agent 落地后为什么会在业务上失败、组织上失败、治理上失败。

## 为什么重要

- 很多 agent 项目不是技术不可行，而是上线方式错误
- 失败往往不是一个 bug，而是任务边界、知识源、审批机制、指标体系一起出了问题
- 如果只看成功案例，很容易误以为“能力更强的模型”就能自动解决落地问题

## 典型失败模式

### 1. 任务边界过宽

- 把高风险、不确定、需要深度判断的任务直接交给 agent
- 没有区分“建议模式”和“执行模式”

### 2. 单一事实源缺失

- policy、pricing、合同、客服口径来自多个来源
- agent 回答与正式规则冲突

### 3. 没有升级与审批机制

- 复杂问题不转人工
- 高风险动作没有 approval gate
- 失败恢复路径不明确

### 4. 只看对话效果，不看业务结果

- 用户觉得“看起来聪明”，但真正解决率低
- 没有跟踪 adoption、ROI、handoff quality 和 error cost

### 5. 评测缺失

- 上线前没有任务级 eval
- 上线后没有 drift 监控
- 没有针对高风险边界做回归测试

## 典型案例

- [[../04-Case-Studies/Air Canada Chatbot Liability Case|Air Canada Chatbot Liability Case]]
- [[../04-Case-Studies/Klarna AI Customer Service Assistant|Klarna AI Customer Service Assistant]]
- [[../04-Case-Studies/OpenAI In-House Data Agent|OpenAI In-House Data Agent]]

## 从失败中提炼出的上线原则

- 先选高频、可验证、可回退的任务
- 把知识源统一到单一事实源
- 默认先做人机协作，再逐步扩大自动执行范围
- 为高风险场景设计 policy tests、approval gates 和 escalation paths
- 衡量解决率、接管率、错误成本，而不是只看回答是否流畅

## 相关

- [[Agent Productization]]
- [[Agent Adoption and Change Management]]
- [[Agent ROI and Value Capture]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
- [[../../AI-Engineering/07-Topics/Task Success and Failure Recovery|Task Success and Failure Recovery]]
