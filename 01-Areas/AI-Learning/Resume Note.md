---
title: Resume Note
type: resume
status: active
domain: AI
updated: 2026-03-25
---

# Resume Note

## Last Session

- We extended the AI frontier branch into a reusable AI infra / GPU cloud / inference serving slice, so the vault now explains not only who released models, but who supplies the platform layers those models actually run on.

## What I Actually Understand Now

- AI competition is no longer just model capability competition; cloud substrate, inference economics, and serving data planes now matter just as much.
- `AI 基础设施与 GPU Cloud` and `Inference Serving` are related but distinct: one is about supply, clusters, and platform substrate; the other is about runtime, routing, cache, and API delivery.
- `NVIDIA` is no longer just “the GPU company”; it now also matters as a serving-stack and data-plane setter through `TensorRT-LLM` and `NVIDIA Dynamo`.
- `CoreWeave` represents the AI-native cloud path, `Groq` represents the low-latency specialized inference path, and `Fireworks AI` represents the inference-platform abstraction path.
- The serving layer now clearly separates runtime backends from the data plane and routing layer.

## What Still Feels Fuzzy

- We still need richer benchmark and cost-methodology notes for inference systems.
- Company histories and people layers remain thinner than systems and topics.
- The application-side consequences of inference economics can still be expanded later.
- We have a strong first-pass infra graph, but runtime comparison cases are still thinner than the concept layer.

## Restart Here

- Read: [[./README|README]], [[06-Topics/AI Topics Index|AI Topics Index]], [[06-Topics/AI 基础设施与 GPU Cloud|AI 基础设施与 GPU Cloud]], [[06-Topics/Inference Serving|Inference Serving]], [[07-Maps/AI Infra 与推理服务生态图|AI Infra 与推理服务生态图]], [[01-Companies/NVIDIA|NVIDIA]], [[01-Companies/CoreWeave|CoreWeave]], [[01-Companies/Groq|Groq]], [[01-Companies/Fireworks AI|Fireworks AI]], [[09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]], [[09-Systems/CoreWeave Cloud|CoreWeave Cloud]], [[09-Systems/GroqCloud|GroqCloud]], [[09-Systems/Fireworks Inference Cloud|Fireworks Inference Cloud]]
- Then continue to: [[../AI-Engineering/07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]], [[../AI-Engineering/07-Topics/Inference Optimization|Inference Optimization]], [[../AI-Engineering/07-Topics/Serving and Scaling|Serving and Scaling]], [[../AI-Engineering/07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]], [[../AI-Engineering/07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]], [[../AI-Engineering/02-Frameworks/vLLM|vLLM]], [[../AI-Engineering/02-Frameworks/SGLang|SGLang]], [[../AI-Engineering/02-Frameworks/TensorRT-LLM|TensorRT-LLM]], [[../AI-Engineering/08-Maps/Inference and Serving Map|Inference and Serving Map]]
