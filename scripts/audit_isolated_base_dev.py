"""Actual DEV export/reader/reviewer read-set proof; no real model or TEST work."""
import hashlib
import json
from pathlib import Path
import sys
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'scripts')]
from jmicro.evaluation_boundary import load_dev_suite,validate_dev_outputs,CASE_FIELDS
from prepare_isolated_base_dev import SOURCE,SOURCE_SHA,OUTPUT,MANIFEST_NAME,CASES_NAME


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    run=ROOT/'reports/phase6/evaluation-boundary-20261015'
    target=run/'actual_DEV_read_boundary_audit.json'
    if target.exists():raise ValueError('Preserve original actual input audit')
    export=json.loads((run/'dev_export.json').read_text())
    allowed={SOURCE,OUTPUT/MANIFEST_NAME,OUTPUT/CASES_NAME}
    observed=[];original=Path.open
    def guarded(path,*args,**kwargs):
        if path not in allowed:raise AssertionError('Unexpected actual evaluation file read: '+str(path))
        observed.append(str(path))
        return original(path,*args,**kwargs)
    with patch.object(Path,'open',guarded):
        blob=SOURCE.read_bytes()
        assert hashlib.sha256(blob).hexdigest()==SOURCE_SHA
        outputs=json.loads(blob)['outputs']
        suite=load_dev_suite(OUTPUT/MANIFEST_NAME,export['manifest_sha256'])
        assert validate_dev_outputs(outputs,suite)
        assert all(set(c)==CASE_FIELDS and c['split']=='dev' for c in suite.cases)
    assert observed==[str(SOURCE),str(OUTPUT/MANIFEST_NAME),str(OUTPUT/CASES_NAME)]
    assert sha(ROOT/'src/jmicro/model.py')=='298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83'
    original_config=json.loads((ROOT/'configs/phase6/base_document_balance_comparison.json').read_text())
    for name in ('src/jmicro/training.py','scripts/run_eos_short_pilot.py'):
        assert sha(ROOT/name)==original_config['source_sha256'][name]
    review=json.loads((ROOT/'configs/phase6/base_document_balance_review.json').read_text())
    name='scripts/review_parameter_displacement_anchor.py'
    assert sha(ROOT/name)==review['helper_sha256'][name]
    proof=dict(passed=True,status='actual_DEV80_identity_and_enforced_read_set_verified',
        source_generation_sha256=SOURCE_SHA,manifest_sha256=suite.manifest_sha256,
        cases_sha256=suite.cases_sha256,case_count=80,opened_paths=observed,
        mixed_suite_or_TEST_opened=False,TEST_parsed=False,generated_answers_exported=False,
        frozen_legacy_generation_review_training_and_native_model_sources_unchanged=True,
        native_model_created=False,real_model_evaluated=False,GPU_work=False,
        new_quality_evidence=False,Base_adopted=False,
        scope='Actual stored80 DEV cases plus new future reader/generation/review boundary. Legacy closed commands are unchanged and must not be reused for new DEV runs.',
        source_sha256=sha(Path(__file__)))
    target.write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(proof,ensure_ascii=False))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
