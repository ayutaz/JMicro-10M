"""Bind16 individually read DEV continuations, without selecting training data."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import read_json,sha256,now
from jmicro.training import atomic_json
import diagnose_base_generalization as study


def validate_notes(rows,notes,raw_sha):
    scores={v[0]:dict(grammar=v[1],relevance=v[2],coherence=v[3],completion=v[4],rationale=v[5]) for v in notes['notes']}
    if (notes['generation_sha256']!=raw_sha or notes['independent_human_blind'] is not False or not notes['reviewer']
            or len(notes['notes'])!=len(scores) or len(rows)!=16 or set(scores)!={r['id'] for r in rows}):
        raise ValueError('Every exact raw-bound DEV16 individual note required')
    for r in rows:
        s=scores[r['id']]
        if (any(type(s[k]) is not int or s[k] not in (0,1,2) for k in ('grammar','relevance','coherence'))
                or type(s['completion']) is not int or s['completion'] not in (0,1) or len(s['rationale'].strip())<12
                or s['completion'] and (r['stop_reason']!='stop_id' or s['relevance']<1 or s['coherence']<1)):
            raise ValueError('Individual complete content score differs')
    return scores


def main(arm,observations):
    raw=study.RUN/arm/'generation.json';rows=read_json(raw)['outputs'];notes=[]
    for line in observations.read_text(encoding='utf-8').splitlines():
        fields=line.split('\t')
        if len(fields)!=6:raise ValueError('One six-field note per continuation required')
        notes.append([fields[0],*(int(v) for v in fields[1:5]),fields[5]])
    record=dict(created_at=now(),reviewer='Codex nonblind; all16 individually read',independent_human_blind=False,
        generation_sha256=sha256(raw),observations=study.reference(observations),notes=notes,
        raw_row_sha256={r['id']:hashlib.sha256(json.dumps(r,sort_keys=True,ensure_ascii=False).encode()).hexdigest() for r in rows},
        rubric='Grammar/relevance/coherence/completion separate. Source articles are context, not verified facts. New entities/plausible creative continuation alone are not errors; unexplained topic jumps/repeated contradictions are. Proper names/digits errors are not automatically syntax errors. Completion requires actual EOS and relevant coherent body.')
    validate_notes(rows,record,sha256(raw));destination=study.RUN/arm/'content-notes.json'
    if destination.exists():raise ValueError('Preserve original DEV16 notes')
    atomic_json(destination,record);print(dict(arm=arm,individually_read=len(notes)))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('arm',choices=study.ARMS);p.add_argument('observations',type=Path);a=p.parse_args();main(a.arm,a.observations)
