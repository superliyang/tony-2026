# 学习知识库

> 一个按学习领域组织的 Obsidian vault。AI 学习只是其中一个专题区，而不是整个 vault 的唯一结构。

## 设计原则

顶层先按“大类”划分，避免所有内容直接平铺在根目录。这样以后新增别的学习方向时，不需要推倒重来。

当前建议的层级是：

```text
.
├── README.md
├── 01-Areas/
│   └── AI-Learning/
├── 08-Shared-Templates/
└── 99-Archive/
```

其中：

- `01-Areas/` 放具体学习领域
- `AI-Learning/` 是当前第一个重点专题
- `08-Shared-Templates/` 以后可放跨领域通用模板
- `99-Archive/` 放长期归档内容

## 当前专题

当前已经建立的专题是：

- [[01-Areas/Cloud-Native/专题总览|Cloud-Native]]
- [[01-Areas/AI-Foundations/专题总览|AI-Foundations]]
- [[01-Areas/AI-Learning/专题总览|AI-Learning]]
- [[01-Areas/AI-Engineering/专题总览|AI-Engineering]]
- [[01-Areas/AI-Applications/专题总览|AI-Applications]]
- [[01-Areas/Skills-Gaming/专题总览|Skills-Gaming]]

后续你可以继续新增：

- `Product-Learning`
- `Management-Learning`
- `Finance-Learning`
- `Language-Learning`

每个专题内部再决定自己的实体、目录和模板。

## 为什么这样更稳

- AI 知识库只是一个专题，不会绑死整个 vault
- 以后新增其他学习方向时，结构仍然一致
- 每个专题都可以有自己的对象模型，不互相污染
- 顶层更干净，首页只负责导航，不负责承载全部知识细节

## 下一步

当前这个 vault 已经不只是一套 AI 学习库，也开始包含新的技术专题，比如 `Cloud-Native`。

现在最成熟的是 AI 这一组 4 个互相关联的专题：

1. `AI-Foundations`：历史、范式、基础概念
2. `AI-Learning`：公司、人物、模型、论文、主题、新闻
3. `AI-Engineering`：训练、框架、工具链、部署
4. `AI-Applications`：产品、工作流、行业落地

建议的学习顺序是：

1. 先看 `AI-Foundations`
2. 再进入 `AI-Learning`
3. 然后过渡到 `AI-Engineering`
4. 最后看 `AI-Applications`

如果你想切到新的技术专题，现在也可以从：

1. `Cloud-Native`
2. `Skills-Gaming`
3. 然后顺着各自的 `README -> 索引 -> 地图 -> 进度/恢复页`
