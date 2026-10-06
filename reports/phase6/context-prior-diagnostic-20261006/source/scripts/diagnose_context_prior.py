"""Bounded CPU-only context/prior comparison on existing fixed encoded targets."""
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
import time
START = time.monotonic()
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import argparse
import copy
import gc
import hashlib
import json
import math
import shutil
import signal
import xml.etree.ElementTree as ET
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json, rng_state, restore_rng
from jmicro.model import JMicroModel
from jmicro.japanese_evaluation import NativeLikelihood
from phase6_performance import identity, alive
from run_eos_short_pilot import equal_state
from context_prior_analysis import (METRICS,request,index_cases,validate_scores,family_rows,
    aggregate,compare_rows,comparison_counts)

PROPOSAL = ROOT/'reports/phase6/context_prior_diagnostic_proposal.json'
CONFIG = ROOT/'configs/phase6/context_prior_diagnostic.json'
RUN = ROOT/'reports/phase6/context-prior-diagnostic-20261006'
MODELS = ('historical_parent','staged_CE','conditional_KL','gold_body_replay')
SUITES = dict(bridge='source_cases',retention='retention_cases')
CONDITIONS = ('original','BOS-only')
SOURCES = ('scripts/diagnose_context_prior.py','scripts/context_prior_analysis.py',
    'scripts/diagnose_context_prior.ps1','tests/test_context_prior_analysis.py',
    'src/jmicro/japanese_evaluation.py','src/jmicro/model.py','src/jmicro/training.py',
    'src/jmicro/evaluation.py','src/jmicro/tokenizer.py','src/jmicro/experiment.py',
    'scripts/phase6_performance.py','scripts/run_eos_short_pilot.py','.python-version','uv.lock')


def reference(path):
    return dict(path=str(path),sha256=sha256(path))


def check_reference(value):
    if sha256(Path(value['path'])) != value['sha256']:
        raise ValueError('Frozen reference differs: '+value['path'])


def scope(c):
    if (c['models'] != list(MODELS) or c['conditions'] != list(CONDITIONS)
            or c['suites'] != SUITES or c['CPU_ceiling_seconds'] != 180 or c['CPU_threads'] != 8
            or c['batch'] != 16 or c['device'] != 'cpu' or c['dtype'] != 'fp32' or c['backend'] != 'math'
            or c['families_per_suite'] != 128 or c['requests_per_suite'] != 512
            or c['original_requests'] != 4096 or c['total_scored_requests'] != 8192
            or c['metrics'] != list(METRICS) or c['GPU_seconds'] or c['optimizer_updates']
            or c['Base_adopted'] or c['Base_complete'] or c['Chat_started'] or c['quantization_started']
            or c['protected_test_used'] or not c['quality_criteria_unchanged']):
        raise ValueError('Fixed read-only CPU180s/all4-model/all256-family diagnostic required')


def prepare():
    if CONFIG.exists():
        inspect();return
    p = read_json(PROPOSAL)
    if (p['total_CPU_ceiling_seconds'] != 180 or p['CPU_threads'] != 8 or p['GPU_seconds']
            or p['optimizer_updates'] or p['new_prepared_corpus_tokens'] or p['Base_complete']
            or set(p['checkpoints']) != set(MODELS) or p['fixed_protocol']['original_encoded_requests'] != 4096):
        raise ValueError('Preserve one bounded proposal')
    tests = ROOT/'reports/phase6/context_prior_analysis_tests.xml'
    cases = list(ET.parse(tests).getroot().iter('testcase'))
    if len(cases) != 2 or any(c.find(k) is not None for c in cases for k in ('failure','error','skipped')):
        raise ValueError('Actual CPU target-transform/component tests required')
    refs = dict(p['references'],proposal=reference(PROPOSAL),CPU_tests=reference(tests),
        completion=p['trigger']['current_completion'])
    for ref in (*refs.values(),*p['checkpoints'].values()):check_reference(ref)
    completion = read_json(Path(refs['completion']['path']))
    if completion['eligible_for_final_Base_validation'] or p['prior_related_GPU_seconds'] != completion['cumulative_related_GPU_seconds']:
        raise ValueError('Actual rejected gold replay comparison required')
    for key in SUITES.values():
        data = read_json(Path(refs[key]['path']))
        if len(data['families']) != 128 or [f['index'] for f in data['families']] != list(range(128)):
            raise ValueError('All128 fixed families required')
        index_cases(data['cases'],128)
    c = dict(created_at=now(),models=list(MODELS),conditions=list(CONDITIONS),suites=SUITES,
        checkpoints=p['checkpoints'],references=refs,source_sha256={f:sha256(ROOT/f) for f in SOURCES},
        CPU_ceiling_seconds=180,CPU_threads=8,batch=16,device='cpu',dtype='fp32',backend='math',
        families_per_suite=128,requests_per_suite=512,original_requests=4096,total_scored_requests=8192,
        metrics=list(METRICS),GPU_seconds=0,optimizer_updates=0,scientific_teacher_tokens=0,
        newly_prepared_source_tokens=0,Base_complete=False,Base_adopted=False,Chat_started=False,
        quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,
        interpretation_limits=p['interpretation_limits'],prior_related_GPU_seconds=p['prior_related_GPU_seconds'])
    scope(c);atomic_json(CONFIG,c);inspect()
    print('CPU-only original/BOS-only diagnostic frozen; no model scored yet',flush=True)


