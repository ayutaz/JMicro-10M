"""CPU native independent learning-seed construction, not GPU/quality evidence."""
import copy
from pathlib import Path
import sys

import pytest
import torch

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from base_parallel_residual_trainer import FreshResidualTrainer, CEOnlyOriginalSampler
from base_teacher_decay_trainer import TeacherDecayTrainer
from base_teacher_decay_seed_protocol import (GOALS, build_independent,
    validate_independent_zero, require_quality_screen)
from base_teacher_decay_2b_protocol import resume_probe
from natural_context_contrast_trainer import host
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool, FixtureCodec, parent


@pytest.fixture
def factories(tmp_path):
    pool = tmp_path/'pool'
    manifest = fixture_pool(pool)
    codec = FixtureCodec()
    config = copy.deepcopy(parent()['model_config'])
    with torch.device('meta'):
        config['expected_parameter_count'] = sum(p.numel() for p in JMicroModel(config).parameters())
    sampler = CEOnlyOriginalSampler(pool, manifest, codec, GOALS)
    plan = dict(source_binding=copy.deepcopy(sampler.binding), goals=copy.deepcopy(GOALS),
        variants=dict(sequential=config), optimizer=dict(seed=42,batch=4,
            warmup_gold=1000,peak_lr=.002,final_lr=1e-5))
    binding = dict(training_seed=43, weights_role='scientific_independent_seed_confirmation',
                   learned_parent_weights_used=False, probe_weights_used=False,
                   source_binding=copy.deepcopy(sampler.binding))
    def source():
        return TeacherDecayTrainer(FreshResidualTrainer(config,
            CEOnlyOriginalSampler(pool,manifest,codec,GOALS),
            dict(weights_role='scientific_fresh_teacher_decay_pilot'),
            'sequential',batch=4,device='cpu',warmup=1000))
    def independent():
        return build_independent(plan,codec,binding,device='cpu')
    return source, independent, plan, codec, binding


def test_real_fresh43_differs_from42_and_is_reproducible(factories):
    source, independent, _, _, _ = factories
    original = host(source().state_dict())
    zero = host(independent().state_dict())
    assert all(validate_independent_zero(original,zero).values())
    assert equal_state(zero,host(independent().state_dict()))
    assert zero['spec']['weight_decay'] == original['spec']['weight_decay']
    assert zero['sampler']['goals'] == original['sampler']['goals'] == GOALS


def test_real_seed43_learned_parent_resume_and_foreign_seed_refusal(factories,tmp_path):
    source, independent, _, _, _ = factories
    trainer = independent();trainer.step();trainer.step()
    checkpoint = tmp_path/'learned43.pt';trainer.save(checkpoint)
    def make(path):
        obj = independent();obj.load(path);return obj
    result = resume_probe(make,checkpoint,tmp_path/'split43.pt',lambda:None)
    assert all(result['checks'].values())
    assert result['initial_counters']['update'] == 2
    assert result['final_verification_counters']['update'] == 6
    original = source();original.step()
    foreign = tmp_path/'learned42.pt';original.save(foreign)
    untouched = independent();before = host(untouched.state_dict())
    with pytest.raises(ValueError,match='recipe/source binding'):
        untouched.load(foreign)
    assert equal_state(before,host(untouched.state_dict()))
    with pytest.raises(ValueError,match='Untouched'):
        validate_independent_zero(host(source().state_dict()),host(trainer.state_dict()))


def test_factory_refuses_resetting_seed42_or_changed_teacher_budget(factories):
    _, _, plan, codec, binding = factories
    bad = dict(binding,training_seed=42)
    with pytest.raises(ValueError,match='independent43'):
        build_independent(plan,codec,bad,device='cpu')
    altered = copy.deepcopy(plan);altered['goals']['web'] += 1
    with pytest.raises(ValueError,match='quota recipe'):
        build_independent(altered,codec,binding,device='cpu')
    bad = copy.deepcopy(binding);bad['source_binding']['manifest_sha256'] = 'foreign'
    with pytest.raises(ValueError,match='independent43'):
        build_independent(plan,codec,bad,device='cpu')


def test_quality_gate_refuses_pilot_and_failed_full_guard():
    # Synthetic guard fixtures, never substituted for actual source evidence.
    with pytest.raises(ValueError,match='full-quality'):
        require_quality_screen(dict(exploratory_advance_eligible=True))
    completion = dict(status='same_parent_teacher_decay2B_all80_reviewed',
        eligible_for_final_Base_validation=True,fixed_condition_closed=False,
        all80_new_individually_read=True,old_control80_original_notes_reused=True,
        process_exited=True,scientific_cumulative_teacher_tokens=sum(GOALS.values()),
        Base_complete=False,Base_adopted=False,Chat_started=False,
        quantization_started=False,protected_test_scored=False,
        absolute_dev_screen={k:True for k in ('grammar_at_least56','coherence_at_least27',
            'appropriate_at_least27','EOS_at_least37','repetition_at_most18','no_empty_role_unicode')},
        quality_comparisons={k:dict(passed=True) for k in ('matched_native','strong','cached_native')},
        original_Web=dict(unchanged_guard=True))
    require_quality_screen(completion)
    bad = copy.deepcopy(completion);bad['quality_comparisons']['strong']['passed'] = False
    with pytest.raises(ValueError,match='original'):
        require_quality_screen(bad)
    bad = copy.deepcopy(completion);bad['absolute_dev_screen']['coherence_at_least27'] = False
    with pytest.raises(ValueError,match='original'):
        require_quality_screen(bad)
