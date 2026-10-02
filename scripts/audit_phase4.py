"""Audit completed Phase 4 evidence and write the measured budget; no Phase 5."""
from pathlib import Path
import argparse
import json
import math
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import numpy as np
import torch
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.shards import BlockSampler, Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import autocast, evaluate_body, generate_suite, gpu_lock, isolated_evaluation, rng_state
from jmicro.model import JMicroModel


def equal(left, right):
    if isinstance(left, torch.Tensor):
        assert torch.equal(left, right)
    elif isinstance(left, np.ndarray):
        assert np.array_equal(left, right)
    elif isinstance(left, dict):
        assert left.keys() == right.keys()
        for name in left:
            equal(left[name], right[name])
    elif isinstance(left, (tuple,list)):
        assert len(left) == len(right)
        for a,b in zip(left,right):
            equal(a,b)
    else:
        assert left == right


def size(directory):
    return sum(p.stat().st_size for p in directory.rglob("*") if p.is_file()) if directory.exists() else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--data-root", type=Path, default=Path.home() / "jmicro-data")
    args = parser.parse_args()
    torch.set_num_threads(2)
    report = {"status": "running", "phase": 4, "created_at": now(),
              "stop_boundary": "Stop now; Phase 5 requires user resumption", "gates": {}}
    try:
        environment = read_json(ROOT / "reports/phase4/environment.json")
        assert environment["platform"]["system"] == "Linux" and environment["platform"]["is_wsl"]
        assert environment["platform"]["python"] == "3.12.7"
        assert environment["torch_probe"]["cuda_available"] and environment["torch_probe"]["bf16_supported"]
        assert "4090" in environment["nvidia_smi"]["stdout"]
        restore = read_json(ROOT / "reports/phase4/artifact_restore.json")
        assert restore["status"] == "passed" and restore["verified_files"] == 25
        assert restore["revision"] == read_json(ROOT / "configs/hub/artifacts.json")["revision"]
        windows = json.loads((ROOT / "reports/phase4/windows_observation.json").read_text(encoding="utf-8-sig"))
        assert all(row["exit_code"] == 0 for row in windows["commands"])
        assert "3.0.1.0" in windows["commands"][0]["output"]
        assert "Ubuntu" in windows["commands"][1]["output"] and "2" in windows["commands"][1]["output"]
        report["windows_wsl_observation"] = windows
        tests = ET.parse(ROOT / "reports/phase4/training_tests.xml").getroot()
        suites = list(tests.iter("testsuite"))
        assert sum(int(s.get("tests",0)) for s in suites) >= 64
        assert all(int(s.get(key,0)) == 0 for s in suites for key in ("failures","errors","skipped"))
        report["gates"]["environment_artifacts_tests"] = "passed"
        states = {}
        evaluations = {}
        for model in ("t8k","t4k"):
            resume = read_json(args.run / f"resume-{model}/resume_report.json")
            assert resume["status"] == "passed" and resume["consumed_ids_equal"]
            checkpoints = [args.run / f"resume-{model}/{name}/checkpoint-00000200.pt" for name in ("continuous","resumed")]
            loaded = [torch.load(p, map_location="cpu", weights_only=False) for p in checkpoints]
            for key in ("model","optimizer","scheduler","rng","sampler","tokens","supervised_tokens","body_bytes","token_digest","implementation_sha256"):
                equal(loaded[0][key], loaded[1][key])
            assert all(torch.isfinite(weight).all() for weight in loaded[0]["model"].values())
            assert all(torch.isfinite(value).all() for state in loaded[0]["optimizer"]["state"].values() for value in state.values() if isinstance(value,torch.Tensor))
            states[model] = loaded[0]
            evaluation = read_json(args.run / f"evaluation-{model}.json")
            assert evaluation["body"]["documents"] == 924
            assert math.isfinite(evaluation["body"]["bpb"])
            outputs = evaluation["generation"]["outputs"]
            assert len(outputs) == 80 * 5 and all(row["split"] == "dev" for row in outputs)
            assert len({row["id"] for row in outputs}) == 80
            assert evaluation["generation"]["sampling_evaluated"]
            evaluations[model] = evaluation
        equal([(row["doc_id"],row["body_bytes"]) for row in evaluations["t8k"]["body"]["rows"]],
              [(row["doc_id"],row["body_bytes"]) for row in evaluations["t4k"]["body"]["rows"]])
        report["gates"]["resume_model_optimizer_scheduler_rng_sampler"] = "passed_exact"
        report["gates"]["held_out_common_bytes_and_fixed_dev_generation"] = "passed"
        with gpu_lock("cuda"):
            model = JMicroModel(states["t8k"]["model_config"]).to("cuda").train()
            model.load_state_dict(states["t8k"]["model"])
            before = rng_state()
            evaluate_body(model, Shard(args.data_root / "shards/t8k-pilot", "dev"), "cuda", "bf16", limit=4)
            generate_suite(model, Tokenizer(ROOT / "artifacts/phase2/8192/tokenizer.model"), "cuda", "bf16", limit=1, max_new=8, sampling=True)
            equal(before, rng_state())
            assert model.training
            other = JMicroModel(states["t4k"]["model_config"]).to("cuda").eval()
            other.load_state_dict(states["t4k"]["model"])
            compiled_parity = {}
            tolerance = read_json(ROOT / "configs/evaluation/protocol.json")["numeric_tolerances"]["bf16_logits"]
            for name,candidate in (("t8k",model),("t4k",other)):
                x,_,_ = BlockSampler(Shard(args.data_root / f"shards/{name}-pilot"),1024,42).batch(8)
                x = x.to("cuda")
                with isolated_evaluation(candidate), autocast("cuda","bf16"):
                    reference = candidate(x).logits
                    compiled = torch.compile(candidate)(x).logits
                    torch.testing.assert_close(reference,compiled,atol=tolerance["atol"],rtol=tolerance["rtol"])
                    compiled_parity[name] = {"max_logit_difference":float((reference-compiled).abs().max()),
                                             "tolerance":tolerance,"batch":8,"context":1024}
            report["compiled_bf16_logit_parity"] = compiled_parity
            tokenizers = {name:Tokenizer(ROOT / f"artifacts/phase2/{vocab}/tokenizer.model")
                          for name,vocab in (("t8k",8192),("t4k",4096))}
            dev = Shard(args.data_root / "shards/t8k-pilot", "dev")
            common = {"split": "dev", "documents": 32, "same_text": True, "rows": []}
            for row in dev.index[:32]:
                ids = dev.tokens[row["offset"]+1:row["offset"]+1+row["body_tokens"]].tolist()
                text = tokenizers["t8k"].decode(ids)[:256]
                while any(len(tok.encode(text)) > 1023 for tok in tokenizers.values()):
                    text = text[:-1]
                measured = {"doc_id": row["doc_id"], "canonical_bytes": len(text.encode()), "nll": {}}
                for name, candidate in (("t8k",model),("t4k",other)):
                    tokens = torch.tensor([[2,*tokenizers[name].encode(text)]],device="cuda")
                    with isolated_evaluation(candidate), autocast("cuda","bf16"):
                        logits = candidate(tokens).logits
                        nll = torch.nn.functional.cross_entropy(logits[0,:-1],tokens[0,1:],reduction="sum")
                    measured["nll"][name] = float(nll)
                common["rows"].append(measured)
            common["total_bytes"] = sum(row["canonical_bytes"] for row in common["rows"])
            common["bpb"] = {name:sum(row["nll"][name] for row in common["rows"]) / (math.log(2)*common["total_bytes"]) for name in tokenizers}
            write_json(args.run / "common_short_windows.json",common)
        report["gates"]["cuda_evaluation_rng_isolation"] = "passed"
        report["gates"]["common_short_text_windows"] = "passed"
        report["gates"]["compiled_bf16_logit_parity"] = "passed"
        throughput = read_json(args.run / "throughput/throughput_report.json")
        assert throughput["status"] == "passed"
        unsupported = []
        for model in ("t8k","t4k"):
            selected = throughput["selected"][model]
            assert selected["maximum_stable_batch"] + 1 == selected["first_oom_batch"]
            points = [r for r in throughput["results"] if r["model"] == model]
            confirmed = [r for r in points if r["status"] == "passed" and r["data_kind"] == "real" and not r["compile"] and r["backend"] == "default" and r["batch"] == selected["maximum_stable_batch"] and r["measured_updates"] == 200]
            assert len(confirmed) == 3
            assert any(r["status"] == "passed" and r["compile"] and r["measured_updates"] == 200 for r in points)
            assert any(r["status"] == "passed" and r["data_kind"] == "synthetic" for r in points)
            assert {r["backend"] for r in points} >= {"default","math","flash"}
            assert any(r["status"] == "passed" and r["backend"] == "math" for r in points)
            for point in points:
                if point["backend"] == "flash" and point["status"] == "failed":
                    log = Path(point["report"]).with_suffix(".log").read_text()
                    assert "Flash Attention does not support non-null attn_mask" in log
                    unsupported.append({"model": model, "backend": "flash", "reason": "explicit non-null attention mask is unsupported by this installed Flash kernel", "raw_report": point["report"]})
                elif point["status"] not in ("passed","oom"):
                    raise ValueError(f"Unresolved benchmark failure: {point['report']}")
        report["unsupported_optional_backends"] = unsupported
        report["gates"]["capacity_backend_compile_synthetic_real"] = "passed"
        report.update(status="passed", completed_at=now(), throughput=throughput["selected"],
            dev_bpb={model:evaluations[model]["body"]["bpb"] for model in evaluations},
            quality_claim="No trained Base/Chat capability claim; small Phase 4 validation runs only",
            trained_checkpoint_paths={model:str((args.run / f"resume-{model}/continuous/checkpoint-00000200.pt").resolve()) for model in states})
        report["evaluation_elapsed_seconds_approx"] = {name:(args.run / f"evaluation-{name}.json").stat().st_mtime - (args.run / f"resume-{name}.log").stat().st_mtime for name in states}
        # Extrapolations, including explicit evaluation/save allowance. No long job is started.
        storage = {"raw": size(ROOT / "data/phase1/raw"), "processed_pilot": size(ROOT / "data/phase1/processed"),
            "shards_both": size(args.data_root / "shards"), "phase4_reports_checkpoints_snapshots": size(ROOT / "reports/phase4"),
            "uv_download_cache": size(Path.home() / ".cache/uv"), "virtual_environment": size(ROOT / ".venv"),
            "free_linux_bytes": shutil.disk_usage(ROOT).free}
        lines = ["# Phase 4 measured resource budget", "", "Measurements are specific to RTX 4090 / WSL / PyTorch 2.14.1 / CUDA 13.0, context 1024, FP32 parameters + BF16 autocast.",
            "", "Maximum stable batch refers to eager/default SDPA with a 94% CUDA allocator ceiling and three 200-update confirmations, including evaluation/save. It is an operational bound, not indefinite stability or a global maximum across every compile/backend configuration.",
            "", "| Model | Stable micro batch | Effective batch tokens | Median tokens/s | Confirmation range |", "|---|---:|---:|---:|---|"]
        for name, point in throughput["selected"].items():
            lines.append(f"| {name} | {point['maximum_stable_batch']} | {point['maximum_stable_batch']*1024} | {point['confirmation_median_tokens_per_second']:.0f} | {point['confirmation_range_tokens_per_second']} |")
        lines.extend(["", "The fastest measured batch/configuration is separately recorded in throughput_report.json; compile cold start is excluded from steady throughput. Capacity is established for the eager baseline; compiled capacity was not searched.",
            "", "The explicit Flash-only backend rejected the model's non-null attention mask. This unsupported candidate is retained as a failed raw probe; default SDPA, math-only and compile/default have successful measurements. It is not a successful Flash benchmark. A mask-free causal training path would be a separate future optimization and is not implemented here.",
            "", "| Tokens | T8K compute hours | T4K compute hours |", "|---:|---:|---:|"])
        for tokens in (100_000_000,1_000_000_000,10_000_000_000,20_000_000_000,50_000_000_000):
            estimates = [tokens / throughput["selected"][name]["confirmation_median_tokens_per_second"] / 3600 for name in ("t8k","t4k")]
            lines.append(f"| {tokens:,} | {estimates[0]:.2f} | {estimates[1]:.2f} |")
        eval_seconds = sum(r.get("evaluation_seconds",0) for r in throughput["results"] if r["status"] == "passed")
        save_seconds = [r["save_seconds"] for r in throughput["results"] if r["status"] == "passed"]
        lines.extend(["", f"Capacity probes measured {eval_seconds:.2f} s total subset evaluation time. Checkpoint save range: {min(save_seconds):.3f}–{max(save_seconds):.3f} s. Full dev evaluation elapsed times are recorded in handoff_report.json. Add each planned full evaluation, checkpoint, comparison and cold compile to the compute-only estimates; no claim that the table is total project time.",
            "", "## Measured storage bytes", "", "```json", json.dumps(storage,indent=2), "```", "", "These are apparent file sizes; shared uv hardlinks are not deduplicated. Pilot unique train body bytes are 32,774,150 for both tokenizers; streams are 6,884,183 / 8,398,329 tokens including BOS/EOS. Fixed-length sampling omits the final incomplete train block; sampler blocks/cursor and actually consumed tokens/bytes are checkpointed. Longer budgets require explicitly reported repetition or staged corpus expansion. Master corpus is not acquired. uint16 shard projection is 2 bytes/token per tokenizer, before indexes/raw/temporary files/checkpoints.",
            "", "Stop boundary: Phase 4 complete. Do not launch Phase 5 until the user resumes."])
        (args.run / "resource_budget.md").write_text("\n".join(lines)+"\n")
        report["storage_bytes"] = storage
    except Exception as exc:
        report.update(status="failed", failure=f"{type(exc).__name__}: {exc}")
        raise
    finally:
        write_json(args.run / "handoff_report.json", report)
    print(json.dumps(report), flush=True)


if __name__ == "__main__":
    main()
