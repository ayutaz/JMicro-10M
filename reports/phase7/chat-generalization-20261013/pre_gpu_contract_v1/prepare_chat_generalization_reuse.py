"""Prove and register unchanged historical control, raw reviews and RPC NLL.

Nothing is learned or generated here. Original files remain immutable and all
rebound records identify their original evidence and zero new GPU work.
"""
import argparse
import ast
import copy
import json
from pathlib import Path
import shutil
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json,implementation_hashes
from jmicro.chat_review import review_items,content_review
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive,finite_state
from run_eos_short_pilot import equal_state
from chat_generalization_contract import RUN,B,reference,require_ref,preflight

OLD=ROOT/'reports/phase7/chat-improvement-20261012'
OLD_CONFIG=ROOT/'configs/phase7/chat-improvement-20261012.json'


def functions(path):
    tree=ast.parse(Path(path).read_text())
    return {n.name:ast.dump(n,include_attributes=False) for n in tree.body if isinstance(n,ast.FunctionDef)}


def prepare():
    target=RUN/'historical_control_preparation.json'
    assert not target.exists(),'Keep completed preparation; inspect its frozen references'
    old=read_json(OLD_CONFIG);oldsha=sha256(OLD_CONFIG)
    assert oldsha=='f18554e4ee8ed2c53ac41ae40d3b1f0db8d09c1cfe14ae47c2985676479169e3'
    assert old['teacher_budget']==B and old['parameter_count']==10001152
    assert old['implementation']==implementation_hashes()
    for source,digest in old['source_sha256'].items():assert sha256(ROOT/source)==digest,source
    for key in ('parent','tokenizer','old_suite'):require_ref(old[key])
    for key in ('records','manifest'):require_ref(old['arms']['C1'][key])
    dry=read_json(RUN/'D0_dry_run.json');prior=read_json(OLD/'C1_dry_run.json')
    assert dry==prior,'Same pure sampler must reproduce every original update/group/counter'
    assert dry['source_sha256']==old['arms']['C1']['records']['sha256']
    assert dry['sampler_binding']==old['arms']['C1']['sampler_binding']
    job=read_json(OLD/'C1/job.json');result=read_json(OLD/'C1/result.json')
    audit=read_json(OLD/'C1/training_audit.json')
    assert job['status']==result['status']=='learning_complete' and not alive(job)
    assert audit['passed'] and audit['config_sha256']==result['config_sha256']==job['config_sha256']==oldsha
    points=read_json(OLD/'C1/checkpoints.json');assert points==result['checkpoints']
    for point,ref in points.items():
        state=torch.load(require_ref(ref),map_location='cpu',weights_only=False)
        assert finite_state(state) and state['implementation_sha256']==old['implementation']
        assert state['lineage']['base_checkpoint']==old['parent'] and state['lineage']['optimizer_policy']=='fresh'
        assert state['spec']['seed']==42 and state['spec']['teacher_chat']['budget']==B
        assert state['spec']['teacher_chat']['data_binding']==dry['sampler_binding']
        assert state['supervised_tokens']==ref['Assistant_teachers'] and state['update']==ref['update']
        if point=='t3':assert state['sampler']==dry['sampler_terminal'] and state['supervised_tokens']==B
        del state
    probe=read_json(OLD/'native_probe.json');resume=read_json(OLD/'native_resume_gate.json')
    assert probe['passed'] and resume['passed'] and probe['config_sha256']==resume['config_sha256']==oldsha
    assert probe['arms']['C1']['finite'] and probe['arms']['C1']['within_limit']
    for tag in ('full-contract','epoch-and-terminal'):
        gate=resume['gates']['C1-'+tag];assert gate['passed'] and all(gate['checks'].values())
        states=[torch.load(require_ref(gate['checkpoint_refs'][branch]),map_location='cpu',weights_only=False)
            for branch in ('continuous','resumed')]
        for key in ('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens',
                    'body_bytes','token_digest','lineage','update','spec'):
            assert equal_state(states[0][key],states[1][key]),('old resume',tag,key)
        del states
    oldf=functions(ROOT/'scripts/evaluate_chat_improvement.py')
    newf=functions(ROOT/'scripts/evaluate_chat_generalization.py')
    same=('load_cases','chat','summarize','nll_batch','nll_windows')
    assert all(oldf[k]==newf[k] for k in same),'Inference/NLL algorithms must be unchanged'
    atomic_json(target,dict(created_at=now(),passed=True,arm='D0',old_arm='C1',
        old_config=reference(OLD_CONFIG),old_spec=old['spec'],old_parent=old['parent'],
        old_tokenizer=old['tokenizer'],old_records=old['arms']['C1']['records'],
        old_manifest=old['arms']['C1']['manifest'],D0_binding=dry['sampler_binding'],
        native_probe=reference(OLD/'native_probe.json'),native_resume=reference(OLD/'native_resume_gate.json'),
        training_audit=reference(OLD/'C1/training_audit.json'),checkpoints=points,
        old_result=reference(OLD/'C1/result.json'),old_job=reference(OLD/'C1/job.json'),
        metrics=reference(OLD/'C1/metrics.jsonl'),same_sampler_full_dry_run=True,
        unchanged_old_frozen_sources=len(old['source_sha256']),identical_evaluation_functions=list(same),
        source_sha256=sha256(Path(__file__)),new_learning_updates=0,new_GPU_optimizer_updates=0,
        independent_trained_seed=False,quality_improved=False))
    print('Historical C1 control proven identical to D0; no GPU rerun')


