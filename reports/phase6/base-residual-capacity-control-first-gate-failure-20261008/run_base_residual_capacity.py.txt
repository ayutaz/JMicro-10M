"""Bounded six-original-TRAIN positive learning control; never a Base candidate."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json, gpu_lock, isolated_evaluation, restore_rng, rng_state, seed_all, synchronize
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer, SUPPRESS_IDS
from base_parallel_residual_model import model_from_config
from natural_context_contrast_trainer import host, right_pad, right_padded_hidden
from phase6_performance import alive, identity, finite_state

PHASE = ROOT / 'reports/phase6'
RUN = PHASE / 'base-residual-capacity-control-20261008'
CONFIG = ROOT / 'configs/phase6/base_residual_capacity_control.json'
OUTPUT = PHASE / 'base_residual_capacity_control.json'
KIND = 'six_original_TRAIN_sequential2B_capacity_control_only_v1'
CAP = 3000000


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def checked(value):
    path = Path(value['path'])
    if sha256(path) != value['sha256']:
        raise ValueError('Frozen reference differs: ' + str(path))
    return read_json(path)


def validate_rows(rows):
    if len(rows) != 6 or len({r['id'] for r in rows}) != 6:
        raise ValueError('Exactly six original units required')
    for r in rows:
        x, y = r['input_ids'], r['gold_targets']
        if (x[0] != 2 or len(x) != len(y) or x[1:] != y[:-1] or y[-1] != 3
                or any(i < 8 for i in y[:-1]) or len(x) >= 1024
                or r['teacher_tokens'] != len(y)
                or r['prompt_ids'] != x[:len(r['prompt_ids'])]
                or r['continuation_gold_ids'] != y[len(r['prompt_ids'])-1:]):
            raise ValueError('Original whole-unit shift/EOS/prefix differs')


def conflicting_histories(rows):
    histories = {}
    for row in rows:
        for i,target in enumerate(row['gold_targets']):
            key=tuple(row['input_ids'][:i+1])
            histories.setdefault(key,[]).append((row['id'],i,target))
    conflicts=[]
    for key,positions in histories.items():
        counts={v:sum(p[2]==v for p in positions) for v in {p[2] for p in positions}}
        if len(counts)>1:
            conflicts.append(dict(input_history=list(key),positions=positions,
                unavoidable_argmax_errors=len(positions)-max(counts.values())))
    return conflicts


def pack(rows, cursor, batch, remaining, device):
    """Cycle original units, masking only trailing gold at a partial final update."""
    if remaining <= 0:
        raise ValueError('Positive remaining teacher budget required')
    chosen = [rows[(cursor + i) % len(rows)] for i in range(batch)]
    ids, _ = right_pad([r['input_ids'] for r in chosen], device)
    targets = torch.full_like(ids, -100)
    used, eos, body_bytes, by_source, draws = 0, 0, 0, {}, []
    for i, row in enumerate(chosen):
        count = min(len(row['gold_targets']), remaining-used)
        if count:
            gold = row['gold_targets'][:count]
            targets[i, :count] = torch.tensor(gold, device=device)
            used += count
            eos += int(gold[-1] == 3)
            # Byte counts are recorded for full original bodies only. Partial
            # final units are explicit and never counted as full body exposure.
            if count == len(row['gold_targets']):
                body_bytes += len(bytes.fromhex(row['actual_first_window_body_bytes_hex']))
            by_source[row['source']] = by_source.get(row['source'], 0) + count
        draws.append((row['id'], count))
    return ids, targets, dict(supervised_tokens=used, EOS_targets=eos,
        completed_original_body_bytes=body_bytes, source_teacher_tokens=by_source,
        CE_input_tokens=sum(len(r['input_ids']) for r in chosen),
        physical_input_tokens=ids.numel(), draws=draws), cursor+batch


class Trainer:
    def __init__(self, parent, rows, binding, device='cuda', batch=80):
        validate_rows(rows)
        self.device, self.rows, self.binding = torch.device(device), rows, binding
        self.spec = dict(kind=KIND, batch=batch, seed=42, lr=.0002, weight_decay=.1,
                         betas=(.9,.999), eps=1e-8, clip=1., schedule='constant')
        seed_all(42)
        self.model = model_from_config(parent['model_config']).to(self.device).train()
        self.model.load_state_dict(parent['model'], strict=True)
        self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=.0002,
                                         betas=(.9,.999), eps=1e-8, weight_decay=.1)
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lambda _: 1.)
        self.cursor = 0
        self.counters = dict(update=0, supervised_tokens=0, EOS_targets=0,
            completed_original_body_bytes=0, CE_input_tokens=0, physical_input_tokens=0,
            source_teacher_tokens={}, token_digest='0'*64)

    def step(self, remaining=CAP):
        ids, targets, stats, next_cursor = pack(self.rows, self.cursor, self.spec['batch'], remaining, self.device)
        self.optimizer.zero_grad(set_to_none=True)
        valid = targets != -100
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        with sdpa_kernel(backend), torch.autocast(self.device.type, dtype=torch.bfloat16,
                                                enabled=self.device.type == 'cuda'):
            hidden = right_padded_hidden(self.model, ids)
            logits = self.model.lm_head(hidden[valid]).float()
            loss = F.cross_entropy(logits, targets[valid])
            if not bool(torch.isfinite(loss)):
                raise ValueError('Nonfinite original gold loss')
            loss.backward()
        norm = torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1., error_if_nonfinite=True)
        self.optimizer.step(); self.scheduler.step()
        self.cursor = next_cursor
        self.counters['update'] += 1
        for key in ('supervised_tokens','EOS_targets','completed_original_body_bytes','CE_input_tokens','physical_input_tokens'):
            self.counters[key] += stats[key]
        for key,value in stats['source_teacher_tokens'].items():
            src = self.counters['source_teacher_tokens']
            src[key] = src.get(key,0) + value
        payload = json.dumps(stats['draws']).encode()
        self.counters['token_digest'] = hashlib.sha256(bytes.fromhex(self.counters['token_digest']) + payload).hexdigest()
        synchronize(self.device)
        return dict(counters=host(self.counters), draws=stats['draws'], targets_this_update=stats['supervised_tokens'],
                    loss=float(loss.detach()), gradient_norm=float(norm), lr=self.optimizer.param_groups[0]['lr'])

    def state(self):
        return host(dict(kind=KIND, model_config=self.model.config, spec=self.spec, binding=self.binding,
            model=self.model.state_dict(), optimizer=self.optimizer.state_dict(), scheduler=self.scheduler.state_dict(),
            RNG=rng_state(), cursor=self.cursor, counters=self.counters))

    def save(self, path):
        state = self.state()
        if not finite_state(state):
            raise ValueError('Nonfinite committed model/optimizer state')
        temporary = path.with_suffix('.tmp')
        torch.save(state, temporary); temporary.replace(path)
        return state

    def load(self, path):
        state = torch.load(path, map_location='cpu', weights_only=False)
        for key in ('kind','model_config','spec','binding'):
            if state[key] != self.state()[key]:
                raise ValueError('Resume recipe/source differs')
        self.model.load_state_dict(state['model'], strict=True)
        self.optimizer.load_state_dict(state['optimizer']); self.scheduler.load_state_dict(state['scheduler'])
        self.cursor, self.counters = state['cursor'], host(state['counters'])
        restore_rng(state['RNG'])


def resume_gate(parent, rows, binding, check):
    a = Trainer(parent,rows,binding)
    history_a = []
    for _ in range(4):
        check(); history_a.append(a.step())
    state_a = a.state()
    del a; torch.cuda.empty_cache()
    b = Trainer(parent,rows,binding)
    history_b = []
    for _ in range(2):
        check(); history_b.append(b.step())
    b.save(RUN / 'resume-gate.pt')
    del b; torch.cuda.empty_cache()
    b = Trainer(parent,rows,binding); b.load(RUN / 'resume-gate.pt')
    for _ in range(2):
        check(); history_b.append(b.step())
    state_b = b.state()
    checks = {key:equal_state(state_a[key],state_b[key]) for key in state_a}
    checks['history'] = equal_state(history_a,history_b)
    checks['finite'] = finite_state(state_a) and finite_state(state_b)
    result = dict(checks=checks, passed=all(checks.values()), history_continuous=history_a,
        history_resumed=history_b, verification_updates=8,
        verification_teacher_tokens=2*state_a['counters']['supervised_tokens'], probe_weights_discarded=True)
    atomic_json(RUN/'resume-gate.json',result)
    if not result['passed']:
        raise ValueError('Own actual CUDA continuous4 vs2+save+2 failed')
    del b; torch.cuda.empty_cache()
    return result


@torch.inference_mode()
def accuracy(model, rows, check):
    result=[]
    with isolated_evaluation(model), sdpa_kernel(SDPBackend.MATH):
        for row in rows:
            check()
            x=torch.tensor([row['input_ids']],device=next(model.parameters()).device)
            with torch.autocast(x.device.type,dtype=torch.bfloat16,enabled=x.device.type=='cuda'):
                logits=model(x).logits[0].float()
            if not bool(torch.isfinite(logits).all()):
                raise ValueError('Nonfinite teacher accuracy logits')
            y=torch.tensor(row['gold_targets'],device=x.device)
            correct=int((logits.argmax(-1)==y).sum())
            cut=len(row['prompt_ids'])-1
            suffix_correct=int((logits.argmax(-1)[cut:]==y[cut:]).sum())
            result.append(dict(id=row['id'],correct=correct,targets=len(y),
                all_targets_exact=correct==len(y),conditioned_correct=suffix_correct,
                conditioned_targets=len(y)-cut,all_conditioned_targets_exact=suffix_correct==len(y)-cut,
                predicted_ids=logits.argmax(-1).tolist()))
    return result


@torch.inference_mode()
def decode(model, rows, codec, check):
    result=[]
    with isolated_evaluation(model), sdpa_kernel(SDPBackend.MATH):
        for row in rows:
            x=torch.tensor([row['prompt_ids']],device=next(model.parameters()).device)
            cache,generated=None,[]
            for _ in range(len(row['continuation_gold_ids'])+8):
                check()
                with torch.autocast(x.device.type,dtype=torch.bfloat16,enabled=x.device.type=='cuda'):
                    output=model(x,cache=cache,use_cache=True)
                cache=output.cache
                logits=output.logits[0,-1].float()
                if not bool(torch.isfinite(logits).all()):
                    raise ValueError('Nonfinite cached continuation logits')
                logits[list(SUPPRESS_IDS)]=-torch.inf
                token=int(logits.argmax()); generated.append(token)
                if token==3: break
                x=torch.tensor([[token]],device=x.device)
            raw=codec.decode_bytes(generated)
            result.append(dict(id=row['id'],generated_ids=generated,
                actual_gold_ids=row['continuation_gold_ids'], exact=generated==row['continuation_gold_ids'],
                actual_EOS=bool(generated and generated[-1]==3),raw_UTF8_bytes_hex=raw.hex(),
                text=raw.decode('utf-8',errors='replace')))
    return result


def freeze():
    if CONFIG.exists() or RUN.exists() or OUTPUT.exists():
        raise ValueError('Preserve prospective config and actual results')
    start=time.monotonic()
    previous=read_json(ROOT/'configs/phase6/base_residual_seen_train_diagnostic.json')
    proposal=PHASE/'base_residual_capacity_control_protocol_correction.json'
    original=PHASE/'base_residual_capacity_control_proposal.json'
    rows=checked(previous['preparation'])['selected']
    validate_rows(rows)
    conflicts=conflicting_histories(rows)
    if not conflicts or any(pos>=len(next(r for r in rows if r['id']==unit)['prompt_ids'])-1
                            for conflict in conflicts for unit,pos,_ in conflict['positions']):
        raise ValueError('Inspect conflicting full/conditioned histories before defining control')
    if not proposal.exists():
        p=read_json(original)
        p.update(created_at=now(),status='prospective_pre_GPU_structural_protocol_correction',
            original_proposal=ref(original),preparation=previous['preparation'],
            conflicting_original_histories=conflicts,
            maximum_possible_full_teacher_argmax_correct=sum(len(r['gold_targets']) for r in rows)
                -sum(c['unavoidable_argmax_errors'] for c in conflicts),
            actual_unique_gold_targets=sum(len(r['gold_targets']) for r in rows),
            conditioned_gold_targets=sum(len(r['continuation_gold_ids']) for r in rows),
            reason='Identical BOS history has six distinct first-token targets. Full teacher100% is impossible. Before any CUDA/learning, correct the diagnostic criterion to exact original suffix after the existing fixed24-token prefix; train on unchanged full originals and retain all full-target scores. This changes no Base gates, source, optimizer, budget or decoder.',
            capacity_completion_condition='All six fixed24-token-prefix-conditioned teacher suffixes100% argmax correct and all six cached BF16/math greedy original suffixes plus real EOS exactly reproduced. Entire original body/EOS still trained and full-target accuracy still reported.',
            capacity_early_stop='Check every25 completed updates; only conditioned suffix100% triggers six cached decodes. No cap/LR/selection rescue.',
            GPU_learning_started=False,GPU_seconds=0,diagnostic_learning_teacher_tokens=0)
        atomic_json(proposal,p)
    p=read_json(proposal)
    if (p['maximum_capacity_control_original_teacher_tokens']!=CAP or p['maximum_cumulative_GPU_seconds']!=300
            or p['optimizer']['lr']!=.0002 or p['parent_checkpoint_sha256']!=previous['checkpoint']['sha256']):
        raise ValueError('Prospective fixed capacity control differs')
    validate_rows(checked(previous['preparation'])['selected'])
    names=['scripts/run_base_residual_capacity.py','scripts/run_base_residual_capacity.ps1',
           'tests/test_base_residual_capacity.py']
    import xml.etree.ElementTree as ET
    tests=PHASE/'base_residual_capacity_runner_tests.xml'
    cases=ET.parse(tests).findall('.//testcase')
    if len(cases)!=4 or any(r.find(t) is not None for r in cases for t in ('failure','error','skipped')):
        raise ValueError('Four passed accounting/resume fixtures required')
    config=dict(created_at=now(),proposal=ref(proposal),preparation=previous['preparation'],
        parent=previous['checkpoint'],training_record=previous['training_record'],CPU_tests=ref(tests),
        source_sha256={**previous['source_sha256'],**{n:sha256(ROOT/n) for n in names}},
        max_teacher_tokens=CAP,GPU_budget_seconds=300,checkpoint_every_updates=25,
        actual_model_class='JMicroModel',actual_unique_parameters=10001152,
        tokenizer=read_json(ROOT/'configs/phase6/base_parallel_residual_comparison.json')['tokenizer'],
        diagnostic_only=True,Base_complete=False,Chat_started=False,quantization_started=False)
    if time.monotonic()-start>30: raise TimeoutError('CPU preparation cap exhausted')
    atomic_json(CONFIG,config)
    print('Capacity control frozen before CUDA: six original units,3M teachers,300seconds,own exact-resume gate')


def inspect():
    c=read_json(CONFIG)
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen code differs: '+name)
    checked(c['proposal']); prepared=checked(c['preparation']); checked(c['training_record'])
    validate_rows(prepared['selected'])
    if c['max_teacher_tokens']!=CAP or c['GPU_budget_seconds']!=300:
        raise ValueError('Fixed budget differs')
    if RUN.exists() or OUTPUT.exists(): raise ValueError('Inspect existing capacity process/result; no duplicate or reroll')
    prior=read_json(PHASE/'base-residual-seen-train-diagnostic-20261008/job.json')
    if alive(prior) or prior['status']!='complete': raise ValueError('Previous diagnostic must be ended')
    lock=Path.home()/'jmicro-data/gpu.lock'
    if lock.exists():
        holder=read_json(lock)
        ui=read_json(ROOT/'reports/local/webui/server.json')
        if Path(f"/proc/{holder['pid']}").exists() and (holder['pid']!=ui['pid'] or not alive(ui)):
            raise ValueError('Another live GPU job holds lock')
    return c,prepared['selected']


def run():
    torch.set_num_threads(2)
    c,rows=inspect()
    if not torch.cuda.is_available() or not torch.cuda.is_bf16_supported():
        raise RuntimeError('Actual CUDA/BF16 required')
    RUN.mkdir(parents=True)
    job=dict(status='starting',**identity(),started_at=now(),config=ref(CONFIG),GPU_seconds=0,
             cumulative_GPU_ledger_closed=False,diagnostic_only=True)
    atomic_json(RUN/'job.json',job)
    started=None
    trainer=None
    try:
        with gpu_lock('cuda'):
            started=time.monotonic()
            def check():
                if time.monotonic()-started>=295:
                    raise TimeoutError('Capacity300-second ledger: reserve5seconds for final state/save')
            parent_path=Path(c['parent']['path'])
            if sha256(parent_path)!=c['parent']['sha256']: raise ValueError('Actual parent checkpoint differs')
            parent=torch.load(parent_path,map_location='cpu',weights_only=False)
            if parent['spec']['arm']!='sequential' or parent['counters']['supervised_tokens']!=2000000000:
                raise ValueError('Actual sequential2B parent required')
            binding=dict(parent=c['parent'],preparation=c['preparation'],config_sha256=sha256(CONFIG))
            gate=resume_gate(parent,rows,binding,check)
            trainer=Trainer(parent,rows,binding)
            if type(trainer.model).__name__!='JMicroModel' or sum(p.numel() for p in trainer.model.parameters())!=10001152:
                raise ValueError('Exact original10M model required')
            codec=Tokenizer(ROOT/c['tokenizer'])
            initial=accuracy(trainer.model,rows,check)
            atomic_json(RUN/'initial-accuracy.json',initial)
            last_accuracy, continuations, passed=initial,[],False
            accuracy_update=0
            reason='teacher_budget_exhausted'
            try:
                with (RUN/'metrics.jsonl').open('x') as metrics:
                    while trainer.counters['supervised_tokens']<CAP:
                        check()
                        record=trainer.step(CAP-trainer.counters['supervised_tokens'])
                        metrics.write(json.dumps(record)+'\n'); metrics.flush()
                        update=trainer.counters['update']
                        if update%25==0 or trainer.counters['supervised_tokens']==CAP:
                            check()
                            trainer.save(RUN/'latest.pt')
                            last_accuracy=accuracy(trainer.model,rows,check)
                            accuracy_update=update
                            if all(r['all_conditioned_targets_exact'] for r in last_accuracy):
                                continuations=decode(trainer.model,rows,codec,check)
                                passed=all(r['exact'] for r in continuations)
                            atomic_json(RUN/f'check-{update:05d}.json',dict(teacher=last_accuracy,free=continuations,passed=passed))
                            job.update(status='running',GPU_seconds=time.monotonic()-started,counters=host(trainer.counters),
                                cursor=trainer.cursor,checkpoint=str(RUN/'latest.pt'),heartbeat_at=now())
                            atomic_json(RUN/'job.json',job)
                            print(json.dumps(dict(update=update,teachers=trainer.counters['supervised_tokens'],
                                teacher_correct=sum(r['correct'] for r in last_accuracy),GPU_seconds=job['GPU_seconds'],passed=passed)),flush=True)
                            if passed: reason='all6_conditioned_original_targets_and_cached_suffix_EOS_exact'; break
            except TimeoutError:
                reason='bounded_GPU_deadline'
            trainer.save(RUN/'latest.pt')
            synchronize('cuda')
            elapsed=time.monotonic()-started
            if elapsed>300: raise TimeoutError('Actual cumulative300-second budget exceeded')
            result=dict(status='complete',created_at=now(),identity=identity(),config=ref(CONFIG),
                parent=c['parent'],preparation=c['preparation'],resume_gate=gate,counters=host(trainer.counters),
                cursor=trainer.cursor,checkpoint=ref(RUN/'latest.pt'),initial_teacher=initial,
                last_teacher=last_accuracy,teacher_measured_at_update=accuracy_update,
                free=continuations,capacity_control_passed=passed,completion_reason=reason,
                GPU_seconds=elapsed,GPU_cap_seconds=300,cumulative_GPU_ledger_closed=True,
                scientific_Base_teacher_tokens=0,diagnostic_learning_teacher_tokens=trainer.counters['supervised_tokens'],
                unique_original_teacher_tokens=sum(len(r['gold_targets']) for r in rows),
                original_parent_not_modified=True,probe_weights_discarded_for_adoption=True,
                Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
                protected_test_scored=False,
                limits='Positive learning control on six consumed TRAIN units only; neither Base quality nor generalization.')
            atomic_json(OUTPUT,result)
            job.update(status='complete',ended_at=now(),GPU_seconds=elapsed,counters=host(trainer.counters),
                       cumulative_GPU_ledger_closed=True,capacity_control_passed=passed)
            atomic_json(RUN/'job.json',job)
    except BaseException as error:
        if started is not None: synchronize('cuda')
        job.update(status='failed',error=repr(error),ended_at=now(),GPU_seconds=0 if started is None else time.monotonic()-started,
                   cumulative_GPU_ledger_closed=True)
        if trainer is not None: job['counters']=host(trainer.counters)
        atomic_json(RUN/'job.json',job)
        raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--freeze',action='store_true'); group.add_argument('--inspect',action='store_true')
    group.add_argument('--wait-ui',action='store_true')
    args=parser.parse_args()
    if args.freeze: freeze()
    elif args.inspect: inspect(); print('Frozen capacity preflight passed; no duplicate GPU job')
    elif args.wait_ui:
        from run_base_residual_seen_train import wait_ui
        wait_ui()
    else: run()
