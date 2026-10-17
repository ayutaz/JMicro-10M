import copy
from pathlib import Path
import sys
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from review_chat_natural import validate_reply
from jmicro.chat_evaluation import decode_reply
from jmicro.japanese_evaluation import repetition_metrics
from jmicro.tokenizer import Tokenizer,SUPPRESS_IDS
from jmicro.experiment import ROOT


def example(terminal):
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    messages=[dict(role='user',content='短い返事をお願いします。')]
    ids=tok.encode('あ')*32
    if terminal:ids[-1]=7
    prompt,_=tok.chat_prompt(messages,992)
    row=dict(**decode_reply(tok,ids),generated_ids=ids,stop_reason='eot' if terminal else 'max_new_tokens',
        generated_tokens=32,max_new_tokens=32,decoding='greedy',suppressed=True,suppressed_ids=list(SUPPRESS_IDS),
        empty_response=False,role_leak=False,unexpected_special=False,prompt_ids=prompt,prompt_tokens=len(prompt),
        removed_turns=0,full_history_retained=True,user_turns=1,repetition=True)
    metrics=repetition_metrics(dict(row,stop_reason='stop_id' if terminal else 'max_new_tokens'))
    row['repeat_metrics']={k:metrics[k] for k in ('char_4gram_repeat','token_4gram_repeat','same_sentence_reappears','first_adjacent_triple_repeat_char')}
    return tok,messages,row


def test_32nd_token_EOT_is_natural_but_32_body_tokens_are_a_length_stop():
    for terminal in (True,False):
        tok,messages,row=example(terminal)
        validate_reply(row,tok,messages,True)
        broken=dict(row,stop_reason='eot' if not terminal else 'max_new_tokens')
        with pytest.raises(AssertionError):validate_reply(broken,tok,messages,True)


@pytest.mark.parametrize('corruption',['old64_policy','wrong_history','corrupt_raw_bytes'])
def test_historical_policy_or_altered_history_bytes_are_refused(corruption):
    tok,messages,row=example(True)
    if corruption=='old64_policy':row['max_new_tokens']=64
    elif corruption=='wrong_history':row['prompt_ids']=[2,5,8,7,6]
    else:row['raw_bytes_hex']='ff'
    with pytest.raises(AssertionError):validate_reply(row,tok,messages,True)
