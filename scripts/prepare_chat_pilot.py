"""Reuse the hash-pinned dialogue pilot, preserving whole-family train/dev splits."""
import argparse
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import numpy as np
from jmicro.assistant_sampler import AssistantSampler
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import identity,alive

PIN = "0b1042979bf32899e24da30790e3ae6b239013c3"
PUBLIC_MANIFEST_SHA = "8072bd218be26637a51c7c11540f1c8c636392c3b1a91f805a5e317e6ca55a09"
DATA = Path("/home/aihub_ubuntu/jmicro-data/phase7/real-persona-pilot-20261006")
RUN = ROOT/"reports/phase7/chat-pilot-20261006"


def windows_summary(records,tokenizer,windows):
    messages = [json.loads(r["messages_json"]) for r in records]
    assistant = [m for dialogue in messages for m in dialogue if m["role"] == "assistant"]
    teacher_tokens = sum(len(tokenizer.encode(m["text"]))+1 for m in assistant)
    selected = [w["labels"][w["labels"] != -100] for w in windows]
    assert len(windows) == len(assistant) and sum(len(ids) for ids in selected) == teacher_tokens
    assert all(ids[-1] == 7 and np.count_nonzero(ids == 7) == 1 and np.all(ids[:-1] >= 8) for ids in selected)
    series = sum(len(w["ids"]) for w in windows)
    return dict(dialogues=len(records),source_body_utf8_bytes=sum(len(r["text"].encode()) for r in records),
        source_messages=sum(len(m) for m in messages),source_Assistant_responses=len(assistant),
        source_message_body_tokens=sum(len(tokenizer.encode(m["text"])) for dialogue in messages for m in dialogue),
        source_serialized_dialogue_tokens=sum(len(tokenizer.dialogue(m)[0]) for m in messages),
        source_Assistant_body_utf8_bytes=sum(len(m["text"].encode()) for m in assistant),
        prepared_SFT_windows=len(windows),prepared_epoch_series_tokens=series,
        prepared_epoch_input_tokens=series-len(windows),prepared_epoch_Assistant_teachers=teacher_tokens,
        prepared_epoch_EOT_teachers=len(windows),prepared_window_capacity_inputs=len(windows)*1024,
        prepared_windows_with_history_trim=sum(w["removed_turns"] > 0 for w in windows),
        prepared_removed_complete_turns=sum(w["removed_turns"] for w in windows),
        Assistant_teacher_length_min=min(len(ids) for ids in selected),Assistant_teacher_length_max=max(len(ids) for ids in selected),
        prepared_not_consumed=True)


