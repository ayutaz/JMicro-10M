"""Single bounded CPU feasibility for a new TRAIN sentence-decay objective.

No model, learning, GPU, DEV/TEST, corpus scan, or saved synthetic dataset.
Only changed sentence/byte-boundary eligibility is audited, using the same
existing 32x48 original TRAIN draws and material state without perturbation.
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
from jmicro.pseudo_repetition import repeat_rows
from jmicro.tokenizer import Tokenizer
from natural_context_contrast_corpus import OriginalTrainCorpusSampler


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def run(contract, pin):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha(contract) != pin:
        raise ValueError('Externally pinned CPU-only contract required')
    c = json.loads(Path(contract).read_text())
    if (c['kind'] != 'native_TRAIN_sentence_decay_CPU_feasibility_v1'
            or c['batch'] != 48 or c['batches'] != 32 or c['seed'] != 42
            or c['CPU_wall_ceiling_seconds'] != 30 or c['minimum_rows'] != 64
            or c['minimum_active_batches'] != 16 or c['GPU_seconds'] != 0
            or c['scientific_teachers'] != 0 or c['model_instantiated'] is not False):
        raise ValueError('Fixed changed-objective CPU preparation scope differs')
    for relative, source_pin in c['sources'].items():
        if sha(ROOT / relative) != source_pin:
            raise ValueError('Frozen preparation source differs: ' + relative)
    proposal = ROOT / c['proposal']['path']
    if sha(proposal) != c['proposal']['sha256']:
        raise ValueError('Prospective sentence-decay proposal differs')
    output = ROOT / c['output']
    if output.exists() or not output.resolve().is_relative_to(ROOT / 'reports/phase6'):
        raise ValueError('Fresh receipt required; never repeat completed audit')
    accepted = ROOT / c['accepted_config']['path']
    if sha(accepted) != c['accepted_config']['sha256']:
        raise ValueError('Accepted original TRAIN recipe changed')
    old = json.loads(accepted.read_text())
    if old['batch'] != 48 or old['seed'] != 42 or sum(old['goals'].values()) != 100000000:
        raise ValueError('Original paired CE source protocol required')
    pool, token_path = Path(old['source_binding']['pool']), ROOT / old['tokenizer']
    ready = pool / ('.compact-index-' + old['source_binding']['manifest_sha256'][:16]) / 'ready.json'
    allowed = {str(p.resolve()) for p in (pool/'manifest.json', ready, pool/'train.bin',
                                         pool/'train.index.jsonl', token_path)}
    roots = (Path('/home/aihub_ubuntu/jmicro-data'), ROOT/'eval', ROOT/'artifacts')
    reads = []

    def audit(event, args):
        if event != 'open' or not isinstance(args[0], (str, bytes)):
            return
        p = Path(os.fsdecode(args[0])).resolve()
        if any(p.is_relative_to(root) for root in roots):
            if str(p) not in allowed or any(flag in (args[1] or '') for flag in 'wax+'):
                raise ValueError('Forbidden data/DEV/TEST open: ' + str(p))
            reads.append(str(p))

    sys.addaudithook(audit)
    if sha(token_path) != old['tokenizer_sha256']:
        raise ValueError('Original native Tokenizer differs')
    codec = Tokenizer(token_path)
    sampler = OriginalTrainCorpusSampler(pool, old['source_binding']['manifest_sha256'], codec, old['goals'], seed=42)
    if sampler.binding != old['source_binding']:
        raise ValueError('Prior accepted TRAIN identity differs; no rescan')
    batches = []
    try:
        for batch in range(c['batches']):
            if time.monotonic() - started > c['CPU_wall_ceiling_seconds']:
                raise TimeoutError('Frozen CPU feasibility budget exceeded')
            rows = sampler.take(c['batch'])
            before_rows, before_sampler = fingerprint(rows), fingerprint(sampler.state_dict())
            selected = repeat_rows(rows, codec)
            if fingerprint(rows) != before_rows or fingerprint(sampler.state_dict()) != before_sampler:
                raise ValueError('Pseudo inputs altered original CE or material state')
            for item in selected:
                if (not 4 <= item['copies'] <= 16 or len(item['input_ids']) > 512
                        or any(item['target_ids'][i] != item['target_ids'][j]
                               for i, j in zip(item['current_positions'], item['previous_positions']))
                        or any(i < 8 for i in item['target_ids'])):
                    raise ValueError('Whole-copy plain-body shift and pair identities differ')
            # No token/text pseudo dataset is written; only identities and counts.
            traces = [{key: item[key] for key in ('source', 'source_family',
                'original_body_sha256', 'sentence_sha256', 'prefix_tokens', 'sentence_tokens',
                'copies', 'pseudo_target_comparisons')} for item in selected]
            batches.append(dict(batch=batch, original_windows=len(rows),
                original_CPU_label_positions=sum(r['teacher_tokens'] for r in rows),
                selected_rows=len(selected), sources=dict(Counter(r['source'] for r in selected)),
                pseudo_target_comparisons=sum(r['pseudo_target_comparisons'] for r in selected),
                pseudo_physical_input_positions=sum(len(r['input_ids']) for r in selected),
                maximum_pseudo_input_positions=max((len(r['input_ids']) for r in selected), default=0),
                original_rows_and_material_state_unchanged=True, trace=traces))
    finally:
        sampler.handle.close()
    row_count = sum(b['selected_rows'] for b in batches)
    active = sum(b['selected_rows'] > 0 for b in batches)
    screen = dict(at_least64_rows=row_count >= c['minimum_rows'],
        at_least16_active_batches=active >= c['minimum_active_batches'],
        original_CE_rows_and_material_state_preserved=True,
        all_pseudo_rows_at_most512=all(b['maximum_pseudo_input_positions'] <= 512 for b in batches))
    elapsed = time.monotonic() - started
    if elapsed > c['CPU_wall_ceiling_seconds']:
        raise TimeoutError('Frozen CPU feasibility budget exceeded')
    result = dict(status='changed_TRAIN_sentence_decay_CPU_feasibility_completed',
        observed_at=datetime.now(timezone.utc).isoformat(), contract_sha256=pin,
        sources=c['sources'], proposal=c['proposal'], source_binding=sampler.binding,
        batches=batches, selected_rows=row_count, active_batches=active,
        pseudo_target_comparisons=sum(b['pseudo_target_comparisons'] for b in batches),
        screen=screen, eligible_for_native_trainer_implementation=all(screen.values()),
        CPU_wall_seconds=elapsed, data_and_Tokenizer_read_paths=sorted(set(reads)),
        model_instantiated=False, optimizer_updates=0, new_GPU_seconds=0,
        new_scientific_teachers=0, new_dataset_prepared=False, DEV_opened=False, TEST_opened=False,
        scientific_contract_frozen=False, Base_qualified=False, Base_adopted=False,
        full_four_item_goal_complete=False,
        limitations='Only32 fixed batches and synthetic token alignment. No learned self-reinforcement diagnosis, quality evidence, trained independent seed, fullDEV, sealedTEST, or scientific learning. Python open monitoring is not an OS sandbox or a blanket native-library guarantee.')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in ('status', 'selected_rows', 'active_batches',
        'pseudo_target_comparisons', 'eligible_for_native_trainer_implementation', 'CPU_wall_seconds')}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract', type=Path, required=True)
    parser.add_argument('--contract-sha256', required=True)
    args = parser.parse_args()
    run(args.contract, args.contract_sha256)
