"""Inspect saved native continuations; no inference, rescoring, or learning."""
import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.sequence_unlikelihood import repeated_ngram_mask
from jmicro.tokenizer import Tokenizer
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes


def inspect(generation, notes, output):
    raw = read_json(generation)
    rows = raw["outputs"]
    validate_rows(rows, Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model"))
    scores = validate_notes(rows, read_json(notes), sha256(generation))
    masks = repeated_ngram_mask([r["generated_ids"] for r in rows])
    details = [dict(id=row["id"], generated_tokens=len(row["generated_ids"]),
                    repeated_4gram_candidate_tokens=sum(mask),
                    first_candidate_position=next((i for i,v in enumerate(mask) if v), None),
                    stop_reason=row["stop_reason"], coherence=scores[row["id"]]["coherence"],
                    completion=scores[row["id"]]["completion"])
               for row,mask in zip(rows,masks,strict=True)]
    marked = [r for r in details if r["repeated_4gram_candidate_tokens"]]
    unmarked = [r for r in details if not r["repeated_4gram_candidate_tokens"]]
    report = dict(status="saved_raw_repetition_candidates_inspected_no_model_update",
                  generation=dict(path=str(generation), sha256=sha256(generation)),
                  notes=dict(path=str(notes),sha256=sha256(notes)),
                  source_sha256=sha256(ROOT/"src/jmicro/sequence_unlikelihood.py"),
                  rows=len(rows), candidate_rows=len(marked),
                  candidate_tokens=sum(r["repeated_4gram_candidate_tokens"] for r in details),
                  candidate_rows_with_coherence2=sum(r["coherence"]==2 for r in marked),
                  noncandidate_rows_with_coherence_below2=sum(r["coherence"]<2 for r in unmarked),
                  candidate_rows_with_appropriate_completion=sum(r["completion"] for r in marked),
                  interpretation="Generated 4-gram candidates are not a new failure threshold; legitimate repeats can exist. Noncandidate incoherence cannot be assumed fixed by repetition loss.",
                  science_teacher_tokens=0,GPU_training_updates=0,new_inference=False,
                  protected_test_used=False,Base_adopted=False,details=details,created_at=now())
    write_json(output,report)
    print({k:report[k] for k in ("rows","candidate_rows","candidate_tokens",
          "candidate_rows_with_coherence2","noncandidate_rows_with_coherence_below2")})


if __name__=="__main__":
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser()
    for key in ("generation","notes","output"):p.add_argument("--"+key,type=Path,required=True)
    args=p.parse_args()
    if args.output.resolve() in (args.generation.resolve(),args.notes.resolve()):
        p.error("Output must not overwrite raw generation or original notes")
    inspect(args.generation,args.notes,args.output)
