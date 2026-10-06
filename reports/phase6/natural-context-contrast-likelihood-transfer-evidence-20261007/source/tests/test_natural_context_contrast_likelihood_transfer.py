"""Suffix masking and native CPU reference fixtures; no learned GPU evidence."""
import json
from pathlib import Path
import sys

import pytest
import torch
from torch.nn import functional as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_natural_context_contrast_likelihood_transfer import VIEWS, tasks_for, score_tasks
from jmicro.model import JMicroModel

torch.set_num_threads(2)


def rows():
    return [dict(doc_id='a',prefix_ids=[10,11,12,13,14],suffix_ids=list(range(20,30)),suffix_bytes=30),
            dict(doc_id='b',prefix_ids=[31,32],suffix_ids=list(range(40,55)),suffix_bytes=45)]


def test_rolling_exact_single_shift_original_context_and_complete_targets():
    cases=rows()
    for view in VIEWS:
        tasks=tasks_for(cases,view,context=8,stride=3)
        for i,case in enumerate(cases):
            selected=[t for t in tasks if t['row']==i]
            source=cases[i if view=='matched' else (i+1)%len(cases)]
            prefix=[] if view=='BOS_only' else source['prefix_ids']
            serialized=[2]+prefix+case['suffix_ids']
            scored=[]
            for task in selected:
                start=task['original_input_start']
                assert 1<=len(task['input_ids'])<=8
                assert task['input_ids']==serialized[start:start+len(task['input_ids'])]
                assert (2 in task['input_ids'])==(start==0)
                for position,target in enumerate(task['targets']):
                    if target != -100:
                        assert target==serialized[start+position+1]
                        scored.append(target)
            assert scored==case['suffix_ids']
            assert all(t['prefix_doc_id']==(None if view=='BOS_only' else source['doc_id']) for t in selected)


def test_native_reference_likelihood_and_same_suffix_byte_denominator():
    c=json.loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    c.update(num_hidden_layers=2,hidden_size=32,intermediate_size=64,num_attention_heads=4,
        num_key_value_heads=2,head_dim=8,rotary_dim=8,attention_scale=8**-.5,vocab_size=100,qk_norm_type='none')
    torch.manual_seed(7)
    model=JMicroModel(c).eval()
    before={k:v.clone() for k,v in model.state_dict().items()}
    cases=rows()
    for view in VIEWS:
        result=score_tasks(model,tasks_for(cases,view),cases,view,'cpu',batch=2)
        for i,case in enumerate(cases):
            source=cases[i if view=='matched' else (i+1)%len(cases)]
            prefix=[] if view=='BOS_only' else source['prefix_ids']
            with torch.inference_mode():
                logits=model(torch.tensor([[2]+prefix+case['suffix_ids']])).logits
                expected=F.cross_entropy(logits[0,len(prefix):len(prefix)+len(case['suffix_ids'])],
                    torch.tensor(case['suffix_ids']),reduction='sum')
            assert result['rows'][i]['nll']==pytest.approx(float(expected),abs=1e-5)
        assert result['body_tokens']==25 and result['body_bytes']==75
        assert result['EOS_scored_positions']==0 and result['EOS_in_vocabulary_normalization'] is True
    assert all(torch.equal(before[k],v) for k,v in model.state_dict().items())
    assert all(p.grad is None for p in model.parameters())


def test_invalid_geometry_and_special_suffix_rejected():
    with pytest.raises(ValueError,match='geometry'):
        tasks_for(rows(),'matched',context=8,stride=8)
    with pytest.raises(ValueError,match='geometry'):
        tasks_for(rows(),'invented')
    cases=rows();cases[0]['suffix_ids'].append(3)
    with pytest.raises(ValueError,match='plain body'):
        tasks_for(cases,'matched')
