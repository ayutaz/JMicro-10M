"""Audit all completed scientific state and every update against actual CPU replay."""
import argparse
import json
import math
import torch
from run_answer_curriculum_resource_v2 import CONFIG,RUN,contract
from answer_learning_common import save,ref,bound,read_json,now
from phase6_performance import finite_state,alive


def audit(arm):
    target=RUN/arm/'training_audit.json'
    if target.exists():
        prior=read_json(target);assert prior['passed'] and prior['config']==ref(CONFIG);bound(prior['checkpoint']);return prior
    c=read_json(CONFIG);result=read_json(RUN/arm/'result.json');job=read_json(RUN/arm/'job.json')
    assert result['status']==job['status']=='learning_complete' and result['config_sha256']==job['config_sha256']==ref(CONFIG)['sha256']
    ledger=read_json(RUN/'GPU_ledger.json');stages=[r for r in ledger['entries'] if r['category']=='train_'+arm]
    assert stages and stages[-1]['status']=='complete' and not any(r['status']=='running' for r in stages)
    state=torch.load(bound(result['checkpoint']),map_location='cpu',weights_only=False)
    dry=read_json(bound(c['arms'][arm]['dry_run']));history=[json.loads(line) for line in (RUN/arm/'metrics.jsonl').read_text().splitlines()]
    assert len(history)==state['update']==dry['updates'] and state['sampler']==result['sampler']==dry['sampler_terminal']
    assert state['implementation_sha256']==c['implementation'] and state['lineage']==result['lineage']
    assert state['lineage']['base_checkpoint']==c['parent'] and state['lineage']['optimizer_policy']=='fresh'
    assert state['lineage']['RNG_policy']=='new frozen seed' and all(state['spec'][k]==v for k,v in c['spec'].items())
    assert state['spec']['teacher_chat']['budget']==1000000 and state['spec']['teacher_chat']['data_binding']==c['arms'][arm]['sampler_binding']
    assert state['shard_manifest_sha256']==c['TRAIN_manifest']['sha256']
    assert finite_state(state) and {'model','optimizer','scheduler','rng','sampler'}<=state.keys()
    assert {'python','numpy','torch','cuda'}==state['rng'].keys() and len(state['rng']['cuda'])==1
    assert state['rng']['torch'].dtype==torch.uint8 and len(state['optimizer']['state'])==119
    assert all(int(s['step'])==state['update'] for s in state['optimizer']['state'].values())
    assert state['scheduler']['last_epoch']==state['update']
    cumulative=0
    for number,(actual,expected) in enumerate(zip(history,dry['history'],strict=True),1):
        assert actual['update']==expected['update']==number
        assert all(actual[k]==expected[k] for k in ('teachers_this_update','microbatches','lr'))
        cumulative+=actual['teachers_this_update']
        assert cumulative==actual['supervised_tokens']==actual['assistant_teacher_tokens']==expected['teachers']
        assert all(math.isfinite(actual[k]) for k in ('loss','gradient_norm','lr','seconds'))
        assert actual['seconds']>0 and actual['gradient_norm']>=0
        assert actual['series_tokens']==actual['tokens_seen']+actual['examples']
        assert actual['EOT_teachers']==actual['examples'] and actual['removed_turns']==0
        assert actual['physical_input_tokens']==actual['tokens_seen']+actual['padding_input_tokens']
    last=history[-1];assert state['supervised_tokens']==cumulative==result['checkpoint']['Assistant_teachers']==dry['actual_teachers']
    assert state['tokens']==last['tokens_seen'] and state['body_bytes']==last['body_bytes_seen'] and state['token_digest']==last['token_digest']
    assert all(group['lr']==last['lr'] for group in state['optimizer']['param_groups'])
    assert 1000000<=cumulative<=1000031 and set(result['checkpoints'])=={'250000','500000','1000000'}
    for key,point in result['checkpoints'].items():
        bound(point);assert int(key)<=point['Assistant_teachers']<=int(key)+542
    value=dict(passed=True,created_at=now(),config=ref(CONFIG),checkpoint=result['checkpoint'],updates=state['update'],
        Assistant_teachers=cumulative,finite_all_typed_state=True,all119_Adam_steps_exact=True,
        full_history_same_teacher_batching_and_LR_as_CPU=True,sampler_terminal_exact=True,
        EOT_teachers=state['sampler']['eot_teachers'],valid_inputs=state['tokens'],physical_inputs=state['sampler']['physical_tokens'],
        source_teacher_fractions=dry['actual_consumed_source_fractions'],
        maximum_semantic_target_exposure=dry['maximum_semantic_target_exposures'],
        actual_training_step_seconds=sum(r['seconds'] for r in history),metrics=ref(RUN/arm/'metrics.jsonl'),
        owning_pipeline_alive_during_audit=alive(job),arm_training_stage_closed=True,
        source=ref(__file__),quality_evidence=False,protected_TEST_used=False)
    save(target,value);print(json.dumps(value,ensure_ascii=False));return value


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('arm',choices=['C0','C1']);audit(p.parse_args().arm)
