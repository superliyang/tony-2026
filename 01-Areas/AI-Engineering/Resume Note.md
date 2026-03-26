---
title: Resume Note
type: resume
status: active
domain: AI-Engineering
updated: 2026-03-26
---

# Resume Note

## Last Session

- We opened a new engineering branch around MLOps, LLMOps, and feedback-driven release engineering, and turned the old seed pages for tracking, evaluation, and registry into a coherent first-pass study path.

## What I Actually Understand Now

- `MLOps` is not just experiment logging; it is lifecycle governance from run tracking to release discipline.
- `LLMOps` adds prompt, dataset, score, trace, and human feedback as first-class assets.
- `AgentOps` is best understood as `LLMOps` extended into action systems with approvals, memory, and long-running state.
- `MLflow`, `Weights & Biases Platform`, `Langfuse`, `Arize Phoenix`, and `Promptfoo` do not sit on the same layer; they occupy different control points in the lifecycle.
- Production AI quality becomes legible only when experiment evidence, eval evidence, and online feedback are linked together.

## What Still Feels Fuzzy

- We still need richer case studies for enterprise MLOps rollout and self-hosted stack choices.
- Annotation operating models and release-gate rituals deserve stronger templates.
- OpenTelemetry-native observability versus platform-specific tracing still needs more comparative treatment.
- The lifecycle is now structurally clear, but still lighter on real failure stories than on engineering abstractions.

## Restart Here

- Read: [[./README|README]], [[07-Topics/Topics Index|Topics Index]], [[07-Topics/Experiment Tracking|Experiment Tracking]], [[07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]], [[07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]], [[07-Topics/Model Registry and Deployment|Model Registry and Deployment]], [[07-Topics/Online Evals、Human Feedback 与 Annotation|Online Evals、Human Feedback 与 Annotation]], [[07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]], [[08-Maps/MLOps 与 LLMOps 工程图|MLOps 与 LLMOps 工程图]]
- Then continue to: [[04-Evaluation/Evaluation Index|Evaluation Index]], [[05-Deployment/Deployment Index|Deployment Index]], [[08-Maps/AI Engineering Stack Map|AI Engineering Stack Map]], [[08-Maps/Inference and Serving Map|Inference and Serving Map]], [[../AI-Learning/06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]], [[../AI-Learning/09-Systems/MLflow|MLflow]], [[../AI-Learning/09-Systems/Weights & Biases Platform|Weights & Biases Platform]], [[../AI-Learning/09-Systems/Langfuse|Langfuse]], [[../AI-Learning/09-Systems/Arize Phoenix|Arize Phoenix]], [[../AI-Learning/09-Systems/Promptfoo|Promptfoo]]
