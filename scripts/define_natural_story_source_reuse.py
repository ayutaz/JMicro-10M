"""Define a source replacement, including finite feasibility and content gates."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from prepare_natural_story_source import PROPOSAL


def ref(path): return dict(path=str(path), sha256=sha256(path))


def main():
    if PROPOSAL.exists(): raise ValueError('Preserve fixed source comparison')
    previous = read_json(ROOT/'reports/phase6/narrative_condition_source_proposal.json')
    c = read_json(ROOT/'configs/phase6/source_order_condition_comparison_v2.json')
    old_names = ('natural_learning', 'story_weight_comparison', 'textbook_quantity_comparison',
                 'historical_parent_condition_comparison_v3', 'source_order_condition_comparison_v2')
    contrasts = {}
    for name in old_names:
        path = ROOT/f'configs/phase6/{name}.json'; old = read_json(path)
        contrasts[name] = dict(config=ref(path), parent=old['parent'], arms=old.get('arms'), peak_lr=old.get('peak_lr'),
            source_order=old.get('source_order'), distinction='Different parent/LR/material/mixture or conditional source still retained; not this same-parent staged conditional->whole-story contrast.')
    ready = ROOT/'reports/phase6/textbook_mixture_ready.json'
    review = ROOT/'reports/phase6/textbook_mixture_content_review.json'
    p = dict(status='one_existing_TRAIN_whole_story_source_replacement_proposed', created_at=now(),
        trigger=ref(ROOT/'reports/phase6/narrative_condition_source_completion.json'),
        rationale='The local expanded renderer failed content readiness, so do not patch/retry it. Use independently authored original whole source-train stories already present, without fact/name/template generation. This tests source representation/diversity as a bundle, not data amount alone.',
        pool=dict(path=c['pool']['pool'], manifest_sha256=c['pool']['manifest_sha256']),
        tokenizer=dict(path='artifacts/phase2/4096/tokenizer.model', sha256='a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'),
        references=dict(accepted_pool_ready=ref(ready), accepted_pool_review=ref(review),
            compact_cache=c['accepted_compact_index'], strong_control_config=ref(ROOT/'configs/phase6/source_order_condition_comparison_v2.json'),
            strong_control_result=previous['proposed_comparison']['strong_control']['result']),
        existing_accepted_source_story_tokens=read_json(ready)['prepared_tokens']['large_story'],
        prior_control_protocols=contrasts,
        preparation=dict(CPU_ceiling_seconds=60, seed=2026100692, source='All story-tagged existing TRAIN document indices only',
            sampling='Uniform64 whole original stories without replacement using predeclared seed; no content/length selection, reroll, patch or post-pilot filtering',
            content_gate='All64 individually read/rawSHA bound; weak<=10, unresolved grammar and temporal/object grounding issues0. Different plausible fictional stories accepted; no external factual truth certification.',
            copy_or_truncate_original_text=False, giant_index_or_source_rescan=False, use_existing_content_bound_compact_cache=True),
        proposed_comparison=dict(parent=c['parent'], strong_control=previous['proposed_comparison']['strong_control'],
            main_teacher_tokens=100000000, staged_slot_quotas=c['arms']['source_order'], source_order=c['source_order'],
            final_slot='Replace only conditional10M with whole source-train stories; other slots Web75M/story5M/ordinary10M',
            final_story_shuffle='Separate seed42 stream with same fixed PositiveStream seed tuple[seed,epoch,3,100], not restart/continuation of first story5M stream',
            actual_LR=.00001, optimizer_policy='inherit full parent model/Adam/scheduler/RNG', shapes=c['shapes'],
            loss='ordinary body+EOS CE weight1; no rank/KL/anchor auxiliary',
            input_comparability='Verify byte-exact first90M source sequences/cursors/counters against staged control. Final conditional body/EOS/length change; terminal all-masked Web padding may change and must be accounted separately, not claimed identical.',
            new_GPU_ceiling_seconds_including_probes=900, nontraining_reserve_seconds=150, margin=1.3, slack_seconds=50,
            CUDA_gate='Own continuous4 vs2+2 full state that actually exercises replacement stream, plus32 measured updates spanning changed source. Probe and failed costs preserved; science configuration frozen only if estimate fits900.',
            evaluation='Same256 commonbyte full bodies/Japanese192-331-1119/all80 individually read/bridge128 and retention128. Same scorer, splits, decoder and strong relative/absolute/historical Web guards.',
            quality_gate=previous['proposed_comparison']['quality_gate'], quality_criteria_unchanged=True),
        limitations='Same existing100M story corpus; no new corpus/family or natural-human-source claim. Replacing artificial conditional material changes semantic content, source diversity, EOS density and length together; not isolated quantity effect. Shared fixeddev/nonblind one seed cannot prove final generalization.',
        completion_condition='One finite source preparation; reject source if prerequisite fails. Only accepted source plus actual measured CUDA/budget qualifies one terminal100M comparison and full content review; no sweep/CPscan/automatic extension.',
        source_sha256={'scripts/prepare_natural_story_source.py':sha256(ROOT/'scripts/prepare_natural_story_source.py')},
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False, protected_test_used=False,
        scientific_teacher_tokens=0, actual_GPU_seconds=0, preserved_related_GPU_seconds=2289.596018486074,
        next_action='Prepare frozen native whole-story source indices/fixed64; all64 raw-bound review before implementing own trainer and actual CUDA gate.')
    atomic_json(PROPOSAL, p)
    print(dict(status=p['status'], source_story_tokens=p['existing_accepted_source_story_tokens']))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
