"""Token-uniform, bounded supply comparison on the accepted native train mmap.

Containing documents have probability proportional to native record length.
The mean selected tokens / original record tokens estimates eligible supply;
unweighted mean selected document length would be biased toward long records.
"""
import argparse
from collections import Counter
import json
import multiprocessing as mp
from pathlib import Path
import random
import shutil
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
import numpy as np
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.eos_pilot import TrainView
from jmicro.larger_material_v2 import material_units
from jmicro.nested_material_v2 import material_unit
from jmicro.training import atomic_json
from phase6_performance import identity, alive
import prepare_complete_units as decode


def containing_document(tokens, offset, maximum_body=8192):
    """Return inclusive BOS/EOS, or None if outside the frozen length bound."""
    assert 0 <= offset < len(tokens)
    left = max(0, offset-maximum_body-1)
    right = min(len(tokens), offset+maximum_body+2)
    starts = np.flatnonzero(tokens[left:offset+1] == 2)
    ends = np.flatnonzero(tokens[offset:right] == 3)
    if not len(starts) or not len(ends):
        return None
    a, b = left+int(starts[-1]), offset+int(ends[0])
    return (a, b) if b-a-1 <= maximum_body else None


def inspect(offset):
    span = containing_document(decode._TRAIN, offset)
    row = dict(sampled_token=offset, record_start=None, record_tokens=None,
               first_tokens=0, all_four_tokens=0, first_rate=0., all_four_rate=0.)
    if span is None:
        return row
    a, b = span
    size = b-a-1
    row.update(record_start=a, record_tokens=size+2)
    if not 64 <= size <= 8192:
        return row
    ids = decode._TRAIN[a+1:b].tolist()
    if any(i < 8 for i in ids):
        return row
    try:
        text = b"".join(decode._PIECES[i] for i in ids).decode("utf-8")
    except UnicodeDecodeError:
        return row
    first = material_unit(text, ids, "web", decode._TOK)
    units = material_units(text, ids, "web", decode._TOK)
    assert (first is None) == (not units)
    if first:
        assert first["canonical_sha256"] == units[0]["canonical_sha256"]
        assert all(u["split"] == first["split"] and u["source_family"] == first["source_family"] for u in units)
    first_tokens = first["body_tokens"]+2 if first and first["split"] == "train" else 0
    all_tokens = sum(u["body_tokens"]+2 for u in units if u["split"] == "train")
    row.update(first_tokens=first_tokens, all_four_tokens=all_tokens,
               first_rate=first_tokens/(size+2), all_four_rate=all_tokens/(size+2))
    # Examples of the additional units only. Frozen first32 distinct parent
    # families, not a content-driven choice of good-looking examples.
    row["examples"] = [dict(u, source_start=a, source_end=b) for u in units[1:]]
    return row


def estimate(rows, total, seed):
    rates = np.asarray([[r["first_rate"], r["all_four_rate"]] for r in rows])
    rng = np.random.default_rng(seed)
    bootstrap = rates[rng.integers(0, len(rows), (2000, len(rows)))].mean(axis=1)*total
    return {name: dict(estimated_train_tokens=float(rates[:,i].mean()*total),
                       bootstrap_ci95=np.quantile(bootstrap[:,i], [.025,.975]).tolist())
            for i, name in enumerate(("first_eligible_unit", "all_eligible_first_four"))}


