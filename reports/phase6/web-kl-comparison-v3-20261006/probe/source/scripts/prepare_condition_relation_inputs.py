"""One bounded CPU replay: original3 teacher sequences vs completed curriculum."""
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.eos_pilot import TrainView
from jmicro.training import atomic_json
from phase6_performance import identity
from condition_relation_language import DATA,RelationLanguageTrainView
from prepare_condition_relation_language import RUN,references
from cached_three_source_index import CachedThreeSourceIndex
from run_condition_source_learning import ordinary_stream_digest,GOALS,check_reference


def main():
    started=time.monotonic();references();out=RUN/'ordinary-stream-audit.json'
    if out.exists():raise ValueError('Retain completed audit; no repeated replay')
    cfg=read_json(ROOT/'configs/phase6/condition_transfer_comparison.json')
    source=cfg['references']['ordinary_stream_audit'];check_reference(source)
    control=read_json(Path(source['path']))['actual_generated']
    view=RelationLanguageTrainView(DATA,sha256(DATA/'manifest.json'))
    check_reference(cfg['accepted_compact_index'])
    pool=TrainView(cfg['pool']['pool'],cfg['pool']['manifest_sha256']);pool.index=CachedThreeSourceIndex(pool)
    if not pool.index.cache_reused:raise ValueError('Must reuse original compact cache, no13GB scan')
    def check():
        if time.monotonic()-started>30:raise TimeoutError('CPU30second ordinary replay budget exhausted')
    actual=ordinary_stream_digest(pool,view,check)
    checks={k:actual[k]==control[k] for k in ('target_sha256','teachers','EOS','body_bytes')}
    if not all(checks.values()):raise ValueError('Bridge changed ordinary supervised sequences')
    report=dict(status='actual_relation_vs_curriculum100M_original3_teachers_identical',created_at=now(),**identity(),
        actual_generated=actual,previous_control=control,checks=checks,goals=GOALS,CPU_seconds=time.monotonic()-started,
        CPU_limit_seconds=30,generated_manifest_sha256=sha256(DATA/'manifest.json'),
        accepted_generated_review_sha256=sha256(DATA/'content-review.json'),
        control_result_sha256=sha256(ROOT/'reports/phase6/condition-transfer-comparison-20261006/compare-result.json'),
        prior_ordinary_audit=source,native_compact_index=cfg['accepted_compact_index'],script_sha256=sha256(Path(__file__)),
        actual_GPU_seconds=0,scientific_teacher_tokens=0,protected_test_used=False,
        limitations='CPU actual sampler replay, not GPU learning. Conditional interleaving/padding and own targets differ; original3 supervision equal.')
    atomic_json(out,report);print(dict(checks=checks,CPU_seconds=report['CPU_seconds'],updates=actual['total_updates']))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