def copy_review(c,arm,point,oldarm):
    oldpath=OLD/'evaluation'/oldarm/point/'old/greedy/result.json'
    oldev=read_json(oldpath);oldnotes=read_json(oldpath.with_name('notes.json'))
    from evaluate_chat_generalization import load_cases
    from review_chat_generalization import fingerprint
    tok=Tokenizer(c['tokenizer']['path']);cases,_=load_cases(c['old_suite']['path'],tok)
    items=review_items(oldev,cases,tok,1024)
    original_review=content_review(oldev,sha256(oldpath),oldnotes,items)
    assert json.loads(json.dumps(original_review))==read_json(oldpath.with_name('review.json'))
    binding=oldev['binding'];oldconfig=read_json(OLD_CONFIG)
    assert binding['config_sha256']==sha256(OLD_CONFIG)
    assert binding['suite_sha256']==c['old_suite']['sha256']
    assert binding['tokenizer_sha256']==c['tokenizer']['sha256']
    assert binding['implementation']==c['implementation']
    assert binding['source_sha256']==oldconfig['source_sha256']
    ref=c['parent'] if arm=='parent' else read_json(RUN/'D0/checkpoints.json')[point]
    assert binding['checkpoint']==ref['path'] and binding['checkpoint_sha256']==ref['sha256']
    ev=copy.deepcopy(oldev)
    ev['binding'].update(config_sha256=c['config_sha256'],stage=arm+'-'+point,source_sha256=c['source_sha256'])
    ev['historical_reuse']=dict(raw=reference(oldpath),notes=reference(oldpath.with_name('notes.json')),
        original_binding=binding,new_generated_responses=0,identical_actual_history_and_raw_output=True)
    out=RUN/'evaluation'/arm/point/'old/greedy';out.mkdir(parents=True,exist_ok=True)
    assert not (out/'result.json').exists()
    atomic_json(out/'result.json',ev);atomic_json(out/'recipe.json',ev['binding'])
    newitems=review_items(ev,cases,tok,1024);assert set(newitems)==set(items)
    assert all(fingerprint(items[k])==fingerprint(newitems[k]) for k in items)
    notes=copy.deepcopy(oldnotes);notes['evaluation_sha256']=sha256(out/'result.json')
    notes['historical_reuse']=reference(oldpath.with_name('notes.json'))
    for note in notes['judgments']:
        note['reuse']=dict(source_notes=dict(path=str(oldpath.with_name('notes.json')),
            sha256=sha256(oldpath.with_name('notes.json')),key=note['key']),fingerprint=fingerprint(items[note['key']]))
    review=content_review(ev,sha256(out/'result.json'),notes,newitems)
    atomic_json(out/'notes.json',notes);atomic_json(out/'review.json',review)
    atomic_json(out/'job.json',dict(status='complete',historical_reuse=True,binding=ev['binding'],new_GPU_work=0))


