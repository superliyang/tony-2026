---
title: Langfuse
type: project
status: learning
domain: ai-open-source
category: Eval、Observability 与 Guardrails
organization: Langfuse
repo: https://github.com/langfuse/langfuse
local_fit: high
mac_fit: high
created: 2026-04-03
updated: 2026-04-03
---

# Langfuse

## 它是什么

`Langfuse` 是一个开源的 `LLM engineering platform`。如果只看最表层，它像“LLM observability”；但如果按工程边界看，它其实同时覆盖了四块：

- observability / tracing
- prompt management
- evaluation
- platform / data plane

它不是单纯日志系统，也不是执行 runtime，而是把 `trace -> prompt -> eval -> metrics -> release comparison` 收进一个统一工作台。

## 为什么现在值得重点关注

现在很多团队已经不再卡在“模型能不能调通”，而是卡在：

- 哪个 prompt 版本退化了
- 哪个 tool span 出错了
- 哪个 dataset run 揭示了 regression
- 哪个 release 提高了 latency 或 cost
- 哪条 agent workflow 在生产里开始不稳定

`Langfuse` 值得学，不是因为它是一个又新的平台，而是因为它把“可观察、可评测、可回归、可治理”这些长期痛点，收成了一套工程控制面。这个定位和只做 tracing 或只做离线 eval 的项目都不一样。

## 它在 stack 的哪一层

更准确地说，`Langfuse` 属于：

- `LLMOps / AgentOps` 控制层
- `observability + eval + prompt` 一体化平台层
- 不是模型 runtime
- 不是训练框架
- 不是 serving data plane

如果用我们当前知识库的坐标系：

- `LangGraph` 更像执行内核
- `OpenClaw` 更像 assistant runtime / operating layer
- `vLLM` / `SGLang` 更像 serving data plane
- `Langfuse` 更像“看、评、比、管”的工作台

## 核心组件与架构

按官方文档，现在可以把它收成几个关键部件：

### 1. Observability

它的 trace 不只看 LLM 调用，还会把 retrieval、embedding、API 调用和非 LLM 逻辑都接进来。官方文档还强调：

- 支持 sessions / user tracking
- agent 可以表示成 graph
- 可以通过 Python / JS SDK、50+ integrations、OpenTelemetry 或 LLM gateway 接入

