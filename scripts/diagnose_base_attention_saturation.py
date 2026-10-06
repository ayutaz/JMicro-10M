"""One native TRAIN-only attention-concentration assay; no parameter updates."""
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
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,now,sha256
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.training import atomic_json,gpu_lock,rng_state,seed_all
from natural_context_contrast_trainer import right_pad,right_padded_hidden,host
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive
from base_attention_saturation_diagnostic import observe_attention,aggregate,broad_screen

CONFIG=ROOT/'configs/phase6/base_attention_saturation_diagnostic.json'
RUN=ROOT/'reports/phase6/base-attention-saturation-diagnostic-20261007'
SOURCES=('scripts/base_attention_saturation_diagnostic.py','scripts/diagnose_base_attention_saturation.py',
    'scripts/diagnose_base_attention_saturation.ps1','tests/test_base_attention_saturation_diagnostic.py',
    'scripts/natural_context_contrast_trainer.py','scripts/natural_context_contrast_memory.py',
    'scripts/phase6_performance.py','src/jmicro/model.py','src/jmicro/training.py','uv.lock')


def read(path):return json.loads(Path(path).read_text())
def ref(path):return dict(path=str(path),sha256=sha256(path))


def prepare():
    started=time.monotonic()
    if CONFIG.exists() or (RUN/'job.json').exists():raise ValueError('Preserve one fixed attention assay')
    old=read(ROOT/'configs/phase6/base_kv_head_gradient_diagnostic.json')
    closed_path=ROOT/'reports/phase6/base_kv_allocation_bucketed_completion.json'
    closed=read(closed_path)
    if closed['science_budget_eligible'] or alive(closed['actual_identity']):
        raise ValueError('Preserve actual closed allocation budget; no duplicate jobs')
    tests=ROOT/'reports/phase6/base_attention_saturation_tests.xml'
    suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if not suites or sum(int(s.attrib['tests']) for s in suites)!=4 or any(int(s.attrib[k]) for s in suites for k in ('errors','failures','skipped')):
        raise ValueError('Actual four native observation CPU checks required')
    payload=read(old['payload']['path'])
    if sha256(Path(old['payload']['path']))!=old['payload']['sha256'] or len(payload['documents'])!=24 or not payload['TRAIN_only']:
        raise ValueError('Same previously fixed24 TRAIN-only selections required')
    examined=0;matches=[]
    excluded={Path(s).name for s in SOURCES[:4]}
    for folder,pattern in ((ROOT/'scripts','*.py'),(ROOT/'configs/phase6','*.json')):
        for candidate in folder.glob(pattern):
            if candidate.name in excluded:continue
            examined+=1
            text=candidate.read_text()
            if 'pmax>=.98 AND entropy/log(causal_keys)' in text:matches.append(candidate.relative_to(ROOT).as_posix())
    if matches:raise ValueError('Potential duplicate registered concentration assay: '+repr(matches))
    c=dict(created_at=now(),payload=old['payload'],checkpoints=old['checkpoints'],checkpoint_identity=old['checkpoint_identity'],
        previous_completion=ref(closed_path),CPU_tests=ref(tests),sources={s:sha256(ROOT/s) for s in SOURCES},
        source_binding=old['source_binding'],documents_per_source=8,batch=4,GPU_limit_seconds=90,
        native_parameters=10001152,precision='FP32 math, TF32 disabled',fresh_calibration_seed=42,
        research_screen=dict(minimum_causal_keys=16,maximum_probability_at_least=.98,
            normalized_entropy_at_most=.05,saturated_head_query_fraction_at_least=.25,
            minimum_fraction_all_layers=.5,minimum_sources=2,require_both_learned_endpoints=True,
            random_weights_are_calibration_only=True,Base_quality_gate=False),
        observation='Temporary attention pre-hooks recompute native normalized Q/K and RoPE, causal softmax statistics, then return None. Original forward/math/logits/loss/parameters are unchanged; no intervention or saved new parameters.',
        attention_sink_control='Report every head/layer and classify saturated argmax as original BOS, recent non-BOS or other. Count BOS concentration in the screen but explicitly report it as potentially functional, never prove collapse from low entropy alone.',
        novelty_scope=dict(top_level_scripts_and_phase6_configs=examined,matches=matches),
        prior_QKNorm='Phase5 already learned4K/8K RMS-head shared normalization and100M no-QKNorm ablation; preserve those results. This is a new read-only mature attention assay, not proof that QKNorm is an untested architecture.',
        completion='Same24 fixed TRAIN units, all13 layers/all4 query heads/source at both learned endpoints plus fresh random calibration. Exact observer/native logits/loss and unchanged weights/tied/RNG/no grads/hooks removed. Report all sources/layers and fixed screen; no DEV/TEST or updates.',
        failure_policy='If either learned endpoint fails the fixed broad screen, close this saturation hypothesis; no layer/head/source/sample/threshold rescue, QK restoration, logit-softcap or sigma reparam learning on its basis. Positive screen only permits defining one measured causal intervention, not launch/adoption.',
        limitations='Small index-byte-biased first/last TRAIN windows, FP32 teacher forcing. No temporal training-entropy trajectory, free-generation context dependence or causal quality claim. Saturated specialized heads and attention sinks can be functional.',
        references=[dict(url='https://proceedings.mlr.press/v202/zhai23a.html',
            meaning='Primary entropy-collapse training study at other settings; motivates observation, not evidence of this models collapse or remedy.'),
            dict(url='https://aclanthology.org/2020.findings-emnlp.379/',
            meaning='Low-resource translation paper uses L2-normalized Q/K plus learned scale; differs from existing native RMS-head normalization and does not prove Base improvement.')],
        preparation_CPU_seconds=time.monotonic()-started,new_scientific_teacher_tokens=0,optimizer_updates=0,
        Base_complete=False,Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True)
    if c['preparation_CPU_seconds']>30:raise TimeoutError('Fixed CPU30s preparation exceeded')
    atomic_json(CONFIG,c)
    print(json.dumps(dict(status='readonly_native_attention_assay_frozen',CPU_seconds=c['preparation_CPU_seconds'],GPU0=True)))


