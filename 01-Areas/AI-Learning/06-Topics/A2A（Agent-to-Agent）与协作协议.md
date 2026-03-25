---
title: A2A（Agent-to-Agent）与协作协议
type: topic
status: learning
tags:
  - ai/topic
  - ai/agent
  - ai/a2a
  - ai/protocol
created: 2026-03-25
updated: 2026-03-25
---

# A2A（Agent-to-Agent）与协作协议

## 这个主题是什么

`A2A` 可以理解成：让一个 agent 能发现、理解并调用另一个 agent，而不是只把对方当成普通工具。

它讨论的是：

- agent 和 agent 怎么发现彼此
- 怎么暴露能力边界
- 怎么发起任务、跟踪状态、接收事件和产物
- 怎么在不同 runtime、不同公司、不同服务之间协作

## 为什么最近很热

因为 agent 生态开始出现一个很现实的问题：

- 一个团队有自己的 agent runtime
- 另一个团队有自己的垂直 agent
- 两边都不想完全重写成同一套框架

这时大家需要的不是“更多 prompt”，而是一个更清晰的 interop layer。

## 它和 Multi-Agent Systems 的关系

- `Multi-Agent Systems` 更偏系统结构：怎么分工、怎么协作、怎么聚合
- `A2A` 更偏协议：不同 agent 之间怎么通信和交付任务

也就是说：

- multi-agent 是架构视角
- A2A 是协议和互操作视角

## 它和 MCP 的关键差异

这是最容易混淆的一点。

### `MCP`

更像：

- host 调 tool / resource / prompt
- 把外部能力接成标准化接口

### `A2A`

更像：

- agent 调另一个 agent
- 对方可能是个完整任务系统，而不只是一个函数或数据库

一个很直观的区分是：

- `MCP` 让 agent 去用工具
- `A2A` 让 agent 去找另一个 agent 协作

## 一个典型 A2A 系统会包含什么

- `Agent Card`：对外说明自己是谁、擅长什么、怎么调用
- `task lifecycle`：任务提交、处理中、需要输入、完成、失败
- `events / streaming`：中间状态不是黑盒，而是可以订阅
- `artifacts`：结果可能不是一句话，而是文件、结构化产物、链接
- `auth / trust`：不同 agent 之间如何授权与隔离

## 为什么它值得学

因为它代表 agent 生态开始从“单体 agent app”走向“agent 网络”。

这会带来几个重要变化：

- 协作不再只发生在一个 runtime 内部
- 边界、身份和能力声明变得更重要
- debugging 和 trust 会比单 agent 难很多

## 什么时候它真正有价值

- 不同团队或不同厂商的 agent 要协作
- 远端 agent 已经是完整系统，不适合降格为普通工具
- 任务天然要跨组织、跨平台、跨上下文

## 什么时候先别急着上 A2A

- 其实一个 supervisor + worker 就够了
- 所有 agent 都在同一个 runtime 里，没必要先协议化
- 你连内部任务边界和状态治理都还没理顺

## 学习时最该记住什么

A2A 不是“比 MCP 更高级”。

更准确地说：

- `CLI` 是直接动作面
- `MCP` 是工具接入层
- `A2A` 是 agent 协作层
- `Harness / App Server` 是工作台与任务控制层

它们解决的不是同一个问题。

## 推荐继续往下读

- [[Multi-Agent Systems]]
- [[Agent Memory]]
- [[../../AI-Engineering/07-Topics/A2A 与 Multi-Agent Coordination|A2A 与 Multi-Agent Coordination]]
- [[../../AI-Engineering/07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]
- [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]

## 相关

- [[Multi-Agent Systems]]
- [[MCP（Model Context Protocol）]]
- [[Tool Use]]
- [[../07-Maps/AI Agent Capability Map|AI Agent Capability Map]]
