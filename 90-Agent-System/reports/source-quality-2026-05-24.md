---
title: Source Quality Report - 2026-05-24
type: source-quality-report
status: generated
key: 2026-05-24
---

# Source Quality Report - 2026-05-24

## 来源质量排名

| source | items | high_value | avg_importance | warnings | top_topic |
| --- | ---: | ---: | ---: | ---: | --- |
| GitHub Trending AI | 10 | 2 | 2.00 | 0 | Others |
| Anthropic News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| DeepSeek News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| Apache Flink Blog | 1 | 1 | 5.00 | 0 | Big-Data |
| LiteLLM Releases | 1 | 0 | 3.00 | 0 | AI-Open-Source |

## 建议

- 优先保留和调优 `GitHub Trending AI`：本轮 high_value=2，avg=2.00。
- 观察 `LiteLLM Releases`：warnings=0，high_value=0。

## Warnings

- arxiv-ai-agents: RSS fetch failed: 429 Client Error: Unknown Error for url: https://export.arxiv.org/api/query?search_query=all:%22LLM%20agent%22%20OR%20all:%22AI%20agent%22&start=0&max_results=10&sortBy=submittedDate&sortOrder=descending

## 输入

- classified_items: 90-Agent-System/logs/semantic-analysis-2026-05-24.json
