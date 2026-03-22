# AI-Engineering

> AI 工程体系：训练、框架、工具链与部署

## 快速入口

- [[07-Topics/Topics Index|Topics Index]]
- [[08-Maps/Maps Index|Maps Index]]
- [[07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[07-Topics/Background Agents|Background Agents]]
- [[08-Maps/Agent Runtime Engineering Map|Agent Runtime Engineering Map]]
- [[08-Maps/Coding Agent Workflow Engineering Map|Coding Agent Workflow Engineering Map]]

## 目录

```text
AI-Engineering/
├── 00-Inbox/
├── 01-Stacks/
├── 02-Frameworks/
├── 03-Training/
├── 04-Evaluation/
├── 05-Deployment/
├── 06-Projects/
├── 07-Topics/
├── 08-Maps/
├── 09-Templates/
└── README.md
```

## 定位

这里关注的不是“哪个公司发布了什么模型”，而是：

- 一个 AI 系统如何被训练出来
- 它如何被评测、优化、上线和运维
- 开源框架、基础设施和工具链各自扮演什么角色

## 建议主线

1. 先从 [[07-Topics/Training Stack Overview|Training Stack Overview]] 建立全局视角
2. 再学习数据、训练、评测、推理、部署五个阶段
3. 最后把框架、开源生态、安全与成本问题串起来看

## 当前重点模块

- 工程栈：[[01-Stacks/Stacks Index|Stacks Index]]
- 框架：[[02-Frameworks/Frameworks Index|Frameworks Index]]
- 训练：[[03-Training/Training Index|Training Index]]
- 数据：[[07-Topics/Data Pipelines|Data Pipelines]]、[[07-Topics/Tokenization|Tokenization]]
- 训练：[[07-Topics/Distributed Training|Distributed Training]]、[[07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]]
- 评测：[[07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]、[[07-Topics/Experiment Tracking|Experiment Tracking]]
- 推理与部署：[[07-Topics/Inference Optimization|Inference Optimization]]、[[07-Topics/Serving and Scaling|Serving and Scaling]]、[[07-Topics/Model Registry and Deployment|Model Registry and Deployment]]
- Agent 系统：[[07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]、[[07-Topics/Session and Memory Design|Session and Memory Design]]、[[07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]、[[07-Topics/Background Agents|Background Agents]]、[[07-Topics/Delegation and Task-Oriented Agents|Delegation and Task-Oriented Agents]]、[[07-Topics/Multi-Agent Coding Workflow|Multi-Agent Coding Workflow]]
- 工程生态：[[07-Topics/Frameworks (PyTorch-JAX-TensorFlow)|Frameworks (PyTorch-JAX-TensorFlow)]]、[[07-Topics/Open-Source Ecosystem|Open-Source Ecosystem]]

## 使用建议

- 先从 Topics Index 建立主线问题
- 再按需要补充结构化卡片
- 如果你是从 `AI-Learning/09-Systems/OpenClaw` 过来的，就顺着 Agent Runtime 这条线读
