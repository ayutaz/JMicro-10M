from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from run_complete_text_comparison import arm_binding
from run_eos_short_pilot import routes
from run_eos_complete_100m import adoption_checks


def test_same_parent_but_distinct_data_bindings_and_balanced_routes():
    plan={'arms':{'web':{'manifest_sha256':'old'}, 'short20':{'manifest_sha256':'old'},
                  'coherent20':{'manifest_sha256':'new'}}}
    binding={'parent':{'sha256':'parent'},'peak_lr':.0002}
    branches=[arm_binding(binding,plan,a) for a in plan['arms']]
    assert all(b['parent']==binding['parent'] for b in branches)
    assert len({b['arm'] for b in branches})==3
    assert branches[2]['short_manifest_sha256']!=branches[1]['short_manifest_sha256']
    path=routes(3052,610)
    assert sum(path)==610 and len(path)==3052
    assert sum(routes(3052,0))==0
    # Mixture routing changes learning source, not total token budget.
    assert sum(path)*32768==19988480


def test_eos_improvement_cannot_waive_raw_failures_or_loss_regression():
    control={'greedy_rates':dict(eos=0,repetition=53,empty=0,role_leak=0,unicode_failure=0),
             'body':{'bpb':1.0},'generation':{'outputs':[]}}
    candidate={'greedy_rates':dict(eos=20,repetition=40,empty=0,role_leak=0,unicode_failure=1),
               'body':{'bpb':1.02},'generation':{'outputs':[{'stop_reason':'stop_id','text':'。'}]}}
    checks=adoption_checks(control,candidate)
    assert checks['EOS_at_least8_more'] and checks['repetition_no_worse']
    assert not checks['no_empty_role_unicode']
    assert not checks['BPB_degradation_at_most1percent']
    assert not checks['no_punctuation_only_stops']
