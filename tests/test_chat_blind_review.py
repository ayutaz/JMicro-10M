"""Synthetic protocol inputs only. These are not actual human submissions."""
import copy
import json
import pytest

from jmicro.chat_blind_review import make_packet, notes_template, restore_judgments, agreement


def fixture_packet():
    items = {f"fixture-{n}": dict(messages=[dict(role="user", content="今日は晴れですか？")],
        checks=[], response=dict(text="そうですね。")) for n in range(219)}
    arms = {"SECRET_MODEL_A": dict(evaluation_sha256="fixture-eval-a", checkpoint_sha256="fixture-checkpoint-a", items=items),
            "SECRET_MODEL_B": dict(evaluation_sha256="fixture-eval-b", checkpoint_sha256="fixture-checkpoint-b", items=items)}
    packet, mapping = make_packet(arms, seed=123)
    mapping["packet_sha256"] = "fixture-packet-sha"
    notes = notes_template(packet, "fixture-packet-sha")
    notes["reviewer"] = dict(identity="synthetic fixture, not a real person", kind="human", independent_human=True, blind=True)
    for row in notes["judgments"]:
        row.update(grammar=2, relevance=2, context=2, rationale="Synthetic scores used only to verify the protocol.")
    return packet, mapping, notes


def test_packet_hides_identity_and_roundtrip_preserves_all_responses():
    packet, mapping, notes = fixture_packet()
    public = json.dumps(packet)
    assert "SECRET_MODEL" not in public and "checkpoint" not in public and "private_seed" not in public
    assert len(packet["samples"]) == 438
    restored = restore_judgments(packet, "fixture-packet-sha", mapping, notes)
    assert set(restored) == {"SECRET_MODEL_A", "SECRET_MODEL_B"}
    assert all(len(r["judgments"]) == 219 for r in restored.values())
    assert {r["key"] for r in restored["SECRET_MODEL_A"]["judgments"]} == {f"fixture-{n}" for n in range(219)}
    assert restored["SECRET_MODEL_A"]["human_identity_source"].startswith("reviewer self-declaration")


def test_editing_displayed_history_or_partial_AI_or_other_packet_notes_rejected():
    packet, mapping, notes = fixture_packet()
    changed = copy.deepcopy(packet)
    changed["samples"][0]["messages"][0]["content"] = "Changed prompt"
    with pytest.raises(AssertionError):
        restore_judgments(changed, "fixture-packet-sha", mapping, notes)
    for mutate in (
        lambda n: n["judgments"].pop(),
        lambda n: n["judgments"].append(n["judgments"][0]),
        lambda n: n["judgments"][0].update(grammar=True),
        lambda n: n.update(packet_sha256="other-packet"),
        lambda n: n["reviewer"].update(kind="codex"),
        lambda n: n["reviewer"].update(blind=False),
    ):
        changed = copy.deepcopy(notes); mutate(changed)
        with pytest.raises(AssertionError):
            restore_judgments(packet, "fixture-packet-sha", mapping, changed)


def test_agreement_kappa_distinct_reviewers_and_degenerate_scores():
    left = dict(packet_sha256="fixture", reviewer=dict(identity="fixture-a"), judgments=[
        dict(sample_id=str(i), grammar=v, relevance=v, context=v) for i, v in enumerate((0, 1, 2))])
    right = copy.deepcopy(left); right["reviewer"]["identity"] = "fixture-b"
    for key in ("grammar", "relevance", "context"): right["judgments"][1][key] = 2
    result = agreement(left, right)
    assert result["dimensions"]["grammar"]["exact_agreement"] == pytest.approx(2/3)
    assert result["dimensions"]["grammar"]["cohen_kappa"] == pytest.approx(.5)
    for notes in (left, right):
        for row in notes["judgments"]: row.update(grammar=2, relevance=2, context=2)
    assert agreement(left, right)["dimensions"]["grammar"]["cohen_kappa"] is None
    right["reviewer"]["identity"] = " " + left["reviewer"]["identity"].upper() + " "
    with pytest.raises(AssertionError, match="distinct reviewers"):
        agreement(left, right)
