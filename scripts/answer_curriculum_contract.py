"""Separate prospective contract; frozen earlier experiments remain unchanged."""
from contextlib import contextmanager
import json
import time
from answer_learning_common import ROOT,RUN as PARENT_RUN,save,ref,bound,read_json,sha256,now
from prepare_answer_curriculum import DIRECTORY as DATA
from jmicro.training import implementation_hashes,gpu_lock
from jmicro.tokenizer import Tokenizer
from phase6_performance import identity

RUN=PARENT_RUN/'curriculum-main'
CONFIG=ROOT/'configs/phase7/answer-curriculum-20261017.json'
BUDGET=1000000
SUITES=('new','previous_new','lr','semantic','generalization','original')
LIMITS=dict(probe=600.,train_C0=3600.,train_C1=3600.,evaluation=10800.)
SPEC=dict(seed=42,context=1024,batch=32,accumulation=1,lr=1e-4,weight_decay=.01,warmup=0,
    schedule_updates=100000,dtype='bf16',compile=False,backend='math',scheduler='wsd',sampler='document',
    training_fast_path=False,update_teachers=512)
SOURCES=('scripts/answer_curriculum_contract.py','scripts/run_answer_curriculum.py','scripts/run_answer_curriculum.ps1',
    'scripts/inspect_answer_curriculum.py','scripts/run_chat_natural.py','scripts/evaluate_chat_natural.py',
    'scripts/chat_natural_contract.py','scripts/phase6_performance.py','scripts/answer_learning_common.py',
    'scripts/prepare_answer_curriculum.py','src/jmicro/model.py','src/jmicro/training.py','src/jmicro/tokenizer.py',
    'src/jmicro/assistant_sampler.py','src/jmicro/teacher_chat_training.py','src/jmicro/chat_evaluation.py',
    'scripts/start_webui.ps1','scripts/stop_webui.ps1')


def read_dev(value):
    from pathlib import Path
    path=Path(value['path']).resolve()
    assert path.parent==(DATA/'dev_suites').resolve() and path.name in {s+'.jsonl' for s in SUITES}
    rows=[json.loads(line) for line in bound(value).read_text().splitlines()]
    contexts=[r for r in rows if len(r['messages'])>1]
    assert len(rows)==80 and len({r['family_id'] for r in rows})==80 and all(r['split']=='dev' for r in rows)
    assert len(contexts)==24 and sum(sum(m['role']=='user' for m in r['messages']) for r in contexts)==59
    return rows,contexts


def freeze():
    assert not CONFIG.exists(),'Do not refreeze an executed or frozen condition'
    manifest=read_json(DATA/'manifest.json');dev=read_json(PARENT_RUN/'curriculum_DEV_preparation.json')
    old=read_json(ROOT/'configs/phase7/chat-natural-sft-20261017.json')
    assert manifest['status']=='TRAIN_frozen_before_new_DEV' and dev['TRAIN_frozen_before_new_DEV']
    assert dev['TRAIN_manifest']==ref(DATA/'manifest.json') and tuple(dev['suites'])==SUITES
    save(CONFIG,dict(format='answer-curriculum-v1',created_at=now(),plan=ref(ROOT/'docs/153_answer_curriculum_comparison.md'),
        parent=old['parent'],tokenizer=old['tokenizer'],parameter_count=10001152,implementation=implementation_hashes(),
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},spec=SPEC,teacher_budget=BUDGET,limits_seconds=LIMITS,
        maximum_teacher_length=32,final_overshoot_maximum=31,max_new_tokens=32,quality_gates=old['quality_gates'],
        TRAIN_manifest=ref(DATA/'manifest.json'),DEV_preparation=ref(PARENT_RUN/'curriculum_DEV_preparation.json'),
        NLL=dev['NLL'],NLL_targets=320,suites=dev['suites'],arms=manifest['arms'],
        baseline_config=ref(ROOT/'configs/phase7/chat-natural-sft-20261017.json'),
        reused_maximum_shape=ref(ROOT/'reports/phase7/chat-natural-sft-20261017/native_gate.json'),
        supplement=ref(DATA/'supplement_unique_TRAIN.json'),preparation=manifest['preparation'],
        probe=dict(timing_updates_per_arm=16,resume_updates_per_branch=2,branches=2,all_numeric_fields_compared=True),
        comparison=dict(primary_point=BUDGET,savepoints=[250000,500000,1000000],final_suites=12,
            final_content_judgments=2628,intermediate_diagnostic_responses=40,paired_family_CI_bootstrap_seed=42,
            bootstrap_replicates=2000,improved_new_content_CI_lower_gt=0,
            matched='New same-Base1e-4 control versus new50percent-answer-curriculum1e-4 candidate',
            historical3e_5_not_matched=True,alias_not_new_semantic_diversity=True,
            source_objective_individual_causal_effect_not_identified=True),
        formal_Base_retention_pending=True,protected_TEST_used=False,new_TEST_created=False,Chat_adopted=False,Base_adopted=False))
    print('Frozen '+str(ref(CONFIG)))


