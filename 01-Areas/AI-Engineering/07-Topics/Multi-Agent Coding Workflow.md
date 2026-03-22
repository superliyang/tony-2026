---
title: Multi-Agent Coding Workflow
type: topic
status: seed
tags:
  - ai/engineering
  - ai/coding-agent
  - ai/workflow
created: 2026-03-22
updated: 2026-03-22
---

# Multi-Agent Coding Workflow

## 为什么重要

- 单个 coding agent 已经能提高效率，但真正进入团队工作流后，问题会变成“多个 agent 怎么并行协作”
- 这不仅是产品问题，也是 repo、review、branch、CI 和 ownership 的工程问题

## 系统视角

`Multi-Agent Coding Workflow` 关注的是：

- 一个任务如何被拆成多个可并行子任务
- 多个 agent 如何避免改到同一片区域
- 每个 agent 的产物如何汇合到 review / CI / merge 流程

所以它通常包含：

- task decomposition
- worktree / branch isolation
- role separation
- result aggregation
- review and merge control

## 常见角色分工

- implementer agent：负责改代码
- reviewer agent：负责查 bug、提测试建议
- investigator agent：负责读代码、查依赖、做根因分析
- maintenance agent：负责升级依赖、修文档、批量修改

## 为什么它比单 agent 难很多

- 单 agent 失败通常只是一次任务失败
- 多 agent 失败会把冲突、重复、遗漏、错误合并一起放大

最常见的问题是：

- scope overlap
- hidden dependency
- merge conflict
- inconsistent assumptions
- duplicated work

## 关键设计点

### 1. 明确写作业边界

多 agent 并行时，最重要的是把文件、模块、责任边界切清楚。

### 2. 结果不要直接进主线

多 agent 产物优先进入：

- patch
- branch
- worktree
- PR

### 3. 人类要在聚合点上把关

并行 agent 最该让人类参与的地方不是每一步，而是：

- 任务拆分时
- 最终聚合时
- 高风险变更时

### 4. 评审 agent 要和实现 agent 分开

如果让同一个 agent 同时负责实现和评审，收益通常会下降。

## 典型工作流

1. 人类或上层 orchestrator 拆任务
2. 多个 agent 分别在独立环境里执行
3. 每个 agent 产出 patch / PR / review note
4. CI 与 reviewer agent 做第二层筛查
5. 人类在最终合并前做判断

## 真正难的地方

- 多 agent 看起来快，但对 repo hygiene、测试体系、评审机制要求更高
- 如果任务拆分能力不足，多 agent 只会放大混乱
- 并行执行虽然提高吞吐，但也更需要统一规则、共享上下文和结果汇总

## 推荐治理方法

- 先从“一个实现 agent + 一个 review agent”开始，而不是一上来全并行
- 让每个 agent 只负责一类输出
- 高风险文件、共享核心模块尽量单线程处理
- 所有 agent 输出都要回到统一 diff / CI / PR 流程里
- 为多 agent 工作流准备明确的任务模板和 merge checklist

## 学习这页时最该记住什么

- multi-agent coding 不是“多开几个窗口”，而是把软件工程流程显式拆成可并行、可治理、可回收的工作单元
- 真正的难点在 orchestration，不在模型能不能多生成一点代码

## 系统案例

- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/Cursor|Cursor]]
- [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
- [[../../AI-Learning/09-Systems/Devin|Devin]]

## 官方资料

- [OpenAI Codex](https://openai.com/codex/)
- [Codex cloud](https://developers.openai.com/codex/cloud)
- [Cursor](https://cursor.com/)
- [Claude Code overview](https://code.claude.com/docs/en/overview)
- [Devin Docs](https://docs.devin.ai/)
