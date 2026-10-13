"""Retain exact source versions named by preparation observations before freeze."""
from pathlib import Path
from chat_lr_contract import RUN, reference
from jmicro.experiment import ROOT, read_json, sha256
from jmicro.training import atomic_json


if __name__ == '__main__':
    current = (ROOT / 'scripts/prepare_chat_lr.py').read_text()
    later = """    consumed = 0
    for row in dry['rows']:
        next_row = dict(row)
        assert row['lr'] == teacher_lr(consumed, row['teachers'], B, CONTROL_SPEC['lr'])
        next_row['lr'] = teacher_lr(consumed, row['teachers'], B, SPEC['lr'])
        consumed += row['teachers']
"""
    earlier = """    for row in dry['rows']:
        next_row = dict(row)
        next_row['lr'] = row['lr'] * (SPEC['lr'] / CONTROL_SPEC['lr'])
"""
    assert current.count(later) == 1
    snapshot = RUN / 'preparation_incident_v1/prepare_chat_lr_split_fix.py'
    assert not snapshot.exists()
    snapshot.write_text(current.replace(later, earlier))
    audit = read_json(RUN / 'dev_audit.json')
    assert sha256(snapshot) == audit['corrected_source']['sha256']
    atomic_json(RUN / 'preparation_source_history.json', dict(passed=True,
        earlier_corrected_overlap_source_at_observation=audit['corrected_source'],
        exact_preserved_snapshot=reference(snapshot),
        current_frozen_source=reference(ROOT / 'scripts/prepare_chat_lr.py'),
        reason='Exact teacher LR formula replaced algebraic scaling before config freeze; original DEV and overlap unchanged',
        new_GPU_updates=0, quality_evidence=False))
    print('Both faulty and corrected preparation source versions preserved by exact original hashes')
