import sys
from pathlib import Path
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
import pytest
from jmicro.experiment import ROOT,read_json
from jmicro.tokenizer import Tokenizer
from tatoeba_original_short_source import candidate,family_split,parse_line,fixed_sample


@pytest.fixture(scope='module')
def tokenizer():
    return Tokenizer(ROOT/read_json(ROOT/'configs/phase6/natural_context_contrast_comparison.json')['tokenizer'])


def record(text,number=1):
    return dict(source_id=number,language='jpn',text=text,modified='2026-01-01 00:00:00')


def test_original_sentence_codec_bytes_and_body_only(tokenizer):
    text='今日は天気がよいので、公園をゆっくり歩いた。'
    row,reason=candidate(record(text),tokenizer,[])
    assert reason is None and row['text']==text and row['body_bytes']==len(text.encode())
    assert tokenizer.decode_bytes(row['body_ids'])==text.encode() and all(n>=8 for n in row['body_ids'])


def test_duplicate_originals_share_split_across_source_ids(tokenizer):
    text='図書館で借りた本を、家に帰ってから読んだ。'
    a,_=candidate(record(text,1),tokenizer,[]);b,_=candidate(record(text,900),tokenizer,[])
    assert a['id']!=b['id'] and (a['family'],a['split'])==(b['family'],b['split'])
    assert family_split(text)==family_split(text)


def test_fixed_eligibility_rejects_wrappers_and_unfinished(tokenizer):
    for text in ('今日は公園に行くので、','<|assistant|>今日は公園に行った。','https://example.comを見ました。','あ。'):
        row,reason=candidate(record(text),tokenizer,[])
        assert row is None and reason
    text='「今日は公園に行きましょう。」'
    assert candidate(record(text),tokenizer,[])[0]['text']==text


def test_schema_strict_UTF8_and_existing_DEV_exclusion(tokenizer):
    raw='7\tjpn\t今日は天気がよいので、公園をゆっくり歩いた。\t2026-01-01 00:00:00\n'.encode()
    r=parse_line(raw)
    assert r['source_id']==7
    assert candidate(r,tokenizer,['今日は天気がよいので'])[1]=='fixed_DEV_prefix_overlap'
    for malformed in (b'7\teng\ttest\tdate\n',b'7\tjpn\ttest\n',b'\xff'):
        with pytest.raises((UnicodeDecodeError,ValueError)): parse_line(malformed)


def test_single_seed_uniform_sample_train_only_no_duplicate_rescue():
    rows=[dict(id=str(i),family=str(i),split='train') for i in range(100)]
    sample,indices=fixed_sample(rows)
    assert len(sample)==len(indices)==len(set(indices))==80 and indices==sorted(indices)
    assert fixed_sample(rows)==(sample,indices)
    rows[0]['split']='dev'
    with pytest.raises(ValueError): fixed_sample(rows)
    rows[0]['split']='train';rows[0]['family']=rows[1]['family']
    with pytest.raises(ValueError): fixed_sample(rows)
