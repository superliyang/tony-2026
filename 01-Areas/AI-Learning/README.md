# AI Learning

> 一个围绕 AI 公司、人物、模型、系统、论文、主题和前沿动态构建的专题知识库。

## 快速入口

- [[07-Maps/AI Ecosystem Map]]
- [[Learning Progress]]
- [[Resume Note]]
- [[../AI-Foundations/README|AI-Foundations]]
- [[../AI-Engineering/README|AI-Engineering]]
- [[../AI-Applications/README|AI-Applications]]
- [[01-Companies/Companies Index]]
- [[02-People/People Index]]
- [[03-Models/Models Index]]
- [[01-Companies/Mistral AI|Mistral AI]]
- [[01-Companies/Cohere|Cohere]]
- [[01-Companies/NVIDIA|NVIDIA]]
- [[01-Companies/CoreWeave|CoreWeave]]
- [[01-Companies/Groq|Groq]]
- [[01-Companies/Fireworks AI|Fireworks AI]]
- [[09-Systems/Systems Index]]
- [[04-Papers/Papers Index]]
- [[06-Topics/AI Topics Index]]
- [[07-Maps/AI Agent Systems Map]]
- [[07-Maps/AI Agent Capability Map]]
- [[07-Maps/Agent Prompt-Context-Harness Map]]
- [[07-Maps/Agent 平台生态图]]
- [[07-Maps/AI Infra 与推理服务生态图|AI Infra 与推理服务生态图]]
- [[07-Maps/MLOps 与 LLMOps 生态图|MLOps 与 LLMOps 生态图]]
- [[05-News/过去半年全球 AI 前沿动态（2025-09-25 至 2026-03-25）|过去半年全球 AI 前沿动态（2025-09-25 至 2026-03-25）]]
- [[07-Maps/过去半年全球 AI 前沿动态图|过去半年全球 AI 前沿动态图]]
- [[07-Maps/AI 前沿主题演化图|AI 前沿主题演化图]]

## 定位

这里不是泛化的“全部学习内容”，而是整个学习 vault 中的一个专题区，专门用于 AI 学习。

## 建议学习路径

