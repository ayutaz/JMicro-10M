import json

import pytest
from jsonschema import ValidationError

from jmicro.experiment import ROOT, prepare_run, read_json, validate_record, verify_run, write_json


def test_preparation_run_freezes_actual_source_and_can_be_verified(tmp_path):
    run = prepare_run("foundation", output_root=tmp_path)
    record = read_json(run / "experiment.json")
    assert record["kind"] == "preparation" and record["status"] == "prepared"
    assert record["counters"]["tokens_seen"] == 0
    assert record["inputs"]["tokenizer_artifact"] is None
    assert record["inputs"]["dataset_manifest"] is None
    assert (run / "source/uv.lock").read_bytes() == (ROOT / "uv.lock").read_bytes()
    assert verify_run(run)["verified"]
    ledger = [json.loads(x) for x in (tmp_path / "experiments.jsonl").read_text().splitlines()]
    assert len(ledger) == 1 and ledger[0]["run_id"] == record["run_id"]


def test_changed_frozen_source_is_detected(tmp_path):
    run = prepare_run("tamper", output_root=tmp_path)
    target = run / "source/src/jmicro/evaluation.py"
    target.write_bytes(target.read_bytes() + b"\n# changed\n")
    with pytest.raises(ValueError, match="Source checksum mismatch"):
        verify_run(run)


def test_changed_experiment_record_is_detected_even_if_schema_valid(tmp_path):
    run = prepare_run("tamper-record", output_root=tmp_path)
    record = read_json(run / "experiment.json")
    record["seed"] = 999
    write_json(run / "experiment.json", record)
    with pytest.raises(ValueError, match="differs from ledger"):
        verify_run(run)


def test_preparation_cannot_be_reported_as_training(tmp_path):
    run = prepare_run("honest-status", output_root=tmp_path)
    record = read_json(run / "experiment.json")
    record["counters"]["tokens_seen"] = 100_000_000
    with pytest.raises(ValidationError):
        validate_record(record)


def test_artifact_inputs_are_snapshotted_with_real_hashes(tmp_path):
    manifest = tmp_path / "manifest.json"
    manifest.write_text('{"purpose":"test_fixture"}\n')
    run = prepare_run("with-input", output_root=tmp_path, dataset_manifest=manifest)
    record = read_json(run / "experiment.json")
    ref = record["inputs"]["dataset_manifest"]
    assert (run / ref["path"]).read_bytes() == manifest.read_bytes()
    assert verify_run(run)["verified"]


def test_artifact_path_cannot_escape_run(tmp_path):
    run = prepare_run("no-traversal", output_root=tmp_path)
    record = read_json(run / "experiment.json")
    record["artifacts"]["environment"]["path"] = "../outside.json"
    write_json(run / "experiment.json", record)
    with pytest.raises((ValidationError, ValueError)):
        verify_run(run)


def test_failed_preparation_leaves_no_ledger_entry(tmp_path):
    with pytest.raises(FileNotFoundError):
        prepare_run("missing-input", output_root=tmp_path, dataset_manifest=tmp_path / "missing.json")
    assert not list(tmp_path.glob("p0-*"))
    assert not (tmp_path / "experiments.jsonl").exists()


@pytest.mark.parametrize("name", ["../escape", "Hello", "", "a/b"])
def test_invalid_run_names_are_rejected(name, tmp_path):
    with pytest.raises(ValueError):
        prepare_run(name, output_root=tmp_path)
