import pytest

from jmicro.text_display import decode_display


@pytest.mark.parametrize('text', ['ASCII', '楓', '😀', '日本語\n emoji😀', ''])
def test_complete_text_is_unchanged(text):
    result = decode_display(text.encode(), 'stop_id')
    assert result['text'] == result['raw_text'] == result['display_text'] == text
    assert result['valid_utf8'] and not result['truncated_utf8_tail']
    assert not result['pending_utf8_bytes_hex'] and result['utf8_error'] is None


@pytest.mark.parametrize('char,length', [('楓',1), ('楓',2), ('😀',1), ('😀',2), ('😀',3)])
def test_cap_tail_keeps_only_complete_characters_and_preserves_raw_failure(char, length):
    tail = char.encode()[:length]
    raw = '完成文。'.encode() + tail
    result = decode_display(raw, 'max_new_tokens')
    assert result['text'] == '完成文。'
    assert result['raw_text'] == raw.decode(errors='replace')
    assert result['pending_utf8_bytes_hex'] == tail.hex()
    assert result['truncated_utf8_tail'] and not result['raw_valid_utf8']
    assert result['utf8_error'] is None


@pytest.mark.parametrize('reason', ['stop_id', 'eos', 'eot'])
def test_incomplete_natural_stop_is_error_not_cap_trimming(reason):
    result = decode_display(b'A\xe6\xa5', reason)
    assert result['utf8_error']['reason'] == 'unexpected end of data'
    assert result['text'] == result['raw_text'] == 'A�'
    assert not result['valid_utf8'] and not result['truncated_utf8_tail']


@pytest.mark.parametrize('raw', [b'A\xffB', b'\xe6A', b'\xed\xa0\x80', b'\xf4\x90\x80\x80'])
def test_interior_surrogate_and_out_of_range_sequences_are_not_hidden(raw):
    result = decode_display(raw, 'max_new_tokens')
    assert result['utf8_error'] is not None
    assert not result['valid_utf8'] and not result['truncated_utf8_tail']
    assert result['text'] == raw.decode(errors='replace')


@pytest.mark.parametrize('backend', ['torch', 'hf', 'gguf'])
def test_all_backend_results_use_display_helper_and_keep_raw_ids(monkeypatch, tmp_path, backend):
    import sys
    from types import SimpleNamespace
    import torch
    import jmicro.inference as inference

    class Model:
        def eval(self):
            return self
        def __call__(self, current, **kwargs):
            scores = torch.zeros(1, current.shape[1], 10)
            scores[:, :, 8] = 1
            return SimpleNamespace(logits=scores, cache=None, past_key_values=None)
    class Tok:
        vocab_size, path = 10, tmp_path / 'tokenizer.model'
        def decode_bytes(self, ids):
            assert ids == [8]
            return b'A\xe6\xa5'
    monkeypatch.setattr(inference, 'read_json', lambda _: dict(vocab_size=10, tokenizer_sha256='hash', weights_sha256='hash'))
    monkeypatch.setattr(inference, 'sha256', lambda _: 'hash')
    monkeypatch.setattr(inference.JMicroModel, 'load', lambda _: Model())
    monkeypatch.setitem(sys.modules, 'transformers', SimpleNamespace(AutoModelForCausalLM=SimpleNamespace(from_pretrained=lambda *a, **kw: Model())))
    fields = {'jmicro.tokenizer_sha256': SimpleNamespace(contents=lambda: 'hash'),
              'tokenizer.ggml.tokens': SimpleNamespace(contents=lambda: list(range(10)))}
    monkeypatch.setitem(sys.modules, 'gguf', SimpleNamespace(GGUFReader=lambda _: SimpleNamespace(fields=fields)))
    monkeypatch.setattr(inference, 'native', lambda *a, **kw: dict(vocab_size=10, generation=dict(ids=[8], stop_reason='max_new_tokens')))
    result = inference.generate(backend, tmp_path, Tok(), [2], max_new_tokens=1, chat=False)
    assert result['text'] == 'A' and result['raw_text'] == 'A�'
    assert result['generated_ids'] == [8] and result['generated_body_bytes_hex'] == '41e6a5'
    assert result['stop_reason'] == 'max_new_tokens' and not result['valid_utf8']


def test_lossless_codec_still_rejects_unknown_token():
    from jmicro.experiment import ROOT
    from jmicro.tokenizer import Tokenizer
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    with pytest.raises(ValueError, match='Unknown token'):
        tok.decode_bytes([1])
