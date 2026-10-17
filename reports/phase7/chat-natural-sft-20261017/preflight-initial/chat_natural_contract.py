"""Owned plan149 contract. Frozen native trainers and old runs are read-only."""
from contextlib import contextmanager
import json
from pathlib import Path
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, sha256, read_json
from jmicro.training import atomic_json, implementation_hashes, gpu_lock
from jmicro.tokenizer import Tokenizer
from phase6_performance import identity, alive

DATA = Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-natural-sft-20261017')
RUN = ROOT / 'reports/phase7/chat-natural-sft-20261017'
CONFIG = ROOT / 'configs/phase7/chat-natural-sft-20261017.json'
BUDGET = 1000000
SPEC = dict(seed=42, context=1024, batch=32, accumulation=1, lr=3e-5, weight_decay=.01,
            warmup=0, schedule_updates=100000, dtype='bf16', compile=False, backend='math',
            scheduler='wsd', sampler='document', training_fast_path=False, update_teachers=512)
LIMITS = dict(probe=600., train_C0=3600., train_C1=3600., evaluation=10800.)
GATES = dict(content_minimum=56, own_context_minimum=15, primary_stop_minimum=76,
             own_stop_minimum=57, primary_empty_maximum=4, own_empty_maximum=2,
             role_leak_maximum=0, raw_unicode_failure_maximum=0, history_trim_maximum=0,
             candidate_repetition_must_not_increase=True)
SUITES = ('new', 'lr', 'semantic', 'generalization', 'original')
SOURCES = ('scripts/chat_natural_contract.py','scripts/run_chat_natural.py',
           'scripts/evaluate_chat_natural.py','scripts/run_chat_natural.ps1',
           'scripts/inspect_chat_natural_environment.py','scripts/start_webui.ps1','scripts/stop_webui.ps1',
           'src/jmicro/model.py','src/jmicro/training.py','src/jmicro/tokenizer.py',
           'src/jmicro/assistant_sampler.py','src/jmicro/teacher_chat_training.py','src/jmicro/chat_evaluation.py')


def ref(path):
    path = Path(path)
    return dict(path=str(path), sha256=sha256(path))


def require_ref(value):
    path = Path(value['path'])
    if not path.is_file() or sha256(path) != value['sha256']:
        raise ValueError(f'Frozen artifact differs: {path}')
    return path


def read_dev(value, allowed_directory=DATA / 'dev_suites'):
    path = Path(value['path']).resolve()
    # The mixed historical file is rejected before opening. Only the five
    # dedicated DEV exports, bound by the signed-off local config, are accepted.
    if path.parent != allowed_directory.resolve() or path.name not in {s+'.jsonl' for s in SUITES}:
        raise ValueError('Only a bound dedicated DEV export may be read')
    require_ref(value)
    cases = []
    for line in path.read_text().splitlines():
        row = json.loads(line)
        if row.get('split') != 'dev':
            raise ValueError('Mixed or protected split refused')
        cases.append(row)
    if len(cases) != 80 or len({c['family_id'] for c in cases}) != 80:
        raise ValueError('Expected80 unique DEV families')
    contexts = [c for c in cases if len(c['messages']) > 1]
    if len(contexts) != 24 or sum(sum(m['role'] == 'user' for m in c['messages']) for c in contexts) != 59:
        raise ValueError('Expected24 own-history families/59 turns')
    return cases, contexts


def preflight():
    c = read_json(CONFIG)
    assert c['format'] == 'natural-short-chat-v1' and c['teacher_budget'] == BUDGET
    assert c['spec'] == SPEC and c['limits_seconds'] == LIMITS and c['quality_gates'] == GATES
    assert c['implementation'] == implementation_hashes() and c['max_new_tokens'] == 32
    assert c['maximum_teacher_length'] == 32 and c['final_overshoot_maximum'] == 31
    assert c['parameter_count'] == 10001152 and tuple(c['suites']) == SUITES
    assert c['parent']['sha256'] == '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
    assert c['tokenizer']['sha256'] == 'a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'
    assert c['source_sha256'] == {p:sha256(ROOT / p) for p in SOURCES}
    assert not c['protected_TEST_used'] and not c['Chat_adopted'] and not c['Base_adopted']
    for value in (c['parent'], c['tokenizer'], c['TRAIN_manifest'], c['TRAIN_QA'], c['DEV_preparation'], c['NLL']):
        require_ref(value)
    dev = read_json(c['DEV_preparation']['path'])
    assert dev['TRAIN_frozen_before_new_DEV'] and not dev['protected_TEST_used']
    tok = Tokenizer(c['tokenizer']['path'])
    for value in c['suites'].values():
        cases, _ = read_dev(value)
        assert all(tok.chat_prompt(case['messages'], 992)[1] == 0 for case in cases)
    identity_file = read_json(DATA / 'RPC_allowed_identities.json')
    allowed = {'real_persona_chat:'+m for m in identity_file['train']}
    forbidden_magpie = set(read_json(DATA / 'magpie_reserved_DEV_identities.json')['ids'])
    arms = {}
    for arm in ('C0','C1'):
        a = c['arms'][arm]
        require_ref(a['records']); require_ref(a['dry_run'])
        rows = [json.loads(line) for line in Path(a['records']['path']).read_text().splitlines()]
        assert all(r['split'] == 'train' and (r['doc_id'] in allowed if r['source'] == 'RPC'
                   else r['doc_id'].startswith('magpie:') and r['doc_id'] not in forbidden_magpie) for r in rows)
        assert len({r['doc_id'] for r in rows}) == len(rows)
        dry = read_json(a['dry_run']['path'])
        assert dry['status'] == 'passed' and dry['records']['sha256'] == a['records']['sha256']
        assert dry['sampler_binding'] == a['sampler_binding']
        arms[arm] = rows
    return dict(c, config_sha256=sha256(CONFIG)), tok, arms


