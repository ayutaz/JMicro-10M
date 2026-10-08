"""Read-only EOS preference for identical bodies with trailing-LF counterfactuals."""
import argparse
import hashlib
from pathlib import Path
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json,gpu_lock,rng_state
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from base_parallel_residual_model import model_from_config
from base_parallel_residual_trainer import KIND
from run_base_residual_seen_train import ref,checked,wait_ui
from phase6_performance import identity,alive

PHASE=ROOT/'reports/phase6'
PROPOSAL=PHASE/'base_residual_boundary_counterfactual_proposal.json'
CONFIG=ROOT/'configs/phase6/base_residual_boundary_counterfactual.json'
OUTPUT=PHASE/'base_residual_boundary_counterfactual.json'
RUN=PHASE/'base-residual-boundary-counterfactual-20261008'


def variants(row,codec):
    text=row['full_original_body_text']; original=row['input_ids'][1:]
    if (codec.decode_bytes(original)!=text.encode('utf-8') or codec.encode(text)!=original
            or hashlib.sha256(text.encode()).hexdigest()!=row['full_original_body_sha256']):
        raise ValueError('Bound original body/token/bytes differ')
    base=text.rstrip('\n')
    if not base: raise ValueError('Nonempty original body required')
    results=[]
    for name,value in (('original',text),('no_trailing_LF',base),('one_LF',base+'\n')):
        ids=original if name=='original' else codec.encode(value)
        if not ids or any(n<8 for n in ids) or len(ids)+1>=1024:
            raise ValueError('Counterfactual plain body must fit context<1024')
        if codec.decode_bytes(ids)!=value.encode(): raise ValueError('Counterfactual exact byte roundtrip differs')
        results.append(dict(variant=name,input_ids=[2]+ids,body_bytes_hex=value.encode().hex(),
            original_bytes_unchanged=name=='original',queried_EOS_is_observed_original_target=name=='original'))
    return results


@torch.inference_mode()
def next_event(model,codec,case,LF_ids,device='cuda'):
    ids=torch.tensor([case['input_ids']],device=device)
    with torch.autocast(torch.device(device).type,dtype=torch.bfloat16,enabled=str(device).startswith('cuda')):
        logits=model(ids).logits[0,-1].float()
    if not bool(torch.isfinite(logits).all()): raise ValueError('Finite actual next-token logits required')
    probabilities=logits.softmax(-1)
    values,indices=probabilities.topk(8)
    return dict(**case,EOS_probability=float(probabilities[3]),EOS_rank=int((logits>logits[3]).sum())+1,
        LF_token_ids=LF_ids,LF_next_token_probability=None if len(LF_ids)!=1 else float(probabilities[LF_ids[0]]),
        top8=[dict(id=int(i),probability=float(p),decoded_bytes_hex=codec.decode_bytes([int(i)]).hex())
              for i,p in zip(indices,values,strict=True)],
        generated_tokens=0,forced_EOS_tokens=0)


def freeze():
    if CONFIG.exists() or OUTPUT.exists() or RUN.exists(): raise ValueError('Preserve frozen counterfactual/results')
    started=time.monotonic()
    old=read_json(ROOT/'configs/phase6/base_residual_train_dev_history.json')
    prepared=checked(old['preparation']);p=read_json(PROPOSAL)
    if (p['GPU_budget_seconds']!=30 or p['optimizer_updates'] or p['scientific_teacher_tokens']
            or p['parent_checkpoint_sha256']!=old['parent']['sha256']):
        raise ValueError('Bounded prospective read-only same2B counterfactual required')
    codec=Tokenizer(ROOT/old['tokenizer'])
    selected=[dict(id=r['id'],population=r['population'],variants=variants(r,codec)) for r in prepared['selected']]
    if len(selected)!=32: raise ValueError('Exactly all32 previous selected units required')
    tests=PHASE/'base_residual_boundary_counterfactual_tests.xml'
    import xml.etree.ElementTree as ET
    cases=ET.parse(tests).findall('.//testcase')
    if len(cases)!=4 or any(r.find(t) is not None for r in cases for t in ('error','failure','skipped')):
        raise ValueError('Four passed LF byte/context/query fixtures required')
    extra=('scripts/run_base_residual_boundary_counterfactual.py','scripts/run_base_residual_boundary_counterfactual.ps1',
           'tests/test_base_residual_boundary_counterfactual.py')
    elapsed=time.monotonic()-started
    if elapsed>30: raise TimeoutError('CPU preparation30-second cap exhausted')
    atomic_json(CONFIG,dict(created_at=now(),proposal=ref(PROPOSAL),preparation=old['preparation'],parent=old['parent'],
        previous_completion=ref(PHASE/'base_residual_train_dev_history_completion.json'),
        observation=ref(PHASE/'base_residual_boundary_format_observation.json'),CPU_tests=ref(tests),CPU_seconds=elapsed,
        source_sha256={**old['source_sha256'],**{n:sha256(ROOT/n) for n in extra}},tokenizer=old['tokenizer'],
        LF_token_ids=codec.encode('\n'),selected=selected,GPU_budget_seconds=30,
        median_EOS_probability_difference_threshold=.25,minimum_positive_differences=24,
        dtype='bf16',backend='math',optimizer_updates=0,scientific_teacher_tokens=0,
        Base_complete=False,Chat_started=False,quantization_started=False))
    print('Frozen all32x3 original/LF-only body variants; next-token query only,30seconds/no learning')


