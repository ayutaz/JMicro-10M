import copy
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import pytest
import torch
from base_gradient_precision import comparison, first_AdamW_direction, vector_metrics, screen


def test_metrics_distinguish_scale_direction_and_zero():
    a = torch.tensor([1.,-2.,3.])
    m = vector_metrics(a,2*a)
    assert m['cosine'] == pytest.approx(1.) and m['relative_L2_error'] == pytest.approx(1.)
    assert vector_metrics(a,-a)['cosine'] == pytest.approx(-1.)
    assert vector_metrics(torch.zeros(3),torch.zeros(3))['both_zero']
    with pytest.raises(ValueError): vector_metrics(a,torch.full((3,),float('nan')))


def test_first_direction_matches_actual_fresh_AdamW_after_clip():
    weights = torch.tensor([.1,.2,-.3,.4],dtype=torch.float64)
    grad = torch.tensor([3.,-4.,1e-9,0.],dtype=torch.float64)
    parameter = torch.nn.Parameter(weights.clone())
    parameter.grad = grad.clone()
    torch.nn.utils.clip_grad_norm_([parameter],1.,error_if_nonfinite=True)
    optimizer = torch.optim.AdamW([parameter],lr=1e-3,weight_decay=.1)
    optimizer.step()
    predicted = weights*(1.-1e-3*.1)-1e-3*first_AdamW_direction(grad)
    assert torch.allclose(parameter,predicted,atol=1e-15,rtol=1e-13)
    assert torch.equal(grad,torch.tensor([3.,-4.,1e-9,0.],dtype=torch.float64))


def test_complete_distinct_parameter_grouping_and_input_preservation():
    names = ['model.embed_tokens.weight','model.layers.0.self_attn.q_proj.weight','model.norm.weight']
    a = {n:torch.ones(2) for n in names}
    before = copy.deepcopy(a)
    m = comparison(a,a,names)
    assert m['gradient']['elements'] == 6 and len(m['groups']) == 3
    assert m['fresh_AdamW_data_direction']['relative_L2_error'] == 0
    assert all(torch.equal(a[n],before[n]) for n in names)
    with pytest.raises(ValueError): comparison(a,{},names)


def test_screen_requires_same_path_two_sources_at_both_endpoints():
    names = ['model.norm.weight']
    good = comparison({names[0]:torch.ones(3)},{names[0]:torch.ones(3)},names)
    bad = comparison({names[0]:torch.ones(3)},{names[0]:-torch.ones(3)},names)
    e = {p:dict(sources={g:dict(comparisons={q:copy.deepcopy(good) for q in ('bf16_math','bf16_flash')})
            for g in ('web','textbook','story','stress1024')}) for p in ('parent','CE100M')}
    for p in e:
        for g in ('web','textbook'): e[p]['sources'][g]['comparisons']['bf16_flash'] = bad
    assert screen(e)['bf16_flash']['supported'] and not screen(e)['bf16_math']['supported']
    e['CE100M']['sources']['textbook']['comparisons']['bf16_flash'] = good
    assert not screen(e)['bf16_flash']['supported']
    with pytest.raises(ValueError): screen({'parent':e['parent']})
