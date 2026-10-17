"""Pin reference assets or sample already allowed TRAIN inventories, never TEST."""
import argparse
from collections import Counter,defaultdict
import json
from pathlib import Path
import shutil
from urllib.request import urlopen
from answer_learning_common import ROOT,RUN,DATA,OLD_RUN,OLD_DATA,PIN,save,ref,bound,digest,read_json,sha256,now


def reference():
    target=RUN/'reference_preparation.json'
    assert not target.exists(),'Inspect and retain completed reference acquisition'
    with urlopen('https://huggingface.co/api/models/hisakata-ai/akebono-10m-chat',timeout=25) as response:
        api=json.load(response)
    assert api['sha']==PIN and not api.get('private') and not api.get('gated')
    original=ROOT/'reports/investigation/rebuild_20261010/reference'
    destination=DATA/'reference';destination.mkdir(parents=True,exist_ok=True)
    checks={line.split()[1]:line.split()[0] for line in (original/'SHA256SUMS').read_text().splitlines()}
    names=('chat.py','modeling_japanesechat10m.py','tokenizer.py','output_integrity.py','config.json',
           'runtime.json','LICENSE','LICENSE_STATUS.md','README.md','EVALUATION_SUMMARY.json','VERIFICATION.json','MANIFEST.json')
    for name in names:
        assert sha256(original/name)==checks[name]
        if (destination/name).exists():assert sha256(destination/name)==checks[name]
        else:shutil.copyfile(original/name,destination/name)
    receipt=dict(status='acquiring',observed_at=now(),repository=api['id'],revision=PIN,
        executable_source_reviewed=True,source_read_only=True,files={name:ref(destination/name) for name in names},
        protected_TEST_used=False,GPU_initialized=False,training_updates=0)
    save(RUN/'reference_acquisition_progress.json',receipt)
    from prepare_chat_natural_sources import download
    for name,limit in (('tokenizer.model',5000000),('model.safetensors',60000000)):
        receipt['files'][name]=download(f'https://huggingface.co/hisakata-ai/akebono-10m-chat/resolve/{PIN}/{name}',
            destination/name,checks[name],limit)
        save(RUN/'reference_acquisition_progress.json',receipt)
        print('Acquired and SHA-verified '+name,flush=True)
    dev=read_json(OLD_RUN/'DEV_preparation.json')['suites']['new']
    cases=[json.loads(line) for line in bound(dev).read_text().splitlines()]
    assert len(cases)==80 and all(c['split']=='dev' for c in cases)
    selected=[]
    for category in ('greeting','daily','question_back','correction','context'):
        rows=[c for c in cases if c['category']==category][:4]
        assert len(rows)==4
        selected.extend(rows)
    questions=RUN/'reference_questions.json'
    assert not questions.exists()
    save(questions,dict(source=dev,questions=selected,selected_before_reference_generation=True,
        selection='First4 in each of greeting,daily,question_back,correction,context;20 known DEV families',
        cpu_conditions=['Akebono_official','Akebono_cap32','JMicro_first_SFT_cap32','JMicro_C1_cap32'],
        maximum_seconds_per_condition=600,protected_TEST_used=False))
    receipt.update(status='complete',completed_at=now(),questions=ref(questions),no_generation_yet=True,
        code_policy='Reviewed original files copied byte-for-byte; adapt decoder only in separately named local driver')
    save(target,receipt)


def audit():
    target=RUN/'TRAIN_audit_sample.json'
    assert not target.exists(),'Do not redraw the prospectively selected sample'
    availability=read_json(OLD_RUN/'availability.json')
    identities=read_json(OLD_DATA/'RPC_allowed_identities.json')
    rpc_allowed={'real_persona_chat:'+name for name in identities['train']}
    reserved=set(read_json(OLD_DATA/'magpie_reserved_DEV_identities.json')['ids'])
    strata=defaultdict(list);totals=Counter();sources={}
    for source in ('RPC','magpie'):
        path=bound(availability['files'][source]);sources[source]=ref(path)
        assert path.parent==OLD_DATA and path.name==source+'_eligible_inventory.jsonl'
        with path.open() as stream:
            for line in stream:
                row=json.loads(line)
                assert row['split']=='train' and row['source']==source
                assert row['doc_id'] in rpc_allowed if source=='RPC' else row['doc_id'].startswith('magpie:') and row['doc_id'] not in reserved
                for t in row['targets']:
                    assert 2<=t['teachers']<=64 and row['messages'][t['index']]['role']=='assistant'
                    band='2-32' if t['teachers']<=32 else '33-64'
                    messages=row['messages'][:t['index']+1]
                    sample=dict(source=source,band=band,doc_id=row['doc_id'],target_message_index=t['index'],
                        teachers=t['teachers'],messages=messages,pair_sha256=t['pair_sha256'],
                        history_binding=digest(json.dumps(messages,ensure_ascii=False,sort_keys=True)))
                    strata[(source,band)].append(sample)
                    totals[source+':'+band+':targets']+=1;totals[source+':'+band+':teachers']+=t['teachers']
    samples=[]
    for key in sorted(strata):
        pool=sorted(strata[key],key=lambda r:digest('answer-audit42:'+r['doc_id']+':'+str(r['target_message_index'])))
        assert len(pool)>=30
        for row in pool[:30]:samples.append(dict(id=f'A{len(samples)+1:03}',**row))
    assert len(samples)==120
    save(DATA/'TRAIN_capability_sample.json',samples)
    save(target,dict(status='120_selected_pending_semantic_judgments',created_at=now(),sources=sources,
        mechanical_full_inventory_counts=dict(totals),sample=ref(DATA/'TRAIN_capability_sample.json'),
        strata_n=30,semantic_population_counts_not_established=True,selection_salt='answer-audit42:',
        old_inventory_provenance=ref(OLD_RUN/'availability.json'),protected_TEST_used=False,new_GPU_updates=0))
    print(json.dumps(dict(sample=120,inventory_counts=dict(totals)),ensure_ascii=False),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=('reference','audit'));a=p.parse_args()
    reference() if a.mode=='reference' else audit()
