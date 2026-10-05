import importlib.util
from pathlib import Path
import torch

spec=importlib.util.spec_from_file_location('diagnostic',Path(__file__).resolve().parents[1]/'scripts/run_root_cause_diagnostic.py')
diagnostic=importlib.util.module_from_spec(spec)
spec.loader.exec_module(diagnostic)


def test_raw_eos_rank_and_probability_do_not_hide_suppressed_tokens():
    scores=torch.tensor([9.,0.,0.,8.,0.,0.,0.,0.,7.])
    result=diagnostic.distribution(scores,3)
    assert result['eos_rank']==2
    assert result['target_probability']==result['eos_probability']
    assert diagnostic.choose(scores)==3


def test_top_p_sampling_uses_seed_and_keeps_eos_available():
    scores=torch.full((16,),-100.);scores[3]=10.
    assert diagnostic.choose(scores,torch.Generator().manual_seed(42))==3
    scores[8]=10.
    a=torch.Generator().manual_seed(43);b=torch.Generator().manual_seed(43)
    assert [diagnostic.choose(scores,a) for _ in range(20)]==[diagnostic.choose(scores,b) for _ in range(20)]


def test_ragged_cache_valid_positions_match_standalone():
    from jmicro.experiment import ROOT,read_json
    from jmicro.model import JMicroModel
    c=read_json(ROOT/'configs/models/t4k.json')
    c.update(vocab_size=32,hidden_size=32,num_hidden_layers=2,num_attention_heads=2,num_key_value_heads=1,
             head_dim=16,rotary_dim=16,intermediate_size=48,attention_scale=.25,qk_norm_type='none')
    torch.set_num_threads(2);torch.manual_seed(42)
    model=JMicroModel(c).eval()
    rows=[[2,8,9],[2,10,11,12,13]]
    ids,mask=diagnostic.padded(rows,'cpu')
    cache=model(ids,attention_mask=mask,use_cache=True).cache
    next_ids=torch.tensor([[14],[15]])
    got=model(next_ids,cache=cache,use_cache=True)
    for i,row in enumerate(rows):
        reference=model(torch.tensor([row+[int(next_ids[i,0])]])).logits[0,-1]
        torch.testing.assert_close(got.logits[i,-1],reference,atol=1e-5,rtol=1e-4)
    assert got.cache.positions[:,-1].tolist()==[3,5]


def test_repetition_start_is_first_repeated_window_not_last_token():
    assert diagnostic.first_repeated_ngram([8,9,10,11,12,8,9,10,11])==dict(first=0,repeated=5,end_step=8,ids=[8,9,10,11])
    assert diagnostic.first_repeated_ngram([8,9,10,11,12]) is None
