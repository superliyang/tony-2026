---
title: Tokenization
type: topic
status: seed
tags:
  - ai/engineering
created: 2026-03-13
updated: 2026-03-13
---

# Tokenization

## 为什么重要

- 决定上下文长度、成本与语义分布
- 直接影响多语言与领域适配能力

## 它在系统里扮演什么角色

tokenization 是训练前最早发生、但会持续影响整个生命周期的步骤。模型不直接看“文字”，而是看 token 序列。于是：

- 输入能被切成多长，影响上下文窗口利用率
- 同一句话被切成多少 token，影响推理成本
- 不同语言和领域术语如何被切分，影响模型学习效率

## 为什么它不是小细节

- token 切得不合理，会让模型把本来应该整体理解的信息拆碎
- 多语言场景下，不同语言 token 密度差异会直接影响公平性和成本
- 长上下文模型是否真的有用，往往先取决于 token 利用率而不是标称窗口大小

## 关键问题

- 词表规模如何影响效率
- 领域特化词表是否必要
- Tokenization 对模型偏差有何影响

## 常见方法

- BPE / Unigram / WordPiece
- SentencePiece

## 常见工程权衡

- 更大词表：单条输入 token 更少，但词表管理和泛化更复杂
- 更小词表：泛化更稳，但上下文成本更高
- 通用词表：部署方便，但领域术语切分可能很差
- 专用词表：领域任务更好，但跨域迁移变弱

## 在大模型时代要特别关注什么

- 长文档任务里 token 数往往比字符数更重要
- 代码、中文、日文、表格、日志等数据的 tokenization 行为差异很大
- tokenizer 版本本身就是模型资产的一部分，不能随便替换

## 学习这页时最该记住什么

- tokenization 是成本问题、能力问题，也是产品体验问题
- 不理解 tokenizer，就很难真正理解 context window 和推理价格

## 相关主题

- [[Data Pipelines]]
- [[Training Stack Overview]]
- [[Inference Optimization]]
