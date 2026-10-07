import json
from pathlib import Path
import sys
import pytest
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.tokenizer import Tokenizer
from tanaka_edited_pd2008_source_v2 import parse_line,candidate,family_split,fixed_sample


def test_exact_japanese_excludes_english_and_indexing():
    body='散歩から帰る途中、小さなパン屋を見つけました。'
    assert parse_line(('A: '+body+'\tOn my way home.\r\n').encode('euc_jp'),'A')==('A',body)
    assert parse_line('B: 散歩 帰る\r\n'.encode('euc_jp'),'B')==('B',None)
    assert parse_line(('#A: '+body+'\tNot for learning.\r\n').encode('euc_jp'),'A')==('comment',None)
    assert parse_line(b'#B: ===\r\n','A')==('comment',None)
    for raw,kind in [(b'A: x\tx\tx\r\n','A'),('A: 犬\tx\r\n'.encode(),'A'),(b'B: words\r\n','A'),(b'A: x\tx\n','A')]:
        with pytest.raises((ValueError,UnicodeError)): parse_line(raw,kind)


def test_actual_original_codec_and_source_identity():
    root=Path(__file__).resolve().parents[1]
    old=json.loads((root/'configs/phase6/natural_context_contrast_comparison.json').read_text())
    tokenizer=Tokenizer(root/old['tokenizer']);body='散歩から帰る途中、小さなパン屋を見つけました。'
    row,error=candidate(body,1,tokenizer,[],'f'*64)
    assert error is None and tokenizer.decode_bytes(row['body_ids'])==body.encode()
    assert row['source']=='tanaka_edited_PD2008' and row['source_line']==1 and 'CC0' not in row['license']
    assert min(row['body_ids'])>=8
    assert candidate(body,1,tokenizer,[body[:12]],'f'*64)[1]=='fixed_DEV_prefix_overlap'
    assert candidate('Assistant: '+body,1,tokenizer,[],'f'*64)[1]=='URL_special_or_wrapper'


def test_family_uses_exact_body_independent_of_line_identity():
    body='日本語の完全な文章です。'
    assert family_split(body)==family_split(body)
    assert family_split(body)!=family_split(body+'。')
    assert family_split(body)[1] in {'train','dev','test'}


def test_fixed_train_sample_has_no_reroll_or_duplicates():
    rows=[dict(family=str(i),split='train') for i in range(100)]
    sample,indices=fixed_sample(rows)
    assert len(sample)==len(set(indices))==80 and fixed_sample(rows)==(sample,indices)
    with pytest.raises(ValueError): fixed_sample(rows[:79])
    with pytest.raises(ValueError): fixed_sample(rows+[rows[0]])
    with pytest.raises(ValueError): fixed_sample([dict(family=str(i),split='dev') for i in range(100)])
