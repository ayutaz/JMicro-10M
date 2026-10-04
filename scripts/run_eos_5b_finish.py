"""Frozen low-LR Web/short20 finishing pair from final5B, unchanged raw metrics."""
import argparse
import gc
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jsonschema import validate
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.eos_pilot import TrainView
from jmicro.evaluation_memory import bound_evaluation_cache
from jmicro.experiment import ROOT, now, read_json, write_json, sha256
from jmicro.low_lr_pilot import LowLRPilotTrainer
from jmicro.model import JMicroModel
from jmicro.readiness import evaluate_batched
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, seed_all, generate_suite, rng_state
from phase6_performance import identity, alive
import run_eos_short_pilot as pilot
from run_eos_complete_100m import adoption_checks, auxiliary_evaluation
from run_eos_low_lr import tests_summary

SOURCES = ('scripts/run_eos_5b_finish.py', 'scripts/run_eos_5b_finish.sh',
    'scripts/run_eos_short_pilot.py', 'scripts/run_eos_complete_100m.py', 'scripts/run_eos_low_lr.py',
    'src/jmicro/eos_pilot.py', 'src/jmicro/low_lr_pilot.py', 'src/jmicro/readiness.py',
    'src/jmicro/evaluation_memory.py', 'src/jmicro/inference.py', 'src/jmicro/text_display.py')


def safe_control(rates, parent_repetition):
    return rates['repetition'] < min(60,parent_repetition)+8 and all(
        rates[k] == 0 for k in ('empty','role_leak','unicode_failure'))


def freeze(path):
    old = read_json(ROOT / 'configs/phase6/eos_low_lr_100m.json')
    base = read_json(ROOT / 'configs/phase6/base_5b_comparison.json')
    plan = {k: old[k] for k in ('web_shards', 'web_manifest_sha256', 'dev_shards', 'tokenizer',
        'tokenizer_sha256', 'suite_sha256', 'short_pool', 'short_manifest_sha256', 'auxiliary_sha256',
        'updates_per_arm', 'stable_updates', 'decay_updates', 'short_updates', 'tokens_per_update',
        'tokens_per_arm', 'scientific_total_tokens', 'peak_lr')}
    plan.update(version=1, scope='Authorized steps1-3 final5B finishing pair; no10B/Chat/UL/sweeps',
        output='reports/phase6/eos-5b-finish-100m-20261004', gpu_budget_seconds=3000,
        parent=dict(path=base['checkpoint'], sha256=base['checkpoint_sha256'], update=152588, tokens_seen=5000003584),
        reused_preparation='reports/phase6/eos-complete-100m-20261004-r2',
        parent_full_body= str(ROOT / base['output'] / 'full-dev.json'),
        parent_generation=str(ROOT / base['output'] / 'generation.json'),
        baseline_body_sha256=sha256(ROOT / base['output'] / 'full-dev.json'),
        baseline_generation_sha256=sha256(ROOT / base['output'] / 'generation.json'),
        parent_full_BPB=.9644840703259737, parent_fixed_repetition=59,
        final_cumulative_tokens=5100011520, final_update=155640,
        quality_criteria_unchanged=True, test_used=False, implementation=implementation_hashes(),
        source_sha256={p: sha256(ROOT / p) for p in SOURCES}, created_at=now())
    parent = torch.load(plan['parent']['path'], map_location='cpu', weights_only=False)
    assert sha256(Path(plan['parent']['path'])) == plan['parent']['sha256']
    assert parent['tokens'] == plan['parent']['tokens_seen'] and parent['update'] == 152588
    assert parent['implementation_sha256'] == plan['implementation']
    assert all(abs(g['lr'] - .0002) < 1e-12 for g in parent['optimizer']['param_groups'])
    assert parent['sampler'].get('kind') != 'eos-pilot-mixture-v1'
    assert parent['spec']['batch'] == 32 and parent['spec']['context'] == 1024
    assert sha256(ROOT / plan['tokenizer']) == plan['tokenizer_sha256']
    assert sha256(ROOT / 'eval/base.jsonl') == plan['suite_sha256']
    assert sha256(Path(plan['short_pool']) / 'manifest.json') == plan['short_manifest_sha256']
    run = ROOT / plan['output']
    assert not (run / 'job.json').exists(), 'Do not refreeze a started job'
    schema = dict(type='object', additionalProperties=False, required=list(plan),
                  properties={k: {'const': v} for k,v in plan.items()})
    validate(plan, schema)
    write_json(path, plan)
    write_json(ROOT / 'schemas' / path.relative_to(ROOT).with_suffix('.schema.json'), schema)
    write_json(ROOT / 'reports/phase6/eos_5b_finish_preflight.json', dict(status='passed_frozen5B_finishing_parent',
        parent=plan['parent'], parent_actual_lrs=[g['lr'] for g in parent['optimizer']['param_groups']],
        train_sampler=parent['sampler'], plan_sha256=sha256(path), implementation=plan['implementation'],
        sources=plan['source_sha256'], GPU_training_started=False, checked_at=now()))


