"""Pin public train supply for plan58, without validation/test acquisition."""
import json
from pathlib import Path
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from huggingface_hub import HfApi, hf_hub_download
from jmicro.experiment import ROOT, write_json, sha256, now

DATA = Path('/home/aihub_ubuntu/jmicro-data/phase6/dataset-expansion-20261005')

def main():
    assert sys.version_info[:3] == (3, 12, 7)
    DATA.mkdir(parents=True, exist_ok=True)
    receipt = DATA / 'supply.json'
    if receipt.exists():
        print(receipt.read_text(), flush=True)
        return
    started = time.monotonic()
    records = {}
    for repository in ('shibatch/TinyStories-JA', 'KeisukeMiyamoto/SyntheticTextbook-jp'):
        try:
            info = HfApi(token=False).dataset_info(repository, files_metadata=True)
            card = Path(hf_hub_download(repository, 'README.md', repo_type='dataset', revision=info.sha, token=False))
            destination = DATA / (repository.split('/')[0] + '.README.source.md')
            destination.write_bytes(card.read_bytes())
            records[repository] = dict(repository=repository, revision=info.sha,
                license=info.card_data.get('license') if info.card_data else None,
                card_sha256=sha256(destination), card_path=str(destination),
                files=[dict(path=f.rfilename, bytes=f.size, sha256=f.lfs.sha256 if f.lfs else None)
                       for f in info.siblings if 'train' in f.rfilename and f.rfilename.endswith(('.parquet', '.jsonl', '.jsonl.gz'))],
                declared_notes=destination.read_text()[:12000])
        except Exception as error:
            records[repository] = dict(error_type=type(error).__name__, error=str(error))
    result = dict(status='pinned_supply_pending_inspection', started_at=now(), seconds=time.monotonic()-started,
        sources=records, official_validation_test_acquired=False, preparation_budget_seconds=1800)
    write_json(receipt, result)
    print(json.dumps(result, ensure_ascii=False), flush=True)

if __name__ == '__main__':
    main()
