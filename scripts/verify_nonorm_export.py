"""Verify learned NoNorm HF/Llama and native float GGUF, without training."""
from pathlib import Path
import argparse
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from transformers import AutoModelForCausalLM
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.export import export_hf, export_gguf
from jmicro.inference import generate, native
from jmicro.model import JMicroModel, RMSNorm
from jmicro.phase2 import golden_cases
from jmicro.phase3 import compare as strict_compare, tensor_types
from jmicro.tokenizer import Tokenizer, CODEC_VERSION
from jmicro.training import implementation_hashes, source_snapshot


def compare(actual, expected, tolerance):
    """Retain every strict failure so all backends/cache paths are diagnosed."""
    try:
        return strict_compare(actual, expected, tolerance)
    except AssertionError as error:
        actual, expected = torch.as_tensor(actual), torch.as_tensor(expected)
        if actual.shape != expected.shape:
            return {'passed':False,'failure':str(error),'shape':list(actual.shape),'expected_shape':list(expected.shape)}
        delta = (actual-expected).abs()
        return {'passed':False,'failure':str(error),'shape':list(actual.shape),
            'finite':bool(torch.isfinite(actual).all() and torch.isfinite(expected).all()),
            'max_abs_error':float(delta.max()),'mean_abs_error':float(delta.mean()),
            'elements_outside_frozen_tolerance':int((delta>tolerance['atol']+tolerance['rtol']*expected.abs()).sum()),
            'tolerance':tolerance}


