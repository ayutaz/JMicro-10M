"""Scientific reuse of original proof; doubled clocks and stochastic RNG audited."""
import copy
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import rdrop_science_protocol as protocol
import run_rdrop_science as runner
from rdrop_target_batch_trainer import TargetBatchRDropTrainer
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from test_document_progress_training import builders


def inputs():
    p = json.loads((ROOT/'reports/phase6/rdrop-target-batch-probe-20261015/result.json').read_text())
    a = json.loads((ROOT/'reports/phase6/rdrop-science-preparation-20261016/authorization.json').read_text())
    return p,a


def test_actual_proof_preserves_old_cost_rejection_and_explicitly_authorized_first_science():
    p,a = inputs()
    assert p['science_budget_eligible'] is False
    assert protocol.science_budget(p,a) == 1757
    assert a['prior_total_GPU_seconds']+1757 > 4800


@pytest.mark.parametrize('bad',['passed','ledger','old_eligible','updates','scientific','DEV','TEST','count',
    'capacity','capadam','graphs','checks','cache','tol','resume','snapshot','timings','forecast','cost','native'])
def test_owned_numerical_proof_historical_cost_and_all32_cannot_be_forged(bad):
    p,a = inputs()
    if bad == 'passed': p['passed'] = False
    elif bad == 'ledger': p['cumulative_GPU_ledger_closed'] = False
    elif bad == 'old_eligible': p['science_budget_eligible'] = True
    elif bad == 'updates': p['verification_optimizer_updates'] -= 1
    elif bad == 'scientific': p['scientific_teacher_positions'] = 1
    elif bad in ('DEV','TEST'): p[bad+'_opened'] = True
    elif bad == 'count': p['training_parameters'] += 1
    elif bad == 'capacity': p['capacity']['shape'] = [48,512]
    elif bad == 'capadam': p['capacity']['optimizer_updates'] = 1
    elif bad == 'graphs': p['capacity']['retained_decoder_graphs'] = 1
    elif bad == 'checks': del p['capacity']['checks']['Adam_zero']
    elif bad == 'cache': p['active_cache']['passed'] = False
    elif bad == 'tol': p['active_cache']['absolute_tolerance'] = .1
    elif bad == 'resume': p['full_state_history_resume_exact'] = False
    elif bad == 'snapshot': p['reference6_snapshot'] = {}
    elif bad == 'timings': p['all32_timings'].pop()
    elif bad == 'forecast': p['scientific_forecast_seconds'] -= 600
    elif bad == 'cost': p['cumulative_total_GPU_seconds'] = p['cumulative_technical_GPU_seconds']
    else: del p['native3_subchecks'][0]['CE_loss']
    with pytest.raises(ValueError): protocol.science_budget(p,a)


@pytest.mark.parametrize('arm',['native_CE_control','normalized_rdrop'])
def test_real_state_all_history_same_original_stream_and_intended_RNG_difference(tmp_path,arm):
    parent,build = builders(tmp_path)
    old = build(legacy=True)
    candidate = TargetBatchRDropTrainer(parent,old.sampler,old.binding,batch=6,device='cpu',arm=arm)
    rows = [candidate.step() for _ in range(3)]
    state = host(candidate.state_dict())
    rollup = protocol.validate_history(rows,state)
    assert rollup['gold_evaluations'] == rollup['main_teachers']*(2 if arm == 'normalized_rdrop' else 1)
    control = build('native_CE_control')
    control_rows = [control.step() for _ in range(3)]
    control_state = host(control.state_dict())
    assert all(protocol.matched_original(state,control_state).values())
    assert protocol.paired_history(rows,control_rows)
    if arm == 'normalized_rdrop':
        assert not equal_state(state['RNG'],control_state['RNG'])
        assert state['counters']['physical_input_tokens'] == 2*control_state['counters']['physical_input_tokens']
    changed = copy.deepcopy(rows)
    changed[0]['main_physical_input_tokens'] += 1
    with pytest.raises(ValueError): protocol.paired_history(changed,control_rows)


@pytest.mark.parametrize('bad',['combined','ce','pairs','teachers','physical','nonfinite','earlier_stream'])
def test_no_partial_or_corrupted_history_even_with_valid_final_checkpoint(tmp_path,bad):
    parent,build = builders(tmp_path)
    old = build(legacy=True)
    trainer = TargetBatchRDropTrainer(parent,old.sampler,old.binding,batch=6,device='cpu')
    rows = [trainer.step() for _ in range(3)]
    state = host(trainer.state_dict())
    if bad == 'combined': rows[0]['combined_loss'] += 1
    elif bad == 'ce': rows[0]['CE_view2_loss'] += 1
    elif bad == 'pairs': rows[0]['consistency_pairs_this_update'] -= 1
    elif bad == 'teachers': rows[0]['CE_targets_this_update'] -= 1
    elif bad == 'physical': rows[0]['second_view_physical_input_tokens'] = 0
    elif bad == 'nonfinite': rows[0]['symmetric_KL'] = float('nan')
    else: rows[0]['main_physical_inputs_this_update'] = 0
    with pytest.raises(ValueError): protocol.validate_history(rows,state)


def test_quality_needs_matched_and_all_original_guards_and_never_adopts(monkeypatch):
    args = [{} for _ in range(9)]
    monkeypatch.setattr(protocol,'quality_gates',lambda *a:dict(passed=False))
    monkeypatch.setattr(protocol,'original_quality',lambda *a:dict(eligible=True))
    assert not protocol.pilot_quality(*args)['eligible_for_separately_defined_main_comparison']
    monkeypatch.setattr(protocol,'quality_gates',lambda *a:dict(passed=True))
    result = protocol.pilot_quality(*args)
    assert result['eligible_for_separately_defined_main_comparison']
    assert result['Base_qualified'] is result['Base_adopted'] is False
    monkeypatch.setattr(protocol,'original_quality',lambda *a:dict(eligible=False))
    assert not protocol.pilot_quality(*args)['eligible_for_separately_defined_main_comparison']


def test_builder_uses_original_parent_not_control_or_probe(monkeypatch):
    calls,parent = [],object()
    monkeypatch.setattr(runner.torch,'load',lambda path,**kw:(calls.append(path),parent)[1])
    monkeypatch.setattr(runner,'Tokenizer',lambda path:object())
    source = dict(pool='fixture',manifest_sha256='m')
    monkeypatch.setattr(runner,'OriginalTrainCorpusSampler',lambda *a,**kw:SimpleNamespace(binding=source))
    monkeypatch.setattr(runner,'TargetBatchRDropTrainer',lambda actual,sampler,b,**kw:(actual,b,kw))
    config = dict(parent=dict(path='original10B'),tokenizer=dict(path='codec'),source_binding=source,goals=runner.GOALS)
    actual,binding,kw = runner.build(config,dict(weights_role='scientific_rdrop_target_batch25M'))
    assert actual is parent and calls == ['original10B'] and kw['batch'] == 48 and kw['seed'] == 42


@pytest.mark.parametrize('bad',['missing','carried_cost','scope'])
def test_missing_new_authorization_or_erased_history_refused(bad):
    p,a = inputs()
    if bad == 'missing': a = {}
    elif bad == 'carried_cost': a['prior_total_GPU_seconds'] = 0
    else: a['old180_4800_are_historical_not_future_global_limits'] = False
    with pytest.raises(ValueError): protocol.science_budget(p,a)
