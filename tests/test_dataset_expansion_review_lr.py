from copy import deepcopy
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import torch
from jmicro.eos_pilot import pilot_lr
from review_dataset_expansion_v2 import rates_follow_logged_convention

def actual_cpu_schedule():
    spec=dict(lr=.0001,pilot_schedule=dict(parent_update=0,stable_updates=2,decay_updates=2))
    parameter=torch.tensor(1.,requires_grad=True)
    optimizer=torch.optim.SGD([parameter],lr=spec['lr'])
    scheduler=torch.optim.lr_scheduler.LambdaLR(optimizer,lambda step:pilot_lr(spec,step))
    history=[]
    for update in range(1,5):
        used_lr=optimizer.param_groups[0]['lr']
        parameter.grad=torch.ones_like(parameter);optimizer.step();scheduler.step()
        history.append(dict(update=update,lr=used_lr))
    return dict(spec=spec,update=4,optimizer=optimizer.state_dict(),scheduler=scheduler.state_dict()),history

def test_applied_LR_and_next_saved_LR_across_real_scheduler_boundary():
    state,history=actual_cpu_schedule()
    assert history[-1]['lr']>.00001
    assert state['optimizer']['param_groups'][0]['lr']==.00001
    assert rates_follow_logged_convention(state,history)

def test_incorrect_applied_or_saved_rate_is_rejected():
    state,history=actual_cpu_schedule();bad=deepcopy(history)
    bad[-1]['lr']=state['optimizer']['param_groups'][0]['lr']
    assert not rates_follow_logged_convention(state,bad)
    state['optimizer']['param_groups'][0]['lr']=.0001
    assert not rates_follow_logged_convention(state,history)
