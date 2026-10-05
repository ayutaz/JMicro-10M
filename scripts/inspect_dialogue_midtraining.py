"""Inspect prepared train dialogue windows; no model or GPU is constructed."""
from functools import lru_cache
import json
from pathlib import Path
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.dialogue_training import DialogueWindows
from jmicro.experiment import ROOT, read_json, sha256, write_json, now
from jmicro.tokenizer import Tokenizer
from phase6_performance import identity
from prepare_chat_pilot import DATA


def inspect():
    started = time.perf_counter(); manifest = read_json(DATA/"manifest.json")
    assert sha256(DATA/"train.jsonl") == manifest["train_records_sha256"]
    assert sha256(ROOT/"artifacts/phase2/4096/tokenizer.model") == manifest["tokenizer_sha256"]
    with (DATA/"train.jsonl").open() as stream: records = [json.loads(line) for line in stream]
    tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    tok.encode = lru_cache(maxsize=100000)(tok.encode)
    prepared = DialogueWindows(records, tok, 1024, 42)
    per_dialogue = {}
    kinds = dict(user=0, assistant=0, system=0, role=0, EOT=0)
    for window in prepared.windows:
        per_dialogue.setdefault(window["doc_id"], []).extend(int(i) for i in window["labels"] if i != -100)
        for kind in window["kinds"]:
            if kind != "context": kinds[kind] += 1
    for record in records:
        ids,_ = tok.dialogue(json.loads(record["messages_json"]))
        assert per_dialogue[record["doc_id"]] == ids[1:]
    series = sum(len(w["ids"]) for w in prepared.windows)
    teachers = sum(kinds.values())
    assert kinds["assistant"]+manifest["splits"]["train"]["source_Assistant_responses"] == manifest["splits"]["train"]["prepared_epoch_Assistant_teachers"]
    report = dict(status="train_dialogue_midtraining_windows_prepared_only", **identity(), dialogues=len(records),
        windows=len(prepared.windows), dialogue_binding=prepared.binding,
        series_tokens=series, valid_input_tokens=series-len(prepared.windows), teacher_tokens=teachers,
        teacher_kinds=kinds, physical_capacity_inputs=len(prepared.windows)*1024,
        every_source_message_taught_once=True, complete_pairs_not_cut=True,
        source_dialogues_with_trailing_user=sum(json.loads(r["messages_json"])[-1]["role"] == "user" for r in records),
        trailing_user_policy="Preserve source user/EOT; no assistant reply invented",
        source_manifest_sha256=sha256(DATA/"manifest.json"), train_records_sha256=manifest["train_records_sha256"],
        implementation_sha256=sha256(ROOT/"src/jmicro/dialogue_training.py"), inspector_sha256=sha256(Path(__file__)),
        CPU_seconds=time.perf_counter()-started, GPU_learning_tokens=0, Base_adopted=False, Chat_adopted=False,
        requested_five_steps_complete=False, protected_test_used=False,
        limitations="Train-only preparation; source facts/independent human quality not certified; replay mixture/budgets require a future frozen recipe", created_at=now())
    write_json(ROOT/"reports/phase7/dialogue_midtraining_preparation.json", report)
    print(json.dumps(report, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3,12,7); inspect()
