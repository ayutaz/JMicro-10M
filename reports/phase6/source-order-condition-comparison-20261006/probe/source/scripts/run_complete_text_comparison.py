"""Frozen final10B three-arm100M comparison; no learning beyond stage3."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
import torch
from jsonschema import validate
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.eos_pilot import TrainView
from jmicro.evaluation_memory import bound_evaluation_cache
from jmicro.experiment import ROOT, now, read_json, write_json, sha256
from jmicro.japanese_evaluation import NativeLikelihood
from jmicro.low_lr_pilot import LowLRPilotTrainer
from jmicro.model import JMicroModel
from jmicro.readiness import evaluate_batched
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, rng_state, seed_all
from phase6_performance import identity, alive, finite_state
import run_eos_short_pilot as pilot
from run_eos_complete_100m import adoption_checks
from evaluate_japanese_base import build_tasks, evaluate_choices

PLAN = ROOT/'configs/phase6/complete_text_10b_100m.json'
RUN = ROOT/'reports/phase6/complete-text-10b-100m-20261004'
POOL = Path('/home/aihub_ubuntu/jmicro-data/phase6/simple-stories-ja-20261004/shards')
SOURCES = ('scripts/run_complete_text_comparison.py', 'scripts/run_complete_text_comparison.ps1',
           'src/jmicro/coherent_units.py', 'scripts/prepare_coherent_text.py',
           'scripts/inspect_complete_text_data.py', 'scripts/prepare_story_text.py', 'src/jmicro/eos_pilot.py',
           'src/jmicro/low_lr_pilot.py', 'scripts/run_eos_short_pilot.py',
           'scripts/run_eos_complete_100m.py', 'scripts/evaluate_japanese_base.py',
           'src/jmicro/japanese_evaluation.py', 'src/jmicro/readiness.py',
           'src/jmicro/evaluation_memory.py', 'src/jmicro/tokenizer.py')


def freeze():
    assert not (RUN/'job.json').exists(), 'Do not refreeze a started run'
    old = read_json(ROOT/'configs/phase6/eos_5b_finish_100m.json')
    base = read_json(ROOT/'configs/phase6/base_10b.json')
    parent_path = ROOT/'reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt'
    parent = torch.load(parent_path, map_location='cpu', weights_only=False)
    assert sha256(parent_path)=='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
    assert (parent['tokens'],parent['update'])==(10000007168,305176)
    assert parent['implementation_sha256']==implementation_hashes()
    assert all(math.isclose(g['lr'], .0002, rel_tol=1e-6) for g in parent['optimizer']['param_groups'])
    assert (parent['spec']['batch'],parent['spec']['context'],parent['spec']['accumulation'])==(32,1024,1)
    assert parent['spec']['backend']=='flash' and parent['spec']['compile'] and parent['spec']['training_fast_path']
    assert finite_state(parent)
    ready = read_json(POOL/'ready.json')
    assert read_json(POOL/'manifest.json')['selection_source_sha256']==sha256(ROOT/'scripts/prepare_story_text.py')
    assert ready['parent_split_disjoint']
    content = read_json(RUN/'data-content-review.json')
    assert 25_000_000 <= ready['totals']['tokens'] <= 50_000_000
    assert content['accepted_for_experiment'] and content['pool_manifest_sha256']==sha256(POOL/'manifest.json')
    assert content['sample_sha256']==sha256(RUN/'data-inspection/stories.json')
    assert all(read_json(RUN/'data-inspection/result.json')['boundary_checks'].values()) and content['independent_human_certification'] is False
    suites=list(ET.parse(RUN/'tests.xml').getroot().iter('testsuite'))
    assert sum(int(s.attrib.get('tests',0)) for s in suites)>=36
    assert not any(int(s.attrib.get(k,0)) for s in suites for k in ('failures','errors','skipped'))
    plan = dict(version=1, scope='authorized stages1–3; report and stop; no500M/1B/20B/Chat',
        output=str(RUN.relative_to(ROOT)), parent=dict(path=str(parent_path),sha256=sha256(parent_path),update=305176,tokens_seen=10000007168),
        web_shards=old['web_shards'], web_manifest_sha256=old['web_manifest_sha256'],
        dev_shards=old['dev_shards'], dev_manifest_sha256=sha256(Path(old['dev_shards'])/'manifest.json'),
        tokenizer=old['tokenizer'],tokenizer_sha256=old['tokenizer_sha256'],suite_sha256=old['suite_sha256'],
        arms={'web':dict(pool=old['short_pool'],manifest_sha256=old['short_manifest_sha256'],short_updates=0),
              'short20':dict(pool=old['short_pool'],manifest_sha256=old['short_manifest_sha256'],short_updates=610),
              'coherent20':dict(pool=str(POOL),manifest_sha256=sha256(POOL/'manifest.json'),short_updates=610)},
        updates_per_arm=3052,stable_updates=2900,decay_updates=152,tokens_per_update=32768,
        tokens_per_arm=100007936,scientific_total_tokens=300023808,peak_lr=.0002,
        final_update=308228,final_tokens=10100015104,
        gpu_budget_seconds=1800,conditional_full_evaluation_budget_seconds=3000,
        evaluation=dict(dev_documents=256, fixed_dev_prefixes=80, max_new_tokens=64,
                        tasks=['semantics','jblimp','jcqa'],config='configs/evaluation/japanese_base_v2.json',
                        config_sha256=sha256(ROOT/'configs/evaluation/japanese_base_v2.json'),
                        semantic_suite='eval/japanese_semantics_v2_1.jsonl',semantic_sha256=sha256(ROOT/'eval/japanese_semantics_v2_1.jsonl'),
                        data_manifest_sha256=sha256(Path('/home/aihub_ubuntu/jmicro-data/evaluation-v2/manifest.json'))),
        gates=dict(v1_unchanged=True,EOS_gain=8,max_BPB_ratio=1.01,coherence_gain=8,
                   paired_coherence_ci_lower_above=0,raw_failure_count=0),
        data_review_sha256=sha256(RUN/'data-content-review.json'),
        tests_sha256=sha256(RUN/'tests.xml'), implementation=implementation_hashes(),
        source_sha256={p:sha256(ROOT/p) for p in SOURCES}, protected_test_used=False, created_at=now())
    schema = dict(type='object', additionalProperties=False, required=list(plan),
                  properties={k:{'const':v} for k,v in plan.items()})
    validate(plan,schema)
    write_json(PLAN,plan)
    write_json(ROOT/'schemas/configs/phase6/complete_text_10b_100m.schema.json',schema)
    write_json(RUN/'preflight.json',dict(status='frozen',parent_actual_lrs=[g['lr'] for g in parent['optimizer']['param_groups']],
        parent_sampler=parent['sampler'], plan_sha256=sha256(PLAN),GPU_training_started=False))
    print('Frozen three100M arms from final10B; no GPU work during freeze',flush=True)


def arm_binding(binding, plan, arm):
    return {**binding, 'arm':arm, 'short_manifest_sha256':plan['arms'][arm]['manifest_sha256']}


def train_arm(arm,parent,web,pool,plan,binding,heartbeat,check):
    directory = RUN/arm
    directory.mkdir(parents=True,exist_ok=True)
    terminal = directory/'result.json'
    if terminal.exists():
        saved = read_json(terminal)
        assert saved['status']=='complete' and saved['binding']==binding
        assert saved['checkpoint_sha256']==sha256(Path(saved['checkpoint']))
        return saved
    routes = pilot.routes(plan['updates_per_arm'],plan['arms'][arm]['short_updates'])
    schedule = dict(parent_update=parent['update'],stable_updates=2900,decay_updates=152)
    trainer = LowLRPilotTrainer(parent,web,pool,routes,schedule,binding)
    if (directory/'latest.json').exists():
        last = read_json(directory/'latest.json')
        assert sha256(Path(last['path']))==last['sha256']
        trainer.load(last['path'])
        metrics = directory/'metrics.jsonl'
        if metrics.exists():
            rows = [json.loads(line) for line in metrics.read_text().splitlines()]
            if rows and rows[-1]['update']>trainer.update:
                shutil.copyfile(metrics,directory/f'metrics-before-resume-{time.time_ns()}.jsonl')
                metrics.write_text(''.join(json.dumps(r)+'\n' for r in rows if r['update']<=trainer.update))
    prior = read_json(directory/'progress.json').get('training_seconds',0) if (directory/'progress.json').exists() else 0
    started = time.monotonic()
    with (directory/'metrics.jsonl').open('a',buffering=1) as log:
        while trainer.update<plan['final_update']:
            try: check()
            except (InterruptedError,TimeoutError):
                trainer.save(directory/f'checkpoint-{trainer.update:08d}.pt')
                raise
            row = trainer.step()
            row['arm']=arm
            log.write(json.dumps(row,allow_nan=False)+'\n')
            local = trainer.update-parent['update']
            if local==1 or local%100==0:
                heartbeat(arm+'-train',updates_completed=local,loss=row['loss'],tokens_per_second=row['tokens_per_second'])
                write_json(directory/'progress.json',dict(updates_completed=local,training_seconds=prior+time.monotonic()-started))
                print(json.dumps(row,allow_nan=False),flush=True)
            if local%500==0: trainer.save(directory/f'checkpoint-{trainer.update:08d}.pt')
    checkpoint = directory/f'checkpoint-{trainer.update:08d}.pt'
    trainer.save(checkpoint)
    expected_short=plan['arms'][arm]['short_updates']*32768
    assert trainer.tokens==plan['final_tokens'] and trainer.tokens-parent['tokens']==plan['tokens_per_arm']
    assert trainer.sampler.source_tokens=={'web':plan['tokens_per_arm']-expected_short,'short':expected_short}
    assert trainer.sampler.short.epoch==0
    result = dict(status='complete',binding=binding,checkpoint=str(checkpoint),checkpoint_sha256=sha256(checkpoint),
        update=trainer.update,tokens=trainer.tokens,additional_input_tokens=trainer.tokens-parent['tokens'],
        training_seconds=prior+time.monotonic()-started,source_tokens=trainer.sampler.source_tokens,
        source_eos_teachers=trainer.sampler.source_eos,sampler=trainer.sampler.state_dict(),
        initial_state='same final10B weights/Adam/RNG/Web cursor; explicit equal low-LR fork',
        learning_rate_fork=trainer.lineage['learning_rate_fork'])
    write_json(terminal,result)
    del trainer
    gc.collect(); torch.cuda.empty_cache()
    return result


def evaluate(arm,trained,dev,tok,plan,binding,heartbeat,check,deadline):
    output=RUN/arm/'evaluation'
    output.mkdir(parents=True,exist_ok=True)
    terminal=output/'result.json'
    if terminal.exists():
        saved=read_json(terminal)
        assert saved['binding']==binding and saved['checkpoint_sha256']==trained['checkpoint_sha256']
        return saved
    state=torch.load(trained['checkpoint'],map_location='cpu',weights_only=False)
    model=JMicroModel(state['model_config']).to('cuda').eval()
    model.load_state_dict(state['model'],strict=True)
    memory=bound_evaluation_cache(model)
    before=rng_state()
    # Every new task result is tied to this exact branch checkpoint.
    score_binding=json.dumps(dict(binding=binding,checkpoint_sha256=trained['checkpoint_sha256']),sort_keys=True)
    with sdpa_kernel(SDPBackend.MATH):
        body_path=output/'body.json'
        if body_path.exists():
            record=read_json(body_path); assert record['binding']==score_binding
            body=record['body']
        else:
            heartbeat(arm+'-dev256')
            body=evaluate_batched(model,dev,'cuda','bf16',limit=256,batch=16,
                progress=lambda done,total: heartbeat(arm+'-dev256',completed_tasks=done,total_tasks=total))
            write_json(body_path,dict(binding=score_binding,body=body))
        generation_path=output/'generation.json'
        if generation_path.exists():
            generated=read_json(generation_path); assert generated['binding']==score_binding
        else:
            heartbeat(arm+'-greedy80')
            generated=dict(binding=score_binding,outputs=pilot.greedy80(model,tok,heartbeat,check),
                           suite_sha256=plan['suite_sha256'],max_new_tokens=64)
            write_json(generation_path,generated)
        config=read_json(ROOT/plan['evaluation']['config'])
        tasks,controls=build_tasks(config)
        counts=np.bincount(np.fromfile(config['unigram_train'],dtype='<u2',count=2_000_000),minlength=4096).astype(float)
        counts[:8]=0; counts[8:]+=1
        unigram=np.log(np.maximum(counts,1e-300)/counts.sum())
        scorer=NativeLikelihood(model,tok,batch=16)
        diagnostics={}
        for name in plan['evaluation']['tasks']:
            check(); heartbeat(arm+'-'+name)
            diagnostics[name]=evaluate_choices(scorer,tasks[name],controls[name],unigram,output/(name+'.json'),score_binding,deadline,slor=name=='jblimp')
            assert diagnostics[name]['complete'],'Incomplete bounded task is not a complete comparison'
        families={}
        for row in read_json(output/'semantics.json')['rows']:
            families.setdefault(row['family'],[]).append(row['credit'])
        assert len(families)==96 and all(len(rows)==2 for rows in families.values())
        diagnostics['semantic_both_contexts']=dict(correct=sum(all(c==1 for c in rows) for rows in families.values()),
            total=len(families),fraction=sum(all(c==1 for c in rows) for rows in families.values())/len(families))
    assert pilot.equal_state(before,rng_state()),'Evaluation consumed training RNG'
    result=dict(binding=binding,checkpoint_sha256=trained['checkpoint_sha256'],body=body,generation=generated,
        greedy_rates=pilot.rate(generated['outputs']),diagnostics=diagnostics,memory=memory,
        evaluation_RNG_isolated=True,protected_test_used=False,completed_at=now())
    write_json(terminal,result)
    del model,state
    gc.collect(); torch.cuda.empty_cache()
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--freeze',action='store_true')
    args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7)
    torch.set_num_threads(2)
    if args.freeze: freeze(); return
    plan=read_json(PLAN)
    validate(plan,read_json(ROOT/'schemas/configs/phase6/complete_text_10b_100m.schema.json'))
    assert plan['implementation']==implementation_hashes()
    assert plan['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    assert plan['data_review_sha256']==sha256(RUN/'data-content-review.json')
    assert plan['tests_sha256']==sha256(RUN/'tests.xml')
    ev=plan['evaluation']
    assert ev['config_sha256']==sha256(ROOT/ev['config']) and ev['semantic_sha256']==sha256(ROOT/ev['semantic_suite'])
    assert ev['data_manifest_sha256']==sha256(Path('/home/aihub_ubuntu/jmicro-data/evaluation-v2/manifest.json'))
    binding=dict(plan_sha256=sha256(PLAN),parent=plan['parent'],peak_lr=plan['peak_lr'],implementation=plan['implementation'],source_sha256=plan['source_sha256'])
    job_path=RUN/'job.json'
    old=read_json(job_path) if job_path.exists() else {}
    if old:
        assert not alive(old),'Actual process is live; do not duplicate'
        assert old['binding']==binding
        if old['status']=='complete': print('Comparison GPU stage already complete; reuse saved results',flush=True); return
    stopped=[False]
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True))
    signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    prior=old.get('gpu_elapsed_seconds',0)
    start=[None]
    job=dict(status='starting',**identity(),binding=binding,gpu_elapsed_seconds=prior,started_at=old.get('started_at',now()),
             restart_command='scripts/run_complete_text_comparison.ps1 -Resume')
    def check():
        if stopped[0]: raise InterruptedError('Stop requested; completed checkpoint retained')
        if start[0] is not None and prior+time.monotonic()-start[0]>plan['gpu_budget_seconds']:
            raise TimeoutError('Cumulative1800s GPU budget exhausted; preserve incomplete results')
    def heartbeat(stage,**extra):
        check(); job.update(stage=stage,heartbeat_at=now(),**extra)
        if start[0] is not None: job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(job_path,job)
    try:
        heartbeat('setup')
        for p,digest in ((ROOT/plan['tokenizer'],plan['tokenizer_sha256']),(ROOT/'eval/base.jsonl',plan['suite_sha256']),
                         (Path(plan['parent']['path']),plan['parent']['sha256'])):
            assert sha256(p)==digest
        web=TrainView(plan['web_shards'],plan['web_manifest_sha256'])
        pools={arm:TrainView(detail['pool'],detail['manifest_sha256'],check_stream=True) for arm,detail in plan['arms'].items()}
        assert sha256(Path(plan['dev_shards'])/'manifest.json')==plan['dev_manifest_sha256']
        dev,tok=Shard(Path(plan['dev_shards']),'dev'),Tokenizer(ROOT/plan['tokenizer'])
        parent=torch.load(plan['parent']['path'],map_location='cpu',weights_only=False)
        source=RUN/'source'
        for relative in (*SOURCES,str(PLAN.relative_to(ROOT))):
            target=source/relative; target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists(): assert target.read_bytes()==(ROOT/relative).read_bytes()
            else: shutil.copyfile(ROOT/relative,target)
        seed_all(42); torch.use_deterministic_algorithms(True)
        with gpu_lock('cuda'):
            start[0]=time.monotonic(); deadline=start[0]+plan['gpu_budget_seconds']-prior
            heartbeat('resume-gate')
            pilot.PilotTrainer=LowLRPilotTrainer
            gate=pilot.exact_gate(parent,web,pools['coherent20'],arm_binding(binding,plan,'coherent20'),RUN,check)
            arms,screens={},{}
            for arm in plan['arms']:
                branch=arm_binding(binding,plan,arm)
                arms[arm]=train_arm(arm,parent,web,pools[arm],plan,branch,heartbeat,check)
                screens[arm]=evaluate(arm,arms[arm],dev,tok,plan,branch,heartbeat,check,deadline)
            checks={arm:adoption_checks(screens['web'],screens[arm]) for arm in ('short20','coherent20')}
            result=dict(status='GPU_stage_complete_pending_content_review',binding=binding,arms=arms,
                screen_rates={a:s['greedy_rates'] for a,s in screens.items()},
                screen_BPB={a:s['body']['bpb'] for a,s in screens.items()},mixture_checks=checks,
                diagnostics={a:s['diagnostics'] for a,s in screens.items()},resume_gate=gate,
                scientific_training_input_tokens=sum(a['additional_input_tokens'] for a in arms.values()),
                verification_training_input_tokens=gate['input_tokens'],
                GPU_seconds=prior+time.monotonic()-start[0],protected_test_used=False,v1_criteria_unchanged=True,
                full_evaluation='conditional on all frozen content and mixture gates; not run in screen stage',completed_at=now())
            assert result['scientific_training_input_tokens']==plan['scientific_total_tokens']
            write_json(RUN/'result.json',result)
            heartbeat('GPU-complete'); job.update(status='complete',completed_at=now())
            print(json.dumps(dict(status=result['status'],screen_BPB=result['screen_BPB'],rates=result['screen_rates'],mixture_checks=checks,GPU_seconds=result['GPU_seconds'])),flush=True)
    except BaseException as error:
        job.update(status='failed',error_type=type(error).__name__,error=str(error))
        raise
    finally:
        if start[0] is not None: job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(job_path,job)


if __name__=='__main__': main()
