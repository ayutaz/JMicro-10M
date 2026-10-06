import copy
import sys
import torch
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/'scripts'))
from source_gradient_geometry import adamw_direction,body_from_full,cosine


def test_full_body_eos_gradient_decomposition_and_opposed_direction():
    p=torch.tensor([.4,-.7],requires_grad=True)
    body=p.square().sum();eos=(p-1).square().sum()
    full=(3*body+eos)/4
    fg=torch.autograd.grad(full,p,retain_graph=True)[0]
    eg=torch.autograd.grad(eos,p,retain_graph=True)[0]
    bg=torch.autograd.grad(body,p)[0]
    assert torch.allclose(body_from_full(fg,eg,4,1),bg)
    assert cosine(bg,-bg)['cosine'] < -.99999


def test_readonly_adamw_estimate_matches_real_clipped_step_and_groups():
    params=[torch.nn.Parameter(torch.tensor([[.3,.4],[.5,.6]])),torch.nn.Parameter(torch.tensor([.7,.8]))]
    opt=torch.optim.AdamW([dict(params=params[:1],weight_decay=.1),dict(params=params[1:],weight_decay=0.)],
        lr=.0002,betas=(.9,.95),eps=1e-8)
    for p in params:p.grad=torch.full_like(p,.02)
    opt.step();saved=copy.deepcopy(opt.state_dict());before=[p.detach().clone() for p in params]
    gradient=torch.arange(1,7,dtype=torch.float32)*.7
    estimated=adamw_direction(params,gradient,saved)
    assert all(torch.equal(p,b) for p,b in zip(params,before))
    assert all(torch.equal(saved['state'][k]['exp_avg'],v['exp_avg']) for k,v in opt.state_dict()['state'].items())
    offset=0
    for p in params:p.grad=gradient[offset:offset+p.numel()].view_as(p).clone();offset+=p.numel()
    torch.nn.utils.clip_grad_norm_(params,1.)
    opt.step()
    actual=torch.cat([(b-p.detach()).reshape(-1) for p,b in zip(params,before)])
    assert torch.allclose(actual,estimated,atol=5e-8,rtol=1e-4)
