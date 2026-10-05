"""New disjoint train calibration and matched v2 pools; preserve plan61 outputs."""
import argparse
import json
from pathlib import Path
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.complete_units import unit_hash
from jmicro.tokenizer import Tokenizer

DATA = Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-v2-20261005')
RUN = ROOT / 'reports/phase6/condition-v2-100m-20261005'
SEED = 202610064


def excluded_hashes():
    prior = read_json(ROOT / 'reports/phase6/condition_preservation_data_review.json')
    result = {r['text_sha256'] for rows in prior['individual_reviews'].values() for r in rows}
    old = read_json(ROOT / 'reports/phase6/condition_preservation_diagnosis.json')
    result.update(r['text_sha256'] for r in old['source_samples']['rows'])
    return result


def calibrate():
    DATA.mkdir(parents=True, exist_ok=True)
    path = DATA / 'calibration.json'
    assert not path.exists(), 'Do not redraw completed calibration'
    started = time.monotonic()
    origin = Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-preservation-20261005/refined')
    manifest = read_json(origin / 'manifest.json')
    known = excluded_hashes()
    records = [json.loads(line) for line in (origin / 'train.index.jsonl').open()]
    unseen = [r for r in records if r['text_sha256'] not in known]
    selected = np.random.default_rng(SEED).choice(len(unseen), 32, replace=False)
    ids = np.memmap(origin / 'train.bin', dtype='<u2', mode='r')
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    rows = []
    for n, slot in enumerate(selected):
        r = unseen[int(slot)]
        assert r['source'] == 'translation' and r['split'] == 'train'
        text = tok.decode_bytes(ids[r['offset'] + 1:r['offset'] + 1 + r['body_tokens']].tolist()).decode('utf-8').strip()
        assert unit_hash(text) == r['text_sha256']
        rows.append(dict(r, calibration_index=n, text=text))
    result = dict(status='fixed32_pending_individual_diagnosis', rows=rows, seed=SEED,
        origin=str(origin), origin_manifest_sha256=sha256(origin / 'manifest.json'),
        sampling='Uniform32 whole documents from prior-v1 eligible pool, excluding all prior inspected80 and prior source40; calibration, not a representative corpus quality estimate',
        previous_inspected_hashes=sorted(known), seconds=time.monotonic() - started,
        train_only=True, protected_test_used=False, created_at=now(),
        script_sha256=sha256(Path(__file__)))
    write_json(path, result)
    print(json.dumps(dict(status=result['status'], count=32, seconds=result['seconds'])))


if __name__ == '__main__':
    assert sys.version_info[:3] == (3, 12, 7)
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=('calibrate',), default='calibrate')
    args = parser.parse_args()
    calibrate()
