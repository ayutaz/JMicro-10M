"""Shared evidence checks for an adopted Base before dialogue GPU training."""
import json
from pathlib import Path
from jmicro.experiment import ROOT, read_json, sha256
from jmicro.tokenizer import Tokenizer
from review_eos_5b_finish import validate_rows
from run_eos_short_pilot import rate


def require_adopted_base(config):
    for key in ("parent", "Base_acceptance", "Base_evaluation", "Base_annotations", "tokenizer"):
        ref = config[key]
        assert sha256(Path(ref["path"])) == ref["sha256"]
    accepted = read_json(Path(config["Base_acceptance"]["path"]))
    if accepted.get("Base_adopted") is not True:
        raise ValueError("A quality-adopted Base is required before dialogue GPU training")
    assert accepted["checkpoint_sha256"] == config["parent"]["sha256"]
    assert accepted["evaluation_sha256"] == config["Base_evaluation"]["sha256"]
    assert accepted["annotations_sha256"] == config["Base_annotations"]["sha256"]
    assert accepted["quality_criteria_unchanged"] is True
    ev = read_json(Path(config["Base_evaluation"]["path"]))
    assert ev["checkpoint_sha256"] == config["parent"]["sha256"] and ev["evaluation_RNG_isolated"] and not ev["protected_test_used"]
    tok = Tokenizer(config["tokenizer"]["path"])
    rows = ev["generation"]["outputs"]; validate_rows(rows, tok)
    cases = {r["id"]:r for r in (json.loads(s) for s in (ROOT/"eval/base.jsonl").read_text().splitlines()) if r["split"] == "dev"}
    assert len(rows) == 80 and {r["id"] for r in rows} == set(cases)
    assert all(r["prefix"] == cases[r["id"]]["prefix"] for r in rows)
    notes = read_json(Path(config["Base_annotations"]["path"]))["notes"]
    scores = {n[0]:n for n in notes}
    assert len(notes) == len(scores) == 80 and set(scores) == set(cases)
    assert all(all(type(n[i]) is int and n[i] in (0,1,2) for i in (1,2,3))
               and type(n[4]) is int and n[4] in (0,1) and isinstance(n[5],str) and len(n[5]) >= 12 for n in notes)
    assert all(not scores[r["id"]][4] or r["stop_reason"] == "stop_id" and scores[r["id"]][2] >= 1 and scores[r["id"]][3] >= 1 for r in rows)
    assert sum(n[1] == 2 for n in notes) >= 56 and sum(n[3] == 2 for n in notes) >= 27 and sum(n[4] for n in notes) >= 27
    rates = rate(rows); assert rates == ev["greedy_rates"]
    assert rates["eos"] >= 37 and rates["repetition"] <= 18 and all(rates[k] == 0 for k in ("unicode_failure", "role_leak", "empty"))
    return tok
