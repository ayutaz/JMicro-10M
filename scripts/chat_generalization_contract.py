"""Frozen plan133 contract and shared, non-overlapping GPU accounting."""
from contextlib import contextmanager
import json
from pathlib import Path
import time

import torch
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock,implementation_hashes
from phase6_performance import alive,identity,finite_state
from chat_first_contract import parent_state

RUN=ROOT/'reports/phase7/chat-generalization-20261013'
B=1899555
# D0 must reuse the exactly matching closed C1 experiment. Its former learning
# allocation reserves conditional recovery and a separate padding diagnostic.
LIMITS=dict(probe=600.,resume=600.,train_D0=0.,train_D1=3600.,evaluation=10800.,
    retention=2400.,recovery=2700.,efficiency=900.)


def reference(path):return dict(path=str(path),sha256=sha256(Path(path)))


def require_ref(ref):
    path=Path(ref['path'])
    assert path.is_file() and sha256(path)==ref['sha256'],f'Frozen artifact differs: {path}'
    return path


def preflight(path):
    path=Path(path);c=read_json(path)
    assert c['format']=='teacher-chat-generalization-v1' and c['teacher_budget']==B
    assert c['purpose']=='direct_SFT_diagnostic_from_unadopted_original10B'
    assert c['implementation']==implementation_hashes() and c['GPU_limits_seconds']==LIMITS
    assert c['parameter_count']==10001152 and c['stop_after_stage']==4 and c['GPU_total_limit_seconds']==21600
    assert c['parent']['sha256']=='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
    for source,digest in c['source_sha256'].items():assert sha256(ROOT/source)==digest,source
    for key in ('parent','tokenizer','new_DEV','old_suite','fixed_NLL'):
        require_ref(c[key])
    for ref in c['preparation_evidence'].values():require_ref(ref)
    reuse=read_json(require_ref(c['historical_control_evidence']))
    assert reuse['passed'] and reuse['arm']=='D0' and reuse['new_learning_updates']==0
    assert reuse['D0_binding']==c['arms']['D0']['sampler_binding']
    assert c['spec']==dict(seed=42,context=1024,batch=32,accumulation=1,lr=1e-4,weight_decay=.01,
        warmup=0,schedule_updates=100000,dtype='bf16',compile=False,backend='math',scheduler='wsd',
        sampler='document',training_fast_path=False,update_teachers=512)
    tok=Tokenizer(c['tokenizer']['path']);assert tok.vocab_size==4096
    arms={}
    for name in ('D0','D1'):
        arm=c['arms'][name];file=require_ref(arm['records']);require_ref(arm['manifest'])
        rows=[json.loads(l) for l in file.read_text().splitlines()]
        assert rows and all(r['split']=='train' for r in rows)
        arms[name]=rows
    dry=read_json(Path(c['preparation_evidence']['consumption']['path']))
    assert dry['status']=='passed' and all(dry['checks'].values())
    for name in arms:
        assert dry[name]['source_sha256']==c['arms'][name]['records']['sha256']
        assert dry[name]['sampler_binding']==c['arms'][name]['sampler_binding']
    review=read_json(Path(c['preparation_evidence']['review']['path']))
    assert review['samples']==280 and review['errors']==0 and review['status']=='fixed_sample_passed'
    audit=read_json(Path(c['preparation_evidence']['DEV_audit']['path']))
    assert audit['families']==80 and audit['own_families']==24 and audit['own_responses']==59
    assert audit['exact_final_question_overlap']==0 and audit['surface_flags']==0
    assert audit['dev_sha256']==c['new_DEV']['sha256']
    c=dict(c,config_sha256=sha256(path),config_path=str(path))
    return c,tok,arms


def load_parent(c):
    # Existing helper verifies native 13-layer/256/10,001,152 architecture,
    # original 305176 update, unmodified implementation and finite source state.
    state=parent_state(c)
    assert finite_state(state)
    return state


def ledger():
    path=RUN/'GPU_ledger.json'
    result=read_json(path) if path.exists() else dict(created_at=now(),limits=LIMITS,total_limit=21600.,entries=[])
    assert result['limits']==LIMITS and result['total_limit']==21600
    for row in result['entries']:
        if row['status']=='running':
            if alive(row):raise RuntimeError('Another recorded GPU stage is alive')
            # A stale process cannot silently restore its unmeasured wall time.
            # Conservatively charge the whole remaining category allocation.
            others=sum(r['charged_seconds'] for r in result['entries'] if r is not row and r['category']==row['category'])
            row.update(status='interrupted_unmeasured_conservatively_charged',
                charged_seconds=max(0.,LIMITS[row['category']]-others),reconciled_at=now())
    atomic_json(path,result)
    return result


def remaining(category):
    data=ledger()
    category_left=LIMITS[category]-sum(r['charged_seconds'] for r in data['entries'] if r['category']==category)
    total_left=21600.-sum(r['charged_seconds'] for r in data['entries'])
    return min(category_left,total_left)


@contextmanager
def GPU_stage(category,name,config_sha):
    assert category in LIMITS
    with gpu_lock('cuda'):
        data=ledger();available=min(LIMITS[category]-sum(r['charged_seconds'] for r in data['entries'] if r['category']==category),
            21600.-sum(r['charged_seconds'] for r in data['entries']))
        if available<=0:raise TimeoutError(f'{category} budget exhausted')
        started=time.monotonic();row=dict(**identity(),category=category,name=name,config_sha256=config_sha,
            status='running',started_at=now(),charged_seconds=0.,available_seconds=available)
        data['entries'].append(row);atomic_json(RUN/'GPU_ledger.json',data)
        def left():return available-(time.monotonic()-started)
        def heartbeat(**values):
            row.update(charged_seconds=time.monotonic()-started,heartbeat_at=now(),**values)
            atomic_json(RUN/'GPU_ledger.json',data)
        try:
            yield left,heartbeat
            row['status']='complete'
        except BaseException as exc:
            row.update(status='failed_or_stopped',error=repr(exc));raise
        finally:
            row.update(charged_seconds=time.monotonic()-started,ended_at=now())
            if row['charged_seconds']>available:row['status']='budget_exceeded'
            data['total_charged_seconds']=sum(r['charged_seconds'] for r in data['entries'])
            atomic_json(RUN/'GPU_ledger.json',data)
            if row['status']=='budget_exceeded':raise TimeoutError(f'{category} exceeded the frozen remaining GPU budget')
