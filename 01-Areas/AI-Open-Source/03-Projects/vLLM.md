---
title: vLLM
type: project
status: learning
domain: ai-open-source
category: 推理服务与 Serving 数据面
organization: vLLM Project
repo: https://docs.vllm.ai/en/latest/
local_fit: medium
mac_fit: low
created: 2026-04-03
updated: 2026-04-03
---

# vLLM

## 它是什么

面向高吞吐 serving 的开源推理平台，核心强项在 KV cache、批处理和 OpenAI-compatible serving。

## 为什么值得关注

它是现代推理服务研究的核心样本之一，很多 serving tradeoff 都可以围绕它来学。

## 核心抽象

- KV cache 与 batching
- OpenAI-compatible server
- disaggregated serving 与并行扩展

## 当前建议的学习动作

- 先判断它到底是底座、壳层、平台还是子系统
- 看它和相邻项目是替代关系还是组合关系
- 再决定是本地实验、架构学习，还是生产研究

## 适合什么场景

- local_fit: `medium`
- mac_fit: `low`

## 相关项目

- [[SGLang]]
- [[KServe]]
- [[Ray]]

## 官方入口

- [官方入口](https://docs.vllm.ai/en/latest/)

## 关联

- [[项目索引|项目索引]]
- [[../01-Categories/推理服务与 Serving 数据面|推理服务与 Serving 数据面]]
- [[../02-Organizations/vLLM Project|vLLM Project]]
