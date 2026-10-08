"""Source slice and unchanged body-target contracts, not actual model quality."""
import hashlib
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
import pytest
from run_base_residual_original_context import recover


class Codec:
    def encode(self,text): return [b+8 for b in text.encode()]
    def decode_bytes(self,ids): return bytes(n-8 for n in ids if n>=8)


def fixture(before):
    text='abcdefghijKLMNOPQRSTUVWXYZ。\n';codec=Codec();body=codec.encode(text);cut=8
    row=dict(id='TRAIN-00',source='web',full_original_body_text=text,
        full_original_body_sha256=hashlib.sha256(text.encode()).hexdigest(),input_ids=[2]+body,
        prompt_ids=[2]+body[:cut],prefix=codec.decode_bytes(body[:cut]).decode(),gold_targets=body+[3],
        continuation_gold_ids=body[cut:]+[3])
    article=before+text+'later。';metadata=dict(source_char_start=len(before),source_char_end=len(before)+len(text))
    return row,metadata,codec.encode(article),codec


def test_recovers_actual_context_and_identical_body_targets_without_paragraph_EOS():
    row,metadata,article,codec=fixture('earlier\n')
    value=recover(row,metadata,article,codec)
    assert value['prompt_ids']==[2]+codec.encode('earlier\n')+row['prompt_ids'][1:]
    assert value['continuation_gold_ids']==row['continuation_gold_ids'][:-1] and 3 not in value['continuation_gold_ids']
    assert value['has_additional_context'] and value['original_unit_EOS_excluded_from_body_comparison']


def test_long_original_context_clips_only_oldest_tokens_without_fragment_BOS():
    row,metadata,article,codec=fixture('earlier\n'*200)
    value=recover(row,metadata,article,codec)
    assert len(value['prompt_ids'])==959 and 2 not in value['prompt_ids']
    assert value['prompt_ids'][-8:]==row['prompt_ids'][1:]
    assert value['oldest_history_tokens_removed']>0 and not value['artificial_fragment_BOS_inserted']


def test_missing_original_source_alignment_rejects_without_fallback_or_reroll():
    row,metadata,article,codec=fixture('earlier\n');metadata['source_char_start']+=1
    with pytest.raises(ValueError,match='slice'): recover(row,metadata,article,codec)


def test_no_preceding_original_context_is_reused_control_not_new_sample():
    row,metadata,article,codec=fixture('')
    value=recover(row,metadata,article,codec)
    assert not value['has_additional_context'] and value['prompt_ids']==row['prompt_ids']
    assert value['oldest_history_tokens_removed']==0
