"""One fixed TRAIN-only, zero-update native gradient-path diagnostic."""
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
from base_embedding_gradient_diagnostic import decompose,gradient_statistics,interference_screen

CONFIG=ROOT/'configs/phase6/base_embedding_gradient_diagnostic.json'
RUN=ROOT/'reports/phase6/base-embedding-gradient-diagnostic-20261007'
PAYLOAD=ROOT/'reports/phase6/base_embedding_gradient_payload.json'
SOURCES=('scripts/base_embedding_gradient_diagnostic.py','scripts/diagnose_base_embedding_gradients.py',
    'scripts/diagnose_base_embedding_gradients.ps1','tests/test_base_embedding_gradient_diagnostic.py',
    'scripts/natural_context_contrast_corpus.py','scripts/natural_context_contrast_trainer.py',
    'scripts/natural_context_contrast_memory.py','scripts/phase6_performance.py',
    'src/jmicro/model.py','src/jmicro/training.py','src/jmicro/tokenizer.py','src/jmicro/phase5.py','uv.lock')


def ref(path):return dict(path=str(path),sha256=sha256(path))


def prepare():
    if CONFIG.exists() or PAYLOAD.exists() or (RUN/'job.json').exists():
        raise ValueError('Preserve fixed one-shot diagnostic; no reroll or blind retry')
    started=time.monotonic()
    old=read_json(ROOT/'configs/phase6/base_residual_dropout_comparison.json')
    closed=ROOT/'reports/phase6/base_residual_dropout_comparison_completion.json'
    completion=read_json(closed)
    job=read_json(ROOT/'reports/phase6/base-residual-dropout-comparison-20261007/job.json')
    if not completion['fixed_recipe_closed'] or job['status']!='complete' or alive(job):
        raise ValueError('Actual prior scientific job must have ended')
    tests=ROOT/'reports/phase6/base_embedding_gradient_tests.xml'
    suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)<3 or any(int(s.attrib[k]) for s in suites for k in ('errors','failures','skipped')):
        raise ValueError('Successful actual CPU attribution checks required')
    codec=Tokenizer(ROOT/old['tokenizer'])
    if sha256(codec.path)!=old['tokenizer_sha256']:raise ValueError('Pinned original codec required')
    sampler=OriginalTrainCorpusSampler(old['source_binding']['pool'],old['source_binding']['manifest_sha256'],
        codec,dict.fromkeys(GENRES,10000000),seed=2026100741)
    if sampler.binding!=old['source_binding']:raise ValueError('Reuse previously verified TRAIN identity without rescanning')
    rows=[];documents=[]
    try:
        for genre in GENRES:
            families=set();bodies=set()
            for attempt in range(64):
                if time.monotonic()-started>30:raise TimeoutError('CPU preparation30s exceeded')
                sampler._draw_document(genre)
                windows=sampler.pending[genre];sampler.pending[genre]=[]
                first=windows[0]
                if first['source_family'] in families or first['full_original_body_sha256'] in bodies:continue
                families.add(first['source_family']);bodies.add(first['full_original_body_sha256'])
                doc_id=genre+'-'+str(len(families)).zfill(2)
                documents.append(dict(id=doc_id,source=genre,source_family=first['source_family'],
                    body_sha256=first['full_original_body_sha256'],index_byte_position=first['index_byte_position'],
                    index_record_sha256=first['index_record_sha256'],full_body_tokens=first['original_body_tokens'],
                    original_windows=len(windows)))
                indices=[0] if len(windows)==1 else [0,len(windows)-1]
                for index in indices:
                    r=windows[index]
                    rows.append(dict(id=doc_id+'-window'+str(index),document=doc_id,source=genre,
                        input_ids=r['input_ids'],target_ids=r['target_ids'],
                        original_window_index=index,target_first=r['target_first'],target_end=r['target_end'],
                        input_start=r['input_start'],body_sha256=r['full_original_body_sha256']))
                if len(families)==8:break
            if len(families)!=8:raise ValueError('Fixed64 draws lack8 distinct TRAIN documents; no reroll')
    finally:sampler.handle.close()
    if len(documents)!=24 or not 24<=len(rows)<=48:raise ValueError('All24 complete diagnostic document selections required')
    ce=read_json(Path(old['control_CE']['path']))
    checkpoints=dict(parent=old['parent'],CE100M=dict(path=ce['checkpoint'],sha256=ce['checkpoint_sha256']))
    cp_identity={k:dict(size=Path(v['path']).stat().st_size,mtime_ns=Path(v['path']).stat().st_mtime_ns)
        for k,v in checkpoints.items()}
    atomic_json(PAYLOAD,dict(created_at=now(),documents=documents,rows=rows,
        TRAIN_only=True,source_binding=sampler.binding,seed=2026100741,
        sampling='Index-byte weighted; first8 distinct families/bodies per source, original first and last windows only. No new extraction/EOS or quality selection. Not a population-uniform sample.'))
    atomic_json(CONFIG,dict(created_at=now(),payload=ref(PAYLOAD),checkpoints=checkpoints,
        checkpoint_identity=cp_identity,previous_completion=ref(closed),CPU_tests=ref(tests),
        sources={p:sha256(ROOT/p) for p in SOURCES},source_binding=sampler.binding,
        documents_per_source=8,batch=4,maximum_rows=48,GPU_limit_seconds=180,
        native_parameters=10001152,precision='FP32 math; TF32 disabled',
        attribution='Native full tied gradient equals input-path plus ephemeral output-leaf gradient, same original teacher mask. No optimizer, new model parameters or weight mutation.',
        hypothesis='Substantial antagonism between tied input/output gradient paths might motivate one new train-only gradient experiment. It has not been measured locally; it is not an asserted cause of poor generation.',
        research_screen=dict(cosine_at_most=-.1,cancellation_at_most=.9,minimum_sources=2,
            require_both_checkpoints=True,Base_quality_gate=False),
        completion='All fixed rows and three source gradient aggregates at both checkpoint endpoints; identical logits/loss, gradient decomposition, unchanged native weights/tied identity/RNG/no accumulated grads. Zero learning/DEV/TEST use. Close this one-shot whether screen passes or fails.',
        failure_policy='If the same severe conflict screen is not passed at both endpoints, do not start input/output projection or untied-architecture training from this hypothesis. Do not reroll sample, soften thresholds or rescue closed recipes.',
        references=[dict(url='https://aclanthology.org/E17-2025/',meaning='Weight tying/update analysis; paper recommends tying and does not establish that untying helps this10M model.'),
            dict(url='https://arxiv.org/abs/2001.06782',meaning='Conflicting gradient projection for multiple task losses; input/output paths of one CE loss are not separate task losses, so applicability is unproven.')],
        preparation_CPU_wall_seconds=time.monotonic()-started,new_GPU_seconds=0,optimizer_updates=0,
        new_scientific_CE_teachers=0,Base_complete=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,quality_criteria_unchanged=True))
    print(json.dumps(dict(status='TRAIN_only_attribution_frozen',documents=24,rows=len(rows),config_sha256=sha256(CONFIG))))


