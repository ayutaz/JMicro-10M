"""Verify actual model/cache/HF/native GGUF/quantization gates before training."""
from collections import Counter
from pathlib import Path
import argparse
import importlib.metadata
import json
import subprocess
import time

import numpy as np
import torch
import gguf

from jmicro.experiment import ROOT, now, read_json, write_json, sha256
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.phase2 import golden_cases
from jmicro.export import export_hf, export_gguf
from jmicro.inference import native, generate


def compare(actual, expected, tolerance):
    actual, expected = torch.as_tensor(actual), torch.as_tensor(expected)
    assert actual.shape == expected.shape
    assert torch.isfinite(actual).all() and torch.isfinite(expected).all()
    torch.testing.assert_close(actual, expected, atol=tolerance["atol"], rtol=tolerance["rtol"])
    return {"passed": True, "shape": list(actual.shape), "max_abs_error": float((actual-expected).abs().max()),
            "mean_abs_error": float((actual-expected).abs().mean()), "tolerance": tolerance}


def tensor_types(path):
    reader = gguf.GGUFReader(path)
    tensors = [{"name": t.name, "type": t.tensor_type.name, "shape": t.shape.tolist(),
                "bytes": t.n_bytes} for t in reader.tensors]
    return {"file_bytes": path.stat().st_size, "file_sha256": sha256(path),
            "type_counts": dict(Counter(t["type"] for t in tensors)), "tensors": tensors,
            "output_embedding_saved_once": "output.weight" not in {t["name"] for t in tensors}}


