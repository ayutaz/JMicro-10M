"""Read-only counts for pending bands;180seconds, no acceptance changes."""
import json
from pathlib import Path
import signal
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src'))
import numpy as np
from jmicro.corpus_state import read_json, write_json
from jmicro.experiment import now
from jmicro.large_corpus import band_order

signal.alarm(180)
directory = Path('/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2')
scope = read_json(directory / 'parallel_bands/scope.json')
ids = np.load(directory / 'parallel_bands/eligible_ids.npy', mmap_mode='r')
sketches = np.memmap(directory / 'signatures.u32.bin', mode='r', dtype='<u4', shape=(scope['records'],128))
pending = [band for band in range(32) if not (directory / 'parallel_bands' / f'band-{band:02d}.json').exists()]
started = time.perf_counter()
reports = []
for band in pending:
    begin = time.perf_counter()
    ordered, bounds = band_order(sketches, ids, band)
    sizes = np.diff(bounds)
    repeated = sizes[sizes > 1]
    report = {'band':band, 'candidate_pairs':int(np.sum(repeated*(repeated-1)//2)),
              'candidate_groups':len(repeated), 'largest_group':int(sizes.max()),
              'groups_above_builder_cache':int(np.count_nonzero(sizes > 2048)),
              'groups_above_auditor_cache':int(np.count_nonzero(sizes > 4096)),
              'sort_seconds':time.perf_counter()-begin}
    reports.append(report)
    print(json.dumps(report),flush=True)
    del ordered, bounds, sizes, repeated
result = {'status':'readonly_pending_band_counts_complete','observed_at':now(),
          'records':scope['records'],'eligible_records':len(ids),'bands':reports,
          'elapsed_seconds':time.perf_counter()-started,'runtime_budget_seconds':180,
          'scope':'Full actual signature equality candidate counts for bands pending at start only; not completed verification, token count or audit'}
write_json(Path('/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/corpus_10b_pending_bands.json'),result)
print(json.dumps(result),flush=True)
