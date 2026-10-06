"""One predeclared conditional Fisher field; no training or parameter sweep."""
import argparse
import copy
import json
import os
from pathlib import Path
import signal
import sys
import time
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.model import JMicroModel
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, rng_state, synchronize
from fisher_parameter_anchor import KIND, estimate_field, tensor_digest
from phase6_performance import identity, alive, finite_state
from run_eos_short_pilot import equal_state
import run_parameter_displacement_anchor_v3 as uniform

RUN = ROOT/'reports/phase6/fisher-parameter-anchor-20261006'
PROPOSAL = ROOT/'reports/phase6/fisher_parameter_anchor_proposal.json'
CONFIG = ROOT/'configs/phase6/fisher_parameter_field.json'
SOURCES = ('scripts/fisher_parameter_anchor.py', 'scripts/build_fisher_parameter_field.py',
           'scripts/build_fisher_parameter_field.ps1', 'tests/test_fisher_parameter_anchor.py')
SETTINGS = dict(seed=2026100647, replicates=2, rows=32, context=1024,
    dtype='fp32', backend='math', TF32=False, autocast=False,
    support='actual_target_ID_ge_8', sampled_vocabulary='full_native_4096',
    score_scaling='each_row_sum_NLL/sqrt(total_fixed_body_tokens)',
    accumulation='sum_row_squared_gradients/replicates_float64',
    normalization='global_unique_coordinate_mean_one', field_floor=None)


