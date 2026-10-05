"""Freeze a fixed seed42 Base after two learned seeds/full dev; then test once.

Preparation never opens test shards or selects test cases. Failed test results
are retained; this command cannot use test to choose another recipe or seed.
"""
import argparse
import gc
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.model import JMicroModel
from jmicro.readiness import evaluate_batched
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, rng_state, generate_suite
from jmicro.evaluation_memory import bound_evaluation_cache
from phase6_performance import alive, identity, finite_state
from run_eos_short_pilot import equal_state
import run_final_base_dev as dev
from review_final_base_dev import validate_content, validate_long, row_key
from run_seeded_base_confirmation import preflight as seed_preflight

GPU_LIMIT=1200
SELECTION=ROOT/'reports/phase6/final_Base_test_selection.json'
SOURCES=('scripts/run_final_base_test.py','scripts/run_final_base_test.ps1',
    'scripts/review_final_base_test.py','scripts/run_final_base_dev.py',
    'scripts/review_final_base_dev.py','scripts/run_seeded_base_confirmation.py',
    'scripts/review_seeded_base_confirmation.py','scripts/require_adopted_base.py',
    'src/jmicro/readiness.py','src/jmicro/evaluation_memory.py','src/jmicro/training.py')


def full_dev_evidence(path):
    config=read_json(path);run=ROOT/config['output']
    job=dev.completed_source(run)
    config,screen,record,inherited=dev.preflight(path)
    result=read_json(run/'result.json');review=read_json(run/'review.json')
    assert review['status']=='full_dev_all400_and_long40_content_evidence_complete'
    assert review['result_sha256']==sha256(run/'result.json')
    assert review['config_sha256']==job['config_sha256']==sha256(path)
    assert job['gpu_elapsed_seconds']<=config['GPU_budget_seconds']
    assert result['binding']['config_sha256']==sha256(path) and result['evaluation_RNG_isolated']
    assert review['quality_criteria_unchanged'] and review['full_automatic_conditions_pass']
    assert not review['protected_test_used'] and not review['Base_adopted']
    assert review['total_raw_content_count']==440 and review['newly_reviewed_raw_count']==360
    assert review['full_evaluation_sha256']==result['full_evaluation_sha256']==sha256(run/'full-dev.json')
    assert review['long_generation_sha256']==result['long_generation_sha256']==sha256(run/'long-generation.json')
    # Notes have a saved SHA; callers provide its exact path in review evidence.
    # Avoid any corpus scan: only use notes_path added to final-dev review below.
    notes_path=Path(review['notes_path'])
    assert notes_path.resolve().is_relative_to(ROOT/'reports/phase6')
    assert sha256(notes_path)==review['notes_sha256']
    document=read_json(notes_path);ev=read_json(run/'full-dev.json');long=read_json(run/'long-generation.json')
    assert document['full_evaluation_sha256']==review['full_evaluation_sha256']
    assert document['long_generation_sha256']==review['long_generation_sha256']
    tok=Tokenizer(config['tokenizer']['path']);validate_long(long['rows'],tok)
    scores=validate_content([*ev['generation']['outputs'],*long['rows']],document['notes'])
    assert document['inherited_fixed80_annotations']==config['source_annotations']
    prior={n[0]:n for n in inherited['notes']}
    fixed=[r for r in ev['generation']['outputs'] if r['suppressed'] and r['decoding']=='greedy']
    assert len(fixed)==80 and all(scores[row_key(r)]==[row_key(r),*prior[r['id']][1:]] for r in fixed)
    checks,_=dev.audit_full(ev,screen,tok,
        read_json(Path(config['references']['parent_body']['path']))['body'],
        read_json(Path(config['references']['parent_generation']['path']))['generation'],
        read_json(Path(config['references']['web_full']['path'])))
    assert checks==review['checks'] and all(v for group in checks.values() for v in group.values())
    return config,screen,record,dict(config=dev.ref(path),job=dev.ref(run/'job.json'),
        result=dev.ref(run/'result.json'),review=dev.ref(run/'review.json'),notes=dev.ref(notes_path))


def confirmation_pair(primary_path,replicate_path):
    primary,screen,record,proof=full_dev_evidence(primary_path)
    replicate,_,other,other_proof=full_dev_evidence(replicate_path)
    secondary_training=Path(replicate['training_config']['path'])
    recipe,base,_=seed_preflight(secondary_training)
    assert recipe['training_config']==primary['training_config']
    assert recipe['source_run']==primary['source_run'] and recipe['source_point']==primary['point']
    assert recipe['training_seed']==43 and recipe['source_training_seed']==42
    assert replicate['point']=='seed43-'+primary['point']
    seed_review=read_json(Path(replicate['source_run'])/'review.json')
    assert seed_review['actual_independent_training_complete'] and seed_review['independent_training_seed_screen_passed']
    assert seed_review['source_review']==recipe['source_review']
    a=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
    b=torch.load(other['checkpoint'],map_location='cpu',weights_only=False)
    assert finite_state(a) and finite_state(b) and a['spec']['seed']==42 and b['spec']['seed']==43
    assert not equal_state(a['model'],b['model'])
    assert primary['tokenizer']==replicate['tokenizer'] and primary['dev_shards']==replicate['dev_shards']
    assert primary['dev_manifest_sha256']==replicate['dev_manifest_sha256']
    return primary,screen,record,base,dict(seed42=proof,seed43=other_proof),recipe