def prepare():
    RUN.mkdir(parents=True,exist_ok=True);job_path = RUN/"prepare-job.json"
    previous = read_json(job_path) if job_path.exists() else {}
    if previous and alive(previous): raise ValueError("Existing preparation process is still live")
    public = ROOT/"artifacts/hub-downloads"/PIN/"artifact_manifest.json"
    assert sha256(public) == PUBLIC_MANIFEST_SHA
    files = read_json(public)["files"]
    input_paths = ("data/phase1/processed/corpus.jsonl","data/phase1/processed/split_manifest.json","artifacts/phase2/4096/tokenizer.model")
    inputs = {p:sha256(ROOT/p) for p in input_paths}
    assert all(inputs[p] == files[p]["sha256"] for p in input_paths)
    split_manifest = read_json(ROOT/input_paths[1])
    assert inputs[input_paths[0]] == split_manifest["corpus_sha256"]
    assert all(sha256(ROOT/p) == expected for p,expected in split_manifest["inputs"]["fixed_suite_sha256"].items())
    builder_sha = sha256(Path(__file__))
    manifest_path = DATA/"manifest.json"
    if manifest_path.exists():
        kept = read_json(manifest_path)
        assert kept["input_sha256"] == inputs and kept["builder_sha256"] == builder_sha
        assert all(sha256(DATA/(split+".jsonl")) == kept[split+"_records_sha256"] for split in ("train","dev"))
        print("Pinned prepared Chat pilot retained; no GPU started");return
    started = time.monotonic();job = dict(status="running",**identity(),started_at=now(),builder_sha256=builder_sha,input_sha256=inputs)
    atomic_json(job_path,job)
    try:
        records = dict(train=[],dev=[]);membership = {s:set(split_manifest["splits"][s]) for s in records}
        clusters,canonical = {},{}
        with (ROOT/input_paths[0]).open() as stream:
            for line in stream:
                row = json.loads(line)
                if row["kind"] != "dialogue" or row["split"] not in records: continue
                # Never select/window/tokenize/score protected source test rows.
                split = row["split"];assert row["doc_id"] in membership[split]
                assert row["doc_id"].startswith("real_persona_chat:") and row["bucket"] == "sharealike"
                messages = json.loads(row["messages_json"])
                assert [m["role"] for m in messages] == ["user" if i%2 == 0 else "assistant" for i in range(len(messages))]
                assert "\n".join(m["text"] for m in messages) == row["text"]
                assert hashlib.sha256(row["text"].encode()).hexdigest() == row["canonical_sha256"]
                family = split_manifest["cluster_by_doc"][row["doc_id"]]
                assert clusters.setdefault(family,split) == split
                assert canonical.setdefault(row["canonical_sha256"],split) == split
                records[split].append(dict(row,cluster_id=family,source="real_persona_chat",
                    revision="28d0b6b3865b29cabc26c230a2db37cdf315e937",license="CC-BY-SA-4.0"))
        assert all(records.values()) and not ({r["doc_id"] for r in records["train"]}&{r["doc_id"] for r in records["dev"]})
        tokenizer = Tokenizer(ROOT/input_paths[2])
        # Preparation-only memoization avoids encoding old history repeatedly;
        # the pinned tokenizer implementation and emitted IDs are unchanged.
        tokenizer.encode = lru_cache(maxsize=100000)(tokenizer.encode)
        train = AssistantSampler(records["train"],tokenizer,1024,42)
        summaries = dict(train=windows_summary(records["train"],tokenizer,train.windows))
        dev_windows = []
        for record in records["dev"]:
            for w in tokenizer.sft_windows(json.loads(record["messages_json"]),context=1025):
                dev_windows.append(dict(ids=np.asarray(w["input_ids"]),labels=np.asarray(w["labels"]),removed_turns=w["removed_turns"]))
        summaries["dev"] = windows_summary(records["dev"],tokenizer,dev_windows)
        DATA.mkdir(parents=True,exist_ok=True)
        outputs = {}
        for split,rows in records.items():
            target = DATA/(split+".jsonl")
            with target.open("w",encoding="utf-8") as stream:
                for row in rows: stream.write(json.dumps(row,ensure_ascii=False,separators=(",",":"))+"\n")
            outputs[split+"_records_sha256"] = sha256(target)
        samples = sorted(records["train"],key=lambda r:hashlib.sha256(("42:chat-pilot-content:"+r["doc_id"]).encode()).hexdigest())[:4]
        atomic_json(DATA/"sample4.json",dict(selection="Fixed four train conversations, unchanged bodies; no model or independent human quality claim",records=samples))
        manifest = dict(version=1,vocab_size=4096,context=1024,seed=42,input_sha256=inputs,builder_sha256=builder_sha,
            tokenizer_wrapper_sha256=sha256(ROOT/"src/jmicro/tokenizer.py"),assistant_sampler_sha256=sha256(ROOT/"src/jmicro/assistant_sampler.py"),
            tokenizer_sha256=inputs[input_paths[2]],dialogue_binding=train.binding,**outputs,splits=summaries,
            public_pilot=dict(repository="japanese-data-analyze/japanese-tiny-llm-10m-artifacts",revision=PIN,manifest_sha256=PUBLIC_MANIFEST_SHA),
            source=dict(repository="nu-dialogue/real-persona-chat",revision="28d0b6b3865b29cabc26c230a2db37cdf315e937",license="CC-BY-SA-4.0",
                attribution="Yamashita et al., RealPersonaChat (2023); nu-dialogue/real-persona-chat",raw_archive_sha256="2fb4fe5c16e6722a0840fe6924113965cffe0b6b9957e436fdb3886fae2743dc"),
            split_policy="Retain original whole-dialogue/connected-family train/dev split; protected test not selected or tokenized; shared speakers may recur",
            supervision="One Assistant body plus EOT per target, old complete turns trimmed only for context fit; no user/system/role/PAD labels",
            quantity_policy="Source dialogue tokens count each original conversation once; prepared SFT window series repeats history. Neither is actual learned tokens or global unique-token union",
            source_history="Pilot body/splits reused unchanged; no new source acquisition, global-near re-audit or persona metadata restoration",
            limitations="Real human casual conversations, not instruction-following or factual-grounding certification; source utterance repetition is preserved",
            sample_sha256=sha256(DATA/"sample4.json"),CPU_prepare_seconds=time.monotonic()-started,Chat_GPU_teacher_tokens=0,
            Base_adopted=False,Chat_adopted=False,protected_test_used=False,requested_five_steps_complete=False,created_at=now())
        atomic_json(manifest_path,manifest);atomic_json(RUN/"preparation.json",manifest)
        job.update(status="complete",completed_at=now(),CPU_seconds=time.monotonic()-started,manifest_sha256=sha256(manifest_path))
        print(json.dumps(dict(status="prepared_only",directory=str(DATA),splits=summaries,CPU_seconds=job["CPU_seconds"],Chat_GPU_teacher_tokens=0),ensure_ascii=False),flush=True)
    except BaseException as error: job.update(status="failed",error=repr(error));raise
    finally: atomic_json(job_path,job)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3,12,7)
    parser = argparse.ArgumentParser();parser.parse_args();prepare()
