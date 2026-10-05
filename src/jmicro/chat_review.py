"""Raw-bound Chat content judgments; mechanical success is not content quality.

All provided/control responses and every own-history turn must be reviewed.
The context target uses 24 dialogue families, not 59 independent turns.
Passing this development screen never adopts a Chat checkpoint.
"""
from collections import Counter
import re

from jmicro.chat_evaluation import decode_reply, summarize_chat, validate_sampling
from jmicro.japanese_evaluation import repetition_metrics
from jmicro.tokenizer import SUPPRESS_IDS


RUBRIC = {
    "grammar": "0: unreadable/broken; 1: understandable with awkward or incomplete clauses; 2: natural complete Japanese. Score language separately from factual correctness.",
    "relevance": "0: unrelated/contradicts the request; 1: partly relevant or vague; 2: directly responds to the final User in the actual history. Do not require literal gold wording.",
    "context": "0: loses or contradicts required conditions; 1: partial/ambiguous retention; 2: retains all relevant conditions and corrections in the actual history. For own-history use generated replies, never supplied gold Assistant messages.",
    "rationale": "At least 12 characters explaining the particular response. Keep fantasy, alternate natural answers, numeric correctness, grammar, and stopping distinct.",
}


def validate_reply(row, tokenizer, messages, context, suppressed, sampling=None):
    ids = row["generated_ids"]
    assert isinstance(ids, list) and 0 < len(ids) <= 64
    assert all(type(i) is int and 0 <= i < tokenizer.vocab_size for i in ids)
    assert not any(i in (3, 7) for i in ids[:-1]), "Generation continued after a terminal token"
    reason = "eot" if ids[-1] == 7 else "eos" if ids[-1] == 3 else "max_new_tokens"
    assert row["stop_reason"] == reason and (reason != "max_new_tokens" or len(ids) == 64)
    assert row["generated_tokens"] == len(ids) and row["max_new_tokens"] == 64
    assert row["decoding"] == ("greedy" if sampling is None else "sampling") and row["suppressed"] is suppressed
    if sampling is not None:
        validate_sampling(sampling, tokenizer.vocab_size)
        assert row["sampling"] == sampling
    assert row["suppressed_ids"] == (list(SUPPRESS_IDS) if suppressed else [])
    if suppressed:
        assert not any(i in SUPPRESS_IDS for i in ids)
    decoded = decode_reply(tokenizer, ids)
    assert all(row[k] == v for k, v in decoded.items()), "Raw token IDs/bytes/text disagree"
    assert row["empty_response"] is (not decoded["text"].strip())
    assert row["role_leak"] is any(i in (4, 5, 6) for i in ids)
    assert row["unexpected_special"] is any(i in (0, 1, 2, 4, 5, 6) for i in ids)
    prompt, removed = tokenizer.chat_prompt(messages, context - 64)
    assert removed == row["removed_turns"] == 0 and row["full_history_retained"] is True
    assert row["prompt_ids"] == prompt and row["prompt_tokens"] == len(prompt)
    assert row["user_turns"] == sum(m["role"] == "user" for m in messages)
    assert row["repetition"] is bool(re.search(r"(.{2,}?)\1\1", row["text"], re.DOTALL))
    metrics = repetition_metrics(dict(row, stop_reason="stop_id" if reason in ("eot", "eos") else reason))
    assert row["repeat_metrics"] == {k: metrics[k] for k in (
        "char_4gram_repeat", "token_4gram_repeat", "same_sentence_reappears", "first_adjacent_triple_repeat_char")}


