"""Independent native seed construction; no GPU launch or Base adoption here."""
import copy

from base_parallel_residual_trainer import FreshResidualTrainer, CEOnlyOriginalSampler
from base_teacher_decay_trainer import TeacherDecayTrainer, committed_decay, policy
from jmicro.phase5 import equal_state


SEED = 43
GOALS = dict(web=1500000000, textbook=400000000, story=100000000)


def require_quality_screen(completion):
    """A positive pilot/BPB result cannot authorize independent long training."""
    if (completion.get('status') != 'same_parent_teacher_decay2B_all80_reviewed'
            or completion.get('eligible_for_final_Base_validation') is not True
            or completion.get('fixed_condition_closed') is not False
            or completion.get('all80_new_individually_read') is not True
            or completion.get('old_control80_original_notes_reused') is not True
            or completion.get('process_exited') is not True
            or completion.get('scientific_cumulative_teacher_tokens') != sum(GOALS.values())
            or any(completion.get(k) is not False for k in
                   ('Base_complete', 'Base_adopted', 'Chat_started',
                    'quantization_started', 'protected_test_scored'))):
        raise ValueError('Completed unchanged full-quality native2B screen required')
    required_absolute = {'grammar_at_least56', 'coherence_at_least27',
                         'appropriate_at_least27', 'EOS_at_least37',
                         'repetition_at_most18', 'no_empty_role_unicode'}
    absolute = completion.get('absolute_dev_screen', {})
    comparisons = completion.get('quality_comparisons', {})
    historical = completion.get('original_Web', {})
    if (set(absolute) != required_absolute
            or any(value is not True for value in absolute.values())
            or set(comparisons) != {'matched_native', 'strong', 'cached_native'}
            or any(row.get('passed') is not True for row in comparisons.values())
            or not historical or any(value is not True for value in historical.values())):
        raise ValueError('All original matched/strong/cached/absolute/Web guards required')


def build_independent(plan, codec, binding, device='cuda'):
    """Fresh weights/Adam/training RNG AND fresh material RNG43, same recipe.

    Source artifacts and successful content review must be verified by the
    eventual durable runner before calling this constructor. This low-level
    factory is also exercised on CPU fixtures; it is not launch authorization.
    Never load seed42 learned/probe weights into this object.
    """
    if (plan['goals'] != GOALS or plan['optimizer']['seed'] != 42
            or binding.get('training_seed') != SEED
            or binding.get('weights_role') != 'scientific_independent_seed_confirmation'
            or binding.get('source_binding') != plan['source_binding']
            or binding.get('learned_parent_weights_used') is not False
            or binding.get('probe_weights_used') is not False):
        raise ValueError('Explicit independent43 and unchanged original2B quota recipe required')
    source = plan['source_binding']
    sampler = CEOnlyOriginalSampler(source['pool'], source['manifest_sha256'],
                                    codec, copy.deepcopy(GOALS), seed=SEED)
    if sampler.binding != source:
        raise ValueError('Same accepted source binding required')
    opt = plan['optimizer']
    native = FreshResidualTrainer(copy.deepcopy(plan['variants']['sequential']),
        sampler, copy.deepcopy(binding), 'sequential', batch=opt['batch'],
        device=device, seed=SEED, warmup=opt['warmup_gold'],
        peak=opt['peak_lr'], final=opt['final_lr'])
    return TeacherDecayTrainer(native)


def validate_independent_zero(source_zero, candidate_zero):
    """Prove a distinct actual initialization without changing the recipe.

    Different material draws are intentional. Do not require seed43 to have
    the seed42 sampler RNG/digest, or call a generation seed a learning seed.
    """
    if (not committed_decay(source_zero) or not committed_decay(candidate_zero)
            or source_zero['spec']['seed'] != 42 or candidate_zero['spec']['seed'] != SEED
            or source_zero['sampler']['seed'] != 42 or candidate_zero['sampler']['seed'] != SEED
            or any(s['counters']['update'] or s['counters']['supervised_tokens']
                   or s['optimizer']['state'] for s in (source_zero, candidate_zero))
            or candidate_zero['binding'].get('training_seed') != SEED
            or candidate_zero['binding'].get('weights_role') != 'scientific_independent_seed_confirmation'
            or candidate_zero['binding'].get('learned_parent_weights_used') is not False
            or candidate_zero['binding'].get('probe_weights_used') is not False
            or candidate_zero['lineage']['parent'] is not None):
        raise ValueError('Untouched actual fresh42/fresh43 states required')
    source_spec = dict(source_zero['spec'], seed=SEED)
    source_lineage = dict(source_zero['lineage'], seed=SEED,
                          weights_role=candidate_zero['lineage']['weights_role'])
    same = ('kind', 'model_config', 'scheduler', 'counters', 'decay')
    if (not equal_state(source_spec, candidate_zero['spec'])
            or not equal_state(source_lineage, candidate_zero['lineage'])
            or any(not equal_state(source_zero[k], candidate_zero[k]) for k in same)
            or any(not equal_state(source_zero['sampler'][k], candidate_zero['sampler'][k])
                   for k in ('kind', 'binding', 'goals', 'consumed', 'pending',
                             'draws', 'documents_drawn', 'windows_emitted', 'auxiliary_reasons'))
            or equal_state(source_zero['model'], candidate_zero['model'])
            or equal_state(source_zero['RNG'], candidate_zero['RNG'])
            or equal_state(source_zero['sampler']['RNG'], candidate_zero['sampler']['RNG'])
            or candidate_zero['decay']['policy'] != policy()):
        raise ValueError('Same native recipe with distinct actual weights/RNG/material43 required')
    return dict(same_native_recipe=True, untouched_zero_updates=True,
                distinct_actual_initial_weights=True, distinct_training_RNG=True,
                distinct_material_RNG=True, no_learned_parent_weights=True)
