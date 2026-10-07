"""Bounded teacher inference for64 fresh train-only natural-prose documents."""
import hashlib
import json
import os
from pathlib import Path
import random
import sys
import time
os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN']='1'
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
import torch
from transformers import AutoTokenizer,AutoModelForCausalLM,StoppingCriteria,StoppingCriteriaList
from jmicro.experiment import ROOT,read_json,sha256,write_json,now
from jmicro.training import gpu_lock,rng_state,restore_rng
from jmicro.tokenizer import Tokenizer
from phase6_performance import identity,alive
from recover_sarashina_prose_teacher import DATA,RUN as RECOVERY,META

RUN=ROOT/'reports/phase6/sarashina-prose-probe-20261007'
PROPOSAL=ROOT/'reports/phase6/sarashina_prose_feasibility_proposal.json'
SEED=2026100681
NAMES=('歩実','理央','真琴','千紘','直人','春子','光平','美央','晴人','絵里','奏','由季','志穂','遥人','健斗','千夏')
PLACES=('川沿いの遊歩道','港町の商店街','小学校の校庭','町の花屋','祖母の台所','近くの体育館','畑の小道','町の公民館','小さな美術館','家の食卓','海辺の遊歩道','町の市場','学校の玄関','果樹園','家の居間','屋根のある広場')
OBJECTS=('紙の風車','木の椅子','黄色いバケツ','絵の具','小さな苗','折り紙','布の袋','木の箱','赤いリボン','白い皿','手帳','楽器','麦わら帽子','木の実','野菜','古い絵本')
EVENTS=('だれかと協力して準備を終える','小さな失敗から工夫してやり直す','忘れていた約束を思い出す','相手の気持ちに気づいて行動する','使い方を試して仕組みが分かる','天気が変わったので予定を工夫する','困っている人を助ける','準備したものを分け合う')
STYLES=('日常の小さな出来事','子どもにも分かる短い物語','身近な物の仕組みを伝える文章','落ち着いた情景と行動の文章')


