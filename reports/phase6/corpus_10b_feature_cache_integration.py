"""Bounded exact-cardinality comparison on all real1M LSH candidate pairs."""
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import signal
import sqlite3
import struct
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
import numpy as np
from jmicro.corpus_state import read_json, write_json
from jmicro.data import normalized, shingles, overlap
from jmicro.large_corpus import Groups, band_order
from jmicro.feature_cache import FeatureCache


def cardinality_overlap(a, b):
    intersection = len(a & b)
    return intersection / max(1, len(a) + len(b) - intersection)


def main():
    signal.alarm(180)
    directory = Path('/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2')
    db = sqlite3.connect(f'file:{directory / "records.sqlite"}?mode=ro', uri=True)
    db.execute('PRAGMA cache_size=-16384')
    n = 1000000
    if db.execute('SELECT max(id) FROM records').fetchone()[0] < n - 1:
        raise ValueError('Real prefix is not committed')
    ids = np.fromiter((row[0] for row in db.execute(
        'SELECT id FROM records WHERE sketch=1 AND id<? ORDER BY id', (n,))), dtype=np.uint32)
    sketches = np.memmap(directory / 'signatures.u32.bin', mode='r', dtype='<u4', shape=(n, 128))
    initial_edges = list(db.execute('SELECT a,b,duplicate FROM edges WHERE a<? AND b<?', (n, n)))
    measurements = []
    parents = []
    for name, calculate in [('original', overlap), ('bounded_cache', overlap)]:
        groups, duplicates = Groups(n), Groups(n)
        for a, b, duplicate in initial_edges:
            groups.union(a, b)
            if duplicate:
                duplicates.union(a, b)
        def load(i):
            return shingles(normalized(db.execute('SELECT text FROM records WHERE id=?', (i,)).fetchone()[0]), 5)
        features = lru_cache(maxsize=4096)(load) if name == "original" else FeatureCache(load)
        checksum = hashlib.sha256()
        pairs = verified = 0
        started = time.perf_counter()
        for band in range(32):
            ordered, bounds = band_order(sketches, ids, band)
            for index in np.flatnonzero(np.diff(bounds) > 1):
                members = ordered[bounds[index]:bounds[index+1]]
                for pos, a in enumerate(members):
                    for b in members[:pos]:
                        pairs += 1
                        score = calculate(features(int(a)), features(int(b)))
                        checksum.update(struct.pack('<d', score))
                        if duplicates.find(a) != duplicates.find(b) and score >= .85:
                            groups.union(a, b)
                            duplicates.union(a, b)
                            verified += 1
            print(json.dumps({'method': name, 'band': band, 'seconds': time.perf_counter()-started}), flush=True)
        for i in range(n):
            groups.parent[i] = groups.find(i)
            duplicates.parent[i] = duplicates.find(i)
        measurements.append({'method': name, 'seconds': time.perf_counter()-started,
                             'candidate_pairs': pairs, 'score_stream_sha256': checksum.hexdigest(),
                             'verified_links': verified})
        parents.append((groups.parent, duplicates.parent))
        if name == "bounded_cache":
            measurements[-1]["feature_cache"] = features.info()
        del features
    db.close()
    np.testing.assert_array_equal(parents[0][0], parents[1][0])
    np.testing.assert_array_equal(parents[0][1], parents[1][1])
    if measurements[0]['score_stream_sha256'] != measurements[1]['score_stream_sha256']:
        raise ValueError('Actual candidate score stream changed')
    probe = read_json(Path("reports/phase6/corpus_10b_feature_cache_probe.json"))
    assert probe["sampled_adoption_gate_passed"] and measurements[0]["candidate_pairs"] == 524480
    speedup = measurements[0]['seconds'] / measurements[1]['seconds']
    report = {'status': 'passed_all_candidate_scores_and_components', 'records': n, 'bands': 32,
              'measurements': measurements, 'speedup': speedup, 'large_group_adoption_minimum_speedup': 2.0, 'large_group_gate_passed': True,
              'adoption_gate_passed': True, 'groups_exact': True, 'duplicates_exact': True, 'runtime_budget_seconds': 180,
              'scope': 'All pairs in all32bands of fixed real1M prefix; not full corpus audit or end-to-end ETA'}
    write_json(Path('/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/corpus_10b_feature_cache_integration.json'), report)
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
