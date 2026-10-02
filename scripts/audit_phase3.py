"""Audit Phase 3 completion against current artifacts, native outputs and tests."""
from pathlib import Path
import argparse
import json
import sys
import tarfile
import hashlib
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import numpy as np
import torch
from jmicro.experiment import ROOT, read_json, write_json, sha256, now, verify_run, source_files
from jmicro.model import JMicroModel
from jmicro.phase3 import compare, tensor_types
from jmicro.phase2 import check_tokenizer
from jmicro.tokenizer import Tokenizer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", type=Path, required=True)
    args = parser.parse_args()
    args.snapshot = args.snapshot.resolve()
    torch.set_num_threads(2)
    reports = ROOT / "reports/phase3"
    models = read_json(reports / "model_contract_report.json")
    exports = read_json(reports / "export_parity_report.json")
    comparison = read_json(ROOT / "reports/phase2/tokenizer_comparison.json")
    assert models["status"] == exports["status"] == comparison["status"] == "passed"
    assert not models["training_performed"]
    assert exports["lock_sha256"] == sha256(ROOT / "uv.lock")
    cli = read_json(reports/"cli_checks.json")
    assert cli["status"] == "passed" and len(cli["checks"]) == 6
    assert cli["inference_source_sha256"] == sha256(ROOT/"src/jmicro/inference.py")
    assert cli["infer_source_sha256"] == sha256(ROOT/"scripts/infer.py")
    assert all(c["exit_code"] == 0 and c["result"]["generated_ids"] for c in cli["checks"])
    validation = read_json(reports/"config_validation.json")
    assert validation["status"] == "passed"
    assert all(sha256(ROOT/c["path"]) == c["sha256"] for c in validation["configs"])
    candidates = read_json(ROOT/"reports/phase2/tokenizer_training_candidates.json")
    assert len(candidates) == 6 and all(c["status"] == "passed" for c in candidates)
    for c in candidates:
        candidate = ROOT/f"artifacts/phase2/candidates/{c['vocab_size']}/{c['coverage']}/tokenizer.model"
        assert sha256(candidate) == c["model_sha256"]
    tests = ET.parse(reports / "tests.xml").getroot().findall("testsuite")
    assert tests and sum(int(x.attrib["tests"]) for x in tests) >= 48
    assert all(int(x.attrib[k]) == 0 for x in tests for k in ["failures","errors","skipped"])
    test_count = sum(int(x.attrib["tests"]) for x in tests)
    snapshot = verify_run(args.snapshot)
    manifest = read_json(args.snapshot / "source_manifest.json")
    # Verify frozen snapshot covers exactly the currently delivered source tree.
    entries = manifest
    current = {str(p.relative_to(ROOT)):sha256(p) for p in source_files(ROOT)}
    frozen = {entry["path"]:entry["sha256"] for entry in entries}
    assert current == frozen, "Source changed after snapshot"
    receipt = read_json(ROOT / "artifacts/runtime/source_receipt.json")
    assert receipt == exports["runtime"]
    assert receipt["revision"] == "46ca246de9bb1c35269722a6240d37d9dfd79cad"
    archive = ROOT / "artifacts/runtime/llama-source.tar.gz"
    assert sha256(archive) == receipt["archive_sha256"]
    assert sha256(ROOT / "scripts/llama_bridge.cpp") == receipt["bridge_source_sha256"]
    for key,path in [("bridge_binary_sha256","artifacts/runtime/llama-bridge"),
                     ("quantizer_binary_sha256","artifacts/runtime/build/bin/llama-quantize"),
                     ("completion_binary_sha256","artifacts/runtime/build/bin/llama-completion")]:
        assert sha256(ROOT/path) == receipt[key]
    source_checked = 0
    with tarfile.open(archive) as tar:
        for member in tar:
            if not member.isfile(): continue
            relative = Path(*Path(member.name).parts[1:])
            original = hashlib.sha256(tar.extractfile(member).read()).hexdigest()
            assert sha256(ROOT/"artifacts/runtime/llama.cpp"/relative) == original, str(relative)
            source_checked += 1
    gates = {}
    files = {}
    for name,count in [("t4k",10002816),("t8k",9772800)]:
        directory = ROOT/f"artifacts/phase3/{name}"
        config = read_json(ROOT/f"configs/models/{name}.json")
        model_report = models["models"][name]
        export_report = exports["models"][name]
        assert model_report["config_sha256"] == sha256(ROOT/f"configs/models/{name}.json")
        model = JMicroModel.load(directory/"torch").eval()
        assert model.config == config
        assert sum(p.numel() for p in model.parameters()) == model_report["parameter_count"] == count
        assert model.lm_head.weight is model.model.embed_tokens.weight
        tok = Tokenizer(ROOT/f"artifacts/phase2/{config['vocab_size']}/tokenizer.model")
        checks = check_tokenizer(tok)
        assert checks["vocab_size"] == config["vocab_size"]
        assert sha256(tok.path) == read_json(tok.path.parent/"training_metadata.json")["model_sha256"]
        assert export_report["external_codec_contract_report_sha256"] == sha256(ROOT/"reports/phase2/tokenizer_contract_report.json")
        assert model_report["finite_gradient_all_parameters"] and model_report["context_overflow_rejected"]
        assert model_report["padding_vs_individual_sequences"]
        for key in ["hf_prefill","hf_disk_reload","torch_disk_reload","future_mask","ragged_cache"]:
            assert model_report[key]["passed"]
        assert "1024" in model_report["cache"]
        assert all(c["custom_vs_full"]["passed"] and c["hf_vs_full"]["passed"] for c in model_report["cache"].values())
        assert all(c["passed"] for c in export_report["float_logits"].values())
        request = read_json(directory/"native-float/request.json")
        native_verified = []
        with torch.no_grad():
            for run in request["runs"]:
                ids = [i for chunk in run["chunks"] for i in chunk]
                logits_path = Path(run["logits_file"])
                array = np.fromfile(logits_path,dtype="<f4").reshape(len(ids),tok.vocab_size)
                metric = compare(array,model(torch.tensor([ids])).logits[0],models["tolerance"])
                native_verified.append({"name":run["name"],"sha256":sha256(logits_path),**metric})
        assert len(native_verified) == 4 and max(x["shape"][0] for x in native_verified) == 1024
        for quant in ["Q8_0","Q4_0","Q4_K_M"]:
            path = directory/f"model-{quant.lower()}.gguf"
            observed = tensor_types(path)
            recorded = export_report["quantized"][quant]
            for key in ["file_bytes","file_sha256","type_counts","tensors","output_embedding_saved_once"]:
                assert observed[key] == recorded[key]
            assert observed["output_embedding_saved_once"]
            assert recorded["load_generation"]["generated_ids"]
            assert recorded["log_sha256"] == sha256(directory/f"quantize-{quant}.log")
            response = read_json(directory/f"generate-{quant}/response.json")["generation"]
            assert response["ids"] == recorded["load_generation"]["generated_ids"]
            files[str(path.relative_to(ROOT))] = sha256(path)
        for stop in ["7","3"]:
            for backend in ["torch","hf","gguf"]:
                outcome = export_report["model_driven_stop_tests"][stop]["results"][backend]
                assert outcome["generated_ids"] == [int(stop)] and outcome["stop_reason"] == "stop_id"
                if backend == "gguf":
                    native_result = read_json(directory/f"stop-fixture-{stop}/run-gguf/response.json")
                    assert native_result["generation"]["ids"] == [int(stop)]
        assert export_report["native_eot_is_eog"] and export_report["native_eos_is_eog"]
        assert export_report["generic_cli"]["runnable"]
        assert not export_report["builtin_tokenizer"]["generic_cli_contract_compatible"]
        for path in [tok.path,directory/"torch/model.safetensors",directory/"hf/model.safetensors",directory/"model-f32.gguf"]:
            files[str(path.relative_to(ROOT))] = sha256(path)
        gates[name] = {"parameter_count":count,"native_outputs_rechecked":native_verified,
                       "model_cache_hf":True,"tokenizer_contract":True,"external_codec_chosen":True,
                       "actual_model_generated_stops":True,"all_quantized_loaded_and_generated":True,
                       "tensor_type_size_hash_checks":True,"generic_cli_ids_compatible":False}
    report = {"status":"passed","audited_at":now(),"goal":"Phase 3 complete; no model training",
              "gates":gates,"tests":{"count":test_count,"failures":0,"errors":0,"skipped":0,"xml_sha256":sha256(reports/"tests.xml")},
              "runtime_archive_source_files_checked":source_checked,"snapshot":str(args.snapshot.relative_to(ROOT)),
              "snapshot_verification":snapshot,"source_files":len(current),"artifact_hashes":files,
              "report_hashes":{str(p.relative_to(ROOT)):sha256(p) for p in [reports/"model_contract_report.json",reports/"export_parity_report.json",
                 reports/"cli_checks.json",reports/"config_validation.json",ROOT/"reports/phase2/tokenizer_training_candidates.json",
                 ROOT/"reports/phase2/tokenizer_contract_report.json",ROOT/"reports/phase2/tokenizer_comparison.json"]},
              "remaining_phase4":["Windows/WSL GPU verification","shards and training loop","save/resume","largest stable RTX4090 micro batch"],
              "training_tokens_seen":0,"gpu_verified":False}
    write_json(reports/"completion_audit.json",report)
    print(json.dumps({"status":"passed","models":list(gates),"tests":test_count,"source_files":len(current)}))


if __name__ == "__main__":
    main()
