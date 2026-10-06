"""Bounded readonly suffix likelihood with observed, cyclic and BOS contexts."""
import argparse
import gc
import hashlib
import json
import math
from pathlib import Path
import signal
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock
from natural_context_contrast_trainer import right_pad, right_padded_hidden
from phase6_performance import alive, identity
from run_natural_context_contrast_dev_transfer import RUN as PRIOR_RUN, CONFIG as PRIOR_CONFIG

RUN = ROOT / 'reports/phase6/natural-context-contrast-likelihood-transfer-20261007'
CONFIG = ROOT / 'configs/phase6/natural_context_contrast_likelihood_transfer.json'
PROPOSAL = ROOT / 'reports/phase6/natural_context_contrast_likelihood_transfer_proposal.json'
VIEWS = ('matched', 'cyclic', 'BOS_only')
SOURCES = ('scripts/run_natural_context_contrast_likelihood_transfer.py',
    'scripts/run_natural_context_contrast_likelihood_transfer.ps1',
    'scripts/natural_context_contrast_trainer.py', 'src/jmicro/model.py',
    'src/jmicro/tokenizer.py', 'uv.lock')


def tasks_for(rows, view, context=1024, stride=512):
    if view not in VIEWS or not 1 <= stride < context or len(rows) < 2:
        raise ValueError('Valid fixed context view/window geometry required')
    tasks = []
    for i, row in enumerate(rows):
        source = rows[i if view == 'matched' else (i+1) % len(rows)]
        prefix = [] if view == 'BOS_only' else source['prefix_ids']
        suffix = row['suffix_ids']
        if not suffix or any(t < 8 for t in prefix + suffix):
            raise ValueError('Original plain body tokens required')
        sequence = [2] + prefix + suffix
        base = len(prefix)+1
        for first in range(0, len(suffix), stride):
            last = min(first+stride, len(suffix))
            end = base+last
            start = max(0, end-context)
            inputs = sequence[start:end]
            targets = [-100]*len(inputs)
            lo, hi = base+first-start-1, end-start-1
            if not 0 <= lo < hi <= len(inputs):
                raise ValueError('One-shift suffix positions exceed current window')
            targets[lo:hi] = suffix[first:last]
            tasks.append(dict(row=i, suffix_first=first, suffix_last=last,
                original_input_start=start, input_ids=inputs, targets=targets,
                prefix_doc_id=None if view == 'BOS_only' else source['doc_id']))
    return tasks


def score_tasks(model, tasks, rows, view, device, check=lambda:None, batch=16):
    """Project only supervised native states; complete rolling suffix targets."""
    result = [dict(doc_id=r['doc_id'], body_tokens=len(r['suffix_ids']),
                   body_bytes=r['suffix_bytes'], nll=0., scored_tokens=0, windows=[])
              for r in rows]
    # Length bucketing changes physical padding only; original pair IDs remain fixed.
    ordered = sorted(tasks, key=lambda t:len(t['input_ids']))
    with torch.inference_mode(), sdpa_kernel(SDPBackend.MATH):
        for offset in range(0, len(ordered), batch):
            check()
            chosen = ordered[offset:offset+batch]
            ids, lengths = right_pad([t['input_ids'] for t in chosen], device)
            targets = torch.full(ids.shape, -100, dtype=torch.long)
            for i, task in enumerate(chosen):
                targets[i, :len(task['targets'])] = torch.tensor(task['targets'])
            positions = targets.ne(-100).nonzero()
            desired = targets[positions[:,0], positions[:,1]].to(device)
            selected = positions.to(device)
            with torch.autocast(torch.device(device).type, dtype=torch.bfloat16,
                                enabled=torch.device(device).type == 'cuda'):
                hidden = right_padded_hidden(model, ids)
                logits = model.lm_head(hidden[selected[:,0], selected[:,1]])
            loss = F.cross_entropy(logits.float(), desired, reduction='none')
            if not bool(torch.isfinite(loss).all()):
                raise ValueError('Nonfinite actual suffix NLL')
            sums = torch.zeros(len(chosen), device=device).index_add(0, selected[:,0], loss).cpu().tolist()
            for task, value in zip(chosen, sums, strict=True):
                record = result[task['row']]
                count = task['suffix_last']-task['suffix_first']
                record['nll'] += value
                record['scored_tokens'] += count
                record['windows'].append(dict(suffix_first=task['suffix_first'], suffix_last=task['suffix_last'],
                    original_input_start=task['original_input_start'], input_tokens=len(task['input_ids']),
                    prefix_doc_id=task['prefix_doc_id'], nll=value, scored_tokens=count))
            del hidden, logits, loss, ids
    if any(r['scored_tokens'] != r['body_tokens'] for r in result):
        raise ValueError('Every original suffix target must be evaluated exactly once')
    for record in result:
        record['windows'].sort(key=lambda w:w['suffix_first'])
    nll, byte_count = sum(r['nll'] for r in result), sum(r['body_bytes'] for r in result)
    return dict(view=view, rows=result, body_nll=nll, body_bytes=byte_count,
        body_tokens=sum(r['body_tokens'] for r in result),
        BPB=nll/(byte_count*math.log(2)), EOS_scored_positions=0,
        EOS_in_vocabulary_normalization=True, context=1024, target_stride=512)


