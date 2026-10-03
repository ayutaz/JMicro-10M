"""Persistent Phase 5 supervisor and measured workers. Launch via uv."""
from pathlib import Path
import argparse
import copy
import fcntl
import hashlib
import json
import math
import os
import subprocess
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.model import JMicroModel
from jmicro.phase5 import bootstrap_bpb, common_windows, continuation_recall, equal_state, score_body
from jmicro.shards import Shard, build_shards
from jmicro.tokenizer import Tokenizer
from jmicro.training import Trainer, atomic_json, evaluate_body, generate_suite, gpu_lock, implementation_hashes, rng_state, seed_all, source_snapshot


def spec(plan, updates, context=None, lr=None):
    keys = ('seed','context','batch','accumulation','lr','weight_decay','warmup','dtype','compile','backend')
    result = {key: plan[key] for key in keys}
    result.update(schedule_updates=updates)
    if context is not None:
        result.update(context=context, batch=plan['overfit']['batch'], warmup=plan['overfit']['warmup'], sampler=plan['overfit']['sampler'])
    if lr is not None:
        result['lr'] = lr
    return result


def resume_worker(args):
    plan, c = read_json(args.plan), read_json(args.model)
    frozen = spec(plan, 200, context=plan['overfit']['context'] if args.mode == 'resume-overfit' else None)
    frozen['warmup'] = 20
    data = Shard(args.shards)
    args.output.mkdir(parents=True, exist_ok=True)
    continuous = Trainer(c, data, frozen, 'cuda')
    reference_losses, reference_digests = [], []
    for _ in range(200):
        row = continuous.step()
        reference_losses.append(row['loss']); reference_digests.append(row['token_digest'])
    continuous.save(args.output/'continuous.pt')
    del continuous
    torch.cuda.empty_cache()
    interrupted = Trainer(c, data, frozen, 'cuda')
    losses, digests = [], []
    for _ in range(100):
        row = interrupted.step(); losses.append(row['loss']); digests.append(row['token_digest'])
    interrupted.save(args.output/'at-100.pt')
    del interrupted
    torch.cuda.empty_cache()
    resumed = Trainer(c, data, frozen, 'cuda')
    resumed.load(args.output/'at-100.pt')
    for _ in range(100):
        row = resumed.step(); losses.append(row['loss']); digests.append(row['token_digest'])
    resumed.save(args.output/'resumed.pt')
    a = torch.load(args.output/'continuous.pt', map_location='cpu', weights_only=False)
    b = torch.load(args.output/'resumed.pt', map_location='cpu', weights_only=False)
    fields = ('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes','token_digest','implementation_sha256')
    checks = {field: equal_state(a[field],b[field]) for field in fields}
    checks.update(losses=reference_losses==losses, digests=reference_digests==digests)
    # Audit evaluation padding on this actual CUDA/BF16 model before long runs.
    dev = Shard(args.shards, 'dev')
    serial = evaluate_body(resumed.model, dev, 'cuda','bf16',limit=8)
    batched = score_body(resumed.model,dev,'cuda','bf16',limit=8)
    checks['batched_bytes_equal'] = serial['body_bytes']==batched['body_bytes']
    # BF16 kernel shape rounding is distinct from implementation correctness.
    checks['batched_bpb_parity'] = abs(serial['bpb']-batched['bpb']) <= 0.01
    if not all(checks.values()):
        write_json(args.output/'resume_report.json',dict(status='failed',checks=checks))
        raise ValueError(f'Resume/score checks failed: {checks}')
    write_json(args.output/'resume_report.json',dict(status='passed_exact', checks=checks,
        spec=frozen, tokens_per_run=a['tokens'], serial_bpb=serial['bpb'], batched_bpb=batched['bpb'],
        batched_bpb_tolerance=0.01, implementation_sha256=implementation_hashes(),
        checkpoints={p.name:sha256(p) for p in args.output.glob('*.pt')}))


