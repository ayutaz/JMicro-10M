"""Bind200 literal judgments to actual requests/IDs; describe this fixed sample."""
import csv
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.tokenizer import Tokenizer
from chat_quality_100 import RUN,ROOT,read,save,sha,now,CHECKPOINT

TAGS={'irrelevant','non_answer','incorrect_fact','contradiction','missed_correction','lost_binding',
    'format_violation','echo','fabricated','repetition','broken_sentence','stale_history'}
FORMAT=['L-36','memo_8','青い空','08:15','北','□','B→D→A','昼 / 夜','3,600','cat']


def main():
    assert not (RUN/'notes.json').exists(),'Do not overwrite completed judgments'
    p=read(RUN/'protocol.json');r=read(RUN/'raw.json');c=read(RUN/'cases.json')
    assert p['cases_sha256']==sha(RUN/'cases.json')==r['cases_sha256']
    assert r['protocol_sha256']==sha(RUN/'protocol.json')
    assert p['source_sha256']==sha(ROOT/'scripts/chat_quality_100.py')
    assert c['created_at']<r['created_at'] and p['created_at']<r['created_at']
    assert r['status']=='all200_actual_responses_complete_pending_literal_review'
    assert r['actual_response_count']==200 and r['completed_cases']==100
    for model in (r['model_before'],r['model_after']):
        assert model['checkpoint_sha256']==CHECKPOINT and model['decoding']=='greedy' and model['max_new_tokens']==32 and model['device']=='CPU'
    authored={}
    for line in (RUN/'authored.tsv').read_text(encoding='utf-8-sig').splitlines():
        cells=line.split('\t');assert len(cells)==7
        i,g,v,x,f,tags,reason=cells;i=int(i);assert i not in authored
        assert g in '012' and v in '012' and x in '012' and f in ('0','1','-') and len(reason)>=12
        tags=[] if tags=='-' else tags.split(',');assert set(tags)<=TAGS
        authored[i]=dict(grammar=int(g),relevance=int(v),context=int(x),factual_correct=None if f=='-' else f=='1',tags=tags,rationale=reason)
    assert set(authored)==set(range(200))
    token_model=ROOT/'artifacts/phase2/4096/tokenizer.model';tok=Tokenizer(token_model)
    assert sha(token_model)==r['model_before']['tokenizer_sha256']
    notes=[];expected_rows=[];offset=0
    for case in c['cases']:
        history=[dict(m) for m in case['history']]
        for turn,t in enumerate(case['turns'],1):
            row=r['responses'][offset];history.append(dict(role='user',content=t['user']))
            assert row['id']==case['id'] and row['category']==case['category'] and row['turn']==turn
            assert row['request']==dict(messages=history,max_new_tokens=32) and row['expected']==t['expected']
            assert row['objective']==t['objective'] and row['final']==(turn==len(case['turns']))
            reply=row['answer']['response'];prompt,removed=tok.chat_prompt(history,1024-32)
            assert prompt==reply['prompt_ids'] and len(prompt)==reply['prompt_tokens'] and removed==reply['removed_turns']==0
            assert reply['full_history_retained'] and reply['max_new_tokens']==32 and reply['decoding']=='greedy'
            ids=reply['generated_ids'];assert len(ids)==reply['generated_tokens'] and 1<=len(ids)<=32
            expected_stop='eot' if ids[-1]==7 else 'eos' if ids[-1]==3 else 'max_new_tokens'
            assert reply['stop_reason']==expected_stop and (expected_stop!='max_new_tokens' or len(ids)==32)
            raw=tok.decode_bytes(ids);assert raw.hex()==reply['raw_bytes_hex']
            try:text=raw.decode('utf-8');valid=True
            except UnicodeDecodeError:text=raw.decode('utf-8',errors='replace');valid=False
            assert text==reply['text'] and valid==reply['valid_utf8']
            note=authored[offset];assert (note['factual_correct'] is not None)==row['objective']
            passed=all(note[k]==2 for k in ('grammar','relevance','context'))
            if passed and row['objective']:assert note['factual_correct']
            notes.append(dict(index=offset,id=row['id'],turn=turn,final=row['final'],category=row['category'],
                task_pass=passed,raw_row_sha256=hashlib.sha256(json.dumps(row,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),**note))
            expected_rows.append(row);history.append(dict(role='assistant',content=text));offset+=1
    assert offset==200
    def summarize(indices):
        selected=[notes[i] for i in indices];raws=[r['responses'][i]['answer']['response'] for i in indices]
        objective=[n for n in selected if n['factual_correct'] is not None]
        frequencies=Counter(row['text'] for row in raws)
        return dict(responses=len(selected),task_pass=sum(n['task_pass'] for n in selected),
            natural_grammar=sum(n['grammar']==2 for n in selected),relevance2=sum(n['relevance']==2 for n in selected),
            context2=sum(n['context']==2 for n in selected),objective_probes=len(objective),
            factual_correct=sum(n['factual_correct'] for n in objective),
            objective_task_pass=sum(n['task_pass'] for n in objective),
            natural_stops=sum(a['stop_reason'] in ('eot','eos') for a in raws),
            repetition_flag=sum(a['repetition'] for a in raws),empty=sum(a['empty_response'] for a in raws),
            invalid_UTF8=sum(not a['valid_utf8'] for a in raws),role_leak=sum(a['role_leak'] for a in raws),
            trimmed_history=sum(a['removed_turns']>0 for a in raws),unique_replies=len(frequencies),
            most_common_replies=frequencies.most_common(5),
            tags=dict(Counter(tag for n in selected for tag in n['tags'])))
    finals=[i for i,row in enumerate(r['responses']) if row['final']];assert len(finals)==100
    categories={category:summarize([i for i in finals if r['responses'][i]['category']==category])
        for category in dict.fromkeys(case['category'] for case in c['cases'])}
    own={}
    loops=[]
    for category in ('own_memory','own_correction'):
        own[category]={f'turn{turn}':summarize([i for i,row in enumerate(r['responses']) if row['category']==category and row['turn']==turn]) for turn in range(1,7)}
        for case in [case for case in c['cases'] if case['category']==category]:
            sequence=[row['answer']['response']['text'] for row in r['responses'] if row['id']==case['id']]
            longest=current=1;adjacent=0
            for a,b in zip(sequence,sequence[1:]):
                current=current+1 if a==b else 1;longest=max(longest,current);adjacent+=a==b
            loops.append(dict(id=case['id'],max_identical_streak=longest,identical_adjacent_pairs=adjacent,
                unique_replies=len(set(sequence)),case_final_task_pass=next(n['task_pass'] for n in notes if n['id']==case['id'] and n['final'])))
    format_exact=[]
    for i,expected in enumerate(FORMAT,1):
        row=next(row for row in r['responses'] if row['id']==f'format-{i:02d}')
        format_exact.append(dict(id=row['id'],expected=expected,actual=row['answer']['response']['text'],exact=row['answer']['response']['text']==expected))
    save(RUN/'notes.json',dict(created_at=now(),reviewer='Codex nonblind; not independent human',
        raw_sha256=sha(RUN/'raw.json'),cases_sha256=sha(RUN/'cases.json'),authored_sha256=sha(RUN/'authored.tsv'),
        all200_literal_judgments=notes,no_semantic_scores_inferred_from_keywords=True,source_sha256=sha(__file__)))
    summary=dict(status='all100_cases_200_responses_reviewed_and_validated',created_at=now(),
        protocol_sha256=sha(RUN/'protocol.json'),raw_sha256=sha(RUN/'raw.json'),notes_sha256=sha(RUN/'notes.json'),
        final100=summarize(finals),all200=summarize(list(range(200))),categories=categories,
        own_history_by_turn=own,exact_format=format_exact,exact_format_pass=sum(row['exact'] for row in format_exact),
        cross_turn_loops=loops,cases_with_at_least3_identical_replies=sum(row['max_identical_streak']>=3 for row in loops),
        mechanical_same_reply_is_not_automatically_wrong=True,raw_prompt_and_actual_history_all_verified=True,
        max_prompt_tokens=max(row['answer']['response']['prompt_tokens'] for row in r['responses']),
        CPU_wall_seconds=r['CPU_wall_seconds'],source_sha256=sha(__file__),
        interpretation='Descriptive results of a fixed balanced diagnostic, not population-wide accuracy or sealed TEST',
        no_training_or_GPU=True,Chat_adopted=False)
    save(RUN/'summary.json',summary)
    with (RUN/'responses.csv').open('w',encoding='utf-8-sig',newline='') as out:
        writer=csv.writer(out);writer.writerow(['case','category','turn','final','user','expected','reply','grammar','relevance','context','factual_correct','task_pass','tags','rationale','full_actual_history'])
        for row,n in zip(r['responses'],notes):
            writer.writerow([row['id'],row['category'],row['turn'],row['final'],row['request']['messages'][-1]['content'],row['expected'],row['answer']['response']['text'],
                n['grammar'],n['relevance'],n['context'],n['factual_correct'],n['task_pass'],','.join(n['tags']),n['rationale'],json.dumps(row['request']['messages'],ensure_ascii=False)])
    print(json.dumps(dict(final100=summary['final100'],categories={k:dict(task_pass=v['task_pass'],factual_correct=v['factual_correct'],objective_probes=v['objective_probes']) for k,v in categories.items()},
        all200=summary['all200'],cross_turn_loop_cases=summary['cases_with_at_least3_identical_replies'],CPU_wall_seconds=summary['CPU_wall_seconds'],max_prompt_tokens=summary['max_prompt_tokens']),ensure_ascii=False))


if __name__=='__main__':main()