def inspect():
    c=read(CONFIG)
    for key in ('payload','previous_completion','CPU_tests'):
        if sha256(Path(c[key]['path']))!=c[key]['sha256']:raise ValueError('Frozen reference differs: '+key)
    for path,digest in c['sources'].items():
        if sha256(ROOT/path)!=digest:raise ValueError('Frozen source differs: '+path)
    for name,row in c['checkpoints'].items():
        stat=Path(row['path']).stat();saved=c['checkpoint_identity'][name]
        if (stat.st_size,stat.st_mtime_ns)!=(saved['size'],saved['mtime_ns']):raise ValueError('Previously SHA-verified checkpoint identity differs')
    if alive(read(c['previous_completion']['path'])['actual_identity']):raise ValueError('Previous native job still alive')
    if (RUN/'job.json').exists():raise ValueError('Inspect attempted one-shot identity and partial/terminal evidence')
    return c


def run():
    c=inspect();payload=read(c['payload']['path'])
    if not torch.cuda.is_available():raise RuntimeError('Actual native WSL CUDA required')
    RUN.mkdir(parents=True,exist_ok=True)
    job=dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),optimizer_updates=0,
        scientific_teacher_tokens=0,Base_complete=False,Chat_started=False,quantization_started=False,
        restart_command='One-shot readonly assay: inspect partial/terminal identity; no blind rerun.')
    atomic_json(RUN/'job.json',job)
    endpoints={};started=None
    def check(*args):
        if args or started is not None and time.monotonic()-started>c['GPU_limit_seconds']:
            raise TimeoutError('Fixed native attention GPU90s exhausted')
    try:
        for name in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            dest=RUN/'source'/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,dest)
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
        with gpu_lock('cuda'):
            started=time.monotonic();signal.signal(signal.SIGALRM,check);signal.alarm(c['GPU_limit_seconds'])
            job.update(status='running',memory_policy=configure_resident_memory(0));atomic_json(RUN/'job.json',job)
            reference_config=None
            for name in (*c['checkpoints'],'fresh_calibration'):
                check()
                if name!='fresh_calibration':
                    reference=c['checkpoints'][name]
                    if sha256(Path(reference['path']))!=reference['sha256']:raise ValueError('Actual learned checkpoint SHA differs')
                    state=torch.load(reference['path'],map_location='cpu',weights_only=False)
                    reference_config=state['model_config']
                    model=JMicroModel(reference_config).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
                else:
                    reference=dict(kind='fresh_random_native_calibration_not_learning',seed=c['fresh_calibration_seed'])
                    seed_all(c['fresh_calibration_seed']);model=JMicroModel(reference_config).to('cuda').eval()
                    state=dict(model=host(model.state_dict()))
                if sum(p.numel() for p in model.parameters())!=c['native_parameters']:raise ValueError('Actual unchanged native10M required')
                saved_rng=host(rng_state());records=[];sources={};measured=[]
                for genre in ('web','textbook','story'):
                    rows=[r for r in payload['rows'] if r['source']==genre];genre_records=[]
                    for start in range(0,len(rows),c['batch']):
                        check();batch=rows[start:start+c['batch']]
                        ids,_=right_pad([r['input_ids'] for r in batch],'cuda')
                        targets=torch.full(ids.shape,-100,dtype=torch.long)
                        for i,row in enumerate(batch):targets[i,:len(row['target_ids'])]=torch.tensor(row['target_ids'])
                        targets=targets.to('cuda');mask=targets.ne(-100)
                        with torch.no_grad(),sdpa_kernel(SDPBackend.MATH):
                            expected=model.lm_head(right_padded_hidden(model,ids)[mask]).float()
                            expected_loss=F.cross_entropy(expected,targets[mask])
                            with observe_attention(model,targets) as captured:
                                actual=model.lm_head(right_padded_hidden(model,ids)[mask]).float()
                            actual_loss=F.cross_entropy(actual,targets[mask])
                        if (not torch.equal(expected,actual) or not torch.equal(expected_loss,actual_loss)
                                or len(captured)!=13 or [r['layer'] for r in captured]!=list(range(13))):
                            raise ValueError('Native attention observer must preserve exact logits/loss and all layers')
                        genre_records.extend(captured);records.extend(captured)
                        measured.append(dict(source=genre,row_ids=[r['id'] for r in batch],teacher_positions=int(mask.sum()),
                            teacher_loss=float(expected_loss),native_logit_max_error=0.,native_loss_difference=0.,layers=captured))
                        job.update(stage=name+'-'+genre,heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started)
                        atomic_json(RUN/'job.json',job)
                        atomic_json(RUN/'partial-result.json',dict(endpoints=endpoints,current_endpoint=name,current_batches=measured))
                        del ids,targets,mask,expected,actual,expected_loss,actual_loss
                    sources[genre]=aggregate(genre_records,13)
                checks=dict(weights_unchanged=equal_state(state['model'],host(model.state_dict())),
                    RNG_unchanged=equal_state(saved_rng,host(rng_state())),
                    native_tied=model.lm_head.weight is model.model.embed_tokens.weight,
                    no_accumulated_grads=all(p.grad is None for p in model.parameters()),
                    hooks_removed=all(not b.self_attn._forward_pre_hooks for b in model.model.layers),
                    all_fixed_rows_measured=[i for b in measured for i in b['row_ids']]==[r['id'] for r in payload['rows']])
                if not all(checks.values()):raise ValueError('Readonly native attention invariants failed: '+repr(checks))
                endpoints[name]=dict(checkpoint=reference,sources=sources,batches=measured,native_checks=checks,screen=broad_screen(sources))
                atomic_json(RUN/'partial-result.json',dict(endpoints=endpoints))
                del model,state;gc.collect();torch.cuda.empty_cache()
            check();elapsed=time.monotonic()-started
            passed=all(endpoints[n]['screen']['passed'] for n in c['checkpoints'])
            result=dict(status='complete',created_at=now(),actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
                config_sha256=sha256(CONFIG),payload=c['payload'],endpoints=endpoints,
                broad_saturation_at_both_learned_endpoints=passed,fixed_diagnostic_closed=True,
                GPU_occupancy_seconds=elapsed,peak_allocated_bytes=torch.cuda.max_memory_allocated(),
                diagnostic_teacher_positions=sum(b['teacher_positions'] for e in endpoints.values() for b in e['batches']),
                scientific_teacher_tokens=0,optimizer_updates=0,new_model_quality_evaluations=0,
                new_parameters_saved=0,DEV_used=False,protected_test_used=False,Base_complete=False,Base_adopted=False,
                Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,
                next_action='Define one bounded causal attention-normalization intervention only if positive at both learned endpoints; otherwise close broad saturation and do not launch QK restoration/softcap/sigma learning from this assay.',
                limitations=c['limitations'])
            atomic_json(RUN/'result.json',result);atomic_json(ROOT/'reports/phase6/base_attention_saturation_result.json',result)
            job.update(status='complete',ended_at=now(),GPU_occupancy_seconds=elapsed);atomic_json(RUN/'job.json',job)
            print(json.dumps(dict(status='readonly_attention_assay_complete',GPU_seconds=elapsed,broad_saturation=passed)))
    except BaseException as exc:
        signal.alarm(0);job.update(status='failed',ended_at=now(),error=repr(exc),GPU_occupancy_seconds=0 if started is None else time.monotonic()-started)
        atomic_json(RUN/'job.json',job);raise
    finally:signal.alarm(0)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group();g.add_argument('--prepare',action='store_true');g.add_argument('--inspect',action='store_true')
    args=p.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Frozen native TRAIN-only attention assay inspected; GPU0')
    else:run()