@contextmanager
def stage(category, config_hash):
    with gpu_lock('cuda'):
        path = RUN / 'GPU_ledger.json'
        ledger = read_json(path) if path.exists() else dict(limits_seconds=LIMITS, entries=[])
        assert ledger['limits_seconds'] == LIMITS
        for row in ledger['entries']:
            if row['status'] == 'running':
                raise RuntimeError('Unreconciled GPU stage; verify identity and time before resuming')
        spent = sum(r['seconds'] for r in ledger['entries'] if r['category'] == category)
        left_at_start = LIMITS[category] - spent
        assert left_at_start > 30
        started = time.monotonic()
        row = dict(**identity(), category=category, status='running', config_sha256=config_hash,
                   started_at=now(), seconds=0., remaining_at_start=left_at_start)
        ledger['entries'].append(row)
        def left():
            return left_at_start - (time.monotonic()-started)
        def beat(**values):
            row.update(seconds=time.monotonic()-started, heartbeat_at=now(), **values)
            atomic_json(path, ledger)
        beat()
        try:
            yield left, beat
            row['status'] = 'complete'
        except BaseException as error:
            row.update(status='failed_or_interrupted', error=repr(error))
            raise
        finally:
            row.update(seconds=time.monotonic()-started, ended_at=now())
            ledger['total_seconds'] = sum(r['seconds'] for r in ledger['entries'])
            atomic_json(path, ledger)
            if left() < 0:
                raise TimeoutError('Frozen stage allocation exceeded; no automatic condition rescue')


def freeze():
    assert not CONFIG.exists(), 'Preserve frozen new comparison'
    manifest = read_json(DATA / 'manifest.json')
    dev = read_json(RUN / 'DEV_preparation.json')
    c = dict(format='natural-short-chat-v1', created_at=now(), spec=SPEC, teacher_budget=BUDGET,
        parameter_count=10001152, limits_seconds=LIMITS, quality_gates=GATES,
        implementation=implementation_hashes(), source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        maximum_teacher_length=32, final_overshoot_maximum=31, max_new_tokens=32,
        parent=ref(ROOT/'reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt'),
        tokenizer=ref(ROOT/'artifacts/phase2/4096/tokenizer.model'),
        TRAIN_manifest=ref(DATA/'manifest.json'), TRAIN_QA=ref(RUN/'TRAIN_QA_review.json'),
        DEV_preparation=ref(RUN/'DEV_preparation.json'), NLL=dev['NLL'], suites=dev['suites'],
        arms={arm:dict(records=manifest['arms'][arm]['records'], dry_run=ref(RUN/f'{arm}_dry_run.json'),
                       sampler_binding=manifest['arms'][arm]['sampler_binding']) for arm in ('C0','C1')},
        comparison=dict(control='New matched original-pilot TRAIN, common filters',
                        candidate='Broader real conversation recipe, actual short Magpie1.556percent teachers',
                        primary_point=1000000, savepoints=[250000,500000,1000000],
                        final_suites=10, final_content_judgments=2190, intermediate_diagnostic_responses=40,
                        paired_family_CI_bootstrap_seed=42, bootstrap_replicates=2000,
                        improved_new_content_CI_lower_gt=0, formal_Base_retention_pending=True),
        old64_token_results_unchanged=True, maximum_token_stop_is_not_natural_stop=True,
        authorized_scope='Plan149 stages1-5; short responses requested before contract freeze',
        protected_TEST_used=False, Chat_adopted=False, Base_adopted=False)
    atomic_json(CONFIG, c)
    preflight()
    atomic_json(RUN/'contract_frozen.json', dict(status='preflight_passed', config=ref(CONFIG), created_at=now(),
        new_GPU_updates=0, whole_five_stage_goal_complete=False))
    print('New10M matched short-response SFT contract frozen; GPU0')


if __name__ == '__main__':
    freeze()