def review_items(evaluation, cases, tokenizer, context):
    """Rebuild actual histories and validate every raw row before showing/scoring it."""
    assert len(cases) == 80 and len({c["id"] for c in cases}) == 80
    assert len({c["family_id"] for c in cases}) == 80
    assert all(c["split"] == "dev" for c in cases)
    binding = evaluation["binding"]
    assert binding["decoding"] in ("greedy", "sampling") and binding["max_new_tokens"] == 64
    sampling = binding.get("sampling") if binding["decoding"] == "sampling" else None
    if binding["decoding"] == "sampling":
        validate_sampling(sampling, tokenizer.vocab_size)
        assert sampling["seed"] == binding["evaluation_seed"]
    assert binding["scored_split"] == "dev" and binding["protected_test_used"] is False
    assert evaluation["evaluation_RNG_isolated"] is True and evaluation["protected_test_used"] is False
    assert evaluation["Chat_adopted"] is False and evaluation["requested_five_steps_complete"] is False
    assert evaluation["status"] == "mechanical_evaluation_complete_pending_all_content_judgments"
    assert context > 64
    provided = evaluation["outputs"]
    assert set(provided) == {mode + "-" + c["id"] for mode in ("suppressed", "unsuppressed") for c in cases}
    items = {}
    groups = {}
    for mode, suppressed in (("suppressed", True), ("unsuppressed", False)):
        rows = []
        for case in cases:
            key = mode + "-" + case["id"]
            row = provided[key]
            assert all(row[k] == case[k] for k in ("id", "family_id", "category", "split", "checks", "messages"))
            assert row["history_mode"] == "provided_assistant_history"
            validate_reply(row, tokenizer, case["messages"], context, suppressed, sampling)
            items[key] = dict(key=key, id=case["id"], family_id=case["family_id"], category=case["category"],
                condition=mode, messages=case["messages"], checks=case["checks"], response=row)
            rows.append(row)
        groups[mode] = rows
    contexts = [c for c in cases if 2 <= sum(m["role"] == "user" for m in c["messages"]) <= 4]
    assert len(contexts) == 24 and set(evaluation["rollouts"]) == {c["id"] for c in contexts}
    all_turns, final_turns = [], []
    for case in contexts:
        rollout = evaluation["rollouts"][case["id"]]
        assert all(rollout[k] == case[k] for k in ("id", "family_id", "category", "split", "checks"))
        assert rollout["full_history_retained"] is True
        users = [m for m in case["messages"] if m["role"] == "user"]
        assert len(rollout["replies"]) == rollout["user_turns"] == len(users)
        history = [dict(case["messages"][0])] if case["messages"][0]["role"] == "system" else []
        for turn, (user, row) in enumerate(zip(users, rollout["replies"], strict=True), 1):
            history.append(dict(user))
            assert row["id"] == case["id"] and row["turn"] == turn
            assert row["history_mode"] == "model_generated_assistant_history"
            turn_sampling = None if sampling is None else dict(sampling, seed=sampling["seed"]+turn-1)
            validate_reply(row, tokenizer, history, context, True, turn_sampling)
            key = f"own-{case['id']}-turn-{turn}"
            items[key] = dict(key=key, id=case["id"], family_id=case["family_id"], category=case["category"],
                condition="own-history", turn=turn, final_turn=turn == len(users), messages=[dict(m) for m in history],
                checks=case["checks"] if turn == len(users) else [], response=row)
            history.append(dict(role="assistant", content=row["text"]))
            all_turns.append(row)
        final_turns.append(rollout["replies"][-1])
    assert len(all_turns) == 59 and len(items) == 219
    for name, rows in (("primary", groups["suppressed"]), ("role_control", groups["unsuppressed"]),
                       ("own_history_final24", final_turns), ("own_history_all_turns", all_turns)):
        assert evaluation[name] == summarize_chat(rows), "Stored mechanical summary differs from raw outputs"
    return items


def notes_template(evaluation_sha256, items):
    return dict(evaluation_sha256=evaluation_sha256, rubric=RUBRIC,
        reviewer=dict(kind="codex_nonblind", identity=None, independent_human=False, blind=False),
        judgments=[dict(key=key, grammar=None, relevance=None, context=None, rationale="") for key in items],
        pending_all_content_judgments=True)


def summarize_content(items, judgments):
    count = len(items)
    assert count
    joint = sum(judgments[i["key"]]["grammar"] == judgments[i["key"]]["relevance"] == 2 for i in items)
    return dict(responses=count, grammar_score2=sum(judgments[i["key"]]["grammar"] == 2 for i in items),
        relevance_score2=sum(judgments[i["key"]]["relevance"] == 2 for i in items),
        context_score2=sum(judgments[i["key"]]["context"] == 2 for i in items),
        joint_grammar_relevance_score2=joint, joint_grammar_relevance_fraction=joint/count,
        response_characters=dict(sorted(Counter(len(i["response"]["text"]) for i in items).items())))


