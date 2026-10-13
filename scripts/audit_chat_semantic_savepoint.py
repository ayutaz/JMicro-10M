"""CPU audit before evaluating a newly learned partial or final native point."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.teacher_chat_training import TeacherBudgetSampler
from jmicro.training import atomic_json
from chat_semantic_contract import RUN,B,preflight,require_ref,reference
from phase6_performance import alive,finite_state


def main():
    p=argparse.ArgumentParser();p.add_argument('--point',choices=('t1','t2','t3'),required=True);args=p.parse_args()
    c,tok,arms=preflight(ROOT/'configs/phase7/chat-semantic-diversity-20261013.json')
    directory=RUN/'S1';job=read_json(directory/'job.json')
    assert not alive(job) and job['config_sha256']==c['config_sha256']
    assert job['status'] in ('saved_for_planned_screen','learning_complete')
    ref=read_json(directory/'checkpoints.json')[args.point];path=require_ref(ref)
    state=torch.load(path,map_location='cpu',weights_only=False)
    assert finite_state(state) and state['implementation_sha256']==c['implementation']
    assert state['lineage']['base_checkpoint']==c['parent'] and state['lineage']['optimizer_policy']=='fresh'
    assert {k:state['spec'][k] for k in c['spec']}==c['spec']
    assert state['spec']['teacher_chat']['trainer_sha256']==c['source_sha256']['src/jmicro/teacher_chat_training.py']
    assert state['spec']['teacher_chat']['data_binding']==c['arms']['S1']['sampler_binding']
    assert state['update']==state['branch_updates']==ref['update']
    assert state['tokens']==state['branch_tokens']==ref['valid_inputs']
    assert state['shard_manifest_sha256']==c['arms']['S1']['manifest']['sha256']
    assert set(state['rng'])=={'python','numpy','torch','cuda'} and len(state['rng']['cuda'])==1
    assert state['optimizer']['state'] and all(int(v['step'].item())==ref['update'] for v in state['optimizer']['state'].values())
    assert state['scheduler']['last_epoch']==ref['update']
    metrics=[json.loads(l) for l in (directory/'metrics.jsonl').read_text().splitlines()][:ref['update']]
    dry=read_json(RUN/'S1_dry_run.json');expected=dry['rows'][:ref['update']]
    assert len(metrics)==len(expected)==ref['update']
    for actual,target in zip(metrics,expected,strict=True):
        assert (actual['update'],actual['teachers_this_update'],actual['lr'],actual['microbatches'])==(
            target['update'],target['teachers'],target['lr'],target['microbatches'])
        assert all(math.isfinite(actual[k]) for k in ('loss','gradient_norm','lr','seconds'))
    row=metrics[-1]
    assert state['supervised_tokens']==ref['Assistant_teachers']==row['assistant_teacher_tokens']
    assert state['scheduler']['_last_lr']==[row['lr']]*len(state['optimizer']['param_groups'])
    assert all(group['lr']==row['lr'] for group in state['optimizer']['param_groups'])
    assert ref['Assistant_teachers']>=ref['requested_teachers']
    assert len(metrics)==1 or metrics[-2]['assistant_teacher_tokens']<ref['requested_teachers']
    sampler=TeacherBudgetSampler(arms['S1'],tok,1024,42,B,update_teachers=512,microbatch=32)
    digest='00'*32
    for _ in range(ref['update']):
        batches,_,_=sampler.next_update();h=hashlib.sha256(bytes.fromhex(digest))
        for x,y in batches:
            h.update(x.numpy().astype('<i8').tobytes());h.update(y.numpy().astype('<i8').tobytes())
        digest=h.hexdigest()
    assert state['sampler']==sampler.state_dict()
    assert state['token_digest']==digest==row['token_digest']
    assert state['sampler']['physical_tokens']==ref['physical_inputs']==row['physical_input_tokens']
    atomic_json(directory/(args.point+'_audit.json'),dict(passed=True,created_at=now(),
        config_sha256=c['config_sha256'],checkpoint=ref,source_sha256=sha256(Path(__file__)),
        complete_state_and_native_binding=True,Adam_scheduler_RNG_present=True,
        actual_sampler_cursor_and_full_padded_stream_digest=True,finite_actual_metrics=True,
        first_completed_update_after_savepoint=True,quality_evidence=False))
    print(args.point+' actual full state/cursor/stream CPU audit passed')


if __name__=='__main__':main()
