"""Audit common targets and archive the completed read-only context diagnostic."""
import hashlib
import json
import math
from pathlib import Path
import re
import sys
import tarfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import alive
import run_broad_context_diagnostic as study

NOTES = ROOT / 'reports/phase6/broad_context_diagnostic_content_notes.json'


def audit_rows(rows, cases, tok, c):
    study.summarize(rows, cases, c['marker'])  # exact complete, unique coverage
    by_id = {case['id']: case for case in cases}
    for row in rows:
        case = by_id[row['id']]
        expected_prefix = case['prefix_ids']
        if row['context'] == 'packed':
            expected_prefix = case['previous_context_ids'] + expected_prefix
        scored = row['scored']; gold = case['gold_ids']
        if (row['prefix_ids'] != expected_prefix or scored['target_ids'] != gold
                or len(scored['target_nll']) != len(gold) or len(scored['target_rank']) != len(gold)
                or any(type(r) is not int or not 1 <= r <= 4096 for r in scored['target_rank'])
                or any(type(v) not in (int, float) or not math.isfinite(v) or v < 0 for v in scored['target_nll'])
                or scored['body_tokens'] != len(gold) - 1
                or not math.isclose(scored['body_nll_sum'], sum(scored['target_nll'][:-1]), rel_tol=1e-6, abs_tol=1e-5)
                or not math.isclose(scored['body_nll_mean'], scored['body_nll_sum'] / (len(gold) - 1), rel_tol=1e-6, abs_tol=1e-5)
                or scored['EOS_nll'] != scored['target_nll'][-1]
                or scored['EOS_rank'] != scored['target_rank'][-1]
                or scored['EOS_top1'] != (scored['EOS_rank'] == 1)):
            raise ValueError('Common target scores or prefix alignment differ')
        if (row['checkpoint_sha256'] != c['checkpoints'][row['checkpoint']]['sha256']
                or row['case_sha256'] != hashlib.sha256(json.dumps(case, sort_keys=True).encode()).hexdigest()
                or row['source'] != case['source']):
            raise ValueError('Checkpoint/train case binding differs')
        ids = row['generated_ids']
        if (not ids or len(ids) > 64 or any(type(i) is not int or not 0 <= i < 4096 for i in ids)
                or any(i in c['generation_suppression_ids'] for i in ids) or 3 in ids[:-1]
                or row['EOS'] != (ids[-1] == 3)
                or row['stop_reason'] != ('stop_id' if ids[-1] == 3 else 'max_new_tokens')
                or (ids[-1] != 3 and len(ids) != 64)):
            raise ValueError('Raw greedy stopping or suppression differs')
        raw = tok.decode_bytes(ids)
        try:
            text = raw.decode(); valid = True
        except UnicodeDecodeError:
            text = raw.decode(errors='replace'); valid = False
        if (row['generated_bytes_hex'] != raw.hex() or row['text'] != text or row['valid_utf8'] != valid
                or row['empty'] != (not text.strip())
                or row['role_leak'] != any(i in (4, 5, 6, 7) for i in ids)
                or row['repetition'] != bool(re.search(r'(.{2,}?)\1\1', text, flags=re.DOTALL))):
            raise ValueError('Raw decoded output or failure flags differ')


def length_subgroups(rows, cases):
    """Gold endpoint is often beyond generation64; do not call every cutoff a failure."""
    short = {case['id'] for case in cases if len(case['gold_ids']) <= 64}
    out = dict(gold_suffix_including_EOS_at_most64=len(short), total_cases=len(cases), groups={})
    for arm in ('oneB', 'twoB'):
        out['groups'][arm] = {}
        for context in ('packed', 'standalone'):
            out['groups'][arm][context] = {}
            for label, eligible in [('gold_endpoint_within64', short),
                                    ('gold_endpoint_beyond64', {case['id'] for case in cases} - short)]:
                selected = [r for r in rows if r['checkpoint'] == arm and r['context'] == context and r['id'] in eligible]
                out['groups'][arm][context][label] = dict(cases=len(selected),
                    greedy_EOS=sum(r['EOS'] for r in selected),
                    gold_EOS_top1=sum(r['scored']['EOS_top1'] for r in selected),
                    empty=sum(r['empty'] for r in selected))
    out['interpretation'] = 'Descriptive length accounting. A different natural continuation may end earlier; max64 on a longer gold suffix is not itself proof of learned EOS failure.'
    return out


