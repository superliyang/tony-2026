---
title: Cost, Latency, and Safety Tradeoffs
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent-runtime
  - ai/governance
created: 2026-03-22
updated: 2026-03-22
---

# Cost, Latency, and Safety Tradeoffs

## 为什么重要

- agent 系统不是单纯追求“能完成任务”就好
- 真正上线时，团队总是在三类目标之间拉扯：
  - 更便宜
  - 更快
  - 更安全
- 很多架构决策，本质上都是在这三者之间找平衡

## 系统视角

这页不是讨论抽象原则，而是讨论一个现实问题：

- 如果你想让 agent 更安全，往往需要更多审批、更多校验、更多回看
- 如果你想让 agent 更快，往往会减少中间确认和上下文压缩
- 如果你想让 agent 更便宜，可能会限制模型、工具、并行度和上下文长度

所以 tradeoff 不是坏事，它是系统设计的常态。

## 三个最常见的冲突

### 1. 安全 vs 速度

- 更多 approval gates 更安全，但更慢
- 更少人工接入更快，但也更容易出高风险动作

### 2. 成本 vs 质量

- 更小模型、更少上下文、更少工具调用更省钱
- 但复杂任务的完成率和稳定性可能立刻下降

### 3. 延迟 vs 成功率

- 更快返回通常意味着更少规划、更少重试、更少验证
- 但复杂任务可能因此更容易失败

## 判断时最该问的 5 个问题

1. 这个场景能接受多高的失败成本
2. 这个任务是高频低风险，还是低频高风险
3. 用户更在意“马上得到一个答案”还是“晚一点但更稳”
4. 是否需要把高风险动作拆到审批门之后
5. 这个系统的单位价值能否覆盖 agent 成本

## 典型策略

- 低风险查询场景：更偏低延迟
- 中风险 coding 场景：更偏可控执行 + 可恢复
- 高风险外部副作用场景：更偏安全门控和人类审批
- 长任务场景：更偏后台执行与阶段性汇报，而不是一次性同步完成

## 常见误区

- 只追求 completion rate，不看单位成本
- 只追求低延迟，忽视结果回退和恢复成本
- 只追求安全，最后把系统做成“几乎什么都不能干”
- 在所有任务上用同一套 tradeoff，而不是做分层策略

## 推荐治理方法

- 不同任务类型定义不同 SLA 与风险等级
- 把 tradeoff 明确写进产品和工程策略，而不是临时拍脑袋
- 用真实 telemetry 追踪：成本、耗时、成功率、审批率、回滚率
- 把高风险动作和普通动作分开管理

## 系统案例

- [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/Cursor|Cursor]]
- [[../../AI-Learning/09-Systems/ChatGPT Agent|ChatGPT Agent]]

## 相关

- [[Cost Optimization]]
- [[Agent Evaluation and Reliability]]
- [[Human-in-the-Loop and Approval Gates]]
- [[Background Agents]]
- [[../../AI-Learning/06-Topics/Coding Agents|Coding Agents]]
