---
title: AI Company-Models Map
type: topic
status: draft
tags:
  - ai/map
created: 2026-03-01
updated: 2026-03-22
---

# AI Company-Models Map

> 这一张图只看公司与代表模型 / 模型家族的关系。产品、平台和 runtime 请看 `AI Company-Systems Map`。

```mermaid
graph LR
    subgraph companies["公司"]
        openai["[[OpenAI]]"]
        anthropic["[[Anthropic]]"]
        deepseek["[[DeepSeek]]"]
        gdm["[[Google DeepMind]]"]
        meta["[[Meta AI]]"]
        zhipu["[[Zhipu AI]]"]
        alibaba["[[Alibaba Cloud]]"]
        baidu["[[Baidu]]"]
        minimax["[[MiniMax]]"]
        xai["[[xAI]]"]
    end

    subgraph models["模型 / 模型家族"]
        gpt["[[GPT 系列]]"]
        claude["[[Claude 系列]]"]
        r1["[[DeepSeek-R1]]"]
        dsv3["[[DeepSeek-V3]]"]
        gemini["[[Gemini 系列]]"]
        llama["[[Llama 系列]]"]
        glm["[[GLM 系列]]"]
        qwen["[[Qwen 系列]]"]
        ernie["[[ERNIE 系列]]"]
        grok["[[Grok]]"]
        minimaxm["[[MiniMax 系列]]"]
    end

    openai -->|模型家族| gpt

    anthropic -->|模型家族| claude

    deepseek -->|模型| r1
    deepseek -->|模型| dsv3
    gdm -->|模型家族| gemini
    meta -->|模型家族| llama
    zhipu -->|模型家族| glm
    alibaba -->|模型家族| qwen
    baidu -->|模型家族| ernie
    xai -->|代表模型| grok
    minimax -->|模型家族| minimaxm
```

## 怎么看这张图

- 这张图适合用来理解“公司如何把能力落成模型家族与代表模型”
- 同一家公司下可以继续拆模型家族、代表模型、论文依赖
- 产品层、平台层、runtime 层请转到 [[AI Company-Systems Map]]
- 如果以后公司变多，建议按国家或阵营拆分成多张图

## 返回

- [[AI Ecosystem Map]]
- [[AI Company-People Map]]
- [[AI Company-Systems Map]]
- [[AI Topic-Papers Map]]
