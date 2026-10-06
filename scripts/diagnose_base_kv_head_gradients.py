"""One fixed TRAIN-only, zero-update native shared K/V head-gradient diagnostic."""
import argparse
import gc
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock,rng_state
from natural_context_contrast_corpus import OriginalTrainCorpusSampler,GENRES
from natural_context_contrast_trainer import right_pad,host
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive
from base_kv_head_gradient_diagnostic import decompose,path_statistics,interference_screen

CONFIG=ROOT/'configs/phase6/base_kv_head_gradient_diagnostic.json'
RUN=ROOT/'reports/phase6/base-kv-head-gradient-diagnostic-20261007'
PAYLOAD=ROOT/'reports/phase6/base_embedding_gradient_payload.json'
SOURCES=('scripts/base_kv_head_gradient_diagnostic.py','scripts/diagnose_base_kv_head_gradients.py',
    'scripts/diagnose_base_kv_head_gradients.ps1','tests/test_base_kv_head_gradient_diagnostic.py',
    'scripts/natural_context_contrast_corpus.py','scripts/natural_context_contrast_trainer.py',
    'scripts/natural_context_contrast_memory.py','scripts/phase6_performance.py',
    'src/jmicro/model.py','src/jmicro/training.py','src/jmicro/tokenizer.py','src/jmicro/phase5.py','uv.lock')


def ref(path):return dict(path=str(path),sha256=sha256(path))


