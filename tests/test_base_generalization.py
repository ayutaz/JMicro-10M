import hashlib
import io
import math
from pathlib import Path
import sys
import tarfile
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from base_generalization_diagnostic import select_dev,original_continuation,collate_positive,score_logits,summarize
from prepare_livedoor_leads import family_split


class CharacterTokenizer:
    def encode(self,text):return [ord(c)+8 for c in text]
    def decode_bytes(self,ids):return ''.join(chr(v-8) for v in ids if v>=8).encode('utf-8')


def test_fixed_DEV_family_draw_never_decodes_TRAIN_or_TEST(tmp_path):
    archive=tmp_path/'source.tar.gz';groups={k:[str(i) for i in range(4000) if family_split(str(i))==k] for k in ('dev','train','test')}
    with tarfile.open(archive,'w:gz') as output:
        for split,articles in groups.items():
            for article in articles[:70 if split=='dev' else 2]:
                raw=(f'https://example.com/{article}\n2012年\n題名\n'+('今日は晴れて街を歩き、友人と話してから家に帰った。'*3)+article+'番の記事でした。').encode() if split=='dev' else b'\xff\xfeinvalid'
                member=tarfile.TarInfo('text/topic/topic-'+article+'.txt');member.size=len(raw);output.addfile(member,io.BytesIO(raw))
    a,counts=select_dev(archive,CharacterTokenizer(),64,20261007,lambda:None);b,_=select_dev(archive,CharacterTokenizer(),64,20261007,lambda:None)
    assert a==b and len({r['id'] for r in a})==64 and all(r['split']=='dev' for r in a)
    assert counts['DEV_bodies_decoded']==70 and counts['train_article_headers']==counts['test_article_headers']==2


def test_original_prefix_advances_only_to_UTF8_boundary():
    class ByteTokenizer:
        def encode(self,text):return [v+8 for v in text.encode()]
        def decode_bytes(self,ids):return bytes(v-8 for v in ids if v>=8)
    tok=ByteTokenizer();text='a'*8+'あ'*22;ids=tok.encode(text)
    row=dict(doc_id='x',source_family='x',split='dev',category='topic',text=text,canonical_sha256=hashlib.sha256(text.encode()).hexdigest(),source_URL='https://example.com/x',original_article_sha256='a'*64)
    case=original_continuation(row,ids,tok)
    assert len(ids)//4==18 and len(case['prompt_ids'])-1==20
    assert case['prompt_ids'][1:]+case['chosen_ids'][:-1]==ids and case['chosen_ids'][-1]==3
    assert case['chosen_body_bytes']==len(tok.decode_bytes(case['chosen_ids'][:-1]))


def test_single_shift_prompt_PAD_and_EOS_body_byte_accounting():
    rows=[dict(id='a',prompt_ids=[2,8,9],chosen_ids=[10,11,3],chosen_body_tokens=2,chosen_body_bytes=4),
        dict(id='b',prompt_ids=[2,8],chosen_ids=[12,3],chosen_body_tokens=1,chosen_body_bytes=3)]
    x,y,mask=collate_positive(rows,7);assert y[0].tolist()==[-100,-100,10,11,3,-100,-100]
    logits=torch.zeros((*x.shape,32))
    for i,j in torch.nonzero(y.ne(-100)).tolist():logits[i,j,y[i,j]]=math.log(31)
    scored=score_logits(logits,y,rows);s=summarize(scored)
    assert s['completion_teacher_positions']==5 and s['body_positions']==3 and s['EOS_positions']==2
    assert s['body_BPB']==pytest.approx(3/7,rel=1e-6) and s['completion_CE_nats']==pytest.approx(math.log(2),rel=1e-6)
    logits[y.eq(-100)]=100;assert score_logits(logits,y,rows)==scored
    logits[0,4,3]=0;changed=summarize(score_logits(logits,y,rows))
    assert changed['body_BPB']==s['body_BPB'] and changed['completion_CE_nats']>s['completion_CE_nats']
