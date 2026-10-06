"""Reject cached-control drift and nonfinite discarded training heads."""
import copy
import sys
from pathlib import Path
import torch

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from run_natural_context_contrast_projection import matched_control_checks, finite_projected_state


def record():
    return dict(counters=dict(update=4,token_digest='same',supervised_tokens=100,
        source_teachers={'web':75,'textbook':20,'story':5},source_EOS={'web':3},
        CE_input_tokens=120,original_body_bytes=400,auxiliary_input_tokens=90),
        sampler=dict(RNG=(1,2,3),pending={'web':[{'target_ids':[65,3]}]},draws=19))


def test_common_CE_checks_keep_full_cursor_but_do_not_equate_auxiliary_compute():
    a,b=record(),record()
    b['counters']['auxiliary_input_tokens']=0
    b['sampler']['RNG']=list(b['sampler']['RNG'])
    assert all(matched_control_checks(a,b).values())
    b['sampler']['pending']['web'][0]['target_ids'][0]=66
    assert not matched_control_checks(a,b)['full_sampler']
    for key in ('update','token_digest','supervised_tokens','source_teachers','source_EOS','CE_input_tokens','original_body_bytes'):
        changed=copy.deepcopy(a)
        changed['counters'][key]={'changed':1} if isinstance(a['counters'][key],dict) else 'changed'
        assert not matched_control_checks(a,changed)[key]


def test_terminal_requires_finite_separate_native_head_and_Adam():
    state=dict(model={'weight':torch.ones(2)},projector={'weight':torch.ones(2)},
        optimizer={'state':{0:{'exp_avg':torch.ones(2)}}})
    assert finite_projected_state(state)
    for section in ('model','projector'):
        changed=copy.deepcopy(state);changed[section]['weight'][0]=float('nan')
        assert not finite_projected_state(changed)
    changed=copy.deepcopy(state);changed['optimizer']['state'][0]['exp_avg'][0]=float('inf')
    assert not finite_projected_state(changed)
    del state['projector']
    assert not finite_projected_state(state)
