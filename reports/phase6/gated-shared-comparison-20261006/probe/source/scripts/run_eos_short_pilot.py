"""Prepare and execute the frozen two-arm EOS pilot through uv in WSL."""
import argparse
import gc
import json
import os
from pathlib import Path
import re
import shutil
import signal
import sys
import time
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend

from jmicro.eos_pilot import TrainView, PilotTrainer, spans
from jmicro.experiment import ROOT, now, read_json, write_json, sha256
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.readiness import evaluate_batched
from jmicro.shards import Shard
from jmicro.tokenizer import SUPPRESS_IDS, Tokenizer
from jmicro.training import gpu_lock, implementation_hashes, generate_suite, isolated_evaluation
from phase6_performance import identity, alive


def sentence_complete(text):
    ending=text.rstrip().rstrip('」』）)"”’】〕〉》]').rstrip()
    if re.search(r'(?:\.{2,}|…|⋯)\s*[。！？.!?]*$',ending):
        return False
    if re.search(r'(?:続きを読む|続きはこちら|もっと見る|Read more)[。！？.!?\s]*$',ending):
        return False
    return ending.endswith(('。','！','？','.','!','?'))


def prepare(plan, tok, heartbeat, check):
    output = Path(plan['short_pool'])
    output.mkdir(parents=True, exist_ok=True)
    if (output / 'ready.json').exists():
        ready = read_json(output / 'ready.json')
        assert ready['source_manifest_sha256'] == plan['web_manifest_sha256']
        assert ready['selection'] == plan['short_selection']
        assert sha256(output / 'manifest.json') == ready['manifest_sha256']
        return ready
    started = time.monotonic()
    web = TrainView(plan['web_shards'], plan['web_manifest_sha256'])
    previous_end, count, total, byte_count, candidates = -1, 0, 0, 0, 0
    indexes, lengths, samples = [], [], []
    chunk_size = 16_000_000
    temporary = output / 'train.partial.bin'
    with temporary.open('wb') as stream:
        for offset in range(0, len(web.tokens), chunk_size):
            check()
            if time.monotonic() - started > plan['prepare_budget_seconds']:
                raise TimeoutError('Bounded short-document extraction exhausted')
            starts, ends, previous_end = spans(web.tokens[offset:offset + chunk_size], offset, previous_end)
            sizes = ends - starts - 1
            chosen = np.flatnonzero((sizes >= 32) & (sizes <= 128))
            for i in chosen:
                start, end, size = int(starts[i]), int(ends[i]), int(sizes[i])
                candidates += 1
                ids = web.tokens[start:end + 1]
                assert ids[0] == 2 and ids[-1] == 3 and bool((ids[1:-1] >= 8).all())
                text = tok.decode_bytes(ids[1:-1].tolist()).decode('utf-8')
                if not sentence_complete(text):
                    continue
                raw_bytes = len(text.encode('utf-8'))
                stream.write(ids.tobytes())
                indexes.append({'source_start': start, 'source_end': end, 'offset': total,
                                'body_tokens': size, 'bytes': raw_bytes, 'split': 'train'})
                lengths.append(size)
                if len(samples) < 8:
                    samples.append({'source_start': start, 'body_tokens': size, 'text': text})
                count += 1
                total += size + 2
                byte_count += raw_bytes
                if total >= plan['short_pool_minimum_tokens']:
                    break
            heartbeat('short-pool', scanned_tokens=min(offset + chunk_size, len(web.tokens)),
                      pool_documents=count, pool_tokens=total, extraction_seconds=time.monotonic() - started)
            if total >= plan['short_pool_minimum_tokens']:
                break
        stream.flush()
        os.fsync(stream.fileno())
    if total < plan['short_pool_minimum_tokens']:
        raise ValueError('Too few original short train documents; preserve partial pool and revise evidence-based plan')
    os.replace(temporary, output / 'train.bin')
    shutil.copyfile(web.directory / 'token_bytes.json', output / 'token_bytes.json')
    write_json(output / 'train.index.json', indexes)
    manifest = {'version': 1, 'dtype': '<u2', 'kind': 'web', 'vocab_size': tok.vocab_size,
        'tokenizer_sha256': plan['tokenizer_sha256'], 'token_bytes_sha256': sha256(output / 'token_bytes.json'),
        'packing': 'Original complete train BOS/body/EOS documents; no added truncation EOS',
        'source_manifest_sha256': plan['web_manifest_sha256'], 'selection': plan['short_selection'],
        'splits': {'train': {'tokens': total, 'documents': count, 'body_bytes': byte_count,
                            'stream_sha256': sha256(output / 'train.bin'),
                            'index_sha256': sha256(output / 'train.index.json')}}}
    write_json(output / 'manifest.json', manifest)
    ready = {'status': 'ready_train_only_short_pool', 'source_manifest_sha256': plan['web_manifest_sha256'],
             'manifest_sha256': sha256(output / 'manifest.json'), 'selection': plan['short_selection'],
             'documents': count, 'tokens': total, 'candidates_examined': candidates,
             'body_tokens_mean': float(np.mean(lengths)), 'body_tokens_min': min(lengths),
             'body_tokens_max': max(lengths), 'seconds': time.monotonic() - started, 'samples': samples,
             'heldout_used': False, 'source_membership': 'Slices only from the accepted train.bin; document boundaries retained',
             'content_limit': 'Sentence-final punctuation is a filter, not a human semantic-quality score'}
    assert ready['seconds'] <= plan['prepare_budget_seconds']
    write_json(output / 'ready.json', ready)
    return ready


