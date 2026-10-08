"""Bounded same-checkpoint consumed Web TRAIN / length-matched DEV histories."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import numpy as np
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json,gpu_lock,rng_state
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer,SUPPRESS_IDS
from base_parallel_residual_model import model_from_config
from base_parallel_residual_trainer import KIND
from base_kv_allocation_trainer import CEOnlyOriginalSampler
from run_base_residual_seen_train import history,ref,checked,wait_ui
from phase6_performance import alive,identity

PHASE=ROOT/'reports/phase6'
PROPOSAL=PHASE/'base_residual_train_dev_history_proposal.json'
PREPARATION=PHASE/'base_residual_train_dev_history_preparation.json'
CONFIG=ROOT/'configs/phase6/base_residual_train_dev_history.json'
OUTPUT=PHASE/'base_residual_train_dev_history.json'
RUN=PHASE/'base-residual-train-dev-history-20261008'


def verify_update(rows,record,digest):
    payload=json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
    digest=hashlib.sha256(bytes.fromhex(digest)+payload).hexdigest()
    trace=[list((r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],r['teacher_tokens'])) for r in rows]
    if (digest!=record['token_digest'] or trace!=record['draw_trace']
            or sum(r['teacher_tokens'] for r in rows)!=record['CE_targets_this_update']
            or len(rows)!=record['original_windows_this_update']):
        raise ValueError('Actual consumed original TRAIN history differs')
    return digest


def match_dev(train,candidates):
    used=set(); pairs=[]
    train_hashes={r['full_original_body_sha256'] for r in train}
    if len(train_hashes)!=len(train): raise ValueError('Distinct original TRAIN units required')
    for row in train:
        eligible=[r for r in candidates if r['index'] not in used
                  and r['canonical_sha256'] not in train_hashes
                  and r['canonical_sha256'] not in {p['canonical_sha256'] for p in pairs}]
        if not eligible: raise ValueError('Insufficient distinct nonoverlapping DEV candidates; no redraw')
        selected=min(eligible,key=lambda r:(abs(r['body_tokens']-row['original_body_tokens']),r['index']))
        used.add(selected['index']); pairs.append(selected)
    return pairs


def unit(body,codec,metadata):
    if not 64<=len(body)<=512 or any(n<8 for n in body):
        raise ValueError('Original plain body length outside frozen range')
    raw=codec.decode_bytes(body); text=raw.decode('utf-8')
    if hashlib.sha256(raw).hexdigest()!=metadata['full_original_body_sha256']:
        raise ValueError('Selected original canonical bytes differ')
    cut=None
    for n in range(24,49):
        try: prefix=codec.decode_bytes(body[:n]).decode('utf-8')
        except UnicodeDecodeError: continue
        if codec.encode(prefix)==body[:n]: cut=n; break
    if cut is None: raise ValueError('Selected unit lacks stable prefix; no reroll')
    return dict(**metadata,original_body_tokens=len(body),full_original_body_text=text,
        full_original_body_bytes_hex=raw.hex(),input_ids=[2]+body,gold_targets=body+[3],
        prefix=prefix,prefix_body_tokens=cut,prompt_ids=[2]+body[:cut],continuation_gold_ids=body[cut:]+[3])


def prepare():
    started=time.monotonic()
    if PREPARATION.exists() or RUN.exists(): raise ValueError('Preserve prospective selection and outputs')
    proposal=read_json(PROPOSAL)
    old=read_json(ROOT/'configs/phase6/base_parallel_residual_comparison.json')
    codec=Tokenizer(ROOT/old['tokenizer'])
    excluded={r['full_original_body_sha256'] for r in read_json(PHASE/'base_residual_seen_train_preparation.json')['selected']}
    sampler=CEOnlyOriginalSampler(old['source_binding']['pool'],old['source_binding']['manifest_sha256'],codec,old['goals'])
    if sampler.binding!=old['source_binding']: raise ValueError('Accepted TRAIN identity differs')
    trained=PHASE/'base-parallel-residual-comparison-20261007/sequential/train-result.json'
    record=read_json(trained)
    histories=list(trained.parent.glob('metrics-*.jsonl'))
    if len(histories)!=1: raise ValueError('Ambiguous consumed history; inspect without selecting a convenient log')
    selected=[]; seen=set(excluded); digest='0'*64; bindings=[]
    try:
        with histories[0].open() as stream:
            for update in range(1,9):
                if time.monotonic()-started>=30: raise TimeoutError('CPU preparation30seconds exhausted')
                actual=json.loads(stream.readline())
                rows=sampler.take(80)
                if actual['update']!=update: raise ValueError('Actual initial completed-update history required')
                digest=verify_update(rows,actual,digest)
                bindings.append(dict(update=update,token_digest=digest,teachers=actual['CE_targets_this_update']))
                for row in rows:
                    body_hash=row['full_original_body_sha256']
                    if (len(selected)==16 or row['source']!='web' or not row['original_document_first_window']
                            or row['input_start'] or not 64<=row['original_body_tokens']<=512 or body_hash in seen
                            or row['target_ids'][-1]!=3 or any(n==-100 for n in row['target_ids'])):
                        continue
                    body=row['input_ids'][1:]
                    if row['target_ids']!=body+[3] or len(body)!=row['original_body_tokens']:
                        raise ValueError('Original whole-unit shift/EOS differs')
                    selected.append(unit(body,codec,dict(id=f'TRAIN-{len(selected):02d}',population='TRAIN',
                        source='web',full_original_body_sha256=body_hash,source_family=row['source_family'],
                        index_byte_position=row['index_byte_position'],index_record_sha256=row['index_record_sha256'],
                        actually_consumed_at_update=update)))
                    seen.add(body_hash)
    finally: sampler.handle.close()
    if len(selected)!=16: raise ValueError('Fixed eight updates lack16 eligible TRAIN units; no extra draws')
    dev_root=Path(old['dev_shards']); manifest=read_json(dev_root/'manifest.json')
    if sha256(dev_root/'manifest.json')!=old['dev_manifest_sha256']:
        raise ValueError('Existing independent DEV manifest differs')
    # Existing checked DEV pool, verify its small index once and selected bytes;
    # do not rescan/re-hash the full corpus or huge TRAIN stream.
    index=dev_root/'dev.index.json'
    if sha256(index)!=manifest['splits']['dev']['index_sha256']:
        raise ValueError('Existing DEV index differs')
    entries=read_json(index)[:4096]
    candidates=[dict(**r,index=i) for i,r in enumerate(entries)
                if r['split']=='dev' and r['kind']=='web' and 64<=r['body_tokens']<=512]
    matches=match_dev(selected,candidates)
    tokens=np.memmap(dev_root/'dev.bin',dtype='<u2',mode='r')
    if tokens.size!=manifest['splits']['dev']['tokens']: raise ValueError('DEV stream size differs')
    dev=[]
    for i,r in enumerate(matches):
        ids=tokens[r['offset']:r['offset']+r['body_tokens']+2].astype(int).tolist()
        if not ids or ids[0]!=2 or ids[-1]!=3: raise ValueError('Original DEV BOS/body/EOS differs')
        dev.append(unit(ids[1:-1],codec,dict(id=f'DEV-{i:02d}',population='DEV',source='web',
            full_original_body_sha256=r['canonical_sha256'],doc_id=r['doc_id'],dev_index=r['index'],
            split='dev',matched_TRAIN_id=selected[i]['id'])))
    elapsed=time.monotonic()-started
    if elapsed>30: raise TimeoutError('CPU preparation30seconds exhausted')
    atomic_json(PREPARATION,dict(created_at=now(),proposal=ref(PROPOSAL),CPU_seconds=elapsed,
        training_record=ref(trained),source_binding=old['source_binding'],dev_manifest=ref(dev_root/'manifest.json'),
        dev_index=ref(index),dev_stream_identity=dict(size=(dev_root/'dev.bin').stat().st_size,
            mtime_ns=(dev_root/'dev.bin').stat().st_mtime_ns),completed_history_prefix=bindings,
        existing_six_body_hashes_excluded=sorted(excluded),all640_consumed_windows_exact=True,
        selected=selected+dev,parent=dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']),
        GPU_seconds=0,scientific_teacher_tokens=0,optimizer_updates=0,Base_complete=False,
        limits=proposal['limits']))
    print('Prepared16 actual-consumed Web TRAIN/16 length-matched separate DEV; all640 consumed windows exact')


def freeze():
    if CONFIG.exists() or OUTPUT.exists() or RUN.exists(): raise ValueError('Preserve frozen diagnostic')
    prepared=read_json(PREPARATION)
    old=read_json(ROOT/'configs/phase6/base_residual_seen_train_diagnostic.json')
    p=checked(prepared['proposal'])
    if (p['GPU_budget_seconds']!=120 or prepared['parent']!=old['checkpoint']
            or not prepared['all640_consumed_windows_exact'] or len(prepared['selected'])!=32):
        raise ValueError('Prospective protocol and actual same2B consumed Web/DEV required')
    tests=PHASE/'base_residual_train_dev_history_tests.xml'
    import xml.etree.ElementTree as ET
    cases=ET.parse(tests).findall('.//testcase')
    if len(cases)!=3 or any(r.find(t) is not None for r in cases for t in ('error','failure','skipped')):
        raise ValueError('Three passed protocol fixtures required')
    extra=('scripts/run_base_residual_train_dev_history.py','scripts/run_base_residual_train_dev_history.ps1',
           'tests/test_base_residual_train_dev_history.py','scripts/phase6_performance.py')
    atomic_json(CONFIG,dict(created_at=now(),proposal=ref(PROPOSAL),preparation=ref(PREPARATION),
        parent=prepared['parent'],capacity_completion=ref(PHASE/'base_residual_capacity_control_completion.json'),
        CPU_tests=ref(tests),source_sha256={**old['source_sha256'],**{n:sha256(ROOT/n) for n in extra}},
        GPU_budget_seconds=120,max_new_tokens=64,dtype='bf16',backend='math',suppressed_ids=sorted(SUPPRESS_IDS),
        tokenizer=read_json(ROOT/'configs/phase6/base_parallel_residual_comparison.json')['tokenizer'],
        optimizer_updates=0,scientific_teacher_tokens=0,Base_complete=False,Chat_started=False,quantization_started=False))
    print('Frozen32 teacher/free histories before new GPU output;120seconds/no learning')


def inspect():
    c=read_json(CONFIG)
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen diagnostic code differs: '+name)
    checked(c['proposal']); prepared=checked(c['preparation']); completed=checked(c['capacity_completion'])
    if (not completed['capacity_control_passed'] or c['GPU_budget_seconds']!=120
            or c['suppressed_ids']!=sorted(SUPPRESS_IDS) or c['max_new_tokens']!=64):
        raise ValueError('Actual completed positive control and fixed protocol required')
    prior=read_json(PHASE/'base-residual-capacity-control-r2-20261008/job.json')
    if alive(prior) or prior['status']!='complete': raise ValueError('Capacity process must have ended')
    if RUN.exists() or OUTPUT.exists(): raise ValueError('Inspect existing diagnostic; no duplicate or reroll')
    lock=Path.home()/'jmicro-data/gpu.lock'
    if lock.exists():
        holder=read_json(lock);ui=read_json(ROOT/'reports/local/webui/server.json')
        if Path(f"/proc/{holder['pid']}").exists() and (holder['pid']!=ui['pid'] or not alive(ui)):
            raise ValueError('Another live GPU process holds lock')
    return c,prepared


def run():
    torch.set_num_threads(2)
    c,prepared=inspect()
    if not torch.cuda.is_available() or not torch.cuda.is_bf16_supported(): raise RuntimeError('Actual CUDA/BF16 required')
    RUN.mkdir(parents=True)
    job=dict(status='starting',**identity(),started_at=now(),config=ref(CONFIG),GPU_seconds=0,
             cumulative_GPU_ledger_closed=False,optimizer_updates=0,scientific_teacher_tokens=0)
    atomic_json(RUN/'job.json',job); started=None
    try:
        with gpu_lock('cuda'):
            started=time.monotonic()
            def check():
                if time.monotonic()-started>=120: raise TimeoutError('Frozen120-second cumulative GPU cap exhausted')
            path=Path(c['parent']['path'])
            if sha256(path)!=c['parent']['sha256']: raise ValueError('Same actual sequential2B parent differs')
            parent=torch.load(path,map_location='cpu',weights_only=False)
            if parent['kind']!=KIND or parent['spec']['arm']!='sequential' or parent['counters']['supervised_tokens']!=2000000000:
                raise ValueError('Typed actual original2B state required')
            model=model_from_config(parent['model_config']).to('cuda').eval()
            model.load_state_dict(parent['model'],strict=True)
            if type(model).__name__!='JMicroModel' or sum(p.numel() for p in model.parameters())!=10001152:
                raise ValueError('Same actual10M model required')
            before=rng_state(); codec=Tokenizer(ROOT/c['tokenizer']); results=[]
            with sdpa_kernel(SDPBackend.MATH):
                for row in prepared['selected']:
                    check()
                    teacher=history(model,codec,row,True,'cuda',check)
                    free=history(model,codec,row,False,'cuda',check)
                    if teacher['steps'][0]!=free['steps'][0]: raise ValueError('Same first-prefix prediction differs')
                    output=dict(id=row['id'],population=row['population'],source=row['source'],prefix=row['prefix'],
                        teacher=teacher,free=free,same_first_prefix_exact=True)
                    atomic_json(RUN/(row['id']+'.json'),output);results.append(output)
                    job.update(status='running',completed_cases=len(results),GPU_seconds=time.monotonic()-started,heartbeat_at=now())
                    atomic_json(RUN/'job.json',job)
                    print(json.dumps(dict(case=row['id'],completed=len(results),GPU_seconds=job['GPU_seconds'])),flush=True)
            torch.cuda.synchronize()
            checks=dict(weights_unchanged=all(torch.equal(v.detach().cpu(),parent['model'][k]) for k,v in model.state_dict().items()),
                RNG_unchanged=equal_state(before,rng_state()),eval_mode_unchanged=not model.training,
                all32_same_first_prefix_exact=all(r['same_first_prefix_exact'] for r in results))
            if not all(checks.values()): raise ValueError('Read-only weights/RNG/mode evidence failed')
            check(); elapsed=time.monotonic()-started
            atomic_json(OUTPUT,dict(status='all32_GPU_complete_content_review_pending',created_at=now(),identity=identity(),
                config=ref(CONFIG),preparation=c['preparation'],parent=c['parent'],checks=checks,results=results,
                GPU_seconds=elapsed,GPU_cap_seconds=120,cumulative_GPU_ledger_closed=True,
                optimizer_updates=0,scientific_teacher_tokens=0,Base_complete=False,Base_adopted=False,
                Chat_started=False,quantization_started=False,protected_test_scored=False))
            job.update(status='complete',ended_at=now(),GPU_seconds=elapsed,cumulative_GPU_ledger_closed=True)
            atomic_json(RUN/'job.json',job)
    except BaseException as error:
        if started is not None: torch.cuda.synchronize()
        job.update(status='failed',ended_at=now(),GPU_seconds=0 if started is None else time.monotonic()-started,
                   cumulative_GPU_ledger_closed=True,error=repr(error))
        atomic_json(RUN/'job.json',job); raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__); group=parser.add_mutually_exclusive_group()
    group.add_argument('--prepare',action='store_true');group.add_argument('--freeze',action='store_true')
    group.add_argument('--inspect',action='store_true');group.add_argument('--wait-ui',action='store_true')
    args=parser.parse_args()
    if args.prepare: prepare()
    elif args.freeze: freeze()
    elif args.inspect: inspect();print('Fixed consumed TRAIN/separate DEV preflight passed')
    elif args.wait_ui: wait_ui()
    else: run()
