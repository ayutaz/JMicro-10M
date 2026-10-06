"""All80 manual raw-bound notes; cache scores only for exactly identical raw."""
import argparse
import hashlib
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from review_textbook_quantity_comparison import validate_notes
from record_parameter_displacement_anchor_content import signature
import run_gated_shared_comparison as study


def main(observations):
    raw=study.RUN/f'evaluation/{study.ARM}/evaluation/generation.json';rows=read_json(raw)['outputs'];notes=[]
    for line in observations.read_text(encoding='utf-8').splitlines():
        fields=line.split('\t')
        if len(fields)!=6:raise ValueError('One six-field individual observation per output required')
        notes.append([fields[0],*(int(v) for v in fields[1:5]),fields[5]])
    record=dict(reviewer='Codex nonblind; all80 individually read',independent_human_blind=False,created_at=now(),
        generation_sha256=sha256(raw),notes=notes,all80_individually_read=True,observations=study.reference(observations),
        raw_row_sha256={r['id']:hashlib.sha256(signature(r).encode()).hexdigest() for r in rows},
        rubric='Grammar/relevance/coherence/completion separate; fantasy, implicit equipment, new people and alternate plausible continuation are not automatic errors. Arithmetic/condition failures are not grammar failures. Nonblind Codex, not independent human.')
    validate_notes(rows,record,sha256(raw));cache={}
    references=[
        (study.native.RUN/'evaluation/matched_staged_CE/evaluation/generation.json',study.native.RUN/'matched_staged_CE-content-notes.json'),
        (ROOT/'reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/generation.json',ROOT/'reports/phase6/conditional-prefix-mask-20261006/content-notes.json'),
        (ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/generation.json',ROOT/'reports/phase6/source_order_condition_notes.json')]
    for source,old_notes in references:
        previous=read_json(source)['outputs'];scores=validate_notes(previous,read_json(old_notes),sha256(source))
        for row in previous:cache.setdefault(signature(row),(scores[row['id']],study.reference(source),study.reference(old_notes)))
    indexed={n[0]:n for n in notes};reused=[]
    for row in rows:
        if signature(row) in cache:
            score,source,previous_notes=cache[signature(row)]
            indexed[row['id']]=[row['id'],*[score[k] for k in ('grammar','relevance','coherence','completion')],'元raw全項目一致で旧採点継承：'+score['rationale']]
            reused.append(dict(id=row['id'],source=source,notes=previous_notes))
    record['notes']=[indexed[r['id']] for r in rows];record['exact_old_score_reuse']=reused
    validate_notes(rows,record,sha256(raw));destination=study.RUN/'content-notes.json'
    if destination.exists():raise ValueError('Preserve original full content notes')
    atomic_json(destination,record);print(f'All80 bound; exact previous scores reused{len(reused)}')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('observations',type=Path);main(p.parse_args().observations)