def register():
    c,_,_=preflight(ROOT/'configs/phase7/chat-generalization-20261013.json')
    proof=read_json(require_ref(c['historical_control_evidence']))
    assert c['spec']==proof['old_spec'] and c['parent']==proof['old_parent'] and c['tokenizer']==proof['old_tokenizer']
    assert c['arms']['D0']['records']==proof['old_records'] and c['arms']['D0']['manifest']==proof['old_manifest']
    for key in ('native_probe','native_resume','training_audit','old_result','old_job','metrics'):require_ref(proof[key])
    directory=RUN/'D0';directory.mkdir(parents=True,exist_ok=True)
    assert not (directory/'result.json').exists()
    result=read_json(proof['old_result']['path']);result.update(config_sha256=c['config_sha256'],
        historical_reuse=True,source_evidence=c['historical_control_evidence'],new_learning_updates=0,new_GPU_work=0)
    job=read_json(proof['old_job']['path']);job.update(config_sha256=c['config_sha256'],arm='D0',
        historical_reuse=True,source_evidence=proof['old_job'],new_learning_updates=0)
    atomic_json(directory/'job.json',job);atomic_json(directory/'result.json',result)
    atomic_json(directory/'checkpoints.json',proof['checkpoints'])
    shutil.copyfile(require_ref(proof['metrics']),directory/'metrics.jsonl')
    for arm,oldarm,points in (('parent','parent',('t0',)),('D0','C1',('t1','t2','t3'))):
        for point in points:copy_review(c,arm,point,oldarm)
    atomic_json(RUN/'historical_control_registration.json',dict(passed=True,config_sha256=c['config_sha256'],
        source_evidence=c['historical_control_evidence'],old_suite_judgments_reused=4*219,
        newly_generated_responses=0,new_learning_updates=0,new_GPU_work=0,
        protected_TEST_used=False,independent_trained_seed=False,completed_at=now()))
    print('D0 checkpoint control and 876 verified old-suite judgments registered; originals preserved')


def reusable_rpc(c,arm,point,ref):
    """Exact frozen RPC targets; batching has no interaction between examples."""
    if arm not in ('parent','D0'):return [],None
    oldarm='parent' if arm=='parent' else 'C1'
    path=OLD/'NLL'/oldarm/(point+'.json');record=read_json(path);old=read_json(OLD_CONFIG)
    assert record['status']=='complete' and record['binding']['config_sha256']==sha256(OLD_CONFIG)
    assert record['binding']['checkpoint']==ref and old['implementation']==c['implementation']
    oldtarget=require_ref(record['binding']['fixed_targets'])
    prior={r['id']:r for r in map(json.loads,oldtarget.read_text().splitlines()) if r['dataset']=='RPC_DEV'}
    current=[r for r in map(json.loads,require_ref(c['fixed_NLL']).read_text().splitlines()) if r['dataset']=='RPC_DEV']
    assert len(prior)==len(current)==2250
    rows={r['id']:r for r in record['targets'] if r['dataset']=='RPC_DEV'}
    result=[]
    for r in current:
        assert r==prior[r['id']],'RPC inputs, labels, bytes and window digest must be identical'
        row=rows[r['id']];assert row['body_teachers']==r['teachers']-1 and row['body_bytes']==r['body_bytes'] and row['EOT_teachers']==1
        result.append(row)
    return result,dict(source=reference(path),targets=2250,new_GPU_NLL_targets=0,
        same_checkpoint_and_exact_target_windows=True,unchanged_fixed32_math_BF16_batch_function=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=('prepare','register'));args=p.parse_args()
    torch.set_num_threads(2)
    prepare() if args.mode=='prepare' else register()
