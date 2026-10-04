from types import SimpleNamespace
import torch
from jmicro.evaluation_memory import bound_evaluation_cache


def test_evaluation_cache_release_does_not_change_forward_input_or_output(monkeypatch):
    released = []
    monkeypatch.setattr(torch.cuda, 'memory_allocated', lambda: 1024**3)
    monkeypatch.setattr(torch.cuda, 'memory_reserved', lambda: 10 * 1024**3)
    monkeypatch.setattr(torch.cuda, 'empty_cache', lambda: released.append(True))
    class Echo(torch.nn.Module):
        def forward(self, value):
            return value
    model = Echo()
    state = bound_evaluation_cache(model)
    value = SimpleNamespace(device=SimpleNamespace(type='cuda'))
    for _ in range(64):
        assert model(value) is value
    assert len(released) == state['cache_releases'] == 2
    assert state['maximum_observed_allocated_bytes'] == 1024**3


def test_cpu_evaluation_does_not_touch_cuda_allocator(monkeypatch):
    monkeypatch.setattr(torch.cuda, 'memory_allocated', lambda: (_ for _ in ()).throw(AssertionError('CPU touched CUDA')))
    model = torch.nn.Linear(2, 2)
    reference = torch.ones(1, 2)
    expected = model(reference)
    state = bound_evaluation_cache(model)
    for _ in range(64):
        assert torch.equal(model(reference), expected)
    assert state['cache_releases'] == 0
