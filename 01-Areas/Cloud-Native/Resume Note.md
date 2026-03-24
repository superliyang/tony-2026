---
title: Resume Note
type: resume
status: active
domain: Cloud-Native
updated: 2026-03-24
---

# Resume Note

## Last Session

- 我们把 `Cloud-Native` 从第一版骨架推进到了第二阶段主线：service mesh、平台工程、policy-as-code 和软件供应链安全。

## What I Actually Understand Now

- 云原生的第二阶段重点不是更多 Kubernetes 资源对象，而是平台与治理能力
- `Istio` 代表服务连接、流量治理与平台化 networking
- `Kyverno` 代表 policy-as-code 与 cluster-level governance
- `Sigstore` 代表 artifact trust 和 software supply chain security
- `Backstage` 代表平台工程的产品入口层
- 这些方向并不是孤立的，而是共同决定平台成熟度

## What Still Feels Fuzzy

- service mesh 的 sidecar / ambient 取舍还没展开
- runtime security、supply chain policy 与 cluster policy 的结合还没展开到 workflow 层
- 还没有进入真实平台团队案例、golden path 和 IDP operating model

## Restart Here

- Read: [[README]]
- Then: [[03-Topics/服务发现与流量治理|服务发现与流量治理]] -> [[02-Projects/Istio|Istio]] -> [[03-Topics/云原生安全|云原生安全]] -> [[03-Topics/软件供应链安全|软件供应链安全]] -> [[02-Projects/Kyverno|Kyverno]] -> [[02-Projects/Sigstore|Sigstore]] -> [[03-Topics/平台工程|平台工程]] -> [[02-Projects/Backstage|Backstage]]
