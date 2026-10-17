"""Separate immutable contract for the same-answer input-structure comparison."""
from contextlib import contextmanager
import json
import time
from pathlib import Path
from answer_learning_common import ROOT,save,ref,bound,read_json,now,sha256
from prepare_chat_recovery_train_v3 import original as preparation
from jmicro.tokenizer import Tokenizer
from jmicro.training import implementation_hashes,gpu_lock
from phase6_performance import identity

PARENT_RUN=ROOT/'reports/phase7/chat-recovery-20261018'
RUN=PARENT_RUN/'input-structure-main'
DATA=preparation.DATA
CONFIG=ROOT/'configs/phase7/chat-input-structure-20261018.json'
BASE_CONFIG=ROOT/'configs/phase7/answer-curriculum-resource-v2-20261017.json'
BASE_SHA='e9172f65215fe44f2a94f5c0e9f1429175a27917b3d32b3e09c848cb318e9e46'
BUDGET=1000000
SUITES=('new','curriculum','previous_new','lr','semantic','generalization','original')
SPEC=read_json(BASE_CONFIG)['spec']
LIMITS=dict(probe=600.,train_C0=7200.,train_C1=7200.,evaluation=10800.)
OWN_SOURCES=('scripts/chat_recovery_contract.py','scripts/run_chat_recovery_sft.py','scripts/run_chat_recovery_sft.ps1',
             'scripts/inspect_chat_recovery_sft.py','scripts/prepare_chat_recovery_train.py','scripts/prepare_chat_recovery_train_v2.py',
             'scripts/prepare_chat_recovery_train_v3.py','scripts/prepare_chat_recovery_dev.py')


def read_dev(value):
    path=Path(value['path']).resolve()
    assert path.parent==(DATA/'dev_suites').resolve() and path.name in {name+'.jsonl' for name in SUITES}
    rows=[json.loads(line) for line in bound(value).read_text().splitlines()]
    contexts=[r for r in rows if len(r['messages'])>1]
    assert len(rows)==len({r['family_id'] for r in rows})==80 and all(r['split']=='dev' for r in rows)
    assert len(contexts)==24 and sum(sum(m['role']=='user' for m in r['messages']) for r in contexts)==59
    return rows,contexts


def freeze():
    assert sha256(BASE_CONFIG)==BASE_SHA and not CONFIG.exists() and not (RUN/'GPU_ledger.json').exists()
    old=read_json(BASE_CONFIG);manifest=read_json(DATA/'manifest.json');dev=read_json(PARENT_RUN/'DEV_preparation.json')
    assert manifest['exact_paired_teacher_streams'] and manifest['status']=='TRAIN_frozen_before_new_DEV'
    assert dev['TRAIN_manifest']==ref(DATA/'manifest.json') and dev['TRAIN_frozen_before_new_DEV']
    assert tuple(dev['suites'])==SUITES and dev['total_main_responses']==3466 and dev['NLL_targets']==432
    sources=tuple(dict.fromkeys(tuple(old['source_sha256'])+OWN_SOURCES))
    for name,value in old['source_sha256'].items():assert sha256(ROOT/name)==value
    save(CONFIG,dict(format='chat-input-structure-v1',created_at=now(),plan=ref(ROOT/'docs/160_chat_input_structure_sft_comparison.md'),
        diagnosis=ref(PARENT_RUN/'diagnostic_analysis.json'),sampling=ref(PARENT_RUN/'sampling_notes.json'),base_config=ref(BASE_CONFIG),
        source_sha256={name:sha256(ROOT/name) for name in sources},implementation=implementation_hashes(),parameter_count=10001152,
        parent=old['parent'],tokenizer=old['tokenizer'],spec=SPEC,teacher_budget=BUDGET,final_overshoot_maximum=31,
        maximum_teacher_length=32,max_new_tokens=32,limits_seconds=LIMITS,TRAIN_manifest=ref(DATA/'manifest.json'),
        TRAIN_preparation=ref(PARENT_RUN/'input-v3-preparation/TRAIN_proposal_receipt.json'),
        TRAIN_QA=ref(PARENT_RUN/'input-v3-preparation/TRAIN_pattern_review.json'),arms=manifest['arms'],
        DEV_preparation=ref(PARENT_RUN/'DEV_preparation.json'),suites=dev['suites'],NLL=dev['NLL'],NLL_targets=432,
        public100=ref(ROOT/'reports/phase7/chat-quality-100-20261017/cases.json'),
        reused_maximum_shape=old['reused_maximum_shape'],quality_gates=old['quality_gates'],
        comparison=dict(primary_point=BUDGET,savepoints=[250000,500000,1000000],final_suites=14,
            final_suite_responses=3066,public100_responses=400,total_main_responses=3466,
            GPU_evaluation_precision='BF16/math for both new arms, including public100; old CPU diagnostic kept separately',
            intervention='Authored input layout only; same targets/order/LR/source quotas',
            paired_family_CI_bootstrap_seed=42,bootstrap_replicates=2000,improved_new_content_CI_lower_gt=0,
            no_counts_regression_suites=list(SUITES[1:]),absolute_screen_from_original_recipe=True,
            semantic_factors_not_individually_identified=True,finite_template_limitations_retained=True),
        practical=dict(new_CPU_ports={'C1':7866,'C0':7867},conversations_per_arm=3,turns_per_conversation=6,CPU_wall_cap_seconds=1800,
            actual_browser_required=True,old_UI_kept=True),
        previous_GPU_ledgers=[ref(Path(old['arms']['C1']['dry_run']['path']).parent/'curriculum-main-resource-v2/GPU_ledger.json')],
        protected_TEST_used=False,new_TEST_created=False,Chat_adopted=False,Base_adopted=False))
    preflight(False)


