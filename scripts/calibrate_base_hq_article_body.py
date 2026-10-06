"""Measure a single source-body extractor on the already inspected64 originals."""
from collections import Counter
import json
from pathlib import Path
import sys
import time

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from base_hq_article_body import select_article
from jmicro.experiment import ROOT,now,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/base-hq-sample-20261007')
OUT=ROOT/'reports/phase6/base_hq_article_calibration.json'
TOK_SHA='a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'


def main():
    if OUT.exists(): raise ValueError('Preserve original calibration; do not repeatedly tune it')
    start=time.monotonic()
    source=DATA/'source-sample.json'; review=ROOT/'reports/phase6/base_hq_source_content_review.json'
    r=json.loads(review.read_text())
    if r['sample_sha256']!=sha256(source) or r['summary']['full_individual_original_body_read']!=64:
        raise ValueError('Original full64 content evidence required')
    tok_path=ROOT/'artifacts/phase2/4096/tokenizer.model'
    if sha256(tok_path)!=TOK_SHA: raise ValueError('Pinned tokenizer changed')
    tok=Tokenizer(tok_path); accepted=[]; reasons=Counter(); decisions=[]
    for row in json.loads(source.read_text())['rows']:
        if time.monotonic()-start>30: raise TimeoutError('CPU30s calibration limit exhausted')
        unit,why=select_article(row['text'],tok)
        decisions.append(dict(index=row['index'],source_id=row['source_id'],original_text_sha256=row['original_text_sha256'],
            structural_candidate=unit is not None,rejected_reason=why))
        if unit is None: reasons[why]+=1; continue
        accepted.append(dict(index=row['index'],source_id=row['source_id'],source_file=row['source_file'],
            source_row=row['source_row'],URL_family_sha256=row['URL_family_sha256'],split=row['split'],
            original_document_sha256=row['original_text_sha256'],**unit))
    target=DATA/'article-calibration.json'; atomic_json(target,dict(rows=accepted))
    durations=time.monotonic()-start
    if durations>30: raise TimeoutError('CPU30s calibration limit exhausted')
    report=dict(status='single_contiguous_article_extractor_calibrated_not_accepted',created_at=now(),
        original_sample_sha256=sha256(source),original_content_review_sha256=sha256(review),
        extractor_sha256=sha256(ROOT/'scripts/base_hq_article_body.py'),tokenizer_sha256=TOK_SHA,
        calibration=dict(path=str(target),sha256=sha256(target)),original_parents=64,
        structural_candidates=len(accepted),distinct_source_families=len({x['URL_family_sha256'] for x in accepted}),
        retained_body_tokens=sum(x['native_body_tokens'] for x in accepted),
        retained_original_UTF8_bytes=sum(x['original_body_UTF8_bytes'] for x in accepted),
        trimmed_candidates=sum(x['removed_prefix_chars']>0 or x['removed_tail_chars']>0 for x in accepted),
        rejection_reasons=dict(reasons),decisions=decisions,
        all_selected_spans_exactly_equal_original_UTF8=True,source_documents_split_into_sentences=False,
        original_punctuation_not_added_or_rewritten=True,CPU_seconds=durations,CPU_limit_seconds=30,
        remote_bytes=0,new_prepared_training_tokens=0,scientific_teacher_tokens=0,GPU_seconds=0,
        source_accepted=False,Base_complete=False,Chat_started=False,quantization_started=False,
        next_action='Freeze this single extractor and a bounded fixed unseen-source acceptance. Reuse selected-column ranges, original family/old-index exclusions, plus extracted-body exclusions. Compare every selected raw parent and extracted contiguous body; at least54/64 grammatical/coherent complete usable original article bodies under the existing source-pilot ceiling, otherwise stop this extractor without reroll/tuning. Record all source and byte/token/GPU budgets before any large prep or learning.',
        limitations='Developed after reading the64 raw calibration sources; output count is a structural supply observation, not a held-out pass or global unique-corpus estimate. Formal metadata/genre validity is separate from target-style. Sentence-end detection cannot certify semantic context or truth. Old-family near overlap and fixed eval suite exclusion remain pending. No source/beta/epoch/LR/checkpoint rescue of failed small CE/DPO/news runs.')
    atomic_json(OUT,report)
    print({k:report[k] for k in ('structural_candidates','distinct_source_families','retained_body_tokens','rejection_reasons','CPU_seconds')})


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
