"""Review all fixed Chat dev outputs. No GPU work or automatic Chat adoption."""
import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
import torch
from jmicro.chat_review import review_items, notes_template, content_review
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive, finite_state
from evaluate_chat_sft import load_dev


def load_evaluation(path, tokenizer_path):
    path = path.resolve()
    assert path.is_relative_to(ROOT/"reports/phase7") and path.name == "result.json"
    job = read_json(path.parent/"job.json")
    if job["status"] != "complete" or alive(job):
        raise ValueError("Chat evaluation must actually finish before content review")
    ev = read_json(path); binding = ev["binding"]
    assert job["binding"] == binding and 0 < job["GPU_elapsed_seconds"] <= binding["GPU_budget_seconds"]
    assert binding["tokenizer_sha256"] == sha256(tokenizer_path)
    assert binding["suite_sha256"] == sha256(ROOT/"eval/chat.jsonl")
    assert all(sha256(path.parent/"source"/p) == value for p, value in binding["source_sha256"].items())
    checkpoint = Path(binding["checkpoint"])
    assert sha256(checkpoint) == binding["checkpoint_sha256"]
    state = torch.load(checkpoint, map_location="cpu", weights_only=False)
    assert finite_state(state) and state["update"] > 0 and state["spec"]["assistant_training"]
    assert state["lineage"]["kind"] == "assistant-sft-fresh-optimizer"
    assert state["implementation_sha256"] == binding["implementation"]
    tok = Tokenizer(tokenizer_path)
    assert tok.vocab_size == state["model_config"]["vocab_size"]
    context = state["model_config"]["max_position_embeddings"]
    assert binding["model_context"] == context and binding["evaluation_seed"] == 42
    cases, _ = load_dev(tok, context)
    return ev, review_items(ev, cases, tok, context)


def run(args):
    evaluation, items = load_evaluation(args.evaluation, args.tokenizer)
    ev_sha = sha256(args.evaluation)
    if args.template:
        items_path = args.template.with_name(args.template.stem+"-items.json")
        assert args.template.resolve().is_relative_to(ROOT/"reports/phase7")
        if args.template.exists() or items_path.exists(): raise FileExistsError("Preserve existing content notes/items")
        write_json(args.template, notes_template(ev_sha, items))
        write_json(items_path, dict(
            evaluation_sha256=ev_sha, rubric=notes_template(ev_sha, items)["rubric"], items=list(items.values()),
            protected_test_used=False, content_not_scored=True))
        print("Prepared 219 unscored responses with their actual histories; no Chat adoption")
        return
    notes = read_json(args.notes)
    report = content_review(evaluation, ev_sha, notes, items)
    report.update(annotations_sha256=sha256(args.notes), checkpoint_sha256=evaluation["binding"]["checkpoint_sha256"],
                  evaluation_binding=evaluation["binding"], reviewed_at=now())
    output = args.evaluation.parent/"content_review.json"
    if output.exists() and read_json(output)["annotations_sha256"] != report["annotations_sha256"]:
        raise FileExistsError("Preserve earlier judgments; use a new evaluation directory for a changed review")
    write_json(output, report)
    print("All 219 content judgments reviewed; development screen:", report["dev_screen_passed"], "; Chat adoption remains pending")


if __name__ == "__main__":
    assert sys.version_info[:3] == (3, 12, 7)
    parser = argparse.ArgumentParser()
    parser.add_argument("--evaluation", type=Path, required=True)
    parser.add_argument("--tokenizer", type=Path, default=ROOT/"artifacts/phase2/4096/tokenizer.model")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--template", type=Path)
    mode.add_argument("--notes", type=Path)
    run(parser.parse_args())