def prepare():
    if CONFIG.exists():
        inspect()
        return
    started = time.monotonic()
    c = uniform.inspect(uniform.CONFIG)
    job = read_json(uniform.RUN/'job.json')
    if job['status'] != 'complete' or alive(job):
        raise ValueError('Actual completed uniform control required')
    completion = read_json(ROOT/'reports/phase6/parameter_displacement_anchor_completion.json')
    # Preserve rejection; the cached comparison is not an adopted Base.
    if completion.get('Base_complete', False) or completion.get('Base_adopted', False):
        raise ValueError('Prior rejection may not be relabeled')
    suites = list(ET.parse(ROOT/'reports/phase6/fisher_parameter_anchor_tests.xml').getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites) != 4 or any(int(s.attrib[k]) for s in suites for k in ('failures', 'errors', 'skipped')):
        raise ValueError('Four actual conditional expectation/fullstate CPU tests required')
    memory = uniform.reference(ROOT/'reports/phase6/finite-Web-constraint-20261006/memory.pt')
    metadata = uniform.reference(ROOT/'reports/phase6/finite-Web-constraint-20261006/memory.json')
    m = torch.load(memory['path'], map_location='cpu', weights_only=False)
    if m['x'].shape != (32, 1024) or m['y'].shape != m['x'].shape or int(m['y'].ge(8).sum()) != 32638:
        raise ValueError('Original fixed TRAIN Web packet required')
    parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
    if parent['update'] != 323503 or not finite_state(parent) or parent['sampler']['source_teachers'] != uniform.GOALS:
        raise ValueError('Same completed mixed parent as uniform control required')
    refs = dict(uniform_config=uniform.reference(uniform.CONFIG),
        uniform_result=uniform.reference(uniform.RUN/'compare-result.json'),
        uniform_review=uniform.reference(uniform.RUN/'review.json'),
        uniform_completion=uniform.reference(ROOT/'reports/phase6/parameter_displacement_anchor_completion.json'),
        block_failure=uniform.reference(ROOT/'reports/phase6/block_Web_constraint_failure_analysis.json'),
        CPU_tests=uniform.reference(ROOT/'reports/phase6/fisher_parameter_anchor_tests.xml'))
    proposal = dict(kind=KIND, created_at=now(), parent_and_anchor=c['parent'],
        hypothesis='Replace the completed uniform L2 field by TRAIN conditional model-sampled diagonal Fisher importance; protect sensitive coordinates and allow less sensitive coordinates to adapt.',
        comparison='One Fisher candidate versus cached completed uniform parameter_anchor; no old GPU rerun. Parent, inherited Adam/scheduler/RNG, source sampler, full CE quotas, LR, lambda, clipping, decoder and fixed evaluators unchanged.',
        distinction='Soft anisotropic quadratic anchor, not a finite actual-loss bound, exact Hessian, empirical GT Fisher, natural-gradient optimizer or proof of preserved quality.',
        lambda_fixed=.04161064039180984, source_teacher_goals=uniform.GOALS, source_CE_teacher_tokens=100000000,
        full_conditional_setup_and_body_and_EOS=True, outcome_weight=1,
        field_settings=SETTINGS, field_GPU_ceiling_seconds=120, own_CUDA_trainer_probe_ceiling_seconds=120,
        total_new_GPU_ceiling_seconds=1800,
        field_cost='64 score gradients/65276 model-sampled labels/65536 physical context tokens; no optimizer updates or ordinary source CE. Field, own trainer probe, science and evaluation all count inside1800s.',
        before_science='Own inherited-state CUDA4 versus2+2 including all optimizer/scheduler/RNG/sampler/counters and field/anchor binding, finite CE/gradient,32 timing updates plus saves; measured1.3margin+200evaluation fits remaining total1800s. Scientific config and training unavailable until these pass.',
        completion='One full100M candidate, same dev256/Japanese192-331-1119/native greedy80/all80 raw-bound content; unchanged relative, absolute and historical Web1% gates. Qualified recipe only proceeds to independent learning seed/full dev/protected test/adoption.',
        selection=copy.deepcopy(read_json(ROOT/'reports/phase6/finite_Web_constraint_proposal.json')['selection']),
        no_rescue='No field/sample count/seed/normalization/module/floor/lambda/LR/source/target mask/order/checkpoint/decoder sweep. Preserve terminal failures; no uniform fallback.',
        field_context_provenance='Reuse frozen original source-gradient TRAIN packet32, no dev/test or new selection. Estimate at6d mixed parent, not d18 original parent; old field losses are not this parent baseline.',
        primary_sources=[dict(title='Elastic weight consolidation, equation3', url='https://arxiv.org/html/1612.00796v2'),
            dict(title='Limitations of empirical Fisher approximation', url='https://arxiv.org/abs/1905.12558')],
        references=refs, quality_criteria_unchanged=True, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False, protected_test_used=False,
        field_GPU_seconds_so_far=0, source_CE_teacher_tokens_so_far=0, scientific_launched=False)
    if PROPOSAL.exists():
        raise ValueError('Preserve existing scientific proposal')
    atomic_json(PROPOSAL, proposal)
    config = dict(kind=KIND, phase='field_only', settings=SETTINGS, GPU_budget_seconds=120,
        parent=c['parent'], memory=memory, memory_metadata=metadata, references=refs,
        proposal=uniform.reference(PROPOSAL), uniform_source_sha256={**c['old_source_sha256'], **c['source_sha256']},
        source_sha256={s: sha256(ROOT/s) for s in SOURCES}, implementation=implementation_hashes(),
        CPU_preparation_seconds=time.monotonic()-started, created_at=now(),
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False, protected_test_used=False)
    if config['CPU_preparation_seconds'] > 30:
        raise TimeoutError('CPU preparation30s exhausted')
    atomic_json(CONFIG, config)
    inspect()
    print(json.dumps(dict(status='Fisher_field_prepared_not_science', GPU_seconds=0,
                         CPU_preparation_seconds=config['CPU_preparation_seconds'])), flush=True)


def inspect():
    c = read_json(CONFIG)
    if (c['kind'] != KIND or c['phase'] != 'field_only' or c['settings'] != SETTINGS
            or c['GPU_budget_seconds'] != 120 or c['implementation'] != implementation_hashes()
            or any(c[k] for k in ('Base_complete', 'Base_adopted', 'Chat_started', 'quantization_started', 'protected_test_used'))):
        raise ValueError('Frozen field recipe/scope differs')
    for name, digest in {**c['uniform_source_sha256'], **c['source_sha256']}.items():
        if sha256(ROOT/name) != digest:
            raise ValueError('Frozen source differs: '+name)
    for ref in (c['parent'], c['memory'], c['memory_metadata'], c['proposal'], *c['references'].values()):
        uniform.check_reference(ref)
    jp = RUN/'field/job.json'
    if jp.exists() and alive(read_json(jp)):
        raise ValueError('Actual live duplicate forbidden')
    return c


