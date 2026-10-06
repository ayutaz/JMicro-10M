"""Protocol evidence rejection; random-weight fixtures do not prove quality."""
import copy
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import pytest
import torch

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.model import JMicroModel
from natural_context_contrast_projection import ProjectedCorpusTrainer
from review_natural_context_contrast_projection import audit_checkpoint,audit_terminal,committed_history,HISTORY_KEYS
from run_natural_context_contrast_projection import matched_control_checks

torch.set_num_threads(2)


@pytest.fixture(scope='module')
def checkpoint_fixture():
    config=json.loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    config['qk_norm_type']='none'
    model=JMicroModel(config)
    parent=dict(model_config=config,model=model.state_dict(),update=5,tokens=90,supervised_tokens=80)
    c=dict(parent={'path':'protocol-parent','sha256':'a'*64},source_binding={'manifest_sha256':'b'*64},
        source_sha256={},goals={'web':12,'textbook':3,'story':1},CE_tokens_per_arm=16,
        batch=48,seed=42,GPU_budget_seconds=100)
    binding=dict(parent=c['parent'],source_binding=c['source_binding'],config_sha256='fixed',
        weights_role='scientific_projection',sources={})
    sampler=SimpleNamespace(goals=c['goals'])
    sampler.state_dict=lambda:dict(binding=c['source_binding'],consumed=c['goals'],goals=c['goals'],seed=42,
        draws=6,windows_emitted=4,pending={},RNG=('source',))
    trainer=ProjectedCorpusTrainer(parent,sampler,binding,batch=48,device='cpu')
    trainer.counters.update(update=3,supervised_tokens=16,source_teachers=c['goals'],
        source_EOS={'web':1,'textbook':1,'story':1},CE_input_tokens=20,auxiliary_input_tokens=12,
        auxiliary_pairs=4,physical_input_tokens=64,original_body_bytes=25)
    state=trainer.state_dict()
    # Synthetic CUDA protocol metadata, not a CUDA training claim.
    state['spec'].update(dtype='bf16',backend='flash')
    state['scheduler']['last_epoch']=3
    state['RNG']['cuda']=[torch.tensor([1],dtype=torch.uint8)]
    ids=state['optimizer']['param_groups'][0]['params']
    for i,(key,param) in enumerate(zip(ids,trainer.parameters,strict=True)):
        # Broadcast moments save fixture memory; no actual learning is claimed.
        state['optimizer']['state'][key]=dict(step=torch.tensor(3. if i<len(ids)-2 else 2.),
            exp_avg=torch.zeros(1).expand_as(param),exp_avg_sq=torch.zeros(1).expand_as(param))
    record=dict(status='complete',binding=binding,counters=copy.deepcopy(state['counters']),
        sampler=state['sampler'],scientific_CE_teacher_tokens=16,parent_CE_teacher_tokens=80)
    return c,state,record,dict(committed_updates=3,head_updates=2)


def test_head_Adam_steps_follow_eligible_pair_updates_not_all_CE_updates(checkpoint_fixture):
    c,state,record,history=checkpoint_fixture
    account=audit_checkpoint(state,record,c,'fixed',history)
    assert account['completed_updates']==3 and account['head_optimizer_updates']==2
    assert account['native_parameters']==10001152 and account['train_only_parameters']==98304
    assert account['native_vocabulary_uses_head'] is False
    assert account['additional_unique_supply_claimed'] is False


@pytest.mark.parametrize('change',('missing_head','seed','shape','nonfinite_head','wrong_Adam_step','missing_CUDA_RNG','native_contamination','quota'))
def test_corrupt_head_recipe_optimizer_RNG_or_teacher_state_rejected(checkpoint_fixture,change):
    c,original,record,history=checkpoint_fixture
    state={**original,'spec':copy.deepcopy(original['spec']),'projector':original['projector'].copy(),
        'model':original['model'].copy(),'optimizer':copy.copy(original['optimizer']),
        'RNG':original['RNG'].copy(),'sampler':copy.deepcopy(original['sampler'])}
    if change=='missing_head':del state['projector']
    elif change=='seed':state['spec']['projection']['head_seed']+=1
    elif change=='shape':state['projector']['2.weight']=torch.zeros(127,256)
    elif change=='nonfinite_head':state['projector']['0.weight']=torch.full((1,),float('nan')).expand(256,256)
    elif change=='wrong_Adam_step':
        state['optimizer']['state']=original['optimizer']['state'].copy()
        key=original['optimizer']['param_groups'][0]['params'][-1]
        state['optimizer']['state'][key]={**state['optimizer']['state'][key],'step':torch.tensor(3.)}
    elif change=='missing_CUDA_RNG':state['RNG']['cuda']=[]
    elif change=='native_contamination':state['model']['projector.0.weight']=torch.ones(1)
    else:state['sampler']['consumed']={'web':11,'textbook':4,'story':1}
    with pytest.raises(ValueError):audit_checkpoint(state,record,c,'fixed',history)


