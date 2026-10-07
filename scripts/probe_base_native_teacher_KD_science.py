"""Bounded native_teacher_KD native CUDA/stream/full-state gate, preceding a single100M study."""
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
from jmicro.experiment import ROOT, now, read_json as _read_json, sha256
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock
from base_native_teacher_KD_committed import CommittedNativeTeacherKDTrainer, committed_state, RECIPE
from base_native_teacher_KD_trainer import predictive_KL
from natural_context_contrast_corpus import OriginalTrainCorpusSampler, NaturalCorpusTrainer
from natural_context_contrast_trainer import host, right_padded_hidden
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity, alive

CONFIG = ROOT/'configs/phase6/base_native_teacher_KD_science_probe.json'
RUN = ROOT/'reports/phase6/base-native-teacher-KD-science-probe-20261007'
PROPOSAL = ROOT/'reports/phase6/base_native_teacher_KD_science_proposal.json'
SOURCES = ('scripts/base_native_teacher_KD_committed.py', 'scripts/probe_base_native_teacher_KD_science.py', 'scripts/probe_base_native_teacher_KD_science.ps1',
    'scripts/base_native_teacher_KD_trainer.py','tests/test_base_native_teacher_KD.py',
    'tests/test_base_native_teacher_KD_committed.py', 'scripts/prepare_base_native_teacher_KD_science_workflow.py', 'scripts/natural_context_contrast_corpus.py',
    'scripts/natural_context_contrast_trainer.py', 'scripts/natural_context_contrast_memory.py',
    'scripts/phase6_performance.py', 'src/jmicro/model.py', 'src/jmicro/training.py', 'src/jmicro/tokenizer.py', 'uv.lock')


def ref(path): return dict(path=str(path), sha256=sha256(path))
def read_json(path): return _read_json(Path(path))


