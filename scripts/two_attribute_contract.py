"""Independent, finite contract for TRAIN64 capability diagnosis and regression."""
from contextlib import contextmanager
import json
import time
from pathlib import Path
from prepare_two_attribute_train import ROOT,RUN,DATA,OLD,BUDGET,PLAN
from answer_learning_common import save,ref,bound,read_json,sha256,now
from jmicro.tokenizer import Tokenizer
from jmicro.training import gpu_lock,implementation_hashes
from phase6_performance import identity

CONFIG=ROOT/'configs/phase7/chat-two-attribute-20261018.json'
LIMITS=dict(probe=600.,training=1800.,diagnosis=1800.,regression=10800.)
SOURCES=('scripts/prepare_two_attribute_train.py','scripts/prepare_two_attribute_dev.py','scripts/two_attribute_contract.py',
         'scripts/run_two_attribute_diagnosis.py','scripts/run_two_attribute_diagnosis.ps1','scripts/inspect_two_attribute_diagnosis.py')

def freeze():
    assert not CONFIG.exists() and not (RUN/'GPU_ledger.json').exists()
    old=read_json(OLD);manifest=read_json(DATA/'manifest.json');dev=read_json(DATA/'DEV.json')
    assert dev['TRAIN_manifest']==ref(DATA/'manifest.json') and manifest['created_at']<dev['created_at']
    sources=tuple(dict.fromkeys(tuple(old['source_sha256'])+SOURCES))
    for name,digest in old['source_sha256'].items():assert sha256(ROOT/name)==digest,name
    save(CONFIG,dict(format='two-attribute-capability-v1',created_at=now(),plan=ref(PLAN),old_config=ref(OLD),
        source_sha256={name:sha256(ROOT/name) for name in sources},implementation=implementation_hashes(),
        parent=old['parent'],tokenizer=old['tokenizer'],spec=old['spec'],parameter_count=10001152,teacher_budget=BUDGET,
        maximum_teacher_length=32,max_new_tokens=32,limits_seconds=LIMITS,TRAIN_manifest=ref(DATA/'manifest.json'),
        records=manifest['records'],TRAIN_review=manifest['review'],replay=manifest['replay'],DEV=ref(DATA/'DEV.json'),
        DEV_preparation=ref(RUN/'DEV_preparation.json'),DEV_review=ref(RUN/'DEV_review.json'),
        suites=old['suites'],public100=old['public100'],reused_maximum_shape=old['reused_maximum_shape'],
        previous_completion=ref(ROOT/'reports/phase7/chat-recovery-20261018/input-structure-main/completion.json'),
        previous_GPU_ledger=ref(ROOT/'reports/phase7/chat-recovery-20261018/input-structure-main/GPU_ledger.json'),
        diagnostic_gates=dict(TRAIN_values=64,TRAIN_stop=64,TRAIN_UTF8_role_trim=0,unseen_values_content=24,unseen_structure_content=24,own_final_context=12),
        quality_gates=old['quality_gates'],regression_baselines='Previous same GPU BF16/math C0 and C1; not new matched small-curriculum arms',
        expected_diagnosis_responses=240,expected_regression_responses=1733,protected_TEST_used=False,new_TEST_created=False,
        Chat_adopted=False,Base_adopted=False))
    preflight()

def preflight():
    c=read_json(CONFIG)
    assert c['format']=='two-attribute-capability-v1' and c['limits_seconds']==LIMITS and c['teacher_budget']==BUDGET
    assert c['parameter_count']==10001152 and c['implementation']==implementation_hashes()
    assert c['source_sha256']=={name:sha256(ROOT/name) for name in c['source_sha256']}
    for name in ('plan','old_config','parent','tokenizer','TRAIN_manifest','records','TRAIN_review','replay','DEV','DEV_preparation','DEV_review','public100','reused_maximum_shape','previous_completion','previous_GPU_ledger'):bound(c[name])
    old=read_json(bound(c['old_config']));assert c['spec']==old['spec'] and c['parent']==old['parent'] and c['quality_gates']==old['quality_gates']
    assert all(not c[k] for k in ('protected_TEST_used','new_TEST_created','Chat_adopted','Base_adopted'))
    for value in c['suites'].values():bound(value)
    m=read_json(bound(c['TRAIN_manifest']));dev=read_json(bound(c['DEV']))
    assert m['created_at']<dev['created_at'] and dev['TRAIN_manifest']==c['TRAIN_manifest']
    qa=read_json(bound(c['DEV_review']));assert qa['DEV']==c['DEV'] and qa['all80_directly_read'] and len(qa['judgments'])==80 and all(r['accepted'] for r in qa['judgments'])
    rows=[json.loads(l) for l in bound(c['records']).read_text().splitlines()]
    assert len(rows)==len({r['doc_id'] for r in rows})==64 and all(r['split']=='train' for r in rows)
    tok=Tokenizer(bound(c['tokenizer']));return dict(c,config_sha256=sha256(CONFIG)),tok,rows

@contextmanager
def stage(category,config_hash):
    with gpu_lock('cuda'):
        path=RUN/'GPU_ledger.json';ledger=read_json(path) if path.exists() else dict(limits_seconds=LIMITS,entries=[])
        assert ledger['limits_seconds']==LIMITS and not any(r['status']=='running' for r in ledger['entries'])
        cap=LIMITS[category]-sum(r['seconds'] for r in ledger['entries'] if r['category']==category);assert cap>30
        started=time.monotonic();row=dict(**identity(),category=category,status='running',seconds=0.,started_at=now(),config_sha256=config_hash,remaining_at_start=cap);ledger['entries'].append(row)
        def left():return cap-(time.monotonic()-started)
        def beat(**values):row.update(values,seconds=time.monotonic()-started,heartbeat_at=now());save(path,ledger)
        beat()
        try:yield left,beat;row['status']='complete'
        except BaseException as error:row.update(status='failed_or_interrupted',error=repr(error));raise
        finally:
            row.update(seconds=time.monotonic()-started,ended_at=now());ledger['total_seconds']=sum(r['seconds'] for r in ledger['entries']);save(path,ledger)
            if left()<0:raise TimeoutError('Frozen stage cap exceeded')

if __name__=='__main__':freeze()
