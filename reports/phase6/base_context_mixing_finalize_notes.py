"""Assemble all80 individual observations; reuse scores only for 11 exact CE rows."""
import csv
import sys
from pathlib import Path
sys.path[:0] = [str(Path.cwd() / 'src'), str(Path.cwd() / 'scripts')]
from jmicro.experiment import ROOT, read_json, sha256
from jmicro.training import atomic_json
from review_textbook_quantity_comparison import validate_notes

phase = ROOT / 'reports/phase6'
raw = phase / 'base-context-mixing-comparison-20261007/evaluation/context_mixing/evaluation/generation.json'
rows = read_json(raw)['outputs']
control = phase / 'natural-context-contrast-comparison-20261007/evaluation/CE/evaluation/generation.json'
old = {r['id']: r for r in read_json(control)['outputs']}
old_notes = {n[0]: n for n in read_json(phase / 'natural_context_contrast_CE_notes.json')['notes']}
changes = phase / 'base_context_mixing_changed_observations.tsv'
with changes.open(encoding='utf-8', newline='') as f:
    observations = list(csv.DictReader(f, delimiter='\t'))
changed = {r['id']: [r['id'], *[int(r[k]) for k in ('grammar','relevance','coherence','completion')], r['rationale']] for r in observations}
assert len(observations) == len(changed) == 69
all_notes, reused, table = [], [], []
for row in rows:
    exact = all(row[k] == old[row['id']][k] for k in ('prefix','text','generated_ids','stop_reason'))
    if exact:
        assert row['id'] not in changed
        n = old_notes[row['id']]
        reused.append(row['id'])
    else:
        n = changed[row['id']]
    all_notes.append(n)
    table.append([*n, str(exact).lower()])
assert len(reused) == 11
target = phase / 'base_context_mixing_observations.tsv'
assert not target.exists() and not (phase / 'base_context_mixing_notes.json').exists()
with target.open('w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter='\t', lineterminator='\n')
    writer.writerow(['id','grammar','relevance','coherence','completion','rationale','exact_CE_score_reused'])
    writer.writerows(table)
notes = dict(reviewer='Codex nonblind; all80 individually read; 69 changed outputs individually scored, 11 exact CE outputs retain unchanged existing scores and reasons',
    independent_human_blind=False, generation_sha256=sha256(raw), notes=all_notes,
    exact_CE_score_reuse_count=len(reused), exact_CE_reused_ids=reused,
    changed_outputs_individually_scored=len(changed),
    observations=dict(path=str(target), sha256=sha256(target)))
validate_notes(rows, notes, sha256(raw))
atomic_json(phase / 'base_context_mixing_notes.json', notes)
print('All80 notes validated: 69 changed, 11 exact CE reused; no quality pass claimed')
