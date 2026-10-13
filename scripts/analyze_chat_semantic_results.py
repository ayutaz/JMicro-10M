"""Summarize already-authored judgments; never infer ratings from gold/keywords."""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.chat_review import content_review
from chat_semantic_contract import RUN,preflight,reference
from review_chat_semantic_observer import get_items


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--final',action='store_true');args=parser.parse_args()
    c,_,_=preflight(ROOT/'configs/phase7/chat-semantic-diversity-20261013.json')
    points=[('parent','t0')]+[(arm,point) for arm in ('S0','S1') for point in (('t1','t2','t3') if args.final else ('t1',))]
    rows={}
    for arm,point in points:
        nll=read_json(RUN/'NLL'/arm/(point+'.json'))
        assert nll['status']=='complete' and nll['binding']['config_sha256']==c['config_sha256']
        for suite in ('new','previous','old'):
            path=RUN/'evaluation'/arm/point/suite/'greedy/result.json'
            evaluation,items=get_items(path);notes=read_json(path.with_name('notes.json'))
            review=content_review(evaluation,sha256(path),notes,items)
            assert json.loads(json.dumps(review))==read_json(path.with_name('review.json'))
            scores={r['key']:r for r in notes['judgments']}
            primary=[i for i in items.values() if i['condition']=='suppressed']
            own=[i for i in items.values() if i['condition']=='own-history']
            final=[i for i in own if i['final_turn']]
            provided={i['id']:scores[i['key']] for i in primary}
            matched=[dict(id=i['id'],provided=provided[i['id']],own=scores[i['key']],
                prior_weak=next(r['prior_content_weak_turns'] for r in review['own_history_families'] if r['id']==i['id']),
                actual_own_messages=i['messages'],actual_own_response=i['response']['text']) for i in final]
            assert len(matched)==24
            rows[arm+'-'+point+'-'+suite]=dict(raw=reference(path),notes=reference(path.with_name('notes.json')),
                summaries=review['summaries'],categories=review['categories'],mechanical={k:evaluation[k] for k in (
                    'primary','role_control','own_history_final24','own_history_all_turns')},
                fluent_but_not_relevant=sum(scores[i['key']]['grammar']==2 and scores[i['key']]['relevance']<2 for i in primary),
                matched24_provided_context2=sum(r['provided']['context']==2 for r in matched),
                matched24_own_context2=sum(r['own']['context']==2 for r in matched),
                provided_correct_to_own_weak=[r['id'] for r in matched if r['provided']['context']==2 and r['own']['context']<2],
                provided_weak_to_own_correct=[r['id'] for r in matched if r['provided']['context']<2 and r['own']['context']==2],
                own_correct_after_weak_prior=[r['id'] for r in matched if r['own']['context']==2 and r['prior_weak']],
                matched24=matched,fixed_NLL=nll['summaries'])
    atomic_json(RUN/('final_analysis.json' if args.final else 'intermediate_analysis.json'),dict(
        config_sha256=c['config_sha256'],source_sha256=sha256(Path(__file__)),completed_at=now(),rows=rows,
        ratings_source='Only complete raw-bound Codex nonblind authored notes; no automatic gold matching',
        matched_unit='Same24 family IDs provided vs actual own histories; not additional independent families',
        fixed_NLL_scope='Compare same target bytes across checkpoints; body and EOT separately',
        Base_adopted=False,Chat_adopted=False,protected_TEST_used=False))
    for name,row in rows.items():
        print(json.dumps(dict(name=name,joint=row['summaries']['primary']['joint_grammar_relevance_score2'],
            own_context=row['matched24_own_context2'],provided24_context=row['matched24_provided_context2'],
            fluent_irrelevant=row['fluent_but_not_relevant'],new_NLL=row['fixed_NLL']['new_DEV']['body_mean_NLL'],
            RPC_BPB=row['fixed_NLL']['RPC_DEV']['body_BPB']),ensure_ascii=False))


if __name__=='__main__':main()
