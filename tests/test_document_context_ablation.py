import json
import sys
from pathlib import Path
import pytest
import torch
from jmicro.model import JMicroModel
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from document_context_ablation import document_attention,context_logits,all_groups,summarize
from source_gradient_attribution import GROUPS,readonly_checks


def small_model():
    torch.manual_seed(42)
    config=json.loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    config.update(num_hidden_layers=2,hidden_size=16,intermediate_size=32,num_attention_heads=2,num_key_value_heads=1,head_dim=8,rotary_dim=8,vocab_size=300)
    return JMicroModel(config).eval()


def test_exact_boundary_causality_and_partial_leading_segment():
    ids=torch.tensor([[8,9,2,10,3,2,11,12]])
    positions,mask=document_attention(ids)
    assert positions.tolist()==[list(range(8))]
    assert mask[0,1].nonzero().flatten().tolist()==[0,1]
    assert mask[0,4].nonzero().flatten().tolist()==[2,3,4]
    assert mask[0,5].nonzero().flatten().tolist()==[5]
    assert mask[0,7].nonzero().flatten().tolist()==[5,6,7]
    _,full=document_attention(ids,False)
    assert full[0,7].all() and not full[0,0,1]
    with pytest.raises(ValueError,match='unpadded'):document_attention(torch.tensor([[2,0]]))


def test_native_control_and_cross_document_noninterference_with_immutable_model():
    model=small_model();ids=torch.tensor([[2,11,12,3,2,15,16,3]])
    before={k:v.detach().clone() for k,v in model.state_dict().items()};rng=torch.get_rng_state().clone()
    old=ids.clone();old[:,1:3]=torch.tensor([[21,22]])
    future=ids.clone();future[:,6]=25
    with torch.no_grad():
        native=model(ids,training_fast_path=True).logits;control=context_logits(model,ids,False)
        assert torch.allclose(native,control,atol=1e-6,rtol=1e-6)
        isolated=context_logits(model,ids)
        assert torch.equal(isolated[:,4:],context_logits(model,old)[:,4:])
        assert torch.equal(isolated[:,:6],context_logits(model,future)[:,:6])
        assert not torch.allclose(control[:,4:],context_logits(model,old,False)[:,4:],atol=1e-9,rtol=0)
    assert all(readonly_checks(model,before).values()) and torch.equal(rng,torch.get_rng_state())


def test_unequal_teacher_weighting_marker_and_missing_changed_group_rejection():
    records=[]
    for i in range(16):
        count=i+1;old={g:dict(teachers=count,nll_sum=float(count)) for g in GROUPS}
        new={g:dict(v) for g,v in old.items()}
        for g in GROUPS[-2:]:new[g]['nll_sum']+=count*(.2 if i<12 else .05)
        records.append(dict(index=i,isolated_groups=all_groups(new),cached_full_causal_groups=all_groups(old)))
    report=summarize(records)
    assert report['descriptive_conditional_history_dependence_marker']
    assert report['groups']['conditional_total']['teacher_weighted_CE_change']==pytest.approx((78*.2+58*.05)/136)
    records[-1]['isolated_groups']['web']['teachers']+=1
    with pytest.raises(ValueError,match='Paired'):summarize(records)
    with pytest.raises(ValueError,match='All16'):summarize(records[:15])
