"""One-shot paired mixture CUDA/full-resume/capacity and all32 timing evidence."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time
import xml.etree.ElementTree as ET
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, rng_state
from base_output_mixture_model import ARMS, POLICY, TAG
from base_output_mixture_trainer import OutputMixtureTrainer, finite_tree, OPT_POLICY
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host, right_padded_hidden
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity

CONFIG = ROOT/'configs/phase6/base_output_mixture_probe.json'
RUN = ROOT/'reports/phase6/base-output-mixture-probe-20261007'
PREPARATION = ROOT/'reports/phase6/base_output_mixture_preparation.json'
SOURCES = ('scripts/probe_base_output_mixture.py', 'scripts/probe_base_output_mixture.ps1',
    'scripts/base_output_mixture_model.py', 'scripts/base_output_mixture_trainer.py',
    'scripts/base_output_mixture_evaluation.py', 'scripts/prepare_base_output_mixture.py',
    'tests/test_base_output_mixture.py', 'scripts/natural_context_contrast_corpus.py',
    'scripts/natural_context_contrast_trainer.py', 'scripts/natural_context_contrast_memory.py',
    'scripts/phase6_performance.py', 'src/jmicro/model.py', 'src/jmicro/training.py',
    'src/jmicro/tokenizer.py', 'uv.lock')

def ref(path):return dict(path=str(path),sha256=sha256(path))


def forecast(seconds,gold):
    if (type(seconds) not in (int,float) or not math.isfinite(seconds) or seconds<=0
            or type(gold) is not int or gold<=0):
        raise ValueError('Positive finite SUM all32 seconds and original gold required')
    return math.ceil(100000000*seconds/gold*1.3+900)


def paired_budget(arms,elapsed):
    if (set(arms)!=set(ARMS) or type(elapsed) not in (int,float)
            or not math.isfinite(elapsed) or not 0<elapsed<=180):
        raise ValueError('Both exact arms and bounded actual probe required')
    budgets = {arm:forecast(arms[arm]['all32_step_seconds'],arms[arm]['all32_original_gold']) for arm in ARMS}
    return budgets,sum(budgets.values())+elapsed<=9000


def passed_tests(path,expected):
    suites = list(ET.parse(path).getroot().iter('testsuite'))
    if (sum(int(s.attrib['tests']) for s in suites)!=expected
            or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped'))):
        raise ValueError('Actual complete CPU checks required')


def inspect():
    c = read_json(CONFIG)
    if (RUN/'job.json').exists():raise ValueError('One-shot probe already recorded; do not repeat')
    if (c['arms']!=list(ARMS) or c['mixture_policy']!=POLICY or c['batch']!=48 or c['seed']!=42
            or c['resource']!=dict(probe_GPU_cap_seconds=180,total_GPU_cap_seconds=9000,warmup_updates=3,timed_updates=32)):
        raise ValueError('Fixed paired mixture recipe differs')
    for name in ('preparation','proposal','CPU_tests','payload','control_CE'):
        r = c[name]
        if sha256(Path(r['path']))!=r['sha256']:raise ValueError('Frozen reference changed: '+name)
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen probe source changed: '+name)
    st = Path(c['parent']['path']).stat()
    if (st.st_size,st.st_mtime_ns)!=(c['parent_size'],c['parent_mtime_ns']):
        raise ValueError('Accepted parent stat differs')
    window = read_json(Path(c['payload']['path']))['window']
    if len(window['input_ids'])!=1024 or sum(i!=-100 for i in window['target_ids'])!=512:
        raise ValueError('Original1024/512 maximum shape required')
    for folder in Path('/proc').iterdir():
        if not folder.name.isdecimal() or int(folder.name)==os.getpid():continue
        try:
            command = (folder/'cmdline').read_bytes().split(b'\0')
            if 'python' in Path(command[0].decode()).name and any(
                    arg.startswith((b'scripts/run_',b'scripts/probe_')) for arg in command[1:]):
                raise ValueError('Another actual project experiment exists: '+folder.name)
        except (FileNotFoundError,ProcessLookupError,PermissionError):continue
    return c


def comparable_history(left,right):
    return len(left)==len(right) and all(equal_state(
        {k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
        {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})
        for a,b in zip(left,right,strict=True))


def source_checks(left,right):
    keys = ('update','token_digest','supervised_tokens','source_teachers','source_EOS',
            'CE_input_tokens','original_body_bytes','auxiliary_input_tokens','auxiliary_pairs','physical_input_tokens')
    return {key:equal_state(left['counters'][key],right['counters'][key]) for key in keys} | {
        'full_sampler':equal_state(left['sampler'],right['sampler'])}


def run():
    c = inspect();RUN.mkdir(parents=True,exist_ok=True)
    job = dict(status='running',**identity(),started_at=now(),config_sha256=sha256(CONFIG),
        scientific_teacher_positions=0,Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(RUN/'job.json',job)
    started,histories = None,{}
    def clear():gc.collect();torch.cuda.empty_cache()
    def beat(stage):
        job.update(stage=stage,heartbeat_at=now())
        if started is not None:job['GPU_occupancy_seconds']=time.monotonic()-started
        atomic_json(RUN/'job.json',job)
    def timeout(*_):raise TimeoutError('Fixed paired CUDA180s exhausted; no rescue')
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        parent = torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
        codec = Tokenizer(ROOT/c['tokenizer'])
        if sha256(codec.path)!=c['tokenizer_sha256']:raise ValueError('Pinned tokenizer changed')
        binding = dict(parent=c['parent'],config_sha256=sha256(CONFIG),weights_role='verification_only')
        def build(arm):
            b = c['source_binding']
            sampler = OriginalTrainCorpusSampler(b['pool'],b['manifest_sha256'],codec,c['goals'],c['seed'])
            if sampler.binding!=b:raise ValueError('Accepted source binding changed')
            return OutputMixtureTrainer(parent,sampler,binding,arm,batch=c['batch'],seed=c['seed'])
        for name in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            destination = RUN/'source'/name;destination.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(ROOT/name,destination)
        with gpu_lock('cuda'):
            started = time.monotonic();signal.signal(signal.SIGALRM,timeout);signal.alarm(180)
            memory = configure_resident_memory(0)
            a = build(ARMS[0]);rng = host(rng_state());b = build(ARMS[1])
            initial = dict(paired_initial_weights=equal_state(a.model.state_dict(),b.model.state_dict()),
                global_RNG_equal=equal_state(rng,host(rng_state())),
                tied_vocab_both=all(t.model.lm_head.weight is t.model.model.embed_tokens.weight for t in (a,b)),
                equal_actual10034434=all(sum(p.numel() for p in t.model.parameters())==10034434 for t in (a,b)),
                actual_parameters_once_both=all([id(p) for p in t.model.parameters()]==
                    [id(p) for group in t.optimizer.param_groups for p in group['params']] for t in (a,b)),
                fresh_AdamW_both=all(not t.optimizer.state and t.scheduler.last_epoch==0 for t in (a,b)),
                full_initial_sampler_equal=equal_state(a.sampler.state_dict(),b.sampler.state_dict()),
                conversion_mixture_zero_both=all(not torch.count_nonzero(v) for t in (a,b)
                    for k,v in t.model.state_dict().items() if k.startswith('lm_head.up.')),
                conversion_original_nonmixture_weights=all(torch.equal(v.to('cuda'),t.model.state_dict()[k])
                    for t in (a,b) for k,v in parent['model'].items()))
            if not all(initial.values()):raise ValueError('Actual initial paired mixture/parent/RNG invariant failed')
            del a,b;clear()
            arms,continuous,first_losses = {},{},{}
            for arm in ARMS:
                states,logs = [],[]
                for route in ('continuous','resumed'):
                    beat(arm+'-'+route);t = build(arm);history = [];histories[arm+'-'+route]=history
                    for index in range(4):
                        history.append(t.step())
                        if route=='resumed' and index==1:
                            t.save(RUN/(arm+'-split.pt'));del t;clear();t=build(arm);t.load(RUN/(arm+'-split.pt'))
                    t.save(RUN/(arm+'-'+route+'.pt'))
                    states.append(host(t.state_dict()));logs.append(history);del t;clear()
                checks = {key:equal_state(states[0][key],states[1][key]) for key in states[0]}
                checks['finite_fullstate']=all(finite_tree(s) for s in states)
                checks['all_history_except_timing']=comparable_history(*logs)
                checks['both_expert_up_weights_learned']=all(
                    bool(torch.count_nonzero(v))
                    for s in states for k,v in s['model'].items() if k.startswith('lm_head.up.'))
                if not all(checks.values()):raise ValueError('Own actual CUDA mixture resume failed: '+arm)
                continuous[arm]=dict(counters=states[0]['counters'],sampler=states[0]['sampler'])
                first_losses[arm]=logs[0][0]['CE_loss']
                arms[arm]=dict(resume_checks=checks)
                del states,logs;clear()
                beat(arm+'-maximum-shape-and-all32');t=build(arm)
                histories[arm+'-timing']=[t.step() for _ in range(3)]
                window = read_json(Path(c['payload']['path']))['window']
                ids=torch.tensor([window['input_ids']]*48,device='cuda')
                targets=torch.tensor([window['target_ids']]*48,device='cuda')
                frozen=host(t.model.state_dict());optimizer=host(t.optimizer.state_dict())
                t.optimizer.zero_grad(set_to_none=True);torch.cuda.reset_peak_memory_stats()
                with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                    selected=targets.ne(-100)
                    loss=F.cross_entropy(t.model.lm_head(right_padded_hidden(t.model,ids)[selected]).float(),targets[selected])
                    loss.backward()
                gradient=torch.nn.utils.clip_grad_norm_(t.model.parameters(),1.,error_if_nonfinite=True)
                torch.cuda.synchronize()
                capacity=dict(batch=48,context=1024,teacher_stride=512,backward_original_positions=int(selected.sum()),
                    peak_VRAM_bytes=torch.cuda.max_memory_allocated(),loss=float(loss.detach()),gradient_norm=float(gradient),
                    optimizer_updates=0,weights_unchanged=equal_state(frozen,host(t.model.state_dict())),
                    optimizer_unchanged=equal_state(optimizer,host(t.optimizer.state_dict())))
                if (not math.isfinite(capacity['loss']) or not 0<capacity['gradient_norm']<float('inf')
                        or not capacity['weights_unchanged'] or not capacity['optimizer_unchanged']
                        or capacity['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']):
                    raise ValueError('Resident finite original48x1024 required: '+arm)
                del ids,targets,loss,frozen,optimizer,selected;clear()
                measured=[]
                for _ in range(32):
                    row=t.step();measured.append(row);histories[arm+'-timing'].append(row)
                t.validate_committed(t.state_dict())
                arms[arm].update(capacity=capacity,all32_step_seconds=sum(r['seconds'] for r in measured),
                    all32_original_gold=sum(r['CE_targets_this_update'] for r in measured),
                    all32_data_wait_seconds=sum(r['data_wait_seconds'] for r in measured))
                del t;clear()
            common=source_checks(continuous[ARMS[0]],continuous[ARMS[1]])
            common['initial_actual_CE_within2e_6']=abs(first_losses[ARMS[0]]-first_losses[ARMS[1]])<=2e-6
            common['all32_full_original_draws_equal']=all(equal_state(left[k],right[k])
                for left,right in zip(histories[ARMS[0]+'-timing'],histories[ARMS[1]+'-timing'],strict=True)
                for k in (*continuous[ARMS[0]]['counters'],'draw_trace','lr'))
            if not all(common.values()):raise ValueError('Paired original source/masks/EOS/first CE differs')
            elapsed=time.monotonic()-started;budgets,eligible=paired_budget(arms,elapsed)
            result=dict(status='complete',passed=True,actual_identity=identity(),config_sha256=sha256(CONFIG),
                initial_checks=initial,arms=arms,common_source_checks=common,memory_policy=memory,
                GPU_occupancy_seconds=elapsed,probe_GPU_cap_seconds=180,science_budget_seconds=budgets,
                science_budget_eligible=eligible,total_GPU_cap_seconds=9000,histories=histories,
                verification_updates=sum(len(h) for h in histories.values()),
                verification_original_teacher_positions=sum(r['CE_targets_this_update'] for h in histories.values() for r in h),
                stress_backward_positions=sum(a['capacity']['backward_original_positions'] for a in arms.values()),
                scientific_teacher_positions=0,probe_weights_used_for_science=False,
                Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
                limitation='Fixed sequential arm order, warm local source cache; not an architecture speed comparison. Forecast retains all32 wall time including sampler wait.',
                next_action='Freeze original quality policy and paired100M science only if total<=9000. Otherwise close fixed recipe without changing budget or teacher amount.')
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',ended_at=now(),GPU_occupancy_seconds=elapsed)
            atomic_json(RUN/'job.json',job);signal.alarm(0)
            print(json.dumps(dict(status='complete',GPU_occupancy_seconds=elapsed,science_budget_seconds=budgets,science_budget_eligible=eligible)))
    except BaseException as error:
        signal.alarm(0);job.update(status='failed',error=repr(error),ended_at=now(),
            GPU_occupancy_seconds=time.monotonic()-started if started else 0)
        atomic_json(RUN/'job.json',job);atomic_json(RUN/'partial_histories.json',histories);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=('inspect','run'));args=parser.parse_args()
    {'inspect':inspect,'run':run}[args.mode]()
