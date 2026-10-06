"""Bind all cases and cluster exact content aliases without rerunning inference."""
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,now,sha256
from jmicro.training import atomic_json
from jmicro.japanese_evaluation import clustered_ci
from phase6_performance import alive

RUN = ROOT/'reports/phase6/teacher-semantic-signal-20261007'
OUT = ROOT/'reports/phase6/teacher_semantic_signal_review.json'


def exact_content_families(rows):
    """Cluster identical context pairs without changing any case weights."""
    groups = defaultdict(list)
    for row in rows:
        groups[row['family']].append(row)
    keys, aliases = {}, defaultdict(list)
    for family, cases in groups.items():
        if len(cases) != 2 or len({r['context'] for r in cases}) != 2:
            raise ValueError('Each semantic family needs two distinct contexts')
        content = sorted([dict(context=r['context'], choices=sorted(r['choices']),
            gold_choice=r['choices'][r['label']], category=r['category'])
            for r in cases], key=lambda r: r['context'])
        key = hashlib.sha256(json.dumps(content, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        keys[family] = key
        aliases[key].append(family)
    return groups, keys, aliases


def main():
    if OUT.exists():
        raise ValueError('Preserve completed full semantic review')
    path = RUN/'result.json'
    result = json.loads(path.read_text())
    job = json.loads((RUN/'job.json').read_text())
    if job['status'] != 'complete' or alive(job) or result['GPU_seconds'] > 180:
        raise ValueError('Completed actual semantic diagnostic required')
    teacher,student = result['rows']['teacher'],result['rows']['native10M']
    if len(teacher) != 192 or len(student) != 192 or [r['case_sha256'] for r in teacher] != [r['case_sha256'] for r in student]:
        raise ValueError('Match all192 raw-bound cases')
    groups, keys, aliases = exact_content_families(teacher)
    effective = {}
    for name,rows in (('teacher',teacher),('native10M',student)):
        mapped = [dict(r,family=keys[r['family']]) for r in rows]
        paired = [dict(id=f,family=keys[f],credit=float(all(r['credit']==1 for r in rows if r['family']==f))) for f in groups]
        effective[name] = dict(accuracy=clustered_ci(mapped),both_contexts_hard_correct=clustered_ci(paired))
    differences = [dict(id=t['id'],family=keys[t['family']],credit=t['credit']-s['credit'])
        for t,s in zip(teacher,student,strict=True)]
    delta = clustered_ci(differences)
    signal = (result['teacher_context_signal_passed']
        and effective['teacher']['accuracy']['ci95'][0]>.5
        and effective['teacher']['both_contexts_hard_correct']['ci95'][0]>.25
        and delta['ci95'][0]>0)
    categories = {k:dict(teacher=v['point'],native=result['models']['native10M']['summary']['categories'][k]['point'])
        for k,v in result['models']['teacher']['summary']['categories'].items()}
    report = dict(status='all192_raw_bound_semantic_comparison_review_complete',created_at=now(),
        result=dict(path=str(path),sha256=sha256(path)),config_sha256=result['config_sha256'],
        cases=192,nominal_families=96,effective_exact_content_pair_families=len(aliases),
        exact_alias_groups=[v for v in aliases.values() if len(v)>1],
        original_nominal_summary=result['models'],effective_content_cluster_summary=effective,
        effective_paired_teacher_minus_native_accuracy=delta,
        original_signal_gate_passed=result['teacher_context_signal_passed'],
        conservative_context_signal_gate_passed=signal,categories=categories,
        all_discordant_case_details=result['comparison']['discordant'],
        all_discordant_cases_read=True,discordant_cases=result['comparison']['discordant_cases'],
        GPU_seconds=result['GPU_seconds'],actual_identity=result['actual_identity'],actual_process_absent=True,
        original_outputs_scores_and_gate_unchanged=True,no_new_GPU_or_training_for_alias_adjustment=True,
        optimizer_updates=0,scientific_teacher_tokens=0,Base_complete=False,Chat_started=False,quantization_started=False,
        protected_test_records_JSON_decoded=False,
        decision='A teacher semantic signal exists; probe whether TRAIN-only context features provide a finite noncollapsed relational loss and a feasible measured GPU budget before controlled training.' if signal else
            'Do not proceed to knowledge-transfer training on this diagnostic: the conservative content-cluster gate is not met.',
        next_action='Use the already accepted broad75/20/5 large2B TRAIN pool for a bounded teacher-feature probe, keeping source/manifest/protected-family bindings.' if signal else
            'Close this teacher-transfer diagnostic: the content-alias-adjusted confidence interval does not prove teacher superiority. Preserve all outputs and gates; do not start the conditional teacher-feature/training branch or rescue it with prompt/model/threshold changes.',
        limitations='Exact duplicate family aliases are clustered while all192 original case weights and historic outcomes are retained. Constructed templates remain correlated beyond exact duplicates; CIs describe this dev packet, not a population of natural Japanese tasks. External teacher differs in data/tokenizer/architecture/post-training and contamination is unknown. The teacher is worse on negation/coreference; transfer can regress those skills and must keep retention/whole-Base gates. This is not Base adoption or knowledge-transfer success.')
    atomic_json(OUT,report)
    print(dict(effective_families=len(aliases),paired_difference=delta,signal_passed=signal,categories=categories))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
