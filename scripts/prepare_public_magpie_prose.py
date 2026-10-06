"""Prepare a fixed whole-prose source from public train records, CPU only."""
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
import numpy as np
from jmicro.experiment import ROOT,read_json,sha256,write_json,now
from jmicro.tokenizer import Tokenizer
from phase6_performance import identity,alive
from recover_public_magpie_source import RUN as RECOVERY,DATA as RAW,META

RUN=ROOT/'reports/phase6/public-magpie-prose-20261006'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/public-magpie-prose-20261006')
PROPOSAL=ROOT/'reports/phase6/public_magpie_prose_preparation_proposal.json'
SEED=2026100682
TARGET=10_000_000
META_OPEN=re.compile(r'^(?:はい[、。！!]|もちろん|ありがとうございます|ご質問|質問|こちら|以下|承知|かしこまり|それは|そうですね|申し訳|この場合|その場合|この文章|この文は|このテキスト|この問題|まず[、。])')
FORMATTED=re.compile(r'```|<\||\|>|^\s*(?:#{1,6}\s|[-*+•]\s|[0-9]+[.)．]\s)',re.M)


def split_family(user):
    key=hashlib.sha256(user.encode('utf-8')).hexdigest()
    return key,('dev' if int(key[:8],16)%10==0 else 'train')


def candidate(record,tokenizer,protected):
    messages=record.get('conversations',[])
    if len(messages)!=2 or [m.get('role') for m in messages]!=['user','assistant']:return None,'roles'
    user,text=messages[0].get('content'),messages[1].get('content')
    if not isinstance(user,str) or not isinstance(text,str):return None,'missing'
    family,split=split_family(user)
    if split!='train':return None,'reserved_family'
    text=text.strip()
    if not 80<=len(text)<=1800:return None,'characters'
    if META_OPEN.search(text):return None,'context_or_instruction_opening'
    if FORMATTED.search(text):return None,'formatted_or_role'
    if not text.endswith(('。','！','？','」','』')):return None,'unfinished'
    for left,right in (('「','」'),('『','』'),('（','）'),('(',')')):
        if text.count(left)!=text.count(right):return None,'unbalanced'
    if any(prefix in text for prefix in protected):return None,'fixed_dev_overlap'
    letters=[c for c in text if c.isalpha()]
    japanese=sum('\u3040'<=c<='\u30ff' or '\u3400'<=c<='\u9fff' for c in letters)
    if not letters or japanese/len(letters)<.9:return None,'language'
    body=tokenizer.encode(text)
    if not 32<=len(body)<=1022 or any(t<8 for t in body):return None,'body_tokens'
    if tokenizer.decode(body)!=text:return None,'codec'
    return dict(id=f'magpie-{record["id"]}',family=family,split=split,text=text,user_sha256=family,
        raw_id=record['id'],body_tokens=len(body),body_bytes=len(text.encode('utf-8')),body_ids=body),None


