---
title: AI Company-Systems Map
type: topic
status: draft
tags:
  - ai/map
created: 2026-03-22
updated: 2026-03-22
---

# AI Company-Systems Map

> 这一张图只看公司与具体系统 / 产品 / 平台的关系。

```mermaid
graph LR
    subgraph companies["公司"]
        openai["[[OpenAI]]"]
        anthropic["[[Anthropic]]"]
        deepseek["[[DeepSeek]]"]
        moonshot["[[Moonshot AI]]"]
        anysphere["[[Anysphere]]"]
        cognition["[[Cognition]]"]
    end

    subgraph systems["系统 / 产品 / 平台"]
        chatgpt["[[../09-Systems/ChatGPT|ChatGPT]]"]
        openaiapi["[[../09-Systems/OpenAI API|OpenAI API]]"]
        codex["[[../09-Systems/Codex|Codex]]"]
        claudecode["[[../09-Systems/Claude Code|Claude Code]]"]
        dsapi["[[../09-Systems/DeepSeek API|DeepSeek API]]"]
        kimi["[[../09-Systems/Kimi|Kimi]]"]
        cursor["[[../09-Systems/Cursor|Cursor]]"]
        devin["[[../09-Systems/Devin|Devin]]"]
    end

    openai -->|产品| chatgpt
    openai -->|平台| openaiapi
    openai -->|agent| codex
    anthropic -->|产品| claudecode
    deepseek -->|平台| dsapi
    moonshot -->|产品| kimi
    anysphere -->|产品| cursor
    cognition -->|产品| devin
```

## 怎么看这张图

- 这张图适合回答“公司把能力落成了什么系统入口”
- `Model` 和 `System` 是两层：一个更偏能力，一个更偏产品/平台/工作入口
- `OpenClaw` 更像跨公司生态里的 runtime 案例，所以放在 `AI Agent Systems Map` 里更合适
- `Anysphere` 和 `Cognition` 的加入，代表公司层已经开始覆盖 agent-native developer tool 公司

## 返回

- [[AI Ecosystem Map]]
- [[AI Company-People Map]]
- [[AI Company-Models Map]]
- [[AI Agent Systems Map]]
