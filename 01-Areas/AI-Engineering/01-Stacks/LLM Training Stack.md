---
title: LLM Training Stack
type: stack
status: seed
tags:
  - ai/engineering
  - ai/training-stack
created: 2026-03-13
updated: 2026-03-13
---

# LLM Training Stack

## 简介

`LLM Training Stack` 描述的是一个大模型从数据准备到训练完成所依赖的核心系统层次。

## 为什么要单独学它

- 因为训练系统不是一个框架、一个算法或一个集群就能解释清楚的
- 你只有把整条链拆开看，才会明白模型能力为什么会受数据、并行、基础设施和评测共同制约

## 关键层次

- 数据层：采集、清洗、混合、版本控制
- 框架层：PyTorch、JAX、TensorFlow
- 分布式训练层：FSDP、DeepSpeed、Megatron-LM
- 基础设施层：GPU、网络、存储、调度
- 实验与评测层：tracking、benchmark、checkpoint

## 一条典型链路

- 原始数据进入 pipeline，被清洗、切分、去重和版本化
- 数据经过 tokenization 后进入训练框架
- 框架调用分布式训练方案和底层硬件完成训练
- 训练产物进入实验跟踪、评测和 checkpoint 管理
- 评测合格后再流向注册表和部署系统

## 真正的工程难点

- 多层问题会互相放大，例如数据慢会表现成 GPU 利用率低
- 单层优化未必带来全局收益，甚至可能把瓶颈转移到别处
- 大部分问题不能只靠论文思维解决，而要靠系统观

## 学习这页时最该记住什么

- 训练栈是“层层依赖”的生产系统
- 模型训练成不成功，很大程度取决于整条链是否协调

## 学习时重点看什么

- 性能瓶颈通常跨层出现，不只属于某一个工具
- 训练栈是“组合问题”，不是单点问题

## 相关

- [[../07-Topics/Training Stack Overview|Training Stack Overview]]
- [[../07-Topics/Distributed Training|Distributed Training]]
- [[../03-Training/训练索引|训练索引]]