def main():
    RUN.mkdir(parents=True,exist_ok=True);DATA.mkdir(parents=True,exist_ok=True)
    p=read_json(PROPOSAL);meta=read_json(META);recovery=read_json(RECOVERY/'result.json')
    if (p['CPU_limit_seconds']!=600 or p['GPU_seconds'] or p['student_scientific_teacher_tokens'] or p['target_serialized_tokens']!=TARGET
            or p['Chat_started'] or p['quantization_started'] or p['source_revision']!=meta['revision']):raise ValueError('Fixed CPU-only public source preparation required')
    for path,digest in p['source_sha256'].items():
        if sha256(ROOT/path)!=digest:raise ValueError('Frozen source preparation code differs')
    if read_json(RECOVERY/'job.json')['status']!='complete' or recovery['metadata_sha256']!=sha256(META):raise ValueError('Verified source required')
    for file in recovery['files']:
        stat=Path(file['path']).stat()
        if stat.st_size!=file['bytes'] or stat.st_mtime_ns!=file['mtime_ns']:raise ValueError('Hash-verified source changed')
    job_path=RUN/'job.json';old=read_json(job_path) if job_path.exists() else None
    if old and alive(old):raise ValueError('Actual CPU source job live')
    if old and old['status']=='complete':print('Completed source preparation retained');return
    if old:raise ValueError('Preserve failed source job; diagnose before a versioned repair')
    job=dict(status='running',**identity(),started_at=now(),proposal_sha256=sha256(PROPOSAL),script_sha256=sha256(Path(__file__)),
        GPU_seconds=0,student_scientific_teacher_tokens=0,Chat_started=False,quantization_started=False,
        restart_command='scripts/prepare_public_magpie_prose.ps1 -Worker')
    started=time.monotonic()
    def check():
        if time.monotonic()-started>600:raise TimeoutError('CPU source600s budget exhausted')
    def heartbeat(stage,**extra):
        job.update(stage=stage,heartbeat_at=now(),CPU_seconds=time.monotonic()-started,**extra);write_json(job_path,job)
    try:
        heartbeat('scan_public_train')
        tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
        fixed=[json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()]
        protected=[r['prefix'] for r in fixed if r['split']=='dev' and len(r['prefix'])>=12]
        accepted=[];rejections=Counter();seen=set();rows=0
        with (RAW/'magpie-sft-v1.0.jsonl').open(encoding='utf-8') as stream:
            for line in stream:
                check();record=json.loads(line);rows+=1;row,reason=candidate(record,tok,protected)
                if reason:rejections[reason]+=1
                else:
                    digest=hashlib.sha256(row['text'].encode()).hexdigest()
                    if digest in seen:rejections['local_exact_duplicate']+=1;continue
                    seen.add(digest);accepted.append(row)
                if rows%5000==0:heartbeat('scan_public_train',scanned_rows=rows,accepted_documents=len(accepted))
        total=sum(r['body_tokens']+2 for r in accepted)
        rng=np.random.default_rng(SEED);order=rng.permutation(len(accepted)).tolist()
        chosen=[];serialized=0
        for index in order:
            if serialized>=TARGET:break
            chosen.append(accepted[index]);serialized+=accepted[index]['body_tokens']+2
        if len(chosen)<64:raise ValueError('Fewer than64 fixed source candidates; no content pilot')
        # Uniform document draw, not byte- or token-weighted sample; no selection
        # using completed Base generation/score/annotations.
        indices=sorted(np.random.default_rng(SEED+1).choice(len(chosen),64,replace=False).tolist())
        samples=[{k:v for k,v in chosen[i].items() if k!='body_ids'} for i in indices]
        write_json(RUN/'fixed64.json',samples)
        write_json(RUN/'source-supply.json',dict(scanned_rows=rows,accepted_documents=len(accepted),candidate_serialized_tokens=total,
            selected_documents=len(chosen),selected_serialized_tokens=serialized,target_serialized_tokens=TARGET,
            target_reached=serialized>=TARGET,rejections=dict(rejections),source=meta['repo_id'],revision=meta['revision']))
        with (DATA/'train-source.jsonl').open('w',encoding='utf-8') as stream:
            for row in chosen:stream.write(json.dumps({k:v for k,v in row.items() if k!='body_ids'},ensure_ascii=False)+'\n')
        lengths=np.array([r['body_tokens']+2 for r in chosen],dtype=np.int64);offsets=np.r_[0,np.cumsum(lengths)[:-1]]
        tokens=np.concatenate([np.array([2,*r['body_ids'],3],dtype=np.uint16) for r in chosen]);focus=np.zeros(len(tokens),dtype=bool)
        np.savez(DATA/'train.npz',tokens=tokens,focus=focus,offsets=offsets,lengths=lengths)
        manifest=dict(kind='public-magpie-whole-plain-prose-v1',source=meta['repo_id'],revision=meta['revision'],license=meta['license'],
            raw_source_sha256=next(f['sha256'] for f in recovery['files'] if f['path'].endswith('.jsonl')),
            source_recovery_sha256=sha256(RECOVERY/'result.json'),documents=len(chosen),serialized_tokens=len(tokens),
            body_tokens=sum(r['body_tokens'] for r in chosen),full_CE_teachers=sum(r['body_tokens']+1 for r in chosen),
            EOS_teachers=len(chosen),focus_teachers=0,arrays_sha256=sha256(DATA/'train.npz'),source_text_sha256=sha256(DATA/'train-source.jsonl'),
            tokenizer_sha256=sha256(tok.path),families=len({r['family'] for r in chosen}),all_train_families=True,
            source_volume_target_reached=serialized>=TARGET,content_accepted=False,
            target_serialized_tokens=TARGET,seed=SEED,proposal_sha256=sha256(PROPOSAL),source_sha256=p['source_sha256'],
            protected_test_used=False,student_scientific_teacher_tokens=0,Chat_started=False,quantization_started=False)
        write_json(DATA/'manifest.json',manifest)
        result=dict(status='actual_CPU_public_prose_candidates_prepared_content_pending',source_supply=read_json(RUN/'source-supply.json'),
            data_directory=str(DATA),manifest_sha256=sha256(DATA/'manifest.json'),fixed64_sha256=sha256(RUN/'fixed64.json'),
            CPU_seconds=time.monotonic()-started,GPU_seconds=0,student_scientific_teacher_tokens=0,optimizer_updates=0,
            Chat_started=False,quantization_started=False,quality_accepted=False,source_volume_target_reached=serialized>=TARGET)
        write_json(RUN/'result.json',result);job['status']='complete';heartbeat('complete',scanned_rows=rows,accepted_documents=len(accepted))
        print(json.dumps(result,ensure_ascii=False))
    except BaseException as error:
        job.update(status='failed',error=repr(error));heartbeat('failed');raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python required')
    main()
