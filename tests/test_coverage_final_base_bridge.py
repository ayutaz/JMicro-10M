"""Coverage admission is conditional; protocol fixtures are not model evidence."""
import sys

import pytest
from jmicro.experiment import ROOT, write_json

sys.path.insert(0, str(ROOT/'scripts'))
import run_textbook_coverage_v2 as coverage
from run_final_base_dev import coverage_source_recipe, screen_checks


def test_completed_coverage_candidate_uses_exact_frozen_guard(monkeypatch, tmp_path):
    run=tmp_path/'run';run.mkdir()
    write_json(run/'job.json',dict(status='complete',pid=2147483647,
        boot_id='fixture-not-real-CUDA',start_ticks='0'))
    config=tmp_path/'version2.json'
    monkeypatch.setattr(coverage,'CONFIG',config)
    monkeypatch.setattr(coverage,'RUN',run)
    recipe=dict(research_kind='same_material_teacher_coverage',recipe_version=2,quality_criteria_unchanged=True)
    called=[]
    def inspect(path):
        called.append(path)
        return recipe,{'fixture':'not-quality'},None,None
    monkeypatch.setattr(coverage,'inspect',inspect)
    assert coverage_source_recipe(config,run,coverage.CANDIDATE)==(recipe,{'fixture':'not-quality'})
    assert called==[config]
    for path,point in ((tmp_path/'other.json',coverage.CANDIDATE),(config,coverage.BASELINE)):
        with pytest.raises(ValueError,match='frozen version2'):
            coverage_source_recipe(path,run,point)
    assert called==[config]


def test_live_coverage_refuses_before_inspection(monkeypatch,tmp_path):
    run=tmp_path/'run';run.mkdir();write_json(run/'job.json',dict(status='running'))
    monkeypatch.setattr(coverage,'inspect',lambda _:pytest.fail('Live source must fail first'))
    with pytest.raises(ValueError,match='actually finish'):
        coverage_source_recipe(tmp_path/'missing.json',run,coverage.CANDIDATE)


def test_coverage_admission_does_not_weaken_absolute_quality():
    scores={str(i):dict(grammar=2,coherence=2,completion=1) for i in range(80)}
    ev=dict(greedy_rates=dict(eos=37,repetition=18,empty=0,role_leak=0,unicode_failure=0))
    assert all(screen_checks(ev,scores).values())
    ev['greedy_rates']['repetition']=19
    assert not all(screen_checks(ev,scores).values())
    ev['greedy_rates']['repetition']=18
    for i in range(54):scores[str(i)]['coherence']=1
    assert not screen_checks(ev,scores)['coherence_at_least27']


def test_independent_seed_missing_cache_refuses_before_index_scan(tmp_path):
    from run_seeded_base_confirmation import accepted_index_cache
    with pytest.raises(ValueError,match='refuse original index rescan'):
        accepted_index_cache(dict(pool=str(tmp_path),manifest_sha256='a'*64))
    assert not list(tmp_path.iterdir())
