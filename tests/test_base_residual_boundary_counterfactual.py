"""LF-only original/counterfactual data and read-only event fixtures."""
import hashlib
from pathlib import Path
import sys
from types import SimpleNamespace
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
import pytest
import torch
from run_base_residual_boundary_counterfactual import variants,next_event


class Codec:
    def encode(self,text): return [b+8 for b in text.encode()]
    def decode_bytes(self,ids): return bytes(i-8 for i in ids if i>=8)


def row(text):
    return dict(full_original_body_text=text,input_ids=[2]+Codec().encode(text),
                full_original_body_sha256=hashlib.sha256(text.encode()).hexdigest())


def test_only_trailing_LF_changes_spaces_CR_punctuation_and_internal_LF_preserved():
    original='本文\n中身。\r \n\n'
    v=variants(row(original),Codec())
    assert [Codec().decode_bytes(r['input_ids'][1:]).decode() for r in v]==[original,'本文\n中身。\r ','本文\n中身。\r \n']
    assert v[0]['input_ids']==row(original)['input_ids']
    assert [r['queried_EOS_is_observed_original_target'] for r in v]==[True,False,False]


def test_original_ID_or_byte_drift_rejected_before_inference():
    r=row('内容。\n');r['input_ids'][-1]+=1
    with pytest.raises(ValueError,match='original'): variants(r,Codec())


def test_added_LF_must_also_fit_strict_context_bound():
    with pytest.raises(ValueError,match='context'): variants(row('a'*1022),Codec())


def test_queries_unmasked_EOS_and_LF_without_generating_or_forcing_any_token():
    class Model:
        def __init__(self): self.seen=[]
        def __call__(self,x):
            self.seen.append(x.tolist())
            logits=torch.zeros(1,x.shape[1],32);logits[:,:,-1]=1;logits[:,:,3]=4
            return SimpleNamespace(logits=logits)
    model=Model();case=dict(variant='original',input_ids=[2,9],body_bytes_hex='01')
    value=next_event(model,Codec(),case,[18],device='cpu')
    assert model.seen==[[[2,9]]] and value['EOS_rank']==1
    assert value['generated_tokens']==value['forced_EOS_tokens']==0
    assert value['EOS_probability']>value['LF_next_token_probability'] and len(value['top8'])==8
