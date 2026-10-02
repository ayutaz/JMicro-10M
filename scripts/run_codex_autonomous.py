"""Run successive recorded Codex work turns; start outside the restricted session.

Uses saved Codex CLI login. Does not install software or change global settings.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]
PROMPT = """このプロジェクトの環境整備、実装、学習、評価、改善を継続してください。
AGENTS.md、docs/autonomous_status.md、docs/15_project_roadmap.md、docs/windows_handoff.mdを読んで現在地から進めてください。
まずWSL 3.x/Linux、RTX 4090、固定Tokenizer/pilot、Python/uv、CUDA/BF16を実機で整えてください。
Python実行は環境確認・テスト・一時スクリプトも含めuv run --frozen経由に統一し、system Pythonへフォールバックしないでください。
その後は計画の順に学習器・保存再開・実測batch・Base・Chat・量子化を実装して実行してください。
必要な通常作業はすでに許可されています。小さな区切りで確認を求めず、実行・検証・修正を続けてください。
既存GPUプロセスとcheckpointを確認し、二重起動を避け、会話終了後も復元可能にしてください。
実際の結果、未完了事項、進行中のジョブ、次の作業をdocs/autonomous_status.mdへ必ず残してください。
条件付き追加学習と改善はroadmapの予算・採用条件に従ってください。
利用可能な実行時間内で具体的なmilestoneを進め、最後に指定schemaのJSONを返してください。
実装や学習が残ればcontinue、実外部操作が必要ならneeds_user、要求を証拠付きで達成した場合のみcompleteです。
"""


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-turns", type=int, default=20, help="Maximum successive Codex invocations for this launch")
    parser.add_argument("--dry-run", action="store_true", help="Show configuration without invoking Codex")
    parser.add_argument("--codex", default="codex", help="Codex executable name or path")
    args = parser.parse_args()
    if args.max_turns < 1:
        parser.error("--max-turns must be positive")
    executable = shutil.which(args.codex)
    if executable is None:
        parser.error("Codex CLI not found. Install/login in this execution environment first.")
    if not (ROOT / ".git").exists():
        parser.error("Run from a Git checkout of the project")
    base = [executable, "exec", "--config", 'approval_policy="never"',
            "--sandbox", "danger-full-access", "--cd", str(ROOT), "--json",
            "--output-schema", str(ROOT / "schemas/autonomous_turn.schema.json")]
    if args.dry_run:
        print(json.dumps({"command": base + ["--output-last-message", "<turn>/result.json", "-"],
                          "max_turns": args.max_turns, "prompt": PROMPT,
                          "started": False}, ensure_ascii=False, indent=2))
        return 0
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    run_root = ROOT / "reports/automation" / run_id
    run_root.mkdir(parents=True)
    lock_path = ROOT / "reports/automation/runner.lock"
    try:
        lock_stream = lock_path.open("x", encoding="utf-8")
    except FileExistsError:
        print(f"Another runner may be active: {lock_path}. Inspect its PID before removing a stale lock.", file=sys.stderr)
        return 2
    try:
        with lock_stream:
            lock_stream.write(json.dumps({"pid": os.getpid(), "run_root": str(run_root)}) + "\n")
        previous = None
        for turn in range(1, args.max_turns + 1):
            turn_root = run_root / f"turn-{turn:03d}"
            turn_root.mkdir()
            result_path = turn_root / "result.json"
            prompt = PROMPT
            if previous is not None:
                prompt += "\n直前の実行結果（実際の状態はファイルとプロセスで確認）:\n" + json.dumps(previous, ensure_ascii=False)
            (turn_root / "prompt.txt").write_text(prompt, encoding="utf-8")
            command = base + ["--output-last-message", str(result_path), "-"]
            print(f"Codex turn {turn}/{args.max_turns}; logs: {turn_root}", flush=True)
            with (turn_root / "events.jsonl").open("wb") as events, (turn_root / "stderr.log").open("wb") as errors:
                result = subprocess.run(command, input=prompt.encode("utf-8"), cwd=ROOT,
                                        stdout=events, stderr=errors, check=False)
            if result.returncode != 0:
                print(f"Codex exited {result.returncode}; review {turn_root / 'stderr.log'}. No automatic retry.", file=sys.stderr)
                return 2
            try:
                previous = json.loads(result_path.read_text(encoding="utf-8"))
                if not isinstance(previous, dict) or previous.get("status") not in {"continue", "complete", "needs_user"}:
                    raise ValueError("Invalid autonomous result status")
            except (OSError, ValueError) as exc:
                print(f"No valid result: {exc}; review {turn_root}", file=sys.stderr)
                return 2
            (run_root / "latest_result.json").write_text(json.dumps(previous, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(json.dumps(previous, ensure_ascii=False, indent=2), flush=True)
            if previous["status"] == "complete":
                return 0
            if previous["status"] == "needs_user":
                return 3
        print(f"Launch turn limit reached; work is not marked complete. Restart this runner to continue from docs/autonomous_status.md. Logs: {run_root}")
        return 4
    finally:
        lock_path.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
