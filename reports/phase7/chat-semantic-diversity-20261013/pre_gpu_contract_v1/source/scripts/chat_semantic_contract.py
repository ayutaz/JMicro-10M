"""Plan135 one-candidate comparison and unchanged six-hour GPU accounting."""
from contextlib import contextmanager
import json
from pathlib import Path
import time
import torch
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes
from phase6_performance import alive, identity, finite_state
from chat_first_contract import parent_state

RUN = ROOT / 'reports/phase7/chat-semantic-diversity-20261013'
OLD = ROOT / 'reports/phase7/chat-generalization-20261013'
B = 1899555
LIMITS = dict(probe=600., resume=600., train_S0=0., train_S1=3000., evaluation=14400., retention=3000.)
SPEC = dict(seed=42, context=1024, batch=32, accumulation=1, lr=1e-4, weight_decay=.01,
            warmup=0, schedule_updates=100000, dtype='bf16', compile=False, backend='math',
            scheduler='wsd', sampler='document', training_fast_path=False, update_teachers=512)
SUITES = ('new', 'previous', 'old')
ABSOLUTE_GATES = dict(joint_minimum=56, own_context_minimum=15, primary_stop_minimum=76,
                      own_stop_minimum=57, primary_empty_maximum=4, own_empty_maximum=2,
                      role_leak_maximum=0, raw_unicode_failure_maximum=0,
                      history_trim_maximum=0, candidate_repetition_must_not_increase=True)

def reference(path):
    return dict(path=str(path), sha256=sha256(Path(path)))

def require_ref(ref):
    path = Path(ref['path'])
    assert path.is_file() and sha256(path) == ref['sha256'], f'Frozen artifact differs: {path}'
    return path

def suite_ref(c, name):
    assert name in SUITES
    return c['suites'][name]

def preflight(path):
    path = Path(path)
    c = read_json(path)
    assert c['format'] == 'teacher-chat-semantic-diversity-v1' and c['teacher_budget'] == B
    assert c['purpose'] == 'direct_SFT_diagnostic_from_unadopted_original10B'
    assert c['implementation'] == implementation_hashes() and c['GPU_limits_seconds'] == LIMITS
    assert c['parameter_count'] == 10001152 and c['stop_after_stage'] == 6
    assert c['GPU_total_limit_seconds'] == sum(LIMITS.values()) == 21600
    assert c['spec'] == SPEC and c['fixed_padding'] is True
    assert c['absolute_quality_gates'] == ABSOLUTE_GATES
    assert c['parent']['sha256'] == '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
    assert c['comparison'] == dict(control='S0_latest_D1_historical', candidate='S1_one_semantic_data_recipe',
                                   final_point='t3', suites=list(SUITES), required_suites=21,
                                   required_content_judgments=4599, required_fixed_NLL_points=7,
                                   new_joint_paired_CI_lower_gt_zero=True,
                                   no_model_architecture_or_optimizer_change=True)
    for source, digest in c['source_sha256'].items():
        assert sha256(ROOT / source) == digest, source
    for key in ('parent', 'tokenizer', 'fixed_NLL'):
        require_ref(c[key])
    for ref in c['suites'].values():
        require_ref(ref)
    for ref in c['preparation_evidence'].values():
        require_ref(ref)
    reuse = read_json(require_ref(c['historical_control_evidence']))
    assert reuse['passed'] and reuse['arm'] == 'S0' and reuse['new_learning_updates'] == 0
    assert reuse['sampler_binding'] == c['arms']['S0']['sampler_binding']
    assert reuse['parent'] == c['parent'] and reuse['spec'] == SPEC
    tok = Tokenizer(c['tokenizer']['path'])
    assert tok.vocab_size == 4096
    arms = {}
    for name in ('S0', 'S1'):
        arm = c['arms'][name]
        rows = [json.loads(line) for line in require_ref(arm['records']).read_text().splitlines()]
        require_ref(arm['manifest'])
        assert rows and all(row['split'] == 'train' for row in rows)
        arms[name] = rows
    dry = read_json(c['preparation_evidence']['consumption']['path'])
    assert dry['status'] == 'passed' and all(dry['checks'].values())
    for name in arms:
        assert dry[name]['source_sha256'] == c['arms'][name]['records']['sha256']
        assert dry[name]['sampler_binding'] == c['arms'][name]['sampler_binding']
    review = read_json(c['preparation_evidence']['review']['path'])
    assert review['samples'] == 280 and review['errors'] == 0 and review['status'] == 'fixed_sample_passed'
    audit = read_json(c['preparation_evidence']['DEV_audit']['path'])
    assert audit['families'] == 80 and audit['own_families'] == 24 and audit['own_responses'] == 59
    assert audit['exact_final_question_overlap'] == 0 and audit['surface_flags'] == 0
    assert audit['dev_sha256'] == c['suites']['new']['sha256']
    assert audit['TRAIN_frozen_before_new_DEV'] is True and audit['protected_TEST_used'] is False
    assert c['Base_adopted'] is c['Chat_adopted'] is c['protected_TEST_used'] is False
    return dict(c, config_sha256=sha256(path), config_path=str(path)), tok, arms

def load_parent(c):
    state = parent_state(c)
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
