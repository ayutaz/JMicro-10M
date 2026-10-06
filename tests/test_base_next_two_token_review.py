"""CPU metadata fixtures reject false native/auxiliary training completion.

Fake CUDA labels/RNG/moments below are protocol fixtures, not GPU learning.
"""
import copy
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import pytest
import torch

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from base_next_two_token_trainer import NextTwoTokenTrainer
from jmicro.model import JMicroModel
from review_base_next_two_token import audit_checkpoint,audit_terminal,committed_history,HISTORY_KEYS
from run_base_next_two_token import matched_control_checks

torch.set_num_threads(2)


@pytest.fixture(scope='module')
def fixture():
    config=json.loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    config.update(qk_norm_type='none',expected_parameter_count=10001152)
    model=JMicroModel(config)
    parent=dict(model_config=config,model=model.state_dict(),update=5,tokens=90,supervised_tokens=80)
    c=dict(parent={'path':'CPU-protocol-parent','sha256':'a'*64},source_binding={'manifest_sha256':'b'*64},
        source_sha256={},goals=dict(web=12,textbook=3,story=1),CE_tokens_per_arm=16,batch=48,seed=42,GPU_budget_seconds=100)
    binding=dict(parent=c['parent'],source_binding=c['source_binding'],config_sha256='fixed',weights_role='scientific_next_two',sources={})
    sampler=SimpleNamespace(goals=c['goals'])
    sampler.state_dict=lambda:dict(binding=c['source_binding'],consumed=c['goals'],goals=c['goals'],seed=42,
        draws=6,windows_emitted=4,pending={},RNG=('fixture-source',))
    trainer=NextTwoTokenTrainer(parent,sampler,binding,batch=48,device='cpu')
    trainer.counters.update(update=3,supervised_tokens=16,source_teachers=c['goals'],source_EOS=dict(web=1,textbook=1,story=1),
        CE_input_tokens=20,physical_input_tokens=64,original_body_bytes=25,
        next_two_teacher_positions=12,next_two_EOS_targets=2,next_two_body_bytes=15,next_two_target_mass=.1*12,
        source_next_two_teachers=dict(web=9,textbook=3,story=0),source_next_two_EOS=dict(web=1,textbook=1,story=0),
        auxiliary_physical_hidden_positions=64)
    state=trainer.state_dict();state['spec'].update(dtype='bf16',backend='flash')
    state['scheduler']['last_epoch']=3;state['RNG']['cuda']=[torch.tensor([1],dtype=torch.uint8)]
    for key,param in zip(state['optimizer']['param_groups'][0]['params'],trainer.all_parameters,strict=True):
        state['optimizer']['state'][key]=dict(step=torch.tensor(3.),exp_avg=torch.zeros(1).expand_as(param),exp_avg_sq=torch.zeros(1).expand_as(param))
    record=dict(status='complete',binding=binding,counters=copy.deepcopy(state['counters']),sampler=state['sampler'],
        scientific_CE_teacher_tokens=16,parent_CE_teacher_tokens=80)
    return c,state,record,dict(committed_updates=3,optimizer_updates=3,auxiliary_optimizer_updates=3)


def test_full_native_and_auxiliary_shapes_steps_separate_mass_and_original_inference(fixture):
    c,state,record,history=fixture
    account=audit_checkpoint(state,record,c,'fixed',history)
    assert account['native_parameters']==10001152 and account['train_only_parameters']==688896
    assert account['training_parameters']==10690048 and account['next_two_teacher_positions']==12
    assert not account['native_inference_changed'] and not account['additional_unique_supply_claimed']


@pytest.mark.parametrize('change',['coefficient','mask','head_seed','mass','quota','aux_Adam_step','missing_aux_moment',
    'missing_aux_weight','nonfinite_aux_weight','CUDA_RNG','aux_in_native'])
def test_incomplete_or_reinterpreted_auxiliary_native_state_rejected(fixture,change):
    c,original,record,history=fixture
    state={**original,'spec':copy.deepcopy(original['spec']),'sampler':copy.deepcopy(original['sampler']),
        'model':original['model'].copy(),'auxiliary_model':original['auxiliary_model'].copy(),
        'optimizer':copy.copy(original['optimizer']),'RNG':original['RNG'].copy()}
    if change=='coefficient':state['spec']['next_two_coefficient']=.2
    elif change=='mask':state['spec']['auxiliary_mask']='after_EOS_or_overlap_allowed'
    elif change=='head_seed':state['spec']['auxiliary_seed']+=1
    elif change=='mass':state['counters']={**state['counters'],'next_two_target_mass':2.}
    elif change=='quota':state['sampler']['consumed']=dict(web=11,textbook=4,story=1)
    elif change in ('aux_Adam_step','missing_aux_moment'):
        state['optimizer']['state']=original['optimizer']['state'].copy()
        key=original['optimizer']['param_groups'][0]['params'][-1]
        if change=='aux_Adam_step':state['optimizer']['state'][key]={**state['optimizer']['state'][key],'step':torch.tensor(2.)}
        else:state['optimizer']['state'].pop(key)
    elif change=='missing_aux_weight':state['auxiliary_model'].pop('norm.weight')
    elif change=='nonfinite_aux_weight':state['auxiliary_model']['norm.weight']=torch.full_like(state['auxiliary_model']['norm.weight'],float('nan'))
    elif change=='CUDA_RNG':state['RNG']['cuda']=[]
    else:state['model']['future_head.weight']=torch.ones(1)
    with pytest.raises((ValueError,RuntimeError)):audit_checkpoint(state,record,c,'fixed',history)


