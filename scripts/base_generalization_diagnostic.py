"""Fixed article-family DEV selection and exact role-free completion scoring."""
from collections import Counter
import hashlib
import math
import random
import re
import tarfile
import torch
from torch.nn import functional as F
from prepare_livedoor_leads import family_split, first_lead
from base_preference_loss import collate_continuations


def original_continuation(row, ids, tok):
    raw=tok.decode_bytes(ids)
    if raw!=row['text'].encode('utf-8') or hashlib.sha256(raw).hexdigest()!=row['canonical_sha256']:
        raise ValueError('Original body/provenance differs')
    cut=max(8,len(ids)//4)
    while cut<len(ids):
        try:prefix=tok.decode_bytes(ids[:cut]).decode('utf-8');break
        except UnicodeDecodeError:cut+=1
    else:raise ValueError('Nonempty original suffix with valid UTF8 prefix required')
    chosen=[*ids[cut:],3];body=tok.decode_bytes(chosen[:-1]);body.decode('utf-8')
    return dict(id=row['doc_id'],source_family=row['source_family'],split=row['split'],category=row['category'],
        source_text_sha256=row['canonical_sha256'],source_URL=row['source_URL'],original_article_sha256=row['original_article_sha256'],
        prompt_ids=[2,*ids[:cut]],chosen_ids=chosen,prefix=prefix,original_body_ids=ids,
        chosen_body_bytes=len(body),chosen_body_tokens=len(chosen)-1)


def select_dev(archive,tok,count,seed,check):
    """TEST/TRAIN bodies never decoded; fixed rules and draw precede any scoring."""
    counts=Counter();eligible=[];families=set();digests=set()
    with tarfile.open(archive,'r:*') as source:
        for member in sorted(source.getmembers(),key=lambda m:m.name):
            check();name=member.name.removeprefix('./')
            if not member.isfile():continue
            match=re.fullmatch(r'text/([a-z-]+)/[a-z-]+-(\d+)\.txt',name)
            if not match:continue
            category,article=match.groups();split=family_split(article);counts[split+'_article_headers']+=1
            if split!='dev':continue
            if article in families:counts['duplicate_DEV_family']+=1;continue
            families.add(article);raw=source.extractfile(member).read();counts['DEV_bodies_decoded']+=1
            original=raw.decode('utf-8-sig');lead=first_lead(original)
            if lead is None:counts['DEV_structural_rejected']+=1;continue
            ids=tok.encode(lead)
            if not 24<=len(ids)<=256:counts['DEV_token_length_rejected']+=1;continue
            digest=hashlib.sha256(lead.encode()).hexdigest()
            if digest in digests:counts['DEV_local_exact_duplicate']+=1;continue
            digests.add(digest)
            row=dict(doc_id='livedoor-'+article,source_family='livedoor-'+article,split='dev',category=category,
                canonical_sha256=digest,text=lead,source_URL=original.splitlines()[0],original_article_sha256=hashlib.sha256(raw).hexdigest())
            eligible.append(original_continuation(row,ids,tok))
    if len(eligible)<count:raise ValueError('Insufficient fixed original DEV leads; no fallback')
    counts['eligible_DEV_leads']=len(eligible)
    return random.Random(seed).sample(eligible,count),dict(counts)


def collate_positive(rows,span):
    paired=[dict(r,rejected_ids=r['chosen_ids']) for r in rows]
    x,y,mask=collate_continuations(paired);n=len(rows);pad=span-x.shape[1]
    if pad<0:raise ValueError('Fixed full-body span is too short')
    return F.pad(x[:n],(0,pad)),F.pad(y[:n],(0,pad),value=-100),F.pad(mask[:n],(0,pad),value=False)


def score_logits(logits,y,rows):
    """EOS belongs to CE teachers; body-only BPB uses exact common bytes."""
    if logits.shape[:2]!=y.shape or len(rows)!=len(y):raise ValueError('Single-shift completion shapes differ')
    mask=y.ne(-100);body=y.ge(8);eos=y.eq(3)
    if not bool((eos.sum(-1)==1).all()):raise ValueError('Exactly one original terminal EOS target required')
    nll=-logits.float().log_softmax(-1).gather(-1,y.clamp_min(0).unsqueeze(-1)).squeeze(-1)
    result=[]
    for i,r in enumerate(rows):
        if int(body[i].sum())!=r['chosen_body_tokens']:raise ValueError('Original completion mask/token count differs')
        result.append(dict(id=r['id'],completion_teacher_tokens=int(mask[i].sum()),body_tokens=int(body[i].sum()),body_bytes=r['chosen_body_bytes'],
            completion_nll=float((nll[i]*mask[i]).sum()),body_nll=float((nll[i]*body[i]).sum()),EOS_nll=float((nll[i]*eos[i]).sum())))
    if any(not math.isfinite(r[k]) for r in result for k in ('completion_nll','body_nll','EOS_nll')):raise ValueError('Finite full likelihood required')
    return result


def summarize(rows):
    teachers=sum(r['completion_teacher_tokens'] for r in rows);body=sum(r['body_tokens'] for r in rows);bytes_=sum(r['body_bytes'] for r in rows)
    return dict(documents=len(rows),completion_teacher_positions=teachers,body_positions=body,body_bytes=bytes_,EOS_positions=len(rows),
        completion_CE_nats=sum(r['completion_nll'] for r in rows)/teachers,
        body_BPB=sum(r['body_nll'] for r in rows)/math.log(2)/bytes_,mean_EOS_NLL=sum(r['EOS_nll'] for r in rows)/len(rows))
