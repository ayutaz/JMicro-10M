"""Verify codecs and freeze the full192-case readonly teacher/native comparison."""
import json
import os
from pathlib import Path
import sys
os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN'] = '1'
os.environ['HF_HUB_OFFLINE'] = '1'
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from transformers import AutoTokenizer
from jmicro.experiment import ROOT, now, sha256
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import encode_request
from teacher_semantic_signal import dev_cases, hf_request
from recover_public_prose_teacher import META, RUN as RECOVERY

CONFIG = ROOT/'configs/phase6/teacher_semantic_signal.json'
RUN = ROOT/'reports/phase6/teacher-semantic-signal-20261007'
PROPOSAL = ROOT/'reports/phase6/base_teacher_semantic_signal_proposal.json'


def read(path):
    return json.loads(Path(path).read_text())


def main():
    if CONFIG.exists():
        raise ValueError('Preserve pre-inference semantic contract')
    proposal = read(PROPOSAL)
    source = ROOT/proposal['source']
    if sha256(source) != proposal['source_sha256'] or proposal['GPU_limit_seconds'] != 180:
        raise ValueError('Use unchanged proposed source and budget')
    rows, selection = dev_cases(source)
    teacher_spec, student_spec = proposal['models']
    meta = read(META)
    recovery_path = RECOVERY/'result.json'
    recovery = read(recovery_path)
    if (teacher_spec['name'] != meta['repo_id'] or teacher_spec['revision'] != meta['revision']
            or recovery['metadata_sha256'] != sha256(META) or meta['private'] or meta['gated']
            or meta['license'] != 'apache-2.0' or read(RECOVERY/'job.json')['status'] != 'complete'):
        raise ValueError('Verified public pinned teacher required')
    for file in recovery['files']:
        stat = Path(file['path']).stat()
        if stat.st_size != file['bytes'] or stat.st_mtime_ns != file['mtime_ns']:
            raise ValueError('Previously verified public model changed')
    model_dir = Path(teacher_spec['model_directory'])
    bos = read(model_dir/'config.json')['bos_token_id']
    hf = AutoTokenizer.from_pretrained(model_dir, local_files_only=True, trust_remote_code=False)
    native_path = ROOT/'artifacts/phase2/4096/tokenizer.model'
    native = Tokenizer(native_path)
    encoded = {}
    for name in ('teacher','native10M'):
        groups = []
        for row in rows:
            requests = [(row['context'],choice) for choice in row['choices']]
            entries = [hf_request(hf,bos,a,b,1024) for a,b in requests] if name == 'teacher' else [encode_request(native,a,b,1024) for a,b in requests]
            groups.append(dict(id=row['id'], requests=entries))
        encoded[name] = groups
    for a,b in zip(encoded['teacher'],encoded['native10M'],strict=True):
        if a['id'] != b['id'] or [r['target_bytes'] for r in a['requests']] != [r['target_bytes'] for r in b['requests']]:
            raise ValueError('Keep common original continuation bytes and case IDs')
    checkpoint = ROOT/student_spec['checkpoint']
    if sha256(checkpoint) != student_spec['sha256']:
        raise ValueError('Unchanged original10B checkpoint required')
    stat = checkpoint.stat()
    RUN.mkdir(parents=True, exist_ok=True)
    packet = RUN/'dev-only-encoded.json'
    atomic_json(packet,dict(cases=rows,encoded=encoded,selection=selection))
    paths = ['scripts/teacher_semantic_signal.py','scripts/prepare_teacher_semantic_signal.py',
        'scripts/run_teacher_semantic_signal.py','scripts/run_teacher_semantic_signal.ps1',
        'scripts/phase6_performance.py','src/jmicro/japanese_evaluation.py','src/jmicro/model.py',
        'src/jmicro/tokenizer.py','src/jmicro/evaluation.py','uv.lock']
    atomic_json(CONFIG, dict(status='all192_dev_codec_preflight_and_contract_frozen_before_GPU',created_at=now(),
        proposal_sha256=sha256(PROPOSAL), source_sha256=sha256(source), selection=selection,
        packet_path=str(packet),packet_sha256=sha256(packet),
        model_directory=str(model_dir), model=meta['repo_id'],revision=meta['revision'],teacher_bos=bos,
        recovery_path=str(recovery_path),recovery_sha256=sha256(recovery_path),
        checkpoint_path=str(checkpoint),checkpoint_sha256=student_spec['sha256'],
        checkpoint_bytes=stat.st_size,checkpoint_mtime_ns=stat.st_mtime_ns,
        native_tokenizer_sha256=sha256(native_path),source_sha256_bindings={p:sha256(ROOT/p) for p in paths},
        GPU_limit_seconds=180,teacher_batch_cases=4,native_batch_cases=16,
        maximum_input_tokens=1024,teacher_dtype='bfloat16',native_dtype='bf16',teacher_attention='sdpa',native_attention='math',
        signal_gate='teacher family-bootstrap accuracy CI lower>.5 AND both-context-hard-correct CI lower>.25 AND paired teacher-native accuracy CI lower>0; all192 finite raw-bound cases mandatory',
        all192_codec_boundaries_and_original_byte_roundtrips_verified=True,
        native_BOS=2,Chat_roles_or_templates=False,EOS_scored=False,protected_test_records_JSON_decoded=False,
        new_weight_download_bytes=0,optimizer_updates=0,scientific_teacher_tokens=0,
        Base_complete=False,Chat_started=False,quantization_started=False,
        limitations=proposal['interpretation'],no_post_outcome_model_prompt_threshold_sweep=True))
    print(dict(cases=192,families=96,other_records_opaque=selection['other_records_opaque'],
        all_codec_roundtrips=True,teacher_BOS=bos,native_BOS=2,
        teacher_target_tokens=sum(len(r['target_ids']) for g in encoded['teacher'] for r in g['requests']),
        native_target_tokens=sum(len(r['target_ids']) for g in encoded['native10M'] for r in g['requests']),
        config_sha256=sha256(CONFIG)))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
