"""Bounded anonymous metadata/card audit of four candidate repositories."""
import hashlib
import json
from pathlib import Path
import sys
import time
from urllib.parse import quote
from urllib.request import urlopen
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,write_json,now,sha256

REPOSITORIES=('kai271/TinyStories-Japanese','aixsatoshi/cosmopedia-japanese-20k',
              'zait-ai/OpenJA','izumi-lab/wikipedia-ja-20230720')
RUN=ROOT/'reports/phase6/public-prose-registry-20261006'


def main():
    target=ROOT/'reports/phase6/public_prose_registry_metadata.json'
    if target.exists():raise ValueError('Preserve completed registry audit')
    RUN.mkdir(parents=True,exist_ok=True)
    started=time.monotonic();rows=[]
    def fetch(url,maximum):
        if time.monotonic()-started>80:raise TimeoutError('Bounded90s metadata audit exhausted')
        with urlopen(url,timeout=10) as response:
            raw=response.read(maximum+1)
        if len(raw)>maximum:raise ValueError('Metadata/card size cap exceeded')
        return raw
    for index,repo in enumerate(REPOSITORIES):
        api='https://huggingface.co/api/datasets/'+repo+'/revision/main?blobs=true'
        raw=fetch(api,4_000_000);info=json.loads(raw)
        (RUN/f'{index}-api.json').write_bytes(raw)
        files=info.get('siblings',[]);card=info.get('cardData',{})
        readme=next((f for f in files if f['rfilename']=='README.md'),None)
        text=None;readme_hash=None;blob_verified=False
        if readme:
            content=fetch('https://huggingface.co/datasets/'+repo+'/resolve/'+info['sha']+'/README.md',100_000)
            (RUN/f'{index}-README.md').write_bytes(content)
            text=content.decode('utf-8');readme_hash=hashlib.sha256(content).hexdigest()
            expected=readme.get('blobId') or readme.get('blob_id')
            if expected:
                blob=hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
                if blob!=expected:raise ValueError('Pinned README Git blob differs')
                blob_verified=True
        hits=[]
        for folder,pattern in (('scripts','*.py'),('configs','*.json')):
            hits.extend(str(p.relative_to(ROOT)) for p in (ROOT/folder).rglob(pattern)
                        if p!=Path(__file__) and repo in p.read_text(encoding='utf-8'))
        rows.append(dict(repository=repo,revision=info['sha'],url='https://huggingface.co/datasets/'+repo,
            private=info.get('private'),gated=info.get('gated'),license=card.get('license'),
            languages=card.get('language'),dataset_info=card.get('dataset_info'),data_configs=card.get('configs'),
            siblings=files,total_repository_bytes=sum(f.get('size') or 0 for f in files),
            card_sha256=readme_hash,card_blob_verified=blob_verified,card_text=text,
            project_exact_repository_hits=hits,api_sha256=hashlib.sha256(raw).hexdigest()))
    result=dict(status='actual_four_repository_metadata_and_cards_complete_not_source_quality',created_at=now(),
        repositories=rows,elapsed_seconds=time.monotonic()-started,runtime_cap_seconds=90,
        source_sha256=sha256(Path(__file__)),bulk_source_bytes_downloaded=0,GPU_seconds=0,
        student_scientific_teacher_tokens=0,optimizer_updates=0,protected_test_used=False,
        Chat_started=False,quantization_started=False,Base_complete=False,Base_adopted=False,
        limits='Exact repository-string search only; no hit is not proof of global source independence. Counts/cards are source claims, not accepted token supply or content quality. No trainer, generation, source filter, or quality threshold changed.')
    write_json(target,result)
    print(json.dumps({k:v for k,v in result.items() if k!='repositories'}))
    for row in rows:
        print(json.dumps({k:row[k] for k in ('repository','revision','license','languages','dataset_info','total_repository_bytes','project_exact_repository_hits')},ensure_ascii=False))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python required')
    main()
