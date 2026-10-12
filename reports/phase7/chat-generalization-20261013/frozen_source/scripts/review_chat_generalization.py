"""CPU raw-bound packets and explicit authored judgments; no automatic grader.

Reuse requires identical complete actual histories, raw IDs/bytes/text and
checks. All 219 judgments remain in every result with source provenance.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.chat_review import review_items,notes_template,content_review,RUBRIC
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from evaluate_chat_generalization import load_cases
from chat_generalization_contract import RUN


def fingerprint(item):
    r=item['response']
    value=dict(messages=item['messages'],checks=item['checks'],category=item['category'],
        generated_ids=r['generated_ids'],raw_bytes_hex=r['raw_bytes_hex'],text=r['text'],
        valid_utf8=r['valid_utf8'],stop_reason=r['stop_reason'],empty=r['empty_response'],
        role_leak=r['role_leak'],prompt_ids=r['prompt_ids'])
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True).encode()).hexdigest()


def get_items(path):
    result=read_json(path);binding=result['binding']
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    assert sha256(tok.path)==binding['tokenizer_sha256']
    config=read_json(ROOT/'configs/phase7/chat-generalization-20261013.json')
    suite=next(config[k]['path'] for k in ('new_DEV','old_suite') if config[k]['sha256']==binding['suite_sha256'])
    cases,_=load_cases(suite,tok);return result,review_items(result,cases,tok,1024)


def reuse_index():
    index={}
    for path in sorted((RUN/'evaluation').rglob('notes.json')):
        evaluation_path=path.parent/'result.json'
        if not evaluation_path.exists():continue
        evaluation,items=get_items(evaluation_path);notes=read_json(path)
        content_review(evaluation,sha256(evaluation_path),notes,items)
        for note in notes['judgments']:
            fp=fingerprint(items[note['key']]);candidate={k:note[k] for k in ('grammar','relevance','context','rationale')}
            if fp in index:assert {k:index[fp][k] for k in candidate}==candidate,'Identical evidence has inconsistent reused judgment'
            else:index[fp]=dict(candidate,source_notes=dict(path=str(path),sha256=sha256(path),key=note['key']),fingerprint=fp)
    return index


def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=('packet','finish'));p.add_argument('evaluation',type=Path)
    p.add_argument('--scores',type=Path);p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=40)
    args=p.parse_args();path=args.evaluation.resolve()
    assert path.is_relative_to(RUN/'evaluation')
    evaluation,items=get_items(path);out=path.parent
    assert not (out/'notes.json').exists(),'Completed review retained; do not overwrite its source provenance'
    if args.mode=='packet' and (out/'packet.json').exists():
        packet=read_json(out/'packet.json');assert packet['evaluation_sha256']==sha256(path)
    elif args.mode=='packet':
        prior=reuse_index();pending=[];reused={};seen={}
        for key,item in items.items():
            fp=fingerprint(item)
            if fp in prior:reused[key]=prior[fp]
            elif fp in seen:reused[key]=dict(same_packet_key=seen[fp],fingerprint=fp)
            else:
                seen[fp]=key
                pending.append(dict(key=key,fingerprint=fp,condition=item['condition'],messages=item['messages'],checks=item['checks'],
                    response=item['response']['text'],ids=item['response']['generated_ids'],raw_bytes=item['response']['raw_bytes_hex'],
                    stop=item['response']['stop_reason'],UTF8=item['response']['valid_utf8']))
        packet=dict(evaluation_sha256=sha256(path),rubric=RUBRIC,pending=pending,reused=reused,
            total_judgments=219,manual_pending=len(pending),reuse_only_identical_actual_history_and_raw_output=True)
        atomic_json(out/'packet.json',packet)
    if args.mode=='packet':
        print(json.dumps(dict(total=219,pending=len(packet['pending']),reused=len(packet['reused']),start=args.start,count=args.count)))
        assert args.start>=0 and args.count>0
        for index,r in enumerate(packet['pending'][args.start:args.start+args.count],args.start):
            print(json.dumps(dict(index=index,**{k:r[k] for k in ('key','messages','response','stop','UTF8')}),ensure_ascii=False))
    else:
        assert args.scores is not None
        packet=read_json(out/'packet.json');assert packet['evaluation_sha256']==sha256(path)
        if args.scores.suffix=='.tsv':
            authored=[]
            for line in args.scores.read_text().splitlines():
                if not line.strip():continue
                key,g,r,c,reason=line.split('\t',4)
                authored.append(dict(key=key,grammar=int(g),relevance=int(r),context=int(c),rationale=reason))
        else:authored=read_json(args.scores)
        scores={r['key']:r for r in authored}
        assert len(authored)==len(scores)==len(packet['pending']) and set(scores)=={r['key'] for r in packet['pending']}
        for key,row in packet['reused'].items():
            if 'same_packet_key' in row:
                base=scores[row['same_packet_key']]
                scores[key]=dict(key=key,**{k:base[k] for k in ('grammar','relevance','context','rationale')},
                    reuse=dict(packet_key=row['same_packet_key'],fingerprint=row['fingerprint']))
            else:
                scores[key]=dict(key=key,**{k:row[k] for k in ('grammar','relevance','context','rationale')},
                    reuse=dict(source_notes=row['source_notes'],fingerprint=row['fingerprint']))
            assert fingerprint(items[key])==row['fingerprint']
        notes=notes_template(sha256(path),items)
        notes.update(reviewer=dict(kind='codex_nonblind',identity='Codex plan133 reviewer',independent_human=False,blind=False),
            judgments=[scores[key] for key in items],pending_all_content_judgments=False,
            authored_score_file=dict(path=str(args.scores.resolve()),sha256=sha256(args.scores)),reviewed_at=now())
        review=content_review(evaluation,sha256(path),notes,items)
        atomic_json(out/'notes.json',notes);atomic_json(out/'review.json',review)
        print(json.dumps(dict(summaries=review['summaries'],dev_screen_passed=review['dev_screen_passed']),ensure_ascii=False))

if __name__=='__main__':main()
