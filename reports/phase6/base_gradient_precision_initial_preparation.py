"""One fixed original-TRAIN assay: FP32 gradients vs BF16 math and flash."""
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
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, read_json, now, sha256
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.training import atomic_json, gpu_lock, rng_state
from natural_context_contrast_memory import configure_resident_memory
from natural_context_contrast_trainer import host, right_pad, right_padded_hidden
from phase6_performance import identity, alive
from base_gradient_precision import comparison, screen

CONFIG = ROOT/'configs/phase6/base_gradient_precision.json'
RUN = ROOT/'reports/phase6/base-gradient-precision-20261007'
PAYLOAD = ROOT/'reports/phase6/base_gradient_precision_payload.json'
SOURCES = ('scripts/base_gradient_precision.py','scripts/diagnose_base_gradient_precision.py',
    'scripts/diagnose_base_gradient_precision.ps1','tests/test_base_gradient_precision.py',
    'scripts/natural_context_contrast_trainer.py','scripts/natural_context_contrast_memory.py',
    'scripts/phase6_performance.py','src/jmicro/model.py','src/jmicro/training.py','src/jmicro/phase5.py','uv.lock')


def reference(path):
    return dict(path=str(path),sha256=sha256(path))


def prepare():
    if CONFIG.exists() or PAYLOAD.exists() or (RUN/'job.json').exists():
        raise ValueError('Preserve fixed one-shot assay; no reselection')
    started = time.monotonic()
    tests = ROOT/'reports/phase6/base_gradient_precision_tests.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=4 or any(int(s.attrib[k]) for s in suites for k in ('errors','failures','skipped')):
        raise ValueError('Four actual successful CPU checks required')
    previous = ROOT/'reports/phase6/base_context_mixing_comparison_completion.json'
    finished = read_json(previous)
    previous_job = read_json(ROOT/'reports/phase6/base-context-mixing-comparison-20261007/job.json')
    if (alive(previous_job) or previous_job['status']!='complete' or not finished['fixed_ContextMixing_condition_closed']
            or finished['eligible_for_final_Base_validation']):
        raise ValueError('Previous science must actually finish and be closed')
    old_config = ROOT/'configs/phase6/base_embedding_gradient_diagnostic.json'
    old = read_json(old_config)
    old_payload = Path(old['payload']['path'])
    if sha256(old_payload)!=old['payload']['sha256']: raise ValueError('Prior fixed original TRAIN rows changed')
    payload = read_json(old_payload)
    rows = payload['rows']
    if len(rows)!=24 or any(len([r for r in rows if r['source']==g])!=8 for g in ('web','textbook','story')):
        raise ValueError('Reuse exactly the24 previously selected original TRAIN documents')
    capacity_record = ROOT/'reports/phase6/natural_context_contrast_capacity_preparation.json'
    capacity = read_json(capacity_record)
    capacity_path = Path(capacity['payload']['path'])
    if sha256(capacity_path)!=capacity['payload']['sha256']: raise ValueError('Original long TRAIN window changed')
    long = read_json(capacity_path)
    if long['original_record']['split']!='train' or len(long['window']['input_ids'])!=1024:
        raise ValueError('Original TRAIN1024 capacity window required')
    stress = dict(id='fixed-original-TRAIN-long-window',source='stress1024',
        input_ids=long['window']['input_ids'],target_ids=long['window']['target_ids'],
        source_family=long['original_record'].get('source_family'),
        index_byte_position=long['index_byte_position'],index_record_sha256=long['index_record_sha256'])
    atomic_json(PAYLOAD,dict(rows=[*rows,stress],new_source_draws=0,original24_document_payload=reference(old_payload),
                            original_long_window_payload=reference(capacity_path)))
    references = {name:reference(ROOT/'reports/phase6'/name) for name in
        ('root_cause_numeric.json','root_cause_precision-contract.json','base_decode_cached_evidence_review.json',
         'base_embedding_gradient_result.json','base_context_mixing_comparison_completion.json')}
    checkpoints = old['checkpoints']
    atomic_json(CONFIG,dict(created_at=now(),status='fixed_readonly_assay_pre_GPU',payload=reference(PAYLOAD),
        references=references,CPU_tests=reference(tests),checkpoints=checkpoints,
        checkpoint_identity={k:dict(bytes=Path(v['path']).stat().st_size,mtime_ns=Path(v['path']).stat().st_mtime_ns) for k,v in checkpoints.items()},
        source_sha256={name:sha256(ROOT/name) for name in SOURCES},original_source_binding=old['source_binding'],
        native_parameters=10001152,batch=4,GPU_limit_seconds=120,
        paths=['fp32_math','bf16_math','bf16_flash'],FP32_TF32=False,
        supervision='Identical original gold body/EOS mask, same original positions, no new labels or boundary tokens',
        assay='All distinct native parameter gradients, target-count weighted original source averages, and ephemeral fresh AdamW first data-step direction after global clip1/eps1e-8; no parameter/optimizer update',
        hypothesis='BF16 training gradients may substantially differ from FP32 even when FP32 inference also repeats. Prior diagnostics compare3 parameter gradients between BF16 backends, not all-parameter FP32-vs-BF16 training directions.',
        research_screen=dict(minimum_reference_norm=1e-6,gradient_cosine_below=.99,gradient_relative_L2_above=.10,
            fresh_AdamW_data_direction_cosine_below=.98,fresh_AdamW_data_direction_relative_L2_above=.20,
            any_of_four_metrics=True,minimum_original_sources=2,require_both_endpoints=True,require_same_BF16_path=True,
            stress_and_per_group_metrics_descriptive_only=True,Base_quality_gate=False),
        completion='All25 fixed windows at both endpoints and three precision/backend paths; unchanged native weights/tie/RNG/no accumulated grads; full records and original-source aggregates. Close one-shot regardless of screen.',
        failure_policy='Absent severe same-path marker at both endpoints, no FP32 or precision-repair training from this assay, no sample/backend/threshold/batch/cap rescue. Retain old7 numerical failures. Positive marker only permits a separately defined controlled comparison, not a quality claim.',
        primary_sources=['https://docs.pytorch.org/docs/stable/notes/amp_examples.html',
                         'https://docs.pytorch.org/docs/main/notes/numerical_accuracy.html'],
        preparation_CPU_seconds=time.monotonic()-started,optimizer_updates=0,scientific_teacher_tokens=0,
        new_unique_data_tokens=0,new_source_draws=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True))
    print(json.dumps(dict(status='fixed25_TRAIN_windows_two_endpoints_gradient_assay',config_sha256=sha256(CONFIG),GPU_seconds=0)))


