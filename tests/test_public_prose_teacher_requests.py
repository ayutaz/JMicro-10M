import sys
from pathlib import Path
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts'),str(Path(__file__).resolve().parents[1]/'src')]
from probe_public_prose_teacher import request,train_requests


def test_family_split_is_fixed_before_generation_and_train_requests_unique():
    rows=train_requests(64)
    assert len({r['id'] for r in rows})==len({r['family'] for r in rows})==64
    assert all(r['split']=='train' for r in rows)
    assert train_requests(64)==rows
    for r in rows:
        assert request(int(r['id'].split('-')[1]))==r
    assert any(request(i)['split']=='dev' for i in range(100))


def test_prompts_request_plain_complete_japanese_without_role_or_eval_inputs():
    for r in train_requests(64):
        assert '日本語' in r['prompt'] and '本文だけ' in r['prompt'] and '最後は' in r['prompt']
        assert not any(marker in r['prompt'] for marker in ('<|','base-','Assistant:','User:'))