def test_auxiliary_Adam_steps_follow_actual_nonempty_future_updates(fixture):
    c,original,record,history=fixture
    state={**original,'optimizer':copy.copy(original['optimizer'])}
    state['optimizer']['state']=original['optimizer']['state'].copy()
    # Auxiliary groups start after all original unique native parameters.
    native=JMicroModel(original['model_config']);at=len(list(native.parameters()))
    for key in original['optimizer']['param_groups'][0]['params'][at:]:
        state['optimizer']['state'][key]={**original['optimizer']['state'][key],'step':torch.tensor(2.)}
    account=audit_checkpoint(state,record,c,'fixed',{**history,'auxiliary_optimizer_updates':2})
    assert account['optimizer_updates']==3 and account['auxiliary_optimizer_updates']==2


def test_terminal_requires_actual_exit_identity_budget_and_Base_only():
    c=dict(CE_tokens_per_arm=16,GPU_budget_seconds=100)
    trained=dict(counters=dict(update=3,token_digest='same',supervised_tokens=16,source_teachers={},source_EOS={},
        CE_input_tokens=20,original_body_bytes=25,auxiliary_input_tokens=0,auxiliary_pairs=0,physical_input_tokens=64),sampler={})
    job=dict(status='complete',config_sha256='fixed',GPU_occupancy_seconds=50,pid=1,boot_id='boot',start_ticks='2')
    result=dict(status='complete',config_sha256='fixed',GPU_occupancy_seconds=50,
        actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},scientific_CE_teacher_tokens=16,
        reused_control_CE_teachers=100000000,reused_control_GPU_seconds=0,results={'next_two':{'training':trained}},
        common_CE_checks={'CE':matched_control_checks(trained,trained)},Base_complete=False,Chat_started=False,quantization_started=False)
    audit_terminal(job,result,c,'fixed',False)
    with pytest.raises(ValueError):audit_terminal(job,result,c,'fixed',True)
    for change in ({'GPU_occupancy_seconds':101},{'Base_complete':True},{'Chat_started':True},
        {'quantization_started':True},{'reused_control_GPU_seconds':1}):
        with pytest.raises(ValueError):audit_terminal(job,{**result,**change},c,'fixed',False)


def logs():
    return [dict(update=i,supervised_tokens=8*i,source_teachers={'web':8*i},source_EOS={'web':i},CE_input_tokens=10*i,
        auxiliary_input_tokens=0,auxiliary_pairs=0,physical_input_tokens=16*i,original_body_bytes=13*i,
        token_digest=str(i)*64,auxiliary_digest='0'*64,next_two_teacher_positions=4*i,next_two_EOS_targets=i,
        next_two_body_bytes=8*i,next_two_target_mass=.1*4*i,auxiliary_physical_hidden_positions=16*i,
        source_next_two_teachers={'web':4*i},source_next_two_EOS={'web':i},CE_loss=2.,next_two_CE_loss=4.,
        combined_loss=2.4,next_two_head_gradient_norm=1.,gradient_norm=2.,seconds=.1,data_wait_seconds=.01,lr=1e-5,
        next_two_coefficient=.1,CE_targets_this_update=8,next_two_targets_this_update=4,
        auxiliary_inputs_this_update=0,physical_inputs_this_update=16) for i in range(1,4)]


def write(path,rows):path.write_text(''.join(json.dumps(row)+'\n' for row in rows))


def test_committed_later_attempt_retains_all_original_future_counters_and_torn_raw(tmp_path):
    rows=logs();terminal={k:rows[-1][k] for k in HISTORY_KEYS}
    old,later=tmp_path/'metrics-999-10.jsonl',tmp_path/'metrics-3-20.jsonl'
    write(old,rows[:2]);old.write_text(old.read_text()+'{"update":3,');write(later,rows[1:])
    result=committed_history([later,old],terminal)
    assert result['committed_updates']==result['auxiliary_optimizer_updates']==3
    assert result['rolled_back_or_replayed_log_rows']==1 and old.read_text().endswith('{"update":3,')
    with pytest.raises(ValueError,match='Complete committed'):committed_history([old],terminal)


@pytest.mark.parametrize('change',['missing_update','future_counter','mass','coefficient','mixed_loss','nonfinite','terminated_torn'])
def test_wrong_history_cannot_qualify_extra_or_missing_future_supervision(tmp_path,change):
    rows=logs();terminal={k:rows[-1][k] for k in HISTORY_KEYS}
    if change=='missing_update':rows.pop(1)
    elif change=='future_counter':rows[1]['next_two_teacher_positions']+=1
    elif change=='mass':rows[1]['next_two_target_mass']+=1
    elif change=='coefficient':rows[1]['next_two_coefficient']=.2
    elif change=='mixed_loss':rows[1]['combined_loss']=2.
    elif change=='nonfinite':rows[1]['next_two_CE_loss']=float('nan')
    path=tmp_path/'metrics-1-10.jsonl';write(path,rows)
    if change=='terminated_torn':
        with path.open('a') as stream:stream.write('{"update":4,\n')
    with pytest.raises(ValueError):committed_history([path],terminal)
