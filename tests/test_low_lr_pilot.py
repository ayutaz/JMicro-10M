import copy
import math

import pytest
import torch

from jmicro.eos_pilot import pilot_lr
from jmicro.low_lr_pilot import set_fork_learning_rate


def test_lr_fork_preserves_adam_moments_and_resumes_decay_exactly():
    value = torch.nn.Parameter(torch.tensor([1., 2.]))
    optimizer = torch.optim.AdamW([value], lr=.002)
    value.grad = torch.tensor([.1, .2])
    optimizer.step()
    moments = copy.deepcopy(optimizer.state_dict()['state'])
    spec = {'pilot_schedule': {'parent_update': 10, 'stable_updates': 2, 'decay_updates': 2}}
    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lambda step: pilot_lr(spec, step))
    scheduler.last_epoch = 12
    set_fork_learning_rate(optimizer, scheduler, spec, .0002, 12)
    assert optimizer.param_groups[0]['lr'] == .0002
    for key in moments[0]:
        assert torch.equal(moments[0][key], optimizer.state_dict()['state'][0][key])
    saved_value = value.detach().clone()
    saved_optimizer, saved_scheduler = copy.deepcopy(optimizer.state_dict()), copy.deepcopy(scheduler.state_dict())
    resumed_value = torch.nn.Parameter(saved_value)
    resumed = torch.optim.AdamW([resumed_value], lr=.0002)
    resumed_scheduler = torch.optim.lr_scheduler.LambdaLR(resumed, lambda step: pilot_lr(spec, step))
    resumed.load_state_dict(saved_optimizer)
    resumed_scheduler.load_state_dict(saved_scheduler)
    for _ in range(2):
        value.grad = resumed_value.grad = torch.tensor([.3, -.1])
        optimizer.step()
        resumed.step()
        scheduler.step()
        resumed_scheduler.step()
        assert torch.equal(value, resumed_value)
        assert scheduler.state_dict() == resumed_scheduler.state_dict()
    assert optimizer.param_groups[0]['lr'] == pytest.approx(.00002)


@pytest.mark.parametrize('lr', [0, -1, math.inf, math.nan])
def test_invalid_lr_fork_leaves_optimizer_unchanged(lr):
    optimizer = torch.optim.AdamW([torch.nn.Parameter(torch.ones(1))], lr=.002)
    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lambda _: 1)
    spec = {'pilot_schedule': {'parent_update': 0, 'stable_updates': 2, 'decay_updates': 2}}
    before = copy.deepcopy(optimizer.state_dict())
    with pytest.raises(ValueError):
        set_fork_learning_rate(optimizer, scheduler, spec, lr, 0)
    assert optimizer.state_dict() == before
