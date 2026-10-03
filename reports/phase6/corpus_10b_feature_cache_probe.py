"""Exact hot-group cache comparison,360seconds; production remains unchanged."""
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import signal
import sqlite3
import struct
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src'))
import numpy as np
from jmicro.corpus_state import read_json, write_json
from jmicro.data import normalized, overlap, shingles
from jmicro.experiment import now
from jmicro.feature_cache import FeatureCache
from jmicro.large_corpus import band_order

signal.alarm(360)
directory = Path('/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2')
scope = read_json(directory / 'parallel_bands/scope.json')
ids = np.load(directory / 'parallel_bands/eligible_ids.npy', mmap_mode='r')
sketches = np.memmap(directory / 'signatures.u32.bin', mode='r', dtype='<u4', shape=(scope['records'],128))
db = sqlite3.connect(f'file:{directory / "records.sqlite"}?mode=ro', uri=True)
db.execute('PRAGMA cache_size=-16384')
started = time.perf_counter()
reports = []
for band in (23, 27, 30):
    ordered, bounds = band_order(sketches, ids, band)
    index = int(np.argmax(np.diff(bounds)))
    members = ordered[bounds[index]:bounds[index+1]].copy()
    del ordered, bounds
    if len(members) < 2066:
        raise ValueError('Measured hot group differs')
    measurements = []
    for name in ('original_lru2048', 'bounded8192'):
        def load(i):
            return shingles(normalized(db.execute('SELECT text FROM records WHERE id=?',(i,)).fetchone()[0]),5)
        features = lru_cache(maxsize=2048)(load) if name == 'original_lru2048' else FeatureCache(load)
        checksum = hashlib.sha256()
        pairs = positives = 0
        begin = time.perf_counter()
        # Positions beyond2048 exercise the measured cache overflow explicitly.
        for position in range(2050,2066):
            a = int(members[position])
            for b in members[:position]:
                score = overlap(features(a),features(int(b)))
                checksum.update(struct.pack('<d',score))
                pairs += 1
                positives += score >= .85
        elapsed = time.perf_counter()-begin
        info = features.cache_info()._asdict() if name == 'original_lru2048' else features.info()
        measurements.append(dict(method=name,seconds=elapsed,pairs=pairs,positives=positives,
                                 score_stream_sha256=checksum.hexdigest(),sample_cache=info))
        print(json.dumps({'band':band,**measurements[-1]}),flush=True)
        if name == 'bounded8192':
            for i in members:
                features(int(i))
            full_group_info = features.info()
            del features
    scores_equal = measurements[0]['score_stream_sha256'] == measurements[1]['score_stream_sha256']
    if not scores_equal:
        raise ValueError('Actual score stream differs')
    result = dict(band=band,group_records=len(members),
                  group_ids_sha256=hashlib.sha256(members.astype('<u4').tobytes()).hexdigest(),
                  measurements=measurements,score_streams_exact=True,
                  speedup=measurements[0]['seconds']/measurements[1]['seconds'],
                  full_group_cache=full_group_info,
                  whole_group_fits=full_group_info['entries']==len(members))
    reports.append(result)
    print(json.dumps(result),flush=True)
db.close()
report = dict(status='passed_actual_group_sample_scores',observed_at=now(),records=scope['records'],
              bands=reports,minimum_adoption_speedup=2.0,
              sampled_adoption_gate_passed=all(r['speedup']>=2 and r['whole_group_fits'] for r in reports),
              full1m_component_gate='pending',runtime_budget_seconds=360,
              elapsed_seconds=time.perf_counter()-started,
              scope='Fixed32920 actual pairs from each measured largest group plus bounded whole-group retention; not full pair or full corpus audit; full1M integration comparison required before adoption')
write_json(Path('/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/corpus_10b_feature_cache_probe.json'),report)
print(json.dumps(report),flush=True)
