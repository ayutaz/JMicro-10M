"""Acquire one pinned public train shard and measure whole-story supply."""
from collections import Counter
import json
from pathlib import Path
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from huggingface_hub import hf_hub_download
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.tokenizer import Tokenizer
from probe_dataset_expansion_supply import DATA
from prepare_story_text import story_candidate
from jmicro.whole_short_text import whole_candidate

def main():
    assert sys.version_info[:3] == (3,12,7)
    source = read_json(DATA/'supply.json')['sources']['shibatch/TinyStories-JA']
    item = source['files'][0]
    started = time.monotonic()
    destination = Path(hf_hub_download(source['repository'], item['path'], revision=source['revision'],
        repo_type='dataset', token=False))
    assert destination.stat().st_size == item['bytes'] and sha256(destination) == item['sha256']
    tok = Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    histogram = Counter(); selected = Counter(); examples = []; rows = 0
    with destination.open() as stream:
        for line in stream:
            record = json.loads(line); text = record['text_ja']; ids = tok.encode(text); rows += 1
            histogram['le128' if len(ids)<=128 else 'le384' if len(ids)<=384 else 'le512' if len(ids)<=512 else 'over512'] += 1
            old = story_candidate(text, tok)
            full = whole_candidate(text, len(ids), 'web')
            if old: selected['old_selection_rows'] += 1; selected['old_selection_tokens'] += len(ids)+2
            if full: selected['whole_64_384_rows'] += 1; selected['whole_64_384_tokens'] += len(ids)+2
            if len(examples) < 12: examples.append(dict(text=text, body_tokens=len(ids), old_accepted=bool(old), whole_accepted=bool(full)))
            if rows == 10000: break
    result = dict(status='inspected', source=source, file=item, local_path=str(destination),
        records_inspected=rows, histogram=dict(histogram), selection=dict(selected), examples=examples,
        seconds=time.monotonic()-started, checked_at=now(), official_validation_test_acquired=False)
    write_json(DATA/'source-inspection.json', result)
    print(json.dumps(result, ensure_ascii=False), flush=True)

if __name__=='__main__': main()
