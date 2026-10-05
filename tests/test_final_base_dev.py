import copy
import json
import math
import sys
import pytest
from jmicro.experiment import ROOT, write_json, sha256
from jmicro.tokenizer import Tokenizer

sys.path.insert(0, str(ROOT/"scripts"))
from run_final_base_dev import completed_source, source_evidence, validate_body, validate_generation, screen_checks
from phase6_performance import identity
from run_eos_short_pilot import rate


def test_final_dev_rejects_running_and_actually_live_learning_before_other_reads(tmp_path):
    run = tmp_path/"learning"; run.mkdir()
    write_json(run/"job.json", dict(status="running"))
    with pytest.raises(ValueError, match="actually finish"):
        source_evidence(tmp_path/"missing-config.json", run, "not-trained")
    write_json(run/"job.json", dict(status="complete", **identity()))
    with pytest.raises(ValueError, match="actually finish"):
        completed_source(run)


def test_full_body_requires_all_targets_common_byte_denominator_and_no_duplicate_documents():
    rows = [dict(doc_id="a", body_tokens=2, scored_body_tokens=2, body_bytes=3, body_nll=2., eos_nll=1.),
            dict(doc_id="b", body_tokens=5, scored_body_tokens=5, body_bytes=100, body_nll=7., eos_nll=1.)]
    body = dict(split="dev", limit_documents=None, documents=2, rows=rows,
        body_bytes=103, body_tokens=7, body_nll=9., bpb=9/math.log(2)/103)
    validate_body(body)
    for change in (lambda b:b["rows"][1].__setitem__("scored_body_tokens", 4),
                   lambda b:b["rows"][1].__setitem__("doc_id", "a"),
                   lambda b:b.__setitem__("bpb", sum(r["body_nll"]/r["body_bytes"] for r in b["rows"])/2/math.log(2)),
                   lambda b:b.__setitem__("split", "test"),
                   lambda b:b.__setitem__("limit_documents", 256)):
        changed = copy.deepcopy(body); change(changed)
        with pytest.raises(AssertionError): validate_body(changed)


def native_generations():
    tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    cases = [json.loads(s) for s in (ROOT/"eval/base.jsonl").read_text().splitlines() if json.loads(s)["split"] == "dev"]
    ids = [*tok.encode("今日は晴れた。"), 3]
    rows = []
    for case in cases:
        for suppressed, seed in ((True, None), (False, None), (True, 42), (True, 43), (True, 44)):
            rows.append(dict(id=case["id"], prefix=case["prefix"], category=case["category"], split="dev",
                suppressed=suppressed, seed=42 if seed is None else seed,
                decoding="greedy" if seed is None else "sampling", generated_ids=list(ids),
                text=tok.decode_bytes(ids).decode(), valid_utf8=True, role_leak=False,
                empty_response=False, stop_reason="stop_id", repetition=False))
    generation = dict(suite_sha256=sha256(ROOT/"eval/base.jsonl"), split="dev", max_new_tokens=64,
        sampling_evaluated=True, temperature=.8, top_p=.9, outputs=rows)
    screen = dict(generation=dict(outputs=[copy.deepcopy(r) for r in rows if r["suppressed"] and r["decoding"] == "greedy"]))
    return tok, generation, screen


def test_full_native_generation_preserves_failures_in_unsuppressed_and_sampling_conditions():
    tok, generation, screen = native_generations()
    reference = copy.deepcopy(generation)
    # The fixed80 screen stays intact, but a validly recorded raw failure in
    # another condition must survive into the full400 counters.
    row = generation["outputs"][1]
    row.update(generated_ids=[1, 3], text="", valid_utf8=False, empty_response=True)
    rates = validate_generation(generation, screen, tok, reference)
    assert rates["fixed80"]["unicode_failure"] == rates["fixed80"]["empty"] == 0
    assert rates["all400"]["unicode_failure"] == rates["all400"]["empty"] == 1
    row["valid_utf8"] = True
    with pytest.raises(AssertionError): validate_generation(generation, screen, tok, reference)


def test_full_generation_rejects_missing_modes_changed_seed_and_different_screen_ids():
    tok, generation, screen = native_generations()
    reference = copy.deepcopy(generation)
    for change in (lambda g:g["outputs"].pop(), lambda g:g["outputs"][2].__setitem__("seed", 99),
                   lambda g:g["outputs"][0].__setitem__("generated_ids", [3])):
        changed = copy.deepcopy(generation); change(changed)
        with pytest.raises(AssertionError): validate_generation(changed, screen, tok, reference)


def test_absolute_base_screen_does_not_accept_loss_or_good_grammar_alone():
    _, generated, screen = native_generations()
    ev = dict(greedy_rates=rate(screen["generation"]["outputs"]))
    scores = {str(i):dict(grammar=2, relevance=2, coherence=2, completion=1) for i in range(80)}
    assert all(screen_checks(ev, scores).values())
    for s in list(scores.values())[:54]: s["coherence"] = 1; s["completion"] = 0
    checks = screen_checks(ev, scores)
    assert checks["grammar_at_least56"] and not checks["coherence_at_least27"] and not checks["appropriate_at_least27"]


def test_full_content_review_requires_every_raw_condition_and_real_EOS():
    from review_final_base_dev import validate_content, row_key
    _, generation, _ = native_generations()
    rows = generation["outputs"]
    notes = [[row_key(r),2,2,2,1,"元の話題に合う日本語の文章がEOSで完結しています。"] for r in rows]
    assert len(validate_content(rows, notes)) == 400
    with pytest.raises(AssertionError): validate_content(rows, notes[:-1])
    changed = copy.deepcopy(rows); changed[2]["stop_reason"] = "max_new_tokens"
    with pytest.raises(AssertionError): validate_content(changed, notes)
    changed_notes = copy.deepcopy(notes); changed_notes[2][1] = True
    with pytest.raises(AssertionError): validate_content(rows, changed_notes)


def test_long_review_checks_both_limits_native_bytes_and_saved_repetition_metrics():
    from collections import Counter
    from jmicro.japanese_evaluation import repetition_metrics
    from review_final_base_dev import validate_long
    tok, _, screen = native_generations()
    counts, cases = Counter(), []
    for row in screen["generation"]["outputs"]:
        if counts[row["category"]] < 2:
            cases.append(row); counts[row["category"]] += 1
    rows = []
    for maximum in (128,512):
        for row in cases:
            r = {k:copy.deepcopy(row[k]) for k in ("id","prefix","category","generated_ids","text","valid_utf8","stop_reason")}
            r["max_new_tokens"] = maximum; r["metrics"] = repetition_metrics(r); rows.append(r)
    validate_long(rows, tok)
    with pytest.raises(AssertionError): validate_long(rows[:-1], tok)
    changed = copy.deepcopy(rows); changed[0]["text"] = "表示だけを変更しました。"
    with pytest.raises(AssertionError): validate_long(changed, tok)
    changed = copy.deepcopy(rows); changed[0]["metrics"]["natural_eos"] = False
    with pytest.raises(AssertionError): validate_long(changed, tok)