def evaluate(checkpoint, dev, tok, auxiliary, path, binding, heartbeat, check, full=False, generation=True):
    digest = sha256(checkpoint)
    if path.exists():
        result = read_json(path)
        assert result['checkpoint_sha256'] == digest and result['binding'] == binding
        return result
    state = torch.load(checkpoint, map_location='cpu', weights_only=False)
    model = JMicroModel(state['model_config']).to('cuda')
    model.load_state_dict(state['model'], strict=True)
    model.eval()
    memory = bound_evaluation_cache(model)
    initial_rng = rng_state()
    count = [0]
    def guard(_model, _args):
        count[0] += 1
        if count[0] % 256 == 0:
            heartbeat(path.stem, forward_calls=count[0])
    hook = model.register_forward_pre_hook(guard)
    def progress(done, total):
        check()
        if done == total or done % 1024 == 0:
            heartbeat(path.stem, completed_tasks=done, total_tasks=total)
    body_path = path.with_name(path.stem + '-body.json')
    with sdpa_kernel([SDPBackend.MATH]):
        if body_path.exists():
            saved = read_json(body_path)
            assert saved['binding'] == binding and saved['checkpoint_sha256'] == digest
            body = saved['body']
        else:
            body = evaluate_batched(model, dev, 'cuda', 'bf16', limit=None if full else 256, batch=16, progress=progress)
            write_json(body_path, dict(binding=binding, checkpoint_sha256=digest, body=body, completed_at=now()))
        result = dict(binding=binding, checkpoint=str(checkpoint), checkpoint_sha256=digest,
                      full=full, body=body, completed_at=now())
        if generation:
            generated = generate_suite(model, tok, 'cuda', 'bf16', limit=80, max_new=64, sampling=True) if full else dict(
                outputs=pilot.greedy80(model, tok, heartbeat, check), max_new_tokens=64,
                suite_sha256=sha256(ROOT / 'eval/base.jsonl'))
            result.update(generation=generated, greedy_rates=pilot.rate([
                r for r in generated['outputs'] if r['decoding'] == 'greedy' and r['suppressed']]))
            if not full:
                result['auxiliary'] = auxiliary_evaluation(model, tok, auxiliary['cases'], heartbeat, check)
                result['auxiliary_sha256'] = binding['auxiliary_sha256']
    assert pilot.equal_state(initial_rng, rng_state()), 'Evaluation must not consume training RNG'
    assert not model.training
    hook.remove()
    result['memory'], result['evaluation_RNG_isolated'] = dict(memory), True
    write_json(path, result)
    check()
    del model, state
    gc.collect()
    torch.cuda.empty_cache()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, default=ROOT / 'configs/phase6/eos_5b_finish_100m.json')
    parser.add_argument('--freeze', action='store_true')
    args = parser.parse_args()
    torch.set_num_threads(2)
    assert sys.version_info[:3] == (3,12,7)
    if args.freeze:
        freeze(args.plan)
        print('Frozen final5B finishing pair, no GPU training', flush=True)
        return
    plan = read_json(args.plan)
    validate(plan, read_json(ROOT / 'schemas' / args.plan.relative_to(ROOT).with_suffix('.schema.json')))
    assert plan['implementation'] == implementation_hashes()
    assert plan['source_sha256'] == {p: sha256(ROOT / p) for p in SOURCES}
    binding = dict(plan_sha256=sha256(args.plan), parent=plan['parent'], peak_lr=plan['peak_lr'],
        short_manifest_sha256=plan['short_manifest_sha256'], auxiliary_sha256=plan['auxiliary_sha256'],
        module_sha256=sha256(ROOT / 'src/jmicro/eos_pilot.py'), runner_sha256=sha256(Path(__file__)),
        implementation=plan['implementation'], new_source=plan['source_sha256'])
    run = ROOT / plan['output']
    run.mkdir(parents=True, exist_ok=True)
    path = run / 'job.json'
    old = read_json(path) if path.exists() else {}
    if old:
        assert not alive(old), 'Actual job is live; do not duplicate'
        assert old['binding'] == binding
        if old['status'] == 'complete':
            print('Final5B finishing already complete; not rerunning', flush=True)
            return
    prior, started, stopped = old.get('gpu_elapsed_seconds',0), [None], [False]
    job = dict(status='running', **identity(), binding=binding, started_at=old.get('started_at',now()),
        stage='setup', gpu_elapsed_seconds=prior, restart_command='bash scripts/run_eos_5b_finish.sh')
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0,True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0,True))
    def check():
        if stopped[0]:
            raise InterruptedError('Stop requested; checkpoint preserved')
        if started[0] is not None and prior + time.monotonic() - started[0] > plan['gpu_budget_seconds']:
            raise TimeoutError('Cumulative3000second GPU budget exhausted; do not reset')
    def heartbeat(stage, **values):
        check()
        job.update(stage=stage, heartbeat_at=now(), **values)
        if started[0] is not None:
            job['gpu_elapsed_seconds'] = prior + time.monotonic() - started[0]
        atomic_json(path,job)
    try:
        seed_all(42)
        torch.use_deterministic_algorithms(True)
        tests = tests_summary(run / 'tests.xml')
        assert sha256(ROOT / plan['tokenizer']) == plan['tokenizer_sha256']
        assert sha256(ROOT / 'eval/base.jsonl') == plan['suite_sha256']
        assert sha256(Path(plan['parent_full_body'])) == plan['baseline_body_sha256']
        assert sha256(Path(plan['parent_generation'])) == plan['baseline_generation_sha256']
        source = ROOT / plan['reused_preparation']
        for name in ('auxiliary-dev.json', 'content-review.json'):
            target = run / name
            if not target.exists():
                shutil.copyfile(source / name, target)
            assert sha256(target) == sha256(source / name)
        assert read_json(run / 'content-review.json')['passed']
        assert sha256(run / 'auxiliary-dev.json') == plan['auxiliary_sha256']
        auxiliary = read_json(run / 'auxiliary-dev.json')
        accepted = read_json(ROOT / 'reports/phase6/corpus_10b_loader_ready.json')
        assert accepted['status'] == 'passed_actual_training_loader'
        assert accepted['shard_manifest_sha256'] == plan['web_manifest_sha256']
        web = TrainView(plan['web_shards'],plan['web_manifest_sha256'])
        short = TrainView(plan['short_pool'],plan['short_manifest_sha256'],check_stream=True)
        dev, tok = Shard(Path(plan['dev_shards']),'dev'), Tokenizer(ROOT / plan['tokenizer'])
        parent_path = Path(plan['parent']['path'])
        assert sha256(parent_path) == plan['parent']['sha256']
        parent = torch.load(parent_path,map_location='cpu',weights_only=False)
        assert parent['update'] == plan['parent']['update'] and parent['tokens'] == plan['parent']['tokens_seen']
        assert all(abs(g['lr']-.0002)<1e-12 for g in parent['optimizer']['param_groups'])
        pilot.PilotTrainer = LowLRPilotTrainer
        with gpu_lock('cuda'):
            started[0] = time.monotonic()
            heartbeat('resume-gate')
            gate = pilot.exact_gate(parent,web,short,binding,run,check)
            aux_path = run / 'parent-auxiliary.json'
            if aux_path.exists():
                parent_aux = read_json(aux_path)
                assert parent_aux['binding'] == binding
            else:
                heartbeat('parent-auxiliary')
                model = JMicroModel(parent['model_config']).to('cuda')
                model.load_state_dict(parent['model'],strict=True)
                model.eval()
                bound_evaluation_cache(model)
                with sdpa_kernel([SDPBackend.MATH]):
                    parent_aux = dict(binding=binding, checkpoint_sha256=plan['parent']['sha256'],
                        auxiliary=auxiliary_evaluation(model,tok,auxiliary['cases'],heartbeat,check))
                write_json(aux_path,parent_aux)
                del model
                gc.collect()
                torch.cuda.empty_cache()
            arms, screens, full = {}, {}, {}
            for arm in ('web','short20'):
                heartbeat(arm+'-training')
                arms[arm] = pilot.train_arm(arm,parent,web,short,plan,binding,run,heartbeat,check)
                # Repair only the inherited descriptive label; the original record remains preserved.
                arms[arm]['initial_state'] = 'Same final5B model/Adam/RNG/Web cursor; explicit equal lowLR finishing fork'
                write_json(run / arm / 'result.json',arms[arm])
                heartbeat(arm+'-screen')
                screens[arm] = evaluate(Path(arms[arm]['checkpoint']),dev,tok,auxiliary,
                    run / (arm+'-evaluation.json'),binding,heartbeat,check)
            mixture = adoption_checks(screens['web'],screens['short20'])
            promising = all(mixture.values())
            web_rates = screens['web']['greedy_rates']
            safe_web = safe_control(web_rates,plan['parent_fixed_repetition'])
            write_json(run / 'screen-decision.json',dict(binding=binding,improvement_checks=mixture,
                improvement_gate_passed=promising,web_full_generation_eligible=safe_web))
            for arm in ('web','short20'):
                eligible = safe_web or promising if arm == 'web' else promising
                if eligible:
                    heartbeat(arm+'-full')
                    full[arm] = evaluate(Path(arms[arm]['checkpoint']),dev,tok,auxiliary,
                        run / (arm+'-full-evaluation.json'),binding,heartbeat,check,full=True,
                        generation=safe_web if arm == 'web' else True)
            full_checks, growth = {}, {}
            if promising:
                fixed = [r for r in full['short20']['generation']['outputs'] if r['decoding']=='greedy' and r['suppressed']]
                full_checks = dict(BPB_within1percent_full_control=full['short20']['body']['bpb']<=full['web']['body']['bpb']*1.01,
                    all80_screen_IDs_match=[r['generated_ids'] for r in fixed]==[r['generated_ids'] for r in screens['short20']['generation']['outputs']],
                    no_new_empty_role_unicode_vs_original2B=all(pilot.rate(full['short20']['generation']['outputs'])[k]==0 for k in ('empty','role_leak','unicode_failure')))
            for arm, measured in full.items():
                if 'generation' in measured:
                    fixed = [r for r in measured['generation']['outputs'] if r['decoding']=='greedy' and r['suppressed']]
                    growth[arm] = dict(full_BPB_no_major_regression=measured['body']['bpb']<=plan['parent_full_BPB']+.001,
                        fixed_repetition_not8_worse=pilot.rate(fixed)['repetition']<plan['parent_fixed_repetition']+8,
                        no_new_empty_role_unicode=all(pilot.rate(measured['generation']['outputs'])[k]==0 for k in ('empty','role_leak','unicode_failure')),
                        all80_screen_IDs_match=[r['generated_ids'] for r in fixed]==[r['generated_ids'] for r in screens[arm]['generation']['outputs']])
            assert sha256(parent_path) == plan['parent']['sha256']
            result = dict(status='completed_5B_finishing_pair_pending_CPU_and_content_review',binding=binding,
                tests=tests,resume_gate=gate,arms=arms,improvement_checks=mixture,improvement_gate_passed=promising,
                full_adoption_checks=full_checks,automatic_full_gate_passed=promising and all(full_checks.values()),
                full_evaluated_arms=list(full),web_full_generation_eligible=safe_web,growth_checks=growth,
                scientific_training_input_tokens=sum(r['additional_input_tokens'] for r in arms.values()),
                verification_training_input_tokens=gate['input_tokens'],quality_targets_achieved=False,test_split_used=False,
                parent_fixed_and_full_reused=True,completed_at=now(),stop_before=['10B','Chat','unlikelihood','decoder_sweeps'])
            write_json(run / 'result.json',result)
            heartbeat('finished')
            job.update(status='complete',completed_at=now(),result=str(run / 'result.json'))
            print(json.dumps(dict(status='complete',mixture=mixture,full_checks=full_checks)),flush=True)
    except BaseException as exc:
        job.update(status='interrupted' if isinstance(exc,(InterruptedError,TimeoutError)) else 'failed',
                   failure=f'{type(exc).__name__}: {exc}',finished_at=now())
        raise
    finally:
        if started[0] is not None:
            job['gpu_elapsed_seconds'] = prior + time.monotonic() - started[0]
        atomic_json(path,job)


if __name__ == '__main__':
    main()
