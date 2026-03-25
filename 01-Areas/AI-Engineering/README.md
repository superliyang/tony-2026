# AI-Engineering

> AI 工程体系：训练、框架、工具链、推理、部署与 agent 平台

## 快速入口

- [[Learning Progress]]
- [[Resume Note]]
- [[07-Topics/Topics Index|Topics Index]]
- [[08-Maps/Maps Index|Maps Index]]
- [[07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]]
- [[07-Topics/Inference Optimization|Inference Optimization]]
- [[07-Topics/Serving and Scaling|Serving and Scaling]]
- [[07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]]
- [[07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]
- [[02-Frameworks/vLLM|vLLM]]
- [[02-Frameworks/SGLang|SGLang]]
- [[02-Frameworks/TensorRT-LLM|TensorRT-LLM]]
- [[08-Maps/Inference and Serving Map|Inference and Serving Map]]
- [[07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]
- [[07-Topics/App Server 与 Rich Agent Protocols|App Server 与 Rich Agent Protocols]]
- [[07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]]
- [[07-Topics/Harness Engineering|Harness Engineering]]
- [[07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]
- [[07-Topics/长期运行 Agent 的记忆系统|长期运行 Agent 的记忆系统]]
- [[07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]
- [[07-Topics/A2A 与 Multi-Agent Coordination|A2A 与 Multi-Agent Coordination]]
- [[08-Maps/Agent Runtime Engineering Map|Agent Runtime Engineering Map]]
- [[08-Maps/Agent Context and Integration Engineering Map|Agent Context and Integration Engineering Map]]
- [[08-Maps/Agent Action Surfaces and Protocols Map|Agent Action Surfaces and Protocols Map]]
- [[08-Maps/Harness Feedback Loop Map|Harness Feedback Loop Map]]
- [[08-Maps/Agent 协作、记忆与信任边界图|Agent 协作、记忆与信任边界图]]
- [[08-Maps/Agent Evaluation and Governance Map|Agent Evaluation and Governance Map]]
- [[07-Topics/Agent SDK 设计|Agent SDK 设计]]
- [[07-Topics/Tool Gateway、MCP Servers 与 SDK Tools|Tool Gateway、MCP Servers 与 SDK Tools]]
- [[07-Topics/飞书与 Lark 作为 Agent Channel Adapter|飞书与 Lark 作为 Agent Channel Adapter]]
- [[07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]
- [[08-Maps/Agent 平台技术栈图|Agent 平台技术栈图]]
- [[06-Projects/项目索引|项目索引]]

## 定位

这里关注的不是“哪个公司发布了什么模型”，而是：

- 一个 AI 系统如何被训练出来
- 它如何被评测、优化、上线和运维
- 开源框架、基础设施和工具链各自扮演什么角色
- inference stack 如何从 backend runtime 演进到 serving data plane 和云平台
- 当系统进入 agent 时代后，runtime、memory、security、approval、eval 和 coordination 如何真正组合成一个可治理系统
- 当团队要从“会跑 agent”走向“能搭 agent platform”时，SDK、tool gateway、channel adapter 和 observability platform 如何组合

## 当前重点模块

- 工程栈：[[01-Stacks/Stacks Index|Stacks Index]]
- 项目文档：[[06-Projects/项目索引|项目索引]]
- 框架：[[02-Frameworks/Frameworks Index|Frameworks Index]]
- 训练：[[03-Training/Training Index|Training Index]]
- 推理系统：[[07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]]、[[07-Topics/Inference Optimization|Inference Optimization]]、[[07-Topics/Serving and Scaling|Serving and Scaling]]、[[07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]]、[[07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]、[[02-Frameworks/vLLM|vLLM]]、[[02-Frameworks/SGLang|SGLang]]、[[02-Frameworks/TensorRT-LLM|TensorRT-LLM]]、[[08-Maps/Inference and Serving Map|Inference and Serving Map]]
- Agent 系统：[[07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]、[[07-Topics/Tool Calling and Action Execution|Tool Calling and Action Execution]]、[[07-Topics/Session and Memory Design|Session and Memory Design]]、[[07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]、[[07-Topics/App Server 与 Rich Agent Protocols|App Server 与 Rich Agent Protocols]]、[[07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]]、[[07-Topics/Harness Engineering|Harness Engineering]]、[[07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]、[[07-Topics/长期运行 Agent 的记忆系统|长期运行 Agent 的记忆系统]]、[[07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]、[[07-Topics/A2A 与 Multi-Agent Coordination|A2A 与 Multi-Agent Coordination]]、[[07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]、[[07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]、[[07-Topics/Task Success and Failure Recovery|Task Success and Failure Recovery]]、[[07-Topics/Cost, Latency, and Safety Tradeoffs|Cost, Latency, and Safety Tradeoffs]]、[[07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]、[[07-Topics/Agent SDK 设计|Agent SDK 设计]]、[[07-Topics/Tool Gateway、MCP Servers 与 SDK Tools|Tool Gateway、MCP Servers 与 SDK Tools]]、[[07-Topics/飞书与 Lark 作为 Agent Channel Adapter|飞书与 Lark 作为 Agent Channel Adapter]]、[[07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]

## 使用建议

- 先从 Topics Index 建立主线问题
- 如果你在看 AI infra / inference serving，顺着这条线读：
  - `Infrastructure`
  - `Inference Optimization`
  - `Serving and Scaling`
  - `KV Cache / Prefill-Decode / Continuous Batching`
  - `Disaggregated Serving`
  - `vLLM / SGLang / TensorRT-LLM`
- 如果你是从 `AI-Learning` 的 Agent 分支过来的，就顺着这条线读：
  - `Prompt / Context`
  - `Tool Use / MCP / Browser / App Server`
  - `Harness / Eval Harness`
  - `Long-Term Memory / Security / A2A`
  - `Human Approval / Reliability / Long-Running Ops`
  - `Agent SDK / Tool Gateway / Channel Adapter / Platform Architecture`
