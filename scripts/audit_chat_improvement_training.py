"""CPU audit of actual learned complete checkpoints against frozen consumption."""
import argparse
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.training import atomic_json
from chat_improvement_contract import RUN,B,preflight,require_ref,reference
from phase6_performance import finite_state,alive


def main():
    p=argparse.ArgumentParser();p.add_argument('--arm',choices=('C0','C1'),required=True);args=p.parse_args();arm=args.arm
    c,_,_=preflight(ROOT/'configs/phase7/chat-improvement-20261012.json')
    directory=RUN/arm;job=read_json(directory/'job.json');result=read_json(directory/'result.json')
    assert job['status']==result['status']=='learning_complete' and not alive(job) and result['config_sha256']==c['config_sha256']
    dry=read_json(RUN/(arm+'_dry_run.json'));points=read_json(directory/'checkpoints.json')
    assert set(points)=={'t1','t2','t3'} and points==result['checkpoints']
    metrics=[json.loads(l) for l in (directory/'metrics.jsonl').read_text().splitlines()]
    assert len(metrics)==dry['updates'] and [r['update'] for r in metrics]==list(range(1,len(metrics)+1))
    for actual,expected in zip(metrics,dry['rows'],strict=True):
        assert (actual['update'],actual['teachers_this_update'],actual['lr'],actual['microbatches'])==(
            expected['update'],expected['teachers'],expected['lr'],expected['microbatches'])
        assert all(math.isfinite(actual[k]) for k in ('loss','gradient_norm','lr','seconds')) and actual['seconds']>0
    checkpoint_checks={}
    for point,ref in points.items():
        require_ref(ref);state=torch.load(ref['path'],map_location='cpu',weights_only=False)
        assert finite_state(state) and state['implementation_sha256']==c['implementation']
        assert state['lineage']['base_checkpoint']==c['parent'] and state['lineage']['optimizer_policy']=='fresh'
        assert state['spec']['teacher_chat']['data_binding']==c['arms'][arm]['sampler_binding']
        assert state['spec']['teacher_chat']['trainer_sha256']==c['source_sha256']['src/jmicro/teacher_chat_training.py']
        row=metrics[ref['update']-1]
        assert state['supervised_tokens']==ref['Assistant_teachers']==row['assistant_teacher_tokens']
        assert state['tokens']==ref['valid_inputs']==row['valid_input_tokens'] and state['token_digest']==row['token_digest']
        assert state['sampler']['physical_tokens']==ref['physical_inputs']==row['physical_input_tokens']
        assert state['sampler']['eot_teachers']==ref['EOT_teachers']==row['EOT_teachers']
        assert ref['Assistant_teachers']>=ref['requested_teachers']
        if ref['update']>1:assert metrics[ref['update']-2]['assistant_teacher_tokens']<ref['requested_teachers']
        model=JMicroModel(state['model_config']);model.load_state_dict(state['model'],strict=True)
        assert sum(p.numel() for p in model.parameters())==10001152
        checkpoint_checks[point]=dict(reference=ref,complete_state=True,finite=True,parent_binding=True,first_completed_update_after_threshold=True)
        if point=='t3':
            assert state['sampler']==dry['sampler_terminal'] and state['sampler']==result['actual_sampler']
            assert state['supervised_tokens']==dry['Assistant_teachers']==B
            assert state['update']==dry['updates'] and state['tokens']==dry['valid_inputs']
        del state,model
    atomic_json(directory/'training_audit.json',dict(passed=True,config_sha256=c['config_sha256'],arm=arm,
        checkpoints=checkpoint_checks,metrics=reference(directory/'metrics.jsonl'),updates=len(metrics),
        Assistant_teachers=B,exact_dry_run_order_quantities_LR=True,all_optimizer_steps_finite=True,
        fresh_optimizer=True,parameter_count=10001152,quality_evidence=False,Base_adopted=False,Chat_adopted=False,completed_at=now()))
    print(arm+' actual learned full-state/consumption audit passed')

if __name__=='__main__':main()
