"""Validate the real CPU profile's causal/cache, precision and safety contracts."""
import json
from pathlib import Path

import pytest
import torch

from jmicro.experiment import ROOT, sha256, write_json
from jmicro.inference_precision import install, probabilities
from jmicro.model import JMicroModel
from jmicro.native_precision import validate_stable_runtime


def model():
    config = json.loads((ROOT/'configs/models/t4k.json').read_text())
    config.update(qk_norm_type='none', num_hidden_layers=2, vocab_size=128)
    torch.manual_seed(42)
    return JMicroModel(config).eval()


def test_profile_preserves_weights_tie_and_full_chunk_and_hf_disk_reload(tmp_path):
    from transformers import AutoModelForCausalLM
    own = model()
    before = {name:weight.clone() for name,weight in own.state_dict().items()}
    own.hf_reference().save_pretrained(tmp_path)
    hf = install(AutoModelForCausalLM.from_pretrained(tmp_path,local_files_only=True,attn_implementation='eager').eval())
    install(own)
    ids = torch.randint(8,128,(1,1024))
    with torch.inference_mode():
        full = own(ids).logits
        hf_full = hf(ids).logits
        parts, refs, cache, past, offset = [], [], None, None, 0
        for width in (511,1,512):
            out = own(ids[:,offset:offset+width],cache=cache,use_cache=True)
            ref = hf(ids[:,offset:offset+width],past_key_values=past,use_cache=True)
            parts.append(out.logits); refs.append(ref.logits)
            cache, past, offset = out.cache, ref.past_key_values, offset+width
        for actual in (hf_full,torch.cat(parts,1),torch.cat(refs,1)):
            torch.testing.assert_close(actual,full,atol=1e-5,rtol=1e-4)
        changed = ids.clone(); changed[:,512:] = torch.randint(8,128,(1,512))
        torch.testing.assert_close(own(changed).logits[:,:512],full[:,:512],atol=0,rtol=0)
    assert own.lm_head.weight is own.model.embed_tokens.weight
    assert hf.lm_head.weight is hf.model.embed_tokens.weight
    assert all(torch.equal(before[name],weight) for name,weight in own.state_dict().items())


def test_profile_ragged_padding_matches_each_unpadded_sequence():
    own = install(model())
    ids = torch.randint(8,128,(2,13))
    valid = torch.tensor([[1]*13,[0,0,1,1,1,0,0,1,1,0,1,1,1]],dtype=torch.bool)
    with torch.inference_mode():
        full = own(ids,valid).logits
        prefix = own(ids[:,:7],valid[:,:7],use_cache=True)
        suffix = own(ids[:,7:],valid[:,7:],cache=prefix.cache,use_cache=True)
        torch.testing.assert_close(suffix.logits,full[:,7:],atol=1e-5,rtol=1e-4)
        for row in range(2):
            expected = own(ids[row:row+1,valid[row]]).logits[0]
            torch.testing.assert_close(full[row,valid[row]],expected,atol=1e-5,rtol=1e-4)
    assert torch.isfinite(full).all() and full[~valid].count_nonzero()==0


def test_stable_softmax_extremes_and_profile_rejects_training_or_autocast():
    values = torch.tensor([[1000.,1000.,-1000.],[-torch.inf,-torch.inf,-torch.inf]])
    assert torch.equal(probabilities(values),torch.tensor([[.5,.5,0.],[0.,0.,0.]]))
    with pytest.raises(ValueError,match='eval CPU FP32'):
        install(model().train())
    own = install(model())
    with pytest.raises(ValueError,match='inference_mode'):
        own(torch.tensor([[2,9]]))
    with torch.inference_mode(),torch.autocast('cpu',dtype=torch.bfloat16):
        with pytest.raises(ValueError,match='inference_mode'):
            own(torch.tensor([[2,9]]))


def test_runtime_validation_binds_shared_libraries_and_refuses_stock(tmp_path):
    source = tmp_path/'llama.cpp/ggml/src/ggml-cpu/vec.cpp'
    source.parent.mkdir(parents=True)
    source.write_text('explicit patched source fixture')
    bridge = tmp_path/'llama-bridge'; bridge.write_bytes(b'bridge fixture')
    library = tmp_path/'build/libggml-cpu.so'; library.parent.mkdir(); library.write_bytes(b'CPU kernel fixture')
    receipt = {'revision':'46ca246de9bb1c35269722a6240d37d9dfd79cad',
        'archive_sha256':'ce86fc42c03c5b93d25cd8b555bce6660b684f131e2047d4265bbb07fa1e9ceb',
        'patches':[{'name':'stable-f32-accumulation-v2','files':[{'file':str(source.relative_to(tmp_path/'llama.cpp')),'patched_sha256':sha256(source)}]}],
        'bridge_binary_sha256':sha256(bridge),'shared_library_sha256':{'build/libggml-cpu.so':sha256(library)},
        'commands':[['cmake','-DGGML_LLAMAFILE=OFF','-DCMAKE_CXX_FLAGS=-ffp-contract=off']]}
    write_json(tmp_path/'source_receipt.json',receipt)
    assert validate_stable_runtime(tmp_path)==receipt
    library.write_bytes(b'changed kernel')
    with pytest.raises(AssertionError):
        validate_stable_runtime(tmp_path)
    receipt['patches']=[]; write_json(tmp_path/'source_receipt.json',receipt)
    with pytest.raises(AssertionError,match='Stable FP32 runtime'):
        validate_stable_runtime(tmp_path)
