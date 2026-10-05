"""Review completed full dev/400/long outputs without repeating inference."""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from jmicro.japanese_evaluation import repetition_metrics
from phase6_performance import alive
from run_eos_short_pilot import equal_state
from run_final_base_dev import preflight, audit_full


def row_key(row):
    return f"{row['id']}|{row.get('max_new_tokens',64)}|{row.get('decoding','greedy')}|{int(row.get('suppressed',True))}|{row.get('seed',42)}"


def validate_long(rows, tok):
    cases, counts = {}, Counter()
    for case in (json.loads(s) for s in (ROOT/"eval/base.jsonl").read_text().splitlines()):
        if case["split"] == "dev" and counts[case["category"]] < 2:
            cases[case["id"]] = case; counts[case["category"]] += 1
    assert len(rows) == 2*len(cases) == 40
    assert {(r["id"], r["max_new_tokens"]) for r in rows} == {(case, n) for case in cases for n in (128,512)}
    for row in rows:
        case, ids = cases[row["id"]], row["generated_ids"]
        assert row["prefix"] == case["prefix"] and row["category"] == case["category"]
        assert 0 < len(ids) <= row["max_new_tokens"] and 3 not in ids[:-1] and 1 not in ids
        raw = tok.decode_bytes(ids)
        try: text, valid = raw.decode(), True
        except UnicodeDecodeError: text, valid = raw.decode(errors="replace"), False
        assert row["text"] == text and row["valid_utf8"] == valid
        assert row["stop_reason"] == ("stop_id" if ids[-1] == 3 else "max_new_tokens")
        assert equal_state(row["metrics"], repetition_metrics(row))


def validate_content(rows, notes):
    by_key = {row_key(r):r for r in rows}
    assert len(by_key) == len(rows)
    scores = {n[0]:n for n in notes}
    assert len(notes) == len(scores) == len(rows) and set(scores) == set(by_key)
    for key, n in scores.items():
        assert len(n) == 6 and all(type(n[i]) is int and n[i] in (0,1,2) for i in (1,2,3))
        assert type(n[4]) is int and n[4] in (0,1) and isinstance(n[5], str) and len(n[5].strip()) >= 12
        assert not n[4] or by_key[key]["stop_reason"] == "stop_id" and n[2] >= 1 and n[3] >= 1
    return scores


def review(path, notes_path, template=False):
    c = read_json(path); output = ROOT/c["output"]
    job = read_json(output/"job.json")
    if job["status"] != "complete" or alive(job):
        raise ValueError("Full dev evaluation must actually finish before review")
    c, screen, _, inherited = preflight(path)
    result, ev, long = (read_json(output/name) for name in ("result.json", "full-dev.json", "long-generation.json"))
    assert job["config_sha256"] == result["binding"]["config_sha256"] == sha256(path)
    assert ev["binding"] == result["binding"] and long["binding"] == json.dumps(result["binding"], sort_keys=True)
    assert result["GPU_seconds"] <= job["gpu_elapsed_seconds"] <= c["GPU_budget_seconds"]
    assert result["full_evaluation_sha256"] == sha256(output/"full-dev.json")
    assert result["long_generation_sha256"] == sha256(output/"long-generation.json")
    assert result["evaluation_RNG_isolated"] and result["long_generation"]["complete"] and long["complete"]
    assert not result["protected_test_used"] and not result["Base_adopted"] and not result["independent_training_seed_confirmed"]
    tok = Tokenizer(c["tokenizer"]["path"])
    parent_body = read_json(Path(c["references"]["parent_body"]["path"]))["body"]
    parent_generation = read_json(Path(c["references"]["parent_generation"]["path"]))["generation"]
    checks, _ = audit_full(ev, screen, tok, parent_body, parent_generation, read_json(Path(c["references"]["web_full"]["path"])))
    assert checks == result["checks"] and result["full_automatic_conditions_pass"] == all(v for g in checks.values() for v in g.values())
    validate_long(long["rows"], tok)
    rows = [*ev["generation"]["outputs"], *long["rows"]]
    previous = {n[0]:n for n in inherited["notes"]}
    fixed = {row_key(r):[row_key(r), *previous[r["id"]][1:]] for r in ev["generation"]["outputs"] if r["suppressed"] and r["decoding"] == "greedy"}
    assert len(fixed) == 80
    if template:
        assert not notes_path.exists(), "Existing notes preserved"
        atomic_json(notes_path, dict(reviewer="Codex nonblind; read all new320+40 outputs individually",
            independent_human_blind=False, full_evaluation_sha256=result["full_evaluation_sha256"],
            long_generation_sha256=result["long_generation_sha256"],
            inherited_fixed80_annotations=c["source_annotations"],
            notes=[fixed.get(row_key(r), [row_key(r),None,None,None,None,""]) for r in rows]))
        print("Saved440 template with exact unchanged80 judgments retained; new360 remain unscored"); return
    document = read_json(notes_path)
    assert document["full_evaluation_sha256"] == result["full_evaluation_sha256"] and document["long_generation_sha256"] == result["long_generation_sha256"]
    assert document["independent_human_blind"] is False and isinstance(document["reviewer"], str) and document["reviewer"].strip()
    scores = validate_content(rows, document["notes"])
    assert document["inherited_fixed80_annotations"] == c["source_annotations"]
    assert all(scores[k] == n for k,n in fixed.items())
    groups = {}
    for r in rows:
        group = row_key(r).split("|",1)[1]; groups.setdefault(group, []).append(scores[row_key(r)])
    report = dict(status="full_dev_all400_and_long40_content_evidence_complete", config_sha256=sha256(path),
        result_sha256=sha256(output/"result.json"), notes_sha256=sha256(notes_path),
        full_evaluation_sha256=result["full_evaluation_sha256"], long_generation_sha256=result["long_generation_sha256"],
        checks=checks, full_automatic_conditions_pass=result["full_automatic_conditions_pass"],
        content={key:dict(count=len(ns), grammar2=sum(n[1]==2 for n in ns), relevance2=sum(n[2]==2 for n in ns),
            coherence2=sum(n[3]==2 for n in ns), appropriate=sum(n[4] for n in ns)) for key,ns in groups.items()},
        long_native_failures=dict(unicode=sum(not r["valid_utf8"] for r in long["rows"]),
            empty=sum(not r["text"].strip() for r in long["rows"]), role_leak=sum(any(i in (4,5,6,7) for i in r["generated_ids"]) for r in long["rows"])),
        inherited_fixed80_count=80, newly_reviewed_raw_count=360, total_raw_content_count=440,
        protected_test_used=False, independent_training_seed_confirmed=False, independent_human_blind=False,
        Base_adopted=False, final_test_pending=True, quality_criteria_unchanged=True, requested_five_steps_complete=False, created_at=now())
    atomic_json(output/"review.json", report)
    atomic_json(ROOT/"reports/phase6"/(output.name+"_review.json"), report)
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    assert sys.version_info[:3] == (3,12,7)
    parser = argparse.ArgumentParser(); parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--notes", type=Path, required=True); parser.add_argument("--template", action="store_true")
    args = parser.parse_args(); path, notes = args.config.resolve(), args.notes.resolve()
    assert path.is_relative_to(ROOT/"configs/phase6") and notes.is_relative_to(ROOT/"reports/phase6")
    review(path, notes, args.template)
