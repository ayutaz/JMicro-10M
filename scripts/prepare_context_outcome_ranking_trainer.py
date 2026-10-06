"""Own CE/conditional-KL/ranking accumulation before a single optimizer update."""
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT
from prepare_hard_body_web_replay import once,write


def main():
    core=(ROOT/'scripts/eos_decoupled_web_kl_condition_trainer.py').read_text()
    core=once(core,'"""Inherited staged CE plus immutable-parent Web KL; checkpoint both samplers."""',
        '"""Inherited CE and conditional-Web-KL plus train-only opposite-context ranking."""')
    core=once(core,'from eos_decoupled_web_kl_preservation import POLICY,WebBodyReplay,body_parent_kl',
        'from eos_decoupled_web_kl_preservation import POLICY,WebBodyReplay,body_parent_kl\n'
        'from context_outcome_ranking import POLICY as RANKING_POLICY,OutcomePairSampler,outcome_ranking_loss')
    core=core.replace('WebKLTrainer','ContextOutcomeRankingTrainer')
    core=core.replace('historical_parent_staged_CE_frozen_Web_conditional_non_EOS_KL_100M',
        'historical_parent_staged_CE_conditional_Web_KL_train_outcome_ranking_100M')
    core=once(core,"('scripts/eos_decoupled_web_kl_condition_trainer.py','scripts/eos_decoupled_web_kl_preservation.py','scripts/web_kl_preservation.py')",
        "('scripts/context_outcome_ranking_trainer.py','scripts/context_outcome_ranking.py','scripts/eos_decoupled_web_kl_preservation.py','scripts/web_kl_preservation.py')")
    core=once(core,"goals,binding,device='cuda'", "goals,binding,ranking_view,device='cuda'")
    core=once(core,'        self.reference_non_EOS_teacher_mass=0.',
        '        self.reference_non_EOS_teacher_mass=0.\n'
        '        self.ranking=OutcomePairSampler(ranking_view,2,42)\n'
        "        self.spec.update(ranking_policy=dict(RANKING_POLICY,context=ranking_view.context),ranking_input_binding=ranking_view.binding)\n"
        "        self.lineage.update(ranking_policy=self.spec['ranking_policy'],ranking_input_binding=ranking_view.binding)")
    core=core.replace("kind='staged-CE-frozen-parent-Web-KL'", "kind='staged-CE-conditional-Web-KL-train-outcome-ranking'")
    core=once(core,"                raise ValueError('Separate retained probability mass ledger differs')",
        "                raise ValueError('Separate retained probability mass ledger differs')\n"
        "        if hasattr(self,'ranking'):\n"
        "            if (self.ranking.updates!=self.update-self.lineage['parent_update']\n"
        "                    or self.ranking.relational_choice_labels!=self.ranking.updates*4\n"
        "                    or self.ranking.physical_input_positions!=self.ranking.updates*8*self.ranking.view.context):\n"
        "                raise ValueError('Completed main update and ranking ledger differ')")
    core=once(core,'        rx,ry=self.replay.next()',
        '        rx,ry=self.replay.next()\n'
        '        before_gold=self.ranking.gold_body_scored_positions;before_foil=self.ranking.foil_body_scored_positions\n'
        '        px,py,pvalid,selected=self.ranking.next()')
    core=once(core,'        kl.backward();del target,prediction',
        '        kl.backward();del target,prediction\n'
        '        px,py,pvalid=px.to(self.device),py.to(self.device),pvalid.to(self.device)\n'
        '        # Padded short outcome batches use eager math attention. Main and Web KL keep their frozen compiled flash path.\n'
        "        with sdpa_kernel(SDPBackend.MATH),autocast(self.device,self.spec['dtype']):\n"
        '            pair_logits=self.model(px,attention_mask=pvalid).logits\n'
        '            pair_loss,pair_counts=outcome_ranking_loss(pair_logits,py)\n'
        '        pair_loss.backward();del pair_logits\n'
        "        if (pair_counts['relational_choice_labels']!=4\n"
        "                or pair_counts['gold_body_scored_positions']!=self.ranking.gold_body_scored_positions-before_gold\n"
        "                or pair_counts['foil_body_scored_positions']!=self.ranking.foil_body_scored_positions-before_foil):\n"
        "            raise ValueError('Measured relational labels/gold/foil positions differ')")
    core=once(core,'        ce_value,kl_value=float(ce.detach()),float(kl.detach())',
        '        ce_value,kl_value,pair_value=float(ce.detach()),float(kl.detach()),float(pair_loss.detach())')
    core=core.replace('(ce_value,kl_value,float(norm))','(ce_value,kl_value,pair_value,float(norm))')
    core=once(core,'loss=ce_value+kl_value,ordinary_CE_loss=ce_value,reference_KL_loss=kl_value,',
        'loss=ce_value+kl_value+pair_value,ordinary_CE_loss=ce_value,reference_KL_loss=kl_value,ranking_loss=pair_value,')
    core=once(core,"            combined_student_physical_input_tokens=self.tokens-self.lineage['parent_tokens']+self.replay.physical_input_tokens)",
        "            main_and_Web_reference_physical_input_tokens=self.tokens-self.lineage['parent_tokens']+self.replay.physical_input_tokens,\n"
        "            combined_student_physical_input_tokens=self.tokens-self.lineage['parent_tokens']+self.replay.physical_input_tokens+self.ranking.physical_input_positions,\n"
        "            combined_student_valid_input_tokens=self.tokens-self.lineage['parent_tokens']+self.replay.physical_input_tokens+self.ranking.valid_input_tokens,\n"
        '            ranking_family_indices=selected,ranking_digest=self.ranking.digest,\n'
        '            ranking_relational_choice_labels=self.ranking.relational_choice_labels,\n'
        '            ranking_valid_input_tokens=self.ranking.valid_input_tokens,ranking_physical_input_positions=self.ranking.physical_input_positions,\n'
        '            ranking_gold_body_scored_positions=self.ranking.gold_body_scored_positions,\n'
        '            ranking_foil_body_scored_positions=self.ranking.foil_body_scored_positions,\n'
        '            ranking_gold_body_scored_bytes=self.ranking.gold_body_scored_bytes,ranking_foil_body_scored_bytes=self.ranking.foil_body_scored_bytes)')
    core=once(core,"            KL_state=dict(policy=self.spec['KL_policy']",
        "            ranking_state=dict(policy=self.spec['ranking_policy'],input_binding=self.ranking.view.binding,sampler=self.ranking.state_dict()),\n"
        "            KL_state=dict(policy=self.spec['KL_policy']")
    core=once(core,"        self.replay.load_state_dict(extra['replay'])",
        "        ranking=state['ranking_state']\n"
        "        if ranking['policy']!=self.spec['ranking_policy'] or ranking['input_binding']!=self.ranking.view.binding:\n"
        "            raise ValueError('Fixed train-family ranking objective/input differs')\n"
        "        self.ranking.load_state_dict(ranking['sampler'])\n"
        "        self.replay.load_state_dict(extra['replay'])")
    resident=(ROOT/'scripts/eos_decoupled_resident_web_kl_trainer.py').read_text()
    resident=resident.replace('eos_decoupled_web_kl_condition_trainer','context_outcome_ranking_trainer')
    resident=resident.replace('BaseWebKLTrainer','BaseContextOutcomeRankingTrainer').replace('WebKLTrainer','ContextOutcomeRankingTrainer')
    resident=once(resident,"goals,binding,device='cuda'", "goals,binding,ranking_view,device='cuda'")
    resident=once(resident,'goals,binding,device,context,batch,reference_batch)', 'goals,binding,ranking_view,device,context,batch,reference_batch)')
    resident=once(resident,'"""Change only Web input delivery; inherit the tested CE/KL math and grad buffers."""',
        '"""Same accepted resident Web inputs, plus existing TRAIN outcome-pair ranking."""')
    outputs={'scripts/context_outcome_ranking_trainer.py':core,'scripts/context_outcome_ranking_resident_trainer.py':resident}
    for relative,text in outputs.items():
        compile(text,relative,'exec')
        if (ROOT/relative).exists():raise ValueError('Preserve own generated trainer')
    for relative,text in outputs.items():write(relative,text)
    print('Own CE/conditionalKL/ranking trainer and resident adaptor prepared; no GPU learning started')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