def inspect():
    c=read_json(CONFIG)
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen code differs: '+name)
    checked(c['proposal']);checked(c['preparation']);checked(c['previous_completion']);checked(c['observation'])
    if (c['GPU_budget_seconds']!=30 or c['median_EOS_probability_difference_threshold']!=.25
            or c['minimum_positive_differences']!=24 or len(c['selected'])!=32):
        raise ValueError('Fixed all32 prospective screen/budget required')
    previous=read_json(PHASE/'base-residual-train-dev-history-20261008/job.json')
    if alive(previous) or previous['status']!='complete': raise ValueError('Prior diagnostic must be exited')
    if OUTPUT.exists() or RUN.exists(): raise ValueError('Inspect existing result/process; no duplicate or reroll')
    lock=Path.home()/'jmicro-data/gpu.lock'
    if lock.exists():
        holder=read_json(lock);ui=read_json(ROOT/'reports/local/webui/server.json')
        if Path(f"/proc/{holder['pid']}").exists() and (holder['pid']!=ui['pid'] or not alive(ui)):
            raise ValueError('Another live GPU process holds lock')
    return c


def run():
    torch.set_num_threads(2);c=inspect()
    if not torch.cuda.is_available() or not torch.cuda.is_bf16_supported(): raise RuntimeError('Actual CUDA/BF16 required')
    RUN.mkdir(parents=True)
    job=dict(status='starting',**identity(),started_at=now(),config=ref(CONFIG),GPU_seconds=0,
             cumulative_GPU_ledger_closed=False,optimizer_updates=0,scientific_teacher_tokens=0)
    atomic_json(RUN/'job.json',job);started=None
    try:
        with gpu_lock('cuda'):
            started=time.monotonic()
            def check():
                if time.monotonic()-started>=30: raise TimeoutError('Frozen30-second cumulative GPU cap exhausted')
            parent_path=Path(c['parent']['path'])
            if sha256(parent_path)!=c['parent']['sha256']: raise ValueError('Actual same2B parent differs')
            parent=torch.load(parent_path,map_location='cpu',weights_only=False)
            if parent['kind']!=KIND or parent['spec']['arm']!='sequential' or parent['counters']['supervised_tokens']!=2000000000:
                raise ValueError('Typed actual sequential2B required')
            model=model_from_config(parent['model_config']).to('cuda').eval()
            model.load_state_dict(parent['model'],strict=True)
            if type(model).__name__!='JMicroModel' or sum(p.numel() for p in model.parameters())!=10001152:
                raise ValueError('Same actual10M model required')
            before=rng_state();codec=Tokenizer(ROOT/c['tokenizer']);results=[]
            with sdpa_kernel(SDPBackend.MATH):
                for row in c['selected']:
                    output=dict(id=row['id'],population=row['population'],variants=[])
                    for case in row['variants']:
                        check();output['variants'].append(next_event(model,codec,case,c['LF_token_ids']))
                    atomic_json(RUN/(row['id']+'.json'),output);results.append(output)
                    job.update(status='running',completed_units=len(results),GPU_seconds=time.monotonic()-started,heartbeat_at=now())
                    atomic_json(RUN/'job.json',job)
            torch.cuda.synchronize()
            checks=dict(weights_unchanged=all(torch.equal(v.detach().cpu(),parent['model'][k]) for k,v in model.state_dict().items()),
                RNG_unchanged=equal_state(before,rng_state()),eval_mode_unchanged=not model.training,
                all96_next_token_only=all(v['generated_tokens']==v['forced_EOS_tokens']==0 for r in results for v in r['variants']))
            if not all(checks.values()): raise ValueError('Read-only weights/RNG/mode/query check failed')
            check();elapsed=time.monotonic()-started
            atomic_json(OUTPUT,dict(status='all96_GPU_complete_CPU_summary_pending',created_at=now(),identity=identity(),
                config=ref(CONFIG),parent=c['parent'],preparation=c['preparation'],checks=checks,results=results,
                GPU_seconds=elapsed,GPU_cap_seconds=30,cumulative_GPU_ledger_closed=True,
                scientific_teacher_tokens=0,optimizer_updates=0,Base_complete=False,Base_adopted=False,
                Chat_started=False,quantization_started=False,protected_test_scored=False))
            job.update(status='complete',ended_at=now(),GPU_seconds=elapsed,cumulative_GPU_ledger_closed=True)
            atomic_json(RUN/'job.json',job)
            print('All96 original/LF counterfactual next-token queries completed within30-second ledger')
    except BaseException as error:
        if started is not None: torch.cuda.synchronize()
        job.update(status='failed',ended_at=now(),GPU_seconds=0 if started is None else time.monotonic()-started,
                   cumulative_GPU_ledger_closed=True,error=repr(error))
        atomic_json(RUN/'job.json',job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__);group=parser.add_mutually_exclusive_group()
    group.add_argument('--freeze',action='store_true');group.add_argument('--inspect',action='store_true');group.add_argument('--wait-ui',action='store_true')
    args=parser.parse_args()
    if args.freeze: freeze()
    elif args.inspect: inspect();print('All32 LF-only next-token diagnostic preflight passed')
    elif args.wait_ui: wait_ui()
    else: run()
