"""Original gold/sampler parity, complete Adam/RNG state and partial refusal."""
import copy
import sys
from pathlib import Path

import pytest
import torch
from torch.nn import functional as F

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from base_headwise_gate_model import ARMS, POLICY, TAG
from base_headwise_gate_trainer import KIND, HeadwiseGateTrainer
from base_headwise_gate_evaluation import validate_record,typed_native_evaluation
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host,right_pad,right_padded_hidden
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool,FixtureCodec,parent


@pytest.fixture
def build(tmp_path):
    pool = tmp_path/'pool';manifest = fixture_pool(pool)
    initial = parent()
    with torch.device('meta'):
        initial['model_config']['expected_parameter_count'] = sum(
            p.numel() for p in JMicroModel(initial['model_config']).parameters())
    def constructor(arm='query_headwise'):
        sampler = OriginalTrainCorpusSampler(pool,manifest,FixtureCodec(),dict(web=7500,textbook=2000,story=500))
        return HeadwiseGateTrainer(initial,sampler,dict(parent=dict(path='fixture',sha256='fixed')),
                                   arm,batch=4,device='cpu')
    return constructor


def test_paired_initial_CE_exact_native_gold_masks_and_full_sampler(build):
    a,b = [build(arm) for arm in ARMS]
    clone = build('static_half')
    rows = clone.sampler.take(4)
    ids,_ = right_pad([r['input_ids'] for r in rows],'cpu')
    targets = torch.full_like(ids,-100)
    for i,r in enumerate(rows):targets[i,:len(r['target_ids'])]=torch.tensor(r['target_ids'])
    logits = clone.model.lm_head(right_padded_hidden(clone.model,ids)[targets.ne(-100)]).float()
    independently_expected_CE = float(F.cross_entropy(logits,targets[targets.ne(-100)]).detach())
    for i in range(4):
        ar,br = a.step(),b.step()
        if not i:assert ar['CE_loss']==br['CE_loss']==independently_expected_CE
        for key in (*a.counters,'draw_trace','lr'):
            assert equal_state(ar[key],br[key]),key
        assert equal_state(a.sampler.state_dict(),b.sampler.state_dict())
        assert ar['auxiliary_pairs']==br['auxiliary_pairs']==0
    assert not equal_state(a.model.state_dict(),b.model.state_dict())
    assert a.lineage['original_parent_optimizer_reused'] is False


@pytest.mark.parametrize('arm',ARMS)
def test_continuous_four_vs_two_save_two_allstate_history_and_sampler(build,tmp_path,arm):
    a = build(arm);ah = [a.step() for _ in range(4)];expected = host(a.state_dict())
    b = build(arm);bh = [b.step() for _ in range(2)]
    path = tmp_path/'checkpoint.pt';b.save(path)
    b = build(arm);b.load(path);bh.extend(b.step() for _ in range(2))
    assert equal_state(expected,host(b.state_dict()))
    for left,right in zip(ah,bh,strict=True):
        assert equal_state({k:v for k,v in left.items() if k not in ('seconds','data_wait_seconds')},
                           {k:v for k,v in right.items() if k not in ('seconds','data_wait_seconds')})


@pytest.mark.parametrize('problem',('kind','arm','policy','moment_step','moment_shape','negative_variance',
    'nonfinite','scheduler','source','tie','static_weights','parameter_partition'))
def test_malformed_fullstate_rejected_before_weight_mutation(build,tmp_path,problem):
    a = build('static_half');a.step();state = copy.deepcopy(host(a.state_dict()))
    moment = next(iter(state['optimizer']['state'].values()))
    if problem=='kind':state['kind']='old_native_CE'
    elif problem=='arm':state['spec']['gate_arm']='query_headwise'
    elif problem=='policy':state['optimizer']['param_groups'][0]['lr']=2e-5
    elif problem=='moment_step':moment['step'].zero_()
    elif problem=='moment_shape':moment['exp_avg']=torch.zeros(1)
    elif problem=='negative_variance':moment['exp_avg_sq'].fill_(-1)
    elif problem=='nonfinite':moment['exp_avg'].fill_(float('nan'))
    elif problem=='scheduler':state['scheduler']['last_epoch']+=1
    elif problem=='source':state['sampler']['consumed']['web']+=1
    elif problem=='tie':state['model']['lm_head.weight']+=1
    elif problem=='static_weights':state['model']['model.layers.0.self_attn.gate_proj.weight'][0,0]=1
    else:state['optimizer']['param_groups'][0]['params'].append(0)
    path = tmp_path/'invalid.pt';torch.save(state,path)
    b = build('static_half');before = host(b.model.state_dict())
    with pytest.raises(ValueError):b.load(path)
    assert equal_state(before,host(b.model.state_dict()))


def test_actual_post_Adam_failure_cannot_save_or_continue_and_clean_resume_recovers(build,tmp_path):
    a = build();a.step();path = tmp_path/'valid.pt';a.save(path)
    expected = host(a.state_dict());step = a.optimizer.step
    def broken_step():
        step();raise RuntimeError('Fixture failure after actual optimizer mutation')
    a.optimizer.step = broken_step
    with pytest.raises(RuntimeError):a.step()
    with pytest.raises(ValueError):a.save(tmp_path/'partial.pt')
    with pytest.raises(ValueError):a.step()
    a.optimizer.step = step;a.load(path)
    assert equal_state(expected,host(a.state_dict()))
    a.step()


def test_typed_evaluator_requires_exact_gate_record_and_restores_native_factory(build,tmp_path):
    trainer = build('query_headwise')
    record = dict(model_config=copy.deepcopy(trainer.model.config),spec=copy.deepcopy(trainer.spec),
                  gate_arm='query_headwise',gate_policy=copy.deepcopy(POLICY),gate_model_class='HeadwiseGateModel')
    validate_record('query_headwise',record)
    for key in ('gate_arm','gate_policy','gate_model_class','model_config'):
        bad = copy.deepcopy(record);del bad[key]
        with pytest.raises(ValueError):validate_record('query_headwise',bad)
    import run_complete_text_comparison as core
    old_factory,old_run = core.JMicroModel,core.RUN
    with pytest.raises(RuntimeError):
        with typed_native_evaluation(tmp_path):
            assert core.JMicroModel is not old_factory and core.RUN==tmp_path
            model = core.JMicroModel(record['model_config'])
            assert model.config[TAG]['arm']=='query_headwise'
            raise RuntimeError('Fixture failure inside evaluator scope')
    assert core.JMicroModel is old_factory and core.RUN==old_run
