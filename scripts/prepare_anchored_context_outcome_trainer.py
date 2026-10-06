"""Copy the completed ranking protocol into new owned positive-anchor trainer files."""
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT
from prepare_hard_body_web_replay import once,write


def main():
    core=(ROOT/'scripts/context_outcome_ranking_trainer.py').read_text()
    core=core.replace('ContextOutcomeRankingTrainer','AnchoredContextOutcomeTrainer')
    core=core.replace("kind='staged-CE-conditional-Web-KL-train-outcome-ranking'",
        "kind='staged-CE-conditional-Web-KL-train-anchored-outcome-ranking'")
    core=core.replace('historical_parent_staged_CE_conditional_Web_KL_train_outcome_ranking_100M',
        'historical_parent_staged_CE_conditional_Web_KL_train_anchored_outcome_ranking_100M')
    core=once(core,'from context_outcome_ranking import POLICY as RANKING_POLICY,OutcomePairSampler,outcome_ranking_loss',
        'from context_outcome_ranking import POLICY as RANKING_POLICY,OutcomePairSampler\n'
        'from anchored_context_outcome import POLICY as ANCHOR_POLICY,anchored_outcome_loss')
    core=once(core,"('scripts/context_outcome_ranking_trainer.py','scripts/context_outcome_ranking.py',",
        "('scripts/anchored_context_outcome_trainer.py','scripts/anchored_context_outcome.py','scripts/context_outcome_ranking.py',")
    core=once(core,'        self.ranking=OutcomePairSampler(ranking_view,2,42)',
        '        self.ranking=OutcomePairSampler(ranking_view,2,42)\n'
        '        self.positive_anchor_body_teacher_tokens=0\n'
        "        self.spec.update(positive_anchor_policy=ANCHOR_POLICY)\n"
        "        self.lineage.update(positive_anchor_policy=ANCHOR_POLICY)")
    core=once(core,"                raise ValueError('Completed main update and ranking ledger differ')",
        "                raise ValueError('Completed main update and ranking ledger differ')\n"
        "        if hasattr(self,'positive_anchor_body_teacher_tokens') and self.positive_anchor_body_teacher_tokens!=self.ranking.gold_body_scored_positions:\n"
        "            raise ValueError('Positive hard teachers and completed gold-body positions differ')")
    core=once(core,'            pair_loss,pair_counts=outcome_ranking_loss(pair_logits,py)',
        '            pair_loss,ranking_loss,anchor_loss,pair_counts=anchored_outcome_loss(pair_logits,py)')
    core=once(core,"                or pair_counts['foil_body_scored_positions']!=self.ranking.foil_body_scored_positions-before_foil):",
        "                or pair_counts['foil_body_scored_positions']!=self.ranking.foil_body_scored_positions-before_foil\n"
        "                or pair_counts['positive_anchor_body_teacher_tokens']!=pair_counts['gold_body_scored_positions']):")
    core=once(core,'        ce_value,kl_value,pair_value=float(ce.detach()),float(kl.detach()),float(pair_loss.detach())',
        '        ce_value,kl_value,pair_value=float(ce.detach()),float(kl.detach()),float(pair_loss.detach())\n'
        '        ranking_value,anchor_value=float(ranking_loss.detach()),float(anchor_loss.detach())')
    core=once(core,'(ce_value,kl_value,pair_value,float(norm))','(ce_value,kl_value,pair_value,ranking_value,anchor_value,float(norm))')
    core=once(core,"        self.reference_non_EOS_teacher_mass+=reference_counts['non_EOS_teacher_probability_mass']",
        "        self.reference_non_EOS_teacher_mass+=reference_counts['non_EOS_teacher_probability_mass']\n"
        "        self.positive_anchor_body_teacher_tokens+=pair_counts['positive_anchor_body_teacher_tokens']")
    core=once(core,'reference_KL_loss=kl_value,ranking_loss=pair_value,',
        'reference_KL_loss=kl_value,ranking_loss=ranking_value,positive_anchor_loss=anchor_value,combined_pair_loss=pair_value,\n'
        '            positive_anchor_body_teacher_tokens=self.positive_anchor_body_teacher_tokens,\n'
        "            combined_hard_teacher_positions=self.supervised_tokens-self.lineage['parent_supervised_tokens']+self.positive_anchor_body_teacher_tokens,")
    core=once(core,"            ranking_state=dict(policy=self.spec['ranking_policy'],input_binding=self.ranking.view.binding,sampler=self.ranking.state_dict()),",
        "            ranking_state=dict(policy=self.spec['ranking_policy'],input_binding=self.ranking.view.binding,sampler=self.ranking.state_dict()),\n"
        "            positive_anchor_state=dict(policy=ANCHOR_POLICY,body_teacher_tokens=self.positive_anchor_body_teacher_tokens,input_binding=self.ranking.view.binding),")
    core=once(core,"        self.ranking.load_state_dict(ranking['sampler'])",
        "        anchor=state['positive_anchor_state']\n"
        "        if anchor['policy']!=ANCHOR_POLICY or anchor['input_binding']!=self.ranking.view.binding:\n"
        "            raise ValueError('Positive likelihood anchor policy/train-input differs')\n"
        "        self.positive_anchor_body_teacher_tokens=anchor['body_teacher_tokens']\n"
        "        self.ranking.load_state_dict(ranking['sampler'])")
    resident=(ROOT/'scripts/context_outcome_ranking_resident_trainer.py').read_text()
    resident=resident.replace('context_outcome_ranking_trainer','anchored_context_outcome_trainer').replace('ContextOutcomeRankingTrainer','AnchoredContextOutcomeTrainer')
    outputs={'scripts/anchored_context_outcome_trainer.py':core,'scripts/anchored_context_outcome_resident_trainer.py':resident}
    for relative,text in outputs.items():
        compile(text,relative,'exec')
        if (ROOT/relative).exists():raise ValueError('Preserve owned positive-anchor prototype')
    for relative,text in outputs.items():write(relative,text)
    print('Owned positive likelihood loss/trainer/resident adapter prepared; GPU not started.')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
