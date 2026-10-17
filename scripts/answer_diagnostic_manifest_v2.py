"""Explicit packaging repair; original failed probe remains closed and counted.

The inherited native trainer hashes its data directory/manifest.json at save.
The first wrapper omitted that file and failed at its first save after two
technical updates. No scientific learning or saved checkpoint existed. This
separate runtime prepares/binds the missing manifest before preflight; it
changes no record, labels, parent, LR, geometry, teacher budget or quality gate.
"""
import argparse
import copy
from pathlib import Path
import answer_diagnostic as original
from answer_learning_common import ROOT,RUN,DATA,save,ref,bound,read_json,sha256,now
from phase6_performance import alive

CONFIG=ROOT/'configs/phase7/answer-diagnostic-manifest-v2-20261017.json'
DIRECTORY=RUN/'diagnostic-manifest-v2'
OLD_CONFIG=ROOT/'configs/phase7/answer-diagnostic-20261017.json'
OLD_DIRECTORY=RUN/'diagnostic'
original.CONFIG=CONFIG
original.DIRECTORY=DIRECTORY


def prepare():
    assert not CONFIG.exists()
    old=read_json(OLD_CONFIG);job=read_json(OLD_DIRECTORY/'job.json')
    ledger=read_json(OLD_DIRECTORY/'GPU_ledger.json')
    assert job['status']=='failed' and not alive(job)
    assert len(ledger['entries'])==1 and ledger['entries'][0]['stage']=='probe' and ledger['entries'][0]['status']=='failed'
    assert not list(OLD_DIRECTORY.glob('*.pt')) and not (OLD_DIRECTORY/'metrics.jsonl').exists()
    assert all(sha256(ROOT/p)==value for p,value in old['source_sha256'].items())
    for key in ('records','cases','CPU_replay','parent','tokenizer','semantic_review','reused_maximum_shape_evidence'):bound(old[key])
    manifest=DATA/'manifest.json';assert not manifest.exists()
    save(manifest,dict(format='TRAIN-only-reviewed32-diagnostic-manifest-v1',created_at=now(),
        records=old['records'],cases=old['cases'],tokenizer=old['tokenizer'],
        sampler_binding=read_json(bound(old['CPU_replay']))['sampler_binding'],vocab_size=4096,
        protected_TEST_used=False,role='Required native checkpoint provenance field; no numerical training input'))
    c=copy.deepcopy(old)
    c.update(created_at=now(),execution_runtime='required_manifest_packaging_v2',data_manifest=ref(manifest),
        failed_probe=ref(OLD_DIRECTORY/'GPU_ledger.json'),previous_config=ref(OLD_CONFIG),
        initial_probe_failure=ref(OLD_DIRECTORY/'job.json'),
        inherited_probe_seconds=ledger['total_seconds'],no_condition_or_quality_rescue=True,
        failure_scope='Missing data/manifest.json at first checkpoint save, two in-memory technical steps; science0, saved state0')
    for name in ('scripts/answer_diagnostic_manifest_v2.py','scripts/inspect_answer_diagnostic_manifest_v2.py','scripts/run_answer_diagnostic_manifest_v2.ps1'):
        c['source_sha256'][name]=sha256(ROOT/name)
    save(CONFIG,c);DIRECTORY.mkdir(parents=True,exist_ok=True)
    carried=copy.deepcopy(ledger);carried['limits']=c['limits_seconds']
    carried['carried_from_closed_technical_wrapper']=ref(OLD_DIRECTORY/'GPU_ledger.json')
    save(DIRECTORY/'GPU_ledger.json',carried)
    save(RUN/'diagnostic_packaging_repair.json',dict(created_at=now(),old_config=ref(OLD_CONFIG),new_config=ref(CONFIG),
        old_job=ref(OLD_DIRECTORY/'job.json'),old_GPU_ledger=ref(OLD_DIRECTORY/'GPU_ledger.json'),
        data_manifest=ref(manifest),scientific_updates_before_failure=0,technical_steps_before_first_save_failure=2,
        no_original_failed_job_relaunch=True,numerical_records_and_recipe_unchanged=True,
        old_cost_carried_in_full=ledger['total_seconds'],new_GPU_or_science_started=False))
    inspect();print('Separate manifest packaging fixed and bound; failed probe cost carried, science0')


def inspect():
    c=original.inspect();bound(c['data_manifest']);bound(c['previous_config']);bound(c['failed_probe'])
    assert c['execution_runtime']=='required_manifest_packaging_v2'
    old=read_json(OLD_CONFIG)
    for key in ('spec','teacher_budget','maximum_updates','maximum_teacher_length','max_new_tokens',
                'seed','limits_seconds','records','cases','CPU_replay','acceptance','parent','tokenizer','implementation'):
        assert c[key]==old[key],key
    return c


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=('prepare','inspect','run'));a=p.parse_args()
    if a.mode=='prepare':prepare()
    elif a.mode=='inspect':inspect();print('Bound manifest and frozen numerical diagnostic contract pass')
    else:inspect();original.run()
