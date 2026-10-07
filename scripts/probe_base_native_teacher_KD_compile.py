"""One finite same-objective compiled-hidden CUDA eligibility measurement."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import signal
import statistics
import sys
import time
import xml.etree.ElementTree as ET
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.phase5 import equal_state
from jmicro.training import atomic_json, gpu_lock
from jmicro.tokenizer import Tokenizer
from base_native_teacher_KD_compiled import CompiledNativeTeacherKDTrainer, compiled_hidden, ORIGINAL_HIDDEN, RECIPE
from base_native_teacher_KD_trainer import predictive_KL, finite_KD_state
from natural_context_contrast_corpus import OriginalTrainCorpusSampler, NaturalCorpusTrainer
from natural_context_contrast_trainer import host, right_pad
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity, alive

CONFIG = ROOT/'configs/phase6/base_native_teacher_KD_compile_probe.json'
RUN = ROOT/'reports/phase6/base-native-teacher-KD-compile-probe-20261007'
PROPOSAL = ROOT/'reports/phase6/base_native_teacher_KD_compile_proposal.json'
OLD_CONFIG = ROOT/'configs/phase6/base_native_teacher_KD_probe_v2.json'
COMPLETION = ROOT/'reports/phase6/base_native_teacher_KD_probe_completion.json'
ADDED_SOURCES = ('scripts/base_native_teacher_KD_compiled.py',
    'scripts/probe_base_native_teacher_KD_compile.py', 'scripts/probe_base_native_teacher_KD_compile.ps1',
    'tests/test_base_native_teacher_KD_compiled.py')
REF_KEYS = ('proposal', 'compile_proposal', 'CPU_tests', 'payload', 'numeric_payload',
    'control_CE', 'control_result', 'prior_completion', 'original_probe_config')


def ref(p): return dict(path=str(p), sha256=sha256(p))


def prepare():
    if CONFIG.exists() or RUN.exists(): raise ValueError('One-shot compiled condition must be preserved')
    c, previous = read_json(OLD_CONFIG), read_json(COMPLETION)
    if previous['science_budget_eligible'] or not previous['actual_process_ended']:
        raise ValueError('Closed eager budget condition required')
    suites = ET.parse(ROOT/'reports/phase6/base_native_teacher_KD_compile_tests.xml').getroot()
    if sum(int(s.get('tests', 0)) for s in suites.iter('testsuite')) != 15 or any(
        int(s.get(k, 0)) for s in suites.iter('testsuite') for k in ('failures', 'errors', 'skipped')):
        raise ValueError('Actual fifteen related CPU checks required')
    proposal = read_json(PROPOSAL)
    if proposal['prior_closeout_SHA256'] != sha256(COMPLETION): raise ValueError('Prospective proposal changed')
    c.update(created_at=now(), compile_proposal=ref(PROPOSAL), prior_completion=ref(COMPLETION),
        original_probe_config=ref(OLD_CONFIG),
        CPU_tests=ref(ROOT/'reports/phase6/base_native_teacher_KD_compile_tests.xml'),
        numeric_payload=ref(ROOT/'reports/phase6/base_gradient_precision_payload.json'),
        prior_probe_GPU_seconds=previous['cumulative_probe_GPU_seconds'],
        hidden_execution=RECIPE, source_sha256={p:sha256(ROOT/p) for p in (*c['source_sha256'], *ADDED_SOURCES)})
    c.pop('correction', None)
    atomic_json(CONFIG, c)
    print(json.dumps(dict(status='compiled_native_KD_probe_frozen_GPU0', config_sha256=sha256(CONFIG))))


def inspect():
    c = read_json(CONFIG)
    for k in REF_KEYS:
        if sha256(Path(c[k]['path'])) != c[k]['sha256']: raise ValueError('Reference changed: '+k)
    for p, digest in c['source_sha256'].items():
        if sha256(ROOT/p) != digest: raise ValueError('Frozen source changed: '+p)
    for name in ('parent', 'teacher'):
        st = Path(c[name]['path']).stat()
        if (st.st_size, st.st_mtime_ns) != (c[name+'_size'], c[name+'_mtime_ns']):
            raise ValueError('Pinned checkpoint changed: '+name)
    if c['hidden_execution'] != RECIPE or c['probe_GPU_cap_seconds'] != 180 or c['total_GPU_cap_seconds'] != 3600:
        raise ValueError('Unchanged prospective recipe/caps required')
    if RUN.exists(): raise ValueError('Inspect existing process/result; no duplicate or retry')
    return c


def vector_difference(pairs):
    dot = aa = bb = dd = 0.
    for a, b in pairs:
        a, b = a.double(), b.double()
        dot += float((a*b).sum()); aa += float(a.square().sum()); bb += float(b.square().sum())
        dd += float((b-a).square().sum())
    if aa <= 0 or bb <= 0: raise ValueError('Nonzero full-vector reference and comparison required')
    return dict(cosine=dot/math.sqrt(aa*bb), relative_L2=math.sqrt(dd/aa))


def run():
    c = inspect(); RUN.mkdir()
    job = dict(status='running', stage='initializing', **identity(), created_at=now(),
               config_sha256=sha256(CONFIG), scientific_teacher_positions=0)
    atomic_json(RUN/'job.json', job)
    start = None; histories = {}; numeric = {}; invocations = []; checks = {}; initial = {}
    def elapsed(): return c['prior_probe_GPU_seconds'] + (time.monotonic()-start if start is not None else 0.)
    def check():
        if elapsed() > 180: raise TimeoutError('Cumulative180s includes prior eager gates and compiler cost')
    def beat(stage):
        check(); job.update(stage=stage, heartbeat_at=now(), GPU_occupancy_seconds=elapsed())
        atomic_json(RUN/'job.json', job)
    def clear(): gc.collect(); torch.cuda.empty_cache()
    def compile_statistics():
        from torch._dynamo.utils import counters
        return {k:{str(a):str(b) for a,b in v.items()} for k,v in counters.items()}
    try:
        torch.set_num_threads(2); torch.use_deterministic_algorithms(True)
        import torch._dynamo.config as dynamo_config
        if dynamo_config.suppress_errors: raise ValueError('Compiler eager fallback must not be enabled')
        parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
        teacher = torch.load(c['teacher']['path'], map_location='cpu', weights_only=False)
        tokenizer = Tokenizer(ROOT/c['tokenizer'])
        binding = dict(parent=c['parent'], config_sha256=sha256(CONFIG), weights_role='verification_only')
        def measured_hidden(model, ids):
            check(); item = dict(role='teacher' if not next(model.parameters()).requires_grad else 'student',
                shape=list(ids.shape), started_after_seconds=elapsed(), grad_enabled=torch.is_grad_enabled())
            invocations.append(item); when=time.monotonic()
            try:
                value = compiled_hidden()(model, ids)
                torch.cuda.synchronize(); item['status']='returned'; return value
            except BaseException as error:
                item.update(status='failed', error=repr(error)); raise
            finally:
                item['wall_seconds']=time.monotonic()-when
                atomic_json(RUN/'hidden_invocations.json', invocations)
        def build(kd=True):
            sampler = OriginalTrainCorpusSampler(c['source_binding']['pool'], c['source_binding']['manifest_sha256'], tokenizer, c['goals'], 42)
            if sampler.binding != c['source_binding']: raise ValueError('Cached accepted pool changed')
            if not kd: return NaturalCorpusTrainer(parent, sampler, binding, batch=48, contrast=False)
            t = CompiledNativeTeacherKDTrainer(parent, sampler, binding, teacher, c['teacher'], batch=48)
            t._hidden = measured_hidden
            return t
        with gpu_lock('cuda'):
            start = time.monotonic()
            signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('Remaining cumulative probe budget exhausted')))
            signal.setitimer(signal.ITIMER_REAL, 180-c['prior_probe_GPU_seconds'])
            memory = configure_resident_memory(11987593728)
            t = build(); initial.update(parent_weights=equal_state(parent['model'], host(t.model.state_dict())),
                teacher_weights=equal_state(teacher['model'], host(t.teacher.state_dict())),
                teacher_eval_no_grad=not t.teacher.training and all(not p.requires_grad for p in t.teacher.parameters()),
                student_tied_vocab=t.model.lm_head.weight is t.model.model.embed_tokens.weight,
                teacher_tied_vocab=t.teacher.lm_head.weight is t.teacher.model.embed_tokens.weight,
                bare_saved_weights=not any('_orig_mod' in k for k in t.state_dict()['model']),
                student_optimizer_only={id(p) for g in t.optimizer.param_groups for p in g['params']}=={id(p) for p in t.model.parameters()})
            rows = read_json(Path(c['numeric_payload']['path']))['rows']
            for genre in ('web', 'textbook', 'story'):
                beat('numeric_'+genre)
                selected_rows=[r for r in rows if r['source']==genre]
                if len(selected_rows)!=8: raise ValueError('Existing fixedTRAIN8 per source required')
                ids,_=right_pad([r['input_ids'] for r in selected_rows], 'cuda')
                targets=torch.full_like(ids,-100)
                for i,r in enumerate(selected_rows): targets[i,:len(r['target_ids'])]=torch.tensor(r['target_ids'],device='cuda')
                mask=targets.ne(-100); endpoints=[]
                for route, helper in (('eager', ORIGINAL_HIDDEN), ('compiled', measured_hidden)):
                    check(); t.optimizer.zero_grad(set_to_none=True)
                    with sdpa_kernel(SDPBackend.FLASH_ATTENTION), torch.autocast('cuda', dtype=torch.bfloat16):
                        with torch.no_grad(): q=t.teacher.lm_head(helper(t.teacher,ids)[mask]).float()
                        p=t.model.lm_head(helper(t.model,ids)[mask]).float()
                        ce=F.cross_entropy(p,targets[mask]); kl=ce.new_zeros(())
                        if genre!='web': kl,_=predictive_KL(p,q,targets[mask],int(mask.sum()))
                        loss=ce+kl
                        if not torch.isfinite(loss): raise ValueError('Finite numerical endpoint required')
                        loss.backward()
                    torch.cuda.synchronize()
                    gradients={k:host(v.grad) for k,v in t.model.named_parameters()}
                    if any(v is None or not torch.isfinite(v).all() for v in gradients.values()): raise ValueError('All student gradients finite and present required')
                    endpoints.append(dict(CE_loss=float(ce.detach()),KD_loss=float(kl.detach()),
                        combined_loss=float(loss.detach()),teacher_logits=host(q),gradients=gradients))
                    del q,p,ce,kl,loss
                a,b=endpoints; difference=vector_difference((a['gradients'][k],b['gradients'][k]) for k in a['gradients'])
                logits=vector_difference([(a['teacher_logits'],b['teacher_logits'])])
                loss_difference={k:abs(a[k]-b[k]) for k in ('CE_loss','KD_loss','combined_loss')}
                numeric[genre]=dict(shape=list(ids.shape),original_gold_positions=int(mask.sum()),
                    eager_losses={k:a[k] for k in loss_difference},compiled_losses={k:b[k] for k in loss_difference},
                    absolute_loss_differences=loss_difference,full_student_gradient=difference,teacher_logits=logits,
                    passed=all(v<=.005 for v in loss_difference.values()) and difference['cosine']>=.9999 and
                        difference['relative_L2']<=.01 and logits['relative_L2']<=.01,
                    teacher_web_logits_diagnostic_only=genre=='web',optimizer_updates=0)
                atomic_json(RUN/'numeric_checks.json',numeric)
                del endpoints,a,b,ids,targets,mask;clear();check()
                if not numeric[genre]['passed']: raise ValueError('Prospective compiler numerical guard failed: '+genre)
            del t;clear();beat('worst_shape_48x1024');t=build()
            window=read_json(Path(c['payload']['path']))['window']
            ids=torch.tensor([window['input_ids']]*48,device='cuda');targets=torch.tensor([window['target_ids']]*48,device='cuda');mask=targets.ne(-100)
            if ids.shape!=(48,1024) or int(mask[0].sum())!=512: raise ValueError('Frozen original TRAIN stress required')
            t.optimizer.zero_grad(set_to_none=True);torch.cuda.reset_peak_memory_stats()
            with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                with torch.no_grad():q=t.teacher.lm_head(measured_hidden(t.teacher,ids)[mask]).float()
                p=t.model.lm_head(measured_hidden(t.model,ids)[mask]).float()
                ce=F.cross_entropy(p,targets[mask]);kl,_=predictive_KL(p,q,targets[mask],int(mask.sum()));loss=ce+kl;loss.backward()
            gradient=torch.nn.utils.clip_grad_norm_(t.model.parameters(),1.,error_if_nonfinite=True);torch.cuda.synchronize()
            capacity=dict(shape=list(ids.shape),diagnostic_positions=int(mask.sum()),peak_VRAM_bytes=torch.cuda.max_memory_allocated(),
                CE_loss=float(ce.detach()),KD_loss=float(kl.detach()),gradient_norm=float(gradient),optimizer_updates=0,
                scope='Artificial all-KD upper bound from frozen original TRAIN stress; not relabeled science.')
            atomic_json(RUN/'capacity.json',capacity)
            if not finite_KD_state(capacity) or capacity['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']:raise ValueError('Capacity finite memory guard failed')
            initial['teacher_unchanged_stress']=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(p.grad is None for p in t.teacher.parameters())
            del t,ids,targets,mask,q,p,ce,kl,loss;clear();beat('continuous_vs_saved2plus2');states=[];logs=[]
            for route in ('continuous','resumed'):
                t=build();history=[];histories[route]=history
                for i in range(4):
                    check();history.append(t.step())
                    if route=='resumed' and i==1:
                        t.save(RUN/'split.pt');del t;clear();t=build();t.load(RUN/'split.pt')
                initial['teacher_unchanged_'+route]=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(p.grad is None for p in t.teacher.parameters())
                t.save(RUN/(route+'.pt'));states.append(host(t.state_dict()));logs.append(history);del t;clear()
            checks.update({k:equal_state(states[0][k],states[1][k]) for k in states[0]})
            checks['finite_all_state']=all(finite_KD_state(s) for s in states)
            checks['history_except_timing']=all(equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')}) for a,b in zip(*logs,strict=True))
            beat('original_gold_control');control=build(False);ch=[];histories['control']=ch
            for _ in range(4):check();ch.append(control.step())
            keys=(*control.counters,'draw_trace','lr')
            checks['same_original_gold_stream']=all(equal_state(a[k],b[k]) for a,b in zip(logs[0],ch,strict=True) for k in keys)
            checks['full_original_sampler']=equal_state(states[0]['sampler'],control.sampler.state_dict())
            del control;clear();atomic_json(RUN/'resume_checks.json',checks)
            if not all(initial.values()) or not all(checks.values()):raise ValueError('Compiled CUDA fullstate/source/immutable teacher guard failed')
            beat('warmup3_timing32');t=build();history=[];histories['timing']=history
            for _ in range(35):
                check();history.append(t.step());atomic_json(RUN/'partial_histories.json',histories)
            initial['teacher_unchanged_timing']=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(p.grad is None for p in t.teacher.parameters())
            if not all(initial.values()): raise ValueError('Immutable native teacher required')
            del t;clear();check();speed=statistics.median(r['CE_targets_this_update']/r['seconds'] for r in history[3:])
            forecast=math.ceil(100000000/speed*1.3+900);consumed=elapsed()
            result=dict(status='complete',passed=True,config_sha256=sha256(CONFIG),actual_identity=identity(),
                numeric_checks=numeric,initial_checks=initial,resume_and_source_checks=checks,capacity=capacity,memory_policy=memory,
                histories=histories,hidden_invocations=invocations,compiler_statistics=compile_statistics(),
                median_original_gold_per_second=speed,scientific_forecast_seconds=forecast,
                science_budget_eligible=consumed+forecast<=3600,GPU_occupancy_seconds=consumed,
                prior_probe_GPU_seconds=c['prior_probe_GPU_seconds'],additional_probe_GPU_seconds=consumed-c['prior_probe_GPU_seconds'],
                verification_updates=sum(len(h) for h in histories.values()),
                scientific_teacher_positions=0,probe_weights_used_for_science=False,Base_complete=False,Chat_started=False,quantization_started=False)
            atomic_json(RUN/'result.json',result);signal.alarm(0)
            job.update(status='complete',stage='complete',ended_at=now(),GPU_occupancy_seconds=consumed)
            atomic_json(RUN/'job.json',job);print(json.dumps(dict(status='compiled_gate_complete',eligible=result['science_budget_eligible'],GPU_seconds=consumed,speed=speed)))
    except BaseException as error:
        signal.alarm(0)
        job.update(status='failed',ended_at=now(),error=repr(error),GPU_occupancy_seconds=elapsed())
        atomic_json(RUN/'job.json',job);atomic_json(RUN/'partial_histories.json',histories)
        atomic_json(RUN/'initial_checks.json',initial);atomic_json(RUN/'compiler_statistics.json',compile_statistics())
        raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();group=parser.add_mutually_exclusive_group()
    group.add_argument('--prepare',action='store_true');group.add_argument('--inspect',action='store_true');args=parser.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Frozen compiled native KD preflight passed;GPU0')
    else:run()
