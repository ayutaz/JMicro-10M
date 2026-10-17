"""Bind literal authored diagnostic ratings; never select an earlier model."""
import argparse
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from chat_natural_contract import RUN,ref
from jmicro.experiment import read_json,now
from jmicro.training import atomic_json


def main(arm,point):
    raw=RUN/'diagnostics'/arm/f'{point}.json'
    target=raw.with_name(f'{point}_notes.json')
    assert not target.exists()
    authored=RUN/f'diagnostic_{arm}_{point}_authored.json'
    rows=read_json(raw)['outputs'];scores=read_json(authored)
    assert len(rows)==len(scores)==10
    notes=[]
    for row,score in zip(rows,scores,strict=True):
        g,r,c,reason=score
        assert all(type(s) is int and s in (0,1,2) for s in (g,r,c)) and len(reason)>=12
        notes.append(dict(id=row['case']['id'],grammar=g,relevance=r,context=c,rationale=reason))
    atomic_json(target,dict(raw=ref(raw),authored=ref(authored),judgments=notes,reviewer='Codex nonblind; diagnostic only',
        primary_selection=False,all10_reviewed=True,created_at=now()))
    print(f'{arm} {point}:10 literal authored diagnostic notes bound')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('arm',choices=('C0','C1'))
    p.add_argument('point',choices=('250000','500000'));a=p.parse_args()
    main(a.arm,a.point)
