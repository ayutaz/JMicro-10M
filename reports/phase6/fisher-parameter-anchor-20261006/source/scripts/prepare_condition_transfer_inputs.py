"""Actual common100M ordinary teacher audit for accepted generated curriculum."""
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.eos_pilot import TrainView
from jmicro.training import atomic_json
from phase6_performance import alive,identity
from condition_transfer_curriculum import CurriculumTrainView
from cached_three_source_index import CachedThreeSourceIndex
from run_condition_source_learning import ordinary_stream_digest,GOALS,check_reference


def main():
    started=time.monotonic()
    run=ROOT/'reports/phase6/condition-transfer-curriculum-20261006-v2'
    output=run/'ordinary-stream-audit.json'
    if output.exists():raise ValueError('Preserve completed fixed teacher audit; do not repeat')
    p=read_json(ROOT/'reports/phase6/condition_source_transfer_proposal.json')
    for ref in (p['evidence'],p['pair_evidence'],p['natural_control']['result'],p['natural_control']['review'],p['natural_control']['generation_notes']):check_reference(ref)
    old=read_json(ROOT/'configs/phase6/condition_source_learning_100m.json')
    prior=ROOT/'reports/phase6/condition-source-learning-100m-20261006'
    job=read_json(prior/'job.json');r=read_json(prior/'compare-result.json')
    if (job['status']!='complete' or alive(job) or r['config_sha256']!=sha256(ROOT/'configs/phase6/condition_source_learning_100m.json')
            or r['checkpoints']['large2048']!=p['natural_control']['checkpoint']
            or r['checkpoints']['large2048']['source_teachers']!=GOALS):
        raise ValueError('Actual terminal unchanged natural100M control required')
    data=Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-transfer-curriculum-20261006-v2')
    view=CurriculumTrainView(data,sha256(data/'manifest.json'))
    check_reference(old['accepted_compact_index'])
    pool=TrainView(old['pool']['pool'],old['pool']['manifest_sha256']);pool.index=CachedThreeSourceIndex(pool)
    if not pool.index.cache_reused:raise ValueError('Original13GB index must not be reparsed')
    def check():
        if time.monotonic()-started>30:raise TimeoutError('Bounded30s common teacher audit exhausted')
    actual=ordinary_stream_digest(pool,view,check)
    prior_ref=old['references']['ordinary_stream_audit'];check_reference(prior_ref)
    control=read_json(Path(prior_ref['path']))['large']
    checks={k:actual[k]==control[k] for k in ('target_sha256','teachers','EOS','body_bytes')}
    if not all(checks.values()):raise ValueError('Curriculum changed original ordinary supervised sequences')
    proof=dict(status='actual_generated_vs_natural100M_ordinary_teacher_sequences_identical',created_at=now(),**identity(),
        actual_generated=actual,previous_natural=control,checks=checks,goals=GOALS,CPU_seconds=time.monotonic()-started,CPU_limit_seconds=30,
        generated_manifest_sha256=sha256(data/'manifest.json'),accepted_generated_review_sha256=sha256(data/'content-review.json'),
        natural_result_sha256=sha256(prior/'compare-result.json'),natural_ordinary_audit=prior_ref,
        native_compact_index=old['accepted_compact_index'],script_sha256=sha256(Path(__file__)),
        scientific_teacher_tokens=0,actual_GPU_seconds=0,protected_test_used=False,
        limitations='CPU replay observes actual teacher IDs/counts/EOS/byte lengths, not model updates or GPU quality. Conditional row interleaving/length/EOS distribution differs. Ordinary physical input padding beyond quotas can differ while supervised target sequences are equal.')
    atomic_json(output,proof);print(dict(checks=checks,CPU_seconds=proof['CPU_seconds'],updates=actual['total_updates']))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
