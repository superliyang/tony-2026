---
title: Resume Note
type: resume
status: active
domain: AI-Engineering
updated: 2026-03-26
---

# Resume Note

## Last Session

- We pushed the MLOps / LLMOps branch from lifecycle basics into enterprise platform tradeoffs, and then opened a first-pass AI security engineering branch.

## What I Actually Understand Now

- Enterprise `LLMOps` choice is really about choosing a control point and a deployment model, not about chasing a single all-in-one product.
- `MLflow`, `W&B`, `Langfuse`, `Phoenix`, and `Promptfoo` sit on different layers of the lifecycle.
- AI security must cover input, context, tools, state, and artifacts, not just model outputs.
- Prompt injection defense is inseparable from tool safety and approval design.
- Model supply-chain security is now a real engineering concern, not an edge case.

## What Still Feels Fuzzy

- We still need richer enterprise case studies and failure stories for AI security.
- Red-team packs and repeatable security review templates are still missing.
- Organizational ownership for LLMOps and AI security could be expanded later.

## Restart Here

- Read: [[./README|README]], [[07-Topics/Enterprise MLOps 与 LLMOps Vendor Tradeoffs|Enterprise MLOps 与 LLMOps Vendor Tradeoffs]], [[07-Topics/Open-Source、Self-Hosting 与 Managed LLMOps|Open-Source、Self-Hosting 与 Managed LLMOps]], [[08-Maps/Enterprise LLMOps Vendor Choice Map|Enterprise LLMOps Vendor Choice Map]], [[07-Topics/Security and Privacy|Security and Privacy]], [[07-Topics/AI Security Threat Modeling|AI Security Threat Modeling]], [[07-Topics/Prompt Injection Defense 与 Tool Safety|Prompt Injection Defense 与 Tool Safety]], [[07-Topics/Guardrails、Policy Enforcement 与 Security Gateways|Guardrails、Policy Enforcement 与 Security Gateways]], [[07-Topics/Model Supply Chain Security|Model Supply Chain Security]], [[07-Topics/AI Security Evaluation 与 Red Teaming|AI Security Evaluation 与 Red Teaming]], [[08-Maps/AI Security Engineering Map|AI Security Engineering Map]]
- Then continue to: [[06-Projects/Enterprise LLMOps/README|Enterprise LLMOps]], [[04-Evaluation/Evaluation Index|Evaluation Index]], [[05-Deployment/Deployment Index|Deployment Index]], [[08-Maps/MLOps 与 LLMOps 工程图|MLOps 与 LLMOps 工程图]], [[08-Maps/AI Engineering Stack Map|AI Engineering Stack Map]], [[08-Maps/Inference and Serving Map|Inference and Serving Map]], [[../AI-Learning/06-Topics/AI Security|AI Security]], [[../AI-Learning/09-Systems/NVIDIA NeMo Guardrails|NVIDIA NeMo Guardrails]], [[../AI-Learning/09-Systems/Protect AI ModelScan|Protect AI ModelScan]]
