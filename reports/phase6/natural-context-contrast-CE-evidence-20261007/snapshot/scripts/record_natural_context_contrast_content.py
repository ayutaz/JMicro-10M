"""Record individually written observations; never generate content scores."""
import argparse
from pathlib import Path
import sys

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes
from review_natural_context_contrast import ARMS, RUN, load_policy, notes_path, raw_path, content


def record(arm, observations):
    c, _ = load_policy()
    observations = observations.resolve()
    if not observations.is_relative_to(ROOT / 'reports/phase6'):
        raise ValueError('Repository phase6 observations required')
    raw = raw_path(arm)
    rows = read_json(raw)['outputs']
    validate_rows(rows, Tokenizer(ROOT / c['tokenizer']))
    notes = []
    for line in observations.read_text(encoding='utf-8').splitlines():
        fields = line.split('\t')
        if len(fields) != 6:
            raise ValueError('One six-field individual observation per continuation required')
        notes.append([fields[0], *(int(v) for v in fields[1:5]), fields[5]])
    document = dict(created_at=now(), reviewer='Codex nonblind; all80 individually read',
        independent_human_blind=False, generation_sha256=sha256(raw), notes=notes,
        observations=dict(path=str(observations.relative_to(ROOT)), sha256=sha256(observations)),
        recorder_sha256=sha256(Path(__file__)))
    validate_notes(rows, document, sha256(raw))
    destination = notes_path(arm)
    if destination.exists():
        old = read_json(destination)
        if (old['generation_sha256'] != sha256(raw) or len(old['notes']) != 80
                or any(n[1:5] != [None] * 4 or n[5] for n in old['notes'])):
            raise ValueError('Preserve previously scored or differently bound notes')
    atomic_json(destination, document)
    ev = read_json(RUN / f'evaluation/{arm}/evaluation/result.json')
    trained = read_json(RUN / arm / 'train-result.json')
    summary, _ = content(arm, ev, trained, c, raw, destination)
    summary.update(scope='one_arm_content_only_comparison_and_final_validation_pending', arm=arm,
        individually_read=80, independent_human_blind=False, Base_complete=False,
        scientific_CE_teacher_tokens=trained['scientific_CE_teacher_tokens'])
    atomic_json(ROOT / f'reports/phase6/natural_context_contrast_{arm}_content_review.json', summary)
    print(summary)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser()
    parser.add_argument('arm', choices=ARMS)
    parser.add_argument('observations', type=Path)
    args = parser.parse_args()
    record(args.arm, args.observations)
