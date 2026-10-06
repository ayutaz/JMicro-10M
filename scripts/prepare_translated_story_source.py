"""One bounded native translation-only preparation of the predeclared source."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
from pathlib import Path
import sys
import time
import json
import hashlib

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.eos_pilot import TrainView
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import identity
from translated_story_source import KIND,REPOSITORY,REVISION,TOKENIZER_SHA,derive_index,fixed_selection,TranslatedStoryTrainView
from story_provenance_lookup import Reader,lookup

RUN=ROOT/'reports/phase6/translated-story-source-20261006'
PROPOSAL=ROOT/'reports/phase6/translated_story_source_proposal.json'
FREEZE=ROOT/'reports/phase6/translated_story_source_freeze.json'
SOURCES=('scripts/translated_story_source.py','scripts/prepare_translated_story_source.py',
         'scripts/review_translated_story_source.py','tests/test_translated_story_source.py')


def main():
    started=time.monotonic();p=read_json(PROPOSAL);freeze=read_json(FREEZE)
    if (RUN/'job.json').exists():raise ValueError('Preserve actual fixed/partial source; no reroll')
    if freeze['proposal_sha256']!=sha256(PROPOSAL) or freeze['source_sha256']!={s:sha256(ROOT/s) for s in SOURCES}:
        raise ValueError('Frozen proposal/native view/selection source differs')
    for record_ref in freeze['references'].values():
        if sha256(Path(record_ref['path']))!=record_ref['sha256']:raise ValueError('Fixed source/exclusion reference differs')
    RUN.mkdir(parents=True,exist_ok=True)
    job=dict(status='preparing',**identity(),started_at=now(),proposal_sha256=sha256(PROPOSAL),freeze_sha256=sha256(FREEZE),
        CPU_ceiling_seconds=60,GPU_seconds=0,scientific_teacher_tokens=0,protected_test_used=False,
        restart_command='Preserve fixed/partial preparation. No automatic reroll, source patch or selection changes.')
    atomic_json(RUN/'job.json',job)
    try:
        source=p['source'];begin,end=source['native_translation_serialized_interval']
        native=TrainView(source['native_pool'],source['manifest']['sha256'])
        offsets,lengths=derive_index(native.tokens,begin,end)
        if len(offsets)!=source['prospective_translation_documents'] or int(lengths.sum())!=source['serialized_tokens']:
            raise ValueError('All original selected TRAIN translations required')
        selected,excluded=fixed_selection(offsets,begin,set(freeze['excluded_native_offsets']))
        index=Path(source['native_pool'])/'train.index.jsonl';stat=index.stat()
        if [stat.st_size,stat.st_mtime_ns]!=freeze['native_index_size_and_mtime_ns']:raise ValueError('Original index identity differs')
        tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
        if sha256(tok.path)!=TOKENIZER_SHA:raise ValueError('Pinned native Tokenizer differs')
        rows=[];exclusion_sha=set(freeze['excluded_text_sha256'])
        with index.open('rb') as stream:
            reader=Reader(stream)
            for number,doc in enumerate(selected.tolist()):
                if time.monotonic()-started>60:raise TimeoutError('CPU60 second preparation ceiling exceeded')
                global_start=begin+int(offsets[doc]);length=int(lengths[doc]);original=lookup(reader,global_start,stat.st_size)
                body=native.tokens[global_start+1:global_start+length-1].tolist()
                raw=tok.decode_bytes(body);text=raw.decode('utf-8');digest=hashlib.sha256(raw).hexdigest()
                if (original['source']!='translation' or original['split']!='train' or original['source_revision']!=REVISION
                        or original['body_tokens']!=length-2 or original['text_sha256']!=digest or original['bytes']!=len(raw)
                        or digest in exclusion_sha or any(i<8 for i in body) or tok.encode(text)!=body):
                    raise ValueError('Unchanged whole original TRAIN native bytes/provenance/calibration required')
                rows.append(dict(index=number,id=f'translation-offset-{global_start}',document_index=doc,
                    native_offset=global_start,relative_offset=int(offsets[doc]),body_tokens=length-2,body_bytes=len(raw),
                    text=text,text_sha256=digest,split='train',original_metadata=original))
        # Also verify source-origin at both declared copy/append interval edges.
        with index.open('rb') as stream:
            boundary_reader=Reader(stream)
            boundaries=[lookup(boundary_reader,begin+int(offsets[doc]),stat.st_size) for doc in (0,len(offsets)-1)]
        if any(r['source']!='translation' or r['split']!='train' or r['source_revision']!=REVISION for r in boundaries):
            raise ValueError('Original contiguous translation interval endpoints differ')
        if len({r['text_sha256'] for r in rows})!=64:raise ValueError('Duplicate fixed64; preserve failure instead of reroll')
        pilot=dict(rows=rows,seed=2026100693,selection='Uniform64 fixed draws among all original translation documents excluding frozen prior content calibration offsets only; no content/length/grammar filter',
            eligible_documents=len(offsets)-excluded,excluded_calibration_documents=excluded,excluded_text_sha256=freeze['excluded_text_sha256'],
            protected_test_used=False,independent_semantic_families_not_claimed=True)
        atomic_json(RUN/'content-pilot.json',pilot)
        np.savez(RUN/'document-index.npz',offsets=offsets,lengths=lengths)
        stream_stat=(Path(source['native_pool'])/'train.bin').stat()
        manifest=dict(kind=KIND,repository=REPOSITORY,revision=REVISION,created_at=now(),
            native_pool=source['native_pool'],native_manifest_sha256=source['manifest']['sha256'],native_interval=[begin,end],
            native_stream_size_and_mtime_ns=[stream_stat.st_size,stream_stat.st_mtime_ns],
            documents=len(offsets),serialized_tokens=int(lengths.sum()),body_tokens=int(lengths.sum())-2*len(offsets),
            full_CE_targets=int(lengths.sum())-len(offsets),EOS_targets=len(offsets),outcome_focus_body_targets=0,
            body_length_min=int(lengths.min())-2,body_length_max=int(lengths.max())-2,
            arrays_sha256=sha256(RUN/'document-index.npz'),pilot_sha256=sha256(RUN/'content-pilot.json'),tokenizer_sha256=TOKENIZER_SHA,
            proposal_sha256=sha256(PROPOSAL),freeze_sha256=sha256(FREEZE),source_sha256=freeze['source_sha256'],
            all_original_selected_TRAIN_translation_records=True,source_text_modified=False,new_original_corpus_tokens=0,
            native_tokens_copied_or_reencoded=False,original_builder_stream_and_family_split_checks_reused=True,
            original_index_fully_scanned=False,index_bytes_read=reader.bytes_read+boundary_reader.bytes_read,
            whole_BOS_EOS_boundaries_and_context_checked=True,native64_exact_bytes_checked=True,source_interval_endpoints=boundaries,
            fixed64_calibration_disjoint=True,excluded_calibration_documents=excluded,
            training_pool_accepted=False,scientific_teacher_tokens=0,GPU_seconds=0,protected_test_used=False,
            loss_policy='Ordinary body+EOS CE weight1; broadcast zero focus annotation',
            limitations=p['limitations'])
        atomic_json(RUN/'manifest.json',manifest)
        TranslatedStoryTrainView(RUN,sha256(RUN/'manifest.json'),require_accepted=False)
        elapsed=time.monotonic()-started
        if elapsed>60:raise TimeoutError('CPU60 second preparation ceiling exceeded')
        job.update(status='complete_pending_fixed64_content',completed_at=now(),CPU_seconds=elapsed,
            documents=len(offsets),serialized_tokens=manifest['serialized_tokens'],manifest_sha256=sha256(RUN/'manifest.json'))
        atomic_json(RUN/'job.json',job)
        print(json.dumps(dict(status=job['status'],CPU_seconds=elapsed,documents=len(offsets),serialized_tokens=manifest['serialized_tokens'],index_bytes_read=manifest['index_bytes_read'])),flush=True)
    except BaseException as error:
        job.update(status='failed_preserve_fixed_or_partial',error=repr(error),CPU_seconds=time.monotonic()-started,ended_at=now())
        atomic_json(RUN/'job.json',job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
