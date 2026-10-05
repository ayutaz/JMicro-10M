import importlib.util
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import run_dataset_expansion as study
from run_eos_short_pilot import routes
from jmicro.eos_pilot import pilot_lr

def test_shared_1b_route_has_same_short_tokens_in_both_halves():
    c=study.settings();routing=routes(c['updates_per_arm'],6102)
    assert len(routing)*c['tokens_per_update']==1000013824
    assert sum(routing[:15259])==sum(routing[15259:])==3051
    assert sum(routing)*c['tokens_per_update']==199950336

def test_new_schedule_decays_only_after_stable_and_reaches_floor():
    c=study.settings();parent=305176
    spec=dict(pilot_schedule=dict(parent_update=parent,stable_updates=c['stable_updates'],decay_updates=c['decay_updates']))
    assert pilot_lr(spec,parent+29000)==1
    assert .1<pilot_lr(spec,parent+29001)<1
    assert pilot_lr(spec,c['final_update'])==.1
    assert c['stable_updates']+c['decay_updates']==c['updates_per_arm']
