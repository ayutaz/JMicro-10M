"""Bounded SAM native CUDA/stream/full-state gate, preceding a single100M study."""
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
from base_sam_trainer import SAMTrainer, committed_state, sam_backward, RECIPE
from natural_context_contrast_corpus import OriginalTrainCorpusSampler, NaturalCorpusTrainer
from natural_context_contrast_trainer import host, right_padded_hidden
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity, alive

CONFIG = ROOT/'configs/phase6/base_sam_probe.json'
RUN = ROOT/'reports/phase6/base-sam-probe-20261007'
PROPOSAL = ROOT/'reports/phase6/base_sam_proposal.json'
SOURCES = ('scripts/base_sam_trainer.py', 'scripts/probe_base_sam.py', 'scripts/probe_base_sam.ps1',
    'tests/test_base_sam_trainer.py', 'scripts/prepare_base_sam_workflow.py', 'scripts/natural_context_contrast_corpus.py',
    'scripts/natural_context_contrast_trainer.py', 'scripts/natural_context_contrast_memory.py',
    'scripts/phase6_performance.py', 'src/jmicro/model.py', 'src/jmicro/training.py', 'src/jmicro/tokenizer.py', 'uv.lock')


def ref(path): return dict(path=str(path), sha256=sha256(path))
def read_json(path): return _read_json(Path(path))