def run():
    torch.set_num_threads(2)
    tolerance = read_json(ROOT / "configs/evaluation/protocol.json")["numeric_tolerances"]["fp32_reference_logits"]
    reports = ROOT / "reports/phase3"
    reports.mkdir(parents=True, exist_ok=True)
    receipt = read_json(ROOT / "artifacts/runtime/source_receipt.json")
    started = time.monotonic()
    contract_report = {"status": "running", "created_at": now(), "training_performed": False,
                       "models": {}, "tolerance": tolerance}
    export_report = {"status": "running", "created_at": now(), "models": {},
        "runtime": receipt, "runtime_backend": "CPU, two threads, F32 K/V, flash attention off",
        "dependencies": {p: importlib.metadata.version(p) for p in ["torch","transformers","sentencepiece","gguf","safetensors"]},
        "lock_sha256": sha256(ROOT / "uv.lock"), "tolerance_frozen_before_native_run": tolerance,
        "quality_evaluation": "Random weights; conversation/quantized quality deferred until trained"}
    for name in ("t4k", "t8k"):
        print(f"{name}: model contracts", flush=True)
        config = read_json(ROOT / f"configs/models/{name}.json")
        torch.manual_seed(42)
        model = JMicroModel(config).eval()
        count = sum(p.numel() for p in model.parameters())
        assert count == config["expected_parameter_count"]
        artifact = ROOT / f"artifacts/phase3/{name}"
        artifact.mkdir(parents=True, exist_ok=True)
        tok = Tokenizer(ROOT / f"artifacts/phase2/{config['vocab_size']}/tokenizer.model")
        model.save(artifact / "torch")
        write_json(artifact / "torch/artifact_manifest.json", {"tokenizer_sha256":sha256(tok.path),
                   "weights_sha256":sha256(artifact / "torch/model.safetensors"), "codec":"sp-unigram-protected-byte-v1"})
        reference = export_hf(model, tok.path, artifact / "hf")
        loaded = JMicroModel.load(artifact / "torch").eval()
        from transformers import AutoModelForCausalLM
        hf_loaded = AutoModelForCausalLM.from_pretrained(artifact / "hf", local_files_only=True, attn_implementation="eager").eval()
        measurements = {"parameter_count": count, "tied_embedding": model.lm_head.weight is model.model.embed_tokens.weight,
                        "config_sha256": sha256(ROOT / f"configs/models/{name}.json"), "cache": {}}
        body = tok.encode("こんにちは。\n今日は　晴れ？🤔 <|assistant|> ▁")
        short = torch.tensor([[2,5,*body,7,6]])
        with torch.no_grad():
            full = model(short).logits
            measurements["hf_prefill"] = compare(reference(short).logits, full, tolerance)
            measurements["hf_disk_reload"] = compare(hf_loaded(short).logits, full, tolerance)
            measurements["torch_disk_reload"] = compare(loaded(short).logits, full, {"atol":0,"rtol":0})
            future = short.clone(); future[:, 10:] = (future[:, 10:] + 20) % tok.vocab_size
            measurements["future_mask"] = compare(model(future).logits[:, :10], full[:, :10], {"atol":0,"rtol":0})
            for length, widths in [(len(short[0]), [7,1,3,len(short[0])-11]),
                                    (1024, [37,173,300,1,512,1])]:
                ids = short if length != 1024 else torch.randint(8,tok.vocab_size,(1,1024))
                expected = model(ids).logits
                custom_cache, hf_cache, position, own_parts, hf_parts = None, None, 0, [], []
                for width in widths:
                    out = model(ids[:,position:position+width], cache=custom_cache, use_cache=True)
                    ref = reference(ids[:,position:position+width], past_key_values=hf_cache, use_cache=True)
                    custom_cache, hf_cache = out.cache, ref.past_key_values
                    own_parts.append(out.logits); hf_parts.append(ref.logits)
                    position += width
                measurements["cache"][str(length)] = {"chunk_widths":widths,
                    "custom_vs_full":compare(torch.cat(own_parts,dim=1),expected,tolerance),
                    "hf_vs_full":compare(torch.cat(hf_parts,dim=1),expected,tolerance)}
                assert custom_cache.valid.sum().item() == length
                if length == 1024:
                    try: model(ids[:,:1],cache=custom_cache)
                    except ValueError: measurements["context_overflow_rejected"] = True
                    else: raise AssertionError("Context overflow accepted")
                    long_ids = ids[0].tolist()
                del expected, own_parts, hf_parts, custom_cache, hf_cache
            ragged_ids = torch.randint(8,tok.vocab_size,(2,24))
            valid = torch.ones_like(ragged_ids,dtype=torch.bool); valid[1,7:16] = False
            ragged_full = model(ragged_ids,valid).logits
            prefix = model(ragged_ids[:,:16],valid[:,:16],use_cache=True)
            suffix = model(ragged_ids[:,16:],valid[:,16:],cache=prefix.cache,use_cache=True)
            measurements["ragged_cache"] = compare(suffix.logits,ragged_full[:,16:],tolerance)
            for b in range(2):
                compare(ragged_full[b,valid[b]],model(ragged_ids[b:b+1,valid[b]]).logits[0],tolerance)
            measurements["padding_vs_individual_sequences"] = True
        messages = [{"role":"user","text":"元気？"},{"role":"assistant","text":"元気です。"}]
        ids, labels = tok.dialogue(messages)
        loss = model(torch.tensor([ids]),labels=torch.tensor([labels])).loss
        loss.backward()
        assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in model.parameters())
        measurements["finite_gradient_all_parameters"] = True
        measurements["assistant_only_shifted_loss"] = float(loss.detach())
        model.zero_grad(set_to_none=True)
        contract_report["models"][name] = measurements
        write_json(reports / "model_contract_report.json",contract_report)

        print(f"{name}: native float GGUF", flush=True)
        names = export_gguf(artifact / "hf", artifact / "model-f32.gguf", config)
        native_work = artifact / "native-float"
        native_work.mkdir(exist_ok=True)
        runs = []
        native_sequences = {"short": short[0].tolist(), "context1024":long_ids}
        for key, ids in native_sequences.items():
            split = 11 if key == "short" else 511
            for mode, chunks in [("prefill",[ids]),("cache",[ids[:split],ids[split:split+1],ids[split+1:]])]:
                runs.append({"name":key+"_"+mode,"chunks":chunks,"logits_file":str(native_work / f"{key}_{mode}.f32")})
        response = native(artifact / "model-f32.gguf",{"runs":runs,"tokenize":[c["canonical"] for c in golden_cases()]},native_work)
        parity = {"weight_mapping":names,"float_gguf":tensor_types(artifact / "model-f32.gguf"),"float_logits":{},
                  "native_eot_is_eog":response["native_eot_is_eog"], "native_eos_is_eog":response["native_eos_is_eog"]}
        assert response["native_eot_is_eog"] and response["native_eos_is_eog"]
        with torch.no_grad():
            for key, ids in native_sequences.items():
                expected = model(torch.tensor([ids])).logits[0]
                native_outputs = []
                for mode in ("prefill","cache"):
                    array = np.fromfile(native_work / f"{key}_{mode}.f32",dtype="<f4").reshape(len(ids),tok.vocab_size)
                    parity["float_logits"][key+"_"+mode] = compare(array,expected,tolerance)
                    native_outputs.append(array)
                parity["float_logits"][key+"_native_cache_vs_prefill"] = compare(native_outputs[1],native_outputs[0],tolerance)
        golden = []
        for case, native_case in zip(golden_cases(),response["tokenize"],strict=True):
            ids = tok.encode(case["canonical"])
            golden.append({"id":case["id"],"external_ids":ids,"native_ids":native_case["ids"],
                           "ids_equal":ids==native_case["ids"],"native_decode_equal":native_case["decoded"]==case["canonical"]})
        parity["builtin_tokenizer"] = {"cases":golden,"matching_ids":sum(c["ids_equal"] for c in golden),
                                      "total":len(golden),"generic_cli_contract_compatible":all(c["ids_equal"] and c["native_decode_equal"] for c in golden)}
        parity["chosen_distribution_path"] = "External SentencePiece protected-byte codec -> native token IDs; decode with same codec"
        parity["external_codec_contract_report_sha256"] = sha256(ROOT / "reports/phase2/tokenizer_contract_report.json")
        parity["quantized"] = {}
        for quant in ("Q8_0","Q4_0","Q4_K_M"):
            print(f"{name}: {quant}",flush=True)
            path = artifact / f"model-{quant.lower()}.gguf"
            with (artifact / f"quantize-{quant}.log").open("w") as log:
                subprocess.run([str(ROOT / "artifacts/runtime/build/bin/llama-quantize"),
                                str(artifact / "model-f32.gguf"),str(path),quant,"2"],check=True,stdout=log,stderr=log)
            quant_report = tensor_types(path)
            quant_report["log_sha256"] = sha256(artifact / f"quantize-{quant}.log")
            quant_report["ffn_down_types"] = dict(Counter(t["type"] for t in quant_report["tensors"] if ".ffn_down." in t["name"]))
            quant_report["load_generation"] = generate("gguf",path,tok,short[0].tolist(),max_new_tokens=8,
                                                       work=artifact / f"generate-{quant}")
            assert len(quant_report["load_generation"]["generated_ids"]) > 0
            assert not set(quant_report["load_generation"]["generated_ids"]) & {0,1,2,4,5,6}
            wrapper_bytes = sum(p.stat().st_size for p in (artifact / "hf").iterdir() if p.name != "model.safetensors")
            quant_report["gguf_plus_tokenizer_config_bytes"] = path.stat().st_size + wrapper_bytes
            parity["quantized"][quant] = quant_report
        parity["generation_backends"] = {}
        for backend, path in [("torch",artifact/"torch"),("hf",artifact/"hf"),("gguf",artifact/"model-f32.gguf")]:
            ordinary = generate(backend,path,tok,short[0].tolist(),max_new_tokens=8,work=artifact/f"generate-{backend}")
            stops = {}
            for stop_id in [7,3]:
                result = generate(backend,path,tok,short[0].tolist(),max_new_tokens=8,
                                  work=artifact/f"stop-{backend}-{stop_id}",forced_first_id=stop_id)
                assert result["generated_ids"] == [stop_id] and result["stop_reason"] == "stop_id"
                stops[str(stop_id)] = result
            parity["generation_backends"][backend] = {"ordinary":ordinary,"forced_stop_controller_tests":stops}
        assert parity["generation_backends"]["torch"]["ordinary"]["generated_ids"] == parity["generation_backends"]["hf"]["ordinary"]["generated_ids"]
        parity["model_driven_stop_tests"] = {}
        # Actual greedy logits select EOT/EOS in a synthetic weight fixture;
        # this verifies the native path without injecting a token into sampling.
        for stop_id in [7,3]:
            fixture = JMicroModel(config).eval()
            with torch.no_grad():
                for parameter in fixture.parameters():
                    parameter.zero_()
                for module in fixture.modules():
                    from jmicro.model import RMSNorm
                    if isinstance(module,RMSNorm): module.weight.fill_(1)
                fixture.model.embed_tokens.weight[6].fill_(0.01)
                fixture.model.embed_tokens.weight[stop_id].fill_(1)
            destination = artifact / f"stop-fixture-{stop_id}"
            fixture.save(destination/"torch")
            write_json(destination/"torch/artifact_manifest.json", {"tokenizer_sha256":sha256(tok.path),
                       "weights_sha256":sha256(destination/"torch/model.safetensors"), "codec":"sp-unigram-protected-byte-v1"})
            export_hf(fixture,tok.path,destination/"hf")
            export_gguf(destination/"hf",destination/"model.gguf",config)
            selected = {}
            for backend,path in [("torch",destination/"torch"),("hf",destination/"hf"),("gguf",destination/"model.gguf")]:
                result = generate(backend,path,tok,[2,5,*tok.encode("はい"),7,6],max_new_tokens=8,
                                  work=destination/f"run-{backend}")
                assert result["generated_ids"] == [stop_id] and result["stop_reason"] == "stop_id"
                selected[backend] = result
            parity["model_driven_stop_tests"][str(stop_id)] = {"fixture":"synthetic weights; actual argmax, no forced ID",
                                                            "results":selected}
            del fixture
        parity["generic_cli"] = {"runnable":False,"tokenizer_contract_compatible":parity["builtin_tokenizer"]["generic_cli_contract_compatible"]}
        cli = ROOT / "artifacts/runtime/build/bin/llama-completion"
        command = [str(cli),"-m",str(artifact/"model-f32.gguf"),"-p","こんにちは","-n","4","-t","2","-ngl","0","-no-cnv"]
        output = subprocess.run(command,capture_output=True)
        (artifact / "generic-cli.stdout").write_bytes(output.stdout)
        (artifact / "generic-cli.stderr").write_bytes(output.stderr)
        assert output.returncode == 0
        parity["generic_cli"].update(runnable=True,exit_code=output.returncode,
            command=command,
            stdout_sha256=sha256(artifact/"generic-cli.stdout"),stderr_sha256=sha256(artifact/"generic-cli.stderr"),
            recommended=False,reason="Built-in tokenizer tested separately; external codec is normative")
        export_report["models"][name] = parity
        write_json(reports / "export_parity_report.json",export_report)
        del model,loaded,reference,hf_loaded
    contract_report["status"] = export_report["status"] = "passed"
    contract_report["completed_at"] = export_report["completed_at"] = now()
    export_report["elapsed_seconds"] = time.monotonic()-started
    for name, report in [("model_contract_report.json",contract_report),("export_parity_report.json",export_report)]:
        write_json(reports / name,report)
    print(json.dumps({"status":"passed","reports":str(reports)}))


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    run()
