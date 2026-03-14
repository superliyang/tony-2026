---
title: Inference Optimization
type: topic
status: seed
tags:
  - ai/engineering
created: 2026-03-13
updated: 2026-03-13
---

# Inference Optimization

## 为什么重要

- 推理成本决定规模化部署能力

## 系统视角

训练决定模型能做什么，推理优化决定这些能力能不能被广泛、稳定、低成本地用起来。推理优化关心的是：

- 每次请求要花多少算力和显存
- 延迟能不能满足交互体验
- 吞吐能不能支撑并发业务

在真实产品里，这往往比单纯提升 benchmark 更关键。

## 关键问题

- 延迟与吞吐如何权衡
- 量化与蒸馏的边界在哪
- 推理栈的瓶颈来自模型还是系统

## 关键手段

- 量化、蒸馏、裁剪
- KV cache 优化
- 批处理与调度

## 优化通常发生在哪几层

- 模型层：量化、蒸馏、结构裁剪
- runtime 层：kernel 优化、图编译、cache 管理
- 调度层：batching、prefill/decode 调度、资源分配
- 产品层：请求合并、上下文截断、缓存命中

## 常见工程权衡

- 更低延迟 vs 更高吞吐
- 更高模型质量 vs 更低显存占用
- 更长上下文 vs 更高单次成本

## 学习这页时最该记住什么

- 推理优化不是“压榨模型”，而是“让能力可交付”
- 很多模型路线最终能否胜出，取决于它的推理经济性

## 相关主题

- [[Serving and Scaling]]
- [[Infrastructure (GPU-TPU)]]
- [[Model Registry and Deployment]]

## 相关实体

- [[../01-Stacks/LLM Inference Stack|LLM Inference Stack]]
- [[../02-Frameworks/vLLM|vLLM]]
