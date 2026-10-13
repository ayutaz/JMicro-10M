"""One LR-only comparison; original sources and closed runs remain frozen."""
from contextlib import contextmanager
import json
from pathlib import Path
import time
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes
from phase6_performance import alive, identity, finite_state
from chat_first_contract import parent_state
from chat_semantic_contract import SPEC as CONTROL_SPEC, ABSOLUTE_GATES

RUN = ROOT / 'reports/phase7/chat-lr-20261014'
OLD = ROOT / 'reports/phase7/chat-semantic-diversity-20261013'
DATA = Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-lr-20261014')
CONFIG = ROOT / 'configs/phase7/chat-lr-20261014.json'
B = 1899555
SPEC = dict(CONTROL_SPEC, lr=3e-5)
SUITES = ('new', 'semantic', 'previous', 'old')
LIMITS = dict(probe=600., resume=600., train_S0=0., train_S1=3000., evaluation=14400., retention=3000.,
              independent_training=3000., independent_evaluation=4200., fullDEV=3600., protectedTEST=1200.)
TOTAL = sum(LIMITS.values())


def reference(path):
    path = Path(path)
    return dict(path=str(path), sha256=sha256(path))


def require_ref(ref):
    path = Path(ref['path'])
    assert path.is_file() and sha256(path) == ref['sha256'], str(path)
    return path


def suite_ref(c, name):
    assert name in SUITES
    return c['suites'][name]


def preflight(path=CONFIG):
    path = Path(path).resolve()
    assert path == CONFIG
    c = read_json(path)
    assert c['format'] == 'teacher-chat-lr-only-v1' and c['teacher_budget'] == B
    assert c['spec'] == SPEC and c['control_spec'] == CONTROL_SPEC
    assert {key for key in SPEC if SPEC[key] != CONTROL_SPEC[key]} == {'lr'}
    assert c['implementation'] == implementation_hashes()
    assert c['GPU_limits_seconds'] == LIMITS and c['GPU_total_limit_seconds'] == TOTAL == 33600
    assert c['parameter_count'] == 10001152 and c['fixed_padding']
    assert c['absolute_quality_gates'] == ABSOLUTE_GATES
    assert c['comparison']['required_suites'] == 28 and c['comparison']['required_content_judgments'] == 6132
    assert c['comparison']['required_fixed_NLL_points'] == 7 and c['comparison']['final_point'] == 't3'
    assert list(c['suites']) == list(SUITES)
    assert c['parent']['sha256'] == '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
    for source, digest in c['source_sha256'].items():
        assert sha256(ROOT / source) == digest, source
    for ref in (c['parent'], c['tokenizer'], c['fixed_NLL'], c['TRAIN'], c['TRAIN_manifest'],
                c['TRAIN_QA'], c['historical_training_audit'], c['historical_learning_metrics'],
                c['candidate_consumption'], c['protected_split_incident'], c['old_config'], *c['suites'].values()):
        require_ref(ref)
    old = read_json(require_ref(c['old_config']))
    assert old['arms']['S1']['records'] == c['TRAIN'] and old['parent'] == c['parent']
    assert old['spec'] == CONTROL_SPEC and old['teacher_budget'] == B
    dry = read_json(require_ref(c['historical_consumption']))
    assert dry['Assistant_teachers'] == 1899557 and dry['updates'] == 3646 and dry['final_overshoot'] == 2
    qa = read_json(require_ref(c['TRAIN_QA']))
    assert qa['samples'] == 280 and qa['errors'] == 0 and qa['status'] == 'fixed_sample_passed'
    dev = read_json(require_ref(c['DEV_audit']))
    assert dev['passed'] and dev['TRAIN_frozen_before_new_DEV'] and not dev['protected_TEST_used']
    assert dev['families'] == 80 and dev['own_families'] == 24 and dev['own_responses'] == 59
    assert dev['source_TRAIN_sha256'] == c['TRAIN']['sha256']
    assert dev['dev_sha256'] == c['suites']['new']['sha256']
    assert c['original_Chat_TEST_parsed_in_failed_preparation'] is True
    assert c['final_Chat_TEST_requires_fresh_sealed_cases'] is True
    incident = read_json(require_ref(c['protected_split_incident']))
    assert incident['old_protected_chat_TEST_parsed'] and not incident['used_for_training']
    audit = read_json(require_ref(c['historical_training_audit']))
    assert audit['passed'] and audit['all_optimizer_steps_finite'] and audit['parameter_count'] == 10001152
    assert not any(c[k] for k in ('Base_adopted', 'Chat_adopted', 'protected_TEST_used'))
    records = [json.loads(line) for line in require_ref(c['TRAIN']).read_text().splitlines()]
    assert len(records) == 41529 and all(row['split'] == 'train' for row in records)
    tok = Tokenizer(require_ref(c['tokenizer']))
    assert tok.vocab_size == 4096
    return dict(c, config_sha256=sha256(path), config_path=str(path)), tok, {'S1': records}


def load_parent(c):
    state = parent_state(c)
    assert finite_state(state)
    return state


def ledger():
    path = RUN / 'GPU_ledger.json'
    data = read_json(path) if path.exists() else dict(created_at=now(), limits=LIMITS, total_limit=TOTAL, entries=[])
    assert data['limits'] == LIMITS and data['total_limit'] == TOTAL
    for entry in data['entries']:
        if entry['status'] == 'running':
            if alive(entry):
                raise RuntimeError('Recorded GPU process alive; duplicate refused')
            other = sum(row['charged_seconds'] for row in data['entries'] if row is not entry and row['category'] == entry['category'])
            entry.update(status='interrupted_unmeasured_conservatively_charged',
                         charged_seconds=max(0., LIMITS[entry['category']] - other), reconciled_at=now())
    atomic_json(path, data)
    return data


def remaining(category):
    data = ledger()
    return min(LIMITS[category] - sum(row['charged_seconds'] for row in data['entries'] if row['category'] == category),
               TOTAL - sum(row['charged_seconds'] for row in data['entries']))


@contextmanager
def GPU_stage(category, name, config_sha):
    assert category in LIMITS
    with gpu_lock('cuda'):
        data = ledger()
        available = min(LIMITS[category] - sum(row['charged_seconds'] for row in data['entries'] if row['category'] == category),
                        TOTAL - sum(row['charged_seconds'] for row in data['entries']))
        if available <= 0:
            raise TimeoutError('Frozen GPU allocation exhausted')
        started = time.monotonic()
        entry = dict(**identity(), category=category, name=name, config_sha256=config_sha,
                     status='running', started_at=now(), charged_seconds=0., available_seconds=available)
        data['entries'].append(entry)
        atomic_json(RUN / 'GPU_ledger.json', data)
        def left():
            return available - (time.monotonic() - started)
        def heartbeat(**values):
            entry.update(charged_seconds=time.monotonic() - started, heartbeat_at=now(), **values)
            atomic_json(RUN / 'GPU_ledger.json', data)
        try:
            yield left, heartbeat
            entry['status'] = 'complete'
        except BaseException as exc:
            entry.update(status='failed_or_stopped', error=repr(exc))
            raise
        finally:
            entry.update(charged_seconds=time.monotonic() - started, ended_at=now())
            if entry['charged_seconds'] > available:
                entry['status'] = 'budget_exceeded'
            data['total_charged_seconds'] = sum(row['charged_seconds'] for row in data['entries'])
            atomic_json(RUN / 'GPU_ledger.json', data)
            if entry['status'] == 'budget_exceeded':
                raise TimeoutError('Frozen GPU allocation exceeded')
