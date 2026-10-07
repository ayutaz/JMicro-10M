"""Pin one Japanese teacher and a same-request source feasibility comparison."""
import dataclasses
import hashlib
import json
import os
from pathlib import Path
import sys

os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN'] = '1'
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'),
                str(Path(__file__).resolve().parents[1] / 'scripts')]
from huggingface_hub import HfApi
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from probe_sarashina_prose_teacher import train_requests


def main():
    meta_path = ROOT / 'reports/phase6/sarashina_prose_teacher_metadata.json'
    proposal_path = ROOT / 'reports/phase6/sarashina_prose_feasibility_proposal.json'
    if meta_path.exists() or proposal_path.exists():
        raise ValueError('Preserve pinned preparation; no model/request sweep')
    prior = ROOT / 'reports/phase6/public_prose_teacher_content_review.json'
    old = read_json(prior)
    if old['accepted'] or old['weak'] != 37 or len(old['notes']) != 64:
        raise ValueError('Prior actual64 rejected teacher evidence required')
    rows = train_requests(64)
    old_requests = read_json(ROOT / 'reports/phase6/public-prose-teacher-probe-20261006/requests.json')
    if rows != old_requests:
        raise ValueError('Use all exact64 prior TRAIN requests, not outcome-selected prompts')
    info = HfApi(token=False).model_info(
        'sbintuitions/sarashina2.2-3b-instruct-v0.1', files_metadata=True, token=False)
    license_name = info.card_data.to_dict().get('license')
    if info.private or info.gated or license_name != 'mit':
        raise ValueError('Anonymous public MIT teacher required')
    allowed = {'config.json', 'generation_config.json', 'tokenizer.json',
               'tokenizer.model', 'tokenizer_config.json', 'special_tokens_map.json',
               'added_tokens.json', 'model.safetensors.index.json', 'README.md', 'LICENSE'}
    files = []
    for entry in info.siblings:
        if entry.rfilename in allowed or entry.rfilename.endswith('.safetensors'):
            lfs = dataclasses.asdict(entry.lfs) if dataclasses.is_dataclass(entry.lfs) else entry.lfs
            files.append(dict(path=entry.rfilename, bytes=entry.size, blob_id=entry.blob_id, lfs=lfs))
    meta = dict(status='public_anonymous_pinned_teacher_metadata_not_recovered',
                repo_id=info.id, revision=info.sha, private=info.private, gated=info.gated,
                license=license_name, files=files, total_bytes=sum(f['bytes'] for f in files),
                created_at=now(), anonymous_access=True, teacher_precision='BF16',
                model_url='https://huggingface.co/' + info.id)
    write_json(meta_path, meta)
    source_names = ['prepare_sarashina_prose_teacher.py', 'recover_sarashina_prose_teacher.py',
                    'recover_sarashina_prose_teacher.ps1', 'probe_sarashina_prose_teacher.py',
                    'probe_sarashina_prose_teacher.ps1', 'review_public_prose_teacher.py']
    proposal = dict(
        status='single_new_Japanese_teacher_exact64_contract_frozen_before_recovery_or_GPU',
        created_at=now(), question='Does an independently pretrained Japanese teacher supply coherent plain prose on the unchanged64 TRAIN scenarios where the prior public teacher failed?',
        teacher_repo=info.id, teacher_revision=info.sha, teacher_license=license_name,
        teacher_metadata_sha256=sha256(meta_path), teacher_precision='BF16',
        recovery_limit_seconds=1800, teacher_probe_GPU_limit_seconds=180,
        fixed_source_content_cases=64, source_seed=2026100681,
        source_sha256={'scripts/' + n: sha256(ROOT / 'scripts' / n) for n in source_names},
        previous_review=dict(path=str(prior), sha256=sha256(prior), weak=37, accepted=False),
        request_digest=hashlib.sha256(json.dumps(rows, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
        changed='Teacher model/codec and its official chat template only; model size and pre/posttraining are confounded. Student stays native10M.',
        unchanged='Exact all64 scenario/prompt/id/family/split/seed; batch8, temperature.7/top_p.8/top_k20/max_new_tokens256; BF16/SDPA; allraw IDs/text/stops retained.',
        rationale='Prior37/64 weak prose and latest paired gate1/80 coherent show that cheap unchanged mature-parent optimizer/attention adjustments have not solved generation. Test a Japanese-pretrained source provider once; official Japanese benchmarks are selection rationale, not proof of this source or student quality.',
        novelty_limit='Registered docs/config/scripts have no Sarashina/calm2/Rakuten/Swallow match. This is not a claim about unregistered work or a pure language-pretraining causal comparison.',
        content_acceptance='Existing weak<=10/64 and zero unresolved retained grammar errors; read every generated body with raw-bound individual reasons. Unfinished, role, instruction, malformed or causal/grammar errors are weak and excluded. No automatic model/prompt/sampling retries.',
        completion='Recover fixed revision and verify each file once; actual64 BF16 outputs, all64 individual judgments, accepted-only source token rate and raw GPU/VRAM evidence. Stop this exact route on source failure. If it passes, freeze a feasible production token/GPU budget from measured timing before new source creation; no source10M or student quality claimed from64.',
        next_controlled_comparison='Only after accepted new source exists: define one matched native10M Base TRAIN comparison using a qualified strong Base parent/reference, preserve Web guard and all generation criteria, independent seed/fullDEV/protectedTEST/adoption. No automatic continuation of failed historical parent recipes.',
        primary_sources=[meta['model_url'], meta['model_url'] + '/blob/' + info.sha + '/LICENSE',
                         'https://arxiv.org/abs/2305.07759'],
        student_parameters=10001152, student_training_started=False,
        student_scientific_teacher_tokens=0, Chat_started=False, quantization_started=False,
        protected_test_used=False, Base_complete=False, Base_adopted=False,
        no_post_outcome_model_prompt_threshold_sweep=True)
    write_json(proposal_path, proposal)
    print(json.dumps(dict(repo_id=info.id, revision=info.sha, bytes=meta['total_bytes'],
                          exact_TRAIN_requests=len(rows), GPU_limit_seconds=180)))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
