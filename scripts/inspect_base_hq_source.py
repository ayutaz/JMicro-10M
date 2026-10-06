"""Bounded public source metadata/HTTP range feasibility, no corpus download."""
import json
from pathlib import Path
import sys
import time
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,now,sha256
from jmicro.training import atomic_json

REPO='epfml/FineWeb2-HQ'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/base-hq-feasibility-20261007')
OUT=ROOT/'reports/phase6/base_hq_source_feasibility.json'


def main():
    if OUT.exists():raise ValueError('Preserve original source metadata observation')
    start=time.monotonic();DATA.mkdir(parents=True,exist_ok=True)
    def read(url,maximum,headers=None):
        if time.monotonic()-start>30:raise TimeoutError('Public source metadata30s exhausted')
        request=urllib.request.Request(url,headers={'User-Agent':'JMicro-10M bounded local Base source feasibility',**(headers or {})})
        with urllib.request.urlopen(request,timeout=15) as response:
            content=response.read(maximum+1)
            if len(content)>maximum:raise ValueError('Bounded metadata response exceeded ceiling')
            return content,response.status,{k:response.headers.get(k) for k in ('Content-Range','Content-Length','Content-Type')}
    raw,status,_=read('https://huggingface.co/api/datasets/'+REPO,8000000);info=json.loads(raw)
    if info.get('private') or info.get('gated'):raise ValueError('Public ungated source metadata required')
    revision=info['sha'];japanese=[v['rfilename'] for v in info['siblings'] if 'jpn_Jpan' in v['rfilename'] and v['rfilename'].endswith('.parquet')]
    if len(revision)!=40 or not japanese:raise ValueError('Pinned Japanese Parquet source required')
    metadata=DATA/'repository.json';metadata.write_bytes(raw)
    card,_,_=read(f'https://huggingface.co/datasets/{REPO}/resolve/{revision}/README.md',300000);card_path=DATA/'README.md';card_path.write_bytes(card)
    path=sorted(japanese)[0];url=f'https://huggingface.co/datasets/{REPO}/resolve/{revision}/{path}'
    # Read just the four-byte magic; close even if the server ignores Range. Never log redirected signed URLs.
    request=urllib.request.Request(url,headers={'Range':'bytes=0-3','User-Agent':'JMicro-10M bounded local Base source feasibility'})
    with urllib.request.urlopen(request,timeout=15) as response:
        prefix=response.read(4);range_status=response.status;content_range=response.headers.get('Content-Range')
    if prefix!=b'PAR1':raise ValueError('Actual Parquet header required')
    report=dict(status='public_Japanese_HQ_metadata_and_range_observed',created_at=now(),repository=REPO,revision=revision,
        private=False,gated=False,license=info.get('cardData',{}).get('license'),metadata=dict(path=str(metadata),sha256=sha256(metadata)),
        README=dict(path=str(card_path),sha256=sha256(card_path)),Japanese_Parquet_files=len(japanese),first_file=path,
        actual_magic=prefix.decode(),range_HTTP_status=range_status,Content_Range=content_range,HTTP_range_supported=range_status==206 and bool(content_range),
        wall_seconds=time.monotonic()-start,corpus_records_downloaded=0,prepared_training_tokens=0,GPU_seconds=0,
        scientific_teacher_tokens=0,Base_complete=False,Chat_started=False,quantization_started=False,
        source_card='https://huggingface.co/datasets/epfml/FineWeb2-HQ',paper='https://arxiv.org/abs/2502.10361',
        published_claims='Top10percent classifier-ranked FineWeb2 per language; Japanese34,185,427documents/393G including embeddings. Published1B-model benchmark efficiencies are not a verified10M Japanese speed or quality gain.',
        next_action='Only if actual ranges work: implement pinned footer/selected-column reader, freeze TRAIN-family64 sample and tokenizer-bound supply estimate under download60s/CPU30s and100MiB remote-byte ceiling. Skip embedding columns and all-corpus scans. No learning/source acceptance claim from metadata.',
        limitations='Same FineWeb2 ancestry as current Edu corpus; global source/test overlap must be bound using existing IDs/protected family registries before any learning. Scored HQ documents may still be noisy; source suitability and additional native-token supply are unmeasured.')
    if report['wall_seconds']>30:raise TimeoutError('Metadata30s exhausted')
    atomic_json(OUT,report);print({k:report[k] for k in ('revision','Japanese_Parquet_files','range_HTTP_status','Content_Range','wall_seconds')})


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
