---
title: Resume Note
type: resume
status: active
domain: AI
updated: 2026-03-26
---

# Resume Note

## Last Session

- We took the first-pass MLOps / LLMOps slice and pushed it to enterprise tradeoffs, then opened a new first-pass AI security branch around prompt injection, guardrails, model supply chain security, and security evaluation.

## What I Actually Understand Now

- `LLMOps` platform choice is really about choosing a control point: lifecycle governance, production observability, pre-release eval, or app workbench.
- `AI Security` is not the same as `AI Safety`; it is more about attack surfaces, trust boundaries, artifact integrity, and runtime controls.
- `NVIDIA NeMo Guardrails` represents the guardrails / policy layer, while `Protect AI ModelScan` represents the model supply-chain layer.
- Prompt injection is dangerous not because it changes text, but because it can change actions, data access, and long-running state.

## What Still Feels Fuzzy

- We still need richer AI security case studies and concrete failure patterns.
- Enterprise rollout patterns for self-hosted vs managed LLMOps need more concrete org examples.
- Security evaluation and red teaming still deserve stronger reusable templates later.

## Restart Here

- Read: [[./README|README]], [[06-Topics/AI Topics Index|AI Topics Index]], [[06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]], [[07-Maps/MLOps 与 LLMOps 生态图|MLOps 与 LLMOps 生态图]], [[06-Topics/AI Security|AI Security]], [[06-Topics/AI Safety 与 AI Security|AI Safety 与 AI Security]], [[06-Topics/Prompt Injection 与 Jailbreaks|Prompt Injection 与 Jailbreaks]], [[07-Maps/AI Security Threat Map|AI Security Threat Map]]
- Then continue to: [[../AI-Engineering/07-Topics/Enterprise MLOps 与 LLMOps Vendor Tradeoffs|Enterprise MLOps 与 LLMOps Vendor Tradeoffs]], [[../AI-Engineering/07-Topics/Open-Source、Self-Hosting 与 Managed LLMOps|Open-Source、Self-Hosting 与 Managed LLMOps]], [[../AI-Engineering/07-Topics/Security and Privacy|Security and Privacy]], [[../AI-Engineering/07-Topics/AI Security Threat Modeling|AI Security Threat Modeling]], [[../AI-Engineering/07-Topics/Prompt Injection Defense 与 Tool Safety|Prompt Injection Defense 与 Tool Safety]], [[../AI-Engineering/07-Topics/Guardrails、Policy Enforcement 与 Security Gateways|Guardrails、Policy Enforcement 与 Security Gateways]], [[../AI-Engineering/07-Topics/Model Supply Chain Security|Model Supply Chain Security]], [[../AI-Engineering/07-Topics/AI Security Evaluation 与 Red Teaming|AI Security Evaluation 与 Red Teaming]], [[../AI-Engineering/08-Maps/AI Security Engineering Map|AI Security Engineering Map]]
