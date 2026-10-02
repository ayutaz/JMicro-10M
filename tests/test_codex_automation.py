"""Exercise runner control flow with a local stub, without invoking an agent."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("jmicro_autonomous_runner", ROOT / "scripts/run_codex_autonomous.py")
RUNNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUNNER)
STUB = '''import json, sys
from pathlib import Path
root = Path.cwd()
scenario = json.loads((root / "scenario.json").read_text())
calls = root / "calls.jsonl"
index = len(calls.read_text().splitlines()) if calls.exists() else 0
with calls.open("a", encoding="utf-8") as stream:
    stream.write(json.dumps({"args": sys.argv[1:], "prompt": sys.stdin.buffer.read().decode("utf-8")}) + "\\n")
entry = scenario[index]
if entry == "cli_error":
    print("stub external failure", file=sys.stderr)
    raise SystemExit(1)
result = {"status": entry, "milestone": "stub", "summary": "local runner test", "evidence": [], "next_action": "stub", "blocker": None}
Path(sys.argv[sys.argv.index("--output-last-message") + 1]).write_text(json.dumps(result), encoding="utf-8")
print(json.dumps({"type": "turn.completed"}))
'''


class AutonomousRunnerTests(unittest.TestCase):
    def setUp(self):
        local = ROOT / "reports/local"
        local.mkdir(parents=True, exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(dir=local)
        self.root = Path(self.directory.name)
        (self.root / ".git").mkdir()
        (self.root / "exec").write_text(STUB, encoding="utf-8")

    def tearDown(self):
        self.directory.cleanup()

    def run_scenario(self, scenario, limit=3):
        (self.root / "scenario.json").write_text(json.dumps(scenario), encoding="utf-8")
        with patch.object(RUNNER, "ROOT", self.root), patch.object(RUNNER.shutil, "which", return_value=sys.executable), \
                patch.object(sys, "argv", ["runner", "--max-turns", str(limit)]), \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            code = RUNNER.main()
        calls_path = self.root / "calls.jsonl"
        calls = [json.loads(line) for line in calls_path.read_text().splitlines()] if calls_path.exists() else []
        return code, calls

    def test_continues_with_previous_result_and_records_each_turn(self):
        code, calls = self.run_scenario(["continue", "complete"])
        self.assertEqual(code, 0)
        self.assertEqual(len(calls), 2)
        self.assertIn('"status": "continue"', calls[1]["prompt"])
        self.assertIn('approval_policy="never"', calls[0]["args"])
        self.assertIn("danger-full-access", calls[0]["args"])
        self.assertEqual(len(list((self.root / "reports/automation").glob("*/turn-*/events.jsonl"))), 2)
        self.assertFalse((self.root / "reports/automation/runner.lock").exists())

    def test_external_blocker_stops_without_launching_another_turn(self):
        code, calls = self.run_scenario(["needs_user", "complete"])
        self.assertEqual((code, len(calls)), (3, 1))

    def test_turn_limit_is_not_reported_as_completion(self):
        code, calls = self.run_scenario(["continue", "continue"], limit=1)
        self.assertEqual((code, len(calls)), (4, 1))

    def test_cli_error_keeps_diagnostics_and_does_not_retry(self):
        code, calls = self.run_scenario(["cli_error", "complete"])
        self.assertEqual((code, len(calls)), (2, 1))
        log = next((self.root / "reports/automation").glob("*/turn-001/stderr.log"))
        self.assertIn("stub external failure", log.read_text())
        self.assertFalse((self.root / "reports/automation/runner.lock").exists())

    def test_existing_runner_lock_prevents_duplicate_invocation(self):
        lock = self.root / "reports/automation/runner.lock"
        lock.parent.mkdir(parents=True)
        lock.write_text('{"pid": 1234}')
        code, calls = self.run_scenario(["complete"])
        self.assertEqual((code, len(calls)), (2, 0))
        self.assertTrue(lock.exists())


if __name__ == "__main__":
    unittest.main()
