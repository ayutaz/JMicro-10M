"""Committed-update boundary around the unchanged frozen native predictive KD.

This does not change its objective or forward/backward implementation. A separately
declared prospective budget study must not overwrite the old3600s budget rejection.
"""
import copy
from pathlib import Path
import torch
from base_native_teacher_KD_trainer import NativeTeacherKDTrainer,KIND,finite_KD_state

BOUNDARY='original_and_KD_counters_after_single_Adam_scheduler_update_v1'
RECIPE=dict(original_CE_coefficient=1.,KD_coefficient=1.,KD_temperature=1.,
    KD_sources=['textbook','story'],KD_denominator='all_original_gold_positions_this_update',
    KD_targets='full_native_vocab_predictive_distribution_on_same_original_supervised_positions',
    teacher_frozen_eval=True,forward_implementation='unchanged_eager_native_no_compile',
    optimizer='fresh_AdamW_lr1e-5_wd0.1_constant',commit_boundary=BOUNDARY,
    study='new_prospective4800_budget_for_previously_untrained_effect_not_novel_math')


def accounting_matches(c,k,sampler_consumed):
    expected={g:(c['source_teachers'][g] if g in ('textbook','story') else 0) for g in ('web','textbook','story')}
    return (c['source_teachers']==sampler_consumed and c['supervised_tokens']==sum(c['source_teachers'].values()) and
        k['updates']==c['update'] and k['source_positions']==expected and
        k['teacher_positions']==sum(expected.values()) and
        k['teacher_EOS']==sum(c['source_EOS'][g] for g in ('textbook','story')) and
        0<=k['teacher_positions']<=k['teacher_valid_inputs']<=k['teacher_physical_inputs'] and
        not c['auxiliary_input_tokens'] and not c['auxiliary_pairs'] and c['auxiliary_digest']=='0'*64)


def committed_state(state):
    try:
        if state['kind']!=KIND or state['spec'].get('commit_boundary')!=BOUNDARY or state['spec'].get('prospective_KD_study')!=RECIPE:
            return False
        c,k=state['counters'],state['native_teacher_KD']; steps=c['update']
        optimizer=state['optimizer']
        if (not accounting_matches(c,k,state['sampler']['consumed']) or state['scheduler']['last_epoch']!=steps or
            any(int(v['step'])!=steps for v in optimizer['state'].values()) or
            (steps>0 and len(optimizer['state'])!=sum(len(g['params']) for g in optimizer['param_groups']))): return False
        return finite_KD_state(state)
    except (KeyError,TypeError,ValueError):
        return False


class CommittedNativeTeacherKDTrainer(NativeTeacherKDTrainer):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.spec.update(commit_boundary=BOUNDARY,prospective_KD_study=copy.deepcopy(RECIPE))
        self._step_in_progress=False

    def state_dict(self):
        if self._step_in_progress: raise ValueError('Cannot serialize incomplete native-KD update')
        return super().state_dict()

    def load(self,path):
        state=torch.load(Path(path),map_location='cpu',weights_only=False)
        if not committed_state(state): raise ValueError('Committed native-KD fullstate required')
        super().load(path)
        self._step_in_progress=False

    def step(self):
        if self._step_in_progress: raise ValueError('Interrupted native-KD update requires valid checkpoint resume')
        self._step_in_progress=True
        row=super().step()
        if not accounting_matches(self.counters,self.KD,self.sampler.consumed):
            raise ValueError('Original/KD/source accounting must commit together')
        self._step_in_progress=False
        return row|{'committed_update':True}
