"""Independent padding comparison: full-B CPU parity, actual native GPU gates.

No new quality model is adopted here, and no main learned checkpoint is changed.
Strict existing numerical tolerances are recorded before measuring either arm.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import statistics
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.dynamic_chat_training import DynamicTeacherSampler,DynamicTeacherTrainer,POLICY
from jmicro.teacher_chat_training import TeacherBudgetSampler,TeacherChatTrainer,teacher_lr
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json,seed_all
from chat_generalization_contract import RUN,B,GPU_stage,preflight,load_parent,reference,require_ref
from phase6_performance import finite_state
from run_eos_short_pilot import equal_state

OUT=RUN/'padding'
TOLERANCES=dict(loss_atol=2e-6,tensor_rtol=2e-4,tensor_atol=2e-7)


def make_sampler(c,tok,rows):
    return TeacherBudgetSampler(rows,tok,1024,42,B,update_teachers=512,microbatch=32)


def prepare(c,tok,rows):
    assert not (OUT/'contract.json').exists(),'Preserve fixed padding contract'
    OUT.mkdir(parents=True,exist_ok=True)
    a=make_sampler(c,tok,rows);b=DynamicTeacherSampler.from_native(make_sampler(c,tok,rows))
    digest=hashlib.sha256();updates=0;shapes=set()
    while a.teacher_tokens<B:
        before=a.teacher_tokens;fixed,teachers,body=a.next_update();dynamic,t2,b2=b.next_update()
        assert (teachers,body,len(fixed))==(t2,b2,len(dynamic))
        digest.update(json.dumps([teachers,body,teacher_lr(before,teachers,B)],sort_keys=True).encode())
        for (x,y),(u,v) in zip(fixed,dynamic,strict=True):
            nr,nc=u.shape;assert torch.equal(x[:nr,:nc],u) and torch.equal(y[:nr,:nc],v)
            assert not bool(x[nr:].ne(0).any()) and not bool(y[nr:].ne(-100).any())
            assert not bool(x[:,nc:].ne(0).any()) and not bool(y[:,nc:].ne(-100).any())
            shapes.add(tuple(u.shape))
            for i in range(nr):
                n=int(u[i].ne(0).sum());digest.update(n.to_bytes(4,'little'))
                digest.update(u[i,:n].numpy().astype('<i8').tobytes())
                digest.update(v[i,:n].numpy().astype('<i8').tobytes())
        updates+=1
        if updates%1000==0:print(json.dumps(dict(CPU_updates=updates,teachers=a.teacher_tokens)),flush=True)
    fixed=a.state_dict();dynamic=b.state_dict()
    assert {k:v for k,v in fixed.items() if k!='physical_tokens'}=={
        k:v for k,v in dynamic.items() if k not in ('physical_tokens','padding_policy')}
    dry=read_json(RUN/'D1_dry_run.json');assert fixed==dry['sampler_terminal'] and updates==dry['updates']
    restored=DynamicTeacherSampler.from_native(make_sampler(c,tok,rows));restored.load_state_dict(dynamic)
    assert restored.state_dict()==dynamic
    assert dynamic['input_tokens']<=dynamic['physical_tokens']<fixed['physical_tokens']
    contract=dict(created_at=now(),format='separate_padding_diagnostic_v1',config=reference(Path(c['config_path'])),
        policy=POLICY,arm='D1',parent=c['parent'],records=c['arms']['D1']['records'],teacher_budget=B,
        sources={s:reference(ROOT/s) for s in ('src/jmicro/dynamic_chat_training.py','scripts/chat_generalization_padding.py')},
        existing_numerical_tolerances=TOLERANCES,speed_improvement_required=.10,
        full_teacher_updates=updates,Assistant_teachers=a.teacher_tokens,semantic_teacher_stream_sha256=digest.hexdigest(),
        exact_nonPAD_inputs_labels_complete_update_groups_LR=True,dynamic_sampler_terminal_resume=True,
        physical_fixed=fixed['physical_tokens'],physical_dynamic=dynamic['physical_tokens'],
        dynamic_shapes=[list(s) for s in sorted(shapes)],GPU_optimizer_updates_planned=8*2+4*2,
        GPU_budget_category='efficiency',GPU_budget_seconds=900.,
        GPU_resume_all_state_exact_required=True,main_training_sources_unchanged=True,
        protected_TEST_used=False,quality_evidence=False,model_adopted=False)
    atomic_json(OUT/'contract.json',contract)
    print(json.dumps(dict(CPU_full_B_parity=True,updates=updates,teachers=a.teacher_tokens,
        fixed=contract['physical_fixed'],dynamic=contract['physical_dynamic'])))


def check_contract(c):
    contract=read_json(OUT/'contract.json');require_ref(contract['config'])
    assert contract['config']['sha256']==c['config_sha256'] and contract['existing_numerical_tolerances']==TOLERANCES
    for ref in contract['sources'].values():require_ref(ref)
    return contract


def gpu(c,tok,rows):
    contract=check_contract(c);assert not (OUT/'result.json').exists(),'Retain completed comparison'
    parent=load_parent(c);histories={};states={};grads={};peaks={};errors=[]
    def build(dynamic):
        cls=DynamicTeacherTrainer if dynamic else TeacherChatTrainer
        return cls(parent,c['parent'],rows,tok,c['arms']['D1']['data_directory'],c['spec'],B,device='cuda')
    import gc
    def release():gc.collect();torch.cuda.empty_cache()
    with GPU_stage('efficiency','separate_dynamic_padding',c['config_sha256']) as (left,heartbeat):
        for name,dynamic in (('fixed',False),('dynamic',True)):
            t=build(dynamic);torch.cuda.reset_peak_memory_stats();histories[name]=[];states[name]=[];grads[name]=[]
            for i in range(8):
                if left()<60:raise TimeoutError('Padding comparison reserve reached')
                histories[name].append(t.step())
                if i<3:
                    states[name].append({k:v.detach().cpu().clone() for k,v in t.model.state_dict().items()})
                    grads[name].append({k:p.grad.detach().cpu().clone() for k,p in t.model.named_parameters() if p.grad is not None})
                heartbeat(phase=name,updates=i+1)
            assert finite_state(dict(model=t.model.state_dict(),optimizer=t.optimizer.state_dict()))
            peaks[name]=torch.cuda.max_memory_allocated();del t;release()
        for i in range(3):
            a,b=histories['fixed'][i],histories['dynamic'][i]
            assert (a['teachers_this_update'],a['microbatches'],a['lr'],a['EOT_teachers'])==(
                b['teachers_this_update'],b['microbatches'],b['lr'],b['EOT_teachers'])
            if abs(a['loss']-b['loss'])>TOLERANCES['loss_atol']:errors.append(dict(update=i+1,kind='loss',delta=abs(a['loss']-b['loss'])))
            for kind,data in (('model',states),('gradient',grads)):
                mismatched=[];maxdelta=0.
                for k,value in data['fixed'][i].items():
                    other=data['dynamic'][i][k];maxdelta=max(maxdelta,float((value-other).abs().max()))
                    if not torch.allclose(value,other,rtol=TOLERANCES['tensor_rtol'],atol=TOLERANCES['tensor_atol']):mismatched.append(k)
                if mismatched:errors.append(dict(update=i+1,kind=kind,parameters=mismatched,max_absolute_difference=maxdelta))
        # Exact continuation/resume within the new dynamic path. Different PAD
        # shapes have distinct native token digests; cross-policy equality is
        # instead the full-B nonPAD input/label/group digest established above.
        checkpoints={};resume_histories=[]
        for branch in ('continuous','resumed'):
            t=build(True);history=[]
            for i in range(4):
                if left()<30:raise TimeoutError('Dynamic resume reserve reached')
                history.append(t.step())
                if branch=='resumed' and i==1:
                    t.save(OUT/'split.pt');del t;release();t=build(True);t.load(OUT/'split.pt')
            t.save(OUT/(branch+'.pt'));checkpoints[branch]=reference(OUT/(branch+'.pt'))
            resume_histories.append(history);del t;release()
        pair=[torch.load(require_ref(checkpoints[k]),map_location='cpu',weights_only=False) for k in ('continuous','resumed')]
        keys=('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes','token_digest','lineage','update','spec')
        checks={key:equal_state(pair[0][key],pair[1][key]) for key in keys}
        for key in ('loss','gradient_norm','lr','assistant_teacher_tokens','EOT_teachers','token_digest'):
            checks['history_'+key]=[r[key] for r in resume_histories[0]]==[r[key] for r in resume_histories[1]]
        checks['finite']=all(finite_state(s) for s in pair)
        assert all(checks.values()),checks
        del pair;release()
    rates={name:sum(r['teachers_this_update'] for r in history[2:])/sum(r['seconds'] for r in history[2:]) for name,history in histories.items()}
    gain=rates['dynamic']/rates['fixed']-1
    result=dict(completed_at=now(),contract=reference(OUT/'contract.json'),histories=histories,
        numerical_errors=errors,numerical_tolerances_met=not errors,exact_dynamic_resume=checks,
        checkpoint_refs=checkpoints,teacher_tokens_per_second=rates,speed_relative_improvement=gain,
        peak_allocated_bytes=peaks,efficiency_candidate_qualified=not errors and gain>=.10,
        main_training_unchanged=True,quality_evidence=False,quality_model_adopted=False,
        GPU_optimizer_updates=24,learning_updates_of_main_candidate=0,
        limitation='Native diagnostic updates are not a full dynamic training quality comparison. BF16 shape changes may fail strict numerical equivalence; keep failures.')
    atomic_json(OUT/'result.json',result)
    print(json.dumps(dict(numerical_tolerances_met=not errors,exact_resume=True,speed_gain=gain,
        efficiency_candidate_qualified=result['efficiency_candidate_qualified'])))


def main():
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('prepare','gpu'),required=True);p.add_argument('--inspect',action='store_true');args=p.parse_args()
    c,tok,arms=preflight(ROOT/'configs/phase7/chat-generalization-20261013.json')
    torch.set_num_threads(2)
    if args.inspect:check_contract(c);print('Frozen padding CPU contract passed; no GPU');return
    if args.mode=='prepare':prepare(c,tok,arms['D1']);return
    torch.use_deterministic_algorithms(True);seed_all(42);gpu(c,tok,arms['D1'])


if __name__=='__main__':main()
