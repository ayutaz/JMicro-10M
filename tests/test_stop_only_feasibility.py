"""Mathematical mechanism and byte/token path support, not model-quality tests."""
from pathlib import Path
import sys
import pytest
import torch
from torch.nn import functional as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from stop_only_feasibility import EOS_binary_loss,available_prefixes


def test_EOS_only_gradient_and_unchanged_non_EOS_order():
    logits=torch.tensor([[.2,-.5,.1,.9,-.3,.7,.3,-.1,.8,.4],[-.3,.2,.4,-.1,.5,.9,.3,.7,.2,.1]],dtype=torch.float64)
    labels=torch.tensor([3,8]);delta=torch.tensor([.4,-.6],dtype=torch.float64,requires_grad=True)
    corrected=logits.clone();corrected[:,3]+=delta
    ce=F.cross_entropy(corrected,labels);binary=EOS_binary_loss(logits,labels,delta)
    assert torch.allclose(torch.autograd.grad(ce,delta,retain_graph=True)[0],torch.autograd.grad(binary,delta)[0],atol=1e-15,rtol=1e-14)
    keep=torch.arange(10)!=3
    assert torch.equal(corrected[:,keep],logits[:,keep])
    assert torch.equal(corrected[:,keep].argmax(-1),logits[:,keep].argmax(-1))
    assert torch.equal(corrected[:,keep].softmax(-1),logits[:,keep].softmax(-1))
    ignored_logits=torch.cat((logits,torch.ones(1,10,dtype=torch.float64)))
    ignored_labels=torch.tensor([3,8,-100]);ignored_delta=torch.tensor([.4,-.6,100.],dtype=torch.float64)
    assert EOS_binary_loss(ignored_logits,ignored_labels,ignored_delta)==binary.detach()
    with pytest.raises(ValueError):EOS_binary_loss(logits,torch.tensor([0,-100]),delta)


def test_only_actual_valid_UTF8_token_boundaries_and_EOS_budget():
    class Tokens:
        def decode_bytes(self,ids):return b''.join({1:b'\xe3',2:b'\x81\x82',3:b'\n',4:b'a'}[v] for v in ids)
    prefixes=available_prefixes(dict(generated_ids=[1,2,3,4]),Tokens())
    assert set(prefixes)=={'あ','あ\na'} and prefixes['あ']['body_tokens']==2
    assert prefixes['あ']['raw_hex']=='e38182'
    assert max(v['body_tokens'] for v in available_prefixes(dict(generated_ids=[4]*64),Tokens()).values())==63
