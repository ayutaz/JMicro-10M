import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import pytest
import torch
from source_gradient_attribution import GROUPS,target_groups,gradients,describe,readonly_checks


def test_tied_parameter_exact_partition_and_logical_denominator():
    weight=torch.nn.Parameter(torch.arange(10,dtype=torch.float64)/10)
    labels=torch.tensor([[8,3,-100],[9,8,3],[8,-100,-100]])
    routes=['conditional_textbook','web','story'];masks=target_groups(labels,routes)
    before=weight.detach().clone();rng=torch.get_rng_state().clone()
    logits=weight.expand(3,3,10)
    vectors,counts,nll=gradients(logits,labels,masks,[weight,weight],6)
    expected=torch.softmax(weight.detach(),0)-torch.bincount(labels[labels!=-100],minlength=10)/6
    assert torch.allclose(vectors['independent_total'],expected,atol=1e-14)
    report=describe(vectors,counts,nll,1e-10)
    assert report['unique_parameter_elements']==10 and report['total_teacher_count']==6
    assert report['groups']['ordinary_textbook']['teachers']==0
    assert report['pairs']['web__ordinary_textbook']['cosine'] is None
    assert torch.equal(weight.detach(),before) and weight.grad is None and torch.equal(rng,torch.get_rng_state())
    # Same sequences split into microbatches, still divide by all six teachers.
    gathered={k:torch.zeros_like(v) for k,v in vectors.items()}
    for i in range(3):
        chunk,_,_=gradients(weight.expand(1,3,10),labels[i:i+1],target_groups(labels[i:i+1],[routes[i]]),[weight],6)
        for k,v in chunk.items():gathered[k]+=v
    assert all(torch.allclose(gathered[k],v,atol=1e-14) for k,v in vectors.items())


def test_opposing_contributions_and_failures():
    vectors={g:torch.zeros(2,dtype=torch.float64) for g in GROUPS}
    vectors['web']=torch.tensor([2.,0.],dtype=torch.float64)
    vectors['conditional_outcome_body']=torch.tensor([-1.,0.],dtype=torch.float64)
    vectors['independent_total']=torch.tensor([1.,0.],dtype=torch.float64)
    counts={g:int(g in ('web','conditional_outcome_body')) for g in GROUPS};nll={g:float(n) for g,n in counts.items()}
    report=describe(vectors,counts,nll,.02)
    assert report['pairs']['web__conditional_outcome_body']['cosine']==-1
    assert report['groups']['conditional_total']['contribution_to_total_squared_norm']==-1
    assert report['sum_source_total_squared_norm_contributions']==1
    with pytest.raises(ValueError,match='decomposition'):describe(dict(vectors,independent_total=torch.ones(2,dtype=torch.float64)),counts,nll,.02)
    with pytest.raises(ValueError,match='finite'):describe(dict(vectors,web=torch.tensor([float('nan'),0.])),counts,nll,.02)
    labels=torch.tensor([[8,3]]);masks=target_groups(labels,['conditional_textbook']);masks['web'][0,0]=True
    with pytest.raises(ValueError,match='Disjoint'):gradients(torch.zeros(1,2,10,requires_grad=True),labels,masks,[torch.nn.Parameter(torch.ones(1))],2)


def test_actual_module_readonly_and_corruption_detection():
    model=torch.nn.Linear(2,10,bias=False).double().eval()
    before={k:v.detach().clone() for k,v in model.state_dict().items()};rng=torch.get_rng_state().clone()
    labels=torch.tensor([[8,3]]);logits=model(torch.tensor([[[1.,0.],[0.,1.]]],dtype=torch.float64))
    vectors,counts,nll=gradients(logits,labels,target_groups(labels,['conditional_textbook']),model.parameters(),2)
    describe(vectors,counts,nll,1e-10)
    assert all(readonly_checks(model,before).values()) and torch.equal(rng,torch.get_rng_state())
    with torch.no_grad():model.weight[0,0]+=1
    assert not readonly_checks(model,before)['weights_unchanged']
    model.train();assert not readonly_checks(model,before)['eval_mode']
    with pytest.raises(ValueError,match='Only outcome'):target_groups(torch.tensor([[2,8]]),['conditional_textbook'])