def terminal_fixture():
    c=dict(CE_tokens_per_arm=16,GPU_budget_seconds=100)
    trained=dict(counters=dict(update=3,token_digest='same',supervised_tokens=16,source_teachers={},source_EOS={},
        CE_input_tokens=20,original_body_bytes=25),sampler={})
    job=dict(status='complete',config_sha256='fixed',GPU_occupancy_seconds=50,pid=1,boot_id='boot',start_ticks='2')
    result=dict(status='complete',config_sha256='fixed',GPU_occupancy_seconds=50,
        actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},scientific_CE_teacher_tokens=16,
        reused_control_CE_teachers=200000000,reused_control_GPU_seconds=0,
        results={'projection':{'training':trained}},
        common_CE_checks={a:matched_control_checks(trained,trained) for a in ('CE','contrast')},
        Base_complete=False,Chat_started=False,quantization_started=False)
    return c,job,result


def test_final_review_requires_real_exit_boolean_checks_full_budget_and_Base_only():
    c,job,result=terminal_fixture()
    audit_terminal(job,result,c,'fixed',False)
    with pytest.raises(ValueError,match='exit'):audit_terminal(job,result,c,'fixed',True)
    for changes in ({'GPU_occupancy_seconds':101},{'reused_control_GPU_seconds':1},
                    {'Base_complete':True},{'Chat_started':True},{'quantization_started':True},
                    {'actual_identity':{'pid':1,'boot_id':'other','start_ticks':'2'}}):
        with pytest.raises(ValueError,match='terminal'):audit_terminal(job,{**result,**changes},c,'fixed',False)
    changed=copy.deepcopy(result);changed['common_CE_checks']['CE']['full_sampler']=1
    with pytest.raises(ValueError,match='terminal'):audit_terminal(job,changed,c,'fixed',False)


def log_rows(uses):
    teachers=aux=pairs=physical=0;rows=[]
    for update,used in enumerate(uses,1):
        teachers+=8;pairs+=used;aux+=6*used;physical+=16+8*used
        rows.append(dict(update=update,supervised_tokens=teachers,source_teachers={'web':teachers},source_EOS={'web':update},
            CE_input_tokens=10*update,auxiliary_input_tokens=aux,auxiliary_pairs=pairs,physical_input_tokens=physical,
            original_body_bytes=13*update,token_digest=str(update)*64,auxiliary_digest=str(pairs)*64,
            CE_loss=2.,contrast_loss=1. if used else 0.,combined_loss=2.1 if used else 2.,
            auxiliary_gradient_norm=1. if used else 0.,train_only_head_gradient_norm=.5 if used else 0.,
            gradient_norm=2.,seconds=.1,data_wait_seconds=.01,lr=1e-5,
            CE_targets_this_update=8,auxiliary_pairs_this_update=used,auxiliary_inputs_this_update=6*used,
            physical_inputs_this_update=16+8*used))
    return rows


def write_log(path,rows):path.write_text(''.join(json.dumps(r)+'\n' for r in rows))


def test_history_keeps_only_resumed_committed_path_and_counts_skipped_heads(tmp_path):
    first=log_rows([2,0,2]);later=log_rows([2,2,0])
    a=tmp_path/'metrics-999-10.jsonl';b=tmp_path/'metrics-3-20.jsonl'
    write_log(a,first);write_log(b,later[1:])
    terminal={k:later[-1][k] for k in HISTORY_KEYS}
    audit=committed_history([b,a],terminal)
    assert audit['committed_updates']==3 and audit['head_updates']==2
    assert audit['observed_completed_attempt_updates']==5 and audit['rolled_back_or_replayed_log_rows']==2
    assert len(audit['raw_metrics'])==2


def test_torn_uncommitted_tail_is_preserved_but_does_not_lose_resumed_completed_updates(tmp_path):
    rows=log_rows([2,0,2]);terminal={k:rows[-1][k] for k in HISTORY_KEYS}
    old=tmp_path/'metrics-1-10.jsonl';later=tmp_path/'metrics-2-20.jsonl'
    write_log(old,rows[:2]);old.write_text(old.read_text()+'{"update":3,')
    write_log(later,rows[2:])
    audit=committed_history([old,later],terminal)
    assert audit['committed_updates']==3 and audit['head_updates']==2
    assert audit['uncommitted_torn_tails']==[dict(path=str(old),uncommitted_tail_bytes=12)]
    assert old.read_text().endswith('{"update":3,')
    with pytest.raises(ValueError,match='Complete committed'):committed_history([old],terminal)


def test_malformed_terminated_row_is_never_silently_skipped(tmp_path):
    rows=log_rows([2,0,2]);terminal={k:rows[-1][k] for k in HISTORY_KEYS}
    path=tmp_path/'metrics-1-10.jsonl';write_log(path,rows)
    with path.open('a') as stream:stream.write('{"update":4,\n')
    with pytest.raises(ValueError,match='Malformed'):committed_history([path],terminal)


@pytest.mark.parametrize('change',('missing_update','wrong_counter','ineligible_head','nonfinite'))
def test_history_rejects_missing_nonfinite_or_ineligible_auxiliary_updates(tmp_path,change):
    rows=log_rows([2,0,2]);terminal={k:rows[-1][k] for k in HISTORY_KEYS}
    if change=='missing_update':del rows[1]
    elif change=='wrong_counter':rows[1]['supervised_tokens']+=1
    elif change=='ineligible_head':rows[1]['train_only_head_gradient_norm']=.1
    else:rows[1]['combined_loss']=float('nan')
    path=tmp_path/'metrics-1-10.jsonl';write_log(path,rows)
    with pytest.raises(ValueError):committed_history([path],terminal)