def prepare():
    if CONFIG.exists(): raise ValueError('Preserve one frozen SAM comparison')
    old = read_json(ROOT/'configs/phase6/base_next_two_token_comparison.json')
    old_probe = read_json(ROOT/'configs/phase6/base_next_two_token_probe.json')
    tests = ROOT/'reports/phase6/base_sam_trainer_tests.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites) != 9 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Nine actual CPU SAM protocol checks required')
    references = {}
    for name in ('base_failure_route_synthesis.json','base_muon_comparison_completion.json',
                 'base_on_policy_teacher_comparison_completion.json','base_gradient_precision_completion.json'):
        path=ROOT/'reports/phase6'/name
        references[name]=ref(path)
    proposal=dict(created_at=now(),question='Does full-batch sharpness-aware CE optimization improve same-parent Japanese Base generalization and repetition while preserving Web quality?',
        prior_turn='progress: actual on-policy100M/all Japanese/all80 content rejection and portable closeout committed1530346; actual process718057 absent',
        references=references,
        novelty='Inspection of existing optimizer/objective proposals found AdamW, Muon, contrastive, dropout/smoothing and teacher feedback, but no full-parameter two-pass SAM. Unlike Muon it uses a second same-batch CE gradient at adversarially perturbed weights; unlike anchors/KL it has no reference model or parameter-location penalty. Exploratory mechanism, not a proven root cause.',
        primary_sources=['https://arxiv.org/abs/2010.01412','https://arxiv.org/abs/2110.08529','https://github.com/google-research/sam'],
        literature_limit='The NLP paper reports task finetuning/choice/QA gains on larger models. It does not prove free Japanese10M continuation quality; this is a local Base full-body/EOS study, no Chat/SFT.',
        recipe=RECIPE,parent=old['parent'],source_binding=old['source_binding'],goals=old['goals'],
        batch=48,seed=42,native_parameters=10001152,extra_parameters=0,original_teachers=100000000,
        repeated_SAM_teacher_evaluations=100000000,new_unique_dataset_tokens=0,control_reused_GPU_seconds=0,
        total_GPU_cap_seconds=7200,probe_GPU_cap_seconds=180,CPU_checks=ref(tests),
        accounting='Draw/CE source quotas, EOS/body/bytes/digest and sampler once; second evaluation of exact same inputs/targets is separate repeated teacher/valid/physical compute. Single optimizer update after exact FP32 restoration. No new data, teacher, auxiliary parameters or decoder changes.',
        acceptance='Actual CPU and CUDA continuous4 vs2-save-resume2/full state, two-pass worst48x1024 finite gradients/restoration before science. Forecast ceil(exact17698 updates*mean32 measured two-pass seconds*1.3+900) plus actual probe within7200. Same cachedCE100M source and fullsampler, same256 commonbyte/Japanese192,331,1119/all80 raw-bound content, unchanged matched/strong/absolute/historicalWeb gates. Only qualified candidate gets independent learnedseed/fullDEV/protected finalTEST/adoption.',
        failure='Close this one fixed condition on finite/state/radius/budget or quality failure. No rho/adaptive/period/optimizer/LR/parent/data/batch/decoder/cap rescue or extension.',
        limitations='One conservative-LR mature-parent transition, extra second-pass compute, repeated nonblind DEV. Negative result does not disprove all SAM; local fit/likelihood is not useful Base quality.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(PROPOSAL, proposal)
    fields = ('parent','parent_size','parent_mtime_ns','source_binding','goals','tokenizer','tokenizer_sha256',
              'dev_shards','dev_manifest_sha256','suite_sha256','evaluation')
    plan = dict(**{k:old[k] for k in fields}, created_at=now(), proposal=ref(PROPOSAL), CPU_tests=ref(tests),
        source_sha256={s:sha256(ROOT/s) for s in SOURCES}, payload=old_probe['payload'],
        batch=48, seed=42, probe_GPU_cap_seconds=180, total_GPU_cap_seconds=7200,
        warmup_updates=3, timed_updates=32, control_CE=old['control_CE'],
        control_result=ref(ROOT/'reports/phase6/natural-context-contrast-comparison-20261007/CE/train-result.json'),
        Base_complete=False, Chat_started=False, quantization_started=False)
    atomic_json(CONFIG, plan)
    print(json.dumps(dict(status='SAM_protocol_frozen_GPU0', total_GPU_cap_seconds=7200, config_sha256=sha256(CONFIG))))


def inspect():
    p = read_json(CONFIG)
    for name in ('proposal','CPU_tests','payload','control_CE','control_result'):
        if sha256(Path(p[name]['path'])) != p[name]['sha256']: raise ValueError('Frozen reference differs: '+name)
    for name, digest in p['source_sha256'].items():
        if sha256(ROOT/name) != digest: raise ValueError('Frozen source differs: '+name)
    payload = read_json(p['payload']['path'])
    if 'window' not in payload or len(payload['window']['input_ids']) != 1024:
        raise ValueError('Existing maximum original-window payload required')
    st = Path(p['parent']['path']).stat()
    if (st.st_size, st.st_mtime_ns) != (p['parent_size'],p['parent_mtime_ns']): raise ValueError('Audited parent identity changed')
    if (RUN/'job.json').exists(): raise ValueError('Inspect one-shot SAM probe; no duplicate/retry')
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
        if started is not None and time.monotonic()-started > 180: raise TimeoutError('SAM probe180s exhausted')
    def clear(): gc.collect(); torch.cuda.empty_cache()
    try:
        torch.set_num_threads(2); torch.use_deterministic_algorithms(True)
        memory = configure_resident_memory(11987593728)
        parent = torch.load(p['parent']['path'], map_location='cpu', weights_only=False)
        tokenizer = Tokenizer(ROOT/p['tokenizer'])
        binding = dict(parent=p['parent'], config_sha256=sha256(CONFIG), weights_role='verification_only')
        def build(sam=True):
            sampler = OriginalTrainCorpusSampler(p['source_binding']['pool'],p['source_binding']['manifest_sha256'],tokenizer,p['goals'],42)
            if sampler.binding != p['source_binding']: raise ValueError('Cached accepted source changed')
            return (SAMTrainer if sam else NaturalCorpusTrainer)(parent,sampler,binding,batch=48,contrast=False)
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('SAM hard probe cap180s')))
            signal.alarm(180)
            t = build()
            initial = dict(native_parent_weights=equal_state(parent['model'],host(t.model.state_dict())),
                tied_native_vocab=t.model.lm_head.weight is t.model.model.embed_tokens.weight,
                native_parameters=sum(v.numel() for v in t.model.parameters()) == 10001152,
                all_parameters_once=len({id(v) for g in t.optimizer.param_groups for v in g['params']}) == len(list(t.model.parameters())))
            history = []; histories['timing'] = history
            for _ in range(35): check(); history.append(t.step())
            speed = statistics.median(r['CE_targets_this_update']/r['seconds'] for r in history[3:])
            payload = read_json(p['payload']['path'])
            window = payload['window']
            ids = torch.tensor([window['input_ids']]*48,device='cuda')
            targets = torch.tensor([window['target_ids']]*48,device='cuda')
            if ids.shape != (48,1024) or targets[0].ne(-100).sum() != 512: raise ValueError('Original maximum1024/512 window required')
            t.optimizer.zero_grad(set_to_none=True); torch.cuda.reset_peak_memory_stats()
            selected=targets.ne(-100)
            def closure():
                with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                    return F.cross_entropy(t.model.lm_head(right_padded_hidden(t.model,ids)[selected]).float(),targets[selected])
            before=host(t.model.state_dict())
            measures=sam_backward(t.model,t.optimizer,closure)
            torch.cuda.synchronize()
            capacity=dict(context=1024,target_stride=512,batch=48,original_target_positions=int(selected.sum()),
                repeated_target_positions=int(selected.sum()),peak_VRAM_bytes=torch.cuda.max_memory_allocated(),
                optimizer_updates=0,exact_restoration=equal_state(before,host(t.model.state_dict())),**measures)
            if not capacity['exact_restoration'] or not all(math.isfinite(measures[k]) for k in measures) or capacity['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']:
                raise ValueError('Finite SAM two-pass/restored resident worst shape required')
            del t,before,ids,targets; clear()
            states, logs = [], []
            for route in ('continuous','resumed'):
                t = build(); history = []; histories[route] = history
                for index in range(4):
                    check(); history.append(t.step())
                    if route == 'resumed' and index == 1:
                        t.save(RUN/'split.pt'); del t; clear(); t = build(); t.load(RUN/'split.pt')
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
                science_budget_eligible=elapsed+forecast<=7200, total_GPU_cap_seconds=7200,
                GPU_occupancy_seconds=elapsed, histories=histories,
                verification_updates=sum(len(h) for h in histories.values()),
                verification_original_teacher_positions=sum(r['CE_targets_this_update'] for h in histories.values() for r in h),
                capacity_forward_backward_original_positions=capacity['original_target_positions'],
                SAM=states[0]['SAM'], all32_timing_seconds=[r['seconds'] for r in histories['timing'][3:]],
                verification_repeated_teacher_evaluations=sum(r.get('repeated_teacher_positions_this_update',0) for h in histories.values() for r in h), scientific_teacher_positions=0,
                probe_weights_used_for_science=False, Base_complete=False, Chat_started=False, quantization_started=False)
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',ended_at=now(),GPU_occupancy_seconds=elapsed)
            atomic_json(RUN/'job.json',job); signal.alarm(0)
            print(json.dumps(dict(status='SAM_CUDA_gate_complete',speed=speed,GPU_seconds=elapsed,science_budget_seconds=forecast,science_budget_eligible=result['science_budget_eligible'])))
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
    elif args.inspect: inspect(); print('Frozen SAM gate inspected; GPU0')
    else: run()
