"""Separate new hard teachers from fixed main/Web/ranking exposure ledgers."""
import math
from anchored_context_outcome import POLICY
from context_outcome_ranking_accounting import audit_reference,audit_ranking


def audit_anchor(parent,state,record,history,config):
    extra=state['positive_anchor_state'];count=extra['body_teacher_tokens']
    if (config['positive_anchor_policy']!=POLICY or extra['policy']!=POLICY
            or state['spec']['positive_anchor_policy']!=POLICY or state['lineage']['positive_anchor_policy']!=POLICY
            or extra['input_binding']!=state['ranking_state']['input_binding']
            or record['positive_anchor_policy']!=POLICY
            or count!=state['ranking_state']['sampler']['gold_body_scored_positions']
            or record['positive_anchor_body_teacher_tokens']!=count
            or record['combined_hard_teacher_positions']!=state['supervised_tokens']-parent['supervised_tokens']+count):
        raise ValueError('Positive likelihood hard teacher policy/input/terminal count differs')
    for row in history:
        if (row['positive_anchor_body_teacher_tokens']!=row['ranking_gold_body_scored_positions']
                or row['combined_hard_teacher_positions']!=row['additional_teacher_tokens']+row['positive_anchor_body_teacher_tokens']
                or not all(math.isfinite(row[k]) for k in ('positive_anchor_loss','combined_pair_loss','ranking_loss'))
                or row['positive_anchor_loss']<0 or row['ranking_loss']<0
                or not math.isclose(row['combined_pair_loss'],row['ranking_loss']+row['positive_anchor_loss'],rel_tol=1e-6,abs_tol=1e-6)
                or not math.isclose(row['loss'],row['ordinary_CE_loss']+row['reference_KL_loss']+row['combined_pair_loss'],rel_tol=1e-12)):
            raise ValueError('Completed positive likelihood/combined teacher history differs')
    if not history or history[-1]['positive_anchor_body_teacher_tokens']!=count:
        raise ValueError('Positive likelihood completed history missing')
    return dict(positive_anchor_body_teacher_tokens=count,combined_hard_teacher_positions=record['combined_hard_teacher_positions'],
        foil_hard_teacher_positions=0,new_original_corpus_tokens=0,extra_input_positions_relative_to_ranking_control=0,
        all_completed_positive_teacher_and_loss_rows_verified=True)
