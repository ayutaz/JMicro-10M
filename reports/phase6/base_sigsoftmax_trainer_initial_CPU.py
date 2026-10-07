"""Same original hard-gold corpus, with sigsoftmax normalized model likelihood."""
import copy
from pathlib import Path
import torch
from natural_context_contrast_corpus import NaturalCorpusTrainer
from base_native_teacher_KD_trainer import finite_KD_state
from base_sigsoftmax_model import LINK, install_sigsoftmax

KIND = 'native_original_gold_sigsoftmax_NLL_v1'
RECIPE = dict(output_probability_link=LINK,
    effective_logits='FP32_raw_z_plus_logsigmoid_raw_z_exactly_once',
    target='original_hard_body_and_EOS_targets_unchanged',
    loss='mean_hard_gold_NLL_under_sigsoftmax_probabilities',
    coefficient_or_temperature=None, added_bias_or_shift=False,
    extra_parameters=0, teacher=False, decoder_forwards=1,
    optimizer='fresh_AdamW_lr1e-5_wd0.1_constant', clip_norm=1.,
    inference='same_link_full_cache_padded_likelihood_greedy_policy_unchanged')


def committed_state(state):
    try:
        if (state['kind'] != KIND or state['spec']['sigsoftmax'] != RECIPE
                or state['spec']['contrast'] or state['model_config'].get('output_probability_link') != LINK):
            return False
        c = state['counters']
        steps = c['update']
        opt = state['optimizer']
        if (type(steps) is not int or steps < 0 or state['scheduler']['last_epoch'] != steps
                or any(int(v['step']) != steps for v in opt['state'].values())
                or (steps and len(opt['state']) != sum(len(g['params']) for g in opt['param_groups']))
                or c['supervised_tokens'] != sum(c['source_teachers'].values())
                or c['source_teachers'] != state['sampler']['consumed']
                or c['auxiliary_input_tokens'] or c['auxiliary_pairs'] or c['auxiliary_digest'] != '0' * 64):
            return False
        return finite_KD_state(state)
    except (KeyError, TypeError, ValueError, OverflowError):
        return False


class SigSoftmaxTrainer(NaturalCorpusTrainer):
    def __init__(self, parent, sampler, binding, batch=48, contrast=False, device='cuda', seed=42):
        if contrast or parent['model_config'].get('output_probability_link') is not None:
            raise ValueError('Original ordinary-softmax parent and hard-gold-only objective required')
        super().__init__(parent, sampler, binding, batch, False, device, seed)
        install_sigsoftmax(self.model)
        self.spec.update(kind=KIND, sigsoftmax=copy.deepcopy(RECIPE))
        self.lineage.update(kind=KIND, output_probability_link=LINK)
        self._step_in_progress = False

    def _state_at_boundary(self):
        state = super().state_dict()
        state['kind'] = KIND
        return state

    def state_dict(self):
        if self._step_in_progress:
            raise ValueError('Cannot serialize uncommitted sigsoftmax update')
        return self._state_at_boundary()

    def load(self, path):
        state = torch.load(Path(path), map_location=self.device, weights_only=False)
        if not committed_state(state):
            raise ValueError('Committed explicitly tagged sigsoftmax state required')
        super().load(path)
        self._step_in_progress = False

    def step(self):
        if self._step_in_progress:
            raise ValueError('Interrupted update requires valid checkpoint resume')
        self._step_in_progress = True
        row = super().step()
        if not committed_state(self._state_at_boundary()):
            raise ValueError('Finite original-gold committed sigsoftmax state required')
        self._step_in_progress = False
        row.update(sigsoftmax_NLL_loss=row['CE_loss'], output_probability_link=LINK,
            probability_positions_this_update=row['CE_targets_this_update'], committed_update=True)
        return row
