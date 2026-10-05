from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_story20_low_lr import next_plan
from run_eos_short_pilot import routes


def base():
    return dict(pool={'pool':'accepted','manifest_sha256':'fixed'},peak_lr=.0001,parent={'sha256':'same'},
                updates_per_arm=3052,stable_updates=2900,decay_updates=152,tokens_per_arm=100007936,
                final_update=308228,final_tokens=10100015104,arms={'web':{},'coherent10':{}})


def test_preserves_parent_LR_total_and_schedule():
    original=base();planned=next_plan(original)
    for key in ('parent','peak_lr','pool','updates_per_arm','stable_updates','decay_updates','tokens_per_arm','final_update','final_tokens'):
        assert planned[key]==original[key]
    assert list(original['arms'])==['web','coherent10']


def test_only_candidate_trained_and_existing_control_reused():
    planned=next_plan(base())
    assert list(planned['arms'])==['coherent20']
    assert planned['scientific_total_tokens']==planned['tokens_per_arm']


def test_actual_story_and_web_consumption_fit_existing_pool():
    planned=next_plan(base());routing=routes(3052,planned['arms']['coherent20']['short_updates'])
    assert len(routing)==3052 and sum(routing)==610
    assert sum(routing)*32768==19988480<25000067
    assert (len(routing)-sum(routing))*32768==80019456


def test_frozen_bounded_screen_and_full_budget():
    planned=next_plan(base())
    assert planned['screen_gpu_budget_seconds']==900
    assert planned['full_gpu_budget_seconds']==3000
