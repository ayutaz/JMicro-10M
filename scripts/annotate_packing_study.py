"""Bind individual Codex notes to raw generations; reuse only exact old outputs."""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
import run_packing_study as study


def old_reviews():
    path=ROOT/'reports/phase6/condition_learning_annotations.json';data=read_json(path)
    lookup={}
    for arm,entry in data['arms'].items():
        for note in entry['notes']:
            raw=entry['raw_by_id'][note[0]]
            key=(note[0],raw['prefix'],tuple(raw['generated_ids']),raw['text'],raw['stop_reason'])
            lookup[key]=dict(note=note,provenance=dict(path=str(path),sha256=sha256(path),arm=arm))
    return lookup


def main(mode,arm=None,start=0,count=40):
    prior=old_reviews();manual_path=study.RUN/'manual-notes.json';manual=read_json(manual_path) if manual_path.exists() else {}
    arms=read_json(study.RUN/'result.json')['checkpoints'] if (study.RUN/'result.json').exists() else dict.fromkeys(('fixed','shuffle','isolated','mixed-fixed','mixed-candidate'))
    if mode=='pending':
        for name in ([arm] if arm else arms):
            path=study.RUN/'evaluation'/name/'evaluation/generation.json'
            if not path.exists():continue
            pending=[];reused=0
            for row in read_json(path)['outputs']:
                key=(row['id'],row['prefix'],tuple(row['generated_ids']),row['text'],row['stop_reason'])
                if key in prior:reused+=1
                elif row['id'] not in manual.get(name,{}):pending.append(row)
            print(json.dumps(dict(arm=name,pending=len(pending),exact_old_review_reused=reused)),flush=True)
            for row in pending[start:start+count]:
                print(json.dumps(dict(arm=name,id=row['id'],prefix=row['prefix'],text=row['text'],stop=row['stop_reason'],repetition=row['repetition']),ensure_ascii=False),flush=True)
        return
    annotations={}
    for name in arms:
        path=study.RUN/'evaluation'/name/'evaluation/generation.json';raw=read_json(path)['outputs'];notes=[];reuse={}
        for row in raw:
            key=(row['id'],row['prefix'],tuple(row['generated_ids']),row['text'],row['stop_reason'])
            if row['id'] in manual.get(name,{}):note=[row['id'],*manual[name][row['id']]]
            elif key in prior:note=prior[key]['note'];reuse[row['id']]=prior[key]['provenance']
            else:raise ValueError('Missing individually read judgment '+name+' '+row['id'])
            notes.append(note)
        assert len(notes)==80 and len({r[0] for r in notes})==80
        annotations[name]=dict(generation_sha256=sha256(path),notes=notes,exact_reused_reviews=reuse,
            raw_by_id={r['id']:dict(prefix=r['prefix'],text=r['text'],generated_ids=r['generated_ids'],stop_reason=r['stop_reason']) for r in raw})
    write_json(study.RUN/'annotations.json',dict(arms=annotations,reviewer='Codex nonblind individual content judgment',
        independent_human_blind=False,annotator_sha256=sha256(Path(__file__)),manual_notes_sha256=sha256(manual_path),created_at=now()))
    print(json.dumps(dict(status='saved_all_content_notes',outputs=80*len(arms))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('pending','save'),default='pending');p.add_argument('--arm');p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=40);a=p.parse_args()
    assert sys.version_info[:3]==(3,12,7);main(a.mode,a.arm,a.start,a.count)
