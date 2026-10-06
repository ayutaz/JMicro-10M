"""One fixed Base-only rank-four/full-update comparison, matched fresh Adam.

Reuses completed sampling evidence, not previous training quality as a new
matched control. Both arms actually learn the identical masked 91,641,755
teachers. No data conversion, rank sweep, Chat or protected-test access.
"""
import argparse
import copy
import gc
import json
import math
import os
from pathlib import Path
import signal
import shutil
import sys
import time
import xml.etree.ElementTree as ET
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,implementation_hashes,gpu_lock,rng_state
from low_rank_base_trainer import LowRankBaseTrainer,KIND,merged_state
from phase6_performance import identity,alive,finite_state
from run_eos_short_pilot import equal_state
import run_interleaved_outcome_order as old
import run_complete_text_comparison as evaluation

RUN=ROOT/'reports/phase6/low-rank-base-comparison-v2-20261006'
PROPOSAL=ROOT/'reports/phase6/low_rank_base_v2_proposal.json'
PROBE_CONFIG=ROOT/'configs/phase6/low_rank_base_v2_probe.json'
CONFIG=ROOT/'configs/phase6/low_rank_base_v2_comparison.json'
ARMS=('full_fresh_Adam','rank4_frozen_backbone')
CEILING=1800
PROBE_CEILING=240
SOURCES=('scripts/low_rank_base_trainer.py','scripts/run_low_rank_base_comparison.py',
         'scripts/run_low_rank_base_comparison.ps1','tests/test_low_rank_base.py')
reference,check_reference=old.reference,old.check_reference