def prepare():
    if CONFIG.exists() or (RUN/'job.json').exists():
        raise ValueError('Preserve fixed one-shot head diagnostic; no reroll')
    started=time.monotonic()
    old=read_json(ROOT/'configs/phase6/base_embedding_gradient_diagnostic.json')
    closed=ROOT/'reports/phase6/base_label_smoothing_comparison_completion.json'
    completion=read_json(closed)
    job=read_json(ROOT/'reports/phase6/base-label-smoothing-comparison-20261007/job.json')
    if not completion['closed_fixed_epsilon0p1_full4096'] or job['status']!='complete' or alive(job):
        raise ValueError('Actual closed smoothing experiment required before any new assay')
    tests=ROOT/'reports/phase6/base_kv_head_gradient_tests.xml'
    suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)<5 or any(int(s.attrib[k]) for s in suites for k in ('errors','failures','skipped')):
        raise ValueError('Successful actual CPU head-attribution checks required')
    if ref(PAYLOAD)!=old['payload']:raise ValueError('Previously frozen TRAIN payload changed')
    payload=read_json(PAYLOAD)
    if not payload['TRAIN_only'] or len(payload['documents'])!=24 or not 24<=len(payload['rows'])<=48:
        raise ValueError('Same24 fixed TRAIN-only selections required')
    matches=[];examined=0
    excluded={Path(name).name for name in SOURCES[:4]}
    for folder,glob in ((ROOT/'scripts','*.py'),(ROOT/'configs/phase6','*.json')):
        for candidate in sorted(folder.glob(glob)):
            if candidate.name in excluded:continue
            examined+=1
            text=candidate.read_text().lower()
            if any(marker in text for marker in ('kv_head_gradient_diagnostic','query_head_offsets','severe_kv_head_conflict')):
                matches.append(candidate.relative_to(ROOT).as_posix())
    if matches:raise ValueError('Potential duplicate registered head attribution: '+repr(matches))
    references={name:ref(ROOT/'reports/phase6'/name) for name in (
        'base_failure_route_synthesis.json','base_intervention_gap_synthesis.json',
        'base_capacity_reference_synthesis.json','base_label_smoothing_comparison_review.json',
        'natural_context_contrast_comparison_review.json','base_residual_dropout_comparison_review.json')}
    newest=read_json(ROOT/'reports/phase6/base_label_smoothing_comparison_review.json')
    synthesis=dict(created_at=now(),status='cached_negative_routes_and_smoothing_reconciled_no_new_scoring',references=references,
        latest_summaries=newest['summaries'],latest_gates=newest['strong_and_matched_quality'],
        latest_final_validation_eligible=newest['eligible_for_final_Base_validation'],
        next_hypothesis='Broad opposition between the two query-head contributions to each shared K/V projection. Existing architecture sweep retained two queries per KV, and loss regularizers did not solve coherence.',
        prior8K_already_trained=True,no_8K_or_depth_width_sweep_repeated=True,
        local_novelty_files_checked=examined,local_novelty_matches=matches,
        novelty_scope='Top-level scripts/*.py and configs/phase6/*.json, fixed textual markers; not an external or global claim.',
        actual_GPU_seconds=0,new_scientific_teacher_tokens=0,new_content_judgments=0,
        Base_complete=False,Chat_started=False,quantization_started=False,protected_test_used=False)
    synthesis_path=ROOT/'reports/phase6/base_post_smoothing_root_synthesis.json'
    if synthesis_path.exists():raise ValueError('Preserve cached synthesis')
    atomic_json(synthesis_path,synthesis)
    c=dict(created_at=now(),payload=old['payload'],checkpoints=old['checkpoints'],checkpoint_identity=old['checkpoint_identity'],
        previous_completion=ref(closed),CPU_tests=ref(tests),evidence_synthesis=ref(synthesis_path),
        sources={p:sha256(ROOT/p) for p in SOURCES},source_binding=old['source_binding'],
        documents_per_source=8,batch=4,maximum_rows=48,GPU_limit_seconds=180,
        native_parameters=10001152,precision='FP32 math; TF32 disabled',
        attribution='Two zero additive pre-RoPE K/V offsets expose gradients per query head. Sum per-head d(projected_K/V) outer normalized input equals original shared K/V weight gradient. Original model/config/parameters remain unchanged.',
        hypothesis='Substantial broad gradient cancellation within GQA groups may warrant one fixed attention-capacity comparison; this is not an asserted cause or proof of MHA improvement.',
        research_screen=dict(cosine_at_most=-.1,cancellation_at_most=.9,minimum_sources=2,require_both_checkpoints=True,
            aggregation='Target-weighted source mean across all13 layers/two KV groups; local group statistics reported without selecting favourable groups.',Base_quality_gate=False),
        completion='Both fixed original10B and cached CE100M endpoints, same24 TRAIN families/first-last windows, all26 shared K/V groups. Exact native logits/loss, all full K/V gradient sums, unchanged weights/RNG/no accumulated grads/forward restoration. No updates or DEV/TEST.',
        failure_policy='If broad screen fails at either endpoint, close this marker and do not launch MHA/gradient surgery on its basis. No threshold/group/layer/sample rescue. Failure does not prove GQA representation capacity adequate.',
        references=[dict(url='https://aclanthology.org/2023.emnlp-main.298/',meaning='Primary paper reports GQA quality close to MHA with efficient decoding at different model scales; does not establish harm or a cure for JMicro10M.')],
        preparation_CPU_wall_seconds=time.monotonic()-started,new_GPU_seconds=0,optimizer_updates=0,new_scientific_CE_teachers=0,
        Base_complete=False,Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True)
    if c['preparation_CPU_wall_seconds']>30:raise TimeoutError('Fixed CPU preparation budget exceeded')
    atomic_json(CONFIG,c)
    print(json.dumps(dict(status='TRAIN_only_KV_attribution_frozen',documents=24,rows=len(payload['rows']),config_sha256=sha256(CONFIG),CPU_seconds=c['preparation_CPU_wall_seconds'])))


