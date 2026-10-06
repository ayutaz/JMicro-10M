"""Own the same cached-score diagnostic for ranking versus positive-anchor models."""
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT
from prepare_hard_body_web_replay import once,write


def main():
    relative='scripts/analyze_anchored_context_outcome_scores.py'
    if (ROOT/relative).exists():raise ValueError('Preserve owned cached-score analyzer')
    source=(ROOT/'scripts/analyze_context_outcome_ranking_scores.py').read_text()
    source=once(source,'import run_context_outcome_ranking_comparison as study','import run_anchored_context_outcome_comparison as study')
    source=once(source,'context_outcome_ranking_absolute_likelihood.json','anchored_context_outcome_absolute_likelihood.json')
    source=source.replace('conditional_KL','context_ranking_control').replace('context_ranking\'','positive_anchor\'')
    # Literal names occur in both score collection and paired direction arithmetic.
    source=once(source,"question='When ranking accuracy improves but generation quality worsens, does absolute gold likelihood improve, or does the foil merely become less likely faster?'",
        "question='Does the added positive likelihood term improve absolute gold likelihood versus completed ranking, and is that accompanied by useful generated text?' ")
    source=once(source,"fixed_comparison='Terminal conditionalKL versus terminal conditionalKL+TRAIN outcome-ranking; all256 fixed families/two context poles, no selection or new scoring.'",
        "fixed_comparison='Terminal ranking versus terminal ranking plus one conditional-nonEOS positive CE anchor; all256 fixed families/two context poles, no selection or new scoring.'")
    compile(source,relative,'exec');write(relative,source)
    print('Owned read-only cached absolute likelihood analysis prepared; GPU/forward0.')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
