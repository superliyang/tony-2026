---
title: Serving and Scaling
type: topic
status: seed
tags:
  - ai/engineering
created: 2026-03-13
updated: 2026-03-13
---

# Serving and Scaling

## 为什么重要

- 直接决定真实用户体验与成本曲线

## 系统视角

serving 关心的是“单个请求怎么跑”，scaling 关心的是“成千上万个请求同时来时怎么稳”。它们共同决定：

- 用户是否觉得快
- 系统是否能扛住峰值
- 单位请求成本是否可接受

## 关键问题

- SLA 如何定义与监控
- 多租户与隔离如何实现
- 异常与峰值如何处理

## 关键模块

- 路由与负载均衡
- 缓存与队列
- 监控与告警

## 真实系统里还要处理什么

- 模型冷热启动
- 多模型路由和 fallback
- 租户隔离与配额
- 流式输出和超时控制
- 容量规划与扩缩容

## 常见失败模式

- 高峰期队列堆积，延迟失控
- 某个模型实例热点过高，负载不均
- 上游 prompt 或上下文长度异常，拖垮整个集群
- 线上版本切换不平滑，出现质量回退

## 学习这页时最该记住什么

- 服务化不是“把模型包个 API”这么简单
- 真正难的是在成本、稳定性、隔离和体验之间找平衡

## 相关主题

- [[Inference Optimization]]
- [[Model Registry and Deployment]]
- [[Security and Privacy]]

## 相关实体

- [[../01-Stacks/LLM Ops Stack|LLM Ops Stack]]
- [[../02-Frameworks/vLLM|vLLM]]
