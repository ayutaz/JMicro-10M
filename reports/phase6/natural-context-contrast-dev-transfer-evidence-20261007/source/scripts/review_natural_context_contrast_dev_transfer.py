"""Review saved64 retrieval scores; this diagnostic cannot adopt a Base."""
import json
from pathlib import Path
import sys

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import numpy as np
import torch
from torch.nn import functional as F
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
from run_natural_context_contrast_dev_transfer import RUN, CONFIG


def review():
    job, result, config = (read_json(p) for p in (RUN/'job.json', RUN/'result.json', CONFIG))
    if (job['status'] != 'complete' or result['status'] != 'complete' or alive(job)
            or result['config_sha256'] != sha256(CONFIG) or job['config_sha256'] != sha256(CONFIG)
            or result['actual_identity'] != {k:job[k] for k in ('pid','boot_id','start_ticks')}
            or not 0 < result['GPU_occupancy_seconds'] <= 60
            or result['GPU_occupancy_seconds'] != job['GPU_occupancy_seconds']
            or result['new_teacher_tokens'] or result['optimizer_updates']):
        raise ValueError('Actual completed bounded readonly process required')
    for ref in (config['cases'], config['proposal'], config['recipe'],
                config['dev_manifest'], config['reference_body']):
        if sha256(Path(ref['path'])) != ref['sha256']:
            raise ValueError('Frozen source binding differs')
    if any(sha256(ROOT/p) != digest for p,digest in config['source_sha256'].items()):
        raise ValueError('Scoring implementation differs')
    cases = read_json(Path(config['cases']['path']))['rows']
    ids = [r['doc_id'] for r in cases]
    if len(ids) != 64 or len(set(ids)) != 64:
        raise ValueError('All64 fixed original DEV pairs required')
    summaries, scores = {}, {}
    if set(result['results']) != {'original','CE','contrast'}:
        raise ValueError('All three documented models required')
    for arm, record in result['results'].items():
        if (record['checkpoint'] != config['checkpoints'][arm]
                or record['input_cases_sha256'] != config['cases']['sha256']
                or record['pairs'] != 64 or record['parameters'] != 10001152
                or record['dtype'] != 'bf16' or record['backend'] != 'math'
                or [r['doc_id'] for r in record['rows']] != ids):
            raise ValueError('Same input/checkpoint/native scoring required')
        matrix = torch.tensor(record['cosine_matrix'], dtype=torch.float32)
        if matrix.shape != (64,64) or not bool(torch.isfinite(matrix).all()):
            raise ValueError('Finite complete retrieval matrix required')
        diagonal = matrix.diag()
        mask = ~torch.eye(64, dtype=torch.bool)
        other = matrix.masked_fill(~mask, -torch.inf)
        values = []
        for i, row in enumerate(record['rows']):
            actual = dict(prefix_to_suffix_rank=int((matrix[i] > diagonal[i]).sum())+1,
                suffix_to_prefix_rank=int((matrix[:,i] > diagonal[i]).sum())+1,
                prefix_to_suffix_unique_top1=bool(diagonal[i] > other[i].max()),
                suffix_to_prefix_unique_top1=bool(diagonal[i] > other[:,i].max()),
                prefix_positive_ties=int((matrix[i] == diagonal[i]).sum()),
                suffix_positive_ties=int((matrix[:,i] == diagonal[i]).sum()))
            if any(actual[k] != row[k] for k in actual):
                raise ValueError('Raw matrix/rank/tie accounting differs')
            values.append((actual['prefix_to_suffix_unique_top1'] +
                           actual['suffix_to_prefix_unique_top1']) / 2)
        labels = torch.arange(64)
        loss = float((F.cross_entropy(matrix/.1, labels) + F.cross_entropy(matrix.T/.1, labels))/2)
        if abs(loss-record['symmetric_InfoNCE']) > 1e-6 or np.mean(values) != record['bidirectional_unique_top1']:
            raise ValueError('Raw matrix/summary accounting differs')
        scores[arm] = np.asarray(values)
        summaries[arm] = {k:record[k] for k in ('bidirectional_unique_top1','symmetric_InfoNCE',
            'mean_positive_cosine','mean_distractor_cosine','representation_variance')}
    rng = np.random.default_rng(42)
    sample = rng.integers(0,64,size=(2000,64))
    differences = {}
    for control, candidate in (('original','CE'),('CE','contrast'),('original','contrast')):
        delta = scores[candidate]-scores[control]
        differences[f'{candidate}_minus_{control}'] = dict(point=float(delta.mean()),
            CI95=np.quantile(delta[sample].mean(1),[.025,.975]).tolist(),
            document_units=64, directions_correlated=True, case_difference=dict(zip(ids,delta.tolist())))
    prior = read_json(ROOT/'reports/phase6/natural_context_contrast_comparison_review.json')
    if any(prior['eligible_for_final_Base_validation'].values()) or prior['Base_complete']:
        raise ValueError('Preserve original failed Base outcome')
    report = dict(status='all_three_fixed_DEV64_retrieval_models_reviewed',created_at=now(),
        reviewer_sha256=sha256(Path(__file__)), result_sha256=sha256(RUN/'result.json'),
        config_sha256=sha256(CONFIG), actual_identity=result['actual_identity'],
        GPU_occupancy_seconds=result['GPU_occupancy_seconds'], summaries=summaries,
        paired_document_differences=differences,
        prior_Base_review_sha256=sha256(ROOT/'reports/phase6/natural_context_contrast_comparison_review.json'),
        conclusion='Contrast transfers some observed document-pair discrimination to this fixed DEV packet. Original failed generation and retention outcomes remain unchanged; retrieval does not certify appropriate next-token continuation, semantic reasoning or Base quality.',
        new_teacher_tokens=0,optimizer_updates=0,protected_test_used=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        quality_criteria_unchanged=True,one_shot_diagnostic_closed=True,
        limitations='Retrospective diagnostic, fixed64 documents and unknown near-family correlations. Bootstrap resamples document pairs, not128 independent directions, and is not an independent seed or natural-Japanese population guarantee. Variance is retained from actual scoring; matrices do not reconstruct feature coordinates.',
        next_action='Check whether conditional-likelihood sensitivity on the same original DEV prefixes/suffixes differs from embedding discrimination. Define a separate bounded readonly diagnostic before execution; do not rescue rejected training or adopt a Base from retrieval.')
    if (RUN/'review.json').exists():
        raise ValueError('Preserve one-shot review')
    atomic_json(RUN/'review.json',report)
    atomic_json(ROOT/'reports/phase6/natural_context_contrast_dev_transfer_review.json',report)
    print(json.dumps(dict(summaries=summaries,paired={k:{s:v[s] for s in ('point','CI95')}
        for k,v in differences.items()})))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2)
    review()
