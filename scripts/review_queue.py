from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from utils import extract_frontmatter, now_iso, repo_root, safe_print, today_str, write_text


STATUS_BY_ACTION = {
    "ignore": "discarded",
    "discard": "discarded",
    "drop": "discarded",
    "忽略": "discarded",
    "丢弃": "discarded",
    "放弃": "discarded",
    "study": "queued-for-study",
    "queue": "queued-for-study",
    "learn": "queued-for-study",
    "学习": "queued-for-study",
    "加入学习": "queued-for-study",
    "加入学习队列": "queued-for-study",
    "keep": "pending-review",
    "保留": "pending-review",
    "暂存": "pending-review",
    "merge": "ready-to-merge",
    "curate": "ready-to-merge",
    "合入": "ready-to-merge",
    "准备合入": "ready-to-merge",
}


@dataclass
class ReviewItem:
    index: int
    path: Path
    title: str
    topic: str
    status: str
    importance_score: str
    source_url: str


def candidate_files() -> list[Path]:
    root = repo_root()
    return sorted((root / "00-Agent-Inbox/Candidates").glob("*/*.md"), key=lambda path: path.stat().st_mtime, reverse=True)


def parse_candidate(path: Path, index: int) -> ReviewItem:
    text = path.read_text(encoding="utf-8")
    meta, _ = extract_frontmatter(text)
    return ReviewItem(
        index=index,
        path=path,
        title=meta.get("title", path.stem),
        topic=meta.get("topic", "Others"),
        status=meta.get("status", "pending-review"),
        importance_score=meta.get("importance_score", "1"),
        source_url=meta.get("source_url", ""),
    )


def review_items(status: str = "pending-review", limit: int = 10) -> list[ReviewItem]:
    items: list[ReviewItem] = []
    for path in candidate_files():
        item = parse_candidate(path, len(items) + 1)
        if status == "all" or item.status == status:
            items.append(item)
        if len(items) >= limit:
            break
    return items


def format_review(items: list[ReviewItem], title: str = "Review Queue") -> str:
    if not items:
        return f"{title}\n\n暂无待 review 候选。"
    lines = [title, ""]
    for item in items:
        lines.append(f"{item.index}. [{item.topic}] {item.title}")
        lines.append(f"   status={item.status} importance={item.importance_score}")
        lines.append(f"   path={item.path.relative_to(repo_root())}")
    lines.extend(["", "快捷决策：`1 学习`、`2 忽略`、`3 保留`、`4 合入`"])
    return "\n".join(lines)


def set_frontmatter_value(text: str, key: str, value: str) -> str:
    if not text.startswith("---\n"):
        return f"---\n{key}: {value}\n---\n\n{text}"
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    head = text[:end]
    body = text[end:]
    pattern = re.compile(rf"^{re.escape(key)}:\s*.*$", re.MULTILINE)
    if pattern.search(head):
        head = pattern.sub(f"{key}: {value}", head)
    else:
        head = f"{head}\n{key}: {value}"
    return head + body


def append_decision(path: Path, action: str, status: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = set_frontmatter_value(text, "status", status)
    decision = (
        "\n\n# Review Decision\n\n"
        f"- decided_at: {now_iso()}\n"
        f"- action: {action}\n"
        f"- status: {status}\n"
    )
    path.write_text(text.rstrip() + decision + "\n", encoding="utf-8")


def write_review_queue(items: list[ReviewItem], date_str: str | None = None, dry_run: bool = False) -> Path:
    root = repo_root()
    target_date = date_str or today_str()
    output = root / f"00-Agent-Inbox/Review-Queue/{target_date}.md"
    lines = [
        "---",
        f"title: Review Queue - {target_date}",
        "type: review-queue",
        "status: generated",
        f"date: {target_date}",
        "---",
        "",
        f"# Review Queue - {target_date}",
        "",
        "## 待人工决策候选",
        "",
    ]
    if items:
        for item in items:
            lines.extend(
                [
                    f"### {item.index}. {item.title}",
                    "",
                    f"- topic: {item.topic}",
                    f"- status: {item.status}",
                    f"- importance_score: {item.importance_score}",
                    f"- file: [[{item.path.relative_to(root).with_suffix('')}]]",
                    f"- source_url: {item.source_url}",
                    "",
                ]
            )
    else:
        lines.append("- 暂无待 review 候选。")
    lines.extend(["## 飞书决策命令", "", "- `/review`", "- `/decide <编号> study|ignore|keep|merge`"])
    write_text(output, "\n".join(lines), dry_run=dry_run)
    return output


def decide(index: int, action: str) -> ReviewItem:
    status = STATUS_BY_ACTION.get(action.strip().lower())
    if not status:
        raise ValueError(f"Unsupported action: {action}. Use study|ignore|keep|merge.")
    items = review_items(status="pending-review", limit=50)
    if index < 1 or index > len(items):
        raise IndexError(f"Review item index out of range: {index}")
    item = items[index - 1]
    append_decision(item.path, action, status)
    return parse_candidate(item.path, index)


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    list_parser = sub.add_parser("list")
    list_parser.add_argument("--limit", type=int, default=10)
    list_parser.add_argument("--status", default="pending-review")
    list_parser.add_argument("--write", action="store_true")
    list_parser.add_argument("--dry-run", action="store_true")
    decide_parser = sub.add_parser("decide")
    decide_parser.add_argument("index", type=int)
    decide_parser.add_argument("action")
    args = parser.parse_args()

    if args.cmd == "list":
        items = review_items(status=args.status, limit=args.limit)
        safe_print(format_review(items))
        if args.write:
            output = write_review_queue(items, dry_run=args.dry_run)
            safe_print(f"[review] output={output.relative_to(repo_root())}")
    elif args.cmd == "decide":
        item = decide(args.index, args.action)
        safe_print(f"[review] {item.title} -> {item.status}")


if __name__ == "__main__":
    main()
