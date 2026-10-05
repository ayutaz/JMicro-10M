"""Seeded native CPU protocol fixtures, never GPU or model quality evidence."""
import copy
import sys
from types import SimpleNamespace

import pytest
import torch
from jmicro.chat_evaluation import generate_reply, rollout_dialogue, validate_sampling
from jmicro.chat_review import review_items
from jmicro.experiment import ROOT, write_json
from jmicro.tokenizer import Tokenizer
from test_chat_review import ReplyFixture, evaluation_fixture

sys.path.insert(0, str(ROOT/"scripts"))
from evaluate_chat_stages import evaluation_seeds, summarize_seed


class ChoiceFixture(torch.nn.Module):
    def __init__(self, tokenizer):
        super().__init__(); self.config = dict(max_position_embeddings=256)
        self.choices = [next(i for i, b in tokenizer.id_bytes.items() if b == text) for text in (b"a", b"b")]

    def forward(self, x, cache=None, use_cache=True):
        index = 0 if cache is None else cache
        logits = torch.full((1, x.shape[1], 4096), -100.)
        if index == 8: logits[0, -1, 7] = 100.
        else: logits[0, -1, self.choices] = 100.
        return SimpleNamespace(logits=logits, cache=index+1)


def test_sampling_uses_local_rng_and_reproduces_each_seed_with_raw_eot():
    tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    model = ChoiceFixture(tok); messages = [dict(role="user", content="こんにちは。")]
    sampling = dict(seed=42, temperature=1., top_p=1., top_k=2)
    before = torch.get_rng_state().clone()
    first = generate_reply(model, tok, messages, max_new=64, sampling=sampling)
    assert torch.equal(before, torch.get_rng_state()) and model.training
    again = generate_reply(model, tok, messages, max_new=64, sampling=sampling)
    other = generate_reply(model, tok, messages, max_new=64, sampling=dict(sampling, seed=43))
    assert first["generated_ids"] == again["generated_ids"] != other["generated_ids"]
    assert first["generated_ids"][-1] == 7 and first["stop_reason"] == "eot"
    assert first["raw_bytes_hex"] == first["text"].encode().hex() and first["valid_utf8"]
    assert first["sampling"] == sampling and first["decoding"] == "sampling"
    assert torch.equal(before, torch.get_rng_state())


def test_sampling_filters_leave_eot_available_and_reject_invalid_parameters():
    tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    sampling = dict(seed=42, temperature=.8, top_p=.01, top_k=1)
    row = generate_reply(ChoiceFixture(tok), tok, [dict(role="user", content="猫。")], max_new=64, sampling=sampling)
    assert row["stop_reason"] == "eot" and len(set(row["generated_ids"][:-1])) == 1
    for bad in (dict(sampling, seed=True), dict(sampling, temperature=0), dict(sampling, temperature=float("nan")),
                dict(sampling, top_p=0), dict(sampling, top_k=5000)):
        with pytest.raises(AssertionError): validate_sampling(bad, 4096)


def test_all_sampling_rows_and_own_turn_seeds_use_existing_content_protocol(evaluation_fixture):
    tok, cases, original = evaluation_fixture
    contexts = [c for c in cases if sum(m["role"] == "user" for m in c["messages"]) >= 2]
    sampling = dict(seed=43, temperature=.8, top_p=.9, top_k=50)
    model = ReplyFixture(tok); saved = dict(provided={}, rollouts={})
    for suppressed in (True, False):
        mode = "suppressed" if suppressed else "unsuppressed"
        for case in cases:
            row = generate_reply(model, tok, case["messages"], max_new=64, suppressed=suppressed, sampling=sampling)
            row.update({k: case[k] for k in ("id", "family_id", "category", "split", "checks", "messages")})
            row["history_mode"] = "provided_assistant_history"
            saved["provided"][mode+"-"+case["id"]] = row
    for case in contexts: saved["rollouts"][case["id"]] = rollout_dialogue(model, tok, case, max_new=64, sampling=sampling)
    binding = dict(original["binding"], decoding="sampling", evaluation_seed=43, sampling=sampling)
    evaluation = summarize_seed(saved, cases, contexts, binding)
    items = review_items(evaluation, cases, tok, 1024)
    assert len(items) == 219 and evaluation["own_history_final24"]["outputs"] == 24
    second = next(r["replies"][1] for r in evaluation["rollouts"].values())
    assert second["sampling"]["seed"] == 44
    bad = copy.deepcopy(evaluation)
    next(iter(bad["rollouts"].values()))["replies"][1]["sampling"]["seed"] = 43
    with pytest.raises(AssertionError): review_items(bad, cases, tok, 1024)


def test_multiple_seeds_are_required_and_greedy_comparison_stays_fixed():
    assert evaluation_seeds("sampling", None) == [42, 43, 44]
    assert evaluation_seeds("greedy", None) == [42]
    for seeds in ([42], [42, 42, 43], [-1, 42, 43], list(range(6))):
        with pytest.raises(ValueError): evaluation_seeds("sampling", seeds)
    with pytest.raises(ValueError): evaluation_seeds("greedy", [43])


def test_stage_controls_reject_incomplete_or_live_learning(tmp_path, monkeypatch):
    import chat_stage_evidence
    import run_chat_sft
    monkeypatch.setattr(chat_stage_evidence, "ROOT", tmp_path)
    config = tmp_path/"configs/phase7/fixture.json"; write_json(config, {})
    recipe = dict(route="direct-sft", parent=dict(path="fixture", sha256="fixture"), output="reports/phase7/fixture")
    monkeypatch.setattr(run_chat_sft, "preflight", lambda _: (recipe, None, []))
    job = tmp_path/recipe["output"]/"job.json"; write_json(job, dict(status="starting"))
    with pytest.raises(ValueError, match="actually finish"): chat_stage_evidence.resolve_stage(config, "sft")
    with pytest.raises(ValueError, match="completed mid-training"): chat_stage_evidence.resolve_stage(config, "mid-training")
    write_json(job, dict(status="complete"))
    monkeypatch.setattr(chat_stage_evidence, "alive", lambda _: True)
    with pytest.raises(ValueError, match="actually finish"): chat_stage_evidence.resolve_stage(config, "sft")


def test_seed_leaf_cannot_bypass_unfinished_parent_or_cumulative_budget(tmp_path, monkeypatch):
    import review_chat_sft
    monkeypatch.setattr(review_chat_sft, "ROOT", tmp_path)
    monkeypatch.setattr(review_chat_sft, "alive", lambda _: False)
    parent_path = tmp_path/"reports/phase7/fixture/job.json"
    leaf_path = parent_path.parent/"seed-42/result.json"
    write_json(leaf_path.parent/"job.json", dict(status="complete", parent_job=str(parent_path),
        parent_binding=dict(GPU_budget_seconds=1800.), binding=dict(GPU_budget_seconds=1800., evaluation_seed=42),
        pid=123, boot_id="fixture", start_ticks="1", GPU_elapsed_seconds=1000.))
    write_json(parent_path, dict(status="starting"))
    with pytest.raises(ValueError, match="Whole multi-seed"):
        review_chat_sft.load_evaluation(leaf_path, tmp_path/"tokenizer")
    write_json(parent_path, dict(status="complete", binding=dict(GPU_budget_seconds=1800.),
        pid=123, boot_id="fixture", start_ticks="1", GPU_elapsed_seconds=1801.))
    with pytest.raises(AssertionError):
        review_chat_sft.load_evaluation(leaf_path, tmp_path/"tokenizer")