def verify(output, runtime, threads=2, precision_profile=None, inputs_from=None):
    torch.set_num_threads(threads)
    torch.manual_seed(42)
    output.mkdir(parents=True, exist_ok=True)
    candidate = read_json(ROOT/'reports/phase5/candidate_configs.json')['100m-no-qknorm']
    checkpoint = Path(candidate['checkpoint'])
    assert sha256(checkpoint) == candidate['checkpoint_sha256']
    state = torch.load(checkpoint, map_location='cpu', weights_only=False)
    assert state['model_config'] == candidate['model_config'] and state['update'] == 12208
    model = JMicroModel(state['model_config']).eval()
    model.load_state_dict(state['model'], strict=True)
    tok = Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    assert sha256(tok.path) == read_json(ROOT/'configs/phase6/performance.json')['tokenizer_sha256']
    tolerance = read_json(ROOT/'configs/evaluation/protocol.json')['numeric_tolerances']['fp32_reference_logits']
    receipt = read_json(runtime/'source_receipt.json')
    assert receipt['revision'] == '46ca246de9bb1c35269722a6240d37d9dfd79cad'
    assert receipt['archive_sha256'] == 'ce86fc42c03c5b93d25cd8b555bce6660b684f131e2047d4265bbb07fa1e9ceb'
    bridge = runtime/'llama-bridge'
    assert receipt['bridge_binary_sha256'] == sha256(bridge)
    for patch in receipt.get('patches', []):
        for entry in patch.get('files',[patch]):
            assert sha256(runtime/'llama.cpp'/entry['file']) == entry.get('final_patched_sha256',entry['patched_sha256'])
    if precision_profile:
        from jmicro.inference_precision import install, PROFILE
        from jmicro.native_precision import validate_stable_runtime
        assert precision_profile == PROFILE
        validate_stable_runtime(runtime)
    import os
    binding = {'checkpoint': str(checkpoint), 'checkpoint_sha256': sha256(checkpoint), 'tokenizer_sha256': sha256(tok.path), 'implementation': implementation_hashes(), 'verifier_sha256': sha256(Path(__file__)), 'protocol_sha256': sha256(ROOT/'configs/evaluation/protocol.json'), 'runtime_receipt_sha256': sha256(runtime/'source_receipt.json'), 'cpu_threads':threads, 'cpu_environment':{key:os.environ.get(key) for key in ('MKL_CBWR','MKL_DYNAMIC','OMP_DYNAMIC')}}
    binding.update(inference_precision=precision_profile or 'stock-fp32',
                   inference_precision_source_sha256=sha256(ROOT/'src/jmicro/inference_precision.py') if precision_profile else None,
                   fixed_inputs_sha256=sha256(inputs_from) if inputs_from else None)
    if (output/'binding.json').exists():
        assert read_json(output/'binding.json') == binding
    else:
        write_json(output/'binding.json', binding)
        write_json(output/'source_sha256.json', source_snapshot(output/'snapshot'))
    report = {'status': 'running', 'binding': binding, 'runtime': receipt, 'tolerance': tolerance, 'checks': {}, 'comparisons': {}, 'scope': 'Learned NoNorm export/cache/controller integrity; not Base quality or quantized quality'}
    write_json(output/'nonorm_export_parity_report.json', report)
    model.save(output/'torch')
    write_json(output/'torch/artifact_manifest.json', {'tokenizer_sha256': sha256(tok.path), 'weights_sha256': sha256(output/'torch/model.safetensors'), 'codec': CODEC_VERSION,
        **({'inference_precision':precision_profile} if precision_profile else {})})
    hf = export_hf(model, tok.path, output/'hf', inference_precision=precision_profile)
    loaded = AutoModelForCausalLM.from_pretrained(output/'hf', local_files_only=True, attn_implementation='eager').eval()
    names = export_gguf(output/'hf', output/'model-f32.gguf', model.config)
    checks = report['checks']
    checks['hf_llama_architecture_without_qknorm'] = loaded.config.model_type == 'llama' and not any('q_norm' in name or 'k_norm' in name for name in loaded.state_dict())
    checks['hf_tied_embedding'] = loaded.lm_head.weight is loaded.model.embed_tokens.weight
    checks['learned_parameter_count'] = sum(parameter.numel() for parameter in model.parameters()) == 10001152
    sequences = {'short': [2, *tok.encode('こんにちは。\n今日は　晴れ？🤔 <|assistant|> ▁')], 'context1024': torch.randint(8, tok.vocab_size, (1024,)).tolist()}
    if inputs_from:
        fixed = read_json(inputs_from)['runs']
        original = {run['name'].removesuffix('_prefill'):sum(run['chunks'],[]) for run in fixed if run['name'].endswith('_prefill')}
        assert sequences == original, 'Keep the original fixed short/1024 inputs'
    if precision_profile:
        before = {name:parameter.detach().clone() for name,parameter in model.state_dict().items()}
        install(model)
        install(loaded)
        checks['precision_profile_keeps_all_weights_exact'] = all(torch.equal(before[name],parameter) for name,parameter in model.state_dict().items())
        checks['profile_is_real_artifact_inference'] = read_json(output/'torch/artifact_manifest.json')['inference_precision'] == read_json(output/'hf/artifact_manifest.json')['inference_precision'] == precision_profile
    requests = []
    for name, ids in sequences.items():
        split = min(11, len(ids)-2) if name == 'short' else 511
        for mode, chunks in [('prefill', [ids]), ('cache', [ids[:split], ids[split:split+1], ids[split+1:]])]:
            requests.append({'name': f'{name}_{mode}', 'chunks': chunks, 'logits_file': str(output/f'{name}_{mode}.f32')})
    response = native(output/'model-f32.gguf', {'runs': requests}, output/'native-float', bridge)
    checks['native_eos_and_eot_eog_metadata'] = response['native_eos_is_eog'] and response['native_eot_is_eog']
    with torch.inference_mode():
        for name, ids in sequences.items():
            tensor = torch.tensor([ids])
            expected = model(tensor).logits
            report['comparisons'][name+'_hf_full'] = compare(loaded(tensor).logits, expected, tolerance)
            split = min(11, len(ids)-2) if name == 'short' else 511
            own_prefix = model(tensor[:, :split], use_cache=True)
            own_parts, hf_parts = [own_prefix.logits], []
            own_cache, hf_cache = own_prefix.cache, None
            position = 0
            for width in [split, 1, len(ids)-split-1]:
                ref = loaded(tensor[:, position:position+width], past_key_values=hf_cache, use_cache=True)
                hf_parts.append(ref.logits)
                hf_cache = ref.past_key_values
                if position:
                    own = model(tensor[:, position:position+width], cache=own_cache, use_cache=True)
                    own_parts.append(own.logits)
                    own_cache = own.cache
                position += width
            report['comparisons'][name+'_torch_cache'] = compare(torch.cat(own_parts, 1), expected, tolerance)
            report['comparisons'][name+'_hf_cache'] = compare(torch.cat(hf_parts, 1), expected, tolerance)
            arrays = []
            for mode in ('prefill', 'cache'):
                array = np.fromfile(output/f'{name}_{mode}.f32', dtype='<f4').reshape(1, len(ids), tok.vocab_size)
                arrays.append(array)
                report['comparisons'][name+'_gguf_'+mode] = compare(array, expected, tolerance)
            report['comparisons'][name+'_gguf_cache_vs_prefill'] = compare(arrays[1], arrays[0], tolerance)
    checks['all_short_and_1024_logits_cache_comparisons'] = all(item['passed'] for item in report['comparisons'].values())
    report['float_gguf'] = tensor_types(output/'model-f32.gguf')
    checks['tied_embedding_exported_once'] = report['float_gguf']['output_embedding_saved_once']
    report['weight_mapping'] = names
    checks['golden_external_codec_roundtrips'] = all(tok.decode(tok.encode(case['canonical'])) == case['canonical'] for case in golden_cases())
    report['ordinary_generation'] = {}
    for backend, artifact in [('torch', output/'torch'), ('hf', output/'hf'), ('gguf', output/'model-f32.gguf')]:
        report['ordinary_generation'][backend] = generate(backend, artifact, tok, sequences['short'], max_new_tokens=8, chat=False, work=output/f'generate-{backend}', bridge=bridge)
    checks['three_backend_greedy_ids_exact'] = len({tuple(item['generated_ids']) for item in report['ordinary_generation'].values()}) == 1
    report['model_driven_stop_fixtures'] = {}
    for stop_id in (3, 7):
        fixture = JMicroModel(model.config).eval()
        with torch.no_grad():
            for parameter in fixture.parameters():
                parameter.zero_()
            for module in fixture.modules():
                if isinstance(module, RMSNorm):
                    module.weight.fill_(1)
            fixture.model.embed_tokens.weight[6].fill_(.01)
            fixture.model.embed_tokens.weight[stop_id].fill_(1)
        location = output/f'stop-fixture-{stop_id}'
        fixture.save(location/'torch')
        write_json(location/'torch/artifact_manifest.json', {'tokenizer_sha256': sha256(tok.path), 'weights_sha256': sha256(location/'torch/model.safetensors'), 'codec': CODEC_VERSION,
            **({'inference_precision':precision_profile} if precision_profile else {})})
        export_hf(fixture, tok.path, location/'hf', inference_precision=precision_profile)
        export_gguf(location/'hf', location/'model.gguf', fixture.config)
        generated = {backend: generate(backend, artifact, tok, [2, 5, *tok.encode('はい'), 7, 6], max_new_tokens=8, chat=True, work=location/backend, bridge=bridge) for backend, artifact in [('torch', location/'torch'), ('hf', location/'hf'), ('gguf', location/'model.gguf')]}
        checks[f'actual_argmax_stop_{stop_id}_all_backends'] = all(item['generated_ids'] == [stop_id] and item['stop_reason'] == 'stop_id' for item in generated.values())
        report['model_driven_stop_fixtures'][str(stop_id)] = {'synthetic_controller_evidence_not_quality': True, 'results': generated}
    checks['original_checkpoint_unchanged'] = sha256(checkpoint) == binding['checkpoint_sha256']
    report.update(status='passed' if all(checks.values()) else 'failed', completed_at=now(), checks=checks)
    write_json(output/'nonorm_export_parity_report.json', report)
    print(json.dumps({'status': report['status'], 'checks': len(checks), 'comparisons': len(report['comparisons'])}), flush=True)
    assert all(checks.values()), checks


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--runtime', type=Path, default=ROOT/'artifacts/runtime')
    parser.add_argument('--threads', type=int, choices=[1,2], default=2)
    parser.add_argument('--precision-profile', choices=['cpu-f32-f64-accumulation-v1'])
    parser.add_argument('--inputs-from', type=Path, help='Assert identity with the preserved original native request')
    args = parser.parse_args()
    try:
        verify(args.output.resolve(), args.runtime.resolve(), args.threads, args.precision_profile, args.inputs_from)
    except Exception as error:
        report_path = args.output/'nonorm_export_parity_report.json'
        if report_path.exists():
            report = read_json(report_path)
            report.update(status='failed', failure=f'{type(error).__name__}: {error}', completed_at=now())
            write_json(report_path, report)
        raise
