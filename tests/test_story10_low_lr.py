from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_story10_low_lr import lower_plan
from run_eos_short_pilot import routes


def test_lowerLR_preserves_parent_source_tokens_and_original_schedule():
    original=dict(peak_lr=.0002,parent={'sha256':'same'},pool={'pool':'accepted','manifest_sha256':'fixed'},
                  updates_per_arm=3052,stable_updates=2900,decay_updates=152,tokens_per_arm=100007936)
    planned=lower_plan(original)
    assert original['peak_lr']==.0002 and planned['peak_lr']==.0001
    assert all(planned[k]==original[k] for k in ('parent','pool','updates_per_arm','stable_updates','decay_updates','tokens_per_arm'))
    assert planned['scientific_total_tokens']==2*planned['tokens_per_arm']


def test_matched_control_contains_no_story_but_has_same_total_updates():
    planned=lower_plan(dict(pool={'pool':'accepted','manifest_sha256':'fixed'}))
    control=routes(3052,planned['arms']['web']['short_updates'])
    treated=routes(3052,planned['arms']['coherent10']['short_updates'])
    assert len(control)==len(treated)==3052 and sum(control)==0 and sum(treated)==305
