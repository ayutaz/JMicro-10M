"""Read-only, bounded gold/free-generation diagnostics for roadmap stages1-3."""
import argparse
import gc
import json
import os
from pathlib import Path
import random
import signal
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import torch
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, seed_all
from phase6_performance import alive, identity
from run_root_cause_diagnostic import teacher, generate

RUN = ROOT / 'reports/phase6/generation-transfer-20261006'
OLD = ROOT / 'reports/phase6/narrative-diversity-v2-20261005'
DATA = Path('/home/aihub_ubuntu/jmicro-data/phase6/narrative-diversity-v2-20261005')
CONFIG = ROOT / 'configs/phase6/generation_transfer.json'


def make_case(record, tok, split):
    body = tok.encode(record['text'])
    # Prefix is a slice of the original token sequence: no retokenization mismatch.
    candidates = []
    for end in range(4, len(body) - 3):
        try:
            text = tok.decode_bytes(body[:end]).decode('utf-8')
        except UnicodeDecodeError:
            continue
        if text.endswith(('。', '！', '？', '\n')):
            candidates.append(end)
    if not candidates:
        raise ValueError('No complete sentence prefix: ' + record['doc_id'])
    end = candidates[0]
    return dict(id=record['doc_id'], source=split, text=record['text'],
        prefix=tok.decode(body[:end]), continuation=tok.decode(body[end:]),
        body_ids=body, prefix_ids=[2, *body[:end]], gold_ids=[*body[end:], 3],
        prefix_body_tokens=end, gold_body_tokens=len(body)-end,
        canonical_sha256=record['canonical_sha256'], origin=record.get('source_metadata', {}),
        semantic_departure='requires qualitative review; token departure alone is not semantic failure')


def summary(cases, scored, short, long):
    if not (len(cases) == len(scored) == len(short) == len(long)):
        raise ValueError('Incomplete diagnostic coverage')
    groups = {}
    for split in ('train', 'dev'):
        indices = [i for i, row in enumerate(cases) if row['source'] == split]
        rows = [scored[i] for i in indices]
        groups[split] = dict(documents=len(indices),
            gold_continuation_exceeds64=sum(len(cases[i]['gold_ids']) > 64 for i in indices),
            teacher_top1_fraction=sum(r['teacher_top1_fraction'] for r in rows)/len(rows),
            teacher_NLL=sum(r['teacher_nll_mean'] for r in rows)/len(rows),
            gold_EOS_top1=sum(r['ending']['eos_rank'] == 1 for r in rows),
            gold_EOS_NLL=sum(r['ending']['target_nll'] for r in rows)/len(rows),
            greedy64_EOS=sum(short[i]['stop_reason'] == 'eos' for i in indices),
            greedy256_EOS=sum(long[i]['stop_reason'] == 'eos' for i in indices),
            additional_stops_after64=sum(short[i]['stop_reason'] != 'eos' and long[i]['stop_reason'] == 'eos' for i in indices),
            greedy256_repeated4gram=sum(long[i]['first_repeated_4gram'] is not None for i in indices),
            first_token_matches_gold=sum(short[i]['generated_ids'][0] == cases[i]['gold_ids'][0] for i in indices),
            interpretation='EOS beyond64 diagnoses truncation; it does not replace frozen64 quality gates')
    return groups


def prepare():
    if CONFIG.exists():
        validate(); print('Existing frozen diagnostic retained'); return
    RUN.mkdir(parents=True, exist_ok=True)
    c = read_json(ROOT / 'configs/phase6/narrative_comparison.json')
    result = read_json(OLD / 'compare-result.json')
    tok = Tokenizer(ROOT / c['tokenizer'])
    assert sha256(tok.path) == c['tokenizer_sha256']
    train = random.Random(202610080).sample(read_json(DATA / 'sample-initial.json'), 32)
    dev = random.Random(202610081).sample(read_json(DATA / 'dev64.json'), 32)
    cases = [make_case(r, tok, split) for split, records in [('train', train), ('dev', dev)] for r in records]
    assert len({r['canonical_sha256'] for r in cases}) == 64
    assert all(len(r['prefix_ids']) + 256 <= 1024 for r in cases)
    write_json(RUN / 'cases.json', cases)
    checkpoints = {name: result['checkpoints'][arm] for name, arm in [('control','mixed-control'), ('diverse','mixed-diverse')]}
    sources = ('scripts/run_generation_transfer.py', 'scripts/run_generation_transfer.ps1', 'scripts/run_root_cause_diagnostic.py')
    config = dict(created_at=now(), scope='Roadmap1-3 resumed: first read-only stage1 diagnostic',
        checkpoints={k:dict(path=v['checkpoint'],sha256=v['checkpoint_sha256']) for k,v in checkpoints.items()},
        tokenizer=c['tokenizer'],tokenizer_sha256=c['tokenizer_sha256'], cases_sha256=sha256(RUN/'cases.json'),
        implementation=implementation_hashes(),source_sha256={p:sha256(ROOT/p) for p in sources},
        contract_sha256=sha256(ROOT/'docs/80_generation_transfer_plan.md'),
        gpu_budget_seconds=600,scientific_teacher_tokens=0,optimizer_updates=0,
        generation_limits=[64,256],protected_test_used=False,quality_goals_changed=False)
    write_json(CONFIG, config)
    print(json.dumps(dict(status='prepared',train=32,dev=32,training_tokens=0)),flush=True)


