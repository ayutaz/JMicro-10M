"""CPU reconciliation: preserve measurements, account exact reuse, keep6h cap."""
import ast
import copy
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json
from jmicro.chat_review import content_review
from chat_generalization_contract import RUN,LIMITS,preflight,reference
from prepare_chat_generalization_reuse import functions
from review_chat_generalization import get_items,fingerprint
from phase6_performance import alive


def main():
    c,_,_=preflight(ROOT/'configs/phase7/chat-generalization-20261013.json')
    archive=RUN/'pre_gpu_contract_v2';old=read_json(archive/'config.json');oldsha=sha256(archive/'config.json')
    for key in ('parent','tokenizer','implementation','spec','arms','new_DEV','old_suite','fixed_NLL','teacher_budget'):
        assert c[key]==old[key],key
    for source,digest in old['source_sha256'].items():
        if source not in ('scripts/chat_generalization_contract.py','scripts/run_chat_generalization.py',
                          'scripts/evaluate_chat_generalization.py','scripts/freeze_chat_generalization_config.py'):
            assert sha256(ROOT/source)==digest,source
    for filename,names in (('run_chat_generalization.py',('trainer','one_resume_gate','cuda_resume','train_arm')),
                            ('evaluate_chat_generalization.py',('load_cases','checkpoint','nll_batch','nll_windows','fixed_nll','summarize','chat'))):
        before=functions(archive/filename);after=functions(ROOT/'scripts'/filename)
        assert all(before[k]==after[k] for k in names),'Numerical/inference algorithm changed'
    assert sum(LIMITS.values())==sum(old['GPU_limits_seconds'].values())==21600
    ledger=read_json(RUN/'GPU_ledger.json');assert ledger==read_json(archive/'GPU_ledger.json')
    assert all(r['status']!='running' and not alive(r) for r in ledger['entries'])
    original_time=sum(r['charged_seconds'] for r in ledger['entries'])
    ledger['allocation_history']=[dict(previous_limits=ledger['limits'],source_config=reference(archive/'config.json'),
        reason='All required actual evaluations retained; original main-learning forecast fits2400s. Reallocate to evaluation before learning.',
        old_failed_forecast=reference(archive/'evaluation_forecast.json'),changed_at=now())]
    ledger['limits']=LIMITS;assert sum(r['charged_seconds'] for r in ledger['entries'])==original_time
    atomic_json(RUN/'GPU_ledger.json',ledger)
    # Original successful GPU tests are re-bound only after checking unchanged
    # parent/data/Trainer/numerical algorithms. Historical measured work stays.
    for name in ('native_probe.json','native_resume_gate.json'):
        record=read_json(archive/name);assert record['passed'] and record['config_sha256']==oldsha
        record['config_sha256']=c['config_sha256'];record['original_GPU_evidence']=reference(archive/name)
        record['CPU_rebinding']=dict(unchanged_numerical_algorithms=True,new_GPU_optimizer_updates=0,at=now())
        if name=='native_probe.json':
            d1=record['arms']['D1'];assert d1['forecast_training_seconds']<=LIMITS['train_D1']
            d1['forecast_limit_seconds']=LIMITS['train_D1'];d1['within_limit']=True
        atomic_json(RUN/name,record)
    for name in ('job.json','result.json'):
        record=read_json(RUN/'D0'/name);assert record['config_sha256']==oldsha
        record['config_sha256']=c['config_sha256'];record['previous_CPU_registration']=reference(archive/'D0'/name)
        atomic_json(RUN/'D0'/name,record)
    for path in sorted((RUN/'evaluation').rglob('result.json')):
        ev,items=get_items(path);assert ev['binding']['config_sha256']==oldsha
        notes=read_json(path.with_name('notes.json'));content_review(ev,sha256(path),notes,items)
        original=copy.deepcopy(items);priorpath=archive/path.relative_to(RUN)
        ev['binding'].update(config_sha256=c['config_sha256'],source_sha256=c['source_sha256'])
        ev['previous_CPU_registration']=reference(priorpath);atomic_json(path,ev)
        _,newitems=get_items(path);assert all(fingerprint(original[k])==fingerprint(newitems[k]) for k in items)
        notes['evaluation_sha256']=sha256(path);notes['previous_CPU_registration']=reference(priorpath.with_name('notes.json'))
        atomic_json(path.with_name('notes.json'),notes)
        atomic_json(path.with_name('review.json'),content_review(ev,sha256(path),notes,newitems))
        atomic_json(path.with_name('recipe.json'),ev['binding'])
        job=read_json(path.with_name('job.json'));job['binding']=ev['binding'];atomic_json(path.with_name('job.json'),job)
    registration=read_json(RUN/'historical_control_registration.json')
    assert registration['passed'] and registration['old_suite_judgments_reused']==876
    registration['config_sha256']=c['config_sha256'];atomic_json(RUN/'historical_control_registration.json',registration)
    source=read_json(archive/'evaluation_forecast.json');assert not source['passed'] and source['config_sha256']==oldsha
    outputs=10*2*219+3*2*219-876
    batches=10*math.ceil(2554/32)-4*(math.ceil(2554/32)-math.ceil(304/32))
    # Preserve the exact measured maximum rate,1.5 margin,27 cold invocations and
    #600s reserve; never infer shorter answers or drop any quality judgments.
    rate=max(r['seconds_per_token'] for r in source['timings'][1:])
    generation=rate*64*outputs*1.5
    nll=max(source['NLL_batch_seconds'][1:])*batches*1.5
    total=generation+nll+source['cold_overhead_seconds']+600
    accepted=dict(source,config_sha256=c['config_sha256'],passed=total<=LIMITS['evaluation'],
        original_failed_forecast=reference(archive/'evaluation_forecast.json'),
        maximum_required_responses=outputs,conservative_generation_seconds=generation,
        conservative_NLL_seconds=nll,maximum_new_NLL_batches=batches,verified_historical_outputs_reused=876,
        forecast_evaluation_seconds=total,limit_seconds=LIMITS['evaluation'],
        conditional_sampling_and_recovery_both_reserved=True,new_GPU_measurements=0,
        measurements_reused_without_numerical_change=True,completed_at=now())
    assert accepted['passed'],(total,LIMITS['evaluation'])
    atomic_json(RUN/'evaluation_forecast.json',accepted)
    atomic_json(RUN/'budget_reconciliation.json',dict(passed=True,created_at=now(),
        config_sha256=c['config_sha256'],source_sha256=sha256(Path(__file__)),
        previous_config=reference(archive/'config.json'),previous_failed_forecast=reference(archive/'evaluation_forecast.json'),
        GPU_charged_seconds_preserved=original_time,total_GPU_cap=21600,current_category_caps=LIMITS,
        new_Greedy_outputs=2190,conditional_sampling_outputs=1314,conditional_recovery_outputs=1314,
        both_conditional_branches_retained=True,NLL_batches_upper_bound=batches,
        measured_forecast_seconds=total,main_training_before_reconciliation=0,
        all_raw_and_judgments_preserved=True,quality_gates_weakened=False))
    print(f'CPU reconciliation passed: all conditional branches, {outputs} new outputs, {batches} NLL batches; {total:.3f}s /{LIMITS["evaluation"]:.0f}s; total cap6h')


if __name__=='__main__':main()