def inspect():
    c=read_json(CONFIG)
    for name in ('payload','previous_completion','CPU_tests','evidence_synthesis'):
        if sha256(Path(c[name]['path']))!=c[name]['sha256']:raise ValueError('Frozen reference changed: '+name)
    for name,digest in c['sources'].items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen source changed: '+name)
    for name,reference in c['checkpoints'].items():
        st=Path(reference['path']).stat();saved=c['checkpoint_identity'][name]
        if (st.st_size,st.st_mtime_ns)!=(saved['size'],saved['mtime_ns']):raise ValueError('Frozen checkpoint identity changed')
    old_job=read_json(ROOT/'reports/phase6/base-label-smoothing-comparison-20261007/job.json')
    if alive(old_job) or old_job['status']!='complete':raise ValueError('Previous scientific job still active')
    if (RUN/'job.json').exists():raise ValueError('Preserve attempted one-shot evidence; inspect actual identity')
    return c


def run():
    c=inspect();payload=read_json(Path(c['payload']['path']))
    if not torch.cuda.is_available():raise RuntimeError('Actual CUDA hardware required')
    RUN.mkdir(parents=True,exist_ok=True)
    job=dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),
        optimizer_updates=0,scientific_teacher_tokens=0,Base_complete=False,
        restart_command='One-shot readonly diagnostic: inspect terminal/partial evidence; no blind rerun.')
    atomic_json(RUN/'job.json',job)
    endpoints={};started=None
    def check(*args):
        if args or started is not None and time.monotonic()-started>c['GPU_limit_seconds']:
            raise TimeoutError('Fixed attribution GPU180s exhausted')
    try:
        for name in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/'source'/name;target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(ROOT/name,target)
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
        with gpu_lock('cuda'):
            started=time.monotonic();signal.signal(signal.SIGALRM,check);signal.alarm(c['GPU_limit_seconds'])
            job.update(status='running',memory_policy=configure_resident_memory(0))
            atomic_json(RUN/'job.json',job)
            for name,reference in c['checkpoints'].items():
                check()
                if sha256(Path(reference['path']))!=reference['sha256']:raise ValueError('Native checkpoint SHA differs')
                state=torch.load(reference['path'],map_location='cpu',weights_only=False)
                model=JMicroModel(state['model_config']).to('cuda').eval()
                model.load_state_dict(state['model'],strict=True)
                if sum(p.numel() for p in model.parameters())!=c['native_parameters']:raise ValueError('Exact native10M required')
                saved_rng=host(rng_state());measured=[];sources={}
                for genre in GENRES:
                    rows=[r for r in payload['rows'] if r['source']==genre]
                    first_sum=second_sum=None;teachers=0
                    for start in range(0,len(rows),c['batch']):
                        check();batch=rows[start:start+c['batch']]
                        ids,_=right_pad([r['input_ids'] for r in batch],'cuda')
                        targets=torch.full_like(ids,-100)
                        for index,row in enumerate(batch):targets[index,:len(row['target_ids'])]=torch.tensor(row['target_ids'],device='cuda')
                        with sdpa_kernel(SDPBackend.MATH):stats,a,b=decompose(model,ids,targets)
                        torch.cuda.synchronize();count=stats['teachers'];teachers+=count
                        # Per-batch CE gradients are means. Aggregate by exact target counts.
                        if first_sum is None:first_sum=a.double()*count;second_sum=b.double()*count
                        else:first_sum+=a.double()*count;second_sum+=b.double()*count
                        measured.append(dict(source=genre,row_ids=[r['id'] for r in batch],**stats))
                        job.update(stage=name+'-'+genre,completed_batches=sum(len(e['batches']) for e in endpoints.values())+len(measured),
                            heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started)
                        atomic_json(RUN/'job.json',job)
                        atomic_json(RUN/'partial-result.json',dict(endpoints=endpoints,current_endpoint=name,current_batches=measured))
                        del ids,targets,a,b
                    mean_first,mean_second=first_sum/teachers,second_sum/teachers
                    sources[genre]=path_statistics(mean_first,mean_second)
                    d=model.config['head_dim'];kv=model.config['num_key_value_heads'];group_rows=2*d
                    source_groups=[]
                    for layer in range(model.config['num_hidden_layers']):
                        for group in range(kv):
                            at=(layer*kv+group)*group_rows
                            a=mean_first[at:at+group_rows];b=mean_second[at:at+group_rows]
                            source_groups.append(dict(layer=layer,KV_group=group,query_heads=[group*2,group*2+1],
                                combined=path_statistics(a,b),K=path_statistics(a[:d],b[:d]),V=path_statistics(a[d:],b[d:])))
                    sources[genre]['groups']=source_groups
                    sources[genre]['locally_opposed_groups']=sum(g['combined']['cosine']<=-.1 for g in source_groups)
                    sources[genre].update(teachers=teachers,rows=len(rows),documents=8)
                    del first_sum,second_sum
                checks=dict(weights_unchanged=equal_state(state['model'],host(model.state_dict())),
                    native_tied=model.lm_head.weight is model.model.embed_tokens.weight,
                    RNG_unchanged=equal_state(saved_rng,host(rng_state())),no_accumulated_grads=all(p.grad is None for p in model.parameters()),
                    all_fixed_rows_measured=[v for batch in measured for v in batch['row_ids']]==[r['id'] for r in payload['rows']],
                    forward_dispatch_restored=all('forward' not in block.self_attn.__dict__ for block in model.model.layers))
                if not all(checks.values()):raise ValueError('Actual readonly native invariants failed: '+repr(checks))
                endpoints[name]=dict(checkpoint=reference,sources=sources,batches=measured,
                    native_checks=checks,screen=interference_screen(sources))
                atomic_json(RUN/'partial-result.json',dict(endpoints=endpoints))
                del model,state;gc.collect();torch.cuda.empty_cache()
            screen=all(e['screen']['passed'] for e in endpoints.values())
            signal.alarm(0);elapsed=time.monotonic()-started
            if elapsed>c['GPU_limit_seconds']:raise TimeoutError('Final actual GPU limit exceeded')
            result=dict(status='complete',created_at=now(),actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
                config_sha256=sha256(CONFIG),payload=c['payload'],endpoints=endpoints,
                severe_interference_at_both_endpoints=screen,GPU_occupancy_seconds=elapsed,
                peak_allocated_bytes=torch.cuda.max_memory_allocated(),optimizer_updates=0,
                scientific_CE_teachers=0,diagnostic_target_positions=sum(b['teachers'] for e in endpoints.values() for b in e['batches']),
                new_original_training_tokens=0,DEV_used=False,protected_test_used=False,
                new_parameters_saved=0,Base_complete=False,Base_adopted=False,
                Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,
                fixed_diagnostic_closed=True,
                next_action=('Define one fixed attention-sharing capacity comparison with10M total parameters/byte and GPU budgets; no automatic architecture launch or adoption.' if screen else
                    'Close this sampled broad GQA head-gradient cancellation marker; no MHA/gradient surgery on its basis and no group/layer/threshold/sample rescue. Select a genuinely different Base mechanism from existing evidence.'),
                limitations='Only8 distinct TRAIN families per source, index-byte biased first/last windows, two reused endpoints. Per-query-head shared K/V gradient statistics are local teacher-forcing diagnostics, not causal proof, a necessity test for every GQA representation limit or new Base-quality evidence. Both forwards use FP32 math, not the scientific BF16 flash path.')
            atomic_json(RUN/'result.json',result)
            atomic_json(ROOT/'reports/phase6/base_kv_head_gradient_result.json',result)
            job.update(status='complete',ended_at=now(),GPU_occupancy_seconds=elapsed)
            atomic_json(RUN/'job.json',job)
            print(json.dumps(dict(status='complete',GPU_seconds=elapsed,severe_interference=screen),ensure_ascii=False))
    except BaseException as error:
        signal.alarm(0);job.update(status='failed',ended_at=now(),error=repr(error),
            GPU_occupancy_seconds=0 if started is None else time.monotonic()-started)
        atomic_json(RUN/'job.json',job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();options=parser.add_mutually_exclusive_group()
    options.add_argument('--prepare',action='store_true');options.add_argument('--inspect',action='store_true')
    args=parser.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Frozen TRAIN-only attribution preflight passed; GPU0')
    else:run()
