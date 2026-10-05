"""Pin Japanese Wikipedia source metadata for a new bounded material comparison."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from huggingface_hub import HfApi
from jmicro.experiment import ROOT,write_json,now

if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    repo='wikimedia/wikipedia';info=HfApi(token=False).dataset_info(repo,files_metadata=True,timeout=30)
    files=[dict(path=f.rfilename,size=f.size,sha256=f.lfs.sha256 if f.lfs else None) for f in info.siblings if f.rfilename.startswith('20231101.ja/') and f.rfilename.endswith('.parquet')]
    assert files
    result=dict(repository=repo,revision=info.sha,subset='20231101.ja',files=files,
        license='CC-BY-SA-3.0 / GFDL, per dataset card; per-article attribution retained',
        dataset_card='https://huggingface.co/datasets/'+repo,
        proposed_use='Literal whole opening paragraph with explicit topic; article-family split;10M pilot, fresh matched comparison',
        maximum_raw_bytes=2000000000,CPU_budget_seconds=600,protected_test_used=False,created_at=now())
    write_json(ROOT/'reports/phase6/wikipedia_source_pin.json',result);print(result,flush=True)
