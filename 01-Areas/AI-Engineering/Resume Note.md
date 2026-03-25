---
title: Resume Note
type: resume
status: active
domain: AI-Engineering
updated: 2026-03-25
---

# Resume Note

## Last Session

- We opened a new engineering branch around AI infra, GPU cloud, inference serving, and serving data planes, and turned the old seed pages into a coherent first-pass study path.

## What I Actually Understand Now

- AI inference engineering is no longer just a backend runtime problem; it now spans cloud substrate, routing, cache, batching, data planes, and deployment products.
- `Infrastructure (GPU-TPU)` should now be read together with AI-native cloud providers like `CoreWeave`, not only with hardware concepts.
- `Inference Optimization` now clearly centers on prefill/decode, KV cache, batching, and runtime-level efficiency.
- `Serving and Scaling` is evolving into a more explicit product and data-plane problem.
- `Disaggregated Serving` is a strong abstraction because it explains why runtime backends and serving control layers are splitting apart.
- `NVIDIA Dynamo` is important not because it replaces every runtime, but because it makes the data-plane layer legible.

## What Still Feels Fuzzy

- We still need richer benchmark and cost methodology for runtime comparison.
- Real production cases for mixed runtimes and vendor-neutral serving are still thinner than the concept layer.
- GPU cloud operating model and procurement tradeoffs can still be expanded later.
- The inference branch is now structurally strong, but still lighter on failure stories and rollout cases.

## Restart Here

- Read: [[./README|README]], [[07-Topics/Topics Index|Topics Index]], [[07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]], [[07-Topics/Inference Optimization|Inference Optimization]], [[07-Topics/Serving and Scaling|Serving and Scaling]], [[07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]], [[07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]], [[02-Frameworks/vLLM|vLLM]], [[02-Frameworks/SGLang|SGLang]], [[02-Frameworks/TensorRT-LLM|TensorRT-LLM]], [[08-Maps/Inference and Serving Map|Inference and Serving Map]]
- Then continue to: [[../AI-Learning/06-Topics/AI 基础设施与 GPU Cloud|AI 基础设施与 GPU Cloud]], [[../AI-Learning/06-Topics/Inference Serving|Inference Serving]], [[../AI-Learning/09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]], [[../AI-Learning/09-Systems/CoreWeave Cloud|CoreWeave Cloud]], [[../AI-Learning/09-Systems/GroqCloud|GroqCloud]], [[../AI-Learning/09-Systems/Fireworks Inference Cloud|Fireworks Inference Cloud]], [[../AI-Learning/07-Maps/AI Infra 与推理服务生态图|AI Infra 与推理服务生态图]]
