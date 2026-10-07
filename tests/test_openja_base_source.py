import json
from pathlib import Path
import sys
import pytest
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.tokenizer import Tokenizer
from openja_base_source import candidate,fixed_sample


@pytest.fixture
def tokenizer():
    root=Path(__file__).resolve().parents[1]
    old=json.loads((root/'configs/phase6/natural_context_contrast_comparison.json').read_text())
    return Tokenizer(root/old['tokenizer'])


def source(text,number=1):
    return dict(id='115005254X02020001201_'+str(number).zfill(3),issueID='115005254X02020001201',text=text,
        speechURL='https://kokkai.ndl.go.jp/txt/115005254X02020001201/'+str(number))


def test_exact_header_span_and_native_roundtrip(tokenizer):
    body='この制度は地域の小さな店を支えるために作られました。'
    original='○山田太郎君　'+body
    row,error=candidate(source(original),7,3,tokenizer,[])
    assert error is None and row['text']==body and min(row['body_ids'])>=8
    span=row['original_UTF8_byte_span']
    assert original.encode()[span[0]:span[1]]==tokenizer.decode_bytes(row['body_ids'])==body.encode()


def test_meeting_family_holdout_and_exact_body_identity(tokenizer):
    body='日本語で制度の目的を説明しています。'
    a,_=candidate(source(body,1),1,0,tokenizer,[])
    b,_=candidate(source(body+'制度は今も続いています。',2),2,0,tokenizer,[])
    c,_=candidate(source(body,3),3,0,tokenizer,[])
    assert a['family']==b['family'] and a['split']==b['split']
    assert a['body_sha256']==c['body_sha256']


def test_no_truncation_rewrite_or_dev_wrapper_leak(tokenizer):
    body='日本語で制度の目的を説明しています。'
    assert candidate(source(body),1,0,tokenizer,[body[:12]])[1]=='fixed_DEV_prefix_overlap'
    assert candidate(source('Assistant: '+body),1,0,tokenizer,[])[1]=='URL_special_or_wrapper'
    assert candidate(source(body[:-1]),1,0,tokenizer,[])[1]=='terminal_punctuation'
    assert candidate(source(body*30),1,0,tokenizer,[])[1]=='characters'


def test_uniform80_training_only_and_exact_duplicate_rejection():
    rows=[dict(body_sha256=str(i),split='train') for i in range(100)]
    sample,indices=fixed_sample(rows)
    assert len(sample)==len(set(indices))==80 and fixed_sample(rows)==(sample,indices)
    with pytest.raises(ValueError): fixed_sample(rows+[rows[0]])
    with pytest.raises(ValueError): fixed_sample([dict(body_sha256=str(i),split='dev') for i in range(100)])