def main():
    c, cases = study.inspect()
    job = read_json(study.RUN / 'job.json')
    result_path = study.RUN / 'result.json'; result = read_json(result_path)
    if job['status'] != 'complete' or alive(job):
        raise ValueError('Actual diagnostic must be terminal')
    if (result['config_sha256'] != sha256(study.CONFIG) or result['cases_sha256'] != c['files']['cases.json']
            or result['optimizer_updates'] != 0 or result['scientific_teacher_tokens'] != 0
            or result['protected_test_used'] or result['Base_adopted'] or result['Chat_adopted']
            or result['GPU_seconds'] > c['GPU_budget_seconds']
            or not all(v for arm in result['checks'].values() for v in arm.values())):
        raise ValueError('Read-only completion invariants failed')
    rows = result['rows']; tok = Tokenizer(c['tokenizer']['path'])
    audit_rows(rows, cases, tok, c)
    if study.summarize(rows, cases, c['marker']) != result['summary']:
        raise ValueError('Result summary differs from raw rows')
    for row in rows:
        path = study.RUN / 'outputs' / row['checkpoint'] / (row['id'] + '-' + row['context'] + '.json')
        if read_json(path) != row or row['config_sha256'] != sha256(study.CONFIG):
            raise ValueError('Standalone raw file differs from result')
    notes = read_json(NOTES)
    if (notes['result_sha256'] != sha256(result_path) or notes['cases_sha256'] != c['files']['cases.json']
            or len(notes['cases']) != len(cases) or {n['id'] for n in notes['cases']} != {n['id'] for n in cases}
            or any(not isinstance(n.get('reason'), str) or not n['reason'].strip() for n in notes['cases'])
            or notes['independent_human_blind'] or notes['quality_adoption_scores']):
        raise ValueError('All-case nonblind content observations are missing or misbound')
    summary = dict(status='read_only_diagnostic_all96_complete', created_at=now(),
        result_sha256=sha256(result_path), config_sha256=sha256(study.CONFIG), notes_sha256=sha256(NOTES),
        optimizer_updates=0, scientific_teacher_tokens=0, GPU_seconds=result['GPU_seconds'],
        summary=result['summary'], length_accounting=length_subgroups(rows, cases),
        checks=result['checks'], complete_outputs=len(rows), raw_outputs_reconstructed=True,
        Base_adopted=False, Chat_adopted=False, protected_test_used=False,
        independent_human_blind=False, quality_criteria_unchanged=True, requested_five_steps_complete=False,
        decision='Neither learned checkpoint meets the frozen local context-dependence marker; do not repeat compact packing/isolation based on this sample. Test one matched everyday/story training-mixture hypothesis next.',
        limitations=c['limitations'])
    summary_path = ROOT / 'reports/phase6/broad_context_diagnostic_review.json'
    atomic_json(summary_path, summary)
    archive = ROOT / 'reports/phase6/broad-context-diagnostic-20261006_evidence.tar.gz'
    if archive.exists():
        raise ValueError('Completed archive retained; do not overwrite')
    files = [study.CONFIG, NOTES, summary_path, Path(__file__),
             ROOT / 'reports/phase6/broad_context_diagnostic_tests.xml']
    files.extend(p for p in study.RUN.rglob('*') if p.is_file() and p.suffix in ('.json', '.py', '.ps1', '.jsonl', '.lock'))
    files = sorted(set(files))
    entries = [dict(path=p.relative_to(ROOT).as_posix(), sha256=sha256(p), bytes=p.stat().st_size) for p in files]
    temporary = archive.with_suffix('.tmp')
    with tarfile.open(temporary, 'w:gz') as stream:
        for path in files:
            stream.add(path, arcname=path.relative_to(ROOT).as_posix(), recursive=False)
    temporary.replace(archive)
    atomic_json(ROOT / 'reports/phase6/broad_context_diagnostic_evidence_manifest.json',
        dict(entries=entries, text_files=len(files), uncompressed_bytes=sum(e['bytes'] for e in entries),
            archive=dict(path=archive.relative_to(ROOT).as_posix(), sha256=sha256(archive), bytes=archive.stat().st_size),
            checkpoint_tensors_included=False, created_at=now()))
    print(json.dumps(dict(status=summary['status'], GPU_seconds=summary['GPU_seconds'],
        marker={k: v['local_context_dependence_marker'] for k, v in summary['summary'].items()},
        archive=sha256(archive))), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