def inspect():
    c = read_json(CONFIG)
    if (RUN/'job.json').exists(): raise ValueError('Inspect existing actual one-shot identity; never blindly restart')
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen assay source changed: '+name)
    for r in [c['payload'],c['CPU_tests'],*c['references'].values()]:
        if sha256(Path(r['path']))!=r['sha256']: raise ValueError('Frozen assay reference changed')
    for name,r in c['checkpoints'].items():
        st = Path(r['path']).stat(); saved = c['checkpoint_identity'][name]
        if (st.st_size,st.st_mtime_ns)!=(saved['bytes'],saved['mtime_ns']): raise ValueError('Native endpoint identity changed')
    binding = c['original_source_binding']; pool = Path(binding['pool'])
    ix,stream = (pool/'train.index.jsonl').stat(),(pool/'train.bin').stat()
    if ((ix.st_size,ix.st_mtime_ns,stream.st_size,stream.st_mtime_ns)!=
        (binding['index_size'],binding['index_mtime_ns'],binding['stream_size'],binding['stream_mtime_ns'])):
        raise ValueError('Previously verified TRAIN source identity changed; no full rescan')
    previous = read_json(ROOT/'reports/phase6/base-context-mixing-comparison-20261007/job.json')
    if alive(previous) or previous['status']!='complete': raise ValueError('Prior science still active')
    return c


