"""Read the frozen authored TRAIN and public diagnostic; never run a model."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    old = root / "reports/phase7/chat-answer-learning-20261017"
    diagnostic = root / "reports/phase7/chat-quality-100-20261017"
    inventory = read(old / "curriculum_synthetic_inventory.json")
    if args.output.exists():
        raise FileExistsError(args.output)
    if args.train.name != "authored_TRAIN.jsonl":
        raise ValueError("Only the already approved authored TRAIN is accepted")
    if sha(args.train) != inventory["records"]["sha256"]:
        raise ValueError("Frozen TRAIN hash mismatch before JSON parsing")
    rows = [json.loads(line) for line in args.train.read_text(encoding="utf-8").splitlines()]
    assert len(rows) == inventory["unique_targets"] == 2048
    families = Counter(row["family"] for row in rows)
    assert dict(families) == inventory["families"]
    assert all(row["split"] == "train" for row in rows)
    grouped = {family: [r for r in rows if r["family"] == family] for family in families}
    arithmetic = grouped["arithmetic"]
    # All arithmetic targets are independently recalculated from the rendered input.
    for row in arithmetic:
        question = row["messages"][-2]["text"]
        numbers = [int(n) for n in re.findall(r"(\d+)個", question)]
        assert len(numbers) == 2
        assert row["messages"][-1]["text"] == f"{sum(numbers)}個です。"
    literal_answers = {r["messages"][-1]["text"] for r in grouped["literal"]}
    corrections = grouped["correction"]
    assert all("集合時刻は" in r["messages"][2]["text"] for r in corrections)
    owners = grouped["owner"]
    owner_order = Counter(
        tuple(re.findall(r"さんが(鍵|地図)を持っています", r["messages"][0]["text"]))
        for r in owners
    )
    quantities = grouped["quantity"]
    quantity_order = Counter(
        tuple(re.findall(r"(青|赤)い箱には", r["messages"][0]["text"]))
        for r in quantities
    )
    final_only = sum(r["target_message_indices"] == [len(r["messages"]) - 1] for r in rows)
    cases = read(diagnostic / "cases.json")["cases"]
    notes = read(diagnostic / "notes.json")["all200_literal_judgments"]
    results = {r["id"]: r for r in notes if r["final"]}
    calc = {}
    for label, marker in (("addition", "足す"), ("subtraction", "引く")):
        selected = [c for c in cases if c["category"] == "arithmetic" and marker in c["turns"][0]["user"]]
        calc[label] = {"cases": len(selected), "task_pass": sum(results[c["id"]]["task_pass"] for c in selected)}
    own = [c for c in cases if c["mode"] == "own"]
    assert len(own) == 20 and all(len(c["turns"]) == 6 for c in own)
    inputs = [old / "curriculum_synthetic_inventory.json", old / "curriculum_TRAIN_preparation.json",
              old / "curriculum_C1_CPU_replay.json", diagnostic / "cases.json",
              diagnostic / "notes.json", diagnostic / "summary.json",
              root / "scripts/prepare_answer_curriculum.py", Path(__file__).resolve()]
    report = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "frozen_TRAIN_and_existing_public_diagnostic_audited_no_model_execution",
        "inputs": [{"path": str(p.relative_to(root)), "sha256": sha(p)} for p in inputs],
        "TRAIN": {"path": inventory["records"]["path"], "observed_path": str(args.train), "sha256": sha(args.train),
                  "rows": len(rows), "families": dict(families),
                  "prompt_message_counts": dict(sorted(Counter(len(r["messages"]) - 1 for r in rows).items())),
                  "final_assistant_only_targets": final_only,
                  "arithmetic": {"addition_targets_independently_recalculated": len(arithmetic), "subtraction_in_this_family": 0},
                  "literal": {"unique_answers": len(literal_answers), "ASCII_letter_or_digit_answers": sum(bool(re.search(r"[A-Za-z0-9]", a)) for a in literal_answers)},
                  "correction": {"meeting_time_changes": len(corrections)},
                  "owner_first_mention_order": [{"order": list(k), "rows": n} for k, n in owner_order.items()],
                  "quantity_first_mention_order": [{"order": list(k), "rows": n} for k, n in quantity_order.items()]},
        "existing_diagnostic": {"arithmetic_final_task": calc, "own_cases": len(own),
                                "own_final_question_turn": 6,
                                "confounded_changes": ["query position and history length", "one versus two requested fields", "extra facts and intervening topics", "actual assistant history content"]},
        "interpretation": [
            "Coverage findings apply to this 2048-row authored subset, not all SFT or Base TRAIN.",
            "All five addition diagnostic prompts also failed: missing subtraction TRAIN alone cannot explain arithmetic failure.",
            "Final-only supervision is the saved intended mask, not evidence of a trainer defect.",
            "Query templates and fixed fact orders limit structural diversity; causal effect is unmeasured.",
            "The 100-case benchmark cannot isolate history distance from requested field count.",
        ],
        "new_training_updates": 0, "new_model_responses": 0, "new_GPU_work": 0, "sealed_TEST_reads": 0,
    }
    assert final_only == 2048
    assert len(literal_answers) == 32
    assert owner_order == {("鍵", "地図"): 256}
    assert quantity_order == {("青", "赤"): 256}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(report, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(json.dumps({"report": str(args.output), "rows": len(rows), "arithmetic": calc}, ensure_ascii=False))


if __name__ == "__main__":
    main()