def run():
    c = inspect()
    folder = RUN/'field'
    folder.mkdir(parents=True, exist_ok=True)
    jp = folder/'job.json'
    if jp.exists():
        if read_json(jp)['status'] == 'complete':
            print('Completed fixed field retained')
            return
        raise ValueError('Preserve one-shot failure; no unbounded field retry')
    job = dict(status='setup', **identity(), config_sha256=sha256(CONFIG), started_at=now(), GPU_elapsed_seconds=0,
        restart_command='scripts/build_fisher_parameter_field.ps1 -Worker; complete fields are retained, terminal failures require a documented repair')
    atomic_json(jp, job)
    stopped = [False]
    started = None
    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, lambda *_: stopped.__setitem__(0, True))
    def check():
        if stopped[0]: raise InterruptedError('Fixed field interrupted')
        if started is not None and time.monotonic()-started > 120:
            raise TimeoutError('Actual120s field budget exhausted')
    def progress(**values):
        check()
        job.update(stage='conditional-model-sampled-score-gradients', heartbeat_at=now(),
                   GPU_elapsed_seconds=time.monotonic()-started, **values)
        atomic_json(jp, job)
    try:
        torch.set_num_threads(2)
        torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32=False
        torch.backends.cudnn.allow_tf32=False
        for relative in (*c['source_sha256'], *c['uniform_source_sha256'], CONFIG.relative_to(ROOT).as_posix(), PROPOSAL.relative_to(ROOT).as_posix()):
            target = folder/'source'/relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT/relative).read_bytes())
        parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
        memory = torch.load(c['memory']['path'], map_location='cpu', weights_only=False)
        with gpu_lock('cuda'):
            started = time.monotonic()
            job.update(status='running', stage='native-parent-loading')
            atomic_json(jp, job)
            model = JMicroModel(parent['model_config']).to('cuda')
            model.load_state_dict(parent['model'], strict=True)
            before = tensor_digest(dict(model.named_parameters()))
            before_rng = rng_state()
            state = estimate_field(model, memory, SETTINGS['seed'], SETTINGS['replicates'], check, progress)
            checks = dict(weights_unchanged=before == tensor_digest(dict(model.named_parameters())),
                RNG_unchanged=equal_state(before_rng, rng_state()), parameter_grads_unchanged=all(p.grad is None for p in model.parameters()),
                native_unique_10M=sum(p.numel() for p in model.parameters()) == 10001152,
                native_unique119=len(list(model.named_parameters())) == 119,
                exact_cost=state['accounting'] == dict(score_gradient_calls=64, sampled_score_labels=65276,
                    physical_context_tokens=65536, ordinary_source_CE_teacher_tokens=0, optimizer_updates=0))
            if not all(checks.values()):
                raise ValueError('Frozen native field integrity/accounting failed')
            check()
            field_path = folder/'field.pt'
            if field_path.exists(): raise ValueError('Preserve existing field artifact')
            state.update(kind=KIND, parent=c['parent'], memory=c['memory'], config_sha256=sha256(CONFIG))
            temporary = field_path.with_suffix('.tmp')
            with temporary.open('wb') as stream:
                torch.save(state, stream)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, field_path)
            synchronize('cuda')
            check()
            elapsed = time.monotonic()-started
            result = dict(kind=KIND, config_sha256=sha256(CONFIG), passed=True, checks=checks,
                field=uniform.reference(field_path), parent=c['parent'], field_tensor_digest=state['field_tensor_digest'],
                settings=SETTINGS, accounting=state['accounting'], normalization=state['normalization'],
                scores=state['scores'], sampled_labels_tensor_digest=tensor_digest({'sampled_labels': state['sampled_labels']}),
                normalized_field_max=max(float(v.max()) for v in state['field'].values()),
                normalized_zero_coordinates=sum(int(v.eq(0).sum()) for v in state['field'].values()),
                GPU_seconds=elapsed, Base_complete=False, scientific_launched=False,
                next_action='Own weighted trainer CUDA fullstate/timing gate within remaining total1800s; field alone is not quality.')
            atomic_json(folder/'result.json', result)
            job.update(status='complete', stage='fixed-field-complete-not-science', ended_at=now(), GPU_elapsed_seconds=elapsed)
            atomic_json(jp, job)
            print(json.dumps(dict(status=job['stage'], GPU_seconds=elapsed, accounting=state['accounting'])), flush=True)
    except BaseException as exc:
        job.update(status='failed_or_interrupted', ended_at=now(), error=f'{type(exc).__name__}: {exc}',
                   GPU_elapsed_seconds=time.monotonic()-started if started is not None else 0)
        atomic_json(jp, job)
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--prepare', action='store_true')
    parser.add_argument('--inspect', action='store_true')
    args = parser.parse_args()
    if args.prepare: prepare()
    elif args.inspect: inspect(); print('Fixed field recipe valid; no GPU')
    else: run()
