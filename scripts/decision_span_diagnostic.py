"""Exact cached likelihood decomposition at the first different candidate token."""
import hashlib
import json
import math

EPS=1e-9


def credit(margin):return .5 if abs(margin)<=EPS else float(margin>0)


def compare(gold,foil,g,f):
    for case,row in ((gold,g),(foil,f)):
        if (case['ids'][case['context_tokens']:]!=case['target_ids']
                or row['target_ids']!=case['target_ids'] or row['target_tokens']!=len(case['target_ids'])
                or row['target_bytes']!=case['target_bytes'] or len(row['token_nll'])!=len(case['target_ids'])
                or type(row['is_greedy']) is not bool or not row['token_nll']
                or any(not math.isfinite(v) or v<0 for v in row['token_nll'])
                or not math.isclose(row['log_likelihood'],-sum(row['token_nll']),abs_tol=EPS)):
            raise ValueError('Complete bound target IDs/bytes/token NLL/argmax conjunction required')
    width=gold['context_tokens']
    if (width!=foil['context_tokens'] or gold['prefix']!=foil['prefix']
            or gold['ids'][:width]!=foil['ids'][:width]):raise ValueError('Same context input required')
    common=0
    for a,b in zip(gold['target_ids'],foil['target_ids']):
        if a!=b:break
        common+=1
    gs,fs=sum(g['token_nll']),sum(f['token_nll'])
    result=dict(gold_body_NLL=gs,foil_body_NLL=fs,gold_body_tokens=g['target_tokens'],foil_body_tokens=f['target_tokens'],
        full_margins=dict(sum_log_likelihood=fs-gs,
            mean_token_log_likelihood=fs/f['target_tokens']-gs/g['target_tokens'],
            mean_byte_log_likelihood=fs/f['target_bytes']-gs/g['target_bytes']),
        gold_exact_greedy_body=g['is_greedy'],foil_exact_greedy_body=f['is_greedy'],shared_target_tokens=common)
    if common==min(g['target_tokens'],f['target_tokens']):
        result.update(status='identical_or_prefix_inclusion_no_scored_different_token',decision_margin=None)
        return result
    before=width+common
    if gold['ids'][:before]!=foil['ids'][:before]:raise ValueError('Earlier target context must be identical')
    margin=f['token_nll'][common]-g['token_nll'][common]
    result.update(status='same_input_first_distinct_token_scored',decision_index=common,decision_margin=margin,
        decision_input_sha256=hashlib.sha256(json.dumps(gold['ids'][:before],separators=(',',':')).encode()).hexdigest(),
        gold_decision_token=gold['target_ids'][common],foil_decision_token=foil['target_ids'][common],
        gold_decision_NLL=g['token_nll'][common],foil_decision_NLL=f['token_nll'][common],
        gold_postdecision_tokens=g['target_tokens']-common-1,
        gold_postdecision_NLL=sum(g['token_nll'][common+1:]),
        foil_postdecision_tokens=f['target_tokens']-common-1,
        foil_postdecision_NLL=sum(f['token_nll'][common+1:]),
        max_shared_target_NLL_difference=max((abs(a-b) for a,b in zip(g['token_nll'][:common],f['token_nll'][:common])),default=0.),
        full_sum_correct_but_decision_wrong=credit(fs-gs)==1 and credit(margin)==0,
        full_sum_correct_but_gold_body_not_greedy=credit(fs-gs)==1 and not g['is_greedy'])
    return result


def aggregate(rows):
    families={}
    for row in rows:families.setdefault(row['family'],{})[row['branch']]=row
    if any(set(group)!={0,1} for group in families.values()):raise ValueError('Both context poles required')
    scored=[r for r in rows if r['decision_margin'] is not None]
    both_scored=[g for g in families.values() if all(r['decision_margin'] is not None for r in g.values())]
    later_tokens=sum(r['gold_postdecision_tokens'] for r in scored)
    metrics={}
    for key in ('sum_log_likelihood','mean_token_log_likelihood','mean_byte_log_likelihood'):
        metrics[key]=dict(families=len(families),accuracy=sum(credit(r['full_margins'][key]) for r in rows)/len(rows),
            both_correct=sum(all(credit(r['full_margins'][key])==1 for r in g.values()) for g in families.values()),
            same_unique_candidate=sum(g[0]['full_margins'][key]*g[1]['full_margins'][key]<0 for g in families.values()),
            aligned_context_margin_shift=sum(g[0]['full_margins'][key]+g[1]['full_margins'][key]>0 for g in families.values()))
    return dict(families=len(families),all_context_poles=len(rows),scorable_decision_poles=len(scored),
        unscorable_context_poles=len(rows)-len(scored),families_both_decisions_scorable=len(both_scored),
        full_candidate=metrics,decision_correct=sum(credit(r['decision_margin'])==1 for r in scored),
        decision_wrong=sum(credit(r['decision_margin'])==0 for r in scored),decision_ties=sum(credit(r['decision_margin'])==.5 for r in scored),
        decision_accuracy_over_scorable=sum(credit(r['decision_margin']) for r in scored)/len(scored) if scored else None,
        decision_both_correct=sum(all(credit(r['decision_margin'])==1 for r in g.values()) for g in both_scored),
        full_sum_correct_but_decision_wrong=sum(r['full_sum_correct_but_decision_wrong'] for r in scored),
        full_sum_correct_but_gold_body_not_greedy=sum(r['full_sum_correct_but_gold_body_not_greedy'] for r in scored),
        gold_exact_greedy_body_poles=sum(r['gold_exact_greedy_body'] for r in rows),
        gold_exact_greedy_body_both_poles=sum(all(r['gold_exact_greedy_body'] for r in g.values()) for g in families.values()),
        gold_mean_decision_NLL=sum(r['gold_decision_NLL'] for r in scored)/len(scored) if scored else None,
        gold_postdecision_tokens=later_tokens,gold_mean_postdecision_token_NLL=sum(r['gold_postdecision_NLL'] for r in scored)/later_tokens if later_tokens else None,
        maximum_shared_target_NLL_difference=max((r['max_shared_target_NLL_difference'] for r in scored),default=0.))
