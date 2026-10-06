"""Bounded immutable2048 Base curriculum and128 disjoint transfer families."""
import json
from pathlib import Path
import sys
import time
from collections import Counter

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import alive, identity
from prepare_condition_positive_teachers import outcome_token_mask
from condition_transfer_curriculum import SEED, KIND, CATEGORIES, generate, validate_split, render, CurriculumTrainView

OUT = Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-transfer-curriculum-20261006-v2')
RUN = ROOT/'reports/phase6/condition-transfer-curriculum-20261006-v2'
PROPOSAL = ROOT/'reports/phase6/condition_source_transfer_proposal.json'
SOURCES = ('scripts/condition_transfer_curriculum.py', 'scripts/prepare_condition_transfer_curriculum.py',
           'scripts/prepare_condition_transfer_curriculum.ps1','scripts/review_condition_transfer_curriculum.py')


def validate_single_repair(groups,rows):
    prior_data=Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-transfer-curriculum-20261006')
    reviewed=read_json(prior_data/'content-review.json');old=read_json(prior_data/'train-source.json')
    if (reviewed['training_pool_accepted'] or reviewed['unresolved_grammar_documents']!=2
            or not reviewed['all64_read'] or reviewed['notes_sha256']!=sha256(prior_data/'content-notes.json')):
        raise ValueError('Preserved actual64 specific grammar failure required')
    if len(old['rows'])!=len(rows):raise ValueError('Repair cannot change document selection')
    changed=[]
    for before,after in zip(old['rows'],rows,strict=True):
        if any(before[k]!=after[k] for k in before if k not in ('text','text_sha256','prefix','cut','end')):
            raise ValueError('Repair changed local states/labels/IDs/order')
        if after['template_id']=='negation-2':
            if before['text'].replace('その内容は、','その記録によると、')!=after['text']:
                raise ValueError('Only observed topic-connection repair allowed')
            changed.append(after['id'])
        elif before!=after:raise ValueError('Repair changed unrelated source')
    old_families=old['families']+read_json(prior_data/'transfer-probes.json')['families']
    new_families=[f for group in groups.values() for f in group]
    if len(old_families)!=len(new_families):raise ValueError('Repair changed probe selection')
    for before,after in zip(old_families,new_families,strict=True):
        if any(before[k]!=after[k] for k in after if k!='branches'):
            raise ValueError('Repair rerolled family facts/selection')
        for old_b,new_b in zip(before['branches'],after['branches'],strict=True):
            if any(old_b[k]!=new_b[k] for k in old_b if k!='prefix'):
                raise ValueError('Repair changed probe truth/choices')
            wanted=old_b['prefix'].replace('その内容は、','その記録によると、') if after['template_id']=='negation-2' else old_b['prefix']
            if wanted!=new_b['prefix']:raise ValueError('Unexpected branch correction')
    return dict(prior_manifest_sha256=sha256(prior_data/'manifest.json'),prior_review_sha256=sha256(prior_data/'content-review.json'),
        changed_train_documents=len(changed),changed_ids=changed,original_facts_labels_ids_order_preserved=True,
        all128_probe_facts_choices_preserved=True,seed_unchanged=True,fixed_first64_ids_unchanged=True,
        correction='negation-2 only: その内容は、 -> その記録によると、. Specific observed grammatical topic connection; no answer, fact or selection changes.')


def references():
    p = read_json(PROPOSAL)
    if (p['curriculum']['train_documents'] != 2048 or p['curriculum']['CPU_preparation_limit_seconds'] != 240
            or p['Base_adopted'] or p['Chat_started'] or p['quantization_started'] or p['protected_test_used']):
        raise ValueError('Immutable Base-only curriculum proposal required')
    for ref in (p['evidence'], p['pair_evidence'], p['natural_control']['result'], p['natural_control']['review'], p['natural_control']['generation_notes']):
        if sha256(Path(ref['path'])) != ref['sha256']:
            raise ValueError('Prior actual100M evidence changed')
    old_run = ROOT/'reports/phase6/condition-source-learning-100m-20261006'
    job = read_json(old_run/'job.json')
    if job['status'] != 'complete' or alive(job):
        raise ValueError('Previous actual science must be terminal')
    base = read_json(ROOT/'configs/phase6/textbook_quantity_comparison.json')
    tokenizer_path = ROOT/base['tokenizer']
    if sha256(tokenizer_path) != base['tokenizer_sha256']:
        raise ValueError('Pinned Tokenizer changed')
    return p, base, old_run


