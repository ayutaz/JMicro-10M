"""Bind the individually read material notes to every sampled original text."""
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now

data=Path('/home/aihub_ubuntu/jmicro-data/phase6/narrative-diversity-v2-20261005')
run=ROOT/'reports/phase6/narrative-diversity-v2-20261005'
sample=data/'sample-initial.json';notes_path=ROOT/'reports/phase6/narrative_diversity_notes.json'
rows=read_json(sample);notes=read_json(notes_path)
assert len(rows)==len(notes)==64 and [r[0] for r in notes]==list(range(64))
assert all(isinstance(n[1],bool) and n[2] for n in notes)
ready=read_json(data/'ready-initial.json');assert ready['sample_sha256']==sha256(sample)
reviews=[dict(slot=i,document=row,weak=n[1],rationale=n[2]) for i,(row,n) in enumerate(zip(rows,notes,strict=True))]
report=dict(sample_sha256=sha256(sample),notes_sha256=sha256(notes_path),documents=64,
    weak_documents=sum(n[1] for n in notes),weak_limit=10,reviews=reviews,
    independent_human_certification=False,
    rubric='Self-contained subject/object/time/causal progression and meaningful closure. Fantasy alone is not an error; decisive ambiguity, contradiction, broken grammar or absent referenced continuation is weak.',
    limitations='This semantic review does not certify realism or absence of fantasy. Lexical story filters did not remove all fantasy or direct speech. Natural source names remain; material is not name-substitution generation.',
    ready_sha256=sha256(data/'ready-initial.json'),reviewed_at=now())
write_json(run/'content-review.json',report)
write_json(ROOT/'reports/phase6/narrative_diversity_material_review.json',report)
print(json.dumps(dict(weak=report['weak_documents'],documents=64,passed=report['weak_documents']<=10)),flush=True)
