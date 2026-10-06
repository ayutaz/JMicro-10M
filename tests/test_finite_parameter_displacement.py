import hashlib
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import numpy as np
import pytest
import torch
from finite_parameter_displacement import recover_batch,directional_dot,summarize_displacement


def test_exact_train_blocks_ignore_BOS_and_refuse_changed_raw_counts():
    tokens=np.asarray([2,8,9,3,2,10,3,2,11,12,3,2,13,14,3,2,15],dtype='<u2')
    sizes=np.arange(32,dtype=np.int64)
    expected_x=np.asarray([[2,8,9,3],[11,12,3,2]],dtype='<i8')
    expected_y=np.asarray([[8,9,3,-100],[12,3,-100,13]],dtype='<i8')
    row=dict(original_Web_blocks=[0,2],input_sha256=hashlib.sha256(expected_x.tobytes()).hexdigest(),
        target_sha256=hashlib.sha256(expected_y.tobytes()).hexdigest(),teachers=6,body_teachers=4,EOS_teachers=2,body_bytes=42)
    x,y=recover_batch(tokens,sizes,row,context=4)
    assert np.array_equal(x,expected_x) and np.array_equal(y,expected_y)
    changed=tokens.copy();changed[9]=13
    with pytest.raises(ValueError,match='hash and counts'):recover_batch(changed,sizes,row,4)
    with pytest.raises(ValueError,match='hash and counts'):recover_batch(tokens,sizes,dict(row,teachers=7),4)
    with pytest.raises(ValueError,match='outside TRAIN'):recover_batch(tokens,sizes,dict(row,original_Web_blocks=[9]),4)


def test_unique_tied_parameter_gradient_without_optimizer_or_grad_assignment():
    model=torch.nn.Module();model.left=torch.nn.Linear(2,2,bias=False);model.right=model.left
    with torch.no_grad():model.left.weight.copy_(torch.eye(2))
    parameters=list(model.parameters());assert len(parameters)==1
    before=model.left.weight.detach().clone()
    loss=(model.left(torch.tensor([[1.,2.]]))**2).sum()
    gradients=torch.autograd.grad(loss,parameters)
    direction=[torch.full_like(before,.25)]
    assert directional_dot(gradients,direction)==pytest.approx(4.5)
    assert torch.equal(model.left.weight,before) and all(p.grad is None for p in parameters)
    with pytest.raises(ValueError,match='Finite'):directional_dot([torch.tensor([float('nan')])],[torch.ones(1)])


def test_linear_quadratic_residual_markers_and_nonpositive_denominator():
    # f(t)=1+0.1*t+2*t^2, slope0.1; statistic is half of quadratic Hessian4.
    r=summarize_displacement(1.,1.55,3.1,.1)
    assert r['actual_body_CE_change']==pytest.approx(2.1)
    assert r['nonlinear_residual']==pytest.approx(2.)
    assert r['finite_difference_statistic']==pytest.approx(2.)
    assert r['harm_marker'] and r['nonlinear_half_or_more_marker']
    linear=summarize_displacement(1.,1.1,1.2,.2)
    assert linear['nonlinear_residual']==pytest.approx(0,abs=1e-15)
    assert not linear['nonlinear_half_or_more_marker']
    assert summarize_displacement(1.,.9,.8,-.2)['nonlinear_fraction_of_positive_change'] is None
    with pytest.raises(ValueError,match='finite'):summarize_displacement(1.,float('inf'),2.,.1)
