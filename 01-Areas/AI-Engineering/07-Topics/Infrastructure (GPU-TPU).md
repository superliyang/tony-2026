---
title: Infrastructure (GPU-TPU)
type: topic
status: learning
tags:
  - ai/engineering
created: 2026-03-13
updated: 2026-03-25
---

# Infrastructure (GPU-TPU)

## 为什么重要

- 大模型工程首先受限于算力、显存、网络和存储，而不是只受限于算法
- 基础设施决定训练规模、推理成本和迭代速度
- 在 2026 年这个时间点，很多公司之间真正的差异，已经是 infra 承载能力，而不是只看模型名字

## 系统视角

基础设施不是背景条件，而是 AI 工程的“物理边界”。模型再好，如果：

- 显存不够
- 网络太慢
- 存储吞吐不够
- 集群调度不稳定

训练和推理都无法达到预期。

## 现在看基础设施，要分清楚哪三层

### 1. accelerator layer

- GPU / TPU / CPU 协同
- 单卡性能
- 显存容量
- 卡间互联

### 2. cluster substrate

- 高速网络
- 对象存储 / 文件系统
- checkpoint / restore
- Kubernetes / bare metal / scheduler

### 3. AI-native cloud layer

- capacity reservation
- managed Kubernetes for AI
- tenant / quota / cost control
- training and inference lifecycle

这一层就是为什么 `CoreWeave` 这种公司值得单独看。

## GPU vs TPU，不要只看芯片名字

真正的工程判断通常是：

- 软件栈成熟度
- 运维经验
- 生态兼容性
- 性能可预测性
- 调度与恢复能力

而不是只看纸面峰值。

## 真实系统里最难的地方

- GPU 利用率低，但不是因为模型差，而是数据/通信没跟上
- 跨机拓扑不合理，导致扩容后反而变慢
- checkpoint 过大，恢复一次需要很长时间
- 推理服务卡在显存和 KV cache，而不是算力峰值
- GPU cloud 的容量、网络和存储策略，直接影响产品上线节奏

## 学习这页时最该记住什么

- AI 工程很多时候首先是系统工程，其次才是模型工程
- 理解硬件和集群约束，会直接提升你对训练与部署问题的判断力
- 现在讨论基础设施，已经不能只停在 GPU / TPU，而要把 `AI-native cloud` 一起看进去

## 推荐继续往下读

- [[Inference Optimization]]
- [[Serving and Scaling]]
- [[../../AI-Learning/06-Topics/AI 基础设施与 GPU Cloud|AI 基础设施与 GPU Cloud]]
- [[../../AI-Learning/09-Systems/CoreWeave Cloud|CoreWeave Cloud]]
- [[../../AI-Learning/09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]]

## 资料

- [NVIDIA AI](https://www.nvidia.com/en-us/ai/)
- [CoreWeave Platform](https://www.coreweave.com/platform)
- [CoreWeave Docs](https://docs.coreweave.com/)
