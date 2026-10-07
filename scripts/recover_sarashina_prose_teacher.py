"""Durably recover exactly one anonymously accessible public BF16 teacher."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import time
os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN']='1'
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from huggingface_hub import hf_hub_download
from jmicro.experiment import ROOT,read_json,sha256,now,write_json
from phase6_performance import identity,alive

RUN=ROOT/'reports/phase6/sarashina-prose-recovery-20261007'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/sarashina-prose-teacher-20261007/model')
META=ROOT/'reports/phase6/sarashina_prose_teacher_metadata.json'


def main():
    RUN.mkdir(parents=True,exist_ok=True);DATA.mkdir(parents=True,exist_ok=True)
    job_path=RUN/'job.json';prior=read_json(job_path) if job_path.exists() else None
    if prior and alive(prior):raise ValueError('Actual recovery process live; no duplicate')
    if prior and prior['status']=='complete':print('Completed verified recovery retained');return
    meta=read_json(META)
    if meta['private'] or meta['gated'] or meta['license']!='mit':raise ValueError('Public MIT model required')
    if shutil.disk_usage(DATA).free < meta['total_bytes']+2_000_000_000:raise ValueError('Insufficient native disk for pinned teacher')
    job=dict(status='running',**identity(),started_at=now(),metadata_sha256=sha256(META),
        script_sha256=sha256(Path(__file__)),restart_command='scripts/recover_sarashina_prose_teacher.ps1 -Worker',
        GPU_seconds=0,student_scientific_teacher_tokens=0,project_Chat_started=False,student_quantization_started=False)
    started=time.monotonic()
    def persist(stage,**extra):
        job.update(stage=stage,heartbeat_at=now(),elapsed_seconds=time.monotonic()-started,**extra)
        write_json(job_path,job)
    try:
        persist('recovering');verified=[]
        for file in meta['files']:
            if time.monotonic()-started>1800:raise TimeoutError('Native teacher recovery1800s budget exhausted')
            target=DATA/file['path'];proof=RUN/'verified'/f'{file["path"]}.json'
            if proof.exists():
                saved=read_json(proof)
                if (target.exists() and saved['metadata_sha256']==sha256(META)
                        and saved['bytes']==target.stat().st_size and saved['mtime_ns']==target.stat().st_mtime_ns):
                    verified.append(saved);continue
            persist('download',file=file['path'],verified_files=len(verified))
            path=Path(hf_hub_download(meta['repo_id'],file['path'],revision=meta['revision'],token=False,local_dir=DATA))
            persist('verify',file=file['path'])
            if path!=target or path.stat().st_size!=file['bytes']:raise ValueError('Recovered path/size differs')
            content_sha=sha256(path)
            if file['lfs']:
                if content_sha!=file['lfs']['sha256']:raise ValueError('Pinned LFS content SHA differs')
            else:
                content=path.read_bytes()
                blob=hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
                if blob!=file['blob_id']:raise ValueError('Pinned Git blob differs')
            record=dict(path=str(path),sha256=content_sha,bytes=path.stat().st_size,mtime_ns=path.stat().st_mtime_ns,
                metadata_sha256=sha256(META),source_revision=meta['revision'])
            write_json(proof,record);verified.append(record)
        result=dict(status='actual_public_BF16_teacher_recovered_all_hashes_verified',repo_id=meta['repo_id'],revision=meta['revision'],
            license=meta['license'],metadata_sha256=sha256(META),model_directory=str(DATA),files=verified,
            actual_recovery_seconds=time.monotonic()-started,**identity(),anonymous_access=True,
            GPU_seconds=0,student_scientific_teacher_tokens=0,project_Chat_started=False,student_quantization_started=False)
        write_json(RUN/'result.json',result);job['status']='complete';persist('complete')
        print(json.dumps({k:v for k,v in result.items() if k!='files'}))
    except BaseException as error:
        job.update(status='failed',error=repr(error));persist('failed');raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python required')
    main()