def check_dev_leakage(rows, groups, old_run):
    # Reuse ONLY previously scored dev rows; do not open or score protected test.
    old = read_json(old_run/'compare-result.json')['evaluations']['large2048']
    prefixes = [r['prefix'] for r in old['generation']['outputs']]
    semantics = read_json(old_run/'evaluation/large2048/evaluation/semantics.json')['rows']
    if len(prefixes) != 80 or len(semantics) != 192 or any(r['split'] != 'dev' for r in semantics):
        raise ValueError('Previously scored fixeddev only required')
    prefixes += [r['context'] for r in semantics]
    texts = [r['text'] for r in rows]
    texts += [b['prefix']+b['choices'][b['label']] for g in ('lexical_holdout','structural_holdout') for f in groups[g] for b in f['branches']]
    if any(prefix in text for prefix in prefixes for text in texts):
        raise ValueError('Literal originaldev context copied into local material')
    return dict(previous_dev80_and192_literal_contexts_absent=True, protected_test_opened=False,
                templates_independently_authored=True, semantic_similarity_or_global_overlap_certified=False,
                limitations='Literal bounded check is not semantic/template equivalence certification. Six broad abilities follow known dev failures; selection is exploratory, not untouched evaluation.')


def encode_probes(groups, tokenizer):
    families = []; cases = []
    for split in ('lexical_holdout','structural_holdout'):
        for family in groups[split]:
            index = len(families); families.append(dict(index=index, **family))
            for branch in family['branches']:
                prefix_ids = tokenizer.encode(branch['prefix'])
                for candidate, choice in enumerate(branch['choices']):
                    target = tokenizer.encode(choice); ids = [2,*prefix_ids,*target]
                    if len(ids)-1 > 1024 or tokenizer.decode_bytes(ids[1:]) != (branch['prefix']+choice).encode():
                        raise ValueError('Complete probe bytes/context required')
                    cases.append(dict(index=len(cases),family=index,id=family['id'],split=split,
                        category=family['category'],template_id=family['template_id'],branch=branch['label'],
                        label=branch['label'],candidate=candidate,prefix=branch['prefix'],outcome=choice,
                        ids=ids,context_tokens=len(prefix_ids)+1,target_ids=target,target_bytes=len(choice.encode()),
                        joint_tokenization_equal=tokenizer.encode(branch['prefix']+choice)==ids[1:]))
    if len(families) != 128 or len(cases) != 512:
        raise ValueError('All128 opposed families/512 requests required')
    return dict(families=families,cases=cases,primary='sum_log_likelihood',secondary=['mean_token_log_likelihood','mean_byte_log_likelihood'],
        target_policy='Same separately encoded complete candidate bytes/IDs across paired contexts. Body only, no inventedEOS.',
        label_scope='Logical consequences of declared local states. Device settings are definitions, not external fact claims. These source-transfer probes are separate from originaldev/test.')