def inspect():
    c = read_json(CONFIG);scope(c)
    if c['source_sha256'] != {f:sha256(ROOT/f) for f in SOURCES}:
        raise ValueError('Frozen diagnostic implementation differs')
    for ref in (*c['references'].values(),*c['checkpoints'].values()):check_reference(ref)
    job_path = RUN/'job.json'
    if job_path.exists():
        old = read_json(job_path)
        if old['config_sha256'] != sha256(CONFIG) or alive(old):
            raise ValueError('Existing diagnostic binding/live process; no duplicate')
        if old.get('CPU_elapsed_seconds',0) >= 180 or 'budget exhausted' in old.get('error',''):
            raise ValueError('Fixed diagnostic budget exhausted; preserve failure, no retry')
    return c


def weight_digest(model):
    out = hashlib.sha256()
    for name,value in model.state_dict().items():
        out.update(name.encode());out.update(value.detach().contiguous().numpy().tobytes())
    return out.hexdigest()


def run():
    c = inspect();RUN.mkdir(parents=True,exist_ok=True)
    job_path = RUN/'job.json';old = read_json(job_path) if job_path.exists() else {}
    if old.get('status') == 'complete':
        print('Completed diagnostic retained; no duplicate CPU scoring');return
    prior_seconds = old.get('CPU_elapsed_seconds',0.)
    stopped = [False]
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    job = dict(status='running',**identity(),started_at=old.get('started_at',now()),
        config_sha256=sha256(CONFIG),CPU_budget_seconds=180,CPU_elapsed_seconds=prior_seconds,
        GPU_seconds=0,optimizer_updates=0,scientific_teacher_tokens=0,protected_test_used=False,
        restart_command='scripts/diagnose_context_prior.ps1 -Worker',
        source_sha256=c['source_sha256'])
    def check():
        if stopped[0]:raise InterruptedError('Interrupted read-only diagnostic; completed chunks retained')
        if prior_seconds+time.monotonic()-START > 180:
            raise TimeoutError('Fixed180s CPU diagnostic budget exhausted')
    def heartbeat(**values):
        job.update(CPU_elapsed_seconds=prior_seconds+time.monotonic()-START,heartbeat_at=now(),**values)
        atomic_json(job_path,job)
    before_rng = rng_state()
    outputs,readonly,ledgers = {},{},{}
    try:
        if torch.cuda.is_initialized() or torch.cuda.is_available():
            raise ValueError('CPU diagnostic must hide CUDA before importing torch')
        torch.set_num_threads(8);torch.use_deterministic_algorithms(True)
        heartbeat(stage='setup')
        for relative in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            target = RUN/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and target.read_bytes() != (ROOT/relative).read_bytes():
                raise ValueError('Preserve diagnostic source snapshot')
            if not target.exists():shutil.copyfile(ROOT/relative,target)
        prepared = {suite:read_json(Path(c['references'][key]['path'])) for suite,key in SUITES.items()}
        for suite,data in prepared.items():
            index_cases(data['cases'],128);atomic_json(RUN/f'{suite}-prepared.json',data)
        model_config = None
        for name in MODELS:
            check();state = torch.load(c['checkpoints'][name]['path'],map_location='cpu',weights_only=False)
            if model_config is None:model_config = state['model_config']
            if model_config != state['model_config']:
                raise ValueError('Same10M model architecture required')
            model = JMicroModel(model_config).eval()
            model.load_state_dict(state['model'],strict=True);model.requires_grad_(False);del state
            if sum(p.numel() for p in model.parameters()) != 10001152 or any(p.dtype != torch.float32 for p in model.parameters()):
                raise ValueError('Actual10,001,152-parameter FP32 CPU model required')
            restore_rng(before_rng)
            digest = weight_digest(model);model_outputs,model_ledger = {},{}
            scorer = NativeLikelihood(model,None,'cpu','fp32',16)
            hook = model.register_forward_pre_hook(lambda *_:check())
            try:
                with sdpa_kernel(SDPBackend.MATH):
                    for suite,data in prepared.items():
                        model_outputs[suite] = {};model_ledger[suite] = {}
                        for condition in CONDITIONS:
                            cases = [request(case,condition=='BOS-only') for case in data['cases']]
                            rows = [];valid_inputs=physical_inputs=target_tokens=target_bytes=0
                            for start in range(0,512,16):
                                check();batch = cases[start:start+16]
                                path = RUN/'scores'/name/suite/condition/f'{start:04d}.json'
                                bind = dict(config_sha256=sha256(CONFIG),checkpoint_sha256=c['checkpoints'][name]['sha256'],
                                    cases_sha256=c['references'][SUITES[suite]]['sha256'],condition=condition,start=start)
                                valid = sum(len(r['ids'])-1 for r in batch)
                                physical = len(batch)*max(len(r['ids'])-1 for r in batch)
                                if path.exists():
                                    saved = read_json(path)
                                    if any(saved[k] != v for k,v in bind.items()):
                                        raise ValueError('Completed score chunk binding differs')
                                    scored = saved['rows']
                                else:
                                    before = scorer.forward_tokens
                                    scored = [dict(index=case['index'],**s) for case,s in
                                        zip(batch,scorer.score_encoded(batch),strict=True)]
                                    if scorer.forward_tokens-before != valid:
                                        raise ValueError('Actual native valid input accounting differs')
                                    validate_scores(scored,batch)
                                    atomic_json(path,dict(**bind,rows=scored,valid_input_tokens=valid,
                                        physical_input_positions=physical,scored_target_tokens=sum(r['target_tokens'] for r in scored)))
                                validate_scores(scored,batch);rows.extend(scored)
                                valid_inputs+=valid;physical_inputs+=physical
                                target_tokens+=sum(r['target_tokens'] for r in scored)
                                target_bytes+=sum(r['target_bytes'] for r in scored)
                                heartbeat(stage='scoring',model=name,suite=suite,condition=condition,completed_requests=len(rows))
                            model_outputs[suite][condition] = rows
                            model_ledger[suite][condition] = dict(requests=512,valid_input_tokens=valid_inputs,
                                physical_input_positions=physical_inputs,scored_target_tokens=target_tokens,scored_target_bytes=target_bytes)
            finally:hook.remove()
            checks = dict(weights_unchanged=weight_digest(model)==digest,RNG_unchanged=equal_state(before_rng,rng_state()),
                no_gradients=all(p.grad is None and not p.requires_grad for p in model.parameters()),
                eval_mode=not model.training,CPU_FP32=all(p.device.type=='cpu' and p.dtype==torch.float32 for p in model.parameters()),
                CUDA_not_initialized=not torch.cuda.is_initialized())
            if not all(checks.values()):raise ValueError('Read-only CPU weights/RNG/eval/gradient/device invariant failed')
            readonly[name] = checks;outputs[name] = model_outputs;ledgers[name] = model_ledger
            atomic_json(RUN/f'{name}-scores.json',dict(checkpoint=c['checkpoints'][name],scores=model_outputs,ledgers=model_ledger,checks=checks))
            del model,scorer;gc.collect();check()
        all_pairs,aggregates = {},{}
        for name in MODELS:
            all_pairs[name] = {};aggregates[name] = {}
            for suite,data in prepared.items():
                rows = family_rows(outputs[name][suite]['original'],outputs[name][suite]['BOS-only'],data)
                all_pairs[name][suite] = rows;aggregates[name][suite] = {}
                for metric_name in METRICS:
                    selected = [r for r in rows if r['metric']==metric_name]
                    aggregates[name][suite][metric_name] = dict(all128=aggregate(selected),
                        by_category={cat:aggregate([r for r in selected if r['category']==cat]) for cat in sorted({r['category'] for r in selected})},
                        by_split={split:aggregate([r for r in selected if r['split']==split]) for split in ('lexical_holdout','structural_holdout')})
        comparisons,comparison_pairs = {},{}
        for before in ('historical_parent','staged_CE','conditional_KL'):
            comparisons[before] = {};comparison_pairs[before] = {}
            for suite in SUITES:
                rows = compare_rows(all_pairs[before][suite],all_pairs['gold_body_replay'][suite])
                comparison_pairs[before][suite] = rows;comparisons[before][suite] = {}
                for metric_name in METRICS:
                    selected = [r for r in rows if r['metric']==metric_name]
                    comparisons[before][suite][metric_name] = dict(all128=comparison_counts(selected),
                        by_category={cat:comparison_counts([r for r in selected if r['category']==cat]) for cat in sorted({r['category'] for r in selected})})
        total_requests = sum(v['requests'] for model in ledgers.values() for suite in model.values() for v in suite.values())
        if total_requests != 8192 or any(model[s]['original']['scored_target_tokens']!=model[s]['BOS-only']['scored_target_tokens']
                or model[s]['original']['scored_target_bytes']!=model[s]['BOS-only']['scored_target_bytes'] for model in ledgers.values() for s in SUITES):
            raise ValueError('All8192 requests and exact paired target denominators required')
        atomic_json(RUN/'family-rows.json',dict(pairs=all_pairs,comparisons=comparison_pairs))
        check()
        result = dict(status='actual_CPU4_model_all256_family_context_prior_diagnostic_complete',created_at=now(),
            config=reference(CONFIG),proposal=c['references']['proposal'],source_sha256=c['source_sha256'],
            checkpoints=c['checkpoints'],aggregates=aggregates,comparisons=comparisons,
            family_rows=reference(RUN/'family-rows.json'),all_readonly_checks=readonly,ledgers=ledgers,
            total_scored_requests=8192,original_requests=4096,neutral_requests=4096,
            CPU_elapsed_seconds=prior_seconds+time.monotonic()-START,CPU_ceiling_seconds=180,CPU_threads=8,
            precision='Both original and BOS-only recomputed CPU FP32/math; cached GPU BF16 never subtracted.',
            GPU_seconds=0,optimizer_updates=0,scientific_teacher_tokens=0,newly_prepared_source_tokens=0,
            prior_related_GPU_seconds=c['prior_related_GPU_seconds'],Base_complete=False,Base_adopted=False,
            Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,
            limitations=c['interpretation_limits'],arithmetic_limit='Cross-model component swaps are arithmetic diagnostics, not realizable independent model changes or causal training proof.')
        atomic_json(RUN/'result.json',result);atomic_json(ROOT/'reports/phase6/context_prior_diagnostic.json',result)
        job.update(status='complete',completed_at=now());heartbeat(stage='complete',total_scored_requests=8192)
        print({name:{suite:aggregates[name][suite][METRICS[0]]['all128'] for suite in SUITES} for name in MODELS},flush=True)
    except BaseException as error:
        job.update(status='failed',error=repr(error));heartbeat(stage='failed');raise
    finally:
        restore_rng(before_rng);atomic_json(job_path,job)


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p = argparse.ArgumentParser();modes=p.add_mutually_exclusive_group()
    modes.add_argument('--prepare',action='store_true');modes.add_argument('--preflight',action='store_true')
    args = p.parse_args()
    if args.prepare:prepare()
    elif args.preflight:inspect()
    else:run()
