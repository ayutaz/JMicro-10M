"""Fixed source intervention and verified shared Web prefix, before any new GPU."""
from pathlib import Path
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import json
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.training import atomic_json
from phase6_performance import alive,finite_state
from prepare_livedoor_leads import RUN,CONFIG,inspect,reference
from run_eos_short_pilot import equal_state

DESTINATION=ROOT/'reports/phase6/livedoor_base_comparison_proposal.json'
CONTROL=ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006'
CONTROL_CONFIG=ROOT/'configs/phase6/source_order_condition_comparison_v2.json'


def main():
    started=time.monotonic();torch.set_num_threads(2);inspect()
    if DESTINATION.exists():raise ValueError('Preserve original news comparison definition')
    review=read_json(RUN/'content-review.json');ready=read_json(RUN/'ready.json')
    if not review['passed'] or review['weak_documents']>10 or review['sample']!=ready['sample']:
        raise ValueError('Original actual accepted64 news required')
    c=read_json(CONTROL_CONFIG);job=read_json(CONTROL/'job.json')
    if job['status']!='complete' or alive(job):raise ValueError('Actually terminal cached native staged100M required')
    history_path=CONTROL/'source_order/training/metrics.jsonl'
    history={r['update']:r for r in (json.loads(s) for s in history_path.read_text().splitlines())}
    if len(history)!=3068 or history[max(history)]['source_teachers']!={'web':75000000,'story':5000000,'ordinary_textbook':10000000,'conditional_textbook':10000000}:
        raise ValueError('Original100M complete source exposure required')
    candidates=[]
    for path in (CONTROL/'source_order/training').glob('checkpoint-*.pt'):
        update=int(path.stem.split('-')[-1]);row=history.get(update)
        if row and all(not row['source_teachers'][key] for key in ('story','ordinary_textbook','conditional_textbook')):
            candidates.append((update,path))
    if not candidates:raise ValueError('Actual saved Web-only prefix required; do not rerun75M')
    update,path=max(candidates);state=torch.load(path,map_location='cpu',weights_only=False)
    original=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
    if sha256(Path(c['parent']['path']))!=c['parent']['sha256']:raise ValueError('Original d18 parent hash required')
    web=state['sampler']['source_teachers']['web'];row=history[update]
    if (not finite_state(state) or state['lineage']['parent']!=c['parent'] or state['update']!=update
            or state['supervised_tokens']-original['supervised_tokens']!=web or not 0<web<75000000
            or state['sampler']['source_teachers']!={'web':web,'story':0,'ordinary_textbook':0,'conditional_textbook':0}
            or not equal_state(state['sampler']['source_teachers'],row['source_teachers'])
            or state['token_digest']!=row['token_digest'] or state['focus_token_digest']!=row['focus_token_digest']
            or len(state['optimizer']['param_groups'])!=2 or any(g['lr']!=.00001 for g in state['optimizer']['param_groups'])
            or not equal_state(state['lineage']['actual_parent_sampler'],original['sampler'])):
        raise ValueError('Actual common native-only-Web weights/Adam/RNG/cursor lineage differs')
    with torch.random.fork_rng(devices=[]):model=JMicroModel(state['model_config'])
    model.load_state_dict(state['model'],strict=True)
    if sum(p.numel() for p in model.parameters())!=10001152 or model.lm_head.weight is not model.model.embed_tokens.weight:
        raise ValueError('Original native tied10M architecture required')
    cursor=state['sampler']['streams']['web']['sampler'];initial=original['sampler']['web']
    blocks=(cursor['epoch']-initial['epoch'])*initial['blocks']+cursor['position']-initial['position']
    if blocks*initial['context']!=state['sampler']['source_tokens']['web']:
        raise ValueError('Actual reused Web cursor/input budget differs')
    seconds=time.monotonic()-started
    if seconds>30:raise TimeoutError('CPU30s source definition exhausted')
    proposal=dict(kind='authored_Japanese_news_vs_synthetic_native_Base100M_v1',created_at=now(),preparation_CPU_seconds=seconds,
        source_preparation=reference(CONFIG),source_ready=reference(RUN/'ready.json'),source_content_review=reference(RUN/'content-review.json'),
        original_parent=c['parent'],cached_control_config=reference(CONTROL_CONFIG),cached_control_result=reference(CONTROL/'compare-result.json'),
        cached_control_history=reference(history_path),shared_prefix=reference(path),shared_prefix_update=update,
        reused_prefix_teacher_tokens=web,new_teacher_goals=dict(web=75000000-web,authored_news=25000000),
        new_scientific_teacher_tokens=100000000-web,candidate_total_teacher_tokens_from_original_parent=100000000,
        reused_prefix_input_tokens=state['tokens']-original['tokens'],reused_prefix_Web_cursor=cursor,
        prefix_selection='Largest completed cached checkpoint with all short-source teacher counts zero, determined from source ledger only. No checkpoint quality evaluation or selection.',
        native_parameters=10001152,optimizer_policy='inherit actual cached common-prefix native Adam/scheduler/RNG; unchanged LR1e-5, seed42 news stream. No reheat or fresh optimizer.',
        data=dict(original_web=c['original_web'],news_pool=ready['pool'],news_manifest_sha256=ready['manifest_sha256']),
        source_order=['web','authored_news'],body_and_EOS_weights=1.,news_prepared_body_tokens=523883,news_prepared_stream_tokens=533983,
        news_epochs_of_teacher_exposure=25000000/(523883+5050),
        interventions='Replace post-Web25M story/ordinary/conditional targets with original authored-news paragraphs. Corpus, EOS density and diversity change together; not quantity-only or exact matched-input/physical/update count comparison.',
        quality_selection='Unchanged strong staged coherence>=31 and positive paired CI, EOS>=76/repetition<=2; absolute grammar56/coherence27/appropriate27/EOS37/repetition<=18/errors0; original Web BPB<=.9812859519097707; all source/finite/accounting/evaluation proof. Only eligible recipe proceeds to independent learned seed/full dev/protected test/adoption.',
        evaluation='Same dev256 common bytes/Japanese192-331-1119/native80 max64 greedy/suppressed and bridge/retention512each, all80 raw-bound individual content review. Cached control not rerun.',
        own_CUDA_probe_ceiling_seconds=120,total_new_GPU_ceiling_seconds=1800,scientific_GPU_frozen=False,
        new_GPU_seconds=0,Base_complete=False,Base_adopted=False,protected_test_used=False,Chat_started=False,quantization_started=False,
        completion_condition='Implement exact two-source/inherited-state trainer and evaluator/review, test actual save/resume and source budgets; own CUDA4vs2+2/32timing and estimate1.3margin+300eval+probe within1800 before science freeze. Single recipe; no source/selector/epoch/LR/decoder/checkpoint rescue.',
        limitations=review['limitations'])
    atomic_json(DESTINATION,proposal)
    print(dict(CPU_seconds=seconds,prefix_teachers=web,new_teacher_tokens=100000000-web,news_epochs=proposal['news_epochs_of_teacher_exposure'],GPU_seconds=0))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
