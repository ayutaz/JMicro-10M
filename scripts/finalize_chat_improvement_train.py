"""Freeze reviewed TRAIN; applies explicit source review exclusions only."""
from collections import Counter
import json
from pathlib import Path
import shutil
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.chat_curriculum import WEIGHTS,semantic_check
from jmicro.experiment import ROOT,now,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from prepare_chat_improvement_train import DATA,RUN,BOUNDS,content_binding,dump_jsonl

EXCLUDED_SOURCE_SUFFIX='/dialogues/13577.json'

def main():
    assert not (DATA/'train.jsonl').exists(),'Final TRAIN is immutable'
    packet=[json.loads(l) for l in (DATA/'train_review_packet.jsonl').read_text().splitlines()]
    review=json.loads((RUN/'train_content_review_final.json').read_text())
    assert review['status']=='fixed_sample_passed' and review['samples']==280 and review['errors']==0
    assert review['packet_sha256']==sha256(DATA/'train_review_packet.jsonl')
    assert review['candidate_sha256']==sha256(DATA/'candidate.train.jsonl')
    source=[json.loads(l) for l in (DATA/'candidate.train.jsonl').read_text().splitlines()]
    natural=[r for r in source if r['source']=='RealPersonaChat-selected-unedited']
    assert len(natural)==49
    exclusions=[r for r in natural if r['source_doc_id'].endswith(EXCLUDED_SOURCE_SUFFIX)]
    assert len(exclusions)==1 and exclusions[0]['messages'][0]['text']=='こんにちは！'
    assert exclusions[0]['messages'][-1]['text']=='こんばんはー。'
    natural_notes=[dict(doc_id=r['doc_id'],content_sha256=r['content_sha256'],
        passed=r not in exclusions,reason='挨拶に対する自然な挨拶で個人体験を創作しない。' if r not in exclusions else
            'Userの「こんにちは」に「こんばんは」と返して時刻の挨拶を取り違える。元source familyを除外。') for r in natural]
    atomic_json(RUN/'natural_source_content_review.json',dict(created_at=now(),reviewer='Codex nonblind',
        samples=49,passed=48,excluded=1,all_selected_natural_pairs_read=True,judgments=natural_notes,
        independent_human_review=False,candidate_sha256=review['candidate_sha256']))
    selected=[r for r in source if r not in exclusions]
    # Punctuation variants of natural greetings are conservatively ONE family.
    for record in selected:
        if record['source']=='RealPersonaChat-selected-unedited':
            record['source_family']=record['family'];record['family']='rpc-natural-greeting-near-family'
        else:assert semantic_check(record)
        assert record['content_sha256']==content_binding(record)
    by_id={r['doc_id']:r for r in selected}
    assert len(by_id)==len(selected)
    assert all(r['doc_id'] in by_id and r['messages']==by_id[r['doc_id']]['messages'] for r in packet)
    assert all(j['passed'] and j['content_sha256']==by_id[j['doc_id']]['content_sha256'] for j in review['judgments'])
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    total=0;category=Counter();families={k:Counter() for k in WEIGHTS};hist=Counter();bodies=Counter()
    for record in selected:
        n=len(tok.encode(record['messages'][-1]['text']))+1
        assert n==record['teacher_tokens'] and 2<=n<=65
        total+=n;category[record['category']]+=n;families[record['category']][record['family']]+=n
        hist[record['length_bin']]+=1;bodies[record['messages'][-1]['text']]+=1
    reference=json.loads((RUN/'reference_targets.json').read_text())
    fractions=[hist[i]/len(selected) for i in range(4)]
    tv=sum(abs(a-b) for a,b in zip(fractions,reference['bin_fractions']))/2
    eotdiff=abs(len(selected)/total-reference['EOT_fraction'])
    checks=dict(minimum_650k=total>=650000,mixture=all(abs(category[k]/total-w)<=.01 for k,w in WEIGHTS.items()),
        family_cap=all(max(v.values())/category[k]<=.05 for k,v in families.items()),
        length_TV=tv<=.10,EOT_difference=eotdiff<=.01,all_280_bound=True,source_pairs_reviewed=True,
        schema_UTF8_grounding_roundtrip=True,new_DEV_created=False)
    assert all(v for k,v in checks.items() if k!='new_DEV_created')
    dump_jsonl(DATA/'train.jsonl',selected)
    manifest=dict(created_at=now(),status='reviewed_TRAIN_frozen_before_new_DEV',vocab_size=4096,
        train=dict(path=str(DATA/'train.jsonl'),sha256=sha256(DATA/'train.jsonl'),targets=len(selected),teachers_per_pass=total),
        source_candidate=dict(path=str(DATA/'candidate.train.jsonl'),sha256=review['candidate_sha256']),
        design_freeze=dict(path=str(RUN/'train_design_freeze.json'),sha256=sha256(RUN/'train_design_freeze.json')),
        final_policy_sha256=sha256(Path(__file__)),review=dict(path=str(RUN/'train_content_review_final.json'),sha256=sha256(RUN/'train_content_review_final.json')),
        source_review=dict(path=str(RUN/'natural_source_content_review.json'),sha256=sha256(RUN/'natural_source_content_review.json')),
        teacher_categories=dict(category),category_fractions={k:v/total for k,v in category.items()},
        family_statistics={k:dict(count=len(v),max_teacher_fraction=max(v.values())/category[k]) for k,v in families.items()},
        length_bins=[hist[i] for i in range(4)],length_bin_fractions=fractions,length_TV=tv,EOT_absolute_difference=eotdiff,
        exact_response_body_types=len(bodies),most_frequent_body_targets=max(bodies.values()),
        repeated_body_is_not_independent_information=True,natural_source_targets=len(natural)-len(exclusions),
        natural_source_teacher_tokens=sum(r['teacher_tokens'] for r in natural if r not in exclusions),
        near_family_policy='all authored slot/wording variants stay in original authored scenario; all retained natural greeting pairs grouped as one near family',
        excluded_source_doc_ids=[r['source_doc_id'] for r in exclusions],checks=checks,
        independent_human_review=False,all_TRAIN_human_certified=False,Base_adopted=False,Chat_adopted=False)
    atomic_json(DATA/'manifest.json',manifest)
    atomic_json(RUN/'train_preparation.json',dict(manifest,manifest_path=str(DATA/'manifest.json'),manifest_sha256=sha256(DATA/'manifest.json')))
    print(json.dumps(dict(status=manifest['status'],targets=len(selected),teachers=total,train_sha256=manifest['train']['sha256'],
        exact_response_body_types=len(bodies),most_frequent_body_targets=max(bodies.values()),natural_teacher_tokens=manifest['natural_source_teacher_tokens'],checks=checks),ensure_ascii=False,indent=2))

if __name__=='__main__':main()