def prepare():
    if PROBE_CONFIG.exists():inspect(PROBE_CONFIG);return
    started=time.monotonic()
    previous=old.inspect(old.CONFIG);completion=ROOT/'reports/phase6/document_context_ablation_completion.json'
    result=read_json(completion)
    if result['completed_endpoint_history_dependence_marker'] or result['Base_complete']:
        raise ValueError('Retained unsupported packing result required')
    suites=list(ET.parse(ROOT/'reports/phase6/low_rank_base_tests.xml').getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=4 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Four actual CPU gradient/merge/fullstate checks required')
    for folder in (old.RUN,ROOT/'reports/phase6/document-context-ablation-20261006'):
        job=read_json(folder/'job.json')
        if job['status']!='complete' or alive(job):raise ValueError('Preceding actual jobs must terminate')
    ledger=read_json(old.LEDGER)
    if ledger['actual_masked_suffix_teacher_tokens']!=91641755 or len(ledger['rows'])!=3068:
        raise ValueError('Completed fixed input/target ledger required')
    proposal=dict(kind=KIND,created_at=now(),trigger=reference(completion),
        hypothesis='Restrict the learned update subspace rather than adding an L2 penalty or altering data/loss/order. Frozen W0 does not guarantee preserved active-model Web quality.',
        primary_sources=['https://arxiv.org/abs/2106.09685','https://github.com/microsoft/LoRA/blob/main/README.md'],
        distinct_from_failed_branches=['full-model L2 displacement anchor','full-model weight averaging','Web logit KL','packing isolation','sequence unlikelihood'],
        fixed_rank=4,scale=1,dropout=0,target_modules=['q_proj','k_proj','v_proj','o_proj','gate_proj','up_proj','down_proj'],
        same_initial_native_weights=previous['parent'],native_parameters=10001152,rank4_trainable_parameters=232960,
        temporary_rank4_training_parameters=10234112,merged_inference_parameters=10001152,
        arms=list(ARMS),optimizer_policy='Fresh AdamW in BOTH arms; same parent hyperparameters, permanent scheduler floor/clock and actual LR0.00001. Original moments retained as provenance, never claimed active.',
        input_target_budget='Each3068 updates/100532224 input/91641755 actual masked teachers; same original100M reference quota ledger. Not100M actual teachers.',
        control_policy='Actually train fresh-Adam full control. Cached inherited-Adam mixed and strong staged cells remain separately labeled historical references.',
        source_data_masks_order_decoder_unchanged=True,quality_criteria_unchanged=True,
        CPU_preparation_ceiling_seconds=30,probe_GPU_ceiling_seconds=PROBE_CEILING,total_new_GPU_ceiling_seconds=CEILING,
        GPU_seconds_so_far=0,new_teacher_tokens_so_far=0,
        merge_control=dict(dtype='fp32',backend='math',rows=4,context=1024,atol=.0002,rtol=.00002),
        numerical_policy='Evaluate native merged FP32 weights through the unchanged native BF16/math pipeline. BF16 separate-GEMM rounding is not claimed bitwise equivalent. Prior numerical7 failure preserved.',
        completion='Both actual endpoints and all160 raw-bound content reviews; unchanged strong/absolute/historical-Web gates, exact terminal identity and UI restoration. Only a qualified recipe may enter independent learned seed/full-dev/protected-test/adoption.',
        failure_policy='End fixed rank4 comparison; no rank/module/scale/LR/source/mask/decoder/checkpoint salvage sweep.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
    if PROPOSAL.exists():raise ValueError('Preserve original fixed proposal')
    atomic_json(PROPOSAL,proposal)
    c={k:copy.deepcopy(previous[k]) for k in ('parent','pool','original_web','positive_data','original_config','accepted_compact_index',
        'teacher_goals','references','old_source_sha256','implementation','source_order','remaining_updates','actual_scientific_teacher_tokens_predicted','reference_suffix_teacher_tokens')}
    c['old_source_sha256'].update(previous['source_sha256'])
    c['references'].update(proposal=reference(PROPOSAL),CPU_tests=reference(ROOT/'reports/phase6/low_rank_base_tests.xml'),
        reference_input_ledger=reference(old.LEDGER),previous_masked_mixed=reference(old.RUN/'compare-result.json'),
        previous_masked_mixed_notes=reference(old.RUN/'content-notes.json'))
    c.update(research_kind=KIND,phase='probe',arms=list(ARMS),source_sha256={s:sha256(ROOT/s) for s in SOURCES},
        peak_lr=.00001,optimizer_policy='fresh_Adam_both_arms',rank=4,adapter_scale=1,adapter_dropout=0,
        merge_control=proposal['merge_control'],GPU_budget_seconds=PROBE_CEILING,total_new_GPU_ceiling_seconds=CEILING,
        CPU_preparation_seconds=time.monotonic()-started,quality_criteria_unchanged=True,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
    if c['CPU_preparation_seconds']>30:raise TimeoutError('CPU preparation30s exhausted')
    atomic_json(PROBE_CONFIG,c);inspect(PROBE_CONFIG)
    print(json.dumps(dict(status='fixed_rank4_comparison_prepared',CPU_seconds=c['CPU_preparation_seconds'],new_GPU_seconds=0)),flush=True)


def inspect(path):
    c=read_json(path)
    if (c['research_kind']!=KIND or c['arms']!=list(ARMS) or c['rank']!=4 or c['adapter_scale']!=1 or c['adapter_dropout']!=0
            or c['optimizer_policy']!='fresh_Adam_both_arms' or c['peak_lr']!=.00001 or c['remaining_updates']!=3068
            or c['actual_scientific_teacher_tokens_predicted']!=91641755 or c['total_new_GPU_ceiling_seconds']!=CEILING
            or c['implementation']!=implementation_hashes() or c['Base_complete'] or c['Base_adopted']
            or c['Chat_started'] or c['quantization_started'] or c['protected_test_used'] or not c['quality_criteria_unchanged']):
        raise ValueError('Fixed Base-only rank-four recipe differs')
    for relative,digest in {**c['old_source_sha256'],**c['source_sha256']}.items():
        if sha256(ROOT/relative)!=digest:raise ValueError('Frozen source differs: '+relative)
    for ref in (*c['references'].values(),c['parent'],c['accepted_compact_index'],c['original_config']):check_reference(ref)
    folder=RUN/'probe' if path==PROBE_CONFIG else RUN
    if (folder/'job.json').exists() and alive(read_json(folder/'job.json')):raise ValueError('Actual live job; no duplicate')
    if path==PROBE_CONFIG:
        if c['phase']!='probe' or c['GPU_budget_seconds']!=PROBE_CEILING:raise ValueError('Own240s probe required')
    elif path==CONFIG:
        r=probe_evidence();timings,estimate=estimate_training(r)
        if (c['phase']!='scientific' or c['probe_result_sha256']!=sha256(RUN/'probe/result.json')
                or c['probe_config_sha256']!=sha256(PROBE_CONFIG) or c['measured_timing']!=timings
                or c['estimated_GPU_seconds_with_margin']!=estimate or estimate+r['GPU_seconds']>CEILING
                or c['verification_GPU_seconds']!=r['GPU_seconds']
                or not math.isclose(c['GPU_budget_seconds']+r['GPU_seconds'],CEILING,abs_tol=1e-9)):
            raise ValueError('Own measured cumulative budget differs')
    else:raise ValueError('Only fixed probe/science paths allowed')
    return c


def probe_evidence():
    r=read_json(RUN/'probe/result.json');job=read_json(RUN/'probe/job.json')
    if (job['status']!='complete' or alive(job) or r['GPU_seconds']!=job['GPU_elapsed_seconds']
            or r['GPU_seconds']>PROBE_CEILING or r['config_sha256']!=sha256(PROBE_CONFIG)
            or any(not all(r['arms'][a]['initial_checks'].values()) or not r['arms'][a]['gate']['passed']
                   or not r['arms'][a]['merge']['allclose'] for a in ARMS)):
        raise ValueError('Both actual finite CUDA resume/merge probes must terminate')
    return r


def estimate_training(r):
    timings={};estimate=0.
    for arm in ARMS:
        t,e=old.estimate_training({'timing':r['arms'][arm]['timing']},3068)
        timings[arm]=t;estimate+=e
    return timings,estimate


def freeze():
    if CONFIG.exists():inspect(CONFIG);return
    c=copy.deepcopy(inspect(PROBE_CONFIG));r=probe_evidence();timings,estimate=estimate_training(r)
    if estimate+r['GPU_seconds']>CEILING:raise ValueError('Actual two-arm cost exceeds1800s; no science')
    c.update(phase='scientific',probe_config_sha256=sha256(PROBE_CONFIG),probe_result_sha256=sha256(RUN/'probe/result.json'),
        measured_timing=timings,estimated_GPU_seconds_with_margin=estimate,verification_GPU_seconds=r['GPU_seconds'],
        verification_teacher_tokens=r['verification_teacher_tokens'],GPU_budget_seconds=CEILING-r['GPU_seconds'],save_every_updates=250)
    atomic_json(CONFIG,c);inspect(CONFIG);print(json.dumps(dict(status='two_arm_science_frozen',estimated_seconds=estimate,timing=timings)),flush=True)


def binding(c,path,arm):
    return dict(config_sha256=sha256(path),arm=arm,parent=c['parent'],study_kind=KIND,teacher_goals=c['teacher_goals'],
        target_rule='original mixed conditional outcome+EOS only',optimizer_policy='fresh_Adam_both_arms',peak_lr=.00001)


def merge_control(t,pool,original,positive,c,parent):
    sampler=old.InterleavedOutcomeSampler(pool,original,positive,old.historical_web_cursor(parent),c['teacher_goals'])
    sampler.reference_token_digest=parent['token_digest'];x=sampler.batch(32)[0][:4].to(t.device)
    native=JMicroModel(t.model.config).to(t.device);native.load_state_dict(merged_state(t.model));native.eval();t.model.eval()
    with torch.no_grad(),sdpa_kernel(SDPBackend.MATH):
        unmerged=t.model(x,training_fast_path=True).logits;merged=native(x,training_fast_path=True).logits
    d=(unmerged-merged).abs();rule=c['merge_control']
    result=dict(allclose=bool(torch.allclose(unmerged,merged,atol=rule['atol'],rtol=rule['rtol'])),
        max_absolute_error=float(d.max()),RMS_error=float(d.square().mean().sqrt()),rule=rule,
        native_parameter_count=sum(p.numel() for p in native.parameters()),frozen_backbone_unchanged=True)
    t.audit_parameters();t.model.train()
    if not result['allclose'] or result['native_parameter_count']!=10001152:raise ValueError('Own actual FP32 native merge control failed')
    del native;return result


def run(probe=False):
    path=PROBE_CONFIG if probe else CONFIG;c=inspect(path);output=RUN/'probe' if probe else RUN
    output.mkdir(parents=True,exist_ok=True);jp=output/'job.json';previous_job=read_json(jp) if jp.exists() else {}
    if previous_job and previous_job['config_sha256']!=sha256(path):raise ValueError('Interrupted recipe differs')
    if previous_job.get('status')=='complete':print('Completed rank4 run retained');return
    previous=previous_job.get('GPU_elapsed_seconds',0.);started=[None];stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(path),GPU_elapsed_seconds=previous,started_at=now(),
        restart_command=f"scripts/run_low_rank_base_comparison.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Interrupted; completed updates retained')
        if started[0] is not None and previous+time.monotonic()-started[0]>c['GPU_budget_seconds']:raise TimeoutError('Cumulative fixed GPU ceiling exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['GPU_elapsed_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True);heartbeat('setup')
        for relative in (*c['source_sha256'],*c['old_source_sha256'],*c['implementation'],path.relative_to(ROOT).as_posix()):
            target=output/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and target.read_bytes()!=(ROOT/relative).read_bytes():raise ValueError('Frozen snapshot differs')
            if not target.exists():shutil.copyfile(ROOT/relative,target)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);pool,original,positive=old.data(c)
        base=read_json(Path(c['original_config']['path']));ledger=read_json(Path(c['references']['reference_input_ledger']['path']))
        with gpu_lock('cuda'):
            started[0]=time.monotonic();heartbeat('GPU');progress=output/'progress-result.json'
            result=read_json(progress) if progress.exists() else dict(arms={})
            for arm in ARMS:
                record=result['arms'].setdefault(arm,{});b=binding(c,path,arm)
                def build():return LowRankBaseTrainer(parent,pool,original,positive,c['teacher_goals'],b,arm)
                if probe:
                    if 'initial_checks' not in record:
                        t=build();checks=dict(model=equal_state(merged_state(t.model),parent['model']),
                            fresh_Adam=not bool(t.optimizer.state),scheduler=equal_state(t.scheduler.state_dict(),parent['scheduler']),
                            RNG=equal_state(rng_state(),parent['rng']),native_count=t.native_count==10001152,
                            trainable_count=t.trainable_count==(232960 if arm==ARMS[1] else 10001152),
                            actual_Web_cursor=equal_state(t.sampler.streams['web'].sampler.state_dict(),parent['sampler']['web']),
                            actual_parent_sampler_lineage=equal_state(t.lineage['actual_parent_sampler'],parent['sampler']),
                            actual_LR=all(g['lr']==.00001 for g in t.optimizer.param_groups))
                        if not all(checks.values()):raise ValueError('Initial matched fresh-Adam state differs: '+repr(checks))
                        record['initial_checks']=checks;del t;gc.collect();torch.cuda.empty_cache()
                    record['gate']=old.resume_gate(build,output/arm/'resume-gate',sha256(path),check)
                    if 'timing' not in record:
                        folder=output/arm/'timing';folder.mkdir(parents=True,exist_ok=True);t=build();cp=old.prior.latest(folder)
                        if cp is not None:t.load(cp)
                        log=folder/'metrics.jsonl';old.prior.reconcile(log,t.update,parent['update'])
                        with log.open('a',buffering=1) as stream:
                            while t.update-parent['update']<32:
                                try:check()
                                except (InterruptedError,TimeoutError):t.save(folder/'checkpoint.pt');raise
                                row=t.step();stream.write(json.dumps(row,allow_nan=False)+'\n')
                                if (t.update-parent['update'])%8==0:heartbeat('own-timing',arm=arm,completed_updates=t.update-parent['update'])
                        cp=folder/'checkpoint.pt';saved=t.save(cp)
                        if not finite_state(torch.load(cp,map_location='cpu',weights_only=False)):raise ValueError('Own timing state nonfinite')
                        record['timing']=dict(histories=[json.loads(s) for s in log.read_text().splitlines()],terminal_save_seconds=saved,
                            verification_teacher_tokens=t.supervised_tokens-parent['supervised_tokens'],checkpoint=reference(cp),
                            peak_VRAM_bytes=torch.cuda.max_memory_allocated())
                        record['merge']=merge_control(t,pool,original,positive,c,parent)
                        del t;gc.collect();torch.cuda.empty_cache()
                else:
                    if 'checkpoint' not in record:
                        folder=output/arm/'training';folder.mkdir(parents=True,exist_ok=True);t=build();cp=old.prior.latest(folder)
                        if cp is not None:t.load(cp)
                        log=folder/'metrics.jsonl';seconds=old.prior.reconcile(log,t.update,parent['update'])
                        with log.open('a',buffering=1) as stream:
                            while t.sampler.source_teachers!=c['teacher_goals']:
                                try:check()
                                except (InterruptedError,TimeoutError):t.save(folder/f'checkpoint-{t.update:08d}.pt');raise
                                row=t.step();expected=ledger['rows'][t.update-parent['update']-1]
                                if (row['reference_token_digest']!=expected['reference_token_digest']
                                        or row['actual_source_routes']!=expected['actual_source_routes']):raise ValueError('Actual same-input/mask route differs')
                                seconds+=row['seconds'];stream.write(json.dumps(row,allow_nan=False)+'\n')
                                if (t.update-parent['update'])%20==0:heartbeat('Base-training',arm=arm,completed_updates=t.update-parent['update'],total_updates=3068,
                                    actual_teachers=row['additional_teacher_tokens'],loss=row['loss'])
                                if (t.update-parent['update'])%250==0:t.save(folder/f'checkpoint-{t.update:08d}.pt')
                        cp=folder/f'checkpoint-{t.update:08d}.pt';t.save(cp)
                        if (t.update-parent['update']!=3068 or t.supervised_tokens-parent['supervised_tokens']!=91641755
                                or t.sampler.actual!=ledger['actual_source_accounting'] or t.sampler.source_digests!=ledger['source_digests']
                                or not equal_state(t.sampler.reference_state(),ledger['terminal_reference_sampler'])):
                            raise ValueError('Completed same teachers/windows/cursors required')
                        record['checkpoint']=dict(checkpoint=str(cp),checkpoint_sha256=sha256(cp),binding=b,updates=3068,
                            additional_supervised_tokens=t.supervised_tokens-parent['supervised_tokens'],additional_input_tokens=t.tokens-parent['tokens'],
                            actual_body_bytes=t.body_bytes-parent['body_bytes'],reference_suffix_teacher_tokens=100000000,
                            actual_source_accounting=t.sampler.actual,sampler=t.sampler.state_dict(),token_digest=t.token_digest,
                            reference_token_digest=t.sampler.reference_token_digest,source_digests=t.sampler.source_digests,
                            training_seconds=seconds,trainable_parameters=t.trainable_count,native_parameters=t.native_count,
                            frozen_backbone_unchanged=bool(t.targets))
                        record['merge']=merge_control(t,pool,original,positive,c,parent)
                        atomic_json(progress,result);del t;gc.collect();torch.cuda.empty_cache()
                    if 'evaluation' not in record:
                        evaluation.RUN=output/'evaluation';dev=Shard(Path(base['dev_shards']),'dev');tok=Tokenizer(ROOT/base['tokenizer'])
                        record['evaluation']=evaluation.evaluate(arm,record['checkpoint'],dev,tok,base,b,heartbeat,check,started[0]+c['GPU_budget_seconds']-previous)
                atomic_json(progress,result)
            if probe:
                result.update(GPU_optimizer_updates=96,verification_teacher_tokens=sum(r['gate']['verification_teacher_tokens']+r['timing']['verification_teacher_tokens'] for r in result['arms'].values()),
                    scientific_teacher_tokens=0,weights_discarded_for_science=True,passed=True)
            else:
                result.update(scientific_teacher_tokens=183283510,scientific_optimizer_updates=6136,
                    exact_matched_input_targets_and_source_cursors=True,previous_inherited_Adam_not_claimed_matched_new_control=True)
            check();elapsed=previous+time.monotonic()-started[0]
            result.update(status='own_two_arm_CUDA_probe_complete' if probe else 'two_arm_GPU_complete_pending_all160_content_review',config_sha256=sha256(path),GPU_seconds=elapsed,
                Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True)
            atomic_json(output/('result.json' if probe else 'compare-result.json'),result)
            job.update(status='complete',GPU_elapsed_seconds=elapsed,completed_at=now())
    except BaseException as error:job.update(status='failed_or_interrupted',error=repr(error));raise
    finally:
        if started[0] is not None and job['status']!='complete':job['GPU_elapsed_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2);parser=argparse.ArgumentParser();modes=parser.add_mutually_exclusive_group()
    for mode in ('prepare','preflight-probe','probe','freeze','inspect'):modes.add_argument('--'+mode,action='store_true')
    args=parser.parse_args()
    if args.prepare:prepare()
    elif args.preflight_probe:inspect(PROBE_CONFIG)
    elif args.freeze:freeze()
    elif args.inspect:inspect(CONFIG)
    else:run(args.probe)
