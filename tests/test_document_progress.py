"""Absolute original EOS geometry, no window/PAD leakage and scalar gradients."""
import copy
import json
from pathlib import Path
import sys

import pytest
import torch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from natural_context_contrast_corpus import document_windows
from jmicro.document_progress import ProgressHead,progress_targets,progress_loss
from jmicro.model import JMicroModel


def windows(n):
    rows = list(document_windows([11+i%50 for i in range(n)]))
    for r in rows:
        r['original_body_tokens'] = n
        r['teacher_tokens'] = sum(t != -100 for t in r['target_ids'])
        r['original_EOS_targets'] = r['target_ids'].count(3)
    return rows


def test_BOS_body_and_original_EOS_fraction_independent_small_example():
    rows = windows(3)
    assert rows[0]['target_ids'] == [11,12,13,3]
    assert progress_targets(rows) == [[1.,2/3,1/3,0.]]


def test_long_document_absolute_labels_overlap_mask_and_each_teacher_exactly_once():
    rows = windows(2300)
    labels = progress_targets(rows)
    seen = {}
    for row,values in zip(rows,labels,strict=True):
        for i,(target,value) in enumerate(zip(row['target_ids'],values,strict=True)):
            if target == -100:
                assert value == -1.
                continue
            absolute = row['input_start']+i
            assert absolute not in seen
            assert value == (2300-absolute)/2300
            assert (value == 0.) == (target == 3)
            seen[absolute] = value
        if row['target_end'] < 2302:
            assert values[-1] > 0
    assert set(seen) == set(range(2301))
    assert sum(v == 0 for v in seen.values()) == 1
    assert any(-1. in r for r in labels)


def test_partial_quota_does_not_invent_EOS_or_rebase_remaining_fraction():
    rows = windows(900)
    row = copy.deepcopy(rows[0])
    keep = 20
    positions = [i for i,t in enumerate(row['target_ids']) if t != -100]
    for i in positions[keep:]: row['target_ids'][i] = -100
    row.update(teacher_tokens=keep,original_EOS_targets=0)
    values = progress_targets([row])[0]
    assert values[:keep] == [(900-i)/900 for i in range(keep)]
    assert values[keep:] == [-1.]*(len(values)-keep)
    assert min(values[:keep]) > .9 and not any(v == 0 for v in values)


def test_targets_do_not_mutate_original_rows_or_decode_text():
    rows = windows(1200)
    before = copy.deepcopy(rows)
    progress_targets(rows)
    assert rows == before


@pytest.mark.parametrize('bad',['N','start','first','end','length','EOS','overlap','teacher_count','EOS_count','token','empty_gold'])
def test_corrupt_geometry_or_ambiguous_artificial_terminal_refused(bad):
    row = windows(600)[-1]
    if bad == 'N': row['original_body_tokens'] = 0
    elif bad == 'start': row['input_start'] = -1
    elif bad == 'first': row['target_first'] = 0
    elif bad == 'end': row['target_end'] = 603
    elif bad == 'length': row['input_ids'].pop()
    elif bad == 'EOS': row['target_ids'][-2] = 3
    elif bad == 'overlap': row['target_ids'][0] = 11
    elif bad == 'teacher_count': row['teacher_tokens'] += 1
    elif bad == 'EOS_count': row['original_EOS_targets'] = 0
    elif bad == 'token': row['target_ids'][-1] = 1
    else: row['target_ids'] = [-100]*len(row['input_ids']); row['teacher_tokens']=0; row['original_EOS_targets']=0
    with pytest.raises(ValueError): progress_targets([row])


def test_sigmoid_L1_value_and_independent_analytic_gradient():
    z = torch.tensor([-1.,0.,2.],requires_grad=True)
    y = torch.tensor([.1,.3,.9])
    loss = progress_loss(z,y)
    p = 1/(1+torch.exp(-z.detach()))
    expected = (p-y).abs().sum()/3
    assert torch.equal(loss,expected)
    loss.backward()
    torch.testing.assert_close(z.grad,torch.sign(p-y)*p*(1-p)/3,atol=1e-8,rtol=1e-6)


def test_zero_head_preserves_RNG_and_has_no_initial_hidden_gradient_but_head_learns():
    rng = torch.get_rng_state().clone()
    h = ProgressHead(8)
    assert torch.equal(rng,torch.get_rng_state()) and not torch.cuda.is_initialized()
    assert sum(p.numel() for p in h.parameters()) == 8
    x = torch.arange(24,dtype=torch.float32).reshape(3,8).requires_grad_()
    y = torch.tensor([1.,.8,.7])
    progress_loss(h(x),y).backward()
    assert torch.count_nonzero(x.grad) == 0
    assert h.weight.grad.abs().sum() > 0
    assert torch.count_nonzero(h.weight) == 0


def test_active_head_backpropagates_into_native_hidden_without_detach():
    h = ProgressHead(8)
    h.weight.data.fill_(.01)
    x = torch.arange(24,dtype=torch.float32).reshape(3,8).requires_grad_()
    progress_loss(h(x),torch.tensor([1.,.7,.2])).backward()
    assert torch.isfinite(x.grad).all() and x.grad.abs().sum() > 0
    assert h.weight.grad.abs().sum() > 0


def test_scalar_head_explicit_FP32_under_BF16_autocast():
    h = ProgressHead(8)
    h.weight.data.copy_(torch.linspace(-.3,.4,8)[None])
    x = torch.linspace(-1,1,32).reshape(4,8)
    expected = h(x)
    with torch.autocast('cpu',dtype=torch.bfloat16):
        actual = h(x)
    assert actual.dtype == torch.float32 and torch.equal(expected,actual)


def test_actual_training_and_inference_count_remain_inside10M():
    c = json.loads((Path(__file__).resolve().parents[1]/'configs/phase6/base_10b.json').read_text())['model_config']
    with torch.device('meta'):
        native,head = JMicroModel(c),ProgressHead(c['hidden_size'])
    assert sum(p.numel() for p in native.parameters()) == 10001152
    assert sum(p.numel() for p in head.parameters()) == 256
    assert sum(p.numel() for m in (native,head) for p in m.parameters()) == 10001408
    assert native.lm_head.weight is native.model.embed_tokens.weight


@pytest.mark.parametrize('labels',[[-1.,.2],[1.1,.2],[float('nan'),.2]])
def test_ignored_invalid_or_nonfinite_labels_never_enter_auxiliary_loss(labels):
    with pytest.raises(ValueError): progress_loss(torch.zeros(2),torch.tensor(labels))