def content_review(evaluation, evaluation_sha256, notes, items):
    assert notes["evaluation_sha256"] == evaluation_sha256, "Notes belong to different raw evaluation"
    assert notes["rubric"] == RUBRIC
    reviewer = notes["reviewer"]
    assert reviewer["kind"] in ("codex_nonblind", "human_nonblind", "human_blind")
    assert isinstance(reviewer["identity"], str) and reviewer["identity"].strip()
    assert type(reviewer["independent_human"]) is bool and type(reviewer["blind"]) is bool
    if reviewer["kind"] == "codex_nonblind":
        assert reviewer["independent_human"] is False and reviewer["blind"] is False
    if reviewer["kind"] == "human_nonblind":
        assert reviewer["blind"] is False
    if reviewer["kind"] == "human_blind":
        assert reviewer["blind"] is True and reviewer["independent_human"] is True
    rows = notes["judgments"]
    scores = {r["key"]: r for r in rows}
    assert len(rows) == len(scores) == len(items) and set(scores) == set(items), "All 219 judgments required, no duplicates"
    assert all(all(type(r[k]) is int and r[k] in (0, 1, 2) for k in ("grammar", "relevance", "context"))
               and isinstance(r["rationale"], str) and len(r["rationale"].strip()) >= 12 for r in rows)
    primary = [i for i in items.values() if i["condition"] == "suppressed"]
    control = [i for i in items.values() if i["condition"] == "unsuppressed"]
    own = [i for i in items.values() if i["condition"] == "own-history"]
    final = [i for i in own if i["final_turn"]]
    assert len(primary) == len(control) == 80 and len(final) == 24 and len(own) == 59
    summaries = {k: summarize_content(v, scores) for k, v in (
        ("primary", primary), ("role_control", control), ("own_history_final24", final), ("own_history_all_turns", own))}
    content_checks = dict(joint_grammar_relevance_at_least70=summaries["primary"]["joint_grammar_relevance_score2"]*10 >= 80*7,
                          own_history_context_at_least60=summaries["own_history_final24"]["context_score2"]*10 >= 24*6)
    mechanical = {name: evaluation[name]["mechanical_checks_only"] for name in ("primary", "own_history_all_turns")}
    family_rows = []
    for i in final:
        turns = [t for t in own if t["family_id"] == i["family_id"]]
        family_rows.append(dict(id=i["id"], family_id=i["family_id"], turns=len(turns), final_context=scores[i["key"]]["context"],
            prior_content_weak_turns=[t["turn"] for t in turns[:-1] if any(scores[t["key"]][k] < 2 for k in ("grammar", "relevance", "context"))],
            prior_mechanical_failed_turns=[t["turn"] for t in turns[:-1] if not t["response"]["valid_utf8"] or t["response"]["empty_response"]
                or t["response"]["role_leak"] or t["response"]["stop_reason"] == "max_new_tokens"]))
    categories = {condition: {category: summarize_content([i for i in group if i["category"] == category], scores)
        for category in sorted({i["category"] for i in group})} for condition, group in (
            ("primary", primary), ("role_control", control), ("own_history_final24", final))}
    return dict(status="all_content_review_complete_pending_final_Chat_evidence", evaluation_sha256=evaluation_sha256,
        reviewer=reviewer, rubric=RUBRIC, summaries=summaries, categories=categories, own_history_families=family_rows,
        content_checks=content_checks, mechanical_checks=mechanical,
        dev_screen_passed=all(content_checks.values()) and all(all(v.values()) for v in mechanical.values()),
        context_scoring_unit="24 families; final turn with all prior raw/content failures reported separately",
        judgments=rows, independent_human_blind_evidence_verified=False,
        pending=["matched Base/mid-training/direct-SFT comparison", "Base fluency retention", "multiple-seed sampling",
                 "blind human packet/provenance and reviewer agreement", "final recipe frozen then protected test"],
        protected_test_used=False, Chat_adopted=False, requested_five_steps_complete=False)


