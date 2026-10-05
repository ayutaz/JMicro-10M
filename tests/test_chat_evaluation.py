from types import SimpleNamespace
import torch
import pytest
from jmicro.chat_evaluation import generate_reply,rollout_dialogue,summarize_chat
from jmicro.experiment import ROOT
from jmicro.tokenizer import Tokenizer
from jmicro.training import rng_state


class ScriptedModel(torch.nn.Module):
    """Protocol fixture, never model-quality evidence."""
    def __init__(self,ids):
        super().__init__();self.ids = ids;self.config = dict(max_position_embeddings=256)
        self.prompts = []
    def forward(self,x,cache=None,use_cache=True):
        index = 0 if cache is None else cache
        if cache is None: self.prompts.append(x[0].tolist())
        logits = torch.full((1,x.shape[1],4096),-100.)
        logits[0,-1,7] = 0.
        logits[0,-1,self.ids[min(index,len(self.ids)-1)]] = 100.
        return SimpleNamespace(logits=logits,cache=index+1)


def test_chat_eot_survives_suppression_and_unsuppressed_role_errors_are_visible():
    tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    model = ScriptedModel([6,7]);messages = [dict(role="user",content="こんにちは。")]
    primary = generate_reply(model,tok,messages,max_new=8,suppressed=True)
    control = generate_reply(model,tok,messages,max_new=8,suppressed=False)
    assert primary["generated_ids"] == [7] and primary["stop_reason"] == "eot"
    assert primary["empty_response"] and not primary["role_leak"] and 7 not in primary["suppressed_ids"]
    assert control["generated_ids"] == [6,7] and control["role_leak"] and control["empty_response"]
    assert summarize_chat([control])["mechanical_checks_only"]["role_leak_at_most1"] is False
    assert model.training  # Evaluation restores mode.


def test_raw_unicode_failure_and_max_length_do_not_become_successful_stops():
    tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    byte_id = next(i for i,b in tok.id_bytes.items() if b == b"\xe3")
    row = generate_reply(ScriptedModel([byte_id]),tok,[dict(role="user",content="猫。")],max_new=1)
    assert row["raw_bytes_hex"] == "e3" and row["valid_utf8"] is False and row["text"] == "\ufffd"
    assert row["stop_reason"] == "max_new_tokens"
    rates = summarize_chat([row]);assert rates["stop"] == 0 and rates["unicode_failure"] == 1
    unknown = generate_reply(ScriptedModel([1,7]),tok,[dict(role="user",content="猫。")],max_new=2,suppressed=False)
    assert not unknown["valid_utf8"] and unknown["decode_error"] == "unknown-token-id1" and unknown["generated_ids"] == [1,7]


def test_rollout_uses_own_replies_not_provided_gold_and_isolates_rng():
    tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    case = dict(id="fixture",family_id="fixture-family",category="context",split="dev",checks=["訂正を保持"],messages=[
        dict(role="user",content="京都に行くよ。"),dict(role="assistant",content="これは履歴用の正解回答。"),
        dict(role="user",content="大阪に訂正したよ。どこかな？"),dict(role="assistant",content="二番目の正解。"),
        dict(role="user",content="もう一度教えて。")])
    model = ScriptedModel([*tok.encode("了解です。"),7])
    before = torch.get_rng_state().clone()
    result = rollout_dialogue(model,tok,case,max_new=24)
    assert len(result["replies"]) == 3 and result["full_history_retained"]
    expected,_ = tok.chat_prompt([case["messages"][0],dict(role="assistant",content="了解です。"),case["messages"][2]],256-24)
    assert model.prompts[1] == expected and torch.equal(before,torch.get_rng_state())
    assert result["replies"][-1]["user_turns"] == 3
    assert summarize_chat(result["replies"])["stop"] == 3


def test_existing_dev_suite_has_intact_2_3_4turn_cases_and_no_test_selection():
    import sys
    sys.path.insert(0,str(ROOT/"scripts"))
    from evaluate_chat_sft import load_dev
    tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    cases,contexts = load_dev(tok,1024)
    assert len(cases) == 80 and all(c["split"] == "dev" for c in cases)
    lengths = [sum(m["role"] == "user" for m in c["messages"]) for c in contexts]
    assert {n:lengths.count(n) for n in (2,3,4)} == {2:16,3:5,4:3}
    with pytest.raises((AssertionError,ValueError)):
        load_dev(tok,64)