def preflight(load_records=True):
    c=read_json(CONFIG);assert sha256(BASE_CONFIG)==BASE_SHA
    assert c['format']=='chat-input-structure-v1' and c['spec']==SPEC and c['limits_seconds']==LIMITS
    assert c['implementation']==implementation_hashes() and c['parameter_count']==10001152 and c['teacher_budget']==BUDGET
    assert c['source_sha256']=={name:sha256(ROOT/name) for name in c['source_sha256']}
    assert c['maximum_teacher_length']==c['max_new_tokens']==32 and tuple(c['suites'])==SUITES
    for key in ('plan','diagnosis','sampling','base_config','parent','tokenizer','TRAIN_manifest','TRAIN_preparation','TRAIN_QA','DEV_preparation','NLL','public100','reused_maximum_shape'):bound(c[key])
    old=read_json(bound(c['base_config']))
    assert all(c[k]==old[k] for k in ('parent','tokenizer','spec','quality_gates','implementation'))
    assert all(not c[k] for k in ('protected_TEST_used','new_TEST_created','Chat_adopted','Base_adopted'))
    qa=read_json(bound(c['TRAIN_QA']));assert qa['all256_reviewed'] and len(qa['judgments'])==256
    proposal=read_json(bound(c['TRAIN_preparation']))
    assert qa['proposal']==c['TRAIN_preparation'] and qa['QA_sha256']==proposal['QA_patterns']['sha256']
    bound(proposal['QA_patterns']);bound(proposal['records']);bound(proposal['wrapper']);bound(proposal['prior_wrapper']);bound(proposal['source'])
    gate=read_json(bound(c['reused_maximum_shape']));assert gate['passed'] and gate['arms']['C0']['maximum_shape']['shape']==[32,1024]
    manifest=read_json(bound(c['TRAIN_manifest']));assert manifest['exact_paired_teacher_streams'] and manifest['arms']==c['arms']
    dev=read_json(bound(c['DEV_preparation']));assert dev['TRAIN_manifest']==c['TRAIN_manifest'] and dev['TRAIN_frozen_before_new_DEV']
    assert manifest['created_at']<dev['created_at'] and dev['NLL']==c['NLL'] and dev['suites']==c['suites']
    for value in c['previous_GPU_ledgers']:bound(value)
    a=read_json(bound(c['arms']['C0']['dry_run']));b=read_json(bound(c['arms']['C1']['dry_run']))
    for key in ('updates','actual_teachers','physical_microbatches','history','windows','consumed_source_teachers','teacher_stream_sha256','ordered_doc_IDs_sha256'):assert a[key]==b[key]
    assert a['updates']==1929 and a['actual_teachers']==1000000 and c['arms']['C0']['records']['sha256']==old['arms']['C1']['records']['sha256']
    tok=Tokenizer(bound(c['tokenizer']));arms={}
    for value in c['suites'].values():
        rows,_=read_dev(value);assert all(tok.chat_prompt(row['messages'],992)[1]==0 for row in rows)
    for arm in ('C0','C1'):
        bound(c['arms'][arm]['records']);dry=read_json(bound(c['arms'][arm]['dry_run']))
        assert dry['status']=='passed' and dry['records']==c['arms'][arm]['records'] and dry['sampler_binding']==c['arms'][arm]['sampler_binding']
        assert dry['all_teacher_masks_and_complete_roundtrips'] and dry['no_history_trim']
        if load_records:
            rows=[json.loads(line) for line in bound(c['arms'][arm]['records']).read_text().splitlines()]
            assert all(row['split']=='train' for row in rows) and len({row['doc_id'] for row in rows})==len(rows)
            arms[arm]=rows
    return dict(c,config_sha256=sha256(CONFIG)),tok,arms


@contextmanager
def stage(category,config_hash):
    with gpu_lock('cuda'):
        path=RUN/'GPU_ledger.json';ledger=read_json(path) if path.exists() else dict(limits_seconds=LIMITS,entries=[])
        assert ledger['limits_seconds']==LIMITS and not any(row['status']=='running' for row in ledger['entries'])
        cap=LIMITS[category]-sum(row['seconds'] for row in ledger['entries'] if row['category']==category);assert cap>30
        started=time.monotonic();row=dict(**identity(),category=category,status='running',seconds=0.,started_at=now(),config_sha256=config_hash,remaining_at_start=cap);ledger['entries'].append(row)
        def left():return cap-(time.monotonic()-started)
        def beat(**values):row.update(values,seconds=time.monotonic()-started,heartbeat_at=now());save(path,ledger)
        beat()
        try:yield left,beat;row['status']='complete'
        except BaseException as error:row.update(status='failed_or_interrupted',error=repr(error));raise
        finally:
            row.update(seconds=time.monotonic()-started,ended_at=now());ledger['total_seconds']=sum(r['seconds'] for r in ledger['entries']);save(path,ledger)
            if left()<0:raise TimeoutError('Frozen stage cap exceeded; preserve failed condition')


if __name__=='__main__':freeze()
