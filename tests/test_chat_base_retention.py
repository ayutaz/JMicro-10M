"""Retention math/provenance fixtures; not actual Base/Chat quality evidence."""
import copy
import math
import sys
import pytest

from jmicro.experiment import ROOT, write_json
sys.path.insert(0, str(ROOT/"scripts"))
from review_chat_base_retention import paired_bpb, compare, load_run


def body_fixture():
    rows = [dict(doc_id=f"fixture-{i}", body_tokens=10, scored_body_tokens=10,
        body_bytes=1000 if i < 128 else 1, body_nll=20., eos_nll=1.) for i in range(256)]
    total = sum(r["body_nll"] for r in rows); byte_count = sum(r["body_bytes"] for r in rows)
    return dict(rows=rows, documents=256, body_tokens=2560, body_bytes=byte_count, body_nll=total,
        bpb=total/math.log(2)/byte_count, split="dev", context=1024, stride=512)


def test_paired_bpb_uses_common_byte_weighting_not_average_document_bpb():
    control = body_fixture(); target = copy.deepcopy(control)
    for i, row in enumerate(target["rows"]): row["body_nll"] += 10. if i < 128 else 1.
    target["body_nll"] = sum(r["body_nll"] for r in target["rows"])
    target["bpb"] = target["body_nll"]/math.log(2)/target["body_bytes"]
    result = paired_bpb(control, target)
    assert result["documents"] == 256 and result["common_bytes"] == 128*1001
    assert result["point"] == pytest.approx(11/math.log(2)/1001)
    mean_doc_change = sum((b["body_nll"]-a["body_nll"])/math.log(2)/a["body_bytes"] for a, b in zip(control["rows"], target["rows"])) / 256
    assert result["point"] != pytest.approx(mean_doc_change)
    assert result["degradation_ci_lower_above0"] and result["ci95"][0] > 0
    bad = copy.deepcopy(target); bad["rows"][0]["doc_id"] = "other-document"
    with pytest.raises(AssertionError): paired_bpb(control, bad)
    bad = copy.deepcopy(target); bad["rows"][0]["scored_body_tokens"] -= 1
    with pytest.raises(AssertionError): paired_bpb(control, bad)


def test_retention_decline_is_reported_without_automatic_chat_acceptance():
    cases = {f"fixture-{i}":dict(family_id=f"fixture-family-{i}") for i in range(80)}
    scores = {k:dict(grammar=2, relevance=2, coherence=2, completion=1) for k in cases}
    outputs = [dict(stop_reason="stop_id", repetition=False, valid_utf8=True, role_leak=False, empty_response=False) for _ in cases]
    control = dict(body=body_fixture(), generation=dict(outputs=outputs), evaluation_RNG_isolated=True, protected_test_used=False,
        greedy_rates=dict(outputs=80, eos=80, repetition=0, unicode_failure=0, role_leak=0, empty=0),
        diagnostics={k:dict(complete=True, count=n, primary=dict(accuracy=dict(point=.5))) for k, n in {"semantics":192,"jblimp":331,"jcqa":1119}.items()})
    target = copy.deepcopy(control); target_scores = copy.deepcopy(scores)
    for score in target_scores.values(): score["coherence"] = 0
    target["generation"]["outputs"][0]["role_leak"] = True  # Original Base EOT/role failures must stay visible.
    target["greedy_rates"]["role_leak"] = 1
    report = compare(control, target, scores, target_scores, cases)
    assert report["summaries"]["adopted_Base"]["screen_passed"]
    assert not report["summaries"]["target"]["screen_passed"]
    assert report["paired_content"]["coherence"]["point"] == -1
    assert report["failure_differences"]["role_leak"] == 1
    assert not report["Chat_adopted"] and not report["requested_five_steps_complete"] and report["pending"]


def test_unfinished_and_live_retention_evaluation_rejected(tmp_path, monkeypatch):
    import review_chat_base_retention
    monkeypatch.setattr(review_chat_base_retention, "ROOT", tmp_path)
    run = tmp_path/"reports/phase7/fixture"
    write_json(run/"job.json", dict(status="starting"))
    with pytest.raises(ValueError, match="actually finish"): load_run(run)
    write_json(run/"job.json", dict(status="complete"))
    monkeypatch.setattr(review_chat_base_retention, "alive", lambda _: True)
    with pytest.raises(ValueError, match="actually finish"): load_run(run)
