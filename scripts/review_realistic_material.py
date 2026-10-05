"""Bind actual fixed source samples to specific Codex reviews; never reroll."""
import argparse
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now


def review(data,run,notes_path):
    ready=read_json(data/'ready.json');sample=read_json(data/'sample64.json')
    assert ready['sample_sha256']==sha256(data/'sample64.json') and len(sample)==64
    notes=read_json(notes_path)['notes']
    assert len(notes)==64 and [n[0] for n in notes]==list(range(64))
    assert all(n[1] in (0,1) and len(n[2])>=12 for n in notes)
    rows=[dict(id=sample[i]['id'],weak=bool(weak),reason=reason,text=sample[i]['text']) for i,weak,reason in notes]
    weak=sum(r['weak'] for r in rows)
    report=dict(status='content_readiness_passed' if weak<=10 else 'content_readiness_failed',
        documents=64,weak_documents=weak,maximum_weak_documents=10,passed=weak<=10,
        sample_sha256=ready['sample_sha256'],ready_sha256=sha256(data/'ready.json'),
        notes_sha256=sha256(notes_path),reviews=rows,independent_human_blind=False,reviewer='Codex nonblind',
        limitation='Readiness of sampled language and local coherence, not fact verification or a full corpus audit',created_at=now())
    write_json(run/'content-review.json',report)
    print(f"Readiness {'passed' if report['passed'] else 'failed'}: weak{weak}/64",flush=True)
    return report


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True);p.add_argument('--run',type=Path,required=True);p.add_argument('--notes',type=Path,required=True);a=p.parse_args()
    review(a.data,a.run,a.notes)
