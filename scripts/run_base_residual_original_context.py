"""Read-only original-article context recovery for sixteen consumed paragraphs."""
import argparse
import copy
import hashlib
from pathlib import Path
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json,gpu_lock,rng_state
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer,SUPPRESS_IDS
from base_parallel_residual_model import model_from_config
from base_parallel_residual_trainer import KIND
from run_base_residual_seen_train import ref,checked,history,wait_ui
from phase6_performance import identity,alive

PHASE=ROOT/'reports/phase6'
PROPOSAL=PHASE/'base_residual_original_context_diagnostic_proposal.json'
PREPARATION=PHASE/'base_residual_original_context_preparation.json'
CONFIG=ROOT/'configs/phase6/base_residual_original_context.json'
OUTPUT=PHASE/'base_residual_original_context.json'
RUN=PHASE/'base-residual-original-context-20261008'


def recover(row,metadata,article_ids,codec):
    if not article_ids or any(n<8 for n in article_ids): raise ValueError('Original plain article body required')
    raw=codec.decode_bytes(article_ids);article=raw.decode('utf-8')
    start,end=metadata['source_char_start'],metadata['source_char_end']
    if (type(start) is not int or type(end) is not int or not 0<=start<end<=len(article)
            or article[start:end]!=row['full_original_body_text']
            or hashlib.sha256(article[start:end].encode()).hexdigest()!=row['full_original_body_sha256']
            or codec.decode_bytes(row['input_ids'][1:])!=article[start:end].encode()):
        raise ValueError('Original source character slice/selected paragraph bytes differ')
    cut=len(row['prompt_ids'])-1
    if (row['input_ids'][0]!=2 or row['prompt_ids']!=row['input_ids'][:cut+1]
            or row['gold_targets']!=row['input_ids'][1:]+[3]
            or row['continuation_gold_ids']!=row['gold_targets'][cut:]):
        raise ValueError('Unchanged original paragraph prefix/gold shift required')
    preceding_text=article[:start];before=codec.encode(preceding_text)
    if (codec.decode_bytes(before)!=preceding_text.encode()
            or codec.encode(preceding_text+row['prefix'])!=before+row['prompt_ids'][1:]):
        raise ValueError('Actual original context/selected prefix token boundary differs')
    full=[2]+before+row['prompt_ids'][1:]
    clipped=max(0,len(full)-959)
    prompt=full[clipped:]
    if prompt[-cut:]!=row['prompt_ids'][1:] or len(prompt)+64>=1024:
        raise ValueError('Unchanged current paragraph prefix and strict context bound required')
    prompt_raw=codec.decode_bytes(prompt)
    try: prompt_text=prompt_raw.decode('utf-8');valid=True
    except UnicodeDecodeError: prompt_text=prompt_raw.decode('utf-8',errors='replace');valid=False
    body_gold=row['continuation_gold_ids'][:-1]
    if not body_gold or any(n<8 for n in body_gold): raise ValueError('Original body-only continuation required; no artificial EOS')
    return dict(id=row['id'],source='web',has_additional_context=bool(before),prefix=row['prefix'],
        prompt_ids=prompt,continuation_gold_ids=body_gold,paragraph_body_ids=row['input_ids'][1:],
        standalone_prompt_ids=row['prompt_ids'],original_source_metadata=metadata,
        original_article_body_tokens=len(article_ids),original_article_bytes_sha256=hashlib.sha256(raw).hexdigest(),
        actual_preceding_text=preceding_text,actual_preceding_bytes_hex=preceding_text.encode().hex(),
        actual_preceding_token_ids=before,oldest_history_tokens_removed=clipped,
        artificial_fragment_BOS_inserted=False,prompt_UTF8_valid=valid,
        full_supplied_context_text=prompt_text,full_supplied_context_bytes_hex=prompt_raw.hex(),
        original_unit_EOS_excluded_from_body_comparison=True)


