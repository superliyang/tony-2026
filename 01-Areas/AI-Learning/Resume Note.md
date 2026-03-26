---
title: Resume Note
type: resume
status: active
domain: AI
updated: 2026-03-26
---

# Resume Note

## Last Session

- We turned the AI graph from infra-first expansion into a reusable MLOps / LLMOps slice, so the vault now explains not only how models and agents run, but how they are tracked, evaluated, released, and improved over time.

## What I Actually Understand Now

- `MLOps` is not just experiment logging; it is a lifecycle from tracking to registry to release discipline.
- `LLMOps` adds prompt, dataset, trace, score, and human feedback as governed assets.
- `AgentOps` is best understood as `LLMOps` extended with tool calls, memory, approvals, and long-running workflows.
- `MLflow`, `Weights & Biases Platform`, `Langfuse`, `Arize Phoenix`, and `Promptfoo` sit on different parts of the lifecycle rather than solving the exact same problem.
- The most important distinction is no longer “which tool is best”, but “which lifecycle layer a team is currently missing”.

## What Still Feels Fuzzy

- We still need more concrete enterprise case studies for MLOps / LLMOps adoption.
- Open-source vs managed tradeoffs across these platforms can still be made more explicit.
- Production feedback loops, annotation operations, and release-gate rituals still deserve richer templates.
- The boundary between LLMOps and AgentOps is clearer conceptually than it is operationally.

## Restart Here

- Read: [[./README|README]], [[06-Topics/AI Topics Index|AI Topics Index]], [[06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]], [[07-Maps/MLOps 与 LLMOps 生态图|MLOps 与 LLMOps 生态图]], [[09-Systems/MLflow|MLflow]], [[09-Systems/Weights & Biases Platform|Weights & Biases Platform]], [[09-Systems/Langfuse|Langfuse]], [[09-Systems/Arize Phoenix|Arize Phoenix]], [[09-Systems/Promptfoo|Promptfoo]]
- Then continue to: [[../AI-Engineering/07-Topics/Experiment Tracking|Experiment Tracking]], [[../AI-Engineering/07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]], [[../AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]], [[../AI-Engineering/07-Topics/Model Registry and Deployment|Model Registry and Deployment]], [[../AI-Engineering/07-Topics/Online Evals、Human Feedback 与 Annotation|Online Evals、Human Feedback 与 Annotation]], [[../AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]], [[../AI-Engineering/08-Maps/MLOps 与 LLMOps 工程图|MLOps 与 LLMOps 工程图]]