def gradients(model, rows, path):
    ids,_ = right_pad([r['input_ids'] for r in rows],'cuda')
    targets = torch.full_like(ids,-100)
    for i,row in enumerate(rows): targets[i,:len(row['target_ids'])] = torch.tensor(row['target_ids'],device='cuda')
    valid = targets.ne(-100)
    named = list(model.named_parameters())
    backend = SDPBackend.FLASH_ATTENTION if path=='bf16_flash' else SDPBackend.MATH
    with sdpa_kernel(backend),torch.autocast('cuda',dtype=torch.bfloat16,enabled=path!='fp32_math'):
        hidden = right_padded_hidden(model,ids)
        logits = model.lm_head(hidden[valid]).float()
        loss = F.cross_entropy(logits,targets[valid])
    if not torch.isfinite(loss): raise ValueError('Nonfinite diagnostic original CE')
    # Backward follows the dtypes of forward; outside autocast per AMP guidance.
    result = torch.autograd.grad(loss,tuple(p for _,p in named))
    torch.cuda.synchronize()
    if any(not torch.isfinite(g).all() for g in result): raise ValueError('Nonfinite native gradient')
    return dict(loss=float(loss),teachers=int(valid.sum()),physical_inputs=ids.numel(),
                valid_inputs=sum(len(r['input_ids']) for r in rows)),{n:g.detach().cpu() for (n,_),g in zip(named,result)}


