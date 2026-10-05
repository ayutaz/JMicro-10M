"""Protocol fixtures only: none of these scores are learned Chat quality evidence."""
import copy
import sys
from types import SimpleNamespace

import pytest
import torch
from jmicro.chat_evaluation import generate_reply, rollout_dialogue, summarize_chat
from jmicro.chat_review import review_items, notes_template, content_review, paired_chat_comparison
from jmicro.experiment import ROOT
from jmicro.tokenizer import Tokenizer

sys.path.insert(0, str(ROOT/"scripts"))
from evaluate_chat_sft import load_dev


class ReplyFixture(torch.nn.Module):
    def __init__(self, tokenizer):
        super().__init__()
        self.config = dict(max_position_embeddings=1024)
        self.ids = [*tokenizer.encode("そうですね。"), 7]

    def forward(self, x, cache=None, use_cache=True):
        index = 0 if cache is None else cache
        logits = torch.full((1, x.shape[1], 4096), -100.)
        logits[0, -1, self.ids[index]] = 100.
        return SimpleNamespace(logits=logits, cache=index+1)


@pytest.fixture(scope="module")
def evaluation_fixture():
    tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    cases, contexts = load_dev(tok, 1024)
    model = ReplyFixture(tok)
    outputs = {}
    for suppressed in (True, False):
        mode = "suppressed" if suppressed else "unsuppressed"
        for c in cases:
            r = generate_reply(model, tok, c["messages"], max_new=64, suppressed=suppressed)
            r.update({k: c[k] for k in ("id", "family_id", "category", "split", "checks", "messages")})
            r["history_mode"] = "provided_assistant_history"
            outputs[mode+"-"+c["id"]] = r
    rollouts = {c["id"]: rollout_dialogue(model, tok, c, max_new=64) for c in contexts}
    ev = dict(status="mechanical_evaluation_complete_pending_all_content_judgments",
        binding=dict(decoding="greedy", max_new_tokens=64, scored_split="dev", protected_test_used=False),
        outputs=outputs, rollouts=rollouts, evaluation_RNG_isolated=True, protected_test_used=False,
        Chat_adopted=False, requested_five_steps_complete=False)
    for name, rows in (("primary", [outputs["suppressed-"+c["id"]] for c in cases]),
                       ("role_control", [outputs["unsuppressed-"+c["id"]] for c in cases]),
                       ("own_history_final24", [r["replies"][-1] for r in rollouts.values()]),
                       ("own_history_all_turns", [row for r in rollouts.values() for row in r["replies"]])):
        ev[name] = summarize_chat(rows)
    return tok, cases, ev


def judgments(items):
    notes = notes_template("fixture-raw-sha", items)
    notes["reviewer"]["identity"] = "protocol fixture, not a human review"
    for n in notes["judgments"]:
        n.update(grammar=2, relevance=2, context=2, rationale="Protocol fixture scores do not certify model quality.")
    return notes


def test_all_rows_reconstruct_actual_own_history_and_report_exact_denominators(evaluation_fixture):
    tok, cases, ev = evaluation_fixture
    items = review_items(ev, cases, tok, 1024)
    assert len(items) == 219
    own_second = next(i for i in items.values() if i["condition"] == "own-history" and i["turn"] == 2)
    assert [m["content"] for m in own_second["messages"] if m["role"] == "assistant"] == ["そうですね。"]
    result = content_review(ev, "fixture-raw-sha", judgments(items), items)
    assert result["summaries"]["primary"]["responses"] == 80
    assert result["summaries"]["own_history_final24"]["responses"] == 24
    assert result["summaries"]["own_history_all_turns"]["responses"] == 59
    assert result["dev_screen_passed"] is True
    assert not result["Chat_adopted"] and not result["independent_human_blind_evidence_verified"]
    assert not result["requested_five_steps_complete"] and result["pending"]


def test_raw_byte_and_gold_history_substitution_and_summary_tampering_rejected(evaluation_fixture):
    tok, cases, ev = evaluation_fixture
    bad = copy.deepcopy(ev)
    next(iter(bad["outputs"].values()))["raw_bytes_hex"] = ""
    with pytest.raises(AssertionError, match="Raw token"):
        review_items(bad, cases, tok, 1024)
    bad = copy.deepcopy(ev)
    context_case = next(c for c in cases if sum(m["role"] == "user" for m in c["messages"]) >= 2)
    second = bad["rollouts"][context_case["id"]]["replies"][1]
    second["prompt_ids"], _ = tok.chat_prompt(context_case["messages"][:3], 960)
    with pytest.raises(AssertionError):
        review_items(bad, cases, tok, 1024)
    bad = copy.deepcopy(ev)
    bad["primary"]["stop"] -= 1
    with pytest.raises(AssertionError, match="mechanical summary"):
        review_items(bad, cases, tok, 1024)


