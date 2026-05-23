from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

from utils import clamp, load_items, load_yaml, now_iso, repo_root, safe_print, slugify, today_str, write_text


def existing_urls(topic_dir: Path) -> set[str]:
    urls: set[str] = set()
    for path in topic_dir.glob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        match = re.search(r"^source_url:\s*(.+)$", text, flags=re.MULTILINE)
        if match:
            urls.add(match.group(1).strip().strip('"'))
    return urls


def candidate_text(item: dict[str, Any], date_str: str) -> str:
    title = item.get("title", "Untitled")
    return "\n".join(
        [
            "---",
            f"title: {title}",
            "type: candidate-note",
            "status: pending-review",
            f"topic: {item.get('topic', 'Others')}",
            f"source: {item.get('source_name', '')}",
            f"source_url: {item.get('url', '')}",
            f"published_at: {item.get('published_at', '')}",
            f"captured_at: {now_iso()}",
            f"importance_score: {item.get('importance_score', 1)}",
            "---",
            "",
            "# 这是什么",
            "",
            clamp(item.get("summary") or item.get("raw_text") or "外部来源条目，等待人工 review。", 500),
            "",
            "# 为什么值得关注",
            "",
            item.get("classification_reason", "规则分类认为该条目和当前专题有关。"),
            "",
            "# 和现有知识库的关系",
            "",
            f"- 建议先放入 `{item.get('topic', 'Others')}` 候选池，后续由人工判断是否合入正式专题。",
            "",
            "# 建议进入哪个专题",
            "",
            f"- {item.get('topic', 'Others')}",
            "",
            "# 建议动作",
            "",
            "- [ ] 忽略",
            "- [ ] 加入学习队列",
            "- [ ] 合入正式专题",
            "- [ ] 生成 Playbook",
            "- [ ] 生成对比表",
            "",
            "# 原始来源",
            "",
            f"- 来源：{item.get('source_name', '')}",
            f"- 链接：{item.get('url', '')}",
            f"- 发布时间：{item.get('published_at', '') or '未知'}",
            "",
            "# Agent 判断依据",
            "",
            f"- importance_score: {item.get('importance_score', 1)}",
            f"- topic_scores: {item.get('topic_scores', {})}",
            f"- captured_date: {date_str}",
        ]
    )


def generate_candidates(input_path: Path, dry_run: bool = False, date_str: str | None = None) -> list[Path]:
    root = repo_root()
    router = load_yaml(root / "90-Agent-System/topic-router.yaml")
    topics = router.get("topics", {})
    default_topic = router.get("default_topic", "Others")
    items = [item for item in load_items(input_path) if int(item.get("importance_score", 1)) >= 3]
    output_date = date_str or today_str()
    written: list[Path] = []
    for item in items:
        topic = item.get("topic", default_topic)
        output_dir = root / topics.get(topic, {}).get("output_dir", f"00-Agent-Inbox/Candidates/{topic}")
        existing = existing_urls(output_dir) if output_dir.exists() else set()
        if item.get("url") in existing:
            safe_print(f"[candidates] skip existing URL: {item.get('url')}")
            continue
        output = output_dir / f"{output_date}-{slugify(item.get('title', 'untitled'))}.md"
        if output.exists():
            safe_print(f"[candidates] skip existing file: {output.relative_to(root)}")
            continue
        write_text(output, candidate_text(item, output_date), dry_run=dry_run)
        written.append(output)
    safe_print(f"[candidates] created={len(written)}")
    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None)
    parser.add_argument("--input", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = repo_root()
    date_str = args.date or today_str()
    input_path = Path(args.input) if args.input else root / f"90-Agent-System/logs/classified-items-{date_str}.json"
    if not input_path.is_absolute():
        input_path = root / input_path
    generate_candidates(input_path, dry_run=args.dry_run, date_str=date_str)


if __name__ == "__main__":
    main()