def routes(count, short_count):
    return [(i + 1) * short_count // count > i * short_count // count for i in range(count)]


def exact_gate(parent, web, short, binding, output, check):
    path = output / 'resume-gate.json'
    if path.exists():
        result = read_json(path)
        assert result['passed'] and result['binding'] == binding
        return result
    gate_schedule = {'parent_update': parent['update'], 'stable_updates': 2, 'decay_updates': 2}
    gate_routes = [False, True, False, True]
    histories = []
    checkpoints = []
    started = time.monotonic()
    for mode in ('continuous', 'resumed'):
        trainer = PilotTrainer(parent, web, short, gate_routes, gate_schedule, binding)
        history = []
        for update in range(4):
            check()
            history.append(trainer.step())
            if mode == 'resumed' and update == 1:
                checkpoint = output / 'resume-gate' / 'split.pt'
                trainer.save(checkpoint)
                del trainer
                gc.collect()
                torch.cuda.empty_cache()
                trainer = PilotTrainer(parent, web, short, gate_routes, gate_schedule, binding)
                trainer.load(checkpoint)
        checkpoint = output / 'resume-gate' / f'{mode}.pt'
        trainer.save(checkpoint)
        histories.append(history)
        checkpoints.append(checkpoint)
        del trainer
        gc.collect()
        torch.cuda.empty_cache()
    states = [torch.load(p, map_location='cpu', weights_only=False) for p in checkpoints]
    keys = ('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes',
            'token_digest','spec','model_config','implementation_sha256','pilot_implementation_sha256',
            'pilot_binding','update','lineage')
    checks = {key: equal_state(states[0][key], states[1][key]) for key in keys}
    for key in ('loss','gradient_norm','lr','tokens_seen','supervised_tokens','body_bytes_seen','token_digest'):
        checks[f'history_{key}'] = [row[key] for row in histories[0]] == [row[key] for row in histories[1]]
    checks['finite_losses_gradients'] = all(np.isfinite(row['loss']) and np.isfinite(row['gradient_norm']) for h in histories for row in h)
    checks['two_short_two_web_updates'] = states[0]['sampler']['source_tokens'] == {'web':65536,'short':65536}
    result = {'passed': all(checks.values()), 'checks': checks, 'binding': binding,
              'seconds': time.monotonic() - started, 'GPU_optimizer_updates': 8, 'input_tokens': 262144,
              'histories': histories, 'schedule_scope': 'Real CUDA mixed routes, stable-to-decay boundary, optimizer/RNG/samplers',
              'checkpoints': [str(p) for p in checkpoints]}
    write_json(path, result)
    assert result['passed'], checks
    return result


def train_arm(arm, parent, web, short, plan, binding, output, heartbeat, check):
    directory = output / arm
    directory.mkdir(parents=True, exist_ok=True)
    terminal = directory / 'result.json'
    if terminal.exists():
        result = read_json(terminal)
        assert result['status'] == 'complete' and result['binding'] == binding
        return result
    count = plan['updates_per_arm']
    choice = routes(count, plan['short_updates'] if arm == 'short20' else 0)
    schedule = {'parent_update': parent['update'], 'stable_updates': plan['stable_updates'],
                'decay_updates': plan['decay_updates']}
    if arm=='web' and plan.get('reuse_completed_control'):
        source=Path(plan['reuse_completed_control']['result_path'])
        original=read_json(source)
        checkpoint=Path(original['checkpoint'])
        assert original['status']=='complete' and original['additional_input_tokens']==plan['tokens_per_arm']
        assert original['checkpoint_sha256']==plan['reuse_completed_control']['checkpoint_sha256']==sha256(checkpoint)
        saved=torch.load(checkpoint,map_location='cpu',weights_only=False)
        expected_spec=dict(parent['spec'])
        expected_spec.update(scheduler='wsd',schedule_updates=parent['update']+count,pilot_schedule=schedule)
        for key in ('branch_at','decay_updates','minimum_lr_ratio'):
            expected_spec.pop(key,None)
        assert saved['spec']==expected_spec and saved['implementation_sha256']==binding['implementation']
        assert saved['pilot_implementation_sha256']==binding['module_sha256']
        assert saved['pilot_binding']['parent']==binding['parent']
        assert saved['tokens']-parent['tokens']==plan['tokens_per_arm'] and saved['update']==parent['update']+count
        assert not any(saved['sampler']['routes']) and saved['sampler']['position']==count
        assert saved['sampler']['source_tokens']=={'web':plan['tokens_per_arm'],'short':0}
        assert saved['sampler']['short']['position']==0 and saved['sampler']['source_eos']['short']==0
        result={**original,'binding':binding,'stored_checkpoint_binding':saved['pilot_binding'],
                'reused_control':{'source_result':str(source),'no_short_input_ever_used':True,
                    'same_parent_Web_module_schedule_verified':True,
                    'reason':'Short selection tightened before treatment; completed Web control is unchanged and reused without retraining.'}}
        write_json(terminal,result)
        del saved
        return result
    trainer = PilotTrainer(parent, web, short, choice, schedule, binding)
    latest = directory / 'latest.json'
    if latest.exists():
        saved = read_json(latest)
        assert sha256(Path(saved['path'])) == saved['sha256']
        trainer.load(saved['path'])
        metrics = directory / 'metrics.jsonl'
        if metrics.exists():
            rows = [json.loads(line) for line in metrics.read_text().splitlines()]
            if rows and rows[-1]['update'] > trainer.update:
                shutil.copyfile(metrics, directory / f'metrics-before-resume-{time.time_ns()}.jsonl')
                metrics.write_text(''.join(json.dumps(r)+'\n' for r in rows if r['update'] <= trainer.update))
    elapsed_before = read_json(directory / 'progress.json').get('training_seconds', 0) if (directory / 'progress.json').exists() else 0
    started = time.monotonic()
    with (directory / 'metrics.jsonl').open('a', buffering=1) as log:
        while trainer.update < trainer.spec['schedule_updates']:
            try:
                check()
            except (InterruptedError, TimeoutError):
                trainer.save(directory / f'checkpoint-{trainer.update:08d}.pt')
                raise
            row = trainer.step()
            row['arm'] = arm
            log.write(json.dumps(row, allow_nan=False) + '\n')
            local = trainer.update - parent['update']
            if local % 25 == 0 or local == 1:
                heartbeat(arm, updates_completed=local, loss=row['loss'], tokens_per_second=row['tokens_per_second'])
                write_json(directory / 'progress.json', {'training_seconds': elapsed_before + time.monotonic() - started,
                           'updates_completed': local, 'sampler': trainer.sampler.state_dict()})
                print(json.dumps(row, allow_nan=False), flush=True)
            if local % 200 == 0:
                trainer.save(directory / f'checkpoint-{trainer.update:08d}.pt')
    checkpoint = directory / f'checkpoint-{trainer.update:08d}.pt'
    trainer.save(checkpoint)
    sources = trainer.sampler.source_tokens
    assert trainer.tokens - parent['tokens'] == plan['tokens_per_arm'] == sum(sources.values())
    assert sources['short'] == (plan['short_updates'] if arm == 'short20' else 0) * 32768
    assert trainer.sampler.short.epoch == 0
    result = {'status':'complete','binding':binding,'checkpoint':str(checkpoint), 'checkpoint_sha256':sha256(checkpoint),
        'update':trainer.update, 'tokens':trainer.tokens, 'additional_input_tokens':trainer.tokens-parent['tokens'],
        'training_seconds':elapsed_before + time.monotonic()-started, 'source_tokens':dict(sources),
        'source_eos_teachers':dict(trainer.sampler.source_eos), 'sampler':trainer.sampler.state_dict(),
        'initial_state':'Same2B model/Adam moments/RNG/web cursor; explicit equal peak-LR pilot fork, not ordinary resume'}
    write_json(terminal, result)
    del trainer
    gc.collect()
    torch.cuda.empty_cache()
    return result


def rate(rows):
    return {'outputs':len(rows), 'eos':sum(r['stop_reason']=='stop_id' for r in rows),
        'repetition':sum(r['repetition'] for r in rows), 'unicode_failure':sum(not r['valid_utf8'] for r in rows),
        'role_leak':sum(r['role_leak'] for r in rows), 'empty':sum(r['empty_response'] for r in rows)}


@torch.inference_mode()
def greedy80(model, tok, heartbeat, check, limit=80):
    cases = [json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text(encoding='utf-8').splitlines()]
    cases = [case for case in cases if case['split']=='dev']
    assert len(cases)==80
    cases=cases[:limit]
    rows = []
    with isolated_evaluation(model):
        for case in cases:
            ids, cache = [], None
            current = torch.tensor([[2,*tok.encode(case['prefix'])]], device='cuda')
            for _ in range(64):
                check()
                with torch.autocast('cuda', dtype=torch.bfloat16):
                    result = model(current, cache=cache, use_cache=True)
                cache = result.cache
                scores = result.logits[0,-1].clone()
                assert bool(torch.isfinite(scores).all())
                scores[list(SUPPRESS_IDS)] = -torch.inf
                token = int(scores.argmax())
                ids.append(token)
                if token == 3:
                    break
                current = torch.tensor([[token]], device='cuda')
            raw = tok.decode_bytes(ids)
            try:
                text, valid = raw.decode('utf-8'), True
            except UnicodeDecodeError:
                text, valid = raw.decode('utf-8', errors='replace'), False
            rows.append({'id':case['id'],'category':case['category'],'prefix':case['prefix'],
                'split':'dev','decoding':'greedy','suppressed':True,'seed':42,'generated_ids':ids,
                'text':text,'valid_utf8':valid,'role_leak':any(i in (4,5,6,7) for i in ids),
                'empty_response':not text.strip(),'stop_reason':'stop_id' if ids[-1]==3 else 'max_new_tokens',
                'repetition':bool(re.search(r'(.{2,}?)\1\1',text,flags=re.DOTALL))})
            if len(rows)%8==0:
                heartbeat('generation80', completed_cases=len(rows))
    return rows


def evaluate_checkpoint(checkpoint, dev, tok, output, heartbeat, check, full=False):
    if output.exists():
        result=read_json(output)
        assert result['checkpoint']==str(checkpoint) and result['full']==full
        return result
    state=torch.load(checkpoint,map_location='cpu',weights_only=False)
    model=JMicroModel(state['model_config']).to('cuda')
    model.load_state_dict(state['model'],strict=True)
    model.eval()
    def progress(done,total):
        check()
        if done==total or done%1024==0:
            heartbeat('full-dev' if full else 'dev256', completed_tasks=done, total_tasks=total)
    with sdpa_kernel([SDPBackend.MATH]):
        body=evaluate_batched(model,dev,'cuda','bf16',limit=None if full else 256,batch=16,progress=progress)
        check()
        if full:
            generation=generate_suite(model,tok,'cuda','bf16',limit=80,max_new=64,sampling=True)
            rows=generation['outputs']
        else:
            rows=greedy80(model,tok,heartbeat,check)
            generation={'max_new_tokens':64,'outputs':rows,'suite_sha256':sha256(ROOT/'eval/base.jsonl')}
    result={'checkpoint':str(checkpoint),'checkpoint_sha256':sha256(checkpoint),'full':full,
            'body':body,'generation':generation,'greedy_rates':rate([r for r in rows if r['decoding']=='greedy' and r['suppressed']]),
            'completed_at':now()}
    write_json(output,result)
    del model,state
    gc.collect()
    torch.cuda.empty_cache()
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan',type=Path,default=ROOT/'configs/phase6/eos_short_pilot.json')
    args=parser.parse_args()
    plan=read_json(args.plan)
    output=ROOT/plan['output']
    output.mkdir(parents=True,exist_ok=True)
    job_path=output/'job.json'
    old=read_json(job_path) if job_path.exists() else {}
    if old and alive(old):
        raise RuntimeError('Identified pilot process still live; do not duplicate')
    binding={'plan_sha256':sha256(args.plan),'parent':plan['parent'],
             'module_sha256':sha256(ROOT/'src/jmicro/eos_pilot.py'),
             'runner_sha256':sha256(Path(__file__)),'implementation':implementation_hashes(),
             'evaluation_sha256':sha256(ROOT/'src/jmicro/readiness.py')}
    if old:
        assert old['binding']==binding, 'Preserve old run: source/config changed'
        if old['status']=='complete':
            print('Pilot already complete; not rerunning',flush=True)
            return
    job={'status':'running',**identity(),'started_at':old.get('started_at',now()),'binding':binding,
         'restart_command':'bash scripts/run_eos_short_pilot.sh','stage':'setup',
         'gpu_elapsed_seconds':old.get('gpu_elapsed_seconds',plan.get('retired_gpu_elapsed_seconds',0))}
    stopped=[False]
    signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True))
    gpu_start=[None]
    previous_gpu=job['gpu_elapsed_seconds']
    def check():
        if stopped[0]:
            raise InterruptedError('Stop requested; completed-update checkpoint preserved')
        if gpu_start[0] is not None and previous_gpu+time.monotonic()-gpu_start[0]>plan['gpu_budget_seconds']:
            raise TimeoutError('Cumulative pilot GPU budget exhausted')
    def heartbeat(stage,**values):
        job.update(stage=stage,heartbeat_at=now(),**values)
        if gpu_start[0] is not None:
            job['gpu_elapsed_seconds']=previous_gpu+time.monotonic()-gpu_start[0]
        write_json(job_path,job)
    heartbeat('setup')
    try:
        torch.set_num_threads(2)
        assert sha256(ROOT/plan['tokenizer'])==plan['tokenizer_sha256']
        assert sha256(ROOT/'eval/base.jsonl')==plan['suite_sha256']
        accepted=read_json(ROOT/'reports/phase6/corpus_10b_loader_ready.json')
        assert accepted['status']=='passed_actual_training_loader' and accepted['shard_manifest_sha256']==plan['web_manifest_sha256']
        assert accepted['validation_scope']=='built_export_and_actual_train_loader'
        tests={k:0 for k in ('tests','failures','errors','skipped')}
        for suite in ET.parse(output/'tests.xml').getroot().iter('testsuite'):
            for key in tests:
                tests[key]+=int(suite.attrib.get(key,0))
        assert tests['tests']>0 and not any(tests[k] for k in ('failures','errors','skipped'))
        tok=Tokenizer(ROOT/plan['tokenizer'])
        ready=prepare(plan,tok,heartbeat,check)
        web=TrainView(plan['web_shards'],plan['web_manifest_sha256'])
        short=TrainView(plan['short_pool'],ready['manifest_sha256'],check_stream=True)
        parent_path=Path(plan['parent']['path'])
        assert sha256(parent_path)==plan['parent']['sha256']
        parent_stat=(parent_path.stat().st_size,parent_path.stat().st_mtime_ns)
        parent=torch.load(parent_path,map_location='cpu',weights_only=False)
        assert parent['tokens']==2000027648 and parent['update']==61036
        assert (parent['spec']['batch'],parent['spec']['context'],parent['spec']['accumulation'])==(32,1024,1)
        binding['short_manifest_sha256']=ready['manifest_sha256']
        # Keep job binding stable across resume: pool evidence has its own record.
        trainer_binding=dict(binding)
        job['binding'].pop('short_manifest_sha256',None)
        with gpu_lock('cuda'):
            gpu_start[0]=time.monotonic()
            heartbeat('resume-gate')
            gate=exact_gate(parent,web,short,trainer_binding,output,check)
            baseline_check_path=output/'generation-baseline-check.json'
            if not baseline_check_path.exists():
                model=JMicroModel(parent['model_config']).to('cuda')
                model.load_state_dict(parent['model'],strict=True)
                with sdpa_kernel([SDPBackend.MATH]):
                    reproduced=greedy80(model,tok,heartbeat,check,limit=8)
                saved=read_json(ROOT/'reports/phase6/base-2b-10bdata-20261004/evaluation-2B/generation.json')['generation']['outputs']
                equal_ids={r['id']:r['generated_ids']==next(s['generated_ids'] for s in saved if s['id']==r['id'] and s['decoding']=='greedy' and s['suppressed']) for r in reproduced}
                assert all(equal_ids.values())
                write_json(baseline_check_path,{'binding':trainer_binding,'checks':equal_ids,'passed':True})
                del model
                gc.collect()
                torch.cuda.empty_cache()
            else:
                assert read_json(baseline_check_path)['passed'] and read_json(baseline_check_path)['binding']==trainer_binding
            arms={}
            evaluation={}
            dev=Shard(Path(plan['dev_shards']),'dev')
            for arm in ('web','short20'):
                heartbeat(arm)
                arms[arm]=train_arm(arm,parent,web,short,plan,trainer_binding,output,heartbeat,check)
                heartbeat(f'{arm}-evaluation')
                evaluation[arm]=evaluate_checkpoint(Path(arms[arm]['checkpoint']),dev,tok,output/f'{arm}-evaluation.json',heartbeat,check)
            control,treatment=evaluation['web'],evaluation['short20']
            a,b=control['greedy_rates'],treatment['greedy_rates']
            checks={'EOS_at_least8_more':b['eos']>=a['eos']+8,
                    'repetition_no_worse':b['repetition']<=a['repetition'],
                    'no_empty_role_unicode':all(b[k]==0 for k in ('empty','role_leak','unicode_failure')),
                    'BPB_degradation_at_most1percent':treatment['body']['bpb']<=control['body']['bpb']*1.01}
            promising=all(checks.values())
            full=None
            if promising:
                heartbeat('candidate-full-evaluation')
                full=evaluate_checkpoint(Path(arms['short20']['checkpoint']),dev,tok,output/'candidate-full-evaluation.json',heartbeat,check,full=True)
                old_full=read_json(ROOT/'reports/phase6/base-2b-10bdata-20261004/evaluation-2B/full-dev.json')['body']
                checks['full_dev_BPB_no_more_than1percent_vs2B']=full['body']['bpb']<=old_full['bpb']*1.01
                checks['full_generation_matches_screen']=full['greedy_rates']==b
                full_greedy=[r for r in full['generation']['outputs'] if r['decoding']=='greedy' and r['suppressed']]
                checks['full_generated_ids_match_screen']=all(left['id']==right['id'] and left['generated_ids']==right['generated_ids'] for left,right in zip(full_greedy,treatment['generation']['outputs'],strict=True))
                promising=all(checks.values())
            assert parent_stat==(parent_path.stat().st_size,parent_path.stat().st_mtime_ns)
            heartbeat('review')
            summary={'status':'completed_two_arm_eos_improvement_comparison','completed_at':now(),
                'plan':plan,'binding':trainer_binding,'short_pool':ready,'tests':tests,'resume_gate':gate,
                'arms':arms,'screening':{k:{'greedy_rates':v['greedy_rates'],
                    'dev_documents':v['body']['documents'],'dev_body_bytes':v['body']['body_bytes'],
                    'dev_bpb':v['body']['bpb'],'mean_eos_nll':v['body']['eos_nll']/v['body']['documents']} for k,v in evaluation.items()},
                'improvement_checks':checks,'improvement_gate_passed':promising,
                'candidate_full_evaluation_performed':full is not None,
                'candidate_full_evaluation':None if full is None else {'bpb':full['body']['bpb'],'greedy_rates':full['greedy_rates']},
                'scientific_training_input_tokens':sum(a['additional_input_tokens'] for a in arms.values()),
                'verification_training_input_tokens':gate['input_tokens']+plan.get('retired_gate_input_tokens',0),
                'gpu_elapsed_seconds':job['gpu_elapsed_seconds'],
                'parent_checkpoint_stat_unchanged':True,'test_split_used':False,
                'quality_targets_achieved':False,
                'decision':'Promising short-mixture pilot; original Base/Chat acceptance still unmet' if promising else 'Short20 mixture not adopted: frozen improvement gate failed; no5B/Chat launched',
                'raw_run':str(output)}
            write_json(output/'review.json',summary)
            write_json(ROOT/'reports/phase6/eos_short_pilot_review.json',summary)
            job.update(status='complete',completed_at=now(),result=str(output/'review.json'))
    except BaseException as exc:
        job.update(status='interrupted' if isinstance(exc,InterruptedError) else 'failed',
                   failure=f'{type(exc).__name__}: {exc}',finished_at=now())
        raise
    finally:
        if gpu_start[0] is not None:
            job['gpu_elapsed_seconds']=previous_gpu+time.monotonic()-gpu_start[0]
        write_json(job_path,job)


if __name__=='__main__':
    main()
