"""Small local report index, excluding corpora/raw outputs/weights and giant files."""
import argparse
import json
from pathlib import Path
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src')]
from jmicro.experiment import ROOT, now, sha256, read_json
from jmicro.training import atomic_json

PHASE = ROOT/'reports/phase6'
OUTPUT = PHASE/'base_experiment_index_20261008.json'
SUFFIXES = ('_proposal.json', '_completion.json', '_review.json', '_active_job.json')
COUNTS = ('scientific_teacher_tokens', 'scientific_gold_total', 'scientific_original_gold_total',
          'prepared_tokens', 'stable_teacher_tokens', 'GPU_seconds', 'GPU_cap_seconds',
          'GPU_budget_seconds', 'CPU_seconds', 'Base_complete', 'Base_adopted',
          'source_accepted', 'exploratory_advance_eligible', 'eligible_for_final_Base_validation')


def compact_summary(value):
    if not isinstance(value, dict):
        return None
    wanted = ('BPB','grammar2','coherence2','coherent','appropriate','appropriate_end',
              'documents','weak_documents','weak','usable','passed','content_acceptance_passed')
    result = {key:value[key] for key in wanted if key in value}
    if isinstance(value.get('rates'), dict):
        result['rates'] = value['rates']
    return result or None


def build():
    if OUTPUT.exists():
        raise ValueError('Preserve observed index; use a dated successor for future outcomes')
    started = time.monotonic()
    records, skipped = [], []
    for path in sorted(PHASE.iterdir()):
        if time.monotonic()-started > 10:
            raise TimeoutError('Fixed10-second metadata index cap exhausted')
        if not path.name.endswith(SUFFIXES) or not path.is_file():
            continue
        size = path.stat().st_size
        if size > 1048576:
            skipped.append(dict(path=str(path.relative_to(ROOT)), bytes=size,
                                reason='Over1MiB; do not open full content/raw reports for this index'))
            continue
        value = read_json(path)
        if not isinstance(value, dict):
            skipped.append(dict(path=str(path.relative_to(ROOT)), reason='Not a metadata object'))
            continue
        summary = compact_summary(value.get('summary'))
        arms = {name:result for name, item in value.get('summaries', {}).items()
                if (result := compact_summary(item)) is not None} if isinstance(value.get('summaries'),dict) else {}
        records.append(dict(path=str(path.relative_to(ROOT)), sha256=sha256(path), bytes=size,
            status=value.get('status','not_recorded'), created_at=value.get('created_at',value.get('observed_at')),
            next_action=value.get('next_action'), summary=summary, summaries=arms or None,
            recorded_flags={key:item for key,item in value.items()
                if ('closed' in key or 'passed' in key or key in COUNTS)
                and isinstance(item,(bool,int,float,str,type(None)))},
            runtime_record_requires_live_process_revalidation=path.name.endswith('_active_job.json')))
    elapsed = time.monotonic()-started
    if elapsed > 10:
        raise TimeoutError('Fixed10-second metadata index cap exhausted')
    atomic_json(OUTPUT,dict(status='bounded_local_report_index_observed_not_a_new_experiment',created_at=now(),
        source_script=dict(path=str(Path(__file__).relative_to(ROOT)),sha256=sha256(Path(__file__))),
        records=records,skipped=skipped,CPU_seconds=elapsed,CPU_cap_seconds=10,GPU_seconds=0,
        scientific_teacher_tokens=0,new_ratings=0,
        limits='Dated lookup aid only. Source status strings/flags are retained without inferring global completion, causality or adoption. Confirm referenced source hashes/current reports and actual PID/boot/start before acting; especially active-job snapshots can be stale. Raw content over1MiB is skipped, not silently accepted. Original notes and quality gates unchanged.'))
    print(json.dumps(dict(records=len(records),skipped=len(skipped),CPU_seconds=elapsed,output=str(OUTPUT))))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--build',action='store_true')
    group.add_argument('--query',help='Case-insensitive substring in source filename/status/next action')
    args = parser.parse_args()
    if args.build:
        build()
    else:
        index=read_json(OUTPUT)
        needle=args.query.casefold()
        selected=[row for row in index['records'] if needle in
                  ' '.join(str(row[k]) for k in ('path','status','next_action')).casefold()]
        print(json.dumps(dict(observed_at=index['created_at'],records=selected,
                             skipped_files_not_covered=len(index['skipped'])),ensure_ascii=False,indent=2))
