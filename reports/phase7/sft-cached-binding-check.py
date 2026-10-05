import json
import sys
import time
from functools import lru_cache
from pathlib import Path
sys.path.insert(0, 'src')
from jmicro.assistant_sampler import AssistantSampler
from jmicro.experiment import ROOT, read_json, sha256, write_json, now
from jmicro.tokenizer import Tokenizer
started = time.perf_counter()
data = Path('/home/aihub_ubuntu/jmicro-data/phase7/real-persona-pilot-20261006')
m = read_json(data/'manifest.json')
assert sha256(data/'train.jsonl') == m['train_records_sha256']
with (data/'train.jsonl').open() as stream: records = [json.loads(line) for line in stream]
tok = Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
assert sha256(tok.path) == m['tokenizer_sha256']
tok.encode = lru_cache(maxsize=100000)(tok.encode)
s = AssistantSampler(records,tok,1024,42)
assert s.binding == m['dialogue_binding']
assert len(s.windows) == m['splits']['train']['prepared_SFT_windows']
report = dict(status='cached_encoding_matches_frozen_all_train_SFT_masks',train_dialogues=len(records),windows=len(s.windows),binding=s.binding,source_manifest_sha256=sha256(data/'manifest.json'),CPU_seconds=time.perf_counter()-started,cache_info=dict(hits=tok.encode.cache_info().hits,misses=tok.encode.cache_info().misses),GPU_learning_tokens=0,quality_evaluated=False,protected_test_used=False,created_at=now())
write_json(ROOT/'reports/phase7/sft_cached_binding_check.json',report)
print(json.dumps(report),flush=True)