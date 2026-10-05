"""Held-out admission/quality protocol fixtures; no real test split access."""
import copy
import sys

import pytest
from jmicro.experiment import ROOT,write_json

sys.path.insert(0,str(ROOT/'scripts'))
import run_final_base_test as command
from review_final_base_test import quality_checks,validate_generation
from review_final_base_dev import row_key,validate_content


class FixtureTokenizer:
    def decode_bytes(self,ids):
        return b'fixture sentence.' if 11 in ids else b''


def examples():
    cases={f'fixture-{i}':dict(id=f'fixture-{i}',prefix='fixture prefix',category='fixture') for i in range(20)}
    rows=[]
    for case in cases.values():
        for mode,suppressed,seed in (('greedy',True,42),('greedy',False,42),
                                     ('sampling',True,42),('sampling',True,43),('sampling',True,44)):
            rows.append(dict(case,split='test',decoding=mode,suppressed=suppressed,seed=seed,
                generated_ids=[11,3],text='fixture sentence.',valid_utf8=True,empty_response=False,
                role_leak=False,repetition=False,stop_reason='stop_id'))
    generation=dict(split='test',max_new_tokens=64,sampling_evaluated=True,temperature=.8,top_p=.9,outputs=rows)
    notes=[[row_key(r),2,2,2,1,'This fixture is a protocol check, not actual model evidence.'] for r in rows]
    rules=command.test_rules(dict(targets=dict(base_grammar_2_rate=.7,stop_success_min=.95,
        empty_response_max=.05,role_leak_max=.01,unicode_failure_max_fixed_suite=0),test_per_suite=20))
    return generation,cases,notes,rules


def test_incomplete_full_dev_cannot_freeze_or_open_test(monkeypatch,tmp_path):
    monkeypatch.setattr(command,'SELECTION',tmp_path/'selection.json')
    def incomplete(_):raise ValueError('Independent learned seed/full dev pending')
    monkeypatch.setattr(command,'full_dev_evidence',incomplete)
    monkeypatch.setattr(command,'Shard',lambda *_:pytest.fail('Protected split opened before eligibility'))
    with pytest.raises(ValueError,match='pending'):
        command.freeze(tmp_path/'recipe.json',tmp_path/'primary.json',tmp_path/'replicate.json')
    assert not list(tmp_path.iterdir())


def test_protected_selection_cannot_be_replaced_after_results(monkeypatch,tmp_path):
    seal=tmp_path/'selection.json';write_json(seal,dict(fixture='already sealed'))
    monkeypatch.setattr(command,'SELECTION',seal)
    monkeypatch.setattr(command,'confirmation_pair',lambda *_:pytest.fail('Another candidate selected'))
    with pytest.raises(ValueError,match='no alternate recipe'):
        command.freeze(tmp_path/'another.json',tmp_path/'primary.json',tmp_path/'replicate.json')
    assert not (tmp_path/'another.json').exists()


def test_final_generation_requires_all_test_modes_and_correct_seed():
    generation,cases,_,_=examples()
    assert len(validate_generation(generation,cases,FixtureTokenizer(),20))==20
    for mutate in (lambda g:g['outputs'].pop(),lambda g:g['outputs'][2].__setitem__('seed',99),
                   lambda g:g['outputs'][0].__setitem__('split','dev'),
                   lambda g:g['outputs'][0].__setitem__('valid_utf8',False)):
        changed=copy.deepcopy(generation);mutate(changed)
        with pytest.raises(AssertionError):validate_generation(changed,cases,FixtureTokenizer(),20)


def test_final_stop_uses_frozen95pct_not_dev_screen_ratio():
    generation,cases,notes,rules=examples()
    primary=validate_generation(generation,cases,FixtureTokenizer(),20)
    scores=validate_content(generation['outputs'],notes)
    assert all(quality_checks(primary,scores,rules,generation['outputs']).values())
    primary[0]['stop_reason']='max_new_tokens'
    assert quality_checks(primary,scores,rules,generation['outputs'])['stop_success_at_least_protocol95pct']
    primary[1]['stop_reason']='max_new_tokens'
    assert not quality_checks(primary,scores,rules,generation['outputs'])['stop_success_at_least_protocol95pct']


def test_unsuppressed_or_sampling_failures_cannot_hide_behind_greedy():
    generation,cases,notes,rules=examples()
    primary=validate_generation(generation,cases,FixtureTokenizer(),20)
    scores=validate_content(generation['outputs'],notes)
    generation['outputs'][4]['role_leak']=True
    checks=quality_checks(primary,scores,rules,generation['outputs'])
    assert checks['role_within_protocol'] and not checks['all100_raw_failures_zero']


def test_test_review_requires_all100_real_raw_bound_scores():
    generation,_,notes,_=examples()
    assert len(validate_content(generation['outputs'],notes))==100
    with pytest.raises(AssertionError):validate_content(generation['outputs'],notes[:-1])
    wrong=copy.deepcopy(notes);wrong[0][1]=True
    with pytest.raises(AssertionError):validate_content(generation['outputs'],wrong)


def test_chat_refuses_live_final_test_even_with_adoption_flag(tmp_path):
    from require_adopted_base import require_final_test_acceptance
    from jmicro.experiment import sha256
    from phase6_performance import identity
    run=tmp_path/'test';run.mkdir()
    evidence={}
    for key in ('final_test_config','final_test_review','final_test_result'):
        path=run/(key+'.json');write_json(path,dict(fixture='not actual GPU evidence'))
        evidence[key]=dict(path=str(path),sha256=sha256(path))
    write_json(run/'job.json',dict(status='complete',**identity()))
    accepted=dict(evidence,Base_adopted=True,selected_training_seed=42,
        independent_training_seed_confirmed=True,protected_test_used=True)
    with pytest.raises(ValueError,match='actually finished'):
        require_final_test_acceptance(accepted,'fixture-checkpoint')