def run():
    c = inspect(); rows = read_json(Path(c['payload']['path']))['rows']
    if not torch.cuda.is_available(): raise RuntimeError('Actual CUDA required; no CPU fallback')
    RUN.mkdir(parents=True,exist_ok=True)
    job = dict(status='starting',**identity(),created_at=now(),config_sha256=sha256(CONFIG),
        optimizer_updates=0,scientific_teacher_tokens=0,
        restart_command='One-shot readonly diagnostic; inspect terminal/partial evidence, no blind rerun.')
    atomic_json(RUN/'job.json',job)
    endpoints = {}; started = None
    def check(*args):
        if args or started is not None and time.monotonic()-started>c['GPU_limit_seconds']:
            raise TimeoutError('Fixed120-second gradient assay cap exhausted')
    try:
        for name in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            target = RUN/'source'/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,target)
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
        with gpu_lock('cuda'):
            started=time.monotonic();signal.signal(signal.SIGALRM,check);signal.alarm(c['GPU_limit_seconds'])
            memory = configure_resident_memory(0)
            job.update(status='running',memory_policy=memory,heartbeat_at=now())
            atomic_json(RUN/'job.json',job)
            for endpoint,ref in c['checkpoints'].items():
                check()
                if sha256(Path(ref['path']))!=ref['sha256']: raise ValueError('Native checkpoint SHA differs')
                state = torch.load(ref['path'],map_location='cpu',weights_only=False)
                model = JMicroModel(state['model_config']).to('cuda').eval()
                model.load_state_dict(state['model'],strict=True)
                names = [n for n,_ in model.named_parameters()]
                if sum(p.numel() for p in model.parameters())!=c['native_parameters']: raise ValueError('Native10M required')
                saved_rng=host(rng_state()); all_batches=[]; source_stats={}
                for genre in ('web','textbook','story','stress1024'):
                    source_rows=[r for r in rows if r['source']==genre]
                    aggregate={p:None for p in c['paths']}; teachers=0
                    for start in range(0,len(source_rows),c['batch']):
                        batch=source_rows[start:start+c['batch']]; measurements={}; grads={}
                        for path in c['paths']:
                            check();measurements[path],grads[path]=gradients(model,batch,path)
                            count=measurements[path]['teachers']
                            if aggregate[path] is None: aggregate[path]={n:g.double()*count for n,g in grads[path].items()}
                            else:
                                for n,g in grads[path].items(): aggregate[path][n]+=g.double()*count
                        if len({m['teachers'] for m in measurements.values()})!=1: raise ValueError('Identical gold mask required')
                        teachers+=measurements['fp32_math']['teachers']
                        all_batches.append(dict(source=genre,row_ids=[r['id'] for r in batch],measurements=measurements,
                            comparisons={p:comparison(grads['fp32_math'],grads[p],names) for p in c['paths'][1:]}))
                        del grads
                        job.update(stage=endpoint+'-'+genre,completed_batches=sum(len(e['batches']) for e in endpoints.values())+len(all_batches),
                            heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started)
                        atomic_json(RUN/'job.json',job)
                        atomic_json(RUN/'partial-result.json',dict(endpoints=endpoints,current_endpoint=endpoint,batches=all_batches))
                    for mapping in aggregate.values():
                        for n in mapping: mapping[n]/=teachers
                    source_stats[genre]=dict(teachers=teachers,rows=len(source_rows),
                        comparisons={p:comparison(aggregate['fp32_math'],aggregate[p],names) for p in c['paths'][1:]})
                    del aggregate
                checks=dict(weights_unchanged=equal_state(state['model'],host(model.state_dict())),
                    native_tied=model.lm_head.weight is model.model.embed_tokens.weight,
                    RNG_unchanged=equal_state(saved_rng,host(rng_state())),no_accumulated_grads=all(p.grad is None for p in model.parameters()),
                    all_fixed_rows_measured=sorted(i for b in all_batches for i in b['row_ids'])==sorted(r['id'] for r in rows),
                    FP32_master_parameters=all(p.dtype==torch.float32 for p in model.parameters()))
                if not all(checks.values()): raise ValueError('Readonly assay state or completeness changed')
                endpoints[endpoint]=dict(checkpoint=ref,checks=checks,batches=all_batches,sources=source_stats)
                del model,state;gc.collect();torch.cuda.empty_cache()
            check(); severe=screen(endpoints);torch.cuda.synchronize();elapsed=time.monotonic()-started;signal.alarm(0)
            result=dict(status='fixed_all_parameter_training_precision_assay_complete',created_at=now(),config_sha256=sha256(CONFIG),
                actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},endpoints=endpoints,research_screen=severe,
                GPU_occupancy_seconds=elapsed,GPU_cap_seconds=c['GPU_limit_seconds'],memory_policy=memory,
                peak_VRAM_bytes=torch.cuda.max_memory_allocated(),torch_version=torch.__version__,
                BF16_reduced_precision_matmul_reduction=torch.backends.cuda.matmul.allow_bf16_reduced_precision_reduction,
                fixed_diagnostic_closed=True,optimizer_updates=0,scientific_teacher_tokens=0,new_unique_data_tokens=0,
                diagnostic_teacher_positions_all_paths=sum(b['measurements'][p]['teachers'] for e in endpoints.values() for b in e['batches'] for p in c['paths']),
                Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
                protected_test_used=False,quality_criteria_unchanged=True,old_numeric7_preserved=True,
                next_action='Only a positive fixed screen supports a separately defined precision training comparison. Otherwise close this sampled severe-precision hypothesis; no precision/sample/threshold/cap rescue.',
                limitations='Only24 fixed previously selected TRAIN families and one original long window, two mature endpoints. Local all-parameter CE gradients and simulated fresh first AdamW direction cannot prove accumulated optimizer behavior, quality, every corpus position or sole cause. BF16 backend comparison is descriptive; previous numeric failures are preserved.')
            atomic_json(RUN/'result.json',result);atomic_json(ROOT/'reports/phase6/base_gradient_precision_result.json',result)
            job.update(status='complete',ended_at=now(),GPU_occupancy_seconds=elapsed);atomic_json(RUN/'job.json',job)
            print(json.dumps(dict(status='complete',GPU_seconds=elapsed,research_screen=severe)))
    except BaseException as error:
        signal.alarm(0);job.update(status='failed',ended_at=now(),error=repr(error),GPU_occupancy_seconds=0 if started is None else time.monotonic()-started)
        atomic_json(RUN/'job.json',job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();group=parser.add_mutually_exclusive_group()
    group.add_argument('--prepare',action='store_true');group.add_argument('--inspect',action='store_true')
    args=parser.parse_args()
    if args.prepare: prepare()
    elif args.inspect: inspect();print('Frozen original TRAIN precision assay preflight passed; GPU0')
    else: run()
