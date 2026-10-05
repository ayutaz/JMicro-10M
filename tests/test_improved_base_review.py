"""Actual CPU extension states, distinct from useful GPU/Base quality evidence."""
import sys

import pytest
import torch
from jmicro.experiment import ROOT, write_json, sha256

sys.path.insert(0, str(ROOT/"scripts"))
from test_curve_extension import fixture
from review_improved_base import audit_extension, review


def test_review_checks_new_rows_against_inherited_cumulative_state(tmp_path):
    path, _, _, _, build = fixture(tmp_path)
    parent = torch.load(path, map_location="cpu", weights_only=False)
    trainer = build(); trainer.load_extension(path)
    rows = []
    while trainer.sampler.source_teachers["short"] < 4000: rows.append(trainer.step())
    final = tmp_path/"final.pt"; trainer.save(final)
    # detail uses CUDA peak accounting in production; this CPU fixture provides
    # equivalent saved-state metadata without claiming a CUDA measurement.
    saved = torch.load(final, map_location="cpu", weights_only=False)
    record = dict(checkpoint=str(final), checkpoint_sha256=sha256(final), binding=saved["pilot_binding"],
        additional_supervised_tokens=saved["supervised_tokens"], additional_input_tokens=saved["tokens"],
        physical_input_tokens=sum(saved["sampler"]["source_physical_tokens"].values()), update=saved["update"],
        tokens=saved["tokens"], supervised_tokens=saved["supervised_tokens"], sampler=saved["sampler"],
        genre_teachers=saved["sampler"]["genre_teachers"], genre_eos=saved["sampler"]["genre_eos"],
        measured_stage_teachers=2000, training_step_seconds=sum(r["seconds"] for r in rows))
    recipe = dict(target_teachers=4000, parent=dict(sha256=sha256(path)))
    audit_extension(record, rows, parent, recipe, dict(peak_lr=.002))
    assert rows[0]["update"] == parent["update"]+1 > 1
    changed = [dict(row) for row in rows]; changed[0]["lr"] = .001
    with pytest.raises(AssertionError): audit_extension(record, changed, parent, recipe, dict(peak_lr=.002))
    with pytest.raises(AssertionError): audit_extension(dict(record, measured_stage_teachers=4000), rows, parent, recipe, dict(peak_lr=.002))
    with pytest.raises(AssertionError): audit_extension(record, rows[1:], parent, recipe, dict(peak_lr=.002))


def test_live_or_unfinished_review_cannot_publish_acceptance(tmp_path):
    from phase6_performance import identity
    run = tmp_path/"run"; run.mkdir()
    config = tmp_path/"config.json"; write_json(config, dict(output=str(run)))
    for job in (dict(status="running"), dict(status="complete", **identity())):
        write_json(run/"job.json", job)
        with pytest.raises(ValueError, match="actually finish"): review(config, tmp_path/"nonexistent-notes.json")
    assert not (run/"review.json").exists() and not (run/"annotations.json").exists()
