"""Real 200-update versus 100+100-update verification (launch through uv)."""
from pathlib import Path
import argparse
import json
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import torch
from jmicro.experiment import ROOT, read_json, write_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shards", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--device", default="cuda", choices=["cuda", "cpu"])
    parser.add_argument("--dtype", default="bf16", choices=["bf16", "fp32"])
    parser.add_argument("--model", type=Path, default=ROOT / "configs/models/t8k.json")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    # Fixed before seeing any result, matching the strict reference tolerances.
    report = {"status": "running", "device": args.device, "dtype": args.dtype,
              "steps": 200, "split_at": 100, "weight_atol": 1e-7, "weight_rtol": 1e-6,
              "loss_atol": 1e-6, "loss_rtol": 1e-5, "consumed_ids": "exact_digest_equality"}
    write_json(args.output / "resume_report.json", report)
    common = [sys.executable, str(ROOT / "scripts/train.py"), "train", "--shards", str(args.shards), "--model", str(args.model),
              "--device", args.device, "--dtype", args.dtype, "--batch", "2",
              "--schedule-updates", "200", "--save-every", "100"]
    stages = [("continuous", []), ("resumed", ["--stop-after", "100"]),
              ("resumed", ["--resume", str(args.output / "resumed/checkpoint-00000100.pt")])]
    try:
        for index, (name, extra) in enumerate(stages):
            with (args.output / f"stage-{index}.log").open("w") as log:
                subprocess.run([*common, "--output", str(args.output / name), *extra], check=True,
                               stdout=log, stderr=subprocess.STDOUT)
            print(json.dumps({"stage": index, "run": name, "status": "passed"}), flush=True)
        metrics = [[json.loads(line) for line in (args.output / name / "metrics.jsonl").read_text().splitlines()]
                   for name in ("continuous", "resumed")]
        if len(metrics[0]) != 200 or len(metrics[1]) != 200:
            raise ValueError("Missing/duplicate updates")
        assert [r["token_digest"] for r in metrics[0]] == [r["token_digest"] for r in metrics[1]]
        losses = [torch.tensor([r["loss"] for r in rows], dtype=torch.float64) for rows in metrics]
        torch.testing.assert_close(*losses, atol=report["loss_atol"], rtol=report["loss_rtol"])
        states = [torch.load(args.output / name / "checkpoint-00000200.pt", map_location="cpu", weights_only=False)
                  for name in ("continuous", "resumed")]
        differences = []
        for name, weight in states[0]["model"].items():
            other = states[1]["model"][name]
            torch.testing.assert_close(weight, other, atol=report["weight_atol"], rtol=report["weight_rtol"])
            differences.append(float((weight-other).abs().max()))
        assert states[0]["sampler"] == states[1]["sampler"]
        assert states[0]["scheduler"] == states[1]["scheduler"]
        assert states[0]["tokens"] == states[1]["tokens"]
        report.update(status="passed", consumed_ids_equal=True,
                      max_loss_difference=float((losses[0]-losses[1]).abs().max()),
                      max_weight_difference=max(differences), tokens_per_run=states[0]["tokens"],
                      sampler=states[0]["sampler"], checkpoints=[str((args.output / name / "checkpoint-00000200.pt").resolve()) for name in ("continuous", "resumed")])
    except Exception as exc:
        report.update(status="failed", failure=f"{type(exc).__name__}: {exc}")
        raise
    finally:
        write_json(args.output / "resume_report.json", report)
    print(json.dumps(report), flush=True)


if __name__ == "__main__":
    main()
