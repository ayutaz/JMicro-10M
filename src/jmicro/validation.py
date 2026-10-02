"""Validate the Phase 0 artifacts against their actual contracts."""

from collections import Counter
from pathlib import Path
import argparse
import json

from jsonschema import Draft202012Validator, FormatChecker

from jmicro.evaluation import canonicalize_text
from jmicro.experiment import ROOT, now, read_json, sha256, write_json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_phase0(root: Path = ROOT) -> dict:
    configs = []
    for path in sorted((root / "configs").rglob("*.json")):
        relative = path.relative_to(root)
        schema = read_json(root / "schemas" / relative.with_suffix(".schema.json"))
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema, format_checker=FormatChecker()).validate(read_json(path))
        configs.append({"path": relative.as_posix(), "sha256": sha256(path)})
    for name, expected in (("t8k", 9_772_800), ("t4k", 10_002_816)):
        m = read_json(root / f"configs/models/{name}.json")
        h, d, q, kv = m["hidden_size"], m["head_dim"], m["num_attention_heads"], m["num_key_value_heads"]
        require(q * d == h and q % kv == 0, f"{name}: invalid GQA dimensions")
        require(m["tie_word_embeddings"] and m["qk_norm_type"] == "rms_head_shared", f"{name}: parameter allocation changed")
        count = m["vocab_size"] * h + m["num_hidden_layers"] * (h * (q * d + 2 * kv * d) + q * d * h + 3 * h * m["intermediate_size"] + 2 * h + 2 * d) + h
        require(count == expected == m["expected_parameter_count"], f"{name}: parameter count mismatch")
        require(m["max_position_embeddings"] == 1024 and m["rotary_dim"] == d, f"{name}: context/rotary mismatch")
    train = read_json(root / "configs/training/baseline.json")
    require(train["micro_batch"] is None and train["effective_batch_tokens"] is None, "Unmeasured batch must stay unresolved")
    require(not train["training_on_imac"] and train["seed"] == 42, "Training environment or seed mismatch")
    tok = read_json(root / "configs/tokenizer/contract.json")
    require([x["id"] for x in tok["special_tokens"]] == list(range(8)), "Special IDs must be unique and fixed")
    require(len({x["piece"] for x in tok["special_tokens"]}) == 8, "Duplicate special pieces")
    require(tok["encode_body_separately"] and tok["insert_role_ids"], "Role symbols must be separate structural IDs")
    golden = read_json(root / "eval/tokenizer_golden.json")["cases"]
    for case in golden:
        require(canonicalize_text(case["input"]) == case["canonical"], f"Canonicalization mismatch: {case['id']}")
    suite_manifest = read_json(root / "eval/split_manifest.json")
    case_schema = read_json(root / "schemas/evaluation_case.schema.json")
    Draft202012Validator.check_schema(case_schema)
    validator = Draft202012Validator(case_schema)
    suites = {}
    all_ids, families, prompts = set(), {}, set()
    for suite in ("base", "chat"):
        entry = suite_manifest["files"][suite]
        path = root / entry["path"]
        require(sha256(path) == entry["sha256"], f"{suite}: split manifest checksum mismatch")
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        require(len(rows) == entry["count"] == 100, f"{suite}: expected 100 cases")
        counts = Counter()
        for row in rows:
            validator.validate(row)
            require(row["suite"] == suite, "Suite mismatch")
            require(row["id"] not in all_ids, f"Duplicate ID: {row['id']}")
            all_ids.add(row["id"])
            old_split = families.setdefault(row["family_id"], row["split"])
            require(old_split == row["split"], "Prompt family crosses dev/test")
            counts[(row["category"], row["split"])] += 1
            if suite == "chat":
                messages = row["messages"]
                require(len(messages) % 2 == 1, "Chat history must end on a user turn")
                require([m["role"] for m in messages] == ["user" if i % 2 == 0 else "assistant" for i in range(len(messages))], "Unexpected role sequence")
                if row["category"] == "context":
                    require(3 <= (len(messages) + 1) // 2 <= 4, "Context case must have 3-4 user turns")
                prompt = json.dumps(messages, ensure_ascii=False, sort_keys=True)
            else:
                prompt = row["prefix"]
            require(prompt not in prompts, "Exact duplicate evaluation input")
            prompts.add(prompt)
        for split, expected in (("dev", 80), ("test", 20)):
            ids = [x["id"] for x in rows if x["split"] == split]
            require(len(ids) == expected and ids == entry[f"{split}_ids"], f"{suite}: {split} membership mismatch")
        require(set(entry["categories"]) == {x["category"] for x in rows}, f"{suite}: category mismatch")
        require(len(entry["categories"]) == 10, f"{suite}: expected 10 categories")
        for category in entry["categories"]:
            require(counts[(category, "dev")] == 8 and counts[(category, "test")] == 2, "Category balance mismatch")
        suites[suite] = {"cases": len(rows), "dev": 80, "test": 20, "categories": 10, "sha256": sha256(path)}
    protocol = read_json(root / "configs/evaluation/protocol.json")
    require(protocol["generation"]["chat_stop_ids"] == tok["chat_stop_ids"], "Chat stop IDs mismatch")
    require(protocol["generation"]["base_stop_ids"] == tok["base_stop_ids"], "Base stop IDs mismatch")
    require(protocol["generation"]["suppress_body_ids"] == [0, 1, 2, 4, 5, 6], "Unexpected generation suppression")
    examples = read_json(root / "eval/rubric_examples.json")["examples"]
    require(len(examples) >= 9, "Insufficient rubric examples")
    for example in examples:
        require(example["reviewer_type"] == "assistant_manual_design_review", "Do not claim independent human evaluation")
        for metric in ("grammar", "relevance", "context"):
            require(example["scores"][metric] in (None, 0, 1, 2), "Invalid rubric score")
    return {"schema_version": 1, "checked_at": now(), "status": "passed",
            "checks": ["config_schema", "parameter_budget_formula", "fixed_special_ids", "unmeasured_batch",
                       "canonicalization_golden", "suite_schema", "unique_inputs", "family_split_disjoint",
                       "split_manifest_hashes", "category_balance", "history_roles", "stop_ids", "rubric_examples"],
            "configs": configs, "suites": suites, "canonicalization_examples": len(golden),
            "rubric_examples": len(examples), "model_implementation_checked_by_this_validator": False, "gpu_verified": False,
            "independent_human_review_done": False}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "reports/phase0/validation.json")
    args = parser.parse_args()
    result = validate_phase0()
    output = args.output
    write_json(output, result)
    print(json.dumps({"status": result["status"], "suites": result["suites"], "report": str(output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
