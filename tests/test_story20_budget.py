from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_story20_budget import budget_plan
from run_eos_short_pilot import routes


def plan():
    return budget_plan(dict(parent={'tokens_seen':10000007168,'update':305176},peak_lr=.0001),'expanded','fixed')


def test500M_budgets_are_equal_and_do_not_count_verification_or_branches_as_one_model():
    p=plan()
    assert p['tokens_per_arm']==p['updates_per_arm']*32768==500006912
    assert p['scientific_total_tokens']==2*p['tokens_per_arm']==1000013824
    assert p['final_tokens']==p['parent']['tokens_seen']+p['tokens_per_arm']
    assert p['final_update']==p['parent']['update']+p['updates_per_arm']


def test_intermediate_is_same_schedule_not_reheated_decayed100M_branch():
    p=plan()
    assert p['stable_updates']+p['decay_updates']==p['updates_per_arm']
    assert p['intermediate_update']-p['parent']['update']==3052<p['stable_updates']
    assert p['intermediate_tokens']-p['parent']['tokens_seen']==p['intermediate_additional_tokens']==100007936


def test_both_arms_and_both_budgets_share_fixed_pool():
    p=plan();routing=routes(p['updates_per_arm'],p['arms']['coherent20']['short_updates'])
    assert sum(routing)==3051 and sum(routing[:3052])==610
    assert sum(routing)*32768==99975168
    assert all(a['pool']=='expanded' and a['manifest_sha256']=='fixed' for a in p['arms'].values())


def test_scientific_plus_full_evaluation_budget_is_bounded():
    p=plan()
    assert p['screen_gpu_budget_seconds']+p['full_gpu_budget_seconds']==p['total_GPU_budget_seconds']==7200
