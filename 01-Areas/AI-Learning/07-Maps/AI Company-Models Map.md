---
title: AI Company-Models Map
type: topic
status: draft
tags:
  - ai/map
created: 2026-03-01
updated: 2026-03-01
---

# AI Company-Models Map

> 这一张图只看公司与代表模型 / 产品的关系。

```mermaid
graph LR
    subgraph companies["公司"]
        openai["[[OpenAI]]"]
        anthropic["[[Anthropic]]"]
        deepseek["[[DeepSeek]]"]
        gdm["[[Google DeepMind]]"]
        meta["[[Meta AI]]"]
        moonshot["[[Moonshot AI]]"]
        zhipu["[[Zhipu AI]]"]
        alibaba["[[Alibaba Cloud]]"]
        baidu["[[Baidu]]"]
        minimax["[[MiniMax]]"]
        xai["[[xAI]]"]
    end

    subgraph models["模型 / 产品"]
        gpt["[[GPT 系列]]"]
        chatgpt["[[ChatGPT]]"]
        openaiapi["[[OpenAI API]]"]
        claude["[[Claude 系列]]"]
        claudecode["[[Claude Code]]"]
        r1["[[DeepSeek-R1]]"]
        dsv3["[[DeepSeek-V3]]"]
        dsapi["[[DeepSeek API]]"]
        gemini["[[Gemini 系列]]"]
        llama["[[Llama 系列]]"]
        kimi["[[Kimi]]"]
        glm["[[GLM 系列]]"]
        qwen["[[Qwen 系列]]"]
        ernie["[[ERNIE 系列]]"]
        grok["[[Grok]]"]
        minimaxm["[[MiniMax 系列]]"]
    end

    openai -->|模型家族| gpt
    openai -->|产品| chatgpt
    openai -->|平台| openaiapi

    anthropic -->|模型家族| claude
    anthropic -->|产品| claudecode

    deepseek -->|模型| r1
    deepseek -->|模型| dsv3
    deepseek -->|平台| dsapi
    gdm -->|模型家族| gemini
    meta -->|模型家族| llama
    moonshot -->|产品| kimi
    zhipu -->|模型家族| glm
    alibaba -->|模型家族| qwen
    baidu -->|模型家族| ernie
    xai -->|代表产品| grok
    minimax -->|模型家族| minimaxm
```

## 怎么看这张图

- 这张图适合用来理解“公司如何把能力落成模型和产品”
- 同一家公司下可以继续补产品层、API 层、模型家族层
- 如果以后公司变多，建议按国家或阵营拆分成多张图

## 返回

- [[AI Ecosystem Map]]
- [[AI Company-People Map]]
- [[AI Topic-Papers Map]]