def inspect():
    c=read_json(CONFIG)
    for name in ('payload','previous_completion','CPU_tests'):
        if sha256(Path(c[name]['path']))!=c[name]['sha256']:raise ValueError('Frozen reference changed: '+name)
    for name,digest in c['sources'].items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen source changed: '+name)
    for name,reference in c['checkpoints'].items():
        st=Path(reference['path']).stat();saved=c['checkpoint_identity'][name]
        if (st.st_size,st.st_mtime_ns)!=(saved['size'],saved['mtime_ns']):raise ValueError('Frozen checkpoint identity changed')
    old_job=read_json(ROOT/'reports/phase6/base-residual-dropout-comparison-20261007/job.json')
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
                    input_sum=output_sum=None;teachers=0
                    for start in range(0,len(rows),c['batch']):
                        check();batch=rows[start:start+c['batch']]
                        ids,_=right_pad([r['input_ids'] for r in batch],'cuda')
                        targets=torch.full_like(ids,-100)
                        for index,row in enumerate(batch):targets[index,:len(row['target_ids'])]=torch.tensor(row['target_ids'],device='cuda')
                        with sdpa_kernel(SDPBackend.MATH):stats,a,b=decompose(model,ids,targets)
                        torch.cuda.synchronize();count=stats['teachers'];teachers+=count
                        # Per-batch CE gradients are means. Aggregate by exact target counts.
                        if input_sum is None:input_sum=a.double()*count;output_sum=b.double()*count
                        else:input_sum+=a.double()*count;output_sum+=b.double()*count
                        measured.append(dict(source=genre,row_ids=[r['id'] for r in batch],**stats))
                        job.update(stage=name+'-'+genre,completed_batches=sum(len(e['batches']) for e in endpoints.values())+len(measured),
                            heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started)
                        atomic_json(RUN/'job.json',job)
                        atomic_json(RUN/'partial-result.json',dict(endpoints=endpoints,current_endpoint=name,current_batches=measured))
                        del ids,targets,a,b
                    sources[genre]=gradient_statistics(input_sum/teachers,output_sum/teachers)
                    sources[genre].update(teachers=teachers,rows=len(rows),documents=8)
                    del input_sum,output_sum
                checks=dict(weights_unchanged=equal_state(state['model'],host(model.state_dict())),
                    native_tied=model.lm_head.weight is model.model.embed_tokens.weight,
                    RNG_unchanged=equal_state(saved_rng,host(rng_state())),no_accumulated_grads=all(p.grad is None for p in model.parameters()),
                    all_fixed_rows_measured=[v for batch in measured for v in batch['row_ids']]==[r['id'] for r in payload['rows']])
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
                next_action=('Define one matched train-only gradient-path comparison before any learning; no automatic untying or adoption.' if screen else
                    'Close this sampled tied-path interference hypothesis; no gradient projection/untying training or threshold/sample rescue. Select a genuinely different Base mechanism from existing evidence.'),
                limitations='Only8 distinct TRAIN families per source, index-byte biased first/last windows, two reused endpoints. Gradient-path statistics are local teacher-forcing diagnostics, not causal proof, independent generation generalization or new Base-quality evidence. Both forwards use FP32 math, not the scientific BF16 flash path.')
            atomic_json(RUN/'result.json',result)
            atomic_json(ROOT/'reports/phase6/base_embedding_gradient_result.json',result)
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
