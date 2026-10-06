"""Prepare terminal metadata accounting without changing the active frozen experiment."""
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT
from prepare_hard_body_web_replay import once,write


def main():
    relative='scripts/record_anchored_context_outcome_completion.py'
    if (ROOT/relative).exists():raise ValueError('Preserve owned completion writer')
    source=(ROOT/'scripts/record_context_outcome_ranking_completion.py').read_text()
    source=source.replace('run_context_outcome_ranking_comparison','run_anchored_context_outcome_comparison')
    source=source.replace('context_outcome_ranking100M_terminal_pilot_fully_reviewed','positive_anchor100M_terminal_pilot_fully_reviewed')
    source=source.replace('context_outcome_ranking_comparison_','anchored_context_outcome_comparison_')
    source=source.replace("glob('context_outcome_ranking_*')","glob('anchored_context_outcome_*')")
    source=source.replace("glob('context_outcome_ranking_*.json')","glob('anchored_context_outcome_*.json')")
    source=source.replace("glob('*context_outcome*')","glob('*anchored_context_outcome*')")
    source=source.replace("glob('test_context_outcome*.py')","glob('test_anchored_context_outcome*.py')")
    source=once(source,"            or not review['ranking_accounting']['all_completed_train_family_order_and_ledger_rows_verified']):",
        "            or not review['ranking_accounting']['all_completed_train_family_order_and_ledger_rows_verified']\n"
        "            or not review['all3068_main_Web_and_ranking_input_protocols_equal']\n"
        "            or not review['positive_anchor_accounting']['all_completed_positive_teacher_and_loss_rows_verified']):")
    source=once(source,"    record=r['checkpoints'][study.ARM];ev=r['evaluations'][study.ARM]",
        "    record=r['checkpoints'][study.ARM];ev=r['evaluations'][study.ARM]\n"
        "    analysis=ROOT/'reports/phase6/anchored_context_outcome_absolute_likelihood.json'\n"
        "    a=read_json(analysis)\n"
        "    if (a['forward_requests'] or a['GPU_seconds'] or a['raw_requests_reused']!=2048\n"
        "            or a['terminal_result_refs']!=[study.reference(study.MECHANISM_RUN/'compare-result.json'),study.reference(study.RUN/'compare-result.json')]\n"
        "            or record['positive_anchor_body_teacher_tokens']!=73725\n"
        "            or record['combined_hard_teacher_positions']!=100073725):\n"
        "        raise ValueError('Actual same-input anchor teacher and full cached likelihood evidence required')")
    source=once(source,'        ranking_ordinary_CE_teacher_tokens=0,ranking_soft_distribution_target_positions=0,',
        "        ranking_ordinary_CE_teacher_tokens=0,ranking_soft_distribution_target_positions=0,\n"
        "        positive_anchor_body_teacher_tokens=record['positive_anchor_body_teacher_tokens'],\n"
        "        combined_hard_teacher_positions=record['combined_hard_teacher_positions'],\n"
        "        positive_anchor_accounting=review['positive_anchor_accounting'],absolute_likelihood_analysis=study.reference(analysis),\n"
        "        all3068_main_Web_and_ranking_input_protocols_equal=review['all3068_main_Web_and_ranking_input_protocols_equal'],")
    source=once(source,"        verification_CE_teacher_tokens=probe['verification_teacher_tokens'],",
        "        verification_CE_teacher_tokens=probe['verification_teacher_tokens'],\n"
        "        verification_positive_anchor_teacher_tokens=probe['verification_positive_anchor_teacher_tokens'],")
    source=source.replace('against_conditional_KL=paired','against_relative_only_ranking=paired')
    source=source.replace('Additional TRAIN context/outcome/foil input exposures and relational supervision differ; not equal total supervision/time.',
        'All main/Web/pair input exposures match the ranking mechanism control; adds73725 positive hard teacher positions. Strong stagedCE remains the quality control; no equality of supervision/time is claimed.')
    source=source.replace('Preserve rejected100M outcome-ranking hypothesis','Preserve rejected100M positive-likelihood anchor hypothesis')
    compile(source,relative,'exec');write(relative,source)
    print('Owned terminal positive-anchor accounting/archive writer prepared; science completion not claimed.')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