def run(args):
    assert sys.version_info[:3] == (3,12,7)
    assert 500 <= args.draws <= 10000 and 1 <= args.workers <= 8 and 0 < args.budget_seconds <= 600
    config = read_json(ROOT/"configs/phase6/architecture_comparison.json")
    view = TrainView(config["web_shards"], config["web_manifest_sha256"])
    assert view.manifest["tokenizer_sha256"] == config["tokenizer_sha256"]
    tok = ROOT/config["tokenizer"]; assert sha256(tok) == config["tokenizer_sha256"]
    scripts = ("scripts/probe_larger_web_supply.py", "src/jmicro/larger_material_v2.py",
               "src/jmicro/nested_material_v2.py", "src/jmicro/nested_material.py",
               "src/jmicro/complete_units.py", "src/jmicro/coherent_units.py",
               "src/jmicro/evaluation.py", "src/jmicro/tokenizer.py",
               "scripts/prepare_complete_units.py", "src/jmicro/eos_pilot.py")
    binding = dict(pool=config["web_shards"], manifest_sha256=config["web_manifest_sha256"],
        original_train_tokens=len(view.tokens), tokenizer_sha256=sha256(tok), draws=args.draws,
        workers=args.workers, seed=args.seed, CPU_budget_seconds=args.budget_seconds,
        source_sha256={p:sha256(ROOT/p) for p in scripts},
        sample_policy="Uniform native token offsets; containing BOS/EOS record; selected train tokens/original record tokens; oversized ineligible documents contribute zero",
        new_selector="All eligible first-four intact paragraphs unless whole body accepted; unchanged quality filters; all siblings first eligible family/split",
        caveat="Gross eligible supply; no corpus-wide canonical/near duplicate, protected-prefix or exact four-group loss adjustment; not distinct quantity or quality")
    output = args.output.resolve(); assert output.is_relative_to(ROOT/"reports/phase6")
    output.mkdir(parents=True, exist_ok=True); path = output/"job.json"
    if path.exists():
        old = read_json(path); assert old["binding"] == binding and not alive(old)
        if old["status"] == "complete": print("Completed supply comparison retained"); return
        raise RuntimeError("Preserve failed bounded comparison before a new attempt")
    start = time.monotonic(); rows = []; examples = []; example_families = set()
    job = dict(status="running", **identity(), binding=binding, started_at=now())
    def heartbeat():
        if time.monotonic()-start > args.budget_seconds: raise TimeoutError("Web supply probe exceeded frozen CPU budget")
        job.update(heartbeat_at=now(), completed_draws=len(rows), CPU_seconds=time.monotonic()-start)
        atomic_json(path, job)
    try:
        heartbeat(); atomic_json(output/"recipe.json", binding)
        for p in scripts:
            target=output/"source"/p; target.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(ROOT/p,target)
        rng=random.Random(args.seed); offsets=[rng.randrange(len(view.tokens)) for _ in range(args.draws)]
        with mp.get_context("fork").Pool(args.workers, initializer=decode.worker_init,
             initargs=(str(tok), str(view.directory/"train.bin"))) as pool:
            for row in pool.imap(inspect, offsets, chunksize=16):
                extra=row.pop("examples", []); rows.append(row)
                for unit in extra:
                    family=unit["source_family"]
                    if unit["split"] == "train" and family not in example_families and len(examples)<32:
                        example_families.add(family); examples.append(unit)
                if len(rows)%256 == 0: heartbeat()
        heartbeat(); measured=estimate(rows, len(view.tokens), args.seed)
        atomic_json(output/"draws.json",dict(binding=binding,rows=rows))
        atomic_json(output/"sample32.json",dict(binding=binding,examples=examples,
            selection="First32 distinct additional-unit train families in fixed token-uniform draw order; not content reviewed"))
        result=dict(status="bounded_supply_comparison_complete_not_prepared_or_distinct", binding=binding,
            estimates=measured, counts=dict(Counter("additional_units" if r["all_four_tokens"]>r["first_tokens"] else "same_or_rejected" for r in rows)),
            duplicate_record_draws=len(rows)-len({r["record_start"] for r in rows if r["record_start"] is not None})-sum(r["record_start"] is None for r in rows),
            target_web_train_tokens=1900000000,
            predicted_first_upper_below_target=measured["first_eligible_unit"]["bootstrap_ci95"][1]<1900000000,
            predicted_all_four_lower_above_target=measured["all_eligible_first_four"]["bootstrap_ci95"][0]>1900000000,
            new_prepared_tokens=0, GPU_teacher_tokens=0, protected_test_used=False,
            independent_human_blind=False, Base_adopted=False, requested_five_steps_complete=False,
            CPU_seconds=time.monotonic()-start,completed_at=now())
        atomic_json(output/"result.json",result); heartbeat(); job.update(status="complete",completed_at=now())
        print(json.dumps({k:v for k,v in result.items() if k!="binding"}),flush=True)
    except BaseException as error: job.update(status="failed",error=repr(error)); raise
    finally: job["CPU_seconds"]=time.monotonic()-start; atomic_json(path,job)


if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--output",type=Path,required=True)
    p.add_argument("--draws",type=int,default=6000); p.add_argument("--workers",type=int,default=4)
    p.add_argument("--budget-seconds",type=float,default=600); p.add_argument("--seed",type=int,default=2026100622)
    run(p.parse_args())