def evaluation_worker(args):
    plan, c = read_json(args.plan), read_json(args.model)
    seed_all(plan['seed'])
    model = JMicroModel(c).cuda()
    state = None
    if args.checkpoint:
        state = torch.load(args.checkpoint,map_location='cpu',weights_only=False)
        if state['implementation_sha256'] != implementation_hashes():
            raise ValueError('Checkpoint source differs')
        if state['model_config'] != c or state['shard_manifest_sha256'] != sha256(args.shards/'manifest.json'):
            raise ValueError('Checkpoint model/data differs')
        model.load_state_dict(state['model'])
    tok = Tokenizer(args.tokenizer)
    if sha256(tok.path) != Shard(args.shards,'dev').manifest['tokenizer_sha256']:
        raise ValueError('Tokenizer differs')
    report = dict(status='passed',created_at=now(),model_config=c,
        checkpoint=str(args.checkpoint) if args.checkpoint else None,
        checkpoint_sha256=sha256(args.checkpoint) if args.checkpoint else None,
        tokens_seen=state['tokens'] if state else 0,
        body=score_body(model,Shard(args.shards,'dev'),'cuda','bf16'))
    if args.mode == 'overfit-eval':
        report['train'] = score_body(model,Shard(args.shards,'train'),'cuda','bf16',context=plan['overfit']['context'])
        report['continuation'] = continuation_recall(model,tok,Shard(args.shards,'train'),'cuda','bf16')
        train, thresholds = report['train'],plan['overfit']
        report['gates'] = dict(nll=train['nll_per_token']<=thresholds['max_nll_per_token'],
            teacher_accuracy=train['teacher_forced_accuracy']>=thresholds['min_teacher_accuracy'],
            continuation=report['continuation']['exact_rate']>=thresholds['min_continuation_exact_rate'],
            eos=train['eos_argmax_accuracy']>=thresholds['min_eos_argmax_accuracy'],
            eos_generation=report['continuation']['eos_generation_rate']>=thresholds['min_eos_argmax_accuracy'])
        report['status'] = 'passed' if all(report['gates'].values()) else 'failed'
    elif state:
        common, digest = common_windows(tok)
        report['common_windows'] = score_body(model,common,'cuda','bf16')
        report['common_windows']['text_manifest_sha256'] = digest
        if args.mode != 'budget-evaluate':
            report['generation'] = generate_suite(model,tok,'cuda','bf16',sampling=True)
    write_json(args.output,report)
    print(json.dumps({'status':report['status'],'bpb':report['body']['bpb'],
                      'train':{k:v for k,v in report.get('train',{}).items() if k!='rows'},
                      'continuation_exact_rate':report.get('continuation',{}).get('exact_rate')}),flush=True)
    if report['status']!='passed':
        raise ValueError('Overfit criteria failed; retain run and repair without lowering criteria')


def rates(report):
    rows=[r for r in report['generation']['outputs'] if r['suppressed'] and r['decoding']=='greedy']
    return dict(cases=len(rows), eos=sum(r['stop_reason']=='stop_id' for r in rows)/len(rows),
        unicode_failure=sum(not r['valid_utf8'] for r in rows)/len(rows),
        repetition=sum(r['repetition'] for r in rows)/len(rows),
        role_leak=sum(r['role_leak'] for r in rows)/len(rows),
        empty=sum(r['empty_response'] for r in rows)/len(rows))