def main():
    started = time.monotonic(); p, base, old_run = references()
    job_path = RUN/'job.json'
    if OUT.exists() or job_path.exists():
        raise ValueError('Preserve prepared or partial fixed curriculum; do not reroll or overwrite')
    RUN.mkdir(parents=True,exist_ok=True)
    job = dict(status='preparing', **identity(), started_at=now(), proposal_sha256=sha256(PROPOSAL),
        CPU_limit_seconds=240, scientific_teacher_tokens=0, actual_GPU_seconds=0,protected_test_used=False,
        restart_command='Inspect existing fixed or partial preparation; no automatic reroll. uv run --frozen --extra hub --extra data --extra ml --extra export scripts/prepare_condition_transfer_curriculum.py')
    atomic_json(job_path,job)
    try:
        groups,rows = generate(); checks = validate_split(groups,rows)
        repair=validate_single_repair(groups,rows)
        leakage = check_dev_leakage(rows,groups,old_run)
        tokenizer = Tokenizer(ROOT/base['tokenizer'])
        tokens=[]; masks=[]; offsets=[]; lengths=[]; metadata=[]; body_tokens=body_bytes=0
        for row in rows:
            if time.monotonic()-started > 240:
                raise TimeoutError('CPU240s curriculum preparation exhausted')
            ids=tokenizer.encode(row['text'])
            if tokenizer.decode_bytes(ids) != row['text'].encode() or len(ids)+1>1024:
                raise ValueError('Complete native4k body encoding required')
            mask=outcome_token_mask(row['text'],ids,tokenizer,[row])
            offsets.append(len(tokens));lengths.append(len(ids)+2);tokens.extend([2,*ids,3]);masks.extend(mask.tolist())
            body_tokens+=len(ids);body_bytes+=len(row['text'].encode())
            metadata.append(dict(id=row['id'],family=row['family'],category=row['category'],template_id=row['template_id'],
                text_sha256=row['text_sha256'],body_tokens=len(ids),body_bytes=len(row['text'].encode()),outcome_focus_enabled=True))
        probes=encode_probes(groups,tokenizer)
        pilot=dict(rows=rows[:64],sampling='Fixed first64 round-robin category/structure train documents; both branches kept; no favorable reroll.',
            all24_train_structures_covered=len({r['template_id'] for r in rows[:64]})==24,
            generated_source=True,source_families_independent=False,protected_test_used=False)
        if not pilot['all24_train_structures_covered']:
            raise ValueError('Fixed first64 must cover all24 structures')
        OUT.mkdir(parents=True)
        atomic_json(RUN/'single-repair.json',repair)
        for name,value in (('train-source.json',dict(rows=rows,families=groups['train'])),('transfer-probes.json',probes),('content-pilot.json',pilot)):
            atomic_json(OUT/name,value);atomic_json(RUN/name,value)
        arrays=dict(tokens=np.asarray(tokens,dtype='<u2'),focus=np.asarray(masks,dtype=np.uint8),
            offsets=np.asarray(offsets,dtype='<i8'),lengths=np.asarray(lengths,dtype='<i4'))
        np.savez(OUT/'train.npz',**arrays)
        m=dict(kind=KIND,source='local_programmatic_Japanese',created_at=now(),seed=SEED,documents=2048,
            train_families=1024,template_count=24,category_counts=dict(Counter(r['category'] for r in rows)),
            template_counts=dict(Counter(r['template_id'] for r in rows)),unique_normalized_bodies=2048,
            generated_body_tokens=body_tokens,generated_body_bytes=body_bytes,serialized_tokens=len(tokens),
            full_CE_targets=body_tokens+2048,EOS_targets=2048,outcome_focus_body_targets=int(arrays['focus'].sum()),
            metadata=metadata,arrays_sha256=sha256(OUT/'train.npz'),tokenizer_sha256=base['tokenizer_sha256'],
            source_sha256={s:sha256(ROOT/s) for s in SOURCES},train_source_sha256=sha256(OUT/'train-source.json'),
            probe_sha256=sha256(OUT/'transfer-probes.json'),pilot_sha256=sha256(OUT/'content-pilot.json'),
            generation_draws=sum(f['generation_attempt'] for g in groups.values() for f in g),
            local_exact_duplicate_draws_rejected=sum(f['generation_attempt']-1 for g in groups.values() for f in g),
            actual_checks=checks,leakage=leakage,newly_prepared_original_corpus_tokens=0,
            single_repair=repair,
            new_local_serialized_tokens=len(tokens),science_teacher_tokens=0,actual_GPU_seconds=0,protected_test_used=False,
            loss_policy='Full body plusEOS CE, outcome weight1. Mask annotates positive continuation spans only; no negative learning, no roles, no synthetic QA formatting.',
            limitations='24 hand-authored structures share programmatic rules;2048 documents are not2048 independent semantic domains.128 generator probes also share program logic; not independent human/real-world generalization or Base quality proof. Length/EOS/lexical distribution differs from natural2048.',
            training_pool_accepted=False)
        atomic_json(OUT/'manifest.json',m);atomic_json(RUN/'manifest.json',m)
        view=CurriculumTrainView(OUT,sha256(OUT/'manifest.json'),require_accepted=False)
        if len(view.lengths)!=2048:
            raise ValueError('Actual generated train arrays not loaded')
        elapsed=time.monotonic()-started
        if elapsed>240:raise TimeoutError('CPU240s curriculum preparation exhausted')
        job.update(status='complete_pending_fixed64_content',completed_at=now(),CPU_seconds=elapsed,
            data_path=str(OUT),manifest_sha256=sha256(OUT/'manifest.json'),checks=checks)
        atomic_json(job_path,job)
        report=dict(status=job['status'],created_at=now(),job=job,data_path=str(OUT),manifest_sha256=job['manifest_sha256'],
            documents=2048,train_families=1024,train_templates=24,generated_body_tokens=body_tokens,
            generated_body_bytes=body_bytes,serialized_tokens=len(tokens),source_transfer_families=128,
            source_transfer_requests_per_checkpoint=512,CPU_seconds=elapsed,scientific_teacher_tokens=0,actual_GPU_seconds=0,
            protected_test_used=False,Base_adopted=False,Chat_started=False,quantization_started=False,
            next_action='Read fixed64 full texts individually and save raw-bound content acceptance before GPU; then implement one matched100M curriculum replacement versus preserved natural2048 control, measured CUDA resume/timing/budget<=900s, original gates unchanged.')
        atomic_json(ROOT/'reports/phase6/condition_source_transfer_v2_preparation.json',report)
        print(json.dumps(report,ensure_ascii=False),flush=True)
    except BaseException as error:
        job.update(status='failed_preserve_fixed_or_partial',error=repr(error),CPU_seconds=time.monotonic()-started,ended_at=now())
        atomic_json(job_path,job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