def prepare():
    start = time.monotonic()
    if CONFIG.exists() or (RUN/'cases.json').exists():
        raise ValueError('Preserve one fixed diagnostic; no new draw')
    prior, proposal = read_json(PRIOR_CONFIG), read_json(PROPOSAL)
    job = read_json(PRIOR_RUN/'job.json')
    if job['status'] != 'complete' or alive(job):
        raise ValueError('Previous actual diagnostic must have exited')
    if (sha256(PRIOR_CONFIG) != proposal['references']['DEV64_config_sha256']
            or sha256(ROOT/'reports/phase6/natural_context_contrast_dev_transfer_review.json') !=
            proposal['references']['DEV64_review_sha256'] or proposal['GPU_seconds_limit'] != 60):
        raise ValueError('Documented frozen diagnostic source required')
    path = Path(prior['cases']['path'])
    if sha256(path) != prior['cases']['sha256']:
        raise ValueError('Frozen64 pairs differ')
    rows = read_json(path)['rows']
    if len(rows) != 64 or len({r['doc_id'] for r in rows}) != 64:
        raise ValueError('Same64 original pairs required')
    recipe = read_json(Path(prior['recipe']['path']))
    tok = Tokenizer(ROOT/recipe['tokenizer'])
    if sha256(tok.path) != recipe['tokenizer_sha256']:
        raise ValueError('Pinned tokenizer differs')
    for row in rows:
        if row['split'] != 'dev':
            raise ValueError('Only original DEV rows permitted')
        raw = tok.decode_bytes(row['suffix_ids'])
        raw.decode('utf-8')
        row['suffix_bytes'] = len(raw)
        row['suffix_sha256'] = hashlib.sha256(raw).hexdigest()
    for checkpoint in prior['checkpoints'].values():
        stat = Path(checkpoint['path']).stat()
        if (stat.st_size, stat.st_mtime_ns) != (checkpoint['size'], checkpoint['mtime_ns']):
            raise ValueError('Previously hash-verified checkpoint changed')
    tasks = {view:tasks_for(rows, view) for view in VIEWS}
    if time.monotonic()-start > 30:
        raise TimeoutError('Readonly preparation30s exhausted')
    RUN.mkdir(parents=True, exist_ok=True)
    atomic_json(RUN/'cases.json',dict(rows=rows))
    config = dict(created_at=now(), proposal=dict(path=str(PROPOSAL),sha256=sha256(PROPOSAL)),
        source_config=dict(path=str(PRIOR_CONFIG),sha256=sha256(PRIOR_CONFIG)),
        source_cases=prior['cases'], cases=dict(path=str(RUN/'cases.json'),sha256=sha256(RUN/'cases.json')),
        checkpoints=prior['checkpoints'], source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        pairs=64, views=VIEWS, context=1024, target_stride=512, batch=16,
        task_windows={v:len(t) for v,t in tasks.items()}, GPU_limit_seconds=60,
        CPU_preparation_seconds=time.monotonic()-start, new_teacher_tokens=0,optimizer_updates=0,
        protected_test_used=False,Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(CONFIG,config)
    print(json.dumps(dict(status='prepared',CPU_seconds=config['CPU_preparation_seconds'],windows=config['task_windows'])))


def inspect():
    c = read_json(CONFIG)
    for reference in (c['proposal'],c['source_config'],c['source_cases'],c['cases']):
        if sha256(Path(reference['path'])) != reference['sha256']:
            raise ValueError('Frozen source inputs differ')
    if any(sha256(ROOT/p) != digest for p,digest in c['source_sha256'].items()):
        raise ValueError('Frozen scoring code differs')
    for checkpoint in c['checkpoints'].values():
        stat = Path(checkpoint['path']).stat()
        if (stat.st_size,stat.st_mtime_ns) != (checkpoint['size'],checkpoint['mtime_ns']):
            raise ValueError('Previously verified checkpoint changed')
    if (RUN/'job.json').exists():
        raise ValueError('Preserve existing one-shot job; no retry or duplicate')
    previous = read_json(PRIOR_RUN/'job.json')
    if previous['status'] != 'complete' or alive(previous):
        raise ValueError('Previous actual process not terminal')
    return c


def run():
    c=inspect(); rows=read_json(Path(c['cases']['path']))['rows']
    tasks={view:tasks_for(rows,view) for view in VIEWS}
    job=dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),
        GPU_limit_seconds=60,GPU_occupancy_seconds=0,new_teacher_tokens=0,optimizer_updates=0,
        Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(RUN/'job.json',job)
    started=None; results={}
    def check():
        if started is not None and time.monotonic()-started >= 60:
            raise TimeoutError('Readonly likelihood60s budget exhausted')
    def deadline(*_):
        raise TimeoutError('Readonly likelihood hard60s deadline')
    signal.signal(signal.SIGALRM,deadline)
    try:
        with gpu_lock('cuda'):
            started=time.monotonic(); signal.alarm(60)
            if not torch.cuda.is_available():
                raise RuntimeError('CUDA unavailable; no CPU fallback')
            torch.cuda.set_per_process_memory_fraction(.90)
            for arm,checkpoint in c['checkpoints'].items():
                check()
                state=torch.load(checkpoint['path'],map_location='cpu',weights_only=False)
                with torch.random.fork_rng(devices=[]): model=JMicroModel(state['model_config']).to('cuda')
                model.load_state_dict(state['model'],strict=True); model.eval()
                if sum(p.numel() for p in model.parameters()) != 10001152:
                    raise ValueError('Original native10M required')
                results[arm]={}
                for view in VIEWS:
                    job.update(status='running',stage=f'{arm}-{view}',GPU_occupancy_seconds=time.monotonic()-started)
                    atomic_json(RUN/'job.json',job)
                    scored=score_tasks(model,tasks[view],rows,view,'cuda',check,batch=c['batch'])
                    check()
                    scored.update(checkpoint=checkpoint,input_cases_sha256=c['cases']['sha256'],dtype='bf16',backend='math')
                    atomic_json(RUN/f'{arm}-{view}.json',scored); results[arm][view]=scored
                del model,state
                gc.collect(); torch.cuda.empty_cache()
            check(); signal.alarm(0); elapsed=time.monotonic()-started
            report=dict(status='complete',created_at=now(),actual_identity=identity(),config_sha256=sha256(CONFIG),
                results=results,GPU_occupancy_seconds=elapsed,GPU_limit_seconds=60,new_teacher_tokens=0,optimizer_updates=0,
                protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
                quality_criteria_unchanged=True,limitations='Retrospective original DEV article association, not false factual labels or free-generation quality. Exactly64 paired suffixes across three context views; repeated directions/views are not independent cases.',
                next_action='Review same-target NLL/byte accounting and prefix benefit; close this one-shot without adopting a Base or automatically rescuing rejected training.')
            atomic_json(RUN/'result.json',report)
            job.update(status='complete',ended_at=now(),GPU_occupancy_seconds=elapsed)
            atomic_json(RUN/'job.json',job)
            print(json.dumps(dict(status='complete',GPU_seconds=elapsed,BPB={a:{v:s['BPB'] for v,s in views.items()} for a,views in results.items()})))
    except BaseException as error:
        signal.alarm(0)
        job.update(status='failed',ended_at=now(),error=repr(error),GPU_occupancy_seconds=time.monotonic()-started if started is not None else 0)
        atomic_json(RUN/'job.json',job)
        raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2)
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--prepare',action='store_true'); group.add_argument('--inspect',action='store_true')
    args=parser.parse_args()
    if args.prepare: prepare()
    elif args.inspect: inspect(); print('Frozen readonly likelihood diagnostic ready')
    else: run()