def prepare():
    if CONFIG.exists(): raise ValueError('Preserve one frozen native_teacher_KD comparison')
    old = read_json(ROOT/'configs/phase6/base_native_teacher_KD_probe_v2.json')
    old_probe = read_json(ROOT/'configs/phase6/base_next_two_token_probe.json')
    tests = ROOT/'reports/phase6/base_native_teacher_KD_science_trainer_tests.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites) != 19 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Nineteen actual unchanged-math and committed-boundary CPU checks required')
    references={}
    for name in ('base_current_objective_evidence.json','base_native_teacher_KD_proposal.json',
                 'base_native_teacher_KD_probe_completion.json','base_native_teacher_KD_compile_completion.json',
                 'base_confidence_penalty_comparison_completion.json','base_on_policy_teacher_comparison_completion.json'):
        references[name]=ref(ROOT/'reports/phase6'/name)
    previous=read_json(ROOT/'reports/phase6/base_native_teacher_KD_proposal.json')
    evidence=read_json(ROOT/'reports/phase6/base_current_objective_evidence.json')
    proposal=dict(created_at=now(),question='Does unchanged dense native short gold-prefix predictive KD transfer useful generation while retaining original Web CE?',
        prior_turn='progress: confidence100M/allJapanese/all80 rejected and committed8eb62f1; scientific729058 absent. Four actual quality failures distinguished from never-trained denseKD.',
        references=references,recipe=RECIPE,parent=old['parent'],teacher=old['teacher'],
        teacher_quality=previous['evidence']['teacher_quality'],teacher_is_adopted_Base=False,
        source_binding=old['source_binding'],goals=old['goals'],batch=48,seed=42,
        native_parameters=10001152,extra_student_parameters=0,teacher_resident_parameters=10001152,
        original_gold_positions=100000000,KD_distribution_positions=25000000,new_unique_dataset_tokens=0,
        novelty='Not a new loss, new teacher or new algorithm. Earlier same eager full-vocabulary native KD passed CUDA/state but never entered science because its self-selected3600 resource plan failed. This is an explicit separate prospective resource-plan reconsideration; no old file or failure is overwritten or retroactively passed. Current user authorization covers local GPU;3600 was not a user lifetime budget.',
        resource_reconsideration=dict(old_total_cap=3600,old_closed=True,old_scientific_gold_positions=0,
            old_median_based_forecast=4029,old_exact_update_mean32_forecast=evidence['untrained_native_KD']['exact17698_mean32_forecast_seconds'],
            new_total_GPU_cap_seconds=4800,new_probe_GPU_cap_seconds=180,
            rationale='Later bounded100M studies used4800 total, including actual confidence1495s/middle1480s; old32 measured steps imply4489s conservative mean forecast. Keep one fixed new4800 plan before new gate/results; reject if new mean forecast plus actual probe exceeds it. This does not reuse discarded old probe weights or change numeric tolerances.'),
        distinction='On-policy279734 distribution positions trained on sampled student contexts; here25M original short-source gold-prefix positions. Closed online rollout, contrast/entropy/anchor routes are not retried. Compiler numeric failure remains failed; this is unchanged eager native math.',
        primary_sources=['https://proceedings.mlr.press/v80/furlanello18a.html'],
        literature_limit='Born Again Neural Networks studies identically parameterized teacher/student, including language modeling. Different language, data, teacher history and optimization; not an exact reproduction or Japanese10M success proof.',
        accounting='Original hard body/EOS CE100M counted once. Add teacher-to-student full4096 forward KL(T1/coefficient1), only textbook/story25M positions, normalized by all original gold positions in each update. Extra distribution targets and teacher valid/physical inputs/entropy/goldprob/KL are separate, not new hard labels or corpus. Student native inference unchanged; frozen teacher never optimized or stored as student weights.',
        acceptance='CPU frozen analytic KL/mask/teacher/source checks plus committed update safety/parity/full save-resume. Actual CUDA4 vs2+2 allstate/history/source/teacher immutable, max48x1024 finite backward/memory, all32 actual postwarmup times. ceil17698*mean32seconds*1.3+900 plus current probe<=4800. Original100M/fullsampler exactly matched to cachedCE; commonDEV256/Japanese192,331,1119/native80/all80 individual reasons and unchanged matched/strong/absolute/historicalWeb quality. Qualification before independent trainedseed/fullDEV/protected finalTEST/adoption.',
        failure='After this prospective reconsideration no further cap/teacher/coefficient/temperature/LR/parent/source/batch/shape/backend/decoder rescue or automatic extension. Keep original3600 and compiled numeric failures intact. Close this study on new gate/budget or quality failure.',
        limitations='Single mature student seed and different historically trained staged teacher;25M extra predictive supervision/teacher compute, repeatedly used nonblind DEV. No isolated data/architecture or capacity proof.',
        CPU_checks=ref(tests),Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(PROPOSAL, proposal)
    fields = ('parent','parent_size','parent_mtime_ns','teacher','teacher_size','teacher_mtime_ns','source_binding','goals','tokenizer','tokenizer_sha256',
              'dev_shards','dev_manifest_sha256','suite_sha256','evaluation')
    plan = dict(**{k:old[k] for k in fields}, created_at=now(), proposal=ref(PROPOSAL), CPU_tests=ref(tests),
        source_sha256={s:sha256(ROOT/s) for s in SOURCES}, payload=old_probe['payload'],
        batch=48, seed=42, probe_GPU_cap_seconds=180, total_GPU_cap_seconds=4800,
        warmup_updates=3, timed_updates=32, control_CE=old['control_CE'],
        control_result=ref(ROOT/'reports/phase6/natural-context-contrast-comparison-20261007/CE/train-result.json'),
        Base_complete=False, Chat_started=False, quantization_started=False)
    atomic_json(CONFIG, plan)
    print(json.dumps(dict(status='native_teacher_KD_protocol_frozen_GPU0', total_GPU_cap_seconds=4800, config_sha256=sha256(CONFIG))))


def inspect():
    p = read_json(CONFIG)
    for name in ('proposal','CPU_tests','payload','control_CE','control_result'):
        if sha256(Path(p[name]['path'])) != p[name]['sha256']: raise ValueError('Frozen reference differs: '+name)
    for name, digest in p['source_sha256'].items():
        if sha256(ROOT/name) != digest: raise ValueError('Frozen source differs: '+name)
    payload = read_json(p['payload']['path'])
    if 'window' not in payload or len(payload['window']['input_ids']) != 1024:
        raise ValueError('Existing maximum original-window payload required')
    for name in ('parent','teacher'):
        st=Path(p[name]['path']).stat()
        if (st.st_size,st.st_mtime_ns)!=(p[name+'_size'],p[name+'_mtime_ns']): raise ValueError('Pinned checkpoint identity changed: '+name)
    if (RUN/'job.json').exists(): raise ValueError('Inspect one-shot native_teacher_KD probe; no duplicate/retry')
    return p


def run():
    p = inspect()
    RUN.mkdir(parents=True, exist_ok=True)
    job = dict(status='running', **identity(), started_at=now(), config_sha256=sha256(CONFIG),
               scientific_teacher_positions=0, Base_complete=False, Chat_started=False, quantization_started=False)
    atomic_json(RUN/'job.json', job)
    started = None
    histories = {}
    def check(*_):
        if started is not None and time.monotonic()-started > 180: raise TimeoutError('native_teacher_KD probe180s exhausted')
    def clear(): gc.collect(); torch.cuda.empty_cache()
    try:
        torch.set_num_threads(2); torch.use_deterministic_algorithms(True)
        memory = configure_resident_memory(13047812096)
        parent = torch.load(p['parent']['path'], map_location='cpu', weights_only=False)
        teacher = torch.load(p['teacher']['path'], map_location='cpu', weights_only=False)
        tokenizer = Tokenizer(ROOT/p['tokenizer'])
        binding = dict(parent=p['parent'], config_sha256=sha256(CONFIG), weights_role='verification_only')
        def build(native_teacher_KD=True):
            sampler = OriginalTrainCorpusSampler(p['source_binding']['pool'],p['source_binding']['manifest_sha256'],tokenizer,p['goals'],42)
            if sampler.binding != p['source_binding']: raise ValueError('Cached accepted source changed')
            if not native_teacher_KD: return NaturalCorpusTrainer(parent,sampler,binding,batch=48,contrast=False)
            return CommittedNativeTeacherKDTrainer(parent,sampler,binding,teacher,p['teacher'],batch=48)
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('native_teacher_KD hard probe cap180s')))
            signal.alarm(180)
            t = build()
            initial = dict(native_parent_weights=equal_state(parent['model'],host(t.model.state_dict())),
                tied_native_vocab=t.model.lm_head.weight is t.model.model.embed_tokens.weight,
                native_parameters=sum(v.numel() for v in t.model.parameters()) == 10001152,
                all_parameters_once=len({id(v) for g in t.optimizer.param_groups for v in g['params']}) == len(list(t.model.parameters())))
            initial.update(frozen_teacher_weights=equal_state(teacher['model'],host(t.teacher.state_dict())),
                teacher_eval_no_grad=not t.teacher.training and all(not v.requires_grad for v in t.teacher.parameters()),
                teacher_native_tied=t.teacher.lm_head.weight is t.teacher.model.embed_tokens.weight,
                teacher_parameters=sum(v.numel() for v in t.teacher.parameters())==10001152,
                student_optimizer_only={id(v) for g in t.optimizer.param_groups for v in g['params']}=={id(v) for v in t.model.parameters()})
            history = []; histories['timing'] = history
            for _ in range(35): check(); history.append(t.step())
            speed = statistics.median(r['CE_targets_this_update']/r['seconds'] for r in history[3:])
            initial['teacher_unchanged_after35']=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(v.grad is None for v in t.teacher.parameters())
            payload = read_json(p['payload']['path'])
            window = payload['window']
            ids = torch.tensor([window['input_ids']]*48,device='cuda')
            targets = torch.tensor([window['target_ids']]*48,device='cuda')
            if ids.shape != (48,1024) or targets[0].ne(-100).sum() != 512: raise ValueError('Original maximum1024/512 window required')
            t.optimizer.zero_grad(set_to_none=True); torch.cuda.reset_peak_memory_stats()
            before=host(t.model.state_dict());selected=targets.ne(-100)
            with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                with torch.no_grad(): q=t.teacher.lm_head(right_padded_hidden(t.teacher,ids)[selected]).float()
                logits=t.model.lm_head(right_padded_hidden(t.model,ids)[selected]).float()
                ce=F.cross_entropy(logits,targets[selected]);kl,_=predictive_KL(logits,q,targets[selected],int(selected.sum()))
                combined=ce+kl
            combined.backward();gradient=torch.nn.utils.clip_grad_norm_(t.model.parameters(),1.,error_if_nonfinite=True)
            torch.cuda.synchronize()
            capacity=dict(context=1024,target_stride=512,batch=48,original_target_positions=int(selected.sum()),
                KD_distribution_positions=int(selected.sum()),peak_VRAM_bytes=torch.cuda.max_memory_allocated(),
                optimizer_updates=0,unchanged_weights=equal_state(before,host(t.model.state_dict())),
                CE_loss=float(ce.detach()),KD_loss=float(kl.detach()),combined_loss=float(combined.detach()),gradient_norm=float(gradient),
                scope='Artificial all-KD upper-bound shape; not relabeled Web or new scientific gold')
            initial['teacher_unchanged_after_stress']=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(v.grad is None for v in t.teacher.parameters())
            if not capacity['unchanged_weights'] or not all(math.isfinite(capacity[k]) for k in ('CE_loss','KD_loss','combined_loss','gradient_norm')) or capacity['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']:
                raise ValueError('Finite native original CE/KD worst shape required')
            del t,before,ids,targets,selected,logits,q,ce,kl,combined; clear()
            states, logs = [], []
            for route in ('continuous','resumed'):
                t = build(); history = []; histories[route] = history
                for index in range(4):
                    check(); history.append(t.step())
                    if route == 'resumed' and index == 1:
                        t.save(RUN/'split.pt'); del t; clear(); t = build(); t.load(RUN/'split.pt')
                initial['teacher_unchanged_'+route]=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(v.grad is None for v in t.teacher.parameters())
                t.save(RUN/(route+'.pt')); states.append(host(t.state_dict())); logs.append(history)
                del t; clear()
            checks = {k:equal_state(states[0][k],states[1][k]) for k in states[0]}
            checks['finite_hybrid_model_buffers'] = all(committed_state(s) for s in states)
            checks['history_except_timing'] = all(equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')}) for a,b in zip(*logs,strict=True))
            control = build(False); ch = []; histories['control'] = ch
            for _ in range(4): check(); ch.append(control.step())
            keys = ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens','physical_input_tokens',
                    'original_body_bytes','token_digest','draw_trace','lr')
            checks['same_original_stream'] = all(equal_state(a[k],b[k]) for a,b in zip(logs[0],ch,strict=True) for k in keys)
            checks['full_sampler_matches_AdamW'] = equal_state(states[0]['sampler'],control.sampler.state_dict())
            del control; clear(); check()
            if not all(initial.values()) or not all(checks.values()): raise ValueError('Hybrid state/source CUDA gate failed')
            elapsed = time.monotonic()-started
            forecast = math.ceil(17698/32*sum(r['seconds'] for r in histories['timing'][3:])*1.3+900)
            result = dict(status='complete', passed=True, actual_identity=identity(),config_sha256=sha256(CONFIG),
                initial_checks=initial, all_resume_and_source_checks=checks, memory_policy=memory,capacity=capacity,
                all32_timing_speeds=[r['CE_targets_this_update']/r['seconds'] for r in histories['timing'][3:]],
                median_original_teachers_per_second=speed, science_budget_seconds=forecast,
                science_budget_eligible=elapsed+forecast<=4800, total_GPU_cap_seconds=4800,
                GPU_occupancy_seconds=elapsed, histories=histories,
                verification_updates=sum(len(h) for h in histories.values()),
                verification_original_teacher_positions=sum(r['CE_targets_this_update'] for h in histories.values() for r in h),
                capacity_forward_backward_original_positions=capacity['original_target_positions'],
                native_teacher_KD=states[0]['native_teacher_KD'], all32_timing_seconds=[r['seconds'] for r in histories['timing'][3:]],
                verification_KD_distribution_positions=sum(r.get('KD_targets_this_update',0) for h in histories.values() for r in h), scientific_teacher_positions=0,
                probe_weights_used_for_science=False, Base_complete=False, Chat_started=False, quantization_started=False)
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',ended_at=now(),GPU_occupancy_seconds=elapsed)
            atomic_json(RUN/'job.json',job); signal.alarm(0)
            print(json.dumps(dict(status='native_teacher_KD_CUDA_gate_complete',speed=speed,GPU_seconds=elapsed,science_budget_seconds=forecast,science_budget_eligible=result['science_budget_eligible'])))
    except BaseException as error:
        signal.alarm(0)
        job.update(status='failed',error=repr(error),ended_at=now(),GPU_occupancy_seconds=time.monotonic()-started if started else 0)
        atomic_json(RUN/'job.json',job); atomic_json(RUN/'partial_histories.json',histories)
        raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser(); group = parser.add_mutually_exclusive_group()
    group.add_argument('--prepare',action='store_true'); group.add_argument('--inspect',action='store_true')
    args = parser.parse_args()
    if args.prepare: prepare()
    elif args.inspect: inspect(); print('Frozen native_teacher_KD gate inspected; GPU0')
    else: run()
