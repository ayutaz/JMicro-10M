"""Prepare local model-blinded Chat packets or import actual human submissions.

Never publish/send the packet. No GPU jobs are started by this command.
"""
import argparse
from pathlib import Path
import secrets
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.chat_blind_review import make_packet, notes_template, restore_judgments, agreement
from jmicro.chat_review import content_review
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from review_chat_sft import load_evaluation


def phase7(path):
    path = path.resolve()
    if not path.is_relative_to(ROOT/"reports/phase7"): raise ValueError("Blind evidence must stay in reports/phase7")
    return path


def prepare(args):
    directory = phase7(args.output)
    if directory.exists(): raise FileExistsError("Keep prior packet and mapping immutable")
    refs = read_json(args.evaluations)
    assert len(refs) >= 2
    arms = {}; checkpoints = set()
    for name, ref in refs.items():
        path = phase7(Path(ref["path"]))
        assert sha256(path) == ref["sha256"]
        ev, items = load_evaluation(path, args.tokenizer)
        checkpoints.add(ev["binding"]["checkpoint_sha256"])
        arms[name] = dict(items=items, evaluation_sha256=sha256(path), checkpoint_sha256=ev["binding"]["checkpoint_sha256"])
    assert len(checkpoints) == len(arms), "Compare distinct actual learned checkpoints"
    packet, mapping = make_packet(arms, secrets.randbits(64))
    directory.mkdir(parents=True)
    write_json(directory/"reviewer_packet.json", packet)
    packet_sha = sha256(directory/"reviewer_packet.json")
    mapping.update(packet_sha256=packet_sha, evaluation_refs=refs, tokenizer_sha256=sha256(args.tokenizer),
                   created_at=now(), human_submissions=0, independent_human_evidence=False)
    write_json(directory/"private_mapping.json", mapping)
    write_json(directory/"reviewer_notes_template.json", notes_template(packet, packet_sha))
    print("Prepared model-blinded packet and separate private mapping; human submissions0")


def review(args):
    directory = phase7(args.packet_directory)
    output = phase7(args.output)
    if output.exists(): raise FileExistsError("Preserve prior imported evidence")
    packet_path = directory/"reviewer_packet.json"
    packet, mapping = read_json(packet_path), read_json(directory/"private_mapping.json")
    packet_sha = sha256(packet_path)
    assert mapping["tokenizer_sha256"] == sha256(args.tokenizer)
    submissions = [read_json(p) for p in args.notes]
    assert len(submissions) >= 2
    restored = [restore_judgments(packet, packet_sha, mapping, notes) for notes in submissions]
    assert len({n["reviewer"]["identity"].strip().casefold() for n in submissions}) == len(submissions), "Two distinct reviewers required"
    # Revalidate every actual source rather than accepting a forged or stale
    # private mapping as proof that the packet depicts the learned checkpoints.
    reports = []
    for name, ref in mapping["evaluation_refs"].items():
        path = phase7(Path(ref["path"]))
        assert sha256(path) == ref["sha256"] == mapping["arms"][name]["evaluation_sha256"]
        ev, items = load_evaluation(path, args.tokenizer)
        assert ev["binding"]["checkpoint_sha256"] == mapping["arms"][name]["checkpoint_sha256"]
        links = [r for r in mapping["samples"] if r["arm"] == name]
        public = {r["sample_id"]: r for r in packet["samples"]}
        assert {r["key"] for r in links} == set(items)
        for link in links:
            displayed, item = public[link["sample_id"]], items[link["key"]]
            assert displayed["messages"] == item["messages"] and displayed["checks"] == item["checks"] and displayed["response"] == item["response"]["text"]
        reports.append(dict(arm=name, evaluation_sha256=ref["sha256"], reviews=[
            content_review(ev, ref["sha256"], notes[name], items) for notes in restored]))
    pairs = [dict(left=submissions[i]["reviewer"]["identity"], right=submissions[j]["reviewer"]["identity"],
                  agreement=agreement(submissions[i], submissions[j])) for i in range(len(submissions)) for j in range(i+1, len(submissions))]
    write_json(output, dict(status="blind_protocol_and_human_declared_submissions_recorded_pending_final_quality",
        packet_sha256=packet_sha, private_mapping_sha256=sha256(directory/"private_mapping.json"),
        submission_sha256=[sha256(p) for p in args.notes], reviewers=[n["reviewer"] for n in submissions],
        blind_protocol_verified=True, human_identity_source="Reviewer declarations, not externally authenticated; never fabricate human submissions",
        per_arm=reports, agreement=pairs, adjudication="No automatic consensus or selection of the most favorable reviewer",
        Chat_adopted=False, requested_five_steps_complete=False, protected_test_used=False, reviewed_at=now()))
    print("Imported declared human submissions and agreement; no automatic consensus or Chat adoption")


if __name__ == "__main__":
    assert sys.version_info[:3] == (3, 12, 7)
    parser = argparse.ArgumentParser()
    parser.add_argument("--tokenizer", type=Path, default=ROOT/"artifacts/phase2/4096/tokenizer.model")
    commands = parser.add_subparsers(dest="command", required=True)
    build = commands.add_parser("prepare")
    build.add_argument("--evaluations", type=Path, required=True, help="Private named evaluation path/SHA refs JSON")
    build.add_argument("--output", type=Path, required=True)
    score = commands.add_parser("review")
    score.add_argument("--packet-directory", type=Path, required=True)
    score.add_argument("--notes", type=Path, nargs="+", required=True)
    score.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    prepare(args) if args.command == "prepare" else review(args)
