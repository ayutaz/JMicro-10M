"""Verify completed full states and every measured update against CPU replay."""
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from chat_natural_contract import RUN,CONFIG,SPEC,BUDGET,ref,read_bound,require_ref
from jmicro.experiment import read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,finite_state


def audit(arm):
    target=RUN/arm/'training_audit.json'
    if target.exists():
        prior=read_json(target)
        assert prior['config']['sha256']==sha256(CONFIG) and prior['passed']
        return prior
    c=read_json(CONFIG)
    result=read_json(RUN/arm/'result.json');job=read_json(RUN/arm/'job.json')
    assert result['status']==job['status']=='learning_complete'
    ledger=read_json(RUN/'GPU_ledger.json')
    arm_stages=[entry for entry in ledger['entries'] if entry['category']=='train_'+arm]
    assert arm_stages and arm_stages[-1]['status']=='complete'
    assert not any(entry['category']=='train_'+arm and entry['status']=='running' for entry in ledger['entries'])
    assert result['config_sha256']==job['config_sha256']==sha256(CONFIG)
    value=result['checkpoint'];state=torch.load(require_ref(value),map_location='cpu',weights_only=False)
    dry=read_bound(c['arms'][arm]['dry_run'])
    history=[json.loads(line) for line in (RUN/arm/'metrics.jsonl').read_text().splitlines()]
    assert len(history)==state['update']==dry['updates']==1921
    assert [r['update'] for r in history]==list(range(1,state['update']+1))
    assert state['sampler']==result['sampler']==dry['sampler_terminal']
    assert state['implementation_sha256']==c['implementation']
    assert state['lineage']==result['lineage'] and state['lineage']['base_checkpoint']==c['parent']
    assert state['lineage']['optimizer_policy']=='fresh' and state['lineage']['RNG_policy']=='new frozen seed'
    assert all(state['spec'][k]==v for k,v in SPEC.items())
    assert state['spec']['teacher_chat']['budget']==BUDGET
    assert state['spec']['teacher_chat']['data_binding']==c['arms'][arm]['sampler_binding']
    assert finite_state(state)
    assert {'model','optimizer','scheduler','rng','sampler'}<=state.keys()
    assert {'python','numpy','torch','cuda'}==state['rng'].keys()
    assert len(state['rng']['cuda'])==1 and state['rng']['torch'].dtype==torch.uint8
    assert len(state['optimizer']['state'])==119
    assert all(int(s['step'])==state['update'] for s in state['optimizer']['state'].values())
    assert state['scheduler']['last_epoch']==state['update']
    cumulative=0
    for actual,expected in zip(history,dry['history'],strict=True):
        assert actual['update']==expected['update']
        assert actual['teachers_this_update']==expected['teachers_this_update']
        assert actual['microbatches']==expected['microbatches'] and actual['lr']==expected['lr']
        cumulative+=actual['teachers_this_update']
        assert cumulative==actual['supervised_tokens']==actual['assistant_teacher_tokens']==expected['teachers']
        assert all(math.isfinite(actual[k]) for k in ('loss','gradient_norm','lr','seconds'))
        assert actual['seconds']>0 and actual['gradient_norm']>=0
        assert actual['series_tokens']==actual['tokens_seen']+actual['examples']
        assert actual['EOT_teachers']==actual['examples'] and actual['removed_turns']==0
        assert actual['physical_input_tokens']==actual['tokens_seen']+actual['padding_input_tokens']
    last=history[-1]
    assert state['supervised_tokens']==cumulative==value['Assistant_teachers']==dry['actual_Assistant_teachers']
    assert state['tokens']==last['tokens_seen'] and state['token_digest']==last['token_digest']
    assert state['body_bytes']==last['body_bytes_seen']
    assert all(group['lr']==last['lr'] for group in state['optimizer']['param_groups'])
    assert BUDGET<=cumulative<=BUDGET+31
    points=result['checkpoints']
    assert set(points)=={'250000','500000','1000000'}
    for key,p in points.items():
        assert int(key)<=p['Assistant_teachers']<=int(key)+542
        require_ref(p)
    audit=dict(passed=True,created_at=now(),config=ref(CONFIG),checkpoint=value,updates=state['update'],
        full_typed_model_Adam_scheduler_RNG_sampler_retained=True,finite_model_and_all_Adam_tensors=True,
        full_history_same_teacher_batching_LR_as_CPU_replay=True,sampler_terminal_exact=True,
        metrics=ref(RUN/arm/'metrics.jsonl'),Assistant_teachers=cumulative,
        EOT_teachers=state['sampler']['eot_teachers'],valid_inputs=state['tokens'],
        physical_inputs=state['sampler']['physical_tokens'],maximum_target_exposure=dry['max_target_exposures'],
        actual_consumed_source_teachers=dry['actual_consumed_source_teachers'],
        actual_training_step_seconds=sum(r['seconds'] for r in history),checkpoints=points,
        raw_model_tensors=len(state['model']),Adam_parameter_states=len(state['optimizer']['state']),
        owning_pipeline_still_alive_during_audit=alive(job),arm_training_stage_closed=True,
        source=ref(Path(__file__)),quality_evidence=False,protected_TEST_used=False)
    atomic_json(target,audit)
    print(json.dumps({k:audit[k] for k in ('passed','updates','Assistant_teachers','EOT_teachers','actual_training_step_seconds')},ensure_ascii=False))
    return audit


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--arm',choices=('C0','C1'),required=True)
    audit(p.parse_args().arm)
