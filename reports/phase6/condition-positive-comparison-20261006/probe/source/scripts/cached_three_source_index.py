"""Content-bound compact index cache; preserve the original document order."""
import hashlib
import json
from pathlib import Path

import numpy as np

from jmicro.experiment import read_json, sha256
from jmicro.training import atomic_json
from textbook_quantity_trainer import ThreeSourceIndex, TAG_MAPPING


class CachedThreeSourceIndex(ThreeSourceIndex):
    def __init__(self, view, heartbeat=lambda **_: None):
        detail = view.manifest['splits']['train']
        source = view.directory / 'train.index.jsonl'
        stat = source.stat()
        manifest = sha256(view.directory / 'manifest.json')
        folder = view.directory / ('.compact-index-' + manifest[:16])
        binding = dict(manifest_sha256=manifest, index_sha256=detail['index_sha256'],
                       index_size=stat.st_size, index_mtime_ns=stat.st_mtime_ns,
                       documents=detail['documents'], tokens=len(view.tokens), tags=TAG_MAPPING)
        record = folder / 'ready.json'
        if record.exists():
            kept = read_json(record)
            if kept['binding'] != binding:
                raise ValueError('Cached index source identity differs')
            for name, dtype in (('offsets', np.int64), ('lengths', np.int32), ('sources', np.uint8)):
                path = folder / (name + '.npy')
                if sha256(path) != kept['arrays'][name]:
                    raise ValueError('Cached index array checksum differs')
                values = np.load(path, mmap_mode='r', allow_pickle=False)
                if values.shape != (detail['documents'],) or values.dtype != dtype:
                    raise ValueError('Cached index array shape/dtype differs')
                setattr(self, name, values)
            self.cache_reused = True
            return
        count = detail['documents']
        self.offsets = np.empty(count, dtype=np.int64)
        self.lengths = np.empty(count, dtype=np.int32)
        self.sources = np.empty(count, dtype=np.uint8)
        digest = hashlib.sha256(); offset = 0; read = 0
        # Hash the exact same bytes while parsing, instead of reading 13GB twice.
        with source.open('rb') as stream:
            for i, line in enumerate(stream):
                digest.update(line); row = json.loads(line)
                if (i >= count or row['offset'] != offset or row['split'] != 'train'
                        or type(row['body_tokens']) is not int or not 0 <= row['body_tokens'] < 2**31):
                    raise ValueError('Original index document boundaries differ')
                self.offsets[i], self.lengths[i] = offset, row['body_tokens']
                self.sources[i] = TAG_MAPPING[row['source']]
                offset += row['body_tokens'] + 2; read += 1
                if read % 500000 == 0:
                    heartbeat(index_documents=read, index_total_documents=count)
        after = source.stat()
        if ((after.st_size, after.st_mtime_ns) != (stat.st_size, stat.st_mtime_ns)
                or read != count or offset != len(view.tokens)
                or digest.hexdigest() != detail['index_sha256']):
            raise ValueError('Original index checksum/size/count differs')
        folder.mkdir(exist_ok=True)
        hashes = {}
        for name in ('offsets', 'lengths', 'sources'):
            path = folder / (name + '.npy')
            temporary = folder / (name + '.tmp.npy')
            np.save(temporary, getattr(self, name), allow_pickle=False)
            temporary.replace(path); hashes[name] = sha256(path)
        atomic_json(record, dict(binding=binding, arrays=hashes,
                                 source_hash_verified_during_single_parse=True))
        self.cache_reused = False
