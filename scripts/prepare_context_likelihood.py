"""One bounded CPU audit of prospective natural likelihood pairs.

No model/optimizer/GPU/DEV/TEST or new dataset. Actual native TRAIN48x32
draws only, no whole-corpus scan. Context commits simulate ownership semantics
for feasibility and are not completed optimizer updates or quality evidence.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'src'), str(ROOT / 'scripts')]
from jmicro.context_likelihood import CAPACITY, ContextFIFO, original_anchors
from jmicro.tokenizer import Tokenizer
from natural_context_contrast_corpus import OriginalTrainCorpusSampler


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def run(contract, pin):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha(contract) != pin:
        raise ValueError('Pinned CPU-only feasibility contract required')
    c = json.loads(Path(contract).read_text())
    if (c['kind'] != 'native_TRAIN_equal_length_context_FIFO_CPU_feasibility_v1'
            or c['batch'] != 48 or c['batches'] != 32 or c['seed'] != 42
            or c['FIFO_capacity'] != CAPACITY or c['CPU_wall_ceiling_seconds'] != 30
            or c['minimum_pairs'] != 64 or c['minimum_active_batches'] != 16
            or c['GPU_seconds'] != 0 or c['scientific_teachers'] != 0):
        raise ValueError('Fixed prospective preparation scope differs')
    for relative, source_pin in c['sources'].items():
        if sha(ROOT / relative) != source_pin:
            raise ValueError('Frozen CPU preparation source differs: ' + relative)
    output = ROOT / c['output']
    if output.exists() or not output.resolve().is_relative_to(ROOT / 'reports/phase6'):
        raise ValueError('Fresh preparation receipt required; do not repeat completed audit')
    config_path = ROOT / c['accepted_config']['path']
    if sha(config_path) != c['accepted_config']['sha256']:
        raise ValueError('Accepted matched source/optimizer configuration differs')
    old = json.loads(config_path.read_text())
    if old['batch'] != 48 or old['seed'] != 42 or sum(old['goals'].values()) != 100000000:
        raise ValueError('Existing matched CE protocol required')
    pool = Path(old['source_binding']['pool'])
    token_path = ROOT / old['tokenizer']
    ready = pool / ('.compact-index-' + old['source_binding']['manifest_sha256'][:16]) / 'ready.json'
    allowed = {str(p.resolve()) for p in (pool / 'manifest.json', ready, pool / 'train.bin',
                                         pool / 'train.index.jsonl', token_path)}
    roots = (Path('/home/aihub_ubuntu/jmicro-data'), ROOT / 'eval', ROOT / 'artifacts')
    reads = []
    def audit(event, args):
        if event != 'open' or not isinstance(args[0], (str, bytes)):
            return
        p = Path(os.fsdecode(args[0])).resolve()
        if any(p.is_relative_to(root) for root in roots):
            if str(p) not in allowed:
                raise ValueError('Forbidden preparation data/DEV/TEST open: ' + str(p))
            if any(flag in (args[1] or '') for flag in 'wax+'):
                raise ValueError('Existing TRAIN/Tokenizer must remain read-only')
            reads.append(str(p))
    sys.addaudithook(audit)
    if sha(token_path) != old['tokenizer_sha256']:
        raise ValueError('Original Tokenizer differs')
    codec = Tokenizer(token_path)
    sampler = OriginalTrainCorpusSampler(pool, old['source_binding']['manifest_sha256'], codec, old['goals'], seed=42)
    if sampler.binding != old['source_binding']:
        raise ValueError('Previously verified original TRAIN identity differs')
    memory = ContextFIFO(dict(source_binding=sampler.binding, tokenizer_sha256=old['tokenizer_sha256'],
                              role='CPU_feasibility_simulation_not_learning'))
    batches = []
    try:
        for batch in range(c['batches']):
            if time.monotonic() - started > c['CPU_wall_ceiling_seconds']:
                raise TimeoutError('Fixed CPU feasibility budget exhausted')
            rows = sampler.take(c['batch'])
            original_rows, original_sampler = fingerprint(rows), fingerprint(sampler.state_dict())
            anchors = original_anchors(rows, codec)
            pairs = memory.select(anchors)
            for pair in pairs:
                positive, negative = pair['positive'], pair['negative']
                if (positive['target_ids'] != negative['target_ids']
                        or len(positive['input_ids']) != len(negative['input_ids'])
                        or len(positive['input_ids']) > 512
                        or sum(i != -100 for i in positive['target_ids']) != pair['suffix_tokens']
                        or 3 in positive['target_ids']):
                    raise ValueError('Identical original suffix/positions and no auxiliary EOS required')
            memory.commit(anchors)
            if fingerprint(rows) != original_rows or fingerprint(sampler.state_dict()) != original_sampler:
                raise ValueError('Auxiliary preparation altered original CE rows/material sampler')
            trace = [{key: pair[key] for key in (
                'source', 'source_family', 'positive_body_sha256', 'negative_body_sha256',
                'positive_prefix_sha256', 'negative_prefix_sha256', 'suffix_sha256', 'prefix_tokens', 'suffix_tokens')}
                for pair in pairs]
            batches.append(dict(batch=batch, original_windows=len(rows), original_teacher_positions=sum(r['teacher_tokens'] for r in rows),
                eligible_anchors=len(anchors), pairs=len(pairs), sources=dict(Counter(p['source'] for p in pairs)),
                repeated_auxiliary_likelihood_targets=2 * sum(p['suffix_tokens'] for p in pairs),
                valid_auxiliary_inputs=sum(len(p[side]['input_ids']) for p in pairs for side in ('positive', 'negative')),
                original_rows_and_sampler_unchanged=True, memory_entries=len(memory.entries), pair_trace=trace))
    finally:
        sampler.handle.close()
    pair_count = sum(row['pairs'] for row in batches)
    active_batches = sum(row['pairs'] > 0 for row in batches)
    screen = dict(at_least64_pairs=pair_count >= c['minimum_pairs'],
                  at_least16_active_batches=active_batches >= c['minimum_active_batches'],
                  all_original_rows_and_material_state_unchanged=all(b['original_rows_and_sampler_unchanged'] for b in batches))
    result = dict(status='fixed_native_TRAIN_context_likelihood_CPU_feasibility_completed',
        created_at=datetime.now(timezone.utc).isoformat(), contract_sha256=pin, sources=c['sources'],
        source_binding=sampler.binding, batches=batches, pair_count=pair_count, active_batches=active_batches,
        screen=screen, eligible_for_owned_CUDA_implementation_probe=all(screen.values()),
        final_FIFO_sha256=fingerprint(memory.state_dict()), original_cpu_label_positions=sum(b['original_teacher_positions'] for b in batches),
        repeated_auxiliary_likelihood_positions=sum(b['repeated_auxiliary_likelihood_targets'] for b in batches),
        metadata_and_TRAIN_read_paths=sorted(set(reads)), CPU_wall_seconds=time.monotonic() - started,
        new_GPU_seconds=0, new_scientific_teachers=0, optimizer_updates=0, model_instantiated=False,
        DEV_opened=False, TEST_opened=False, new_dataset_prepared=False, training_recipe_frozen=False,
        Base_qualified=False, independent_learning_completed=False, fullDEV_completed=False, Base_adopted=False,
        limitations=['Only32 native TRAIN source batches, not corpus-wide coverage or model quality evidence.',
                    'CPU context commits are simulation, not successful Adam updates or learned checkpoints.',
                    'Other observed contexts are document-matching distractors, not certified false facts.',
                    'A positive preparation screen only permits implementing an owned CUDA technical probe, not scientific learning.'])
    if result['CPU_wall_seconds'] > c['CPU_wall_ceiling_seconds']:
        raise TimeoutError('CPU budget exceeded')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in ('status', 'pair_count', 'active_batches',
        'eligible_for_owned_CUDA_implementation_probe', 'CPU_wall_seconds', 'new_GPU_seconds')}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract', type=Path, required=True)
    parser.add_argument('--contract-sha256', required=True)
    args = parser.parse_args()
    run(args.contract, args.contract_sha256)
