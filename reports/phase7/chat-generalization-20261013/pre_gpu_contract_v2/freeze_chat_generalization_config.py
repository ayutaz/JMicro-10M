"""Freeze runnable plan133 bindings only after TRAIN and independent DEV."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json,implementation_hashes
from chat_generalization_contract import RUN,B,LIMITS,preflight,reference

SOURCES=('src/jmicro/teacher_chat_training.py','src/jmicro/assistant_sampler.py','src/jmicro/tokenizer.py',
    'src/jmicro/chat_evaluation.py','src/jmicro/chat_review.py','src/jmicro/japanese_evaluation.py',
    'scripts/chat_generalization_contract.py','scripts/run_chat_generalization.py','scripts/run_chat_generalization.ps1',
    'scripts/evaluate_chat_generalization.py','scripts/check_chat_generalization_launch.py','scripts/freeze_chat_generalization_config.py',
    'scripts/chat_first_contract.py','scripts/phase6_performance.py','scripts/run_eos_short_pilot.py',
    'scripts/prepare_chat_generalization_dev.py','scripts/prepare_chat_generalization_nll.py','scripts/audit_chat_generalization_dev.py',
    'src/jmicro/chat_generalization_curriculum.py','scripts/prepare_chat_generalization_train.py',
    'scripts/finalize_chat_generalization_train.py','scripts/dry_run_chat_generalization.py',
    'scripts/prepare_chat_improvement_train.py','scripts/dry_run_chat_improvement.py',
    'scripts/review_chat_generalization_train.py','scripts/prepare_chat_generalization_reuse.py',
    'scripts/review_chat_generalization.py','scripts/audit_chat_generalization_training.py',
    'scripts/compare_chat_generalization.py','scripts/analyze_chat_generalization_results.py')


def main():
    path=ROOT/'configs/phase7/chat-generalization-20261013.json'
    assert not path.exists(),'Frozen config exists; inspect rather than overwrite'
    data=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-generalization-20261013')
    rpc=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-improvement-20261012')
    dry=read_json(RUN/'consumption_dry_run.json')
    c=dict(format='teacher-chat-generalization-v1',purpose='direct_SFT_diagnostic_from_unadopted_original10B',
        created_at=now(),teacher_budget=B,GPU_limits_seconds=LIMITS,GPU_total_limit_seconds=21600,
        parameter_count=10001152,stop_after_stage=4,implementation=implementation_hashes(),
        historical_control_evidence=reference(RUN/'historical_control_preparation.json'),
        recovery_predicate=dict(final_point='t3',both_suites_joint_at_least=56,
            both_suites_matched_provided_context_at_least=15,all_primary_mechanical_gates=True,
            new_joint_improvement_over_D0_required=True,own_history_failure_required=True,
            policy='Only if every predicate holds; otherwise record not triggered, never relax gates'),
        efficiency_separate=True,all_requested_GPU_stages_total_cap_seconds=21600,
        parent=reference(ROOT/'reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt'),
        tokenizer=reference(ROOT/'artifacts/phase2/4096/tokenizer.model'),new_DEV=reference(data/'dev.jsonl'),
        old_suite=reference(ROOT/'eval/chat.jsonl'),fixed_NLL=reference(data/'nll_fixed.jsonl'),
        source_sha256={s:sha256(ROOT/s) for s in SOURCES},
        preparation_evidence={name:reference(RUN/file) for name,file in dict(consumption='consumption_dry_run.json',
            review='train_content_review_final.json',DEV_audit='dev_audit.json',NLL='nll_preparation.json',
            DEV='dev_preparation.json',TRAIN='train_preparation.json').items()},
        spec=dict(seed=42,context=1024,batch=32,accumulation=1,lr=1e-4,weight_decay=.01,warmup=0,
            schedule_updates=100000,dtype='bf16',compile=False,backend='math',scheduler='wsd',sampler='document',
            training_fast_path=False,update_teachers=512),
        arms={name:dict(data_directory=str(directory),records=reference(directory/'train.jsonl'),
            manifest=reference(directory/'manifest.json'),sampler_binding=dry[name]['sampler_binding'])
            for name,directory in (('D0',rpc),('D1',data))},
        Base_adopted=False,Chat_adopted=False,protected_TEST_used=False)
    atomic_json(path,c)
    preflight(path);print('Frozen runnable contract passed CPU preflight: '+str(path))

if __name__=='__main__':main()
