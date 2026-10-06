"""Bounded train-distribution/span inspection of the completed Base comparison.

No model forward pass, optimizer, test records, global index parse or data build.
"""
import json
from pathlib import Path
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
import torch
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from cached_three_source_index import CachedThreeSourceIndex
from condition_positive_trainer import PositiveStream
from condition_transfer_curriculum import CurriculumTrainView
from condition_relation_language import RelationLanguageTrainView
from story_weight_trainer import GenreStream
from phase6_performance import identity, alive
import run_mature_base_condition_comparison as study

PROPOSAL = ROOT / 'reports/phase6/mature_base_distribution_diagnostic_proposal.json'
RUN = ROOT / 'reports/phase6/mature-base-distribution-diagnostic-20261006'
SEED, CONTEXT, WINDOW, LIMIT = 2026100631, 1024, 24, 30


def target_counts(targets, byte_lengths):
    y = np.asarray(targets)
    if np.any((y < 8) & (y != -100) & (y != 3)) or np.any(y >= len(byte_lengths)):
        raise ValueError('Expected body/EOS/BOS-masked train targets')
    body = y[y >= 8]
    return dict(teachers=int(np.count_nonzero(y != -100)), EOS=int(np.count_nonzero(y == 3)),
        masked_BOS=int(np.count_nonzero(y == -100)), body_tokens=int(len(body)),
        body_bytes=int(byte_lengths[body].sum()))


def sample_summary(rows, kind, source, check):
    total = dict.fromkeys(('teachers','EOS','masked_BOS','body_tokens','body_bytes'), 0)
    gaps = []
    for row in rows:
        check()
        for key in total: total[key] += row[key]
        gaps.extend(row['complete_between_EOS_gaps'])
    if not total['teachers']: raise ValueError('Nonempty train sample required')
    return dict(sampling=kind, source=source, blocks=len(rows), physical_inputs=len(rows)*CONTEXT,
        **total, EOS_fraction_of_teachers=total['EOS']/total['teachers'],
        sampled_inputs_per_EOS=(len(rows)*CONTEXT/total['EOS'] if total['EOS'] else None),
        between_EOS_gap_quantiles=(np.quantile(gaps,[0,.25,.5,.75,1]).tolist() if gaps else None),
        between_EOS_gap_count=len(gaps),
        limitation='EOS gaps wholly within sampled blocks only; long documents are censored. These are sampled teacher/byte statistics, not whole-corpus unique volume or an unbiased document-length estimate.')


def row_counts(y, byte_lengths, **position):
    ends = np.flatnonzero(y == 3)
    return dict(**position, **target_counts(y,byte_lengths),
        complete_between_EOS_gaps=np.diff(ends).tolist())


def span_index(view, check):
    index = {}
    for document, (offset,length) in enumerate(zip(view.offsets,view.lengths,strict=True)):
        check()
        body = tuple(map(int,view.tokens[int(offset)+1:int(offset+length)-1]))
        if any(t < 8 for t in body): raise ValueError('Only whole document bodies in span dictionary')
        for start in range(len(body)-WINDOW+1):
            index.setdefault(body[start:start+WINDOW],[]).append((document,start))
    return index


def matches(ids, view, index, check):
    tokens = tuple(map(int,ids)); found = []; best = None
    for position in range(len(tokens)-WINDOW+1):
        check(); key = tokens[position:position+WINDOW]
        if any(t < 8 for t in key): continue
        references = index.get(key,())
        if references: found.append(position)
        for document, offset in references:
            begin = int(view.offsets[document])+1
            end = int(view.offsets[document]+view.lengths[document])-1
            length = WINDOW
            while (position+length < len(tokens) and begin+offset+length < end
                    and tokens[position+length] >= 8 and tokens[position+length] == int(view.tokens[begin+offset+length])):
                length += 1
            if best is None or length > best['tokens']:
                best = dict(generated_offset=position,source_document_index=document,
                    source_body_offset=offset,tokens=length)
    return dict(matched_windows=len(found), matched_generated_offsets=found, longest_exact_body_span=best)


