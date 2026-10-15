"""Strict reference equality and independently measured saved dense storage."""
import pytest
import torch
import weakref

from jmicro.rdrop import two_view_objective
from jmicro.rdrop_analytic import analytic_two_view_objective


def pair(n,v,scale=1.,dtype=torch.float32):
    generator = torch.Generator().manual_seed(20261015)
    a = (torch.randn(n,v,generator=generator)*scale).to(dtype).requires_grad_()
    b = (torch.randn(n,v,generator=generator)*scale).to(dtype).requires_grad_()
    y = torch.randint(v,(n,),generator=generator)
    return a,b,y


@pytest.mark.parametrize('n,v,scale',[(1,3,.1),(2,3,1.),(7,17,3.),(32,4096,1.)])
@pytest.mark.parametrize('dtype',[torch.float32,torch.float64,torch.bfloat16])
def test_ALL_five_values_and_BOTH_full_gradients_EXACT_reference(n,v,scale,dtype):
    a,b,y = pair(n,v,scale,dtype)
    x,z = a.detach().clone().requires_grad_(),b.detach().clone().requires_grad_()
    reference = two_view_objective(a,b,y)
    actual = analytic_two_view_objective(x,z,y)
    assert reference.keys() == actual.keys()
    assert all(torch.equal(actual[k],reference[k]) for k in reference)
    reference['combined_loss'].backward()
    actual['combined_loss'].backward()
    assert torch.equal(a.grad,x.grad)
    assert torch.equal(b.grad,z.grad)


@pytest.mark.parametrize('weights',[(1.,0.,0.),(0.,1.,0.),(0.,0.,1.),(.37,-.23,.81)])
def test_individual_and_asymmetric_upstream_derivatives_EXACT_reference(weights):
    a,b,y = pair(7,17,1.)
    x,z = a.detach().clone().requires_grad_(),b.detach().clone().requires_grad_()
    r,c = two_view_objective(a,b,y),analytic_two_view_objective(x,z,y)
    fields = ('CE_view1_loss','CE_view2_loss','symmetric_KL')
    grad = tuple(torch.tensor(w) for w in weights)
    left = torch.autograd.grad(tuple(r[k] for k in fields),(a,b),grad_outputs=grad)
    right = torch.autograd.grad(tuple(c[k] for k in fields),(x,z),grad_outputs=grad)
    assert all(torch.equal(u,v) for u,v in zip(left,right,strict=True))


def test_gradient_against_independent_double_precision_probability_oracle():
    a,b,y = pair(2,3,.7)
    p,q = a.detach().double().softmax(-1),b.detach().double().softmax(-1)
    d = p.log()-q.log()
    hot = torch.nn.functional.one_hot(y,3).double()
    want_a = .5*(p-hot)/2+.25*(p*(d-(p*d).sum(-1,keepdim=True))+(p-q))/2
    want_b = .5*(q-hot)/2+.25*(q*(-d+(q*d).sum(-1,keepdim=True))+(q-p))/2
    analytic_two_view_objective(a,b,y)['combined_loss'].backward()
    assert torch.allclose(a.grad.double(),want_a,atol=1e-7,rtol=1e-6)
    assert torch.allclose(b.grad.double(),want_b,atol=1e-7,rtol=1e-6)


def test_saved_unique_dense_storage_strictly_less_than_original_autograd():
    def measure(function):
        a,b,y = pair(32,4096)
        packed = []
        class Saved:
            def __init__(self,tensor):
                self.tensor = tensor.detach()
        def pack(tensor):
            saved = Saved(tensor)
            if tensor.shape == a.shape:
                packed.append(weakref.ref(saved))
            return saved
        with torch.autograd.graph.saved_tensors_hooks(pack,lambda saved:saved.tensor):
            loss = function(a,b,y)
        storages = {}
        for ref in packed:
            saved = ref()
            if saved is not None:
                storage = saved.tensor.untyped_storage()
                storages[storage.data_ptr()] = storage.nbytes()
        return sum(storages.values()),len(storages),loss
    old,nold,_ = measure(two_view_objective)
    new,nnew,_ = measure(analytic_two_view_objective)
    assert nnew == 2 and new == 2*32*4096*4
    assert new < old and nnew < nold


def test_input_and_RNG_not_mutated_and_equal_views_zero_KL():
    a,_,y = pair(2,3)
    b = a.detach().clone().requires_grad_()
    before = (a.detach().clone(),b.detach().clone(),y.clone(),torch.get_rng_state().clone())
    loss = analytic_two_view_objective(a,b,y)
    assert loss['symmetric_KL'] == 0
    loss['symmetric_KL'].backward()
    assert torch.count_nonzero(a.grad) == torch.count_nonzero(b.grad) == 0
    for x,z in zip((a,b,y,torch.get_rng_state()),before,strict=True):
        assert torch.equal(x,z)


@pytest.mark.parametrize('change',['swap','repeat','shift'])
def test_probability_invariants(change):
    a,b,y = pair(2,3)
    r = analytic_two_view_objective(a,b,y)
    if change == 'swap': a,b = b,a
    elif change == 'repeat': a,b,y = a.repeat(3,1),b.repeat(3,1),y.repeat(3)
    else: a,b = a+3.,b-2.
    c = analytic_two_view_objective(a,b,y)
    for key in ('CE_loss','symmetric_KL','combined_loss'):
        assert torch.allclose(r[key],c[key],atol=3e-7,rtol=1e-6)


@pytest.mark.parametrize('bad',['masked','nonfinite','wrong_shape'])
def test_invalid_inputs_rejected(bad):
    a,b,y = pair(2,3)
    if bad == 'masked': y[0] = -100
    elif bad == 'wrong_shape': b = b[:1]
    else: b = b.detach(); b[0,0] = float('nan')
    with pytest.raises(ValueError): analytic_two_view_objective(a,b,y)


def test_higher_order_requests_explicitly_refused():
    a,b,y = pair(2,3)
    loss = analytic_two_view_objective(a,b,y)['combined_loss']
    with pytest.raises(RuntimeError,match='first-order'):
        torch.autograd.grad(loss,(a,b),create_graph=True)
