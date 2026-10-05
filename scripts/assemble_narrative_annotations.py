"""Join individually authored scores with their raw-generation hash; never infer scores."""
import argparse
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from run_narrative_comparison import RUN

parser=argparse.ArgumentParser();parser.add_argument('--stage',choices=('compare','expand'),default='compare');args=parser.parse_args()
arms=['mixed-control','mixed-diverse'] if args.stage=='compare' else ['mixed-expanded']
result=dict(arms={},reviewer='Codex individual raw-text judgments; not independent blind human evaluation',created_at=now())
for arm in arms:
    label=arm.removeprefix('mixed-')
    notes=read_json(ROOT/f'reports/phase6/narrative_diversity_{label}_notes.json')
    path=RUN/'evaluation'/arm/'evaluation/generation.json';rows=read_json(path)['outputs']
    assert len(notes)==len(rows)==80 and [n[0] for n in notes]==[r['id'] for r in rows]
    assert all(len(n)==6 and n[5] for n in notes)
    result['arms'][arm]=dict(notes=notes,generation_sha256=sha256(path),notes_sha256=sha256(ROOT/f'reports/phase6/narrative_diversity_{label}_notes.json'))
write_json(RUN/(args.stage+'-annotations.json'),result)
print('Bound all individual content notes to original raw generation')
