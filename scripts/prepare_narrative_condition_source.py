"""Single finite CPU preparation of the frozen TRAIN-only narrative source."""
import json
from collections import Counter
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import identity
from narrative_condition_source import DATA, KIND, SOURCE, SEED, TOKENIZER_SHA, generate, select_pilot, encode_rows, NarrativeTrainView

RUN = ROOT / 'reports/phase6/narrative-condition-source-20261006'
PROPOSAL = ROOT / 'reports/phase6/narrative_condition_source_proposal.json'
FREEZE = ROOT / 'reports/phase6/narrative_condition_source_freeze.json'
SOURCES = ('scripts/narrative_condition_source.py', 'scripts/prepare_narrative_condition_source.py',
           'scripts/review_narrative_condition_source.py', 'tests/test_narrative_condition_source.py')


def references():
    p = read_json(PROPOSAL); freeze = read_json(FREEZE)
    if (freeze['proposal_sha256'] != sha256(PROPOSAL)
            or freeze['source_sha256'] != {s: sha256(ROOT / s) for s in SOURCES}
            or p['CPU_preparation']['seed'] != SEED or p['CPU_preparation']['ceiling_seconds'] != 60
            or p['CPU_preparation']['tokenizer_sha256'] != TOKENIZER_SHA
            or p['new_source']['data_directory'] != str(DATA) or p['new_source']['prospective_documents'] != 16384
            or sha256(ROOT / p['CPU_preparation']['tokenizer']) != TOKENIZER_SHA):
        raise ValueError('Frozen proposal/input/renderer/sampling/native Tokenizer differs')
    for ref in p['source'].values():
        if isinstance(ref, dict) and 'path' in ref and sha256(Path(ref['path'])) != ref['sha256']:
            raise ValueError('Accepted TRAIN source input hash differs')
    review = read_json(Path(p['source']['accepted_review']['path']))
    if not review['training_pool_accepted'] or review['manifest_sha256'] != p['source']['manifest']['sha256']:
        raise ValueError('Existing selected TRAIN source must be accepted')
    return p, freeze


def main():
    started = time.monotonic(); p, freeze = references()
    if DATA.exists() or (RUN / 'job.json').exists():
        raise ValueError('Preserve actual fixed/partial source; no overwrite/filter/reroll')
    RUN.mkdir(parents=True, exist_ok=True)
    job = dict(status='preparing', **identity(), started_at=now(), CPU_limit_seconds=60,
        proposal_sha256=sha256(PROPOSAL), freeze_sha256=sha256(FREEZE), source_sha256=freeze['source_sha256'],
        actual_GPU_seconds=0, scientific_teacher_tokens=0, protected_test_used=False,
        restart_command='Inspect preserved fixed/partial preparation. Do not reroll or patch renderer after actual pilot freeze.')
    atomic_json(RUN / 'job.json', job)
    try:
        control = read_json(Path(p['source']['train_source']['path']))
        rows = generate(control); pilot = select_pilot(rows)
        arrays, metadata = encode_rows(rows, Tokenizer(ROOT / p['CPU_preparation']['tokenizer']))
        if time.monotonic() - started > 60:
            raise TimeoutError('CPU60 second ceiling exhausted; preserve failure')
        DATA.mkdir(parents=True)
        for name, value in (('train-source.json', dict(rows=rows, families=control['families'])), ('content-pilot.json', pilot)):
            atomic_json(DATA / name, value)
            if name == 'content-pilot.json': atomic_json(RUN / name, value)
        np.savez(DATA / 'train.npz', **arrays)
        body = sum(r['body_tokens'] for r in metadata)
        m = dict(kind=KIND, source=SOURCE, created_at=now(), seed=SEED, documents=16384, train_families=1024,
            new_independent_semantic_families=0, surface_realizations_per_branch=8, template_count=48,
            original_source_forms=24, original_form_specific_scenes_and_roles=True,
            category_counts=dict(Counter(r['category'] for r in rows)), metadata=metadata,
            generated_body_tokens=body, generated_body_bytes=sum(r['body_bytes'] for r in metadata),
            serialized_tokens=len(arrays['tokens']), full_CE_targets=body + 16384, EOS_targets=16384,
            outcome_focus_body_targets=int(arrays['focus'].sum()),
            body_length_min=min(r['body_tokens'] for r in metadata), body_length_max=max(r['body_tokens'] for r in metadata),
            body_length_mean=body / 16384, whole_documents=True, truncations=0, reserved_body_ids=0,
            every_TRAIN_family_branch_surface_covered=True, all_whole_texts_unique=True,
            unchanged_TRAIN_facts_and_local_states=True, unchanged_train_selection_and_family_order=True,
            no_evaluation_source_read=True, new_original_corpus_tokens=0, newly_prepared_original_corpus_tokens=0,
            new_local_serialized_tokens=len(arrays['tokens']), arrays_sha256=sha256(DATA / 'train.npz'),
            train_source_sha256=sha256(DATA / 'train-source.json'), pilot_sha256=sha256(DATA / 'content-pilot.json'),
            tokenizer_sha256=TOKENIZER_SHA, source_sha256=freeze['source_sha256'], original_source=p['source'],
            proposal_sha256=sha256(PROPOSAL), freeze_sha256=sha256(FREEZE), training_pool_accepted=False,
            scientific_teacher_tokens=0, actual_GPU_seconds=0, protected_test_used=False,
            loss_policy='All body+EOS ordinary CE weight1. Focus annotation does not change supervision.',
            limitations=p['new_source']['limitations'])
        atomic_json(DATA / 'manifest.json', m); atomic_json(RUN / 'manifest.json', m)
        NarrativeTrainView(DATA, sha256(DATA / 'manifest.json'), require_accepted=False)
        elapsed = time.monotonic() - started
        if elapsed > 60: raise TimeoutError('CPU60 second ceiling exhausted; preserve failure')
        job.update(status='complete_pending_fixed64_content', completed_at=now(), CPU_seconds=elapsed,
            data_path=str(DATA), manifest_sha256=sha256(DATA / 'manifest.json'),
            documents=16384, body_tokens=body, serialized_tokens=m['serialized_tokens'])
        atomic_json(RUN / 'job.json', job)
        atomic_json(ROOT / 'reports/phase6/narrative_condition_source_preparation.json', dict(status=job['status'], job=job,
            documents=16384, body_tokens=body, body_bytes=m['generated_body_bytes'], serialized_tokens=m['serialized_tokens'],
            full_CE_targets=m['full_CE_targets'], EOS_targets=16384, actual_GPU_seconds=0, scientific_teacher_tokens=0,
            Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False, protected_test_used=False,
            next_action='Read all fixed64 individually; unchanged weak<=10 and unresolved grammar/grounding0 before any GPU.'))
        print(json.dumps(dict(status=job['status'], CPU_seconds=elapsed, documents=16384, body_tokens=body)), flush=True)
    except BaseException as error:
        job.update(status='failed_preserve_fixed_or_partial', ended_at=now(), CPU_seconds=time.monotonic() - started, error=repr(error))
        atomic_json(RUN / 'job.json', job); raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
