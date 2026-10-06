"""Find actual maximum source window via compact arrays, not13GB JSON scan."""
import hashlib
import json
from pathlib import Path
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import numpy as np
from jmicro.experiment import ROOT, sha256, now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from natural_context_contrast_corpus import document_windows

OUT = ROOT/'reports/phase6/natural_context_contrast_capacity_preparation.json'
RUN = Path('/home/aihub_ubuntu/jmicro-data/phase6/natural-context-contrast-capacity-20261007')


def index_record(path, target_offset):
    low, high = 0, path.stat().st_size
    with path.open('rb') as stream:
        for _ in range(64):
            if low >= high:
                break
            middle = (low+high)//2
            stream.seek(max(0, middle-1))
            previous = stream.read(1) if middle else b'\n'
            stream.seek(middle)
            if previous != b'\n':
                stream.readline(16384)
            position = stream.tell()
            raw = stream.readline(16385)
            if not raw:
                high = middle
                continue
            if len(raw) > 16384:
                raise ValueError('Bounded original index record exceeded16KiB')
            row = json.loads(raw)
            if row['offset'] == target_offset:
                return position, raw, row
            if row['offset'] < target_offset:
                low = stream.tell()
            else:
                high = middle
    raise ValueError('Actual compact-array document offset lacks matching original index record')


def main():
    if OUT.exists():
        raise ValueError('Preserve completed maximum-source geometry measurement')
    started = time.monotonic()
    preparation = ROOT/'reports/phase6/natural_context_contrast_corpus_preparation.json'
    data = json.loads(preparation.read_text())
    binding = data['source_binding']
    pool = Path(binding['pool'])
    cache = pool/('.compact-index-'+binding['manifest_sha256'][:16])
    if sha256(cache/'ready.json') != binding['ready_sha256']:
        raise ValueError('Already verified compact source cache binding differs')
    ready = json.loads((cache/'ready.json').read_text())
    arrays = {}
    for name, dtype in (('offsets', np.int64), ('lengths', np.int32)):
        path = cache/(name+'.npy')
        if sha256(path) != ready['arrays'][name]:
            raise ValueError('Existing compact array content differs')
        arrays[name] = np.load(path, mmap_mode='r', allow_pickle=False)
        if arrays[name].dtype != dtype:
            raise ValueError('Actual compact index dtype differs')
    index = int(arrays['lengths'].argmax())
    count, offset = int(arrays['lengths'][index]), int(arrays['offsets'][index])
    location, raw, record = index_record(pool/'train.index.jsonl', offset)
    if record['split'] != 'train' or record['body_tokens'] != count:
        raise ValueError('Actual maximum original TRAIN unit differs')
    tokens = np.memmap(pool/'train.bin', dtype='<u2', mode='r')
    serialized = tokens[offset:offset+count+2].tolist()
    if serialized[0] != 2 or serialized[-1] != 3:
        raise ValueError('Maximum unit original BOS/EOS differs')
    tokenizer = Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    body_bytes = tokenizer.decode_bytes(serialized[1:-1])
    if hashlib.sha256(body_bytes).hexdigest() != record['canonical_sha256']:
        raise ValueError('Maximum unit original canonical bytes differ')
    window = max(document_windows(serialized[1:-1]), key=lambda w: len(w['input_ids']))
    RUN.mkdir(parents=True, exist_ok=True)
    payload = RUN/'maximum-original-window.json'
    atomic_json(payload, dict(original_record=record, index_byte_position=location,
        index_record_sha256=hashlib.sha256(raw).hexdigest(), window=window))
    seconds = time.monotonic()-started
    if seconds > 30:
        raise TimeoutError('Maximum-source geometry CPU30s exhausted')
    report = dict(status='actual_maximum_original_source_window_prepared', created_at=now(),
        corpus_preparation=dict(path=str(preparation), sha256=sha256(preparation)),
        payload=dict(path=str(payload), sha256=sha256(payload)), compact_arrays_once_SHA_verified=True,
        maximum_original_body_tokens=count, maximum_actual_CE_input_tokens=len(window['input_ids']),
        source_family=record['source_family'], source=record['source'], index_byte_position=location,
        original_body_sha256=record['canonical_sha256'], original_index_record_sha256=hashlib.sha256(raw).hexdigest(),
        CPU_seconds=seconds, scientific_teacher_tokens=0, optimizer_updates=0, GPU_seconds=0,
        old_index_JSON_full_scan=False, old_token_stream_full_scan=False, Base_complete=False,
        Chat_started=False, quantization_started=False,
        purpose='Conservative physical-shape CUDA forward/backward capacity stress using repetitions of this actual original context. This is not a contrastive negative batch, model-quality test or scientific learning. Native two-branch feature stress uses the same maximum allowed context to bound allocation.',
        limitations='Compact length/offset arrays are scanned/hashed once (about200MB);13GB JSON and4GB TRAIN stream are not scanned. Content/teacher-transfer criteria unchanged; source quantity is reused, not new supply.')
    atomic_json(OUT, report)
    print(json.dumps({k:report[k] for k in ('maximum_original_body_tokens','maximum_actual_CE_input_tokens','CPU_seconds')}))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
