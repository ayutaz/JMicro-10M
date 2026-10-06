"""Raw source bytes, common target masks and ranking accounting; no quality claims."""
import copy
import json
import sys
import pytest
import torch
from jmicro.experiment import ROOT,read_json
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import NativeLikelihood
sys.path.insert(0,str(ROOT/'scripts'))
import run_condition_source_ranking as study


def test_actual_fixed_pilots_keep_raw_UTF8_and_common_candidate_ids():
    original=read_json(ROOT/'configs/phase6/textbook_quantity_comparison.json'); tok=Tokenizer(ROOT/original['tokenizer'])
    p=read_json(study.PROPOSAL); prepared=study.build_cases(p,tok)
    assert len(prepared['families'])==128 and len(prepared['cases'])==1024
    assert sum(f['content_annotation']['weak_pair'] for f in prepared['families'])==12
    for family in prepared['families']:
        rows=[r for r in prepared['cases'] if r['family']==family['index']]
        for candidate in (0,1):
            selected=[r for r in rows if r['candidate']==candidate]
            assert all(r['target_ids']==selected[0]['target_ids'] for r in selected)
            assert all(tok.decode_bytes(r['ids'])==(r['prefix']+r['outcome']).encode() for r in selected)
            assert all(3 not in r['ids'] and 7 not in r['ids'] for r in selected)


def test_real_native_target_mask_padding_BOS_without_added_EOS_is_read_only():
    config=json.loads((ROOT/'configs/models/t4k.json').read_text());config.update(num_hidden_layers=2,vocab_size=300)
    torch.manual_seed(18);model=JMicroModel(config).eval();before=copy.deepcopy(model.state_dict())
    cases=[dict(ids=[2,8,9,10,11],context_tokens=3,target_ids=[10,11],target_bytes=2),
           dict(ids=[2,12,13,14,10,11],context_tokens=4,target_ids=[10,11],target_bytes=2)]
    scorer=NativeLikelihood(model,None,'cpu');batch=scorer.score_encoded(cases);one=scorer.score_encoded(cases[:1])[0]
    assert batch[0]['token_nll']==pytest.approx(one['token_nll'],abs=1e-5)
    with torch.inference_mode():
        logits=model(torch.tensor([[2,8,9,10]])).logits.float().log_softmax(-1)
        expected=[-float(logits[0,2,10]),-float(logits[0,3,11])]
    assert batch[0]['token_nll']==pytest.approx(expected,abs=1e-5)
    assert all(torch.equal(before[k],v) for k,v in model.state_dict().items()) and all(p.grad is None for p in model.parameters())


def test_same_candidate_primary_and_normalization_sensitivity_are_distinct():
    prepared=dict(cases=[],families=[]);rows=[]
    for family,group in enumerate(('old512_fixed64','new1536_fixed64')):
        prepared['families'].append(dict(index=family,group=group,source=dict(id=str(family)),content_annotation=dict(weak_pair=False)))
        for mode in study.MODES:
            for label in (0,1):
                for candidate in (0,1):
                    ids=[8] if candidate==0 else [9,10]; losses=[1.+label] if candidate==0 else [1.5,1.5]; index=len(rows)
                    prepared['cases'].append(dict(index=index,family=family,mode=mode,source_matching_label=label,candidate=candidate,target_ids=ids,target_bytes=len(ids)))
                    rows.append(dict(index=index,checkpoint='a',target_ids=ids,target_tokens=len(ids),target_bytes=len(ids),token_nll=losses,log_likelihood=-sum(losses)))
    s=study.summarize(rows,prepared,arms=('a',))['aggregate']['a']['original_history']
    assert s['sum_log_likelihood']['all128']['source_matching_fraction']==.5
    assert s['sum_log_likelihood']['all128']['both_source_matches']==0
    assert s['sum_log_likelihood']['all128']['same_unique_candidate']==2
    assert s['mean_token_log_likelihood']['all128']['both_source_matches']==2
    for bad in (rows[:-1],rows+rows[:1]):
        with pytest.raises(ValueError):study.summarize(bad,prepared,arms=('a',))
    bad=copy.deepcopy(rows);bad[0]['target_ids']=[11]
    with pytest.raises(ValueError):study.summarize(bad,prepared,arms=('a',))
    bad=copy.deepcopy(rows);bad[0]['token_nll']=[float('nan')]
    with pytest.raises(ValueError):study.summarize(bad,prepared,arms=('a',))


def test_scope_never_turns_read_only_diagnostic_into_learning_or_Chat():
    c=dict(kind='original_train_branch_ranking_read_only',GPU_budget_seconds=60,optimizer_updates=0,scientific_teacher_tokens=0,new_original_tokens=0,
        protected_test_used=False,Base_adopted=False,Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,
        checkpoints={a:{} for a in study.ARMS},families=128,cases=1024,batch=16,dtype='bf16',backend='math',primary_metric=study.METRICS[0])
    study.scope(c)
    for changes in (dict(GPU_budget_seconds=61),dict(Chat_started=True),dict(optimizer_updates=1),dict(cases=512),dict(primary_metric=study.METRICS[1])):
        with pytest.raises(ValueError):study.scope(dict(c,**changes))
