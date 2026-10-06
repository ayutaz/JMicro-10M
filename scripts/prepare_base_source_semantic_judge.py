"""Freeze one judge/prompt and file-separated retrospective source diagnostic."""
import json
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, sha256
from jmicro.training import atomic_json
from base_source_semantic_judge import SYSTEM
from recover_public_prose_teacher import META, RUN as RECOVERY, DATA

CONFIG = ROOT/'configs/phase6/base_source_semantic_judge.json'


def main():
    if CONFIG.exists():
        raise ValueError('Preserve pre-inference contract; no prompt or outcome tuning')
    metadata = json.loads(META.read_text())
    recovery = json.loads((RECOVERY/'result.json').read_text())
    if (metadata['gated'] or metadata['private'] or metadata['license'] != 'apache-2.0'
            or recovery['metadata_sha256'] != sha256(META)
            or json.loads((RECOVERY/'job.json').read_text())['status'] != 'complete'):
        raise ValueError('Public pinned verified BF16 model recovery required')
    for file in recovery['files']:
        stat = Path(file['path']).stat()
        if stat.st_size != file['bytes'] or stat.st_mtime_ns != file['mtime_ns']:
            raise ValueError('Previously verified pinned model files changed')
    gold_path = ROOT/'reports/phase6/base_hq_acceptance_review.json'
    gold = json.loads(gold_path.read_text())
    actual_path = ROOT/'reports/phase6/base_hq_acceptance_sample.json'
    actual = json.loads(actual_path.read_text())
    sample = Path(actual['sample']['path'])
    if sha256(sample) != gold['sample_sha256'] or gold['summary']['documents'] != 64:
        raise ValueError('Unchanged original64 and full fixed linguistic gold required')
    files = json.loads((ROOT/'configs/phase6/base_hq_acceptance.json').read_text())['files']
    rows = json.loads(sample.read_text())['rows']
    development = [r['index'] for r in rows if r['source_file'] in files[:2]]
    holdout = [r['index'] for r in rows if r['source_file'] in files[2:]]
    if len(development) != 32 or len(holdout) != 32 or set(development) & set(holdout):
        raise ValueError('Fixed32/32 file-separated diagnostic required')
    paths = ['scripts/base_source_semantic_judge.py', 'scripts/run_base_source_semantic_judge.py',
        'scripts/run_base_source_semantic_judge.ps1', 'scripts/prepare_base_source_semantic_judge.py',
        'scripts/phase6_performance.py', 'scripts/recover_public_prose_teacher.py', 'uv.lock']
    atomic_json(CONFIG, dict(status='frozen_before_judge_inference', created_at=now(),
        model=metadata['repo_id'], revision=metadata['revision'], model_directory=str(DATA),
        model_license=metadata['license'], anonymous_local_reuse=True, new_weight_download_bytes=0,
        recovery_path=str(RECOVERY/'result.json'), recovery_sha256=sha256(RECOVERY/'result.json'),
        metadata_sha256=sha256(META), original_sample_path=str(sample), original_sample_sha256=sha256(sample),
        gold_path=str(gold_path), gold_sha256=sha256(gold_path),
        system_prompt=SYSTEM, source_sha256={p:sha256(ROOT/p) for p in paths},
        development_indices=development, holdout_indices=holdout, seed=2026100741,
        batch=4, maximum_input_tokens=8192, max_new_tokens=192, do_sample=False,
        dtype='bfloat16', attention='sdpa', truncation=False,
        GPU_limit_seconds=180, maximum_peak_allocated_bytes=22_000_000_000,
        gate=dict(minimum_accepted=8, minimum_precision=.9, minimum_recall=.5, maximum_format_errors=0),
        failure_action='Close this fixed model/prompt judge diagnostic; no post-outcome model/prompt/threshold sweep or repeated generation.',
        next_on_pass='Only classifier feasibility. Obtain truly new predeclared source-family64 acceptance and measured large-pool unique supply/protected-family exclusion before any Base training.',
        limitations='Retrospective nonblind Codex gold, not independent human truth. Prompt author previously read all64. File-separated judge holdout is neither untouched final Base test nor proof of global transfer. No gold reasons/labels/source IDs are given to the model. No model/prompt tuned on outputs. Prior Qwen prose-generation recipe failed and remains closed; this is a different classification mechanism, with no generated training prose.',
        Base_complete=False, Chat_started=False, quantization_started=False,
        prepared_training_tokens=0, scientific_teacher_tokens=0, optimizer_updates=0, GPU_seconds=0,
        primary_sources=['https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507', 'https://qwenlm.github.io/blog/qwen3/']))
    print(dict(model=metadata['repo_id'], revision=metadata['revision'], development=32, holdout=32,
        new_weight_download_bytes=0, GPU_limit_seconds=180, config_sha256=sha256(CONFIG)))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