def test_rules(protocol):
    targets=protocol['targets']
    return dict(grammar_2_rate=targets['base_grammar_2_rate'],
        stop_success_min=targets['stop_success_min'],empty_response_max=targets['empty_response_max'],
        role_leak_max=targets['role_leak_max'],unicode_failure_max=targets['unicode_failure_max_fixed_suite'],
        coherence_2_rate=27/80,appropriate_completion_rate=27/80,repetition_max_rate=18/80,
        all_raw_conditions_failures_zero=True,
        primary_cases=protocol['test_per_suite'],raw_modes_per_case=5,
        selection='Fixed primary learned seed42; no test-driven seed/recipe choice')


def freeze(path,primary_path,replicate_path):
    if path.exists():preflight(path);print('Final test recipe retained; no new selection');return
    if SELECTION.exists():
        raise ValueError('Final test selection is already sealed; no alternate recipe/seed using this protected test')
    primary,screen,record,base,proof,seed=confirmation_pair(primary_path,replicate_path)
    protocol=ROOT/'configs/evaluation/protocol.json'
    c=dict(kind='fixed_recipe_final_Base_test',version=1,
        primary_dev_config=dev.ref(primary_path),replicate_dev_config=dev.ref(replicate_path),confirmations=proof,
        checkpoint=dev.ref(Path(record['checkpoint'])),tokenizer=primary['tokenizer'],
        protocol=dev.ref(protocol),suite_sha256=primary['suite_sha256'],
        shards=primary['dev_shards'],manifest_sha256=primary['dev_manifest_sha256'],
        primary_point=primary['point'],primary_source_run=primary['source_run'],
        rules=test_rules(read_json(protocol)),GPU_budget_seconds=GPU_LIMIT,
        selected_training_seed=42,independent_training_seed=43,
        selection_frozen_before_test=True,protected_test_used=False,Base_adopted=False,
        quality_criteria_unchanged=True,requested_five_steps_complete=False,
        implementation=implementation_hashes(),source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        output='reports/phase6/'+path.stem,created_at=now())
    preflight(path,c);path.parent.mkdir(parents=True,exist_ok=True);atomic_json(path,c)
    atomic_json(SELECTION,dict(config=dev.ref(path),checkpoint=c['checkpoint'],selected_training_seed=42,
        suite_sha256=c['suite_sha256'],selection_frozen_before_test=True,created_at=now()))
    print('Fixed seed42 final test recipe frozen after both learned seeds/full dev; test unopened')


def preflight(path,recipe=None):
    c=read_json(path) if recipe is None else recipe
    # Confirm learning/full dev BEFORE reading the protected split.
    primary,screen,record,base,proof,seed=confirmation_pair(
        Path(c['primary_dev_config']['path']),Path(c['replicate_dev_config']['path']))
    assert c['confirmations']==proof
    for key in ('primary_dev_config','replicate_dev_config','checkpoint','tokenizer','protocol'):
        value=c[key];assert sha256(Path(value['path']))==value['sha256']
    assert c['checkpoint']==dev.ref(Path(record['checkpoint']))
    assert c['primary_source_run']==primary['source_run'] and c['primary_point']==primary['point']
    assert c['shards']==primary['dev_shards'] and c['manifest_sha256']==primary['dev_manifest_sha256']
    assert sha256(Path(c['shards'])/'manifest.json')==c['manifest_sha256']
    assert c['suite_sha256']==sha256(ROOT/'eval/base.jsonl')
    assert c['rules']==test_rules(read_json(Path(c['protocol']['path'])))
    assert c['kind']=='fixed_recipe_final_Base_test' and c['GPU_budget_seconds']==GPU_LIMIT
    assert c['selected_training_seed']==42 and c['independent_training_seed']==43 and c['selection_frozen_before_test']
    assert not c['protected_test_used'] and not c['Base_adopted'] and c['quality_criteria_unchanged']
    assert c['implementation']==implementation_hashes() and c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    if recipe is None:
        selection=read_json(SELECTION)
        assert selection['config']==dev.ref(path) and selection['checkpoint']==c['checkpoint']
        assert selection['selected_training_seed']==42 and selection['suite_sha256']==c['suite_sha256']
        assert selection['selection_frozen_before_test']
    output=(ROOT/c['output']).resolve();assert output.is_relative_to(ROOT/'reports/phase6')
    if (output/'job.json').exists() and alive(read_json(output/'job.json')):
        raise ValueError('Final test process is live; do not duplicate')
    return c,screen


