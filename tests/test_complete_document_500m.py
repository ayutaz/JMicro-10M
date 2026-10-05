from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_complete_document_500m import candidate_plan
from run_story20_budget import budget_plan
from run_eos_short_pilot import routes


def test_single_candidate_keeps_scientific_budget_and_schedule_equal_to_saved_controls():
    base=budget_plan({'parent':{'tokens_seen':10000007168,'update':305176},'peak_lr':.0001},'old','oldhash')
    changed=candidate_plan(base,'new','newhash')
    assert list(changed['arms'])==['whole20']
    assert changed['scientific_total_tokens']==changed['tokens_per_arm']==500006912
    assert changed['stable_updates']+changed['decay_updates']==changed['updates_per_arm']==15259
    assert changed['final_tokens']==10500014080 and changed['final_update']==320435
    assert sum(routes(15259,changed['arms']['whole20']['short_updates']))*32768==99975168
    assert changed['peak_lr']==base['peak_lr']==.0001
    assert base['pool']['pool']=='old' and changed['pool']['pool']=='new'


def test_primary_and_conditional_full_budget_do_not_retrain_saved_controls():
    changed=candidate_plan(budget_plan({},'old','oldhash'),'new','newhash')
    assert changed['screen_gpu_budget_seconds']==changed['full_gpu_budget_seconds']==1800
    assert changed['total_GPU_budget_seconds']==3600
    assert len(changed['arms'])==1
