"""Original-source and fresh token-scheduled state; fixtures are not quality."""
import copy
from pathlib import Path
import sys

import pytest
import torch
from torch.nn import functional as F

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from base_kv_allocation_trainer import CEOnlyOriginalSampler, FreshKVAllocationTrainer, TargetPositionSchedule
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host, right_pad
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool, FixtureCodec, parent


def builders(tmp_path):
    pool = tmp_path/'pool'
    manifest = fixture_pool(pool)
    original = parent()
    configs = {}
    for name, heads, ffn in [('GQA',2,64),('MHA',4,56)]:
        config = copy.deepcopy(original['model_config'])
        config.update(num_key_value_heads=heads, intermediate_size=ffn)
        with torch.device('meta'):
            config['expected_parameter_count'] = sum(p.numel() for p in JMicroModel(config).parameters())
        configs[name] = config
    goals = dict(web=7500, textbook=2000, story=500)
    def source(cls=CEOnlyOriginalSampler):
        return cls(pool,manifest,FixtureCodec(),goals)
    def build(name='GQA'):
        return FreshKVAllocationTrainer(configs[name],source(),dict(proposal='fixture'),batch=4,
                                        device='cpu',warmup=1000)
    return source,build,configs


def test_omits_pair_encoding_but_preserves_every_original_draw_mask_byte_and_eos(tmp_path):
    source,_,_ = builders(tmp_path)
    original,ce = source(OriginalTrainCorpusSampler),source()
    def unused_encode(_):
        raise AssertionError('CE-only sampler must not extract or encode auxiliary pairs')
    ce.tokenizer.encode = unused_encode
    excluded = {'prefix_ids','suffix_ids','auxiliary_eligibility'}
    all_rows = []
    while not ce.exhausted:
        a,b = original.take(4),ce.take(4)
        assert equal_state([{k:v for k,v in r.items() if k not in excluded} for r in a],
                           [{k:v for k,v in r.items() if k not in excluded} for r in b])
        all_rows.extend(b)
    assert ce.consumed == ce.goals
    assert any(-100 in r['target_ids'] for r in all_rows)  # Original long-unit overlaps.
    for key in ('RNG','consumed','draws','documents_drawn','windows_emitted'):
        assert equal_state(original.state_dict()[key],ce.state_dict()[key])
    with pytest.raises(ValueError,match='binding'):
        source().load_state_dict(original.state_dict())


@pytest.mark.parametrize('name',['GQA','MHA'])
def test_actual_full_state_and_history_continuous_four_vs_two_saved_two(tmp_path,name):
    _,build,_ = builders(tmp_path)
    continuous = build(name)
    expected_rows = [continuous.step() for _ in range(4)]
    expected = host(continuous.state_dict())
    split = build(name)
    rows = [split.step() for _ in range(2)]
    split.save(tmp_path/'split.pt')
    resumed = build(name)
    resumed.load(tmp_path/'split.pt')
    rows.extend(resumed.step() for _ in range(2))
    assert equal_state(expected,host(resumed.state_dict()))
    for a,b in zip(expected_rows,rows,strict=True):
        assert equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                           {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})
    assert resumed.model.lm_head.weight is resumed.model.model.embed_tokens.weight
    assert expected['scheduler']['tokens'] == expected['counters']['supervised_tokens']
    assert expected['counters']['source_teachers'] == expected['sampler']['consumed']
    assert not equal_state(host(build(name).model.state_dict()),expected['model'])


def test_fresh_configs_share_source_accounting_and_correct_original_native_masked_ce(tmp_path):
    source,build,_ = builders(tmp_path)
    a,b = build(),build('MHA')
    assert a.lineage['parent'] is None and not a.lineage['learned_parent_weights_used']
    assert equal_state(host(a.model.state_dict()),host(build().model.state_dict()))
    selected = source().take(4)
    ids,_ = right_pad([r['input_ids'] for r in selected],'cpu')
    labels = torch.full_like(ids,-100)
    for index,row in enumerate(selected):
        labels[index,:len(row['target_ids'])] = torch.tensor(row['target_ids'])
    expected = F.cross_entropy(a.model(ids).logits.reshape(-1,128),labels.reshape(-1),ignore_index=-100)
    first,other = a.step(),b.step()
    assert first['CE_loss'] == pytest.approx(float(expected.detach()),abs=1e-6)
    for key in ('source_teachers','source_EOS','CE_input_tokens','physical_input_tokens',
                'original_body_bytes','token_digest','draw_trace','lr'):
        assert equal_state(first[key],other[key])
    assert equal_state(a.sampler.state_dict(),b.sampler.state_dict())


def test_schedule_uses_target_positions_exact_boundary_and_last_partial_goal():
    optimizer = torch.optim.AdamW([torch.nn.Parameter(torch.ones(1))])
    s = TargetPositionSchedule(optimizer,total=100,warmup=20)
    assert s.value(0) == 0 and s.value(20) == .002 and s.value(100) == 1e-5
    assert s.prepare(7) == .002*7/20 and s.tokens == 0
    s.commit(7)
    assert s.prepare(13) == .002
    s.commit(13)
    assert s.prepare(80) == 1e-5
    s.commit(80)
    with pytest.raises(ValueError,match='outside'):
        s.prepare(1)


@pytest.mark.parametrize('change',['architecture','schedule','cursor','auxiliary'])
def test_reject_changed_architecture_schedule_accounting_or_auxiliary_before_weights(tmp_path,change):
    _,build,_ = builders(tmp_path)
    trained = build()
    trained.step()
    state = host(trained.state_dict())
    if change == 'architecture':
        state['model_config']['num_key_value_heads'] = 4
    elif change == 'schedule':
        state['scheduler']['warmup'] += 1
    elif change == 'cursor':
        state['scheduler']['tokens'] -= 1
    else:
        state['counters']['auxiliary_input_tokens'] = 1
    torch.save(state,tmp_path/'changed.pt')
    recipient = build()
    initial = host(recipient.model.state_dict())
    with pytest.raises(ValueError):
        recipient.load(tmp_path/'changed.pt')
    assert equal_state(initial,host(recipient.model.state_dict()))
    recipient.model.eval()
    with pytest.raises(ValueError,match='model.train'):
        recipient.step()