def prepare():
    started=time.monotonic()
    if PREPARATION.exists() or RUN.exists(): raise ValueError('Preserve original context preparation and outputs')
    old=read_json(ROOT/'configs/phase6/base_residual_train_dev_history.json')
    previous=checked(old['preparation']);baseline=read_json(PHASE/'base_residual_train_dev_history.json')
    provenance=read_json(PHASE/'base_residual_consumed_unit_provenance.json')
    if provenance['preparation_sha256']!=old['preparation']['sha256']:
        raise ValueError('Same already-consumed unit provenance required')
    metadata={r['index_byte_position']:r for r in provenance['units']}
    source=read_json(ROOT/'configs/phase6/architecture_comparison.json')
    view=TrainView(source['web_shards'],source['web_manifest_sha256'])
    codec=Tokenizer(ROOT/old['tokenizer']);selected=[]
    for row in previous['selected'][:16]:
        if time.monotonic()-started>=30: raise TimeoutError('CPU source recovery30seconds exhausted')
        item=metadata[row['index_byte_position']]
        if (item['source_manifest_sha256']!=source['web_manifest_sha256']
                or item['index_record_sha256']!=row['index_record_sha256']
                or item['canonical_sha256']!=row['full_original_body_sha256']):
            raise ValueError('Actual selected consumed unit source identity differs')
        a,b=item['source_start'],item['source_end']
        if not 0<=a<b<len(view.tokens) or int(view.tokens[a])!=2 or int(view.tokens[b])!=3:
            raise ValueError('Original full article source BOS/body/EOS bounds differ')
        selected.append(recover(row,item,view.tokens[a+1:b].astype(int).tolist(),codec))
    if [r['id'] for r in selected]!=[r['id'] for r in baseline['results'][:16]]:
        raise ValueError('All16 fixed previous TRAIN units required')
    elapsed=time.monotonic()-started
    if elapsed>30: raise TimeoutError('CPU source recovery30seconds exhausted')
    atomic_json(PREPARATION,dict(created_at=now(),proposal=ref(PROPOSAL),CPU_seconds=elapsed,
        previous_preparation=old['preparation'],baseline=ref(PHASE/'base_residual_train_dev_history.json'),
        provenance=ref(PHASE/'base_residual_consumed_unit_provenance.json'),parent=old['parent'],
        original_source_manifest=ref(view.directory/'manifest.json'),
        original_source_stream_identity=dict(size=(view.directory/'train.bin').stat().st_size,
            mtime_ns=(view.directory/'train.bin').stat().st_mtime_ns),selected=selected,
        units_with_additional_context=sum(r['has_additional_context'] for r in selected),
        original_unit_EOS_targets_used=0,GPU_seconds=0,scientific_teacher_tokens=0,optimizer_updates=0,
        Base_complete=False,Chat_started=False,quantization_started=False))
    print('Recovered all16 original article slices; additional-context units: '+str(sum(r['has_additional_context'] for r in selected)))


def freeze():
    if CONFIG.exists() or OUTPUT.exists() or RUN.exists(): raise ValueError('Preserve prospective context config/results')
    prepared=read_json(PREPARATION);p=checked(prepared['proposal'])
    old=read_json(ROOT/'configs/phase6/base_residual_train_dev_history.json')
    if p['GPU_budget_seconds']!=60 or prepared['parent']!=old['parent'] or prepared['original_unit_EOS_targets_used']:
        raise ValueError('Prospective same2B body-only context diagnostic required')
    tests=PHASE/'base_residual_original_context_tests.xml'
    import xml.etree.ElementTree as ET
    cases=ET.parse(tests).findall('.//testcase')
    if len(cases)!=4 or any(r.find(t) is not None for r in cases for t in ('failure','error','skipped')):
        raise ValueError('Four passed original context/boundary fixtures required')
    extra=('scripts/run_base_residual_original_context.py','scripts/run_base_residual_original_context.ps1',
           'tests/test_base_residual_original_context.py','src/jmicro/eos_pilot.py')
    atomic_json(CONFIG,dict(created_at=now(),proposal=ref(PROPOSAL),preparation=ref(PREPARATION),
        parent=prepared['parent'],baseline=prepared['baseline'],CPU_tests=ref(tests),
        previous_completion=ref(PHASE/'base_residual_boundary_counterfactual_completion.json'),
        source_sha256={**old['source_sha256'],**{n:sha256(ROOT/n) for n in extra}},tokenizer=old['tokenizer'],
        GPU_budget_seconds=60,max_new_tokens=64,max_prompt_tokens=959,dtype='bf16',backend='math',
        suppressed_ids=sorted(SUPPRESS_IDS),minimum_context_units=8,mean_BODY_NLL_improvement_threshold=.20,
        optimizer_updates=0,scientific_teacher_tokens=0,Base_complete=False,Chat_started=False,quantization_started=False))
    print('Frozen same16 original-article context/body-target diagnostic;60seconds/no learning')


def inspect():
    c=read_json(CONFIG)
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen context code differs: '+name)
    checked(c['proposal']);prepared=checked(c['preparation']);baseline=checked(c['baseline']);checked(c['previous_completion'])
    if (c['GPU_budget_seconds']!=60 or c['max_new_tokens']!=64 or c['suppressed_ids']!=sorted(SUPPRESS_IDS)
            or c['minimum_context_units']!=8 or c['mean_BODY_NLL_improvement_threshold']!=.20):
        raise ValueError('Fixed original-context protocol required')
    previous=read_json(PHASE/'base-residual-boundary-counterfactual-20261008/job.json')
    if alive(previous) or previous['status']!='complete': raise ValueError('Prior GPU process must have ended')
    if OUTPUT.exists() or RUN.exists(): raise ValueError('Inspect existing context process/result; no duplicate or reroll')
    lock=Path.home()/'jmicro-data/gpu.lock'
    if lock.exists():
        holder=read_json(lock);ui=read_json(ROOT/'reports/local/webui/server.json')
        if Path(f"/proc/{holder['pid']}").exists() and (holder['pid']!=ui['pid'] or not alive(ui)):
            raise ValueError('Another actual GPU process holds lock')
    return c,prepared,{r['id']:r for r in baseline['results'][:16]}


