# AI-Engineering

> AI 工程体系：训练、框架、工具链、推理、部署、MLOps / LLMOps、AI Security 与 agent 平台

## 快速入口

- [[Learning Progress]]
- [[Resume Note]]
- [[07-Topics/Topics Index|Topics Index]]
- [[08-Maps/Maps Index|Maps Index]]
- [[04-Evaluation/Evaluation Index|Evaluation Index]]
- [[05-Deployment/Deployment Index|Deployment Index]]
- [[07-Topics/Experiment Tracking|Experiment Tracking]]
- [[07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]
- [[07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]
- [[07-Topics/Model Registry and Deployment|Model Registry and Deployment]]
- [[07-Topics/Online Evals、Human Feedback 与 Annotation|Online Evals、Human Feedback 与 Annotation]]
- [[07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]
- [[07-Topics/Enterprise MLOps 与 LLMOps Vendor Tradeoffs|Enterprise MLOps 与 LLMOps Vendor Tradeoffs]]
- [[08-Maps/MLOps 与 LLMOps 工程图|MLOps 与 LLMOps 工程图]]
- [[08-Maps/Enterprise LLMOps Vendor Choice Map|Enterprise LLMOps Vendor Choice Map]]
- [[07-Topics/Security and Privacy|Security and Privacy]]
- [[07-Topics/AI Security Threat Modeling|AI Security Threat Modeling]]
- [[07-Topics/Prompt Injection Defense 与 Tool Safety|Prompt Injection Defense 与 Tool Safety]]
- [[07-Topics/Guardrails、Policy Enforcement 与 Security Gateways|Guardrails、Policy Enforcement 与 Security Gateways]]
- [[07-Topics/Model Supply Chain Security|Model Supply Chain Security]]
- [[07-Topics/AI Security Evaluation 与 Red Teaming|AI Security Evaluation 与 Red Teaming]]
- [[08-Maps/AI Security Engineering Map|AI Security Engineering Map]]
- [[07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]]
- [[07-Topics/Inference Optimization|Inference Optimization]]
- [[07-Topics/Serving and Scaling|Serving and Scaling]]
- [[07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]]
- [[07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]
- [[07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]
- [[06-Projects/项目索引|项目索引]]

## 定位

这里关注的不是“哪个公司发布了什么模型”，而是：

- 一个 AI 系统如何被训练出来
- 它如何被评测、优化、上线和运维
- inference stack 如何从 backend runtime 演进到 serving data plane 和云平台
- `MLOps / LLMOps` 如何把实验、评测、prompt、trace、registry 和反馈回路收成工程主线
- `AI Security` 如何把 prompt、tool、memory、artifact 和 deployment 这些新攻击面纳入系统设计
- 当系统进入 agent 时代后，runtime、memory、security、approval、eval 和 coordination 如何真正组合成一个可治理系统

## 当前重点模块

- MLOps / LLMOps：[[07-Topics/Experiment Tracking|Experiment Tracking]]、[[07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]、[[07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]、[[07-Topics/Model Registry and Deployment|Model Registry and Deployment]]、[[07-Topics/Online Evals、Human Feedback 与 Annotation|Online Evals、Human Feedback 与 Annotation]]、[[07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]、[[07-Topics/Enterprise MLOps 与 LLMOps Vendor Tradeoffs|Enterprise MLOps 与 LLMOps Vendor Tradeoffs]]、[[07-Topics/Open-Source、Self-Hosting 与 Managed LLMOps|Open-Source、Self-Hosting 与 Managed LLMOps]]
- AI Security：[[07-Topics/Security and Privacy|Security and Privacy]]、[[07-Topics/AI Security Threat Modeling|AI Security Threat Modeling]]、[[07-Topics/Prompt Injection Defense 与 Tool Safety|Prompt Injection Defense 与 Tool Safety]]、[[07-Topics/Guardrails、Policy Enforcement 与 Security Gateways|Guardrails、Policy Enforcement 与 Security Gateways]]、[[07-Topics/Model Supply Chain Security|Model Supply Chain Security]]、[[07-Topics/AI Security Evaluation 与 Red Teaming|AI Security Evaluation 与 Red Teaming]]
- 推理系统：[[07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]]、[[07-Topics/Inference Optimization|Inference Optimization]]、[[07-Topics/Serving and Scaling|Serving and Scaling]]、[[07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]]、[[07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]
- Agent 系统：[[07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]、[[07-Topics/Harness Engineering|Harness Engineering]]、[[07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]、[[07-Topics/A2A 与 Multi-Agent Coordination|A2A 与 Multi-Agent Coordination]]、[[07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]
