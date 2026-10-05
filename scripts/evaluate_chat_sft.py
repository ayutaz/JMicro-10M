"""Fixed dev Chat evaluation, including raw role control and own-history rollouts."""
import argparse
import gc
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG",":4096:8")
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.chat_evaluation import generate_reply,rollout_dialogue,summarize_chat
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock,implementation_hashes,rng_state,seed_all
from phase6_performance import identity,alive,finite_state
from run_eos_short_pilot import equal_state

SOURCES = ("scripts/evaluate_chat_sft.py","src/jmicro/chat_evaluation.py",
    "src/jmicro/tokenizer.py","src/jmicro/japanese_evaluation.py","scripts/phase6_performance.py","scripts/run_eos_short_pilot.py")


def load_dev(tokenizer,context):
    with (ROOT/"eval/chat.jsonl").open() as stream:
        # Protected test rows are not selected as scored/preflight cases.
        cases = [r for r in (json.loads(s) for s in stream) if r["split"] == "dev"]
    assert len(cases) == 80 and len({r["id"] for r in cases}) == 80 and len({r["family_id"] for r in cases}) == 80
    for case in cases:
        ids,removed = tokenizer.chat_prompt(case["messages"],context-64)
        assert removed == 0,"Fixed dev history must fit intact; do not silently weaken the context task"
    contexts = [r for r in cases if 2 <= sum(m["role"] == "user" for m in r["messages"]) <= 4]
    assert len(contexts) == 24 and {sum(m["role"] == "user" for m in r["messages"]) for r in contexts} == {2,3,4}
    return cases,contexts


def run(args):
    checkpoint = args.checkpoint.resolve();directory = (ROOT/args.output).resolve()
    if not directory.is_relative_to(ROOT/"reports/phase7"): raise ValueError("Chat outputs must stay under project reports/phase7")
    state = torch.load(checkpoint,map_location="cpu",weights_only=False)
    assert state["implementation_sha256"] == implementation_hashes() and state["update"] > 0 and finite_state(state)
    assert state["lineage"]["kind"] == "assistant-sft-fresh-optimizer" and state["spec"]["assistant_training"]
    tokenizer = Tokenizer(args.tokenizer)
    assert tokenizer.vocab_size == state["model_config"]["vocab_size"]
    cases,contexts = load_dev(tokenizer,state["model_config"]["max_position_embeddings"])
    binding = dict(checkpoint=str(checkpoint),checkpoint_sha256=sha256(checkpoint),tokenizer_sha256=sha256(args.tokenizer),
        suite_sha256=sha256(ROOT/"eval/chat.jsonl"),max_new_tokens=64,dtype="bf16",backend="math",GPU_budget_seconds=args.gpu_budget_seconds,
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},implementation=implementation_hashes(),
        decoding="greedy",evaluation_seed=42,model_context=state["model_config"]["max_position_embeddings"],scored_split="dev",protected_test_used=False,
        protocol="provided80 suppressed + provided80 unsuppressed role control +24 own-history2-4turn dialogues")
    directory.mkdir(parents=True,exist_ok=True);job_path = directory/"job.json"
    previous = read_json(job_path) if job_path.exists() else {}
    if previous:
        assert previous["binding"] == binding and not alive(previous)
        if previous["status"] == "complete": print("Completed Chat evaluation retained");return
    started = None;prior = previous.get("GPU_elapsed_seconds",0.);stopped = [False]
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True))
    signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    job = dict(status="starting",**identity(),binding=binding,started_at=previous.get("started_at",now()),GPU_elapsed_seconds=prior)
    progress_path = directory/"progress.json"
    saved = read_json(progress_path) if progress_path.exists() else dict(binding=binding,provided={},rollouts={})
    assert saved["binding"] == binding
    def check():
        if stopped[0]: raise InterruptedError("Chat evaluation stopped; completed cases retained")
        if started is not None and prior+time.monotonic()-started > args.gpu_budget_seconds: raise TimeoutError("Cumulative fixed Chat evaluation budget exhausted")
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        atomic_json(job_path,job)
    try:
        heartbeat("setup");torch.set_num_threads(2);seed_all(42);torch.use_deterministic_algorithms(True)
        for source in SOURCES:
            target = directory/"source"/source;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists(): assert target.read_bytes() == (ROOT/source).read_bytes()
            else: shutil.copyfile(ROOT/source,target)
        atomic_json(directory/"recipe.json",binding)
        with gpu_lock("cuda"),sdpa_kernel(SDPBackend.MATH):
            started = time.monotonic()
            model = JMicroModel(state["model_config"]).cuda().eval();model.load_state_dict(state["model"],strict=True);del state
            before = rng_state()
            for suppressed in (True,False):
                mode = "suppressed" if suppressed else "unsuppressed"
                for index,case in enumerate(cases):
                    key = mode+"-"+case["id"]
                    if key in saved["provided"]: continue
                    heartbeat("provided-"+mode,completed=index,total=80)
                    row = generate_reply(model,tokenizer,case["messages"],"cuda","bf16",64,suppressed,check)
                    row.update(id=case["id"],family_id=case["family_id"],category=case["category"],split="dev",checks=case["checks"],
                        messages=case["messages"],history_mode="provided_assistant_history")
                    assert row["full_history_retained"]
                    saved["provided"][key] = row;atomic_json(progress_path,saved)
            for index,case in enumerate(contexts):
                if case["id"] in saved["rollouts"]: continue
                heartbeat("own-history",completed=index,total=24)
                row = rollout_dialogue(model,tokenizer,case,"cuda","bf16",64,check)
                assert row["full_history_retained"],"Generated-history task exceeded context; preserve error, do not drop a condition"
                saved["rollouts"][case["id"]] = row;atomic_json(progress_path,saved)
            assert equal_state(before,rng_state()),"Chat inference consumed training RNG"
            assert len(saved["provided"]) == 160 and len(saved["rollouts"]) == 24
            primary = [saved["provided"]["suppressed-"+c["id"]] for c in cases]
            control = [saved["provided"]["unsuppressed-"+c["id"]] for c in cases]
            final_turns = [saved["rollouts"][c["id"]]["replies"][-1] for c in contexts]
            all_turns = [r for c in contexts for r in saved["rollouts"][c["id"]]["replies"]]
            result = dict(status="mechanical_evaluation_complete_pending_all_content_judgments",binding=binding,
                primary=summarize_chat(primary),role_control=summarize_chat(control),own_history_final24=summarize_chat(final_turns),
                own_history_all_turns=summarize_chat(all_turns),context_scoring_unit="24 dialogue families; final context score plus prior failures, not independent59 turns",
                outputs=saved["provided"],rollouts=saved["rollouts"],evaluation_RNG_isolated=True,protected_test_used=False,
                grammar_relevance_context_not_scored=True,Chat_adopted=False,requested_five_steps_complete=False,completed_at=now())
            atomic_json(directory/"result.json",result);heartbeat("complete");job.update(status="complete",completed_at=now())
            del model;gc.collect();torch.cuda.empty_cache()
    except BaseException as error: job.update(status="failed",error=repr(error));raise
    finally:
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        atomic_json(job_path,job)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3,12,7)
    parser = argparse.ArgumentParser();parser.add_argument("--checkpoint",type=Path,required=True);parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--tokenizer",type=Path,default=ROOT/"artifacts/phase2/4096/tokenizer.model")
    parser.add_argument("--gpu-budget-seconds",type=float,default=600.);args = parser.parse_args()
    assert args.gpu_budget_seconds > 0;run(args)
