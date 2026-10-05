"""Small metadata checks and an explicit nonlaunch record after the bounded comparison."""
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from run_narrative_comparison import RUN,DATA,CONFIG,load_config

c=load_config();result=read_json(RUN/'compare-result.json');review=read_json(RUN/'review.json')
ev=c['evaluation']
checks=dict(evaluation_config=sha256(ROOT/ev['config'])==ev['config_sha256'],
    semantic_suite=sha256(ROOT/ev['semantic_suite'])==ev['semantic_sha256'],
    evaluation_data_manifest=sha256(Path('/home/aihub_ubuntu/jmicro-data/evaluation-v2/manifest.json'))==ev['data_manifest_sha256'],
    science_budget=result['scientific_teacher_tokens']==200000000,
    valid_sum=result['scientific_valid_input_tokens']==sum(v['additional_input_tokens'] for v in result['checkpoints'].values()),
    physical_sum=result['physical_input_tokens']==sum(v['physical_input_tokens'] for v in result['checkpoints'].values()),
    comparison_goals=all(v['source_teachers']==c['comparison_goals'] for v in result['checkpoints'].values()),
    every_structural_EOS_finite=all(math.isfinite(r['eos_nll']) and r['eos_nll']>=0 for v in result['structures'].values() for r in v['body']['rows']),
    full_raw_reviews=all(len(v['notes'])==80 for v in read_json(RUN/'compare-annotations.json')['arms'].values()),
    quality_failed=not review['eligible_for_expansion'],
    expanded_preparation_not_launched=not (DATA/'ready-expanded.json').exists() and not (RUN/'prepare-expanded-job.json').exists(),
    expanded_training_not_launched=not (RUN/'job-expand.json').exists())
assert all(checks.values()),checks
integrity=dict(checks=checks,passed=True,config_sha256=sha256(CONFIG),checked_at=now(),script_sha256=sha256(Path(__file__)))
write_json(RUN/'metadata-integrity.json',integrity)
write_json(ROOT/'reports/phase6/narrative_diversity_integrity.json',integrity)
judgment=dict(candidate_adopted=False,reason='unchanged_quality_gates_failed',
    stage3=dict(status='not_launched',expanded_documents=0,additional_teacher_tokens=0,
        proposed_minimum_documents=50000,proposed_minimum_prepared_tokens=5000000,proposed_teacher_tokens=500000000),
    original_UI_retained=True,review_sha256=sha256(RUN/'review.json'),checked_at=now())
write_json(RUN/'judgment.json',judgment)
write_json(ROOT/'reports/phase6/narrative_diversity_judgment.json',judgment)
print('Metadata pins and actual branch checked; growth not launched')
