"""Collect saved fixed outputs and unique natural stops for content review."""
import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, write_json, sha256, now


def main():
    plan = read_json(ROOT / 'configs/phase6/eos_5b_finish_100m.json')
    run = ROOT / plan['output']
    parents = read_json(Path(plan['parent_generation']))['generation']['outputs']
    parent = {r['id']:r for r in parents if r['decoding']=='greedy' and r['suppressed']}
    screens = {a:read_json(run/(a+'-evaluation.json'))['generation']['outputs'] for a in ('web','short20')}
    web = {r['id']:r for r in screens['web']}
    fixed = [dict(id=r['id'],prefix=r['prefix'],parent=parent[r['id']]['text'],
        control=web[r['id']]['text'],candidate=r['text'],candidate_EOS=r['stop_reason']=='stop_id',
        candidate_repetition=r['repetition']) for r in screens['short20']]
    unique = {}
    total = 0
    full_path = run/'short20-full-evaluation.json'
    rows = read_json(full_path)['generation']['outputs'] if full_path.exists() else screens['short20']
    for index,row in enumerate(rows):
        if row['stop_reason']!='stop_id':
            continue
        total += 1
        key = (row['id'],row['text'])
        if key not in unique:
            unique[key] = dict(id=row['id'],prefix=row['prefix'],text=row['text'],conditions=[])
        unique[key]['conditions'].append(dict(index=index,decoding=row['decoding'],
            suppressed=row['suppressed'],seed=row.get('seed',42)))
    packet = dict(status='pending_content_review',created_at=now(),fixed80=fixed,
        natural_stops_total=total,unique_natural_stop_texts=list(unique.values()),
        source_sha256={str(p.relative_to(ROOT)):sha256(p) for p in
            [run/'web-evaluation.json',run/'short20-evaluation.json',*([full_path] if full_path.exists() else [])]},
        blind_human_score=False,test_used=False)
    write_json(run/'content-review-packet.json',packet)
    print(dict(fixed80=len(fixed),natural_stops=total,unique_natural_stop_texts=len(unique)))


if __name__=='__main__':
    main()
