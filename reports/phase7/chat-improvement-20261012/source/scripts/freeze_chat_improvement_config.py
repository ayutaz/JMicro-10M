"""Freeze runnable plan131 bindings only after TRAIN and independent DEV."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json,implementation_hashes
from chat_improvement_contract import RUN,B,LIMITS,preflight,reference

SOURCES=('src/jmicro/teacher_chat_training.py','src/jmicro/assistant_sampler.py','src/jmicro/tokenizer.py',
    'src/jmicro/chat_evaluation.py','src/jmicro/chat_review.py','src/jmicro/japanese_evaluation.py',
    'scripts/chat_improvement_contract.py','scripts/run_chat_improvement.py','scripts/run_chat_improvement.ps1',
    'scripts/evaluate_chat_improvement.py','scripts/check_chat_improvement_launch.py','scripts/freeze_chat_improvement_config.py',
    'scripts/chat_first_contract.py','scripts/phase6_performance.py','scripts/run_eos_short_pilot.py',
    'scripts/prepare_chat_improvement_dev.py','scripts/prepare_chat_improvement_nll.py','scripts/audit_chat_improvement_dev.py')


def main():
    path=ROOT/'configs/phase7/chat-improvement-20261012.json'
    assert not path.exists(),'Frozen config exists; inspect rather than overwrite'
    data=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-improvement-20261012')
    rpc=Path('/home/aihub_ubuntu/jmicro-data/phase7/real-persona-pilot-20261006')
    dry=read_json(RUN/'consumption_dry_run.json')
    c=dict(format='teacher-chat-improvement-v1',purpose='direct_SFT_diagnostic_from_unadopted_original10B',
        created_at=now(),teacher_budget=B,GPU_limits_seconds=LIMITS,GPU_total_limit_seconds=21600,
        parameter_count=10001152,stop_after_stage=5,implementation=implementation_hashes(),
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
            for name,directory in (('C0',rpc),('C1',data))},
        Base_adopted=False,Chat_adopted=False,protected_TEST_used=False)
    atomic_json(path,c)
    preflight(path);print('Frozen runnable contract passed CPU preflight: '+str(path))

if __name__=='__main__':main()
