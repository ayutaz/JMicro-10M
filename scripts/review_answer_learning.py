"""Bind literal content judgments; counts are not an automatic semantic grader."""
import argparse
from collections import Counter,defaultdict
from pathlib import Path
from answer_learning_common import RUN,DATA,save,ref,bound,read_json,now


def reference():
    path=RUN/'reference_notes.json';assert not path.exists()
    raw=read_json(RUN/'reference_raw.json');assert raw['status']=='all80_raw_complete_pending_individual_content_notes'
    authored=read_json(RUN/'reference_authored.json');notes={};summary={}
    original=raw['conditions']['Akebono_official']['responses']
    bounded=raw['conditions']['Akebono_cap32']['responses']
    assert all(a['id']==b['id'] and a['messages']==b['messages'] and a['response']['raw_generated_ids']==b['response']['raw_generated_ids']
        and a['response']['input_ids']==b['response']['input_ids'] and a['response']['text']==b['response']['text']
        and a['response']['stop_reason']==b['response']['stop_reason'] for a,b in zip(original,bounded,strict=True))
    for name,value in raw['conditions'].items():
        scores=authored['Akebono_official' if name=='Akebono_cap32' else name]
        assert value['status']=='complete' and len(value['responses'])==len(scores)==20
        rows=[]
        for item,(g,r,c,reason) in zip(value['responses'],scores,strict=True):
            assert all(type(v) is int and v in (0,1,2) for v in (g,r,c)) and len(reason)>=12
            rows.append(dict(id=item['id'],grammar=g,relevance=r,context=c,rationale=reason,
                reused_from='Akebono_official' if name=='Akebono_cap32' else None))
        notes[name]=rows
        summary[name]=dict(content=sum(v['grammar']==v['relevance']==2 for v in rows),responses=20,
            natural_stops=sum(v['response']['stop_reason'] in ('END','EOS','eot','eos') for v in value['responses']),
            empty=sum(not v['response']['text'].strip() for v in value['responses']))
    save(path,dict(status='all80_content_reviewed',raw=ref(RUN/'reference_raw.json'),authored=ref(RUN/'reference_authored.json'),
        judgments=notes,summaries=summary,reviewer='Codex nonblind; known authored DEV; no independent human',
        reference20_reuse='All actual messages/input IDs/generated IDs/text/stop identical between official and32',
        cross_model_causal_effect_not_established=True,protected_TEST_used=False,created_at=now()))
    print(summary)


def audit():
    path=RUN/'TRAIN_capability_review.json';assert not path.exists()
    contract=read_json(RUN/'TRAIN_audit_sample.json')
    samples=read_json(bound(contract['sample']));authored=read_json(RUN/'TRAIN_capability_authored.json')
    assert len(samples)==len(authored)==120
    notes=[];groups=defaultdict(Counter)
    for sample,score in zip(samples,authored,strict=True):
        uid,kind,direct,memory,correction,ok,reason=score
        assert uid==sample['id'] and kind in ('greeting','ack','clarify','direct','story','other')
        assert all(type(v) is bool for v in (direct,memory,correction,ok)) and len(reason)>=12
        key=sample['source']+':'+sample['band'];count=groups[key]
        count['reviewed']+=1;count['kind:'+kind]+=1
        for label,value in [('direct_answer',direct),('explicit_history_answer',memory),('correction',correction),('neutral_assistant_acceptable',ok)]:count[label]+=int(value)
        notes.append(dict(id=uid,source=sample['source'],band=sample['band'],history_binding=sample['history_binding'],
            kind=kind,direct_answer=direct,explicit_history_answer=memory,correction=correction,
            neutral_assistant_acceptable=ok,rationale=reason))
    save(path,dict(status='all120_sample_judgments_complete',sample=contract['sample'],source_contract=ref(RUN/'TRAIN_audit_sample.json'),
        authored=ref(RUN/'TRAIN_capability_authored.json'),judgments=notes,stratum_counts={k:dict(v) for k,v in groups.items()},
        reviewer='Codex nonblind, immediate user/target and up to two earlier exchanges displayed; full history retained',
        definitions=dict(direct='Specific response to immediate question/request, including personal answers separately marked',
            memory='Explicit answer retrieving earlier given fact, not mere topic continuation',
            correction='Correctly follows explicit revision of prior provided fact',
            neutral_assistant='No unverifiable embodied biography or obvious unsupported answer in displayed scope; sampled editorial judgment'),
        population_semantic_counts_not_established=True,full_history_semantic_certification=False,
        protected_TEST_used=False,created_at=now()))
    print({k:dict(v) for k,v in groups.items()})


def dolly():
    path=RUN/'dolly_QA_review.json';assert not path.exists()
    inventory=read_json(RUN/'dolly_inventory.json')
    samples=read_json(bound(inventory['sample']));authored=read_json(RUN/'dolly_QA_authored.json')
    assert len(samples)==len(authored)==120
    notes=[];counts=defaultdict(Counter)
    for row,(uid,accepted,reason) in zip(samples,authored,strict=True):
        assert uid==row['id'] and type(accepted) is bool and len(reason)>=12
        notes.append(dict(id=uid,doc_id=row['doc_id'],original_row_sha256=row['original_row_sha256'],
            accepted_for_next_recipe=accepted,rationale=reason,category=row['category'],
            source_context_present=row['source_context_present']))
        for key in (row['category'],'source_context_'+str(row['source_context_present'])):
            counts[key]['reviewed']+=1;counts[key]['accepted']+=int(accepted)
    save(path,dict(status='all120_individual_source_QA_complete',created_at=now(),inventory=ref(RUN/'dolly_inventory.json'),
        sample=inventory['sample'],authored=ref(RUN/'dolly_QA_authored.json'),judgments=notes,
        accepted=sum(n['accepted_for_next_recipe'] for n in notes),by_category_or_context={k:dict(v) for k,v in counts.items()},
        reviewer='Codex nonblind, all selected instructions/context/answers displayed; no independent human',
        caveats=['Purposive round-robin QA sample, not a population accuracy estimate',
            'Outside-source niche facts not independently verified were conservatively declined, not proved false',
            'Contextual extraction reviewed against provided text does not certify source historical/legal/scientific truth',
            'A source-context category has errors too; mechanical category alone is not semantic certification'],
        next_selection_pending=True,protected_TEST_used=False,new_training_updates=0))
    print(dict(accepted=sum(n['accepted_for_next_recipe'] for n in notes),counts={k:dict(v) for k,v in counts.items()}))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=('reference','audit','dolly'));a=p.parse_args()
    {'reference':reference,'audit':audit,'dolly':dolly}[a.mode]()
