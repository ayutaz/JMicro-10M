"""Record bounded registry decisions and an unexecuted matched-order comparison."""
import json
from pathlib import Path
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from phase6_performance import alive


def reference(path):
    return dict(path=str(path),sha256=sha256(path))


def main():
    started=time.monotonic()
    registry=ROOT/'reports/phase6/public_prose_registry_metadata.json'
    metadata=read_json(registry)
    if len(metadata['repositories'])!=4 or metadata['bulk_source_bytes_downloaded'] or metadata['GPU_seconds']:
        raise ValueError('Actual four-candidate metadata-only audit required')
    decisions=[
      dict(repository='kai271/TinyStories-Japanese',decision='not_selected_source_volume_not_supported',
           reason='Card reports roughly3000 stories; separate public train file is only2,443,366bytes. No plausible10M student source supply under unchanged whole-document body cap1022; no official validation used and no raw story downloaded.',upstream_teacher='GPT-4o-mini per card'),
      dict(repository='aixsatoshi/cosmopedia-japanese-20k',decision='not_selected_missing_translation_license_provenance',
           reason='Pinned27byte README only declares languages, no license, translator model, family/split or curation. Japanese translations appear alongside English; upstream Cosmopedia licensing does not establish this translated derivative license. No credentials required and no bulk recovery.',upstream_teacher='Not stated in this derivative card'),
      dict(repository='zait-ai/OpenJA',decision='not_selected_domain_does_not_match_short_narrative_hypothesis',
           reason='Card explicitly describes narrow parliamentary speech from Kokkai,3,244,877records and679,496,535 Qwen3.5-9B tokens. Those are not student tokens or accepted standalone everyday narratives. CC-BY4.0 compilation, no synthetic teacher; no raw parquet downloaded.',upstream_teacher=None),
      dict(repository='izumi-lab/wikipedia-ja-20230720',decision='not_selected_same_Wikipedia_provenance_as_prior_trials',
           reason='Different2023 snapshot of the same Japanese Wikipedia source class already tried as wikimedia/wikipedia. Not proven byte-duplicate, but no materially new simple prose/source hypothesis; no alternate snapshot/filter sweep.',upstream_teacher=None)]
    if {r['repository'] for r in decisions}!={r['repository'] for r in metadata['repositories']}:
        raise ValueError('Every pinned candidate must have a decision')
    registry_review=ROOT/'reports/phase6/public_prose_registry_review.json'
    if registry_review.exists():raise ValueError('Preserve completed registry review')
    write_json(registry_review,dict(status='four_pinned_candidates_reviewed_none_selected_for_this_source_pilot',
        created_at=now(),metadata=reference(registry),decisions=decisions,selected_repository=None,
        scope='Bounded four-candidate audit, not proof no other Japanese corpus exists. Cards/size are indirect supply evidence, no sampled quality judgment or tokenizer counts.',
        GPU_seconds=0,student_scientific_teacher_tokens=0,Chat_started=False,quantization_started=False,Base_complete=False))
    historical=ROOT/'reports/phase6/historical-parent-condition-comparison-v3-20261006'
    job=read_json(historical/'job.json');result=read_json(historical/'compare-result.json')
    review_path=ROOT/'reports/phase6/historical_parent_condition_comparison_v3_review.json';review=read_json(review_path)
    old=read_json(ROOT/'reports/phase6/historical_parent_condition_comparison_v3_proposal.json')
    if (job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(historical/'compare-result.json')
            or result['checkpoints']['historical_parent']['source_teachers']!=old['quotas']):
        raise ValueError('Actual terminal cached100M matched teacher control required')
    configs=[]
    for path in sorted((ROOT/'configs/phase6').glob('*.json')):
        c=read_json(path)
        if any('source_order' in str(k) for k in c):
            configs.append(dict(path=str(path.relative_to(ROOT)),sha256=sha256(path),keys=[k for k in c if 'source_order' in k]))
    curriculum=read_json(ROOT/'configs/phase6/curriculum_strategy.json')
    prior_curriculum=read_json(ROOT/'reports/phase6/curriculum_strategy_review.json')
    sources=('scripts/source_order_condition_trainer.py','tests/test_source_order_condition.py')
    proposal=dict(status='defined_same_teacher_source_order_comparison_not_GPU_started',created_at=now(),
        question='Does presenting long Web before complete short prose, instead of interleaving the same teacher streams, change free Japanese generation and Web retention at matched100M teachers?',
        hypothesis='Historical inherited mixed100M meets the Web guard but coherence4/80 and repetition31/80 fail. Small isolated train-fit can improve while broad continuation fails. Source recency/order remains untested by the read-only one-batch gradient marker; this is a hypothesis, not a diagnosed interference cause.',
        source_registry_review=reference(registry_review),parent=old['parent'],parent_actual_metadata=old['parent_actual_metadata'],
        source=old['source'],quotas=old['quotas'],source_order=['web','story','ordinary_textbook','conditional_textbook'],
        cached_control=dict(config=reference(ROOT/'configs/phase6/historical_parent_condition_comparison_v3.json'),
            result=reference(historical/'compare-result.json'),review=reference(review_path),
            notes=reference(ROOT/'reports/phase6/historical_parent_condition_notes.json'),
            generation=reference(historical/'evaluation/historical_parent/evaluation/generation.json'),
            checkpoint=dict(path=result['checkpoints']['historical_parent']['checkpoint'],sha256=result['checkpoints']['historical_parent']['checkpoint_sha256'])),
        actual_inherited_LR=.00001,optimizer_policy='inherit',scheduler_policy='Preserve actual permanent0.1 floor and parent scheduler clocks; no reheat or stage resets',
        seed=42,student_parameters=10001152,context=1024,batch=32,accumulation=1,
        new_scientific_teacher_tokens=100000000,reused_control_teacher_tokens=100000000,new_GPU_ceiling_seconds=900,
        comparison='Only cross-source ordering changes. Same parent/model/fullAdam/scheduler/RNG/actualLR, source content/within-source relative order/seed/tokenizer/loss/fullbody+EOS quotas. All four terminal source block traces/cursors and teacher/EOS/input/byte/focus counters must match cached mixed control; global token digest deliberately changes with order.',
        terminal_padding='After all teacher quotas, pad the final physical batch with all-masked Web blocks exactly as cached control. Source transitions may share an update; physical batch remains32x1024.',
        novelty=dict(registered_source_order_configs=configs,scan_scope='Top-level phase6 config keys plus exact source inspection of frozen quota sampler min(consumed/quota). No claim about unregistered work.',
            previous_fresh_curriculum=dict(config=reference(ROOT/'configs/phase6/curriculum_strategy.json'),
                interpretation=curriculum['interpretation'],coherent=prior_curriculum['summaries']['fresh']['coherent'],
                conclusion='Prior fresh short-pool run contains1M short/4M narrative/5M Web source, not a pure narrative foundation. Do not silently relabel it or pursue a pure-story ratio sweep. New study retains identical four teacher quotas and changes order only.')),
        CPU_sampler_tests=reference(ROOT/'reports/phase6/source_order_condition_tests.xml'),
        source_sha256={p:sha256(ROOT/p) for p in sources},
        CPU_evidence='Three tests pass: actual per-source x/y/focus block hashes, all five counter groups and terminal streams equal mixed; cross-phase resume restores exact tensors/cursors and refuses changed order/old-kind states. Tiny CPU fixtures do not prove GPU fullstate or quality.',
        required_before_science='Implement own immutable runner/reviewer/PowerShell and source binding, inspect existing processes, preserve control raw without GPU rerun. Actual CUDA4vs2+2 all32 fullstate/history/finite checks and32 timing, phase-boundary sampler CPU proof, measured science+eval+verification total<=900s. Discard verification weights. Freeze science only from completed measurement.',
        required_evaluation='Same original256/472055byte dev, Japanese192/331/1119, fixed80 greedy64, bridge128 andretention128. Read all new80, reuse judgments only exact raw matches. Same relative/absolute/historicalWeb guard gates; report all rather than selecting favorable endpoint.',
        completion='Exact100M terminal and all evaluations/content/accounting/adoption screens, durable checkpoint/job identity/logs and portable evidence, original10B UI restored and local commit. Passing this research pilot is not Base completion; independent learned seed/full dev/protected test/adoption remain required.',
        failure_policy='Preserve a failed finite order study; no automatic500M/2B extension, alternative order/ratio/LR/weight/filter/shape sweep, favorable checkpoint selection or gate relaxation.',
        source_material_recovered_or_retokenized=False,GPU_seconds=0,student_scientific_teacher_tokens=0,optimizer_updates=0,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        quality_criteria_unchanged=True,old_numerical7_preserved=True,CPU_proposal_seconds=time.monotonic()-started)
    path=ROOT/'reports/phase6/source_order_condition_comparison_proposal.json'
    if path.exists():raise ValueError('Preserve defined proposal')
    write_json(path,proposal)
    print(json.dumps(dict(status=proposal['status'],CPU_seconds=proposal['CPU_proposal_seconds'],selected_new_source=None,
        registered_source_order_configs=configs,student_scientific_teacher_tokens=0,GPU_seconds=0)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python required')
    main()
