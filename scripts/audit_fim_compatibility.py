"""One bounded CPU feasibility audit on accepted TRAIN, not a FIM trainer.

No model, GPU, DEV, TEST, newly prepared dataset or quality evaluation. Reports
all fixed draws, including over-context failures; never filters to short units.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from jmicro.fim_compatibility import MARKERS, restore_original, serialize_psm, utf8_token_boundaries


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(contract_path, contract_sha256):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '':
        raise ValueError('CPU-only audit requires explicit empty CUDA_VISIBLE_DEVICES')
    if sha(contract_path) != contract_sha256:
        raise ValueError('Pinned feasibility contract differs')
    c = json.loads(Path(contract_path).read_text())
    if (c['kind'] != 'FIM_CPU_serialization_feasibility_only_v1'
            or c['documents_per_source'] != 8 or c['sources'] != ['web', 'textbook', 'story']
            or c['seed'] != 42 or c['context'] != 1024 or c['CPU_wall_ceiling_seconds'] != 30
            or c['markers'] != list(MARKERS) or c['scientific_teacher_budget'] != 0
            or c['GPU_budget_seconds'] != 0):
        raise ValueError('Fixed one-pass CPU-only scope differs')
    for path, pin in c['source_sha256'].items():
        if sha(ROOT / path) != pin:
            raise ValueError('Frozen audit source differs: ' + path)
    parent_config = ROOT / c['accepted_source_config']['path']
    if sha(parent_config) != c['accepted_source_config']['sha256']:
        raise ValueError('Accepted source provenance differs')
    old = json.loads(parent_config.read_text())
    token_path = ROOT / old['tokenizer']
    if sha(token_path) != old['tokenizer_sha256']:
        raise ValueError('Original Tokenizer differs')
    # Import Torch-dependent existing corpus code only after scope/source checks.
    from jmicro.tokenizer import Tokenizer
    from base_kv_allocation_trainer import CEOnlyOriginalSampler
    codec = Tokenizer(token_path)
    sampler = CEOnlyOriginalSampler(old['source_binding']['pool'],
        old['source_binding']['manifest_sha256'], codec, old['goals'], seed=c['seed'])
    if sampler.binding != old['source_binding']:
        raise ValueError('Previously verified TRAIN identity differs; no scan fallback')
    rows = []
    try:
        for genre in c['sources']:
            for draw in range(c['documents_per_source']):
                if time.monotonic() - started >= c['CPU_wall_ceiling_seconds']:
                    raise TimeoutError('Fixed CPU feasibility ceiling exhausted; do not reroll')
                sampler._draw_document(genre)
                windows = sampler.pending[genre]
                original = [token for window in windows for token in window['target_ids'] if token >= 0]
                if original[-1] != 3 or original.count(3) != 1:
                    raise ValueError('Whole original document/EOS reconstruction differs')
                body = original[:-1]
                metadata = windows[0]
                if (len(body) != metadata['original_body_tokens']
                        or hashlib.sha256(codec.decode_bytes(body)).hexdigest()
                        != metadata['full_original_body_sha256']):
                    raise ValueError('Accepted original document identity differs')
                bounds = utf8_token_boundaries(body, codec)
                left = min(bounds[:-1], key=lambda n: (abs(3*n - len(body)), n))
                right = min((n for n in bounds if n > left), key=lambda n: (abs(3*n - 2*len(body)), n))
                record = dict(source=genre, draw=draw,
                    original_body_sha256=metadata['full_original_body_sha256'],
                    index_record_sha256=metadata['index_record_sha256'],
                    original_body_tokens=len(body), original_body_UTF8_bytes=metadata['original_body_UTF8_bytes'],
                    cuts=[left, right], marker_tokens=sum(len(codec.encode(m)) for m in MARKERS),
                    original_teacher_positions=len(original))
                # Verify conservation even when it cannot fit the real context.
                serialized = serialize_psm(body, codec, (left, right), context=len(body) + 128)
                if restore_original(serialized) != original:
                    raise ValueError('Original token identities lost or duplicated')
                record.update(original_token_and_byte_conservation=True,
                    FIM_input_positions=len(serialized.ids)-1,
                    fits_context1024=len(serialized.ids)-1 <= c['context'])
                rows.append(record)
    finally:
        sampler.handle.close()
    elapsed = time.monotonic() - started
    if elapsed > c['CPU_wall_ceiling_seconds']:
        raise TimeoutError('Fixed CPU ceiling exhausted; no successful receipt')
    marker_tokens = sum(len(codec.encode(m)) for m in MARKERS)
    result = dict(status='fixed24_TRAIN_FIM_CPU_feasibility_completed_not_scientific_recipe_selected',
        contract_sha256=contract_sha256, source_sha256=c['source_sha256'],
        accepted_source_binding=sampler.binding, tokenizer_sha256=old['tokenizer_sha256'],
        CPU_wall_seconds=elapsed, fixed_draws=len(rows), unique_original_documents=len({r['original_body_sha256'] for r in rows}),
        rows=rows, marker_ids={m:codec.encode(m) for m in MARKERS}, marker_tokens=marker_tokens,
        marker_overhead_ratio=marker_tokens*len(rows)/sum(r['original_teacher_positions'] for r in rows),
        fits_context1024=sum(r['fits_context1024'] for r in rows),
        original_token_and_byte_conservation=all(r['original_token_and_byte_conservation'] for r in rows),
        new_scientific_teacher_positions=0, new_optimizer_updates=0, new_GPU_seconds=0,
        new_dataset_prepared=False, DEV_opened=False, TEST_opened=False,
        real_model_instantiated=False, quality_improvement_evidence=False, Base_adopted=False,
        limitations=['Only 8 fixed TRAIN draws per source; not a corpus-wide audit or representative quality estimate.',
            'Literal body markers differ from the paper structural sentinels. No vocabulary expansion or role-ID reuse.',
            'Marker supervision/masking, FIM mixture and training horizon remain unfrozen.',
            'EOS marks reconstructed-middle completion in FIM, so unchanged EOS counts do not imply unchanged semantics.',
            'Serialization feasibility is not ordinary continuation improvement; fresh-learning value remains unproven.'])
    output = ROOT / c['output']
    if not output.resolve().is_relative_to(ROOT / 'reports/phase6') or output.exists():
        raise ValueError('A new phase6 receipt path is required; never overwrite old evidence')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status', 'fixed_draws', 'marker_tokens', 'marker_overhead_ratio',
        'fits_context1024', 'CPU_wall_seconds', 'new_scientific_teacher_positions', 'new_GPU_seconds')}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract', type=Path, required=True)
    parser.add_argument('--contract-sha256', required=True)
    args = parser.parse_args()
    run(args.contract, args.contract_sha256)