这意味着它不是一个“专门给某个框架做的 tracing UI”，而是尽量站在更开放的 telemetry 面上。来源：[Langfuse Overview](https://langfuse.com/docs)、[Observability Overview](https://langfuse.com/docs/observability/overview)

### 2. Prompt Management

它把 prompt 从“代码里的字符串”提升成了可版本化对象：

- 可创建、编辑、协作
- 可用 label 部署到不同环境
- 可在 Playground 测试
- 可把 prompt 版本和 traces 连起来看

这点很关键，因为很多团队的 prompt 问题不是“想不出提示词”，而是“不知道生产里到底跑的是哪个版本”。来源：[Prompt Management Overview](https://langfuse.com/docs/prompt-management/overview)

### 3. Evaluation

它把评测放成一等公民，而不是附属脚本。官方文档强调：

- LLM-as-a-judge
- user feedback
- manual labeling / annotation queues
- custom evals
- datasets 与 experiments
- production trace 上的在线评测

也就是说，它同时支持：

- 开发期的离线实验
- 生产期的在线质量监控

这正是 `LLMOps / AgentOps` 真正难的地方。来源：[Evaluation Overview](https://langfuse.com/docs/evaluation/overview)

### 4. Self-hosting / Platform 底座

官方 self-hosting 文档说明了它的运行面：

- `Langfuse Web`
- `Langfuse Worker`
- `Postgres`
- `ClickHouse`
- `Redis/Valkey`
- 可选 LLM API / gateway

这说明它并不是一个轻薄前端，而是带有明确数据平台形态的系统。尤其 `ClickHouse` 的引入，说明它对 traces / observations / scores 这类 OLAP 风格查询是认真设计过的。来源：[Self-Hosting](https://langfuse.com/self-hosting)、[Kubernetes Helm](https://langfuse.com/self-hosting/deployment/kubernetes-helm)

## 核心对象模型

从工程视角看，最该抓住的是这些对象：

- trace
- observation / span
- session
- user
- prompt version
- score
- dataset
- experiment

这组对象连起来，才让它从“看日志”变成“做 release comparison 和质量治理”。

## 最适合它的场景

### 很适合

- agent / workflow 已经跑起来，开始需要真正可调试
- 需要把 prompt、trace、dataset、score 串起来
- 需要做 release comparison
- 有 self-hosting / data control 要求
- 希望 observability 和 eval 不分家

### 没那么适合

- 你现在只是想跑一个极简 demo
- 没有 trace / eval / release 需求
- 团队还没进入 agent 或 LLM app 的长期运营阶段
- 你只想要一个轻量单机评测脚本

## 和相邻项目怎么区分

### 和 Phoenix

- `Phoenix` 更偏 tracing / evaluation 分析体验
- `Langfuse` 更明显往 `prompt + dataset + score + release comparison` 一体化平台走

### 和 Promptfoo

- `Promptfoo` 更偏 pre-release eval、CI、red-team
- `Langfuse` 更偏线上 tracing、dataset runs、prompt lifecycle、production monitoring

### 和 MLflow / W&B

- `MLflow` / `W&B` 更宽，覆盖传统 ML 生命周期
- `Langfuse` 更专注 LLM / agent 这条 control surface

## 自托管与运行判断

如果团队有更强的数据控制要求，`Langfuse` 的 self-hosting 路线很有吸引力。官方文档显示：

- 可本地、云上或 on-prem 部署
- 可用 Helm 在 Kubernetes 上部署
- 也有 Terraform 路线
- 可完全离线 / air-gapped 运行

这使它对受监管团队、平台团队、B2B 团队特别有吸引力。这个判断来自官方 self-hosting 文档和 open-source FAQ。来源：[Self-Hosting](https://langfuse.com/self-hosting)、[Why is Langfuse Open Source?](https://langfuse.com/docs/open-source)

## 对我来说最重要的学习价值

如果你的目标不是“知道有这个项目”，而是提升工程判断力，那 `Langfuse` 最值钱的地方在于：

1. 它帮助你理解 agent 平台为什么不能只看 runtime
2. 它帮助你理解 prompt / eval / trace 为什么必须进入统一控制面
3. 它帮助你看懂 `AgentOps` 真正的长期成本在 observability 和 release governance
4. 它帮助你建立“平台控制面”而不是“单点功能”的视角

## 推荐的学习动作

### 第一步：先看它的边界

先别急着装。先回答：

- 它到底是 tracing 工具，还是平台控制面？
- 它和 `Phoenix` / `Promptfoo` / `MLflow` 的边界在哪？

### 第二步：按对象读文档

建议按这个顺序读官方文档：

1. Overview
2. Observability
3. Prompt Management
4. Evaluation
5. Self-hosting

### 第三步：做一个最小平台心智图

把这些对象连起来：

- trace
- prompt version
- score
- dataset
- experiment
- release decision

只要这张图画出来，你对 `Langfuse` 的理解就已经超过“它是 observability 平台”那种浅层描述了。

## 下一步实验建议

1. 在本地或测试环境里只接 tracing，感受它如何表示 session / agent graph
2. 再接 prompt management，看 prompt 版本是不是能真正进入工作流
3. 最后接 dataset + eval + release comparison，看它是否真的形成 control surface

## 风险与边界

- 不要把它误当 runtime
- 不要把它误当通用 APM 的完全替代
- 不要在团队还没有最小 trace discipline 时就期待它解决所有工程混乱
- 自托管虽然强，但也意味着你要接受它的运维复杂度和数据存储成本

## 适合什么场景

- local_fit: `high`
- mac_fit: `high`
- production_fit: `high`
- learning_fit: `high`

## 相关项目

- [[Phoenix]]
- [[Promptfoo]]
- [[LangGraph]]
- [[LangMem]]
- [[../04-Patterns/Eval Gate 与 Observability 闭环|Eval Gate 与 Observability 闭环]]

## 官方入口

- [Langfuse Docs](https://langfuse.com/docs)
- [Langfuse GitHub](https://github.com/langfuse/langfuse)
- [Langfuse Self-Hosting](https://langfuse.com/self-hosting)

## 关联

- [[项目索引|项目索引]]
- [[../01-Categories/Eval、Observability 与 Guardrails|Eval、Observability 与 Guardrails]]
- [[../02-Organizations/Langfuse|Langfuse]]
- [[../../AI-Learning/09-Systems/Langfuse|Langfuse]]
- [[../../AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]
- [[../../AI-Engineering/07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]
