"""One-shot TRAIN-index metadata audit. No token stream/model/DEV/TEST opens.

Use fixed independent byte draws and bounded neighboring records; no whole
index parse, rehash or dataset build. Frozen historical sources are unchanged.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import random
import statistics
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from jmicro.index_byte_sampling import (
    containing_record, legacy_next_record, legacy_record_weight)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(contract_path, pin):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha(contract_path) != pin:
        raise ValueError('Explicit CPU-only execution and pinned contract required')
    c = json.loads(Path(contract_path).read_text())
    if (c['kind'] != 'fixed_TRAIN_index_byte_boundary_metadata_audit_v1'
            or c['draws'] != 256 or c['seed'] != 20261015
            or c['CPU_wall_ceiling_seconds'] != 30 or c['GPU_seconds'] != 0
            or c['scientific_teachers'] != 0):
        raise ValueError('Fixed diagnostic scope differs')
    for path, source_pin in c['sources'].items():
        if sha(ROOT / path) != source_pin:
            raise ValueError('Frozen audit source differs: ' + path)
    output = ROOT / c['output']
    if not output.resolve().is_relative_to(ROOT / 'reports/phase6') or output.exists():
        raise ValueError('Fresh evidence path required; never overwrite a completed audit')
    reference_path = ROOT / c['accepted_config']['path']
    if sha(reference_path) != c['accepted_config']['sha256']:
        raise ValueError('Accepted source contract differs')
    old = json.loads(reference_path.read_text())
    binding = old['source_binding']
    pool = Path(binding['pool'])
    index = pool / 'train.index.jsonl'
    manifest = pool / 'manifest.json'
    ready = pool / ('.compact-index-' + binding['manifest_sha256'][:16]) / 'ready.json'
    opened = []
    forbidden = []
    allowed = {str(p.resolve()) for p in (index, manifest, ready)}
    sensitive = (Path('/home/aihub_ubuntu/jmicro-data').resolve(), (ROOT / 'eval').resolve())
    def audit(event, args):
        if event != 'open' or not isinstance(args[0], (str, bytes)):
            return
        path = Path(os.fsdecode(args[0])).resolve()
        if any(path.is_relative_to(root) for root in sensitive):
            if str(path) not in allowed:
                forbidden.append(str(path))
                raise ValueError('Forbidden data/eval open: ' + str(path))
            mode = args[1] or ''
            if any(flag in mode for flag in 'wax+'):
                raise ValueError('Read-only source metadata audit required')
            opened.append(str(path))
    sys.addaudithook(audit)
    if sha(manifest) != binding['manifest_sha256'] or sha(ready) != binding['ready_sha256']:
        raise ValueError('Prior accepted manifest/ready identity differs')
    saved = json.loads(ready.read_text())
    stat = index.stat()
    if (not saved['source_hash_verified_during_single_parse']
            or saved['binding']['index_sha256'] != binding['index_sha256']
            or saved['binding']['manifest_sha256'] != binding['manifest_sha256']
            or (stat.st_size, stat.st_mtime_ns) != (binding['index_size'], binding['index_mtime_ns'])
            or (pool / 'train.bin').stat().st_size != binding['stream_size']
            or (pool / 'train.bin').stat().st_mtime_ns != binding['stream_mtime_ns']):
        raise ValueError('Previously verified TRAIN identity differs; no reparse fallback')
    rng = random.Random(c['seed'])
    rows = []
    with index.open('rb') as handle:
        for draw in range(c['draws']):
            if time.monotonic() - started > c['CPU_wall_ceiling_seconds']:
                raise TimeoutError('Fixed CPU budget exceeded')
            position = rng.randrange(stat.st_size)
            own_start, own_raw = containing_record(handle, position, stat.st_size)
            legacy_start, legacy_raw = legacy_next_record(handle, position, stat.st_size)
            current = json.loads(own_raw)
            successor = json.loads(legacy_raw) if legacy_raw else None
            for record in (current, successor):
                if record is not None and (record['split'] != 'train'
                        or record['source'] not in ('web', 'story', 'textbook')):
                    raise ValueError('Accepted TRAIN-only metadata required')
            weight = legacy_record_weight(handle, own_start, stat.st_size)
            rows.append(dict(draw=draw, drawn_byte_position=position,
                containing_index_position=own_start, containing_record_sha256=hashlib.sha256(own_raw).hexdigest(),
                containing_source=current['source'], containing_body_tokens=current['body_tokens'],
                own_record_bytes=len(own_raw), legacy_incoming_bytes=weight,
                legacy_over_containing_weight=weight / len(own_raw),
                legacy_index_position=legacy_start, legacy_record_sha256=hashlib.sha256(legacy_raw).hexdigest(),
                legacy_source=successor['source'] if successor else None,
                legacy_body_tokens=successor['body_tokens'] if successor else None,
                selected_successor=legacy_start != own_start,
                same_source=successor is not None and successor['source'] == current['source']))
        tail_start, tail_raw = containing_record(handle, stat.st_size - 1, stat.st_size)
    groups = {}
    for source in ('web', 'textbook', 'story'):
        selected = [r for r in rows if r['containing_source'] == source]
        ratios = [r['legacy_over_containing_weight'] for r in selected]
        if not ratios:
            groups[source] = dict(draws=0, severity_estimate=None)
            continue
        mean = statistics.mean(ratios)
        groups[source] = dict(draws=len(selected), ratio_mean=mean, ratio_min=min(ratios), ratio_max=max(ratios),
            ratio_CV=statistics.pstdev(ratios) / mean,
            approximate_conditional_total_variation=statistics.mean(abs(r / mean - 1) for r in ratios) / 2,
            interpretation='Finite index-byte sample estimate, not exact corpus-wide probability or a quality gate')
    result = dict(status='bounded_metadata_mapping_audit_completed', created_at=datetime.now(timezone.utc).isoformat(),
        contract_sha256=pin, sources=c['sources'], accepted_source_binding=binding,
        draws=len(rows), unique_containing_records=len({r['containing_record_sha256'] for r in rows}),
        successor_selections=sum(r['selected_successor'] for r in rows),
        cross_source_successors=sum(not r['same_source'] for r in rows),
        containing_source_counts=dict(Counter(r['containing_source'] for r in rows)),
        per_source=groups, rows=rows,
        exact_mapping='byte0 selects first; record2 weight first-line-bytes-minus1; records3+ weight preceding-line-bytes; final-line positions reject at EOF; then requested-genre rejection renormalizes',
        terminal_rejection=dict(last_record_start=tail_start, last_record_bytes=len(tail_raw),
                                unconditional_probability=len(tail_raw) / stat.st_size),
        metadata_read_paths=sorted(set(opened)), forbidden_read_attempts=forbidden,
        CPU_wall_seconds=time.monotonic() - started, new_GPU_seconds=0, new_optimizer_updates=0,
        scientific_teacher_positions=0, token_stream_opened=False, DEV_opened=False, TEST_opened=False,
        model_instantiated=False, dataset_prepared=False, historical_sources_changed=False,
        Base_qualified=False, independent_learning_completed=False, fullDEV_completed=False,
        sealedTEST_completed=False, Base_adopted=False,
        limitations=['This demonstrates a metadata selection-policy mismatch, not the cause of generation failures.',
                    '256 byte-uniform positions are not uniform documents or an independent corpus quality audit.',
                    'Finite conditional variation estimates do not establish a useful training intervention.',
                    'All historical matched comparisons used their actual same selector; their pairing remains valid.'])
    if result['CPU_wall_seconds'] > c['CPU_wall_ceiling_seconds']:
        raise TimeoutError('CPU ceiling exceeded; no successful receipt')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in (
        'status', 'draws', 'successor_selections', 'cross_source_successors',
        'per_source', 'CPU_wall_seconds', 'new_GPU_seconds')}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract', type=Path, required=True)
    parser.add_argument('--contract-sha256', required=True)
    args = parser.parse_args()
    run(args.contract, args.contract_sha256)
