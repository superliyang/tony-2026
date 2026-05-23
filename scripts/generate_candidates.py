from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

from utils import clamp, extract_frontmatter, load_items, load_yaml, now_iso, repo_root, safe_print, slugify, today_str, write_text


def existing_candidates(topic_dir: Path) -> dict[str, Path]:
    candidates: dict[str, Path] = {}
    for path in topic_dir.glob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        match = re.search(r"^source_url:\s*(.+)$", text, flags=re.MULTILINE)
        if match:
            candidates[match.group(1).strip().strip('"')] = path
    return candidates


def set_frontmatter_value(text: str, key: str, value: str) -> str:
    if not text.startswith("---\n"):
        return text
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


def update_section(text: str, heading: str, content: str) -> str:
    pattern = re.compile(rf"({re.escape(heading)}\n\n).*?(\n\n# )", flags=re.DOTALL)
    return pattern.sub(lambda match: f"{match.group(1)}{content}{match.group(2)}", text, count=1)


def set_agent_action(text: str, action: str) -> str:
    if re.search(r"Agent 建议动作：`[^`]+`", text):
        return re.sub(r"Agent 建议动作：`[^`]+`", f"Agent 建议动作：`{action}`", text, count=1)
    return text.replace("\n# 原始来源", f"\nAgent 建议动作：`{action}`\n\n# 原始来源", 1)


def set_analysis_line(text: str, key: str, value: str) -> str:
    pattern = re.compile(rf"^- {re.escape(key)}:.*$", flags=re.MULTILINE)
    replacement = f"- {key}: {value}"
    if pattern.search(text):
        return pattern.sub(replacement, text, count=1)
    return text.replace("- captured_date:", f"{replacement}\n- captured_date:", 1)


def refresh_pending_candidate(path: Path, item: dict[str, Any], dry_run: bool = False) -> bool:
    semantic = item.get("semantic_analysis") if isinstance(item.get("semantic_analysis"), dict) else {}
    if not semantic:
        return False
    text = path.read_text(encoding="utf-8")
    meta, _ = extract_frontmatter(text)
    if meta.get("status", "pending-review") != "pending-review":
        return False
    action = item.get("ai_suggested_action") or semantic.get("suggested_action") or "review"
    updated = set_frontmatter_value(text, "ai_suggested_action", str(action))
    updated = set_frontmatter_value(updated, "ai_confidence", str(semantic.get("confidence", "")))
    updated = update_section(updated, "# 为什么值得关注", str(semantic.get("learning_value", "")).strip())
    updated = update_section(updated, "# 和现有知识库的关系", f"- {semantic.get('vault_relationship', '')}".strip())
    updated = set_agent_action(updated, str(action))
    updated = set_analysis_line(updated, "semantic_topic", str(semantic.get("semantic_topic", "")))
    updated = set_analysis_line(updated, "ai_reason", str(semantic.get("reason", "")))
    if updated == text:
        return False
    write_text(path, updated, dry_run=dry_run)
    return True


def candidate_text(item: dict[str, Any], date_str: str) -> str:
    title = item.get("title", "Untitled")
    semantic = item.get("semantic_analysis") if isinstance(item.get("semantic_analysis"), dict) else {}
    learning_value = item.get("ai_learning_value") or semantic.get("learning_value") or item.get("classification_reason", "")
    vault_relationship = item.get("ai_vault_relationship") or semantic.get("vault_relationship") or f"建议先放入 `{item.get('topic', 'Others')}` 候选池，后续由人工判断是否合入正式专题。"
    suggested_action = item.get("ai_suggested_action") or semantic.get("suggested_action") or "review"
    ai_reason = item.get("ai_reason") or semantic.get("reason") or item.get("classification_reason", "")
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
            f"ai_suggested_action: {suggested_action}",
            f"ai_confidence: {semantic.get('confidence', '')}",
            "---",
            "",
            "# 这是什么",
            "",
            clamp(item.get("summary") or item.get("raw_text") or "外部来源条目，等待人工 review。", 500),
            "",
            "# 为什么值得关注",
            "",
            learning_value or "规则分类认为该条目和当前专题有关。",
            "",
            "# 和现有知识库的关系",
            "",
            f"- {vault_relationship}",
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
            f"Agent 建议动作：`{suggested_action}`",
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
            f"- semantic_topic: {semantic.get('semantic_topic', '')}",
            f"- ai_reason: {ai_reason}",
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
    refreshed = 0
    for item in items:
        topic = item.get("topic", default_topic)
        output_dir = root / topics.get(topic, {}).get("output_dir", f"00-Agent-Inbox/Candidates/{topic}")
        existing = existing_candidates(output_dir) if output_dir.exists() else {}
        existing_path = existing.get(item.get("url", ""))
        if existing_path:
            if refresh_pending_candidate(existing_path, item, dry_run=dry_run):
                refreshed += 1
                safe_print(f"[candidates] refreshed AI triage: {existing_path.relative_to(root)}")
            else:
                safe_print(f"[candidates] skip existing URL: {item.get('url')}")
            continue
        output = output_dir / f"{output_date}-{slugify(item.get('title', 'untitled'))}.md"
        if output.exists():
            safe_print(f"[candidates] skip existing file: {output.relative_to(root)}")
            continue
        write_text(output, candidate_text(item, output_date), dry_run=dry_run)
        written.append(output)
    safe_print(f"[candidates] created={len(written)} refreshed={refreshed}")
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