def main():
    started = time.monotonic(); torch.set_num_threads(2)
    p = read_json(PROPOSAL)
    if (p['CPU_limit_seconds'] != LIMIT or p['GPU_limit_seconds'] or p['new_learning_teacher_tokens']
            or p['Base_adopted'] or p['Chat_started'] or p['quantization_started'] or p['protected_test_used']):
        raise ValueError('Bounded CPU-only Base diagnostic required')
    for key in ('review','pair_evidence'): study.check_reference(p[key])
    job_path = RUN / 'job.json'
    old = read_json(job_path) if job_path.exists() else {}
    if old.get('status') == 'complete': print('Completed diagnostic retained'); return
    if old and alive(old): raise ValueError('Existing CPU diagnostic live')
    job = dict(status='running', **identity(), started_at=now(), proposal_sha256=sha256(PROPOSAL),
        actual_GPU_seconds=0, scientific_teacher_tokens=0)
    def check():
        if time.monotonic()-started > LIMIT: raise TimeoutError('CPU30s diagnostic exhausted; retain partial evidence')
    atomic_json(job_path,job)
    try:
        c = read_json(study.CONFIG); original = read_json(ROOT / 'configs/phase6/base_10b.json')
        previous_job = read_json(study.RUN / 'job.json'); result = read_json(study.RUN / 'compare-result.json')
        review = read_json(Path(p['review']['path']))
        if (previous_job['status'] != 'complete' or alive(previous_job)
                or result['config_sha256'] != sha256(study.CONFIG)
                or review['result_sha256'] != sha256(study.RUN / 'compare-result.json') or result['protected_test_used']):
            raise ValueError('Actual terminal reviewed comparison required')
        # Read the real parent's data identity without creating a sampler/model.
        study.check_reference(c['parent'])
        parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
        if parent['shard_manifest_sha256'] != original['shard_manifest_sha256']:
            raise ValueError('Original training manifest differs from actual parent')
        del parent; check()
        old_web = TrainView(original['shards'],original['shard_manifest_sha256'])
        study.check_reference(c['accepted_compact_index'])
        pool = TrainView(c['pool']['pool'],c['pool']['manifest_sha256']); pool.index = CachedThreeSourceIndex(pool)
        if not pool.index.cache_reused: raise ValueError('No index rebuilding allowed')
        if (old_web.manifest['tokenizer_sha256'] != pool.manifest['tokenizer_sha256']
                or not np.array_equal(old_web.byte_lengths,pool.byte_lengths)):
            raise ValueError('Common token/byte identity required')
        views = {}
        for arm,cls in (('curriculum',CurriculumTrainView),('relation',RelationLanguageTrainView)):
            record = c['positive_data'][arm]; views[arm] = cls(record['path'],record['manifest_sha256'])
        refs = dict(proposal=study.reference(PROPOSAL),config=study.reference(study.CONFIG),
            parent=c['parent'],old_training_config=study.reference(ROOT / 'configs/phase6/base_10b.json'),
            original_manifest=study.reference(old_web.directory / 'manifest.json'),
            selected_manifest=study.reference(pool.directory / 'manifest.json'),compact_index=c['accepted_compact_index'],
            result=study.reference(study.RUN / 'compare-result.json'),review=p['review'],pairs=p['pair_evidence'])
        for arm,view in views.items():
            refs[arm] = dict(manifest=study.reference(view.directory / 'manifest.json'),
                arrays=study.reference(view.directory / 'train.npz'),source=study.reference(view.directory / 'train-source.json'))
        rows, summaries = {}, {}
        total_blocks = (len(old_web.tokens)-1)//CONTEXT
        chosen = np.random.default_rng(SEED).choice(total_blocks,size=256,replace=False)
        rows['original_web'] = []
        for block in chosen:
            offset = int(block)*CONTEXT; y = np.asarray(old_web.tokens[offset+1:offset+CONTEXT+1],dtype=np.int64).copy()
            y[y==2] = -100
            rows['original_web'].append(row_counts(y,old_web.byte_lengths,block_index=int(block),token_offset=offset))
        summaries['original_web'] = sample_summary(rows['original_web'],'uniform without replacement aligned token blocks',str(old_web.directory),check)
        streams = {g:GenreStream(pool,g,SEED) for g in ('web','story','textbook')}
        streams.update({arm:PositiveStream(view,SEED) for arm,view in views.items()})
        for source,stream in streams.items():
            rows[source] = []
            for block in range(256 if source=='web' else 64):
                check(); before = stream.state_dict(); packed = stream.block(CONTEXT); y = packed[1]
                rows[source].append(row_counts(y,pool.byte_lengths,block_index=block,cursor_before=before,cursor_after=stream.state_dict()))
            summaries[source] = sample_summary(rows[source],'fresh deterministic per-document source shuffle',source,check)
        atomic_json(RUN / 'sampled-targets.json',dict(seed=SEED,context=CONTEXT,summaries=summaries,rows=rows))
        indices = {arm:span_index(view,check) for arm,view in views.items()}
        sources = {arm:read_json(view.directory / 'train-source.json')['rows'] for arm,view in views.items()}
        spans, aggregate = {}, {}
        for arm in ('parent10B',*study.ARMS):
            raw_path = study.RUN / f'evaluation/{arm}/evaluation/generation.json'
            raw = read_json(raw_path); notes_path = ROOT / f'reports/phase6/mature_base_{arm}_notes.json'
            notes = read_json(notes_path)
            if notes['generation_sha256'] != sha256(raw_path) or raw != result['evaluations'][arm]['generation']:
                raise ValueError('Actual all80 generation/notes binding differs')
            refs[arm+'_generation'] = study.reference(raw_path); refs[arm+'_notes'] = study.reference(notes_path)
            scores = {n[0]:n[1:5] for n in notes['notes']}; spans[arm] = []; aggregate[arm] = {}
            if len(raw['outputs']) != 80 or len(scores) != 80: raise ValueError('All320 actual reviewed outputs required')
            for row in raw['outputs']:
                check(); entry = dict(id=row['id'],content_scores=scores[row['id']],sources={})
                for source,view in views.items():
                    m = matches(row['generated_ids'],view,indices[source],check)
                    if m['longest_exact_body_span']:
                        document = m['longest_exact_body_span']['source_document_index']
                        m['longest_exact_body_span']['source_document_id'] = sources[source][document]['id']
                    entry['sources'][source] = m
                spans[arm].append(entry)
            for source in views:
                matched = [row for row in spans[arm] if row['sources'][source]['matched_windows']]
                aggregate[arm][source] = dict(outputs_with_24token_span=len(matched),
                    matched_ids=[row['id'] for row in matched],coherent2_with_span=sum(row['content_scores'][2]==2 for row in matched),
                    longest_tokens=max((row['sources'][source]['longest_exact_body_span']['tokens'] for row in matched),default=0))
        report = dict(status='actual_CPU_distribution_and_all320_source_span_diagnostic_complete',created_at=now(),
            **identity(),references=refs,script_sha256=sha256(Path(__file__)),sampled_summaries=summaries,
            source_span_window=WINDOW,source_span_aggregates=aggregate,source_span_rows=spans,
            sampled_targets_sha256=sha256(RUN / 'sampled-targets.json'),CPU_seconds=time.monotonic()-started,
            actual_GPU_seconds=0,scientific_teacher_tokens=0,cache_reused=True,protected_test_used=False,
            Base_adopted=False,Chat_started=False,quantization_started=False,
            limitations='Posthoc train distribution diagnostic, different sampling units, fixed small sample. EOS gaps are censored at block edges. Shared exact body spans do not prove whole-document copying, leakage or causal interference. No new forward pass or quality evaluation; existing nonblind notes reused.')
        check(); atomic_json(RUN / 'result.json',report)
        atomic_json(ROOT / 'reports/phase6/mature_base_distribution_diagnostic.json',report)
        job.update(status='complete',completed_at=now(),CPU_seconds=report['CPU_seconds'],result_sha256=sha256(RUN / 'result.json'))
        print(json.dumps(dict(CPU_seconds=report['CPU_seconds'],EOS_per_teacher={s:r['EOS_fraction_of_teachers'] for s,r in summaries.items()},span_aggregates=aggregate)))
    except BaseException as error:
        job.update(status='failed',error=repr(error)); raise
    finally: atomic_json(job_path,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
