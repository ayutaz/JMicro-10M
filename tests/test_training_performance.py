import pytest
import torch

from jmicro.experiment import ROOT, read_json
from jmicro.model import JMicroModel
from jmicro import training


def tiny_model():
    config = read_json(ROOT/'configs/models/t4k.json')
    config.update(vocab_size=32, hidden_size=32, num_hidden_layers=2,
                  num_attention_heads=2, num_key_value_heads=1, head_dim=16,
                  rotary_dim=16, intermediate_size=48, attention_scale=.25,
                  qk_norm_type='none')
    return JMicroModel(config)


def test_unpadded_causal_fast_path_matches_reference_loss_and_gradients():
    torch.set_num_threads(2)
    torch.manual_seed(42)
    model = tiny_model()
    inputs = torch.randint(8, 32, (2, 16))
    targets = torch.randint(8, 32, (2, 16))
    reference = model(inputs).logits
    loss = torch.nn.functional.cross_entropy(reference.flatten(0, 1), targets.flatten())
    loss.backward()
    gradients = {name: parameter.grad.clone() for name, parameter in model.named_parameters()}
    model.zero_grad(set_to_none=True)
    optimized = model(inputs, training_fast_path=True).logits
    optimized_loss = torch.nn.functional.cross_entropy(optimized.flatten(0, 1), targets.flatten())
    optimized_loss.backward()
    torch.testing.assert_close(optimized, reference, atol=1e-5, rtol=1e-4)
    torch.testing.assert_close(optimized_loss, loss, atol=1e-6, rtol=1e-5)
    for name, parameter in model.named_parameters():
        torch.testing.assert_close(parameter.grad, gradients[name], atol=1e-7, rtol=1e-6)
    changed = inputs.clone()
    changed[:, -1] = 31
    torch.testing.assert_close(model(changed, training_fast_path=True).logits[:, :-1], optimized[:, :-1], atol=0, rtol=0)


@pytest.mark.parametrize('kwargs', [{'attention_mask': torch.ones(1, 4)}, {'use_cache': True}, {'labels': torch.ones(1, 4, dtype=torch.long)}])
def test_fast_path_rejects_padding_cache_and_label_interfaces(kwargs):
    with pytest.raises(ValueError, match='unpadded blocks'):
        tiny_model()(torch.full((1, 4), 8), training_fast_path=True, **kwargs)


def test_compiled_backend_cache_isolation_and_in_memory_reset(tmp_path, monkeypatch):
    monkeypatch.setattr(training, '_COMPILE_CACHE_ROOT', tmp_path)
    monkeypatch.setenv('TORCHINDUCTOR_CACHE_DIR', str(tmp_path/'original'))
    calls = []
    monkeypatch.setattr(torch._dynamo, 'reset', lambda: calls.append('reset'))
    base = {'backend': 'math', 'dtype': 'bf16', 'deterministic': True}
    first = training.configure_compile_cache(base)
    flash = training.configure_compile_cache(dict(base, backend='flash'))
    again = training.configure_compile_cache(base)
    assert first == again and first != flash
    assert calls == ['reset']*3
    assert __import__('os').environ['TORCHINDUCTOR_CACHE_DIR'] == again
    assert __import__('pathlib').Path(flash).is_dir()
    with pytest.raises(ValueError, match='Unknown attention backend'):
        training.configure_compile_cache(dict(base, backend='invalid'))
