---
title: Background Agents
type: topic
status: seed
tags:
  - ai/engineering
  - ai/agent-ops
  - ai/coding-agent
created: 2026-03-22
updated: 2026-03-22
---

# Background Agents

## 为什么重要

- 它标志着 agent 从“同步对话助手”走向“异步任务执行系统”
- 很多 coding agent 的真正价值，不在于当面回答得多快，而在于能否在后台持续推进任务

## 系统视角

`Background Agent` 不是单纯把一次请求放进队列里，它解决的是：

- 任务如何在用户不盯着的情况下继续推进
- agent 在什么环境里执行
- 中间状态怎么保存和汇报
- 结果如何安全地回到主工作流

所以它通常涉及：

- detached execution
- isolated environment
- progress reporting
- result handoff
- approval and review loop

## 和普通同步 agent 的差别

- 同步 agent 更像“你问我答”
- background agent 更像“你先把任务交给我，我跑完再回来交付结果”

也就是说，产品体验从 `conversation` 变成了 `delegation + progress + review`。

## 核心设计问题

- 后台任务运行在本地、云端，还是托管沙箱中
- 一次任务的状态边界和生命周期如何管理
- 中间产物是否可见，用户能否随时接管
- 长任务如何控制成本、权限和失败恢复
- 多个后台 agent 同时运行时如何避免互相污染

## 关键模块

- task queue：任务接收、调度、重试、取消
- execution environment：本地环境、云端环境、沙箱、worktree
- progress channel：状态更新、日志、阶段性产物
- handoff layer：PR、patch、review、artifact delivery
- controls：审批、预算、网络、工具权限、超时

## 真正难的地方

- 用户以为“后台跑”只是更方便，实际上它会把可见性和可控性问题放大
- 一旦执行环境和主工作区分离，就要处理环境一致性、依赖、凭据和结果回收
- 长时间运行的后台任务非常容易出现“安静失败”

## 常见失败模式

- 后台环境和主 repo 环境不一致，结果无法复现
- agent 跑完了，但结果没有顺利回流到 review / PR 流程
- progress reporting 太弱，用户不知道它卡在哪
- 任务切分不清，一次后台任务吞了太大范围，导致失败成本很高
- 多个后台 agent 同时改相近区域，最后冲突大量出现

## 推荐治理方法

- 让后台 agent 默认处理“边界清晰、可验证、可交付”的任务
- 后台执行必须配套中间状态可见性
- 所有长任务都要有 timeout、retry、cancel、escalation
- 结果交付优先走 PR / patch / review，而不是直接落主分支
- 环境模板、依赖安装和权限边界要尽量标准化

## 学习这页时最该记住什么

- `Background Agents` 的价值不只是“省时间”，而是让 agent 真正变成一个可委托的执行层
- 一旦进入后台模式，工程问题会迅速压过 prompt 问题

## 系统案例

- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/Cursor|Cursor]]
- [[../../AI-Learning/09-Systems/Devin|Devin]]

## 官方资料

- [OpenAI Codex](https://openai.com/codex/)
- [Codex cloud](https://developers.openai.com/codex/cloud)
- [Cursor](https://cursor.com/)
- [Devin Docs](https://docs.devin.ai/)