def supervisor(args):
    run=args.output.resolve(); run.mkdir(parents=True,exist_ok=True)
    plan=read_json(args.plan)
    previous=read_json(run/'job.json') if (run/'job.json').exists() else None
    if (run/'plan.json').exists() and read_json(run/'plan.json') != plan:
        raise ValueError('Frozen Phase 5 plan differs')
    write_json(run/'plan.json',plan)
    if not (run/'snapshot').exists():
        source_snapshot(run/'snapshot')
    (run/'logs').mkdir(exist_ok=True)
    record=dict(status='running',phase=5,pid=os.getpid(),boot_id=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
        process_start_ticks=Path('/proc/self/stat').read_text().split()[21],started_at=now(),
        plan_sha256=sha256(args.plan),implementation_sha256=implementation_hashes(),
        completed_stages=previous.get('completed_stages',[]) if previous else [],active_stage=None,
        stop_boundary='Complete Phase 5; stop before Phase 6')
    if previous and previous['implementation_sha256']!=record['implementation_sha256']:
        raise ValueError('Supervisor source differs from frozen run')
    def execute(name,command):
        if name in record['completed_stages']:
            return
        record.update(active_stage=name); atomic_json(run/'job.json',record)
        print(json.dumps({'stage':name,'status':'started','at':now()}),flush=True)
        with (run/'logs'/f'{name}.log').open('a',buffering=1) as log:
            process=subprocess.Popen([sys.executable,*map(str,command)],cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
            record.update(child_pid=process.pid); atomic_json(run/'job.json',record)
            code=process.wait()
        if code:
            raise RuntimeError(f'Stage {name} failed with exit {code}; see log')
        record['completed_stages'].append(name)
        record.update(active_stage=None,child_pid=None); atomic_json(run/'job.json',record)
        print(json.dumps({'stage':name,'status':'passed','at':now()}),flush=True)
    def worker(name,mode,model,shards,tokenizer,output,checkpoint=None):
        command=[ROOT/'scripts/run_phase5.py','--mode',mode,'--plan',args.plan,'--model',model,
                 '--shards',shards,'--tokenizer',tokenizer,'--output',output]
        if checkpoint:
            command += ['--checkpoint',checkpoint]
        execute(name,command)
    def train(name,model,shards,updates,context=None,lr=None,split_at=None):
        directory=run/name
        s=spec(plan,updates,context,lr)
        command=[ROOT/'scripts/train.py','train','--phase','5','--model',model,'--shards',shards,'--output',directory,
                 '--device','cuda','--dtype',s['dtype'],'--context',str(s['context']),'--batch',str(s['batch']),
                 '--accumulation',str(s['accumulation']),'--seed',str(s['seed']),'--lr',str(s['lr']),
                 '--weight-decay',str(s['weight_decay']),'--warmup',str(s['warmup']),
                 '--schedule-updates',str(updates),'--save-every',str(plan['save_every']),'--log-every','500',
                 '--backend',s['backend']]
        if s['compile']: command.append('--compile')
        if s.get('sampler'): command += ['--sampler', s['sampler']]
        if directory.exists():
            latest=read_json(directory/'latest.json')
            if sha256(Path(latest['path']))!=latest['sha256']: raise ValueError('Invalid latest checkpoint')
            command+=['--resume',latest['path']]
        if split_at and f'{name}-first-half' not in record['completed_stages']:
            execute(f'{name}-first-half',[*command,'--stop-after',str(split_at)])
            latest=read_json(directory/'latest.json')
            command=[x for x in command]
            command+=['--resume',latest['path']]
        execute(name,command)
        return directory/f'checkpoint-{updates:08d}.pt'
    try:
        models={name:ROOT/f'configs/models/{name}.json' for name in ('t8k','t4k')}
        shards={name:Path.home()/f'jmicro-data/shards/{name}-pilot' for name in models}
        tokenizers={name:ROOT/f'artifacts/phase2/{size}/tokenizer.model' for name,size in (('t8k',8192),('t4k',4096))}
        for name in models:
            worker(f'resume-{name}','resume',models[name],shards[name],tokenizers[name],run/f'resume-{name}')
            worker(f'initial-{name}','evaluate',models[name],shards[name],tokenizers[name],run/f'initial-{name}.json')
        overfit=Path.home()/'jmicro-data/shards/t8k-overfit100'
        if not overfit.exists():
            build_shards(ROOT/'data/phase1/processed/corpus.jsonl',tokenizers['t8k'],overfit,plan['overfit']['documents_per_split'])
        worker('resume-overfit','resume-overfit',models['t8k'],overfit,tokenizers['t8k'],run/'resume-overfit')
        checkpoint=train('overfit-t8k',models['t8k'],overfit,plan['overfit']['updates'],context=plan['overfit']['context'])
        worker('overfit-evaluation','overfit-eval',models['t8k'],overfit,tokenizers['t8k'],run/'overfit_report.json',checkpoint)
        checkpoint=train('smoke-t8k',models['t8k'],shards['t8k'],plan['smoke_updates'],split_at=600)
        worker('smoke-evaluation','evaluate',models['t8k'],shards['t8k'],tokenizers['t8k'],run/'smoke_report.json',checkpoint)
        if read_json(run/'smoke_report.json')['body']['bpb']>=read_json(run/'initial-t8k.json')['body']['bpb']:
            raise ValueError('Smoke did not improve dev BPB')
        for name in models:
            checkpoint=train(f'100m-{name}',models[name],shards[name],plan['comparison_updates'])
            worker(f'evaluate-100m-{name}','evaluate',models[name],shards[name],tokenizers[name],run/f'100m-{name}.json',checkpoint)
        winner=min(models,key=lambda n:read_json(run/f'100m-{n}.json')['body']['bpb'])
        ablation=read_json(models[winner]); ablation.update(qk_norm_type='none',name=ablation['name']+'-NoQKNorm',
            expected_parameter_count=ablation['expected_parameter_count']-2*ablation['head_dim']*ablation['num_hidden_layers'],status='phase5_ablation')
        ablation_path=run/f'{winner}-no-qknorm.json'; write_json(ablation_path,ablation)
        worker('resume-no-qknorm','resume',ablation_path,shards[winner],tokenizers[winner],run/'resume-no-qknorm')
        checkpoint=train('100m-no-qknorm',ablation_path,shards[winner],plan['comparison_updates'])
        worker('evaluate-no-qknorm','evaluate',ablation_path,shards[winner],tokenizers[winner],run/'100m-no-qknorm.json',checkpoint)
        lr_model=ablation_path if read_json(run/'100m-no-qknorm.json')['body']['bpb']<read_json(run/f'100m-{winner}.json')['body']['bpb'] else models[winner]
        checkpoint=train('100m-lr001',lr_model,shards[winner],plan['comparison_updates'],lr=plan['selection']['lr_comparison'])
        worker('evaluate-lr001','evaluate',lr_model,shards[winner],tokenizers[winner],run/'100m-lr001.json',checkpoint)
        points = {}
        for name in ('t8k','t4k'):
            metrics=[json.loads(line) for line in (run/f'100m-{name}/metrics.jsonl').read_text().splitlines()]
            cumulative=np.cumsum([r['seconds'] for r in metrics])
            points[name]=[dict(checkpoint=p,body_bytes=metrics[int(p.stem.split('-')[-1])-1]['body_bytes_seen'],
                 training_seconds=float(cumulative[int(p.stem.split('-')[-1])-1])) for p in sorted((run/f'100m-{name}').glob('checkpoint-*.pt'))]
        for field in ('body_bytes','training_seconds'):
            target=min(points[name][-1][field] for name in points)*0.8
            for name in points:
                nearest=min(points[name],key=lambda p:abs(p[field]-target))
                worker(f'budget-{field}-{name}','budget-evaluate',models[name],shards[name],tokenizers[name],
                       run/f'budget-{field}-{name}.json',nearest['checkpoint'])
        summarize(run,plan,winner)
        record.update(status='complete',completed_at=now(),active_stage=None)
    except Exception as exc:
        record.update(status='failed',failure=f'{type(exc).__name__}: {exc}',completed_at=now())
        raise
    finally:
        atomic_json(run/'job.json',record)


def summarize(run,plan,winner):
    names=['100m-t8k','100m-t4k','100m-no-qknorm','100m-lr001']
    reports={name:read_json(run/f'{name}.json') for name in names}
    if len({r['common_windows']['text_manifest_sha256'] for r in reports.values()})!=1:
        raise ValueError('Common-window texts differ')
    entries={}
    for name, report in reports.items():
        directory=run/name
        metrics=[json.loads(line) for line in (directory/'metrics.jsonl').read_text().splitlines()]
        state=torch.load(report['checkpoint'],map_location='cpu',weights_only=False)
        assert len(metrics)==plan['comparison_updates'] and [r['update'] for r in metrics]==list(range(1,len(metrics)+1))
        assert all(math.isfinite(r[k]) for r in metrics for k in ('loss','gradient_norm','seconds','tokens_per_second'))
        assert all(torch.isfinite(w).all() for w in state['model'].values())
        assert all(torch.isfinite(v).all() for s in state['optimizer']['state'].values() for v in s.values() if isinstance(v,torch.Tensor))
        base='t8k' if state['model_config']['vocab_size']==8192 else 't4k'
        initial=read_json(run/f'initial-{base}.json')['body']['bpb']
        if report['body']['bpb']>=initial:
            raise ValueError(f'{name} did not improve dev BPB')
        cumulative=np.cumsum([r['seconds'] for r in metrics])
        checkpoints=[]
        for point in sorted(directory.glob('checkpoint-*.pt')):
            update=int(point.stem.split('-')[-1])
            row=metrics[update-1]
            checkpoints.append(dict(path=str(point),update=update,tokens=row['tokens_seen'],body_bytes=row['body_bytes_seen'],training_seconds=float(cumulative[update-1])))
        entries[name]=dict(bpb=report['body']['bpb'],initial_bpb=initial,common_bpb=report['common_windows']['bpb'],
            tokens=state['tokens'],body_bytes=state['body_bytes'],training_seconds=float(cumulative[-1]),
            cold_first_update_seconds=metrics[0]['seconds'],steady_tokens_per_second=float(np.median([r['tokens_per_second'] for r in metrics[1:]])),
            unique_train=Shard(Path.home()/f'jmicro-data/shards/{base}-pilot').manifest['splits']['train'],
            sampler=state['sampler'],generation_rates=rates(report),checkpoint=report['checkpoint'],checkpoint_sha256=report['checkpoint_sha256'],
            model_config=state['model_config'],spec=state['spec'],budget_points=checkpoints,
            loss_first100=float(np.mean([r['loss'] for r in metrics[:100]])),loss_last100=float(np.mean([r['loss'] for r in metrics[-100:]])))
    comparisons={f'{a}_vs_{b}':bootstrap_bpb(reports[a]['body'],reports[b]['body']) for a,b in [('100m-t8k','100m-t4k'),(f'100m-{winner}','100m-no-qknorm'),('100m-no-qknorm' if entries['100m-lr001']['model_config']['qk_norm_type']=='none' else f'100m-{winner}','100m-lr001')]}
    ranking=sorted(names,key=lambda name:entries[name]['bpb'])
    selected=[ranking[0]]
    # Retain the other tokenizer as a meaningful second long-run candidate only
    # when its paired interval includes zero against the best candidate.
    other='100m-t4k' if entries[ranking[0]]['model_config']['vocab_size']==8192 else '100m-t8k'
    uncertainty=bootstrap_bpb(reports[ranking[0]]['body'],reports[other]['body'])
    if uncertainty['ci95'][0]<=0<=uncertainty['ci95'][1]: selected.append(other)
    auxiliary={}
    for field in ('body_bytes','training_seconds'):
        target=min(entries[n][field] for n in ('100m-t8k','100m-t4k'))*0.8
        points={name:min(entries[name]['budget_points'],key=lambda p:abs(p[field]-target)) for name in ('100m-t8k','100m-t4k')}
        auxiliary[field]=dict(label='Approximate nearest saved checkpoint; not equal history or exact budget',target=target,points=points,
                              delta=points['100m-t8k'][field]-points['100m-t4k'][field],
                              dev_bpb={name:read_json(run/f'budget-{field}-{name}.json')['body']['bpb'] for name in ('t8k','t4k')})
    report=dict(status='passed',phase=5,created_at=now(),main_budget='100,007,936 stream tokens, seed 42, repeated pilot',
        entries=entries,paired_comparisons=comparisons,selected=selected,second_tokenizer_uncertainty=uncertainty,
        auxiliary_budget_matches=auxiliary,test_used=False,muon_decision='Deferred: stable AdamW comparisons suffice; no optimizer expansion in Phase 5',
        remaining='Phase 6 requires expanded corpus, long-run scheduler, and quality evaluation; no Phase 6 job launched')
    write_json(run/'tokenizer_model_comparison.json',report)
    lines=['# Phase 5 candidate selection','',f'Selected: {", ".join(selected)}. No test used; Phase 6 not started.','',
        '| Run | dev BPB | common-window BPB | steady tokens/s | greedy EOS |','|---|---:|---:|---:|---:|']
    for name in ranking:
        r=entries[name]; lines.append(f"| {name} | {r['bpb']:.6f} | {r['common_bpb']:.6f} | {r['steady_tokens_per_second']:.0f} | {r['generation_rates']['eos']:.1%} |")
    lines+=['','Selection prioritizes held-out common-byte BPB, then paired uncertainty, generation failures, speed and deployment constraints.',
        'Unselected runs remain recorded as measured alternatives. No-QK-Norm requires a separate HF/GGUF adapter; no native export compatibility claim.',
        '100M exposures repeat the small pilot; they do not establish scaling on 100M unique data. Auxiliary byte/time matches are approximate checkpoint budgets.',
        'Existing Base/Chat quality goals remain unchanged. Phase 5 mechanical success is not Japanese conversational quality success.',
        'Muon deferred because AdamW produced stable, improving candidates. For Phase 6, resolve scheduler extension and acquire the next required data, then validate before long training.']
    (run/'candidate_selection.md').write_text('\n'.join(lines)+'\n')
    (run/'candidates').mkdir(exist_ok=True)
    for name in selected:
        write_json(run/'candidates'/f'{name}.json',entries[name])
    overfit=read_json(run/'overfit_report.json'); smoke=read_json(run/'smoke_report.json')
    assert overfit['status']=='passed' and all(overfit['gates'].values())
    assert smoke['body']['bpb']<read_json(run/'initial-t8k.json')['body']['bpb']
    audit=dict(status='passed',phase=5,created_at=now(),gates=dict(overfit=overfit['gates'],smoke_dev_improvement=True,
        finite_all_comparison_updates=True,held_out_common_bytes=True,common_windows=True,fixed_dev_generation=True,
        exact_selected_backend_resume=all(read_json(run/f'resume-{n}/resume_report.json')['status']=='passed_exact' for n in ('t8k','t4k','overfit','no-qknorm')),
        candidate_selection=True,test_unused=True,phase6_not_started=True),
        evidence={p.name:sha256(p) for p in [run/'plan.json',run/'overfit_report.json',run/'smoke_report.json',run/'tokenizer_model_comparison.json',run/'candidate_selection.md']},
        implementation_sha256=implementation_hashes(),selected=selected)
    if not all(value if isinstance(value,bool) else all(value.values()) for value in audit['gates'].values()):
        raise ValueError('Phase 5 audit failed')
    write_json(run/'completion_audit.json',audit)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode',choices=['supervisor','resume','resume-overfit','evaluate','budget-evaluate','overfit-eval'],default='supervisor')
    parser.add_argument('--plan',type=Path,default=ROOT/'configs/phase5/plan.json')
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--model',type=Path)
    parser.add_argument('--shards',type=Path)
    parser.add_argument('--tokenizer',type=Path)
    parser.add_argument('--checkpoint',type=Path)
    args=parser.parse_args(); torch.set_num_threads(2)
    if args.mode=='supervisor':
        lock_root=Path.home()/'jmicro-data'; lock_root.mkdir(exist_ok=True)
        with (lock_root/'phase5-supervisor.lock').open('a+') as lock:
            fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
            supervisor(args)
    else:
        with gpu_lock('cuda'):
            if args.mode in ('resume','resume-overfit'): resume_worker(args)
            else: evaluation_worker(args)


if __name__=='__main__':
    main()
