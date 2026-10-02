import json
from pathlib import Path

import pytest
import torch

from jmicro.model import JMicroModel, Attention, rope

ROOT = Path(__file__).resolve().parents[1]
torch.set_num_threads(2)


@pytest.fixture
def model():
    torch.manual_seed(42)
    config = json.loads((ROOT / "configs/models/t4k.json").read_text())
    config.update(num_hidden_layers=2, vocab_size=300)
    return JMicroModel(config).eval()


def test_ragged_cache_chunk_and_padding(model):
    ids = torch.randint(8, 300, (2, 9))
    valid = torch.tensor([[1,1,1,1,1,1,1,1,1], [1,1,1,0,0,0,1,1,1]], dtype=torch.bool)
    with torch.no_grad():
        full = model(ids, valid).logits
        prefix = model(ids[:, :6], valid[:, :6], use_cache=True)
        chunk = model(ids[:, 6:], valid[:, 6:], prefix.cache, use_cache=True)
        torch.testing.assert_close(chunk.logits, full[:, 6:], atol=1e-5, rtol=1e-4)
        for b in range(2):
            single = model(ids[b:b+1, valid[b]]).logits
            torch.testing.assert_close(full[b, valid[b]], single[0], atol=1e-5, rtol=1e-4)
        assert chunk.cache.valid.sum(-1).tolist() == [9, 6]
        assert chunk.cache.positions[1, -3:].tolist() == [3, 4, 5]
        assert full[~valid].count_nonzero() == 0


def test_future_tokens_cannot_change_past(model):
    ids = torch.randint(8, 300, (1, 12))
    changed = ids.clone()
    changed[:, 6:] = torch.randint(8, 300, (1, 6))
    with torch.no_grad():
        torch.testing.assert_close(model(ids).logits[:, :6], model(changed).logits[:, :6], rtol=0, atol=0)


def test_gqa_contiguous_head_mapping():
    c = json.loads((ROOT / "configs/models/t4k.json").read_text())
    attention = Attention(c)
    x = torch.randn(2, 5, 256)
    pos = torch.arange(5).expand(2, -1)
    mask = torch.ones(5, 5, dtype=torch.bool).tril().expand(2, -1, -1)
    out, (k, v) = attention(x, pos, mask, None)
    q = rope(attention.q_norm(attention.q_proj(x).reshape(2, 5, 4, 64).transpose(1,2)), pos, 10000)
    heads = []
    for i in range(4):
        scores = q[:, i] @ k[:, i // 2].transpose(-1, -2) * 0.125
        scores = scores.masked_fill(~mask, -torch.inf)
        heads.append(scores.softmax(-1) @ v[:, i // 2])
    expected = attention.o_proj(torch.stack(heads, dim=2).reshape(2, 5, 256))
    torch.testing.assert_close(out, expected, rtol=1e-4, atol=1e-5)


def test_shifted_labels_finite_gradients_and_tie(model):
    ids = torch.tensor([[2,5,9,7,6,10,11,7,0]])
    labels = torch.tensor([[-100,-100,-100,-100,-100,10,11,7,-100]])
    out = model(ids, labels=labels)
    selected = out.logits[0, [4,5,6]]
    expected = torch.nn.functional.cross_entropy(selected, torch.tensor([10,11,7]))
    torch.testing.assert_close(out.loss, expected)
    out.loss.backward()
    assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in model.parameters())
    assert model.lm_head.weight is model.model.embed_tokens.weight


def test_save_load_and_limits(model, tmp_path):
    model.save(tmp_path)
    loaded = JMicroModel.load(tmp_path)
    ids = torch.tensor([[2,9,10]])
    torch.testing.assert_close(model(ids).logits, loaded(ids).logits, atol=0, rtol=0)
    assert loaded.lm_head.weight is loaded.model.embed_tokens.weight
    model.config["max_position_embeddings"] = 3
    cache = model(ids, use_cache=True).cache
    with pytest.raises(ValueError, match="Context exceeded"):
        model(torch.tensor([[11]]), cache=cache)
    with pytest.raises(ValueError, match="No supervised"):
        model(ids, labels=torch.full_like(ids, -100))


def test_hf_independent_eager_reference(model):
    ids = torch.randint(8, 300, (1, 25))
    hf = model.hf_reference()
    with torch.no_grad():
        torch.testing.assert_close(model(ids).logits, hf(ids).logits, atol=1e-5, rtol=1e-4)
        prefix = hf(ids[:, :17], use_cache=True)
        torch.testing.assert_close(model(ids).logits[:, 17:], hf(ids[:, 17:], past_key_values=prefix.past_key_values).logits, atol=1e-5, rtol=1e-4)
