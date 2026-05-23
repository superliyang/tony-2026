from __future__ import annotations

import argparse
from pathlib import Path

from notify_feishu import summarize_markdown
from utils import load_local_env, load_yaml, repo_root, safe_print


def latest_markdown(folder: Path) -> Path | None:
    files = sorted(folder.glob("*.md"), key=lambda path: path.stat().st_mtime, reverse=True)
    return files[0] if files else None


def command_response(text: str) -> str:
    root = repo_root()
    cleaned = text.strip().lower()
    if cleaned in {"/ping", "ping"}:
        return "pong: knowledge automation bot is alive."
    if cleaned.startswith("/daily"):
        path = latest_markdown(root / "00-Agent-Inbox/Daily-Digests")
        return summarize_markdown(path, 5) if path else "还没有 Daily Digest。"
    if cleaned.startswith("/weekly"):
        path = latest_markdown(root / "00-Agent-Inbox/Weekly-Digests")
        return summarize_markdown(path, 5) if path else "还没有 Weekly Digest。"
    if cleaned.startswith("/health"):
        path = latest_markdown(root / "90-Agent-System/reports")
        return summarize_markdown(path, 5) if path else "还没有 Vault Health Report。"
    return "可用命令：/ping、/daily、/weekly、/health"


def run_bot(dry_run: bool = False) -> None:
    load_local_env()
    root = repo_root()
    config = load_yaml(root / "90-Agent-System/feishu-bot.yaml").get("websocket_bot", {})
    app_id_env = config.get("app_id_env", "FEISHU_APP_ID")
    app_secret_env = config.get("app_secret_env", "FEISHU_APP_SECRET")

    import os

    app_id = os.getenv(app_id_env)
    app_secret = os.getenv(app_secret_env)
    if dry_run:
        safe_print(f"[feishu-bot] enabled={config.get('enabled', False)} app_id_configured={bool(app_id)} app_secret_configured={bool(app_secret)}")
        safe_print(f"[feishu-bot] commands={', '.join(config.get('commands', []))}")
        return
    if not config.get("enabled", False):
        safe_print("[feishu-bot] disabled in feishu-bot.yaml")
        return
    if not app_id or not app_secret:
        raise SystemExit(f"Missing {app_id_env} or {app_secret_env}. Put them in 90-Agent-System/.env.local or shell env.")

    try:
        from lark_oapi.channel import FeishuChannel
    except ImportError as exc:
        raise SystemExit("Missing dependency: pip install lark-oapi") from exc

    channel = FeishuChannel(app_id=app_id, app_secret=app_secret)

    async def on_message(msg) -> None:
        text = getattr(msg, "content_text", "") or ""
        chat_id = getattr(msg, "chat_id", "")
        if not chat_id:
            safe_print("[feishu-bot] received message without chat_id; skip reply")
            return
        response = command_response(text)
        await channel.send(chat_id, {"text": response})
        safe_print(f"[feishu-bot] handled command: {text.strip() or '<empty>'}")

    channel.on("message", on_message)
    safe_print("[feishu-bot] connecting via WebSocket. Press Ctrl+C to stop.")
    channel.start()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run_bot(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
