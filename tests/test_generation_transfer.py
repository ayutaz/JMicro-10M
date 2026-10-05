import importlib.util
from pathlib import Path
import pytest

spec=importlib.util.spec_from_file_location('transfer',Path(__file__).resolve().parents[1]/'scripts/run_generation_transfer.py')
transfer=importlib.util.module_from_spec(spec)
spec.loader.exec_module(transfer)


def test_summary_keeps_long_stops_separate_from_frozen64():
    cases=[dict(source=s,gold_ids=[8]*70) for s in ('train','dev')]
    teachers=[dict(teacher_top1_fraction=.5,teacher_nll_mean=1.,ending=dict(eos_rank=1,target_nll=.2))]*2
    short=[dict(stop_reason='max_tokens',generated_ids=[8]*64)]*2
    long=[dict(stop_reason='eos',first_repeated_4gram=None)]*2
    result=transfer.summary(cases,teachers,short,long)
    for r in result.values():
        assert r['greedy64_EOS']==0 and r['greedy256_EOS']==1
        assert r['additional_stops_after64']==1 and r['gold_continuation_exceeds64']==1
    with pytest.raises(ValueError):transfer.summary(cases,teachers[:1],short,long)


def test_prefix_is_exact_slice_of_original_ids():
    from jmicro.experiment import ROOT
    from jmicro.tokenizer import Tokenizer
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    text='窓を開けると雨が吹き込んだ。私は急いで窓を閉めた。'
    row=transfer.make_case(dict(doc_id='unit',text=text,canonical_sha256='unit'),tok,'train')
    assert row['prefix_ids'][1:]+row['gold_ids'][:-1]==tok.encode(text)
    assert row['prefix'].endswith('。') and row['continuation']
