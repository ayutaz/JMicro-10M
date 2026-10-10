"""Audit real terminal SFT checkpoints/counters, not a quality certification."""
import math
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,sha256,write_json,now
from run_chat_first_sft import preflight,SOURCES
from chat_first_contract import RUN,parent_state
from phase6_performance import alive,finite_state
from run_eos_short_pilot import equal_state


def run():
    torch.set_num_threads(2)
    config=ROOT/'configs/phase7/chat_first_sft.json'
    c,_,_=preflight(config)
    parent=parent_state(c);job=read_json(RUN/'job.json');result=read_json(RUN/'result.json')
    assert job['status']=='complete' and not alive(job)
    assert result['status']=='learning_complete_pending_Chat_quality'
    assert result['config_sha256']==job['config_sha256']==sha256(config)
    assert result['Base_adopted'] is result['Chat_adopted'] is False
    assert result['root_Base']==result['model_parent']==c['parent'] and result['purpose']=='chat_first_diagnostic'
    assert 0<job['training_GPU_elapsed_seconds']<=3600 and 0<job['GPU_elapsed_seconds']<=4200
    gate=read_json(RUN/'resume-gate/result.json');gate_job=read_json(RUN/'resume-gate/job.json')
    assert gate_job['status']=='complete' and not alive(gate_job) and 0<gate_job['GPU_elapsed_seconds']<=600
    assert gate_job['config_sha256']==gate['config_sha256']==sha256(config)
    assert gate['passed'] and len(gate['checks'])==19 and all(gate['checks'].values()) and gate['GPU_optimizer_updates']==8
    assert gate==result['resume_gate']
    states=[torch.load(RUN/'resume-gate'/f'{branch}.pt',map_location='cpu',weights_only=False) for branch in ('continuous','resumed')]
    assert all(equal_state(states[0][k],states[1][k]) for k in ('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes','token_digest','lineage','update','spec'))
    del states
    for source,digest in c['source_sha256'].items(): assert sha256(RUN/'source'/source)==digest
    refs=result['checkpoints'];assert set(refs)=={'epoch1','epoch2','epoch3'}
    verified={}
    for n in (1,2,3):
        ref=refs[f'epoch{n}'];path=Path(ref['path'])
        assert path.parent==RUN and sha256(path)==ref['sha256']
        state=torch.load(path,map_location='cpu',weights_only=False);assert finite_state(state)
        assert state['model_config']==parent['model_config'] and state['implementation_sha256']==c['implementation']
        assert all(k in state for k in ('optimizer','scheduler','rng','sampler','token_digest','lineage','body_bytes'))
        assert state['lineage']['base_checkpoint']==c['parent'] and state['lineage']['optimizer_policy']=='fresh'
        assert state['lineage']['local_counter_policy']=='SFT counters start at zero; Base exposure is recorded separately'
        assert {k:v for k,v in state['spec'].items() if k!='assistant_training'}==c['spec']
        sampler=state['sampler']
        assert state['update']==ref['update'] and state['supervised_tokens']==sampler['teacher_tokens']==ref['Assistant_teachers']
        assert state['tokens']==sampler['input_tokens'] and sampler['series_tokens']==ref['series_tokens']
        assert sampler['series_tokens']==sampler['input_tokens']+sampler['examples']
        assert sampler['examples']==sampler['eot_teachers']==ref['examples']
        assert sampler['physical_tokens']==state['update']*1024*c['spec']['batch']
        assert n*40366<=sampler['examples']<n*40366+c['spec']['batch']
        verified[f'epoch{n}']=dict(ref,complete_state_verified=True,parameter_config_unchanged=True)
        if n==3:
            assert state['update']==c['spec']['schedule_updates']
            assert sampler['examples']==121098 and sampler['series_tokens']==30567471 and state['supervised_tokens']==1899555
            assert state['token_digest'] and sampler==result['full_sampler']
            assert equal_state(state['lineage'],result['Base_lineage'])
            assert result['checkpoint']==str(path) and result['checkpoint_sha256']==ref['sha256']
            final_state=state
    with (RUN/'metrics.jsonl').open() as stream:
        import json
        rows=[json.loads(line) for line in stream]
    assert len(rows)==final_state['update'] and [r['update'] for r in rows]==list(range(1,len(rows)+1))
    assert all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) and 0<r['lr']<=1e-4 for r in rows)
    assert rows[-1]['assistant_teacher_tokens']==1899555 and rows[-1]['series_tokens']==30567471 and rows[-1]['EOT_teachers']==121098
    assert rows[-1]['token_digest']==final_state['token_digest']
    assert math.isclose(sum(r['seconds'] for r in rows),result['training_step_seconds'],rel_tol=1e-12)
    report=dict(status='terminal_three_pass_learning_audited_quality_pending',verified_at=now(),config_sha256=sha256(config),
        result_sha256=sha256(RUN/'result.json'),job_sha256=sha256(RUN/'job.json'),metrics_sha256=sha256(RUN/'metrics.jsonl'),
        CUDA_resume_exact_all19=True,checkpoints=verified,TRAIN_passes=3,Assistant_teacher_tokens=1899555,
        EOT_teachers=121098,series_tokens=30567471,parameter_count=10001152,Base_adopted=False,Chat_adopted=False,
        protected_test_used=False,quality_evaluated=False)
    write_json(RUN/'training_audit.json',report);print('Verified terminal3-pass full checkpoints, all metrics/counters and CUDA resume; quality pending')


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);run()
