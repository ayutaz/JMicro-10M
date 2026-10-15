"""Actual GPU evidence, real CPU histories, control identity and quality gates."""
import copy
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import pytest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import scalegrad_science_protocol as protocol
import run_scalegrad as runner
from scalegrad_trainer import ScaleGradTrainer
from natural_context_contrast_trainer import host
from test_document_progress_training import builders


def actual_probe():
    return json.loads((ROOT/'reports/phase6/scalegrad-probe-20261015/result.json').read_text())


def test_actual_own_GPU_gate_fits_original_cumulative_cap_with_fixed25M_reserve():
    p=actual_probe()
    assert protocol.science_budget(p)==1406
    assert protocol.science_budget(p)+p['cumulative_total_GPU_seconds']<4800


@pytest.mark.parametrize('bad',['passed','ledger','eligible','updates','scientific','DEV','TEST','count',
    'capacity','capadam','caplabels','capgraphs','capchecks','cache','cache_tol','cache_subcheck',
    'resume','snapshot','timings','forecast','cost','science_cost','native'])
def test_required_owned_evidence_cannot_be_removed_retimed_or_rebudgeted(bad):
    p=actual_probe()
    if bad=='passed': p['passed']=False
    elif bad=='ledger': p['cumulative_GPU_ledger_closed']=False
    elif bad=='eligible': p['science_budget_eligible']=False
    elif bad=='updates': p['verification_optimizer_updates']=52
    elif bad=='scientific': p['scientific_teacher_positions']=1
    elif bad in ('DEV','TEST'): p[bad+'_opened']=True
    elif bad=='count': p['training_parameters']=10001408
    elif bad=='capacity': p['capacity']['shape']=[48,512]
    elif bad=='capadam': p['capacity']['optimizer_updates']=1
    elif bad=='caplabels': p['capacity']['main_teachers']=0
    elif bad=='capgraphs': p['capacity']['retained_decoder_graphs']=2
    elif bad=='capchecks': del p['capacity']['checks']['RNG_unchanged']
    elif bad=='cache': p['active_cache']['passed']=False
    elif bad=='cache_tol': p['active_cache']['absolute_tolerance']=.1
    elif bad=='cache_subcheck': del p['active_cache']['subchecks']['validity_exact']
    elif bad=='resume': p['full_state_history_resume_exact']=False
    elif bad=='snapshot': p['verification6_snapshot']={}
    elif bad=='timings': p['all32_timings'].pop()
    elif bad=='forecast': p['scientific_forecast_seconds']-=600
    elif bad=='cost': p['cumulative_total_GPU_seconds']=p['cumulative_technical_GPU_seconds']
    elif bad=='science_cost': p['prior_completed_science_GPU_seconds']=0.
    else: del p['native3_subchecks'][0]['CE_loss']
    with pytest.raises(ValueError): protocol.science_budget(p)


@pytest.mark.parametrize('arm',['native_CE_control','scalegrad'])
def test_real_Adam_ALL_history_and_exact_prior_control_stream(tmp_path,arm):
    parent,build=builders(tmp_path)
    old=build(legacy=True)
    current=ScaleGradTrainer(parent,old.sampler,old.binding,batch=6,device='cpu',arm=arm)
    rows=[current.step() for _ in range(3)]
    state=host(current.state_dict())
    rollup=protocol.validate_history(rows,state)
    assert rollup['main_teachers']==state['counters']['supervised_tokens']
    assert rollup['modified_learning_evaluations']==(rollup['main_teachers'] if arm=='scalegrad' else 0)
    control=build('native_CE_control')
    control_rows=[control.step() for _ in range(3)]
    control_state=host(control.state_dict())
    assert all(protocol.matched_original(state,control_state).values())
    assert protocol.paired_history(rows,control_rows)
    changed=copy.deepcopy(rows)
    changed[0]['token_digest']='0'*64
    with pytest.raises(ValueError): protocol.paired_history(changed,control_rows)
    control_state['progress_head']['weight'][0,0]=1.
    assert not protocol.matched_original(state,control_state)['genuine_zero_head_CE_control']


@pytest.mark.parametrize('bad',['combined','forwards','novel','teachers','physical','nonfinite','metric'])
def test_earlier_history_corruption_cannot_hide_behind_unchanged_final_state(tmp_path,bad):
    parent,build=builders(tmp_path)
    old=build(legacy=True)
    current=ScaleGradTrainer(parent,old.sampler,old.binding,batch=6,device='cpu')
    rows=[current.step() for _ in range(3)]
    state=host(current.state_dict())
    if bad=='combined': rows[0]['combined_loss']+=1.
    elif bad=='forwards': rows[0]['decoder_forwards_this_update']=2
    elif bad=='novel': rows[0]['novel_gold_positions_this_update']+=1
    elif bad=='teachers': rows[0]['CE_targets_this_update']+=1
    elif bad=='physical': rows[0]['physical_inputs_this_update']=0
    elif bad=='nonfinite': rows[0]['ScaleGrad_loss']=float('nan')
    else: rows[0]['total_CE_evaluations']=0
    with pytest.raises(ValueError): protocol.validate_history(rows,state)


def test_quality_requires_BOTH_matched25M_and_original_guards_never_adopts(monkeypatch):
    args=[{} for _ in range(9)]
    monkeypatch.setattr(protocol,'quality_gates',lambda *a:dict(passed=False))
    monkeypatch.setattr(protocol,'original_quality',lambda *a:dict(eligible=True))
    assert not protocol.pilot_quality(*args)['eligible_for_separately_defined_main_comparison']
    monkeypatch.setattr(protocol,'quality_gates',lambda *a:dict(passed=True))
    assert protocol.pilot_quality(*args)['eligible_for_separately_defined_main_comparison']
    monkeypatch.setattr(protocol,'original_quality',lambda *a:dict(eligible=False))
    r=protocol.pilot_quality(*args)
    assert not r['eligible_for_separately_defined_main_comparison']
    assert r['Base_qualified'] is r['Base_adopted'] is False


def test_science_builder_loads_original_parent_never_control_or_probe_weights(monkeypatch):
    calls=[]
    parent=object()
    monkeypatch.setattr(runner.torch,'load',lambda path,**kw:(calls.append(path),parent)[1])
    monkeypatch.setattr(runner,'Tokenizer',lambda path:object())
    source=dict(pool='fixture',manifest_sha256='m')
    monkeypatch.setattr(runner,'OriginalTrainCorpusSampler',lambda *a,**k:SimpleNamespace(binding=source))
    monkeypatch.setattr(runner,'ScaleGradTrainer',lambda actual,sampler,b,**k:(actual,b,k))
    c=dict(parent=dict(path='original10B'),tokenizer=dict(path='codec'),source_binding=source,goals=runner.GOALS,
        control_checkpoint=dict(path='CONTROL_NOT_INITIALIZER'))
    actual,b,kw=runner.build(c,dict(weights_role='scientific_scalegrad25M'))
    assert actual is parent and calls==['original10B'] and kw['batch']==48 and kw['seed']==42
