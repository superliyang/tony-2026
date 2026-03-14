---
title: Frameworks (PyTorch-JAX-TensorFlow)
type: topic
status: seed
tags:
  - ai/engineering
created: 2026-03-13
updated: 2026-03-13
---

# Frameworks (PyTorch-JAX-TensorFlow)

## 为什么重要

- 框架决定开发体验、可移植性和优化空间
- 很多工程决策其实是在选“生态”和“工作方式”，不只是选 API

## 框架在工程链中的位置

框架连接了三层东西：

- 上层的模型表达与研究实验
- 中间的自动求导、编译和分布式执行
- 下层的硬件、运行时和部署工具

所以选框架本质上是在选一个完整生态。

## 核心问题

- PyTorch、JAX、TensorFlow 各自适合什么类型的团队和任务
- eager execution、graph compilation 和自动并行对工程有什么影响
- 框架选择如何影响部署、调试和社区资源

## 对比维度

- 研究友好性
- 编译与性能优化能力
- 分布式训练生态
- 部署与生产化能力
- 社区与开源资源

## 学习时重点看什么

- 不要只比较“语法喜好”，要比较工程闭环能力
- 框架往往和训练基础设施、推理栈、监控工具绑定出现
- 很多团队不是只用一个框架，而是训练与部署拆开选型

## 粗粒度理解三者差异

- PyTorch：研究和工程平衡最好，生态最广，今天的大模型训练主线最常见
- JAX：编译变换能力强，适合追求系统化优化和函数式风格的团队
- TensorFlow：生产化经验深，但在当前前沿大模型训练主线上存在感较弱

## 选型时常见误区

- 只看社区热度，不看团队已有能力
- 只看训练体验，不看推理和部署配套
- 只看单个 benchmark，不看维护成本和人才供给

## 学习这页时最该记住什么

- 框架选型是团队工程能力的放大器
- 真正重要的不是“谁最好”，而是谁更适合当前系统和团队

## 相关主题

- [[Training Stack Overview]]
- [[Distributed Training]]
- [[Open-Source Ecosystem]]
- [[Model Registry and Deployment]]

## 相关实体

- [[../02-Frameworks/PyTorch|PyTorch]]
- [[../02-Frameworks/JAX|JAX]]
- [[../02-Frameworks/TensorFlow|TensorFlow]]
- [[../02-Frameworks/Hugging Face Ecosystem|Hugging Face Ecosystem]]
