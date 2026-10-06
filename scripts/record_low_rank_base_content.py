"""Record manual observations for every actual continuation; exact reuse only."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from review_textbook_quantity_comparison import validate_notes
from record_parameter_displacement_anchor_content import signature
import run_low_rank_base_comparison as study


def main(arm,observations):
    raw=study.RUN/f'evaluation/{arm}/evaluation/generation.json';rows=read_json(raw)['outputs']
    notes=[]
    for line in observations.read_text(encoding='utf-8').splitlines():
        fields=line.split('\t')
        if len(fields)!=6:raise ValueError('One individual six-field observation per output required')
        notes.append([fields[0],*(int(v) for v in fields[1:5]),fields[5]])
    record=dict(reviewer='Codex nonblind; all80 individually read',independent_human_blind=False,created_at=now(),
        generation_sha256=sha256(raw),notes=notes,all80_individually_read=True,
        raw_row_sha256={r['id']:hashlib.sha256(signature(r).encode()).hexdigest() for r in rows},
        observations=study.reference(observations),
        rubric='Grammar/relevance/coherence/EOS completion separate. Fantasy, new people, implicit equipment, alternate continuations and gold mismatch are not automatic failures. Arithmetic/condition errors are not grammar errors. Nonblind Codex, no independent human.')
    validate_notes(rows,record,sha256(raw))
    references=[
        (study.old.RUN/f'evaluation/{study.old.ARM}/evaluation/generation.json',study.old.RUN/'content-notes.json'),
        (ROOT/'reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/generation.json',ROOT/'reports/phase6/conditional-prefix-mask-20261006/content-notes.json'),
        (ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/generation.json',ROOT/'reports/phase6/source_order_condition_notes.json'),
    ]
    for peer in study.ARMS:
        if peer!=arm and (study.RUN/f'{peer}-content-notes.json').exists():
            references.append((study.RUN/f'evaluation/{peer}/evaluation/generation.json',study.RUN/f'{peer}-content-notes.json'))
    cache={}
    for source,old_notes in references:
        previous=read_json(source)['outputs'];scores=validate_notes(previous,read_json(old_notes),sha256(source))
        for row in previous:cache.setdefault(signature(row),(scores[row['id']],study.reference(source),study.reference(old_notes)))
    indexed={n[0]:n for n in notes};reused=[]
    for row in rows:
        if signature(row) in cache:
            score,source,previous_notes=cache[signature(row)]
            indexed[row['id']]=[row['id'],*[score[k] for k in ('grammar','relevance','coherence','completion')],
                '元raw全項目一致で旧採点をそのまま継承：'+score['rationale']]
            reused.append(dict(id=row['id'],source=source,notes=previous_notes))
    record['notes']=[indexed[r['id']] for r in rows];record['exact_old_score_reuse']=reused
    validate_notes(rows,record,sha256(raw));destination=study.RUN/f'{arm}-content-notes.json'
    if destination.exists():raise ValueError('Preserve original completed content notes')
    atomic_json(destination,record)
    print(json.dumps(dict(arm=arm,individually_read=80,exact_previous_scores_reused=len(reused))))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('arm',choices=study.ARMS);parser.add_argument('observations',type=Path)
    args=parser.parse_args();main(args.arm,args.observations)
