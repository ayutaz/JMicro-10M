"""Pin public narrative source metadata before downloading any text."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from huggingface_hub import HfApi
from jmicro.experiment import ROOT,write_json,now

if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    repo='globis-university/aozorabunko-clean'
    info=HfApi(token=False).dataset_info(repo,files_metadata=True,timeout=30)
    files=[dict(path=f.rfilename,size=f.size,sha256=f.lfs.sha256 if f.lfs else None) for f in info.siblings]
    result=dict(repository=repo,revision=info.sha,files=files,license='CC-BY-4.0',
        dataset_card='https://huggingface.co/datasets/'+repo,
        filter='meta文字遣い種別=新字新仮名, works marked copyrightなし; keep work/person/library-card attribution',
        proposed_use='Separate narrative source after two bounded Web revisions; paragraph units with whole-work family split; genre and historical-style limitation retained',
        maximum_raw_bytes=500000000,protected_test_used=False,created_at=now())
    write_json(ROOT/'reports/phase6/aozora_source_pin.json',result)
    print(result,flush=True)