def reused_teacher(old,unit,codec):
    teacher=copy.deepcopy(old['teacher']);n=min(64,len(unit['continuation_gold_ids']))
    for key in ('steps','fed_ids','predicted_ids'): teacher[key]=teacher[key][:n]
    raw=codec.decode_bytes(teacher['fed_ids'])
    teacher.update(text=raw.decode('utf-8',errors='replace'),raw_UTF8_bytes_hex=raw.hex(),
        stop_reason='original_body_fragment_end_no_unit_EOS',reused_existing_predictions=True)
    return teacher


def run():
    torch.set_num_threads(2);c,prepared,baseline=inspect()
    if not torch.cuda.is_available() or not torch.cuda.is_bf16_supported(): raise RuntimeError('Actual CUDA/BF16 required')
    RUN.mkdir(parents=True)
    job=dict(status='starting',**identity(),started_at=now(),config=ref(CONFIG),GPU_seconds=0,
             cumulative_GPU_ledger_closed=False,scientific_teacher_tokens=0,optimizer_updates=0)
    atomic_json(RUN/'job.json',job);started=None
    try:
        with gpu_lock('cuda'):
            started=time.monotonic()
            def check():
                if time.monotonic()-started>=60: raise TimeoutError('Frozen60-second cumulative GPU cap exhausted')
            path=Path(c['parent']['path'])
            if sha256(path)!=c['parent']['sha256']: raise ValueError('Same actual2B checkpoint differs')
            parent=torch.load(path,map_location='cpu',weights_only=False)
            if parent['kind']!=KIND or parent['spec']['arm']!='sequential' or parent['counters']['supervised_tokens']!=2000000000:
                raise ValueError('Typed actual original sequential2B required')
            model=model_from_config(parent['model_config']).to('cuda').eval();model.load_state_dict(parent['model'],strict=True)
            if type(model).__name__!='JMicroModel' or sum(p.numel() for p in model.parameters())!=10001152:
                raise ValueError('Same actual10M required')
            before=rng_state();codec=Tokenizer(ROOT/c['tokenizer']);results=[]
            with sdpa_kernel(SDPBackend.MATH):
                for unit in prepared['selected']:
                    check()
                    if unit['has_additional_context']:
                        teacher=history(model,codec,unit,True,'cuda',check);free=history(model,codec,unit,False,'cuda',check)
                        if teacher['steps'][0]!=free['steps'][0]: raise ValueError('Same recovered-context first prediction differs')
                    else:
                        teacher=reused_teacher(baseline[unit['id']],unit,codec);free=baseline[unit['id']]['free']
                    row=dict(id=unit['id'],has_additional_context=unit['has_additional_context'],teacher_body=teacher,free=free,
                             baseline_reused_for_no_context_control=not unit['has_additional_context'])
                    atomic_json(RUN/(unit['id']+'.json'),row);results.append(row)
                    job.update(status='running',completed_units=len(results),GPU_seconds=time.monotonic()-started,heartbeat_at=now())
                    atomic_json(RUN/'job.json',job)
            torch.cuda.synchronize()
            checks=dict(weights_unchanged=all(torch.equal(v.detach().cpu(),parent['model'][k]) for k,v in model.state_dict().items()),
                RNG_unchanged=equal_state(before,rng_state()),eval_mode_unchanged=not model.training,
                no_unit_EOS_in_teacher_BODY=all(not s['actual_gold_EOS'] for r in results for s in r['teacher_body']['steps']))
            if not all(checks.values()): raise ValueError('Read-only/body-only checks failed')
            check();elapsed=time.monotonic()-started
            atomic_json(OUTPUT,dict(status='all16_context_GPU_complete_content_summary_pending',created_at=now(),identity=identity(),
                config=ref(CONFIG),preparation=c['preparation'],parent=c['parent'],baseline=c['baseline'],checks=checks,
                results=results,GPU_seconds=elapsed,GPU_cap_seconds=60,cumulative_GPU_ledger_closed=True,
                scientific_teacher_tokens=0,optimizer_updates=0,Base_complete=False,Base_adopted=False,
                Chat_started=False,quantization_started=False,protected_test_scored=False))
            job.update(status='complete',ended_at=now(),GPU_seconds=elapsed,cumulative_GPU_ledger_closed=True);atomic_json(RUN/'job.json',job)
            print('All16 fixed context cases complete; unchanged weights, original BODY targets only')
    except BaseException as error:
        if started is not None: torch.cuda.synchronize()
        job.update(status='failed',ended_at=now(),GPU_seconds=0 if started is None else time.monotonic()-started,
                   cumulative_GPU_ledger_closed=True,error=repr(error));atomic_json(RUN/'job.json',job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__);group=parser.add_mutually_exclusive_group()
    group.add_argument('--prepare',action='store_true');group.add_argument('--freeze',action='store_true')
    group.add_argument('--inspect',action='store_true');group.add_argument('--wait-ui',action='store_true')
    args=parser.parse_args()
    if args.prepare: prepare()
    elif args.freeze: freeze()
    elif args.inspect: inspect();print('Same16 original source-context preflight passed')
    elif args.wait_ui: wait_ui()
    else: run()
