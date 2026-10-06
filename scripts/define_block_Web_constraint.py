"""Distinct block-boundary functional constraint, not old per-update success."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import sys
from pathlib import Path
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,now
from jmicro.training import atomic_json
import run_finite_Web_constraint as original
import probe_compiled_Web_oracle as compiled


def main():
    path=ROOT/'reports/phase6/block_Web_constraint_proposal.json'
    if path.exists():raise ValueError('Preserve original block proposal')
    c=original.inspect(original.PROBE_CONFIG);p=read_json(original.PROPOSAL)
    result=read_json(compiled.RUN/'result.json');job=read_json(compiled.RUN/'job.json')
    from phase6_performance import alive
    if job['status']!='complete' or alive(job) or not result['passed'] or result['estimated_total_with_prior_and_own_probes']<=2400:
        raise ValueError('Actual completed, over-budget per-update implementation required')
    proposal=dict(p,kind='finite_Web_body_NLL_at_20_update_transaction_boundaries_v1',created_at=now(),
        block_updates=20,probe_GPU_ceiling_seconds=120,total_new_GPU_ceiling_seconds=2400,
        previous_related_GPU_seconds=result['GPU_seconds']+read_json(compiled.CONFIG)['previous_related_GPU_seconds'],
        implemented=False,launched=False,Base_complete=False,GPU_seconds_so_far=0,new_CE_teacher_tokens_so_far=0,
        hypothesis='Constrain the same native FP32/math memory loss at fixed 20-update accepted boundaries; use full source learning between boundaries and amortize loss measurement. This may retain the function without the per-update computation budget failure. Held-out quality remains unproven.',
        scope_difference='Does not satisfy the old per-update constraint contract. Intermediate tentative source updates may exceed the memory ceiling. Only accepted block boundaries are bounded/saved; old per-update budget rejection stays rejected.',
        transaction='Snapshot full weights/Adam/scheduler/RNG/sampler/counters at each accepted boundary, propose up to20 original staged updates, apply unchanged single finite projector/backtracks from block start; accept all rows only if boundary native MATH loss<=original*1.01. Reject/interrupt restores the entire tentative block; tentative exposures separate.',
        optimizer_policy='Inherited original Adam and scheduler floor/actualLR.00001; accepted projection changes boundary weights, keeps the proposed Adam state; no optimizer reset.',
        accounting='Whole accepted CE91641755/reference100M/source ledger3068 unchanged if completed. Additional memory gradients, finite observations and rejected block source exposures separate; no equal-total-supervision claim.',
        persistence='Every accepted block saved atomically; metrics contain only accepted rows and identify boundary-only constraint. On interruption resume the last accepted block, not an internal tentative update.',
        probe='CPU fullstate/whole-block rollback/final short block; actual CUDA2blocks continuous versus1+1, four20-update timing blocks, strict inherited state/LR/finite/boundary loss; cached unchanged projector control reused as such.',
        measured_budget='3068*measured source update +154*(5 native MATH memory forwards+1 full memory gradient+snapshot/save), warmup,1.3margin+200evaluation; all previous related diagnostics and own probe included within2400 seconds.',
        no_rescue='No block cadence, memory, ceiling, margin, projector/backtrack, LR, source, mask, order, checkpoint or decoder sweep. Failure terminal, all original quality gates unchanged.')
    proposal['references']=dict(p['references'],per_update_budget_failure=original.reference(ROOT/'reports/phase6/finite_Web_constraint_budget_rejected.json'),
        compiled_budget_failure=original.reference(ROOT/'reports/phase6/compiled_Web_oracle_terminal.json'))
    atomic_json(path,proposal);print('Defined fixed20 boundary research, not old per-update adoption; new GPU0.')


if __name__=='__main__':main()