def test_missing_duplicate_boolean_unscored_and_wrong_raw_notes_rejected(evaluation_fixture):
    tok, cases, ev = evaluation_fixture
    items = review_items(ev, cases, tok, 1024)
    base = judgments(items)
    for mutate in (
        lambda n: n["judgments"].pop(),
        lambda n: n["judgments"].append(n["judgments"][0]),
        lambda n: n["judgments"][0].update(grammar=True),
        lambda n: n["judgments"][0].update(context=None),
        lambda n: n.update(evaluation_sha256="other-raw"),
        lambda n: n["reviewer"].update(independent_human=True),
    ):
        bad = copy.deepcopy(base); mutate(bad)
        with pytest.raises(AssertionError):
            content_review(ev, "fixture-raw-sha", bad, items)
    with pytest.raises(AssertionError):
        content_review(ev, "fixture-raw-sha", notes_template("fixture-raw-sha", items), items)


def test_joint_70_percent_and_family_60_percent_boundaries(evaluation_fixture):
    tok, cases, ev = evaluation_fixture
    items = review_items(ev, cases, tok, 1024)
    notes = judgments(items)
    primary = [n for n in notes["judgments"] if items[n["key"]]["condition"] == "suppressed"]
    final = [n for n in notes["judgments"] if items[n["key"]].get("final_turn")]
    for n in primary[56:]: n["grammar"] = 1
    for n in final[15:]: n["context"] = 1
    result = content_review(ev, "fixture-raw-sha", notes, items)
    assert result["dev_screen_passed"]
    assert result["summaries"]["primary"]["joint_grammar_relevance_score2"] == 56
    assert result["summaries"]["own_history_final24"]["context_score2"] == 15
    primary[55]["relevance"] = 1
    final[14]["context"] = 1
    result = content_review(ev, "fixture-raw-sha", notes, items)
    assert not any(result["content_checks"].values()) and not result["dev_screen_passed"]


def test_unfinished_or_live_evaluation_cannot_be_reviewed(tmp_path, monkeypatch):
    import review_chat_sft
    monkeypatch.setattr(review_chat_sft, "ROOT", tmp_path)
    run = tmp_path/"reports/phase7/fixture"; run.mkdir(parents=True)
    path = run/"result.json"
    from jmicro.experiment import write_json
    write_json(run/"job.json", dict(status="starting"))
    with pytest.raises(ValueError, match="actually finish"):
        review_chat_sft.load_evaluation(path, tmp_path/"tokenizer")
    write_json(run/"job.json", dict(status="complete"))
    monkeypatch.setattr(review_chat_sft, "alive", lambda _: True)
    with pytest.raises(ValueError, match="actually finish"):
        review_chat_sft.load_evaluation(path, tmp_path/"tokenizer")


def test_paired_ablation_preserves_family_units_and_rejects_protocol_changes(evaluation_fixture):
    tok, cases, original = evaluation_fixture
    ev = copy.deepcopy(original)
    ev["binding"].update(tokenizer_sha256="fixture-tok", suite_sha256="fixture-suite", model_context=1024,
        dtype="fp32", backend="math", evaluation_seed=42, source_sha256={}, implementation={}, protocol="fixture")
    items = review_items(ev, cases, tok, 1024)
    left_notes, right_notes = judgments(items), judgments(items)
    first = next(n for n in left_notes["judgments"] if n["key"].startswith("suppressed-"))
    first["relevance"] = 1
    left = content_review(ev, "fixture-raw-sha", left_notes, items)
    right = content_review(ev, "fixture-raw-sha", right_notes, items)
    report = paired_chat_comparison(ev, ev, items, items, left, right)
    delta = report["paired"]["primary"]["joint_grammar_relevance"]
    assert delta["units"] == delta["examples"] == 80 and delta["point"] == pytest.approx(1/80)
    assert report["paired"]["own_history_final24"]["context_score2"]["units"] == 24
    assert not report["Chat_adopted"] and not report["requested_five_steps_complete"]
    bad = copy.deepcopy(ev); bad["binding"]["evaluation_seed"] = 43
    with pytest.raises(AssertionError):
        paired_chat_comparison(ev, bad, items, items, left, right)


def test_same_sft_proposal_is_not_enough_when_actual_exposure_or_batch_differs():
    from review_chat_ablation import validate_matched_sft
    root = dict(path="fixture-base", sha256="fixture-root")
    recipe = dict(route="direct-sft", parent=root, spec=dict(batch=32, seed=42), series_budget=10000000,
        dialogue_binding="fixture-dialogues", train_records={}, data_manifest_sha256="fixture-data", tokenizer={},
        implementation={}, source_sha256={})
    main_recipe = dict(copy.deepcopy(recipe), route="midtraining-sft", parent=dict(path="fixture-mid", sha256="fixture-mid"), adopted_Base=root)
    exposure = dict(actual_series_tokens=10000001, Assistant_teacher_tokens=633185, valid_input_tokens=9000000,
                    physical_tokens=12000000, EOT_teachers=40366, full_sampler=dict(position=100))
    direct, main = (recipe, exposure), (main_recipe, copy.deepcopy(exposure))
    validate_matched_sft(direct, main)
    main[1]["Assistant_teacher_tokens"] += 1
    with pytest.raises(AssertionError, match="actual SFT"):
        validate_matched_sft(direct, main)
    main[1]["Assistant_teacher_tokens"] -= 1
    main[0]["spec"]["batch"] = 16
    with pytest.raises(AssertionError, match="Match SFT"):
        validate_matched_sft(direct, main)
