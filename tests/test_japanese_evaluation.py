import math
from types import SimpleNamespace

import pytest
import torch

from jmicro.japanese_evaluation import (NativeLikelihood, answer_metrics, classification_summary,
    clustered_ci, encode_request, repetition_metrics, tied_prediction)


class Codec:
    def encode(self, text):
        return [ord(c) + 8 for c in text]
    def decode_bytes(self, ids):
        return "".join(chr(i-8) for i in ids).encode()


class Model:
    config = {"max_position_embeddings": 1024}
    def __call__(self, ids, attention_mask=None):
        logits = torch.zeros((*ids.shape, 140))
        # Vary probabilities with preceding token, making shift/context errors observable.
        logits.scatter_(-1, ((ids + 1) % 140).unsqueeze(-1), 3.)
        return SimpleNamespace(logits=logits)


def test_target_shift_context_and_right_padding():
    scorer = NativeLikelihood(Model(), Codec(), device="cpu", dtype="fp32")
    pairs = [("a\n", "bc"), ("long prefix\n", "z")]
    batch = scorer.score(pairs)
    for (context, target), row in zip(pairs, batch):
        single = scorer.score([(context, target)])[0]
        assert row == single
        assert row["target_tokens"] == len(target)
        ids = [2, *Codec().encode(context + target)]
        losses = []
        for position in range(len(context)+1, len(ids)):
            expected_logits = torch.zeros(140)
            expected_logits[(ids[position-1]+1) % 140] = 3.
            losses.append(-torch.log_softmax(expected_logits, 0)[ids[position]].item())
        assert row["log_likelihood"] == pytest.approx(-sum(losses))


def test_bos_empty_context_no_eos():
    row = NativeLikelihood(Model(), Codec(), device="cpu").score([("", "a")])[0]
    assert row["target_ids"] == [ord("a")+8]
    assert row["target_tokens"] == 1


def test_reject_overflow_empty_and_unstable_boundary():
    with pytest.raises(ValueError, match="overflow"):
        encode_request(Codec(), "a", "bc", maximum=2)
    with pytest.raises(ValueError, match="Empty"):
        encode_request(Codec(), "a", "")
    class Unstable(Codec):
        def encode(self, text):
            return [8 + len(text)]
    with pytest.raises(ValueError, match="boundary"):
        encode_request(Unstable(), "a", "b")


def test_rolling_scores_every_token_once():
    scorer = NativeLikelihood(Model(), Codec(), device="cpu", dtype="fp32")
    text = "abc" * 400
    result = scorer.loglikelihood_rolling([(text,)])[0][0]
    expected = scorer.score([( "", text[:600])])[0]["log_likelihood"] * 2
    assert result == pytest.approx(expected)


def test_chance_ties_macro_f1_mcc_and_clusters():
    assert tied_prediction([0, 0], 1) == {"prediction": 0, "credit": .5, "ties": 2}
    rows = [{"id": str(i), "family": str(i//2), "label": i % 2,
             "prediction": i % 2, "credit": 1} for i in range(6)]
    summary = classification_summary(rows, 2)
    assert summary["mcc"] == 1 and summary["macro_f1"] == 1
    assert clustered_ci(rows)["units"] == 3
    assert clustered_ci(rows)["ci95"] == [1, 1]


def test_cluster_point_keeps_example_weighting():
    rows = [{"id": "a", "family": "one", "credit": 1},
            {"id": "b", "family": "one", "credit": 1},
            {"id": "c", "family": "two", "credit": 0}]
    assert clustered_ci(rows)["point"] == pytest.approx(2/3)


def test_semantic_families_are_unique_counterbalanced_and_split_safe():
    import importlib.util
    from pathlib import Path
    spec = importlib.util.spec_from_file_location("prepare_eval", Path(__file__).parents[1]/"scripts/prepare_japanese_evaluation.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rows = module.semantic_suite()
    assert len(rows) == 240
    assert len({row["context"] for row in rows}) == 240
    families = {}
    for row in rows:
        families.setdefault(row["family"], []).append(row)
    assert len(families) == 120
    for pair in families.values():
        assert len(pair) == 2 and pair[0]["split"] == pair[1]["split"]
        assert pair[0]["choices"] == pair[1]["choices"]
        assert set(row["label"] for row in pair) == {0, 1}
    assert sum(row["split"] == "dev" for row in rows) == 192


def test_raw_flags_distinguish_role_eot_and_replacement():
    row = {"text": "同じ文章。同じ文章。同じ文章。\ufffd", "generated_ids": [8, 7, 3],
           "valid_utf8": True, "stop_reason": "stop_id"}
    result = repetition_metrics(row)
    assert result["same_sentence_reappears"] and result["first_adjacent_triple_repeat_char"] == 0
    assert result["base_eot_id_7"] and not result["role_ids_4_5_6"]
    assert result["literal_replacement_character"] and not result["raw_utf8_failure"]
    assert answer_metrics("東京都。", ["東京都"])["normalized_em"] == 1
    assert answer_metrics("東京", ["東京都"])["character_f1"] == .8
