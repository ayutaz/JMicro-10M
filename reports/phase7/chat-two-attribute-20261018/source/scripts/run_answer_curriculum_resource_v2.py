"""Prospective resource-only replan under existing unlimited cumulative authorization.

Keep original closed35c14f6f wrapper and its failed forecast intact. All
numerical data/teachers/quality settings stay identical; every new technical
step is durably recorded before any subsequent forecast assertion.
"""
import copy
import json
from answer_learning_common import ROOT,RUN as PARENT_RUN,save,ref,bound,read_json,now
import answer_curriculum_contract as contract
import run_answer_curriculum as original
from phase6_performance import alive

OLD_CONFIG=contract.CONFIG
OLD_RUN=contract.RUN
CONFIG=ROOT/'configs/phase7/answer-curriculum-resource-v2-20261017.json'
RUN=PARENT_RUN/'curriculum-main-resource-v2'
LIMITS=dict(contract.LIMITS,train_C0=7200.,train_C1=7200.)
contract.CONFIG=CONFIG;contract.RUN=RUN;contract.LIMITS=LIMITS
contract.SOURCES=contract.SOURCES+('scripts/run_answer_curriculum_resource_v2.py',
    'scripts/inspect_answer_curriculum_resource_v2.py','scripts/run_answer_curriculum_resource_v2.ps1')
original.CONFIG=CONFIG;original.RUN=RUN;original.LIMITS=LIMITS
unobserved_build=original.build
build_number=0


def observed_build(parent,c,tok,rows):
    global build_number
    trainer=unobserved_build(parent,c,tok,rows);build_number+=1;number=build_number
    step=trainer.step
    def observed_step(*args,**kwargs):
        result=step(*args,**kwargs)
        with (RUN/'technical_all_steps.jsonl').open('a') as stream:
            stream.write(json.dumps(dict(build=number,**result),allow_nan=False)+'\n');stream.flush()
        return result
    trainer.step=observed_step
    return trainer


original.build=observed_build


def prepare():
    assert not CONFIG.exists() and not (RUN/'GPU_ledger.json').exists()
    old=read_json(OLD_CONFIG);job=read_json(OLD_RUN/'pipeline.json');ledger=read_json(OLD_RUN/'GPU_ledger.json')
    assert job['status']=='failed' and not alive(job) and job['config_sha256']==ref(OLD_CONFIG)['sha256']
    assert len(ledger['entries'])==1 and ledger['entries'][0]['category']=='probe' and ledger['entries'][0]['technical_update']==16
    assert ledger['entries'][0]['status']=='failed_or_interrupted' and not (OLD_RUN/'C0/result.json').exists()
    assert '4882.053283151938' in job['error'] and not (OLD_RUN/'native_gate.json').exists()
    assert not list(OLD_RUN.glob('*.pt')) and not list(OLD_RUN.glob('*/metrics.jsonl'))
    assert old['source_sha256']=={p:contract.sha256(ROOT/p) for p in old['source_sha256']}
    estimate=4882.053283151938
    c=copy.deepcopy(old)
    c.update(created_at=now(),limits_seconds=LIMITS,resource_replan=ref(ROOT/'docs/154_curriculum_resource_replan.md'),
        source_sha256={p:contract.sha256(ROOT/p) for p in contract.SOURCES},
        previous_closed_config=ref(OLD_CONFIG),previous_failed_job=ref(OLD_RUN/'pipeline.json'),
        previous_GPU_ledger=ref(OLD_RUN/'GPU_ledger.json'),inherited_probe_seconds=ledger['total_seconds'],
        previous_C0_forecast_seconds=estimate,previous_3600_condition_stays_failed=True,
        resource_rationale='Existing user unlimited cumulative local GPU authorization; correct self-imposed time planning before science, keep finite7200 per arm',
        preserved_numerical_and_quality_fields=['spec','teacher_budget','parent','tokenizer','arms','TRAIN_manifest','DEV_preparation','NLL','suites','quality_gates'],
        all_technical_step_history_written_before_forecast=True)
    for key in c['preserved_numerical_and_quality_fields']:assert c[key]==old[key]
    save(CONFIG,c);RUN.mkdir(parents=True,exist_ok=True)
    carried=copy.deepcopy(ledger);carried['limits_seconds']=LIMITS;carried['carried_closed_cost_source']=ref(OLD_RUN/'GPU_ledger.json')
    save(RUN/'GPU_ledger.json',carried)
    save(PARENT_RUN/'curriculum_resource_replan.json',dict(created_at=now(),old_config=ref(OLD_CONFIG),new_config=ref(CONFIG),
        old_failed_job=ref(OLD_RUN/'pipeline.json'),old_forecast_seconds=estimate,
        candidate_same_old_rate_forecast_seconds=(estimate-300)*3901/3048+300,
        carried_probe_seconds=ledger['total_seconds'],science_updates_before_replan=0,
        time_plan_explicitly_revised=True,numerical_quality_fields_unchanged=True))
    contract.preflight(load_records=False)
    print('Resource-v2 frozen; original failed wrapper closed, full5.505592s carried, all science/quality settings equal')


if __name__=='__main__':
    import sys
    if sys.argv[1:] == ['prepare']:prepare()
    else:original.main()