def preflight(load_records=True):
    c=read_json(CONFIG)
    assert c['format']=='answer-curriculum-v1' and c['spec']==SPEC and c['limits_seconds']==LIMITS
    assert c['teacher_budget']==BUDGET and c['implementation']==implementation_hashes()
    assert c['maximum_teacher_length']==c['max_new_tokens']==32 and c['final_overshoot_maximum']==31
    assert c['parameter_count']==10001152 and tuple(c['suites'])==SUITES
    assert c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    assert not any(c[k] for k in ('protected_TEST_used','new_TEST_created','Chat_adopted','Base_adopted'))
    for key in ('plan','parent','tokenizer','TRAIN_manifest','DEV_preparation','NLL','baseline_config',
        'reused_maximum_shape','supplement','preparation'):bound(c[key])
    old=read_json(bound(c['baseline_config']))
    assert c['parent']==old['parent'] and c['tokenizer']==old['tokenizer'] and c['quality_gates']==old['quality_gates']
    gate=read_json(bound(c['reused_maximum_shape']));assert gate['passed']
    assert gate['arms']['C0']['maximum_shape']['shape']==[32,1024]
    manifest=read_json(bound(c['TRAIN_manifest']));assert manifest['arms']==c['arms']
    dev=read_json(bound(c['DEV_preparation']));assert dev['TRAIN_frozen_before_new_DEV'] and dev['final_responses']==2628
    tok=Tokenizer(bound(c['tokenizer']))
    for value in c['suites'].values():
        rows,_=read_dev(value);assert all(tok.chat_prompt(r['messages'],992)[1]==0 for r in rows)
    arms={}
    for arm in ('C0','C1'):
        a=c['arms'][arm];bound(a['records']);dry=read_json(bound(a['dry_run']))
        assert dry['status']=='passed' and dry['records']==a['records'] and dry['sampler_binding']==a['sampler_binding']
        assert dry['all_teacher_masks_and_complete_roundtrips'] and dry['no_history_trim']
        if load_records:
            rows=[json.loads(line) for line in bound(a['records']).read_text().splitlines()]
            assert all(r['split']=='train' for r in rows) and len({r['doc_id'] for r in rows})==len(rows)
            arms[arm]=rows
    assert c['arms']['C0']['records']['sha256']==old['arms']['C1']['records']['sha256']
    if load_records:
        assert arms['C1'][:len(arms['C0'])]==arms['C0']
        originals={r['doc_id']:r for r in read_json(bound(c['supplement']))}
        for row in arms['C1'][len(arms['C0']):]:
            original=originals[row['semantic_original_id']]
            assert row['messages']==original['messages'] and row['target_message_indices']==original['target_message_indices']
    return dict(c,config_sha256=sha256(CONFIG)),tok,arms


@contextmanager
def stage(category,config_hash):
    with gpu_lock('cuda'):
        path=RUN/'GPU_ledger.json';ledger=read_json(path) if path.exists() else dict(limits_seconds=LIMITS,entries=[])
        assert ledger['limits_seconds']==LIMITS and not any(r['status']=='running' for r in ledger['entries'])
        cap=LIMITS[category]-sum(r['seconds'] for r in ledger['entries'] if r['category']==category)
        assert cap>30
        started=time.monotonic();row=dict(**identity(),category=category,status='running',seconds=0.,
            started_at=now(),config_sha256=config_hash,remaining_at_start=cap);ledger['entries'].append(row)
        def left():return cap-(time.monotonic()-started)
        def beat(**values):row.update(values,seconds=time.monotonic()-started,heartbeat_at=now());save(path,ledger)
        beat()
        try:yield left,beat;row['status']='complete'
        except BaseException as e:row.update(status='failed_or_interrupted',error=repr(e));raise
        finally:
            row.update(seconds=time.monotonic()-started,ended_at=now());ledger['total_seconds']=sum(r['seconds'] for r in ledger['entries']);save(path,ledger)
            if left()<0:raise TimeoutError('Frozen stage cap exceeded; retain condition without rescue')


if __name__=='__main__':freeze()
