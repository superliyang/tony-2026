---
title: Automation Doctor - 2026-05-23
type: automation-doctor-report
status: passed
network_checks: false
generated_at: 2026-05-23T23:20:28+00:00
---

# Automation Doctor - 2026-05-23

## 总览

- failed: 0
- warnings: 1
- checks: 33

## 检查项

| status | check | detail |
| --- | --- | --- |
| ok | python package: yaml | installed |
| ok | python package: feedparser | installed |
| ok | python package: requests | installed |
| ok | python package: lark_oapi | installed |
| ok | env: FEISHU_WEBHOOK_URL | configured for Feishu active push |
| ok | env: FEISHU_APP_ID | configured for Feishu WebSocket bot |
| ok | env: FEISHU_APP_SECRET | configured for Feishu WebSocket bot |
| ok | env: DEEPSEEK_API_KEY | configured for DeepSeek semantic analysis |
| warning | env: GITHUB_TOKEN | missing; GitHub release sources may hit anonymous API rate limits |
| ok | directory: 00-Agent-Inbox/Daily-Digests | exists |
| ok | directory: 00-Agent-Inbox/Weekly-Digests | exists |
| ok | directory: 00-Agent-Inbox/Candidates | exists |
| ok | directory: 00-Agent-Inbox/Review-Queue | exists |
| ok | directory: 00-Agent-Inbox/Study-Queue | exists |
| ok | directory: 90-Agent-System/logs | exists |
| ok | directory: 90-Agent-System/reports | exists |
| ok | source: openai-blog | type=rss enabled=True |
| ok | source: anthropic-news | type=url enabled=True |
| ok | source: deepseek-news | type=url enabled=True |
| ok | source: github-trending-ai | type=github_trending enabled=True |
| ok | source: manual-url-inbox | type=manual_urls enabled=True |
| ok | source: aws-security-blog | type=rss enabled=True |
| ok | source: cloudflare-blog | type=rss enabled=True |
| ok | source: apache-flink | type=url enabled=True |
| ok | source: arxiv-ai-agents | type=rss enabled=True |
| ok | source: github-langgraph-releases | type=github_releases enabled=True |
| ok | source: github-litellm-releases | type=github_releases enabled=True |
| ok | source: github-opencode-releases | type=github_releases enabled=True |
| ok | source: cisa-alerts | type=rss enabled=True |
| ok | source: cisa-kev | type=cisa_kev enabled=True |
| ok | launchd: com.tony2026.knowledge-feishu-bot | 3776	-15	com.tony2026.knowledge-feishu-bot |
| ok | launchd: com.tony2026.knowledge-daily | -	0	com.tony2026.knowledge-daily |
| ok | launchd: com.tony2026.knowledge-weekly | -	0	com.tony2026.knowledge-weekly |

## 建议

- `failed=0` 才适合认为自动化环境可稳定运行。
- warning 不一定阻塞运行，但应该进入后续优化清单。
- 如果 source network 失败，优先判断是信息源失效、网络抖动，还是本地 TLS / DNS 问题。