def run(path):
    c,_=preflight(path);output=ROOT/c['output'];output.mkdir(parents=True,exist_ok=True)
    jp=output/'job.json';old=read_json(jp) if jp.exists() else {}
    if old:
        assert old['config_sha256']==sha256(path) and not alive(old)
        if old['status']=='complete':print('Completed final test retained; no rerun');return
    prior=old.get('GPU_elapsed_seconds',0.);started=None;stop=[False]
    if old:assert old['selection_sha256']==sha256(SELECTION)
    job=dict(status='starting',**identity(),config_sha256=sha256(path),selection_sha256=sha256(SELECTION),started_at=old.get('started_at',now()),
        GPU_elapsed_seconds=prior,additional_training_tokens=0,protected_test_used=False,Base_adopted=False,
        restart_command=f"scripts/run_final_base_test.ps1 -Config {path.relative_to(ROOT).as_posix()} -Worker")
    signal.signal(signal.SIGTERM,lambda *_:stop.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stop.__setitem__(0,True))
    def check():
        if stop[0]:raise InterruptedError('Interrupted; completed test sections retained')
        if started is not None and prior+time.monotonic()-started>GPU_LIMIT:
            raise TimeoutError('Cumulative final test GPU budget exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started is not None:job['GPU_elapsed_seconds']=prior+time.monotonic()-started
        atomic_json(jp,job)
    try:
        heartbeat('setup');torch.set_num_threads(2)
        for relative in (*SOURCES,path.relative_to(ROOT).as_posix()):
            target=output/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,target)
        with gpu_lock('cuda'),sdpa_kernel(SDPBackend.MATH):
            started=time.monotonic()
            # The first protected split access happens only after a valid
            # immutable selection and exclusive GPU ownership.
            job['protected_test_used']=True;heartbeat('protected-test-body')
            shard=Shard(Path(c['shards']),'test');tok=Tokenizer(c['tokenizer']['path'])
            state=torch.load(c['checkpoint']['path'],map_location='cpu',weights_only=False)
            model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
            memory=bound_evaluation_cache(model);before=rng_state()
            original_weights={k:v.detach().cpu().clone() for k,v in model.state_dict().items()}
            calls=[0]
            def guard(*_):
                check();calls[0]+=1
                if calls[0]%256==0:
                    heartbeat(job['stage'],forward_calls=calls[0])
            hook=model.register_forward_pre_hook(guard)
            binding=dict(config_sha256=sha256(path),checkpoint_sha256=c['checkpoint']['sha256'],selection_sha256=sha256(SELECTION))
            body_path=output/'test-body.json';generation_path=output/'test-generation.json'
            if body_path.exists():
                body_doc=read_json(body_path);assert body_doc['binding']==binding;body=body_doc['body']
            else:
                body=evaluate_batched(model,shard,'cuda','bf16',limit=None,batch=16,
                    progress=lambda done,total:heartbeat('protected-test-body',completed_tasks=done,total_tasks=total))
                atomic_json(body_path,dict(binding=binding,body=body))
            heartbeat('protected-test-generation')
            if generation_path.exists():
                saved=read_json(generation_path);assert saved['binding']==binding
            else:
                generated=generate_suite(model,tok,'cuda','bf16',split='test',limit=None,max_new=64,sampling=True)
                atomic_json(generation_path,dict(binding=binding,generation=generated))
            assert equal_state(before,rng_state()) and not model.training
            assert all(equal_state(original_weights[k],v.detach().cpu()) for k,v in model.state_dict().items())
            assert sha256(Path(c['checkpoint']['path']))==c['checkpoint']['sha256']
            hook.remove();heartbeat('complete')
            elapsed=prior+time.monotonic()-started
            atomic_json(output/'result.json',dict(status='fixed_recipe_final_test_complete_pending_all100_content',
                binding=binding,GPU_seconds=elapsed,body_sha256=sha256(body_path),generation_sha256=sha256(generation_path),
                evaluation_RNG_isolated=True,weights_unchanged=True,additional_training_tokens=0,
                protected_test_used=True,Base_adopted=False,requested_five_steps_complete=False,memory=dict(memory)))
            job.update(status='complete',completed_at=now(),GPU_elapsed_seconds=elapsed)
            del model,state;gc.collect();torch.cuda.empty_cache()
    except BaseException as error:
        job.update(status='failed',error=repr(error));raise
    finally:
        if started is not None and job['status']!='complete':job['GPU_elapsed_seconds']=prior+time.monotonic()-started
        atomic_json(jp,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--config',type=Path,required=True)
    mode=p.add_mutually_exclusive_group();mode.add_argument('--freeze',action='store_true');mode.add_argument('--inspect',action='store_true')
    p.add_argument('--primary-dev-config',type=Path);p.add_argument('--replicate-dev-config',type=Path)
    args=p.parse_args();path=args.config.resolve();assert path.is_relative_to(ROOT/'configs/phase6')
    if args.freeze:
        assert args.primary_dev_config is not None and args.replicate_dev_config is not None
        freeze(path,args.primary_dev_config.resolve(),args.replicate_dev_config.resolve())
    elif args.inspect:preflight(path);print('Final test preflight passed; no test split opened')
    else:run(path)