def request(index):
    # Hash the independently created scenario before generation; no eval files.
    rng=random.Random(SEED+index)
    scenario=dict(name=rng.choice(NAMES),place=rng.choice(PLACES),object=rng.choice(OBJECTS),event=rng.choice(EVENTS),style=rng.choice(STYLES))
    key=hashlib.sha256(json.dumps(scenario,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    split='dev' if int(key[:8],16)%10==0 else 'train'
    prompt=(f"自然な日本語だけで、{scenario['style']}を一つ書いてください。登場する人は{scenario['name']}、"
        f"場所は{scenario['place']}、使う物は{scenario['object']}です。{scenario['event']}という出来事を含めてください。"
        '小学生に分かる言葉を使い、120～220字、三～六文程度で、出来事の順序と理由が通るようにしてください。'
        '最後は出来事が終わる自然な一文にしてください。タイトル、箇条書き、依頼への返事、文章の解説は書かず、本文だけを出力してください。')
    return dict(id=f'prose-{index:07d}',scenario=scenario,family=key,split=split,prompt=prompt,seed=SEED+index)


def train_requests(count):
    rows=[];seen=set();index=0
    while len(rows)<count:
        row=request(index);index+=1
        if row['split']=='train' and row['family'] not in seen:rows.append(row);seen.add(row['family'])
    return rows


def main():
    torch.set_num_threads(2);RUN.mkdir(parents=True,exist_ok=True)
    p=read_json(PROPOSAL);recovery=read_json(RECOVERY/'result.json');meta=read_json(META)
    if (p['teacher_probe_GPU_limit_seconds']!=180 or p['fixed_source_content_cases']!=64 or p['student_training_started']
            or p['Chat_started'] or p['quantization_started'] or p['teacher_revision']!=meta['revision']):raise ValueError('Bounded teacher-only64 feasibility scope required')
    for relative,digest in p['source_sha256'].items():
        if sha256(ROOT/relative)!=digest:raise ValueError('Frozen teacher probe source differs')
    if read_json(RECOVERY/'job.json')['status']!='complete':raise ValueError('Verified teacher recovery required')
    if recovery['metadata_sha256']!=sha256(META):raise ValueError('Pinned teacher metadata differs')
    for file in recovery['files']:
        path=Path(file['path']);stat=path.stat()
        if stat.st_size!=file['bytes'] or stat.st_mtime_ns!=file['mtime_ns']:raise ValueError('Previously hash-verified teacher changed')
    job_path=RUN/'job.json';old=read_json(job_path) if job_path.exists() else None
    if old and alive(old):raise ValueError('Actual teacher probe live; no duplicate GPU')
    if old and old['status']=='complete':print('Completed teacher64 retained');return
    if old:raise ValueError('Failed teacher probe needs diagnosis/versioned repair, not identical retry')
    job=dict(status='running',**identity(),started_at=now(),proposal_sha256=sha256(PROPOSAL),script_sha256=sha256(Path(__file__)),
        GPU_seconds=0,student_scientific_teacher_tokens=0,optimizer_updates=0,Chat_started=False,quantization_started=False,
        restart_command='scripts/probe_sarashina_prose_teacher.ps1 -Worker')
    write_json(job_path,job);started=None
    def check():
        if started is not None and time.monotonic()-started>180:raise TimeoutError('Teacher64 GPU180s budget exhausted')
    class Deadline(StoppingCriteria):
        def __call__(self,input_ids,scores,**kwargs):check();return False
    def heartbeat(stage,**extra):
        job.update(stage=stage,heartbeat_at=now(),GPU_seconds=0 if started is None else time.monotonic()-started,**extra);write_json(job_path,job)
    try:
        rows=train_requests(64);write_json(RUN/'requests.json',rows)
        student_tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
        before=rng_state()
        with gpu_lock('cuda'):
            started=time.monotonic();heartbeat('load_BF16_teacher')
            tok=AutoTokenizer.from_pretrained(DATA,local_files_only=True,trust_remote_code=False,padding_side='left')
            model=AutoModelForCausalLM.from_pretrained(DATA,local_files_only=True,trust_remote_code=False,dtype=torch.bfloat16,attn_implementation='sdpa').to('cuda').eval()
            eos_ids=model.generation_config.eos_token_id
            eos_ids=[eos_ids] if isinstance(eos_ids,int) else list(eos_ids)
            tok.pad_token_id=tok.eos_token_id;torch.cuda.reset_peak_memory_stats();outputs=[];timings=[]
            for offset in range(0,64,8):
                check();batch=rows[offset:offset+8];torch.manual_seed(SEED+offset);torch.cuda.manual_seed_all(SEED+offset)
                texts=[tok.apply_chat_template([dict(role='user',content=r['prompt'])],tokenize=False,add_generation_prompt=True) for r in batch]
                inputs=tok(texts,padding=True,return_tensors='pt').to('cuda');torch.cuda.synchronize();begin=time.monotonic()
                with torch.inference_mode():
                    ids=model.generate(**inputs,max_new_tokens=256,do_sample=True,temperature=.7,top_p=.8,top_k=20,
                        use_cache=True,stopping_criteria=StoppingCriteriaList([Deadline()]),pad_token_id=tok.pad_token_id)
                torch.cuda.synchronize();seconds=time.monotonic()-begin
                for request_row,sequence in zip(batch,ids[:,inputs.input_ids.shape[1]:].tolist(),strict=True):
                    ends=[i for i,t in enumerate(sequence) if t in eos_ids];real=sequence[:ends[0]+1] if ends else sequence
                    text=tok.decode(real,skip_special_tokens=True).strip();student_ids=student_tok.encode(text)
                    row=dict(**request_row,text=text,teacher_generated_ids=real,teacher_stop='EOS' if ends else 'max_new_tokens',
                        teacher_generated_tokens=len(real),student_body_tokens=len(student_ids),student_body_bytes=len(text.encode()),
                        student_serialized_tokens=len(student_ids)+2,teacher_model=meta['repo_id'],teacher_revision=meta['revision'],
                        generation_batch_seed=SEED+offset)
                    outputs.append(row);write_json(RUN/'raw'/f'{row["id"]}.json',row)
                timings.append(dict(offset=offset,documents=8,seconds=seconds,teacher_tokens=sum(r['teacher_generated_tokens'] for r in outputs[-8:]),student_body_tokens=sum(r['student_body_tokens'] for r in outputs[-8:])))
                heartbeat('generate64',completed_documents=len(outputs))
            check();peak=torch.cuda.max_memory_allocated();del model;torch.cuda.empty_cache();restore_rng(before)
        result=dict(status='actual_teacher64_generation_complete_content_not_yet_accepted',outputs=outputs,timings=timings,
            requests_sha256=sha256(RUN/'requests.json'),script_sha256=job['script_sha256'],proposal_sha256=job['proposal_sha256'],
            teacher_recovery_sha256=sha256(RECOVERY/'result.json'),GPU_seconds=time.monotonic()-started,peak_allocated_bytes=peak,
            student_scientific_teacher_tokens=0,optimizer_updates=0,Chat_started=False,quantization_started=False,protected_test_used=False,
            completed_student_body_tokens=sum(r['student_body_tokens'] for r in outputs),completed_teacher_generated_tokens=sum(r['teacher_generated_tokens'] for r in outputs),
            teacher_EOS_completed=sum(r['teacher_stop']=='EOS' for r in outputs),quality_accepted=False)
        write_json(RUN/'result.json',result);job['status']='complete';heartbeat('complete',completed_documents=64)
        print(json.dumps({k:v for k,v in result.items() if k not in ('outputs','timings')}))
    except BaseException as error:
        job.update(status='failed',error=repr(error));heartbeat('failed');raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python required')
    main()
