"""Validate every32-token raw output and bind explicit, individual judgments.

Original rubric/summary arithmetic is reused; the old64-token raw validator
is not called or weakened. Reuse requires identical actual histories, checks,
token IDs, bytes, text and stop. Scores are read from authored TSV, never
inferred from gold, keyword inclusion, lengths or stopping.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.chat_evaluation import decode_reply,summarize_chat
from jmicro.chat_review import RUBRIC,content_review
from jmicro.japanese_evaluation import repetition_metrics
from jmicro.tokenizer import Tokenizer,SUPPRESS_IDS
from jmicro.training import atomic_json
from jmicro.experiment import read_json,sha256,now
from chat_natural_contract import RUN,CONFIG,SUITES,read_dev,require_ref,ref


def fingerprint(item):
    r=item['response']
    value=dict(messages=item['messages'],checks=item['checks'],category=item['category'],
        max_new_tokens=32,generated_ids=r['generated_ids'],raw_bytes_hex=r['raw_bytes_hex'],text=r['text'],
        valid_utf8=r['valid_utf8'],stop_reason=r['stop_reason'],empty=r['empty_response'],
        role_leak=r['role_leak'],prompt_ids=r['prompt_ids'])
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True).encode()).hexdigest()


def validate_reply(row,tok,messages,suppressed):
    ids=row['generated_ids']
    assert isinstance(ids,list) and 1<=len(ids)<=32
    assert all(type(i) is int and 0<=i<tok.vocab_size for i in ids)
    assert not any(i in (3,7) for i in ids[:-1])
    reason='eot' if ids[-1]==7 else 'eos' if ids[-1]==3 else 'max_new_tokens'
    assert row['stop_reason']==reason and (reason!='max_new_tokens' or len(ids)==32)
    assert row['generated_tokens']==len(ids) and row['max_new_tokens']==32
    assert row['decoding']=='greedy' and row['suppressed'] is suppressed
    assert row['suppressed_ids']==(list(SUPPRESS_IDS) if suppressed else [])
    assert not suppressed or not any(i in SUPPRESS_IDS for i in ids)
    assert all(row[k]==v for k,v in decode_reply(tok,ids).items())
    assert row['empty_response'] is (not row['text'].strip())
    assert row['role_leak'] is any(i in (4,5,6) for i in ids)
    assert row['unexpected_special'] is any(i in (0,1,2,4,5,6) for i in ids)
    prompt,removed=tok.chat_prompt(messages,992)
    assert removed==row['removed_turns']==0 and row['full_history_retained'] is True
    assert row['prompt_ids']==prompt and row['prompt_tokens']==len(prompt)
    assert row['user_turns']==sum(m['role']=='user' for m in messages)
    assert row['repetition'] is bool(re.search(r'(.{2,}?)\1\1',row['text'],re.DOTALL))
    metrics=repetition_metrics(dict(row,stop_reason='stop_id' if reason in ('eot','eos') else reason))
    assert row['repeat_metrics']=={k:metrics[k] for k in ('char_4gram_repeat','token_4gram_repeat',
        'same_sentence_reappears','first_adjacent_triple_repeat_char')}


def get_items(path):
    path=Path(path).resolve()
    assert path.is_relative_to(RUN/'evaluation') and path.name=='result.json'
    evaluation=read_json(path)
    c=read_json(CONFIG)
    assert evaluation['status']=='raw_complete' and evaluation['binding']['config_sha256']==sha256(CONFIG)
    assert evaluation['binding']['max_new_tokens']==32 and evaluation['binding']['dtype']=='bf16'
    assert evaluation['binding']['decoding']=='greedy' and not evaluation['binding']['protected_TEST_used']
    assert evaluation['evaluation_RNG_isolated'] and not evaluation['protected_TEST_used']
    suite=path.parent.name
    assert suite in SUITES and evaluation['binding']['suite']==c['suites'][suite]
    tok=Tokenizer(require_ref(c['tokenizer']))
    cases,contexts=read_dev(c['suites'][suite])
    items={}
    for suppressed in (True,False):
        mode='suppressed' if suppressed else 'unsuppressed'
        for case in cases:
            key=mode+'-'+case['id']
            row=evaluation['outputs'][key]
            assert all(row[k]==case[k] for k in ('id','family_id','category','split','checks','messages'))
            validate_reply(row,tok,case['messages'],suppressed)
            items[key]=dict(key=key,id=case['id'],family_id=case['family_id'],category=case['category'],
                condition=mode,messages=case['messages'],checks=case['checks'],response=row)
    assert len(evaluation['outputs'])==160 and len(items)==160
    assert set(evaluation['rollouts'])=={case['id'] for case in contexts}
    final,own=[],[]
    for case in contexts:
        rollout=evaluation['rollouts'][case['id']]
        assert all(rollout[k]==case[k] for k in ('id','family_id','category','split','checks'))
        users=[m for m in case['messages'] if m['role']=='user']
        assert len(rollout['replies'])==rollout['user_turns']==len(users)
        history=[dict(case['messages'][0])] if case['messages'][0]['role']=='system' else []
        for turn,(user,row) in enumerate(zip(users,rollout['replies'],strict=True),1):
            history.append(dict(user))
            validate_reply(row,tok,history,True)
            assert row['turn']==turn and row['id']==case['id']
            assert row['history_mode']=='model_generated_assistant_history'
            key=f'own-{case["id"]}-turn-{turn}'
            is_final=turn==len(users)
            items[key]=dict(key=key,id=case['id'],family_id=case['family_id'],category=case['category'],
                condition='own-history',turn=turn,final_turn=is_final,messages=[dict(m) for m in history],
                checks=case['checks'] if is_final else [],response=row)
            history.append(dict(role='assistant',content=row['text']))
            own.append(row)
        final.append(rollout['replies'][-1])
    assert len(items)==219 and len(own)==59 and len(final)==24
    primary=[i['response'] for i in items.values() if i['condition']=='suppressed']
    control=[i['response'] for i in items.values() if i['condition']=='unsuppressed']
    assert evaluation['primary']==summarize_chat(primary)
    assert evaluation['unsuppressed']==summarize_chat(control)
    assert evaluation['own_history']==summarize_chat(own)
    # Explicit summary field adapter for the unchanged original content rubric.
    view=dict(evaluation,role_control=evaluation['unsuppressed'],own_history_all_turns=evaluation['own_history'],
              own_history_final24=summarize_chat(final))
    return evaluation,view,items


def reuse_index():
    index={}
    for notes_path in sorted((RUN/'evaluation').glob('*/*/notes.json')):
        raw,view,items=get_items(notes_path.with_name('result.json'))
        notes=read_json(notes_path)
        content_review(view,sha256(notes_path.with_name('result.json')),notes,items)
        for note in notes['judgments']:
            fp=fingerprint(items[note['key']])
            rating={k:note[k] for k in ('grammar','relevance','context','rationale')}
            if fp in index:
                assert all(index[fp][k]==rating[k] for k in rating)
            else:
                index[fp]=dict(rating,source_notes=dict(ref(notes_path),key=note['key']),fingerprint=fp)
    return index


def packet(path):
    raw,view,items=get_items(path)
    target=path.with_name('packet.json')
    if target.exists():
        saved=read_json(target);assert saved['evaluation_sha256']==sha256(path)
        return saved
    assert not path.with_name('notes.json').exists()
    index,seen,pending,reused=reuse_index(),{},{},{}
    for key,item in items.items():
        fp=fingerprint(item)
        if fp in index:
            reused[key]=index[fp]
        elif fp in seen:
            reused[key]=dict(same_packet_key=seen[fp],fingerprint=fp)
        else:
            seen[fp]=key
            pending[key]=dict(fingerprint=fp,condition=item['condition'],messages=item['messages'],
                checks=item['checks'],response=item['response']['text'],stop=item['response']['stop_reason'],
                valid_utf8=item['response']['valid_utf8'])
    saved=dict(evaluation_sha256=sha256(path),rubric=RUBRIC,pending=pending,reused=reused,
               total_judgments=219,manual_pending=len(pending),created_at=now(),
               reviewer_source=ref(Path(__file__)),reuse_only_identical_actual_history_and_raw=True)
    atomic_json(target,saved)
    return saved


def finish(path,scores_path):
    raw,view,items=get_items(path)
    saved=read_json(path.with_name('packet.json'))
    assert saved['evaluation_sha256']==sha256(path)
    authored={}
    pending_keys=list(saved['pending'])
    for line in scores_path.read_text().splitlines():
        if not line.strip():continue
        i,g,r,c,reason=line.split('\t',4)
        i=int(i);assert 0<=i<len(pending_keys)
        key=pending_keys[i];assert key not in authored
        authored[key]=dict(key=key,grammar=int(g),relevance=int(r),context=int(c),rationale=reason)
    assert set(authored)==set(pending_keys),'All literal authored judgments required'
    for key,source in saved['reused'].items():
        if 'same_packet_key' in source:
            original=authored[source['same_packet_key']]
        else:
            prior=read_json(require_ref(source['source_notes']))
            original=next(n for n in prior['judgments'] if n['key']==source['source_notes']['key'])
            assert all(original[k]==source[k] for k in ('grammar','relevance','context','rationale'))
        assert fingerprint(items[key])==source['fingerprint']
        authored[key]=dict(key=key,**{k:original[k] for k in ('grammar','relevance','context','rationale')},reuse=source)
    assert set(authored)==set(items)
    notes=dict(evaluation_sha256=sha256(path),rubric=RUBRIC,
        reviewer=dict(kind='codex_nonblind',identity='Codex',independent_human=False,blind=False),
        judgments=[authored[key] for key in items],pending_all_content_judgments=False,
        source=ref(scores_path),validator_source=ref(Path(__file__)),created_at=now())
    review=content_review(view,sha256(path),notes,items)
    assert not path.with_name('notes.json').exists()
    atomic_json(path.with_name('notes.json'),notes)
    atomic_json(path.with_name('review.json'),review)
    print(json.dumps(dict(raw=str(path),manual=len(pending_keys),reused=len(saved['reused']),
        primary=review['summaries']['primary'],own_context=review['summaries']['own_history_final24']['context_score2']),ensure_ascii=False))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=('packet','finish'))
    parser.add_argument('arm',choices=('C0','C1'))
    parser.add_argument('suite',choices=SUITES)
    parser.add_argument('--start',type=int,default=0);parser.add_argument('--count',type=int,default=40)
    args=parser.parse_args()
    path=RUN/'evaluation'/args.arm/args.suite/'result.json'
    if args.mode=='finish':
        finish(path,path.with_name('authored_indices.tsv'))
    else:
        saved=packet(path)
        print(json.dumps(dict(total=219,manual_pending=saved['manual_pending'],reused=len(saved['reused']))))
        for i,(key,row) in enumerate(list(saved['pending'].items())[args.start:args.start+args.count],args.start):
            print(json.dumps(dict(index=i,key=key,**row),ensure_ascii=False))


if __name__=='__main__':main()
