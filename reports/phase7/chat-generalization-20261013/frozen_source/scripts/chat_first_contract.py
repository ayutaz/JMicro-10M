"""Explicitly unadopted-parent diagnostic contract; no adoption gate changes."""
import json
import math
from pathlib import Path
import torch
from jmicro.chat_training import AssistantBudgetSampler
from jmicro.experiment import ROOT, read_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.model import JMicroModel
from jmicro.training import implementation_hashes
from phase6_performance import alive, finite_state
from chat_batch_evidence import require_batch_evidence

PARENT_SHA = "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290"
TOKENIZER_SHA = "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318"
MANIFEST_SHA = "1ad9f04c0b7d43c4fc253c7cdc8057e9a09d7ef34b9073e53d972aeef278e0ee"
RUN = ROOT / "reports/phase7/chat-first-sft-20261010"


def validate_quantities(manifest, sampler, budget):
    t = manifest["splits"]["train"]
    assert len(sampler.windows) == t["prepared_SFT_windows"] == 40366
    assert sum(len(w["ids"]) for w in sampler.windows) == t["prepared_epoch_series_tokens"] == 10189157
    assert sum(int((w["labels"] != -100).sum()) for w in sampler.windows) == t["prepared_epoch_Assistant_teachers"] == 633185
    assert budget == 3 * t["prepared_epoch_series_tokens"] == 30567471
    assert sampler.binding == manifest["dialogue_binding"]


def preflight(config, sources, *, require_batch=True):
    c = read_json(config)
    assert c["purpose"] == "chat_first_diagnostic" and c["route"] == "direct-sft"
    assert c["Base_adopted"] is c["Chat_adopted"] is c["protected_test_used"] is False
    assert c["implementation"] == implementation_hashes()
    assert c["source_sha256"] == {p: sha256(ROOT/p) for p in sources}
    assert c["parent"]["sha256"] == PARENT_SHA == sha256(Path(c["parent"]["path"]))
    assert c["tokenizer"]["sha256"] == TOKENIZER_SHA == sha256(Path(c["tokenizer"]["path"]))
    tok = Tokenizer(Path(c["tokenizer"]["path"]))
    directory = Path(c["data_directory"])
    assert c["data_manifest_sha256"] == MANIFEST_SHA == sha256(directory/"manifest.json")
    manifest = read_json(directory/"manifest.json")
    assert c["train_records"]["sha256"] == manifest["train_records_sha256"] == sha256(Path(c["train_records"]["path"]))
    assert c["dev_records"]["sha256"] == manifest["dev_records_sha256"] == sha256(Path(c["dev_records"]["path"]))
    assert Path(c["train_records"]["path"]).resolve() == (directory/"train.jsonl").resolve()
    with Path(c["train_records"]["path"]).open() as stream:
        records = [json.loads(line) for line in stream]
    assert len(records) == 2688 and all(r["split"] == "train" for r in records)
    sampler = AssistantBudgetSampler(records, tok, c["spec"]["context"], c["spec"]["seed"], c["series_budget"])
    validate_quantities(manifest, sampler, c["series_budget"])
    assert c["dialogue_binding"] == sampler.binding
    for path, digest in c["evaluation_sha256"].items():
        assert sha256(ROOT/path) == digest
    spec = c["spec"]
    assert spec["context"] == 1024 and spec["dtype"] == "bf16" and spec["backend"] == "math"
    assert spec["seed"] == 42 and spec["sampler"] == "document" and spec["accumulation"] == 1
    assert spec["compile"] is spec["training_fast_path"] is False
    assert spec["lr"] == 1e-4 and spec["weight_decay"] == .01
    assert spec["schedule_updates"] == math.ceil(121098/spec["batch"])
    assert spec["warmup"] == max(1, math.ceil(.05*spec["schedule_updates"]))
    assert (ROOT/c["output"]).resolve() == RUN
    assert c["GPU_budget_seconds"] == 4200 and c["training_GPU_budget_seconds"] == 3600 and c["resume_GPU_budget_seconds"] == 600
    if require_batch:
        require_batch_evidence(c, "sft", sampler.binding, "src/jmicro/chat_training.py")
    return c, tok, records


def parent_state(c):
    state = torch.load(c["parent"]["path"], map_location="cpu", weights_only=False)
    assert state["implementation_sha256"] == c["implementation"] and finite_state(state)
    assert not state["spec"].get("assistant_training") and not state["spec"].get("dialogue_midtraining")
    assert state["update"] == 305176
    # state_dict contains both tied embedding/output names; count Parameters once.
    model = JMicroModel(state["model_config"])
    model.load_state_dict(state["model"], strict=True)
    assert sum(p.numel() for p in model.parameters() if p.requires_grad) == 10001152
    return state


def resolve_diagnostic(config, stage):
    from run_chat_first_sft import SOURCES
    c, tok, _ = preflight(config, SOURCES, require_batch=False)
    if stage == "base":
        state, ref = parent_state(c), c["parent"]
    else:
        assert stage in ("epoch1", "epoch2", "epoch3")
        job = read_json(RUN/"job.json")
        assert job["status"] == "complete" and not alive(job)
        result = read_json(RUN/"result.json")
        assert result["config_sha256"] == job["config_sha256"] == sha256(config)
        ref = result["checkpoints"][stage]
        assert sha256(Path(ref["path"])) == ref["sha256"]
        state = torch.load(ref["path"], map_location="cpu", weights_only=False)
        assert state["implementation_sha256"] == c["implementation"] and finite_state(state)
        assert state["lineage"]["base_checkpoint"] == c["parent"]
        assert state["lineage"]["kind"] == "assistant-sft-fresh-optimizer"
        assert state["spec"]["assistant_training"]["data_binding"] == c["dialogue_binding"]
        assert state["spec"]["assistant_training"]["series_budget"] == c["series_budget"]
        assert state["supervised_tokens"] > 0 and state["update"] > 0
        if stage == "epoch3":
            assert state["sampler"]["examples"] == 121098 and state["supervised_tokens"] == 1899555
            assert state["sampler"]["series_tokens"] == 30567471
    assert sha256(Path(ref["path"])) == ref["sha256"]
    return state, tok, dict(purpose="chat_first_diagnostic", Base_adopted=False, Chat_adopted=False,
        config=dict(path=str(config), sha256=sha256(config)), checkpoint=ref, stage=stage)