def validate():
    c=read_json(CONFIG)
    assert c['implementation']==implementation_hashes()
    assert all(sha256(ROOT/p)==s for p,s in c['source_sha256'].items())
    assert sha256(RUN/'cases.json')==c['cases_sha256']
    assert sha256(ROOT/c['tokenizer'])==c['tokenizer_sha256']
    assert sha256(ROOT/'docs/80_generation_transfer_plan.md')==c['contract_sha256']
    return c


def run():
    c=validate(); job_path=RUN/'job.json'
    previous=read_json(job_path) if job_path.exists() else {}
    if previous:
        assert not alive(previous), 'Diagnostic already live'
        assert previous['config_sha256']==sha256(CONFIG)
        if previous['status']=='complete': print('Completed diagnostic retained'); return
    start=time.monotonic(); prior=previous.get('gpu_elapsed_seconds',0); stopped=[False]
    job=dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),
        gpu_elapsed_seconds=prior,scientific_teacher_tokens=0,restart_command='scripts/run_generation_transfer.ps1')
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True))
    def check(stage):
        if stopped[0]:raise InterruptedError('Stop requested')
        if prior+time.monotonic()-start>c['gpu_budget_seconds']:raise TimeoutError('600s diagnostic GPU budget exhausted')
        job.update(status='running',stage=stage,heartbeat_at=now(),gpu_elapsed_seconds=prior+time.monotonic()-start)
        atomic_json(job_path,job)
    try:
        seed_all(42);torch.set_num_threads(2);tok=Tokenizer(ROOT/c['tokenizer']);cases=read_json(RUN/'cases.json')
        with gpu_lock('cuda'):
            for arm,entry in c['checkpoints'].items():
                check(arm+'-load');assert sha256(Path(entry['path']))==entry['sha256']
                state=torch.load(entry['path'],map_location='cpu',weights_only=False)
                model=JMicroModel(state['model_config']).cuda().eval();model.load_state_dict(state['model']);del state
                scored=[]; short=[]; long=[]
                for offset in range(0,len(cases),16):
                    path=RUN/f'{arm}-{offset:02d}.json'
                    if path.exists():
                        chunk=read_json(path);assert chunk['checkpoint_sha256']==entry['sha256']
                    else:
                        rows=cases[offset:offset+16];check(f'{arm}-{offset}-teacher')
                        gold=teacher(model,rows);check(f'{arm}-{offset}-greedy64')
                        g64=generate(model,rows,tok,None,64);check(f'{arm}-{offset}-greedy256')
                        g256=generate(model,rows,tok,None,256)
                        assert all(a['generated_ids']==b['generated_ids'][:len(a['generated_ids'])] for a,b in zip(g64,g256))
                        chunk=dict(checkpoint_sha256=entry['sha256'],teacher=gold,greedy64=g64,greedy256=g256)
                        write_json(path,chunk)
                    scored.extend(chunk['teacher']);short.extend(chunk['greedy64']);long.extend(chunk['greedy256'])
                write_json(RUN/(arm+'-result.json'),dict(checkpoint=entry,cases_sha256=c['cases_sha256'],
                    summary=summary(cases,scored,short,long),teacher=scored,greedy64=short,greedy256=long,
                    training_tokens=0,protected_test_used=False))
                print(json.dumps(dict(arm=arm,summary=summary(cases,scored,short,long))),flush=True)
                del model;gc.collect();torch.cuda.empty_cache()
        job.update(status='complete',completed_at=now())
    except BaseException as error:
        job.update(status='failed',error=repr(error));raise
    finally:
        job['gpu_elapsed_seconds']=prior+time.monotonic()-start;atomic_json(job_path,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--prepare',action='store_true');a=p.parse_args()
    prepare() if a.prepare else run()