1. 先在 [[../AI-Foundations/README|AI-Foundations]] 建立历史、范式和基础概念
2. 再到 [[06-Topics/AI Topics Index|AI Topics Index]] 理解现代 AI 主线
3. 然后阅读 [[03-Models/Models Index|Models Index]]，把技术概念映射到代表模型
4. 再阅读 [[09-Systems/Systems Index|Systems Index]]，理解产品、平台和 runtime 这一层
5. 如果你要系统理解 Agent，先顺着：[[06-Topics/Agent|Agent]] -> [[06-Topics/提示词工程|提示词工程]] -> [[06-Topics/上下文工程|上下文工程]] -> [[06-Topics/Tool Use|Tool Use]] -> [[06-Topics/MCP（Model Context Protocol）|MCP（Model Context Protocol）]] -> [[06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]] -> [[06-Topics/Agent Memory|Agent Memory]] -> [[06-Topics/Planning and Control|Planning and Control]] -> [[06-Topics/Multi-Agent Systems|Multi-Agent Systems]] -> [[06-Topics/A2A（Agent-to-Agent）与协作协议|A2A（Agent-to-Agent）与协作协议]]
6. 再打开 [[07-Maps/AI Agent Capability Map|AI Agent Capability Map]] 和 [[07-Maps/Agent Prompt-Context-Harness Map|Agent Prompt-Context-Harness Map]] 建立能力图
7. 然后沿着 [[09-Systems/ChatGPT Agent|ChatGPT Agent]]、[[09-Systems/Claude Code|Claude Code]]、[[09-Systems/Codex|Codex]]、[[09-Systems/Cursor|Cursor]]、[[09-Systems/Devin|Devin]]、[[09-Systems/Manus|Manus]]、[[09-Systems/OpenClaw|OpenClaw]] 这条系统线进入
8. 如果你想往 Agent 开发和 Agent 平台继续深入，再读 [[06-Topics/Agent 平台|Agent 平台]]，然后进入 [[09-Systems/Google Agent Development Kit（ADK）|Google Agent Development Kit（ADK）]]、[[09-Systems/LangGraph|LangGraph]]、[[09-Systems/Langfuse|Langfuse]] 和 [[07-Maps/Agent 平台生态图|Agent 平台生态图]]
9. 如果你想跟上 AI infra / GPU cloud / inference serving 这条主线，先读 [[06-Topics/AI 基础设施与 GPU Cloud|AI 基础设施与 GPU Cloud]] -> [[06-Topics/Inference Serving|Inference Serving]] -> [[07-Maps/AI Infra 与推理服务生态图|AI Infra 与推理服务生态图]]，再进入 [[09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]]、[[09-Systems/CoreWeave Cloud|CoreWeave Cloud]]、[[09-Systems/GroqCloud|GroqCloud]]、[[09-Systems/Fireworks Inference Cloud|Fireworks Inference Cloud]]
10. 如果你想系统理解实验、评测、registry、反馈和 agent/LLM observability，顺着 [[06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]] -> [[07-Maps/MLOps 与 LLMOps 生态图|MLOps 与 LLMOps 生态图]] -> [[09-Systems/MLflow|MLflow]] -> [[09-Systems/Weights & Biases Platform|Weights & Biases Platform]] -> [[09-Systems/Langfuse|Langfuse]] -> [[09-Systems/Arize Phoenix|Arize Phoenix]] -> [[09-Systems/Promptfoo|Promptfoo]]
11. 然后进入 [[../AI-Engineering/README|AI-Engineering]]，顺着 [[../AI-Engineering/07-Topics/Experiment Tracking|Experiment Tracking]]、[[../AI-Engineering/07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]、[[../AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]、[[../AI-Engineering/07-Topics/Model Registry and Deployment|Model Registry and Deployment]]、[[../AI-Engineering/07-Topics/Online Evals、Human Feedback 与 Annotation|Online Evals、Human Feedback 与 Annotation]]、[[../AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]] 建立工程主线
12. 如果你想快速跟上最近半年的全球前沿动态，先读 [[05-News/过去半年全球 AI 前沿动态（2025-09-25 至 2026-03-25）|过去半年全球 AI 前沿动态（2025-09-25 至 2026-03-25）]] -> [[05-News/全球 AI 前沿动态时间线（2025-09-25 至 2026-03-25）|全球 AI 前沿动态时间线（2025-09-25 至 2026-03-25）]] -> [[07-Maps/过去半年全球 AI 前沿动态图|过去半年全球 AI 前沿动态图]]
13. 再进入 [[../AI-Applications/README|AI-Applications]] 看真实 workflow 与产品落地

## 目录

```text
AI-Learning/
├── 00-Inbox/
├── 01-Companies/
├── 02-People/
├── 03-Models/
├── 04-Papers/
├── 05-News/
├── 06-Topics/
├── 07-Maps/
├── 08-Templates/
├── 09-Systems/
└── README.md
```

## 核心对象

- 公司 / 组织
- 人物
- 模型
- 系统 / 产品 / 平台
- 论文
- 前沿信息
- 主题

## 图谱导航

- 总图：[[07-Maps/AI Ecosystem Map]]
- 公司与人物：[[07-Maps/AI Company-People Map]]
- 公司与模型：[[07-Maps/AI Company-Models Map]]
- 公司与系统：[[07-Maps/AI Company-Systems Map]]
- 主题与论文：[[07-Maps/AI Topic-Papers Map]]
- Agent 系统：[[07-Maps/AI Agent Systems Map]]
- Agent 能力：[[07-Maps/AI Agent Capability Map]]
- Agent 产品定位：[[07-Maps/AI Agent Product Positioning Map]]
- Coding Agent 定位：[[07-Maps/AI Coding Agent Positioning Map]]
- Prompt/Context/Harness：[[07-Maps/Agent Prompt-Context-Harness Map]]
- Agent 平台生态：[[07-Maps/Agent 平台生态图]]
- AI infra / serving：[[07-Maps/AI Infra 与推理服务生态图|AI Infra 与推理服务生态图]]
- MLOps / LLMOps：[[07-Maps/MLOps 与 LLMOps 生态图|MLOps 与 LLMOps 生态图]]
- 前沿动态：[[07-Maps/过去半年全球 AI 前沿动态图|过去半年全球 AI 前沿动态图]]
- 前沿主题：[[07-Maps/AI 前沿主题演化图|AI 前沿主题演化图]]

## 内容导航

- [[01-Companies/Companies Index]]
- [[02-People/People Index]]
- [[03-Models/Models Index]]
- [[01-Companies/Mistral AI|Mistral AI]]
- [[01-Companies/Cohere|Cohere]]
- [[01-Companies/NVIDIA|NVIDIA]]
- [[01-Companies/CoreWeave|CoreWeave]]
- [[01-Companies/Groq|Groq]]
- [[01-Companies/Fireworks AI|Fireworks AI]]
- [[09-Systems/Systems Index]]
- [[04-Papers/Papers Index]]
- [[05-News/News Index]]
- [[05-News/过去半年全球 AI 前沿动态（2025-09-25 至 2026-03-25）|过去半年全球 AI 前沿动态（2025-09-25 至 2026-03-25）]]
- [[06-Topics/AI Topics Index]]
- [[06-Topics/Knowledge Graph Schema]]