def paired_chat_comparison(control_evaluation, candidate_evaluation, control_items, candidate_items, control_review, candidate_review):
    """Matched dev differences only; not final adoption or independent confirmation."""
    from jmicro.japanese_evaluation import clustered_ci
    protocol_keys = ("tokenizer_sha256", "suite_sha256", "max_new_tokens", "model_context", "dtype", "backend",
                     "decoding", "evaluation_seed", "source_sha256", "implementation", "scored_split", "protected_test_used", "protocol")
    assert all(control_evaluation["binding"][k] == candidate_evaluation["binding"][k] for k in protocol_keys)
    if control_evaluation["binding"]["decoding"] == "sampling":
        assert control_evaluation["binding"]["sampling"] == candidate_evaluation["binding"]["sampling"]
        assert control_evaluation["binding"]["evaluation_seeds"] == candidate_evaluation["binding"]["evaluation_seeds"]
    assert control_review["rubric"] == candidate_review["rubric"] == RUBRIC
    assert control_review["reviewer"] == candidate_review["reviewer"], "Keep the reviewer/protocol matched"
    assert set(control_items) == set(candidate_items)
    scores = [{r["key"]: r for r in review["judgments"]} for review in (control_review, candidate_review)]
    paired = {}
    for condition in ("primary", "own_history_final24"):
        keys = [k for k, i in control_items.items() if (i["condition"] == "suppressed" if condition == "primary"
                else i["condition"] == "own-history" and i["final_turn"])]
        assert len(keys) == (80 if condition == "primary" else 24)
        metrics = ("grammar_score2", "relevance_score2", "joint_grammar_relevance", "context_score2",
                   "stop", "repetition", "empty", "role_leak", "unicode_failure")
        comparisons = {}
        for metric in metrics:
            rows = []
            for key in keys:
                left, right = control_items[key], candidate_items[key]
                assert all(left[k] == right[k] for k in ("id", "family_id", "category", "checks", "condition"))
                # Provided histories are identical. Own histories intentionally
                # differ because each model's actual responses are fed back.
                if condition == "primary": assert left["messages"] == right["messages"]
                values = []
                for side, item in enumerate((left, right)):
                    judgment, raw = scores[side][key], item["response"]
                    if metric.endswith("_score2"): value = judgment[metric.removesuffix("_score2")] == 2
                    elif metric == "joint_grammar_relevance": value = judgment["grammar"] == judgment["relevance"] == 2
                    elif metric == "stop": value = raw["stop_reason"] in ("eot", "eos")
                    elif metric == "empty": value = raw["empty_response"]
                    elif metric == "unicode_failure": value = not raw["valid_utf8"]
                    else: value = raw[metric]
                    values.append(int(value))
                rows.append(dict(id=left["id"], family=left["family_id"], difference=values[1]-values[0]))
            comparisons[metric] = clustered_ci(rows, key="difference")
        paired[condition] = comparisons
    return dict(status="matched_dev_ablation_complete_pending_Base_retention_and_final_evidence",
        difference_direction="mid-training+SFT minus direct SFT; positive failures mean regression",
        paired=paired, summaries=dict(direct_sft=control_review["summaries"], midtraining_sft=candidate_review["summaries"]),
        dev_screens=dict(direct_sft=control_review["dev_screen_passed"], midtraining_sft=candidate_review["dev_screen_passed"]),
        statistical_note="Family-paired descriptive bootstrap; multiple comparisons uncorrected, not independent confirmation",
        reviewer=control_review["reviewer"], independent_human_blind_evidence_verified=False,
        generation_policy={k: control_evaluation["binding"][k] for k in ("decoding", "evaluation_seed")},
        sampling_comparison_scope="One matched seed; final multi-seed claims require all configured seed reviews" if control_evaluation["binding"]["decoding"] == "sampling" else "Fixed greedy comparison",
        protected_test_used=False, Chat_adopted=False, requested_five_steps_complete=False,
        pending=candidate_review["pending"])
