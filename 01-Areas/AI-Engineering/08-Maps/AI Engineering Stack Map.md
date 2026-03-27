---
title: AI Engineering Stack Map
type: map
status: learning
tags:
  - ai/maps
created: 2026-03-13
updated: 2026-03-26
---

# AI Engineering Stack Map

```mermaid
flowchart TD
  D["Data Pipelines"] --> T["Training Stack Overview"]
  T --> DT["Distributed Training"]
  DT --> INF["Infrastructure (GPU-TPU)"]
  INF --> ET["Experiment Tracking"]
  ET --> EV["Evaluation and Benchmarks"]
  EV --> PR["Prompt Registry / Datasets / Evals"]
  PR --> REG["Model Registry and Deployment"]
  REG --> SRV["Serving and Scaling"]
  SRV --> OPT["Inference Optimization"]
  OPT --> KV["KV Cache / Prefill-Decode / Continuous Batching"]
  KV --> DS["Disaggregated Serving 与推理数据面"]
  SRV --> ON["Online Evals / Human Feedback / Annotation"]
  ON --> OBS["LLMOps / AgentOps / Observability"]
  OBS --> AG["Agent Runtime Architecture"]
  AG --> HAR["Harness Engineering"]
  HAR --> EVALH["Eval Harness 与 Regression Suites"]
  AG --> SEC["Agent Security / Approval"]
  AG --> MEM["Long-Running Agent Memory"]

  subgraph systems["Cross-Cutting Systems"]
    MLF["[[../../AI-Learning/09-Systems/MLflow|MLflow]]"]
    WNB["[[../../AI-Learning/09-Systems/Weights & Biases Platform|Weights & Biases Platform]]"]
    LFS["[[../../AI-Learning/09-Systems/Langfuse|Langfuse]]"]
    PHX["[[../../AI-Learning/09-Systems/Arize Phoenix|Arize Phoenix]]"]
    PFO["[[../../AI-Learning/09-Systems/Promptfoo|Promptfoo]]"]
  end

  ET --> MLF
  ET --> WNB
  EV --> PFO
  EV --> PHX
  PR --> LFS
  PR --> MLF
  REG --> MLF
  ON --> PHX
  ON --> LFS
  OBS --> LFS
  OBS --> PHX
```

## 地图目标

- 用一张图串起数据、训练、评测、推理、部署、LLMOps 和 agent runtime 全链路

## 怎么读

- 左半边更偏经典 AI engineering 生命周期
- 中间是 `MLOps / LLMOps` 的治理与发布主线
- 右半边是 inference 与 agent runtime 的生产化延伸

## 关联

- [[../07-Topics/主题索引|主题索引]]
- [[MLOps 与 LLMOps 工程图]]
- [[Inference and Serving Map]]
- [[Agent Runtime Engineering Map]]
