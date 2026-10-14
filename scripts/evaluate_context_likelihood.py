"""Actual checkpoint-bound DEV-only Base and fixed Japanese diagnostics."""
from pathlib import Path

from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.evaluation_boundary import load_dev_suite
from jmicro.evaluation_memory import bound_evaluation_cache
from jmicro.isolated_japanese_scoring import evaluate_isolated_japanese
from jmicro.shards import Shard
from jmicro.readiness import evaluate_batched
from jmicro.training import atomic_json, rng_state, restore_rng
from jmicro.experiment import sha256
from jmicro.phase5 import equal_state
from base_fim_pilot_protocol import EvaluationReadGuard, validate_body, validate_raw, rates
from isolated_base_evaluation import generate_isolated_dev


def evaluate(trainer, contract, record, output, heartbeat, check):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    suite_path = Path(contract['DEV_manifest']['path'])
    data = Path(contract['DEV_shards']['path'])
    japanese = Path(contract['Japanese_manifest']['path'])
    unigram = Path(contract['unigram']['path'])
    allowed = [suite_path, suite_path.parent / 'base.dev.jsonl', data / 'manifest.json',
               data / 'dev.index.json', data / 'dev.bin', data / 'token_bytes.json',
               japanese, *(japanese.parent / (task + '.dev.jsonl') for task in ('semantics', 'jblimp', 'jcqa')), unigram]
    guard = EvaluationReadGuard([suite_path.parent.parent, data.parent.parent.parent, unigram.parent], allowed)
    model = trainer.model
    mode, before = model.training, rng_state()
    try:
        with guard, sdpa_kernel(SDPBackend.MATH):
            suite = load_dev_suite(suite_path, contract['DEV_manifest']['sha256'])
            if sha256(data / 'manifest.json') != contract['DEV_shards']['manifest_sha256']:
                raise ValueError('Pinned DEV shards differ')
            dev = Shard(data, 'dev')
            if any(row['split'] != 'dev' for row in dev.index[:256]):
                raise ValueError('Foreign split in DEV-only index')
            model.eval()
            # Existing bounded eager inference cache, preserving native logits.
            bound_evaluation_cache(model)
            check()
            body = evaluate_batched(model, dev, 'cuda', 'bf16', limit=256, batch=16,
                progress=lambda done, total: (check(), heartbeat('DEV256', completed=done, total=total)))
            validate_body(body)
            generation = generate_isolated_dev(model, trainer.sampler.tokenizer, suite_path,
                contract['DEV_manifest']['sha256'], heartbeat, check)
            generation.update(binding=record['binding'], checkpoint_sha256=record['checkpoint_sha256'])
            validate_raw(generation['outputs'], trainer.sampler.tokenizer, suite)
            atomic_json(output / 'generation.json', generation)
            japanese_result = evaluate_isolated_japanese(model, trainer.sampler.tokenizer, japanese,
                contract['Japanese_manifest']['sha256'], unigram, contract['unigram']['sha256'], check,
                lambda task, done, total: heartbeat(task, completed=done, total=total), device='cuda')
            diagnostics = {}
            for task, scored in japanese_result['tasks'].items():
                atomic_json(output / (task + '.json'), dict(binding=record['binding'],
                    checkpoint_sha256=record['checkpoint_sha256'], **scored))
                diagnostics[task] = dict(complete=scored['complete'], expected=scored['expected'], **scored['summary'])
            atomic_json(output / 'Japanese_provenance.json', {k: v for k, v in japanese_result.items() if k != 'tasks'})
        if not equal_state(before, rng_state()):
            raise ValueError('Actual training RNG changed during isolated evaluation')
        result = dict(status='complete', checkpoint_sha256=record['checkpoint_sha256'], binding=record['binding'],
            body=body, generation=generation, greedy_rates=rates(generation['outputs']), diagnostics=diagnostics,
            semantic_both_contexts=japanese_result['semantic_both_contexts'],
            evaluation_RNG_isolated=True, evaluation_read_paths=guard.paths,
            TEST_opened=False, legacy_mixed_suite_opened=False, Base_adopted=False)
        atomic_json(output / 'result.json', result)
        return result
    finally:
        model.train(mode)
        restore_rng(before)
