"""Persistent full192-case no-update CUDA teacher/native semantic diagnostic."""
import json
import os
from pathlib import Path
import sys
import time
os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN'] = '1'
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn.attention import SDPBackend, sdpa_kernel
from transformers import AutoModelForCausalLM
from jmicro.experiment import ROOT, now, sha256
from jmicro.training import atomic_json, gpu_lock
from jmicro.tokenizer import Tokenizer
from jmicro.model import JMicroModel
from jmicro.japanese_evaluation import NativeLikelihood
from phase6_performance import identity, alive
from teacher_semantic_signal import hf_scores, case_scores, summary, compare

CONFIG = ROOT/'configs/phase6/teacher_semantic_signal.json'
RUN = ROOT/'reports/phase6/teacher-semantic-signal-20261007'


def read(path):
    return json.loads(Path(path).read_text())


def main():
    torch.set_num_threads(2)
    config = read(CONFIG)
    for relative, expected in config['source_sha256_bindings'].items():
        if sha256(ROOT/relative) != expected:
            raise ValueError('Frozen semantic code/codec changed')
    packet = Path(config['packet_path'])
    if sha256(packet) != config['packet_sha256']:
        raise ValueError('Dev-only encoded packet changed')
    recovery_path = Path(config['recovery_path'])
    if sha256(recovery_path) != config['recovery_sha256']:
        raise ValueError('Verified model recovery changed')
    for file in read(recovery_path)['files']:
        stat = Path(file['path']).stat()
        if stat.st_size != file['bytes'] or stat.st_mtime_ns != file['mtime_ns']:
            raise ValueError('Verified teacher files changed')
    checkpoint = Path(config['checkpoint_path'])
    original_stat = checkpoint.stat()
    if original_stat.st_size != config['checkpoint_bytes'] or original_stat.st_mtime_ns != config['checkpoint_mtime_ns']:
        raise ValueError('Verified native checkpoint changed')
    if not torch.cuda.is_available():
        raise RuntimeError('Actual CUDA required')
    job_path = RUN/'job.json'
    if job_path.exists():
        old = read(job_path)
        if alive(old):
            raise ValueError('Actual semantic process live; no duplicate')
        if old['status'] == 'complete':
            print('Completed full192 diagnostic retained')
            return
        raise ValueError('Preserve incomplete diagnostic; diagnose before a versioned repair')
    data = read(packet)
    cases, encoded = data['cases'],data['encoded']
    job = dict(status='running',**identity(),started_at=now(),config_sha256=sha256(CONFIG),
        GPU_seconds=0,optimizer_updates=0,scientific_teacher_tokens=0,Base_complete=False,
        Chat_started=False,quantization_started=False,
        restart_command='scripts/run_teacher_semantic_signal.ps1 -Worker (inspect saved job first; completed run is never repeated)')
    atomic_json(job_path,job)
    start = None
    all_rows = {}
    model_stats = {}

    def heartbeat(stage,completed=0):
        job.update(stage=stage,completed_cases_in_stage=completed,heartbeat_at=now(),
            GPU_seconds=0 if start is None else time.monotonic()-start)
        atomic_json(job_path,job)

    def check():
        if start is not None and time.monotonic()-start > config['GPU_limit_seconds']:
            raise TimeoutError('Full semantic GPU180s budget exhausted')

    try:
        with gpu_lock('cuda'):
            start = time.monotonic()
            for name in ('teacher','native10M'):
                check()
                begin = time.monotonic()
                heartbeat('load_'+name)
                torch.cuda.reset_peak_memory_stats()
                if name == 'teacher':
                    model = AutoModelForCausalLM.from_pretrained(config['model_directory'],local_files_only=True,
                        trust_remote_code=False,dtype=torch.bfloat16,attn_implementation='sdpa').to('cuda').eval()
                    batch = config['teacher_batch_cases']
                    scorer = None
                else:
                    saved = torch.load(checkpoint,map_location='cpu',weights_only=False)
                    model = JMicroModel(saved['model_config']).to('cuda').eval()
                    model.load_state_dict(saved['model'],strict=True)
                    if sum(p.numel() for p in model.parameters()) != 10001152:
                        raise ValueError('Keep native10M parameter count')
                    del saved
                    batch = config['native_batch_cases']
                    scorer = NativeLikelihood(model,Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model'),
                        'cuda','bf16',batch=batch*2)
                output = []
                seconds = []
                for offset in range(0,192,batch):
                    check()
                    part = cases[offset:offset+batch]
                    requests = [r for g in encoded[name][offset:offset+batch] for r in g['requests']]
                    torch.cuda.synchronize()
                    tick = time.monotonic()
                    if name == 'teacher':
                        scores = hf_scores(model,requests)
                    else:
                        with sdpa_kernel(SDPBackend.MATH):
                            scores = scorer.score_encoded(requests)
                    torch.cuda.synchronize()
                    seconds.append(time.monotonic()-tick)
                    for index, case in enumerate(part):
                        output.append(case_scores(case,scores[index*2:index*2+2]))
                    atomic_json(RUN/(name+'-partial.json'),dict(config_sha256=sha256(CONFIG),rows=output))
                    heartbeat('score_'+name,len(output))
                check()
                grads_none = all(p.grad is None for p in model.parameters())
                if not grads_none or model.training:
                    raise ValueError('Inference mode with no gradients required')
                model_stats[name] = dict(seconds_including_load=time.monotonic()-begin,
                    scoring_seconds=sum(seconds),batch_seconds=seconds,peak_allocated_bytes=torch.cuda.max_memory_allocated(),
                    all_gradients_none=grads_none,eval_mode=True,summary=summary(output),
                    model_specific_BOS=config['teacher_bos'] if name == 'teacher' else 2,
                    total_forward_tokens=sum(len(r['ids'])-1 for g in encoded[name] for r in g['requests']))
                all_rows[name] = output
                atomic_json(RUN/(name+'-complete.json'),dict(config_sha256=sha256(CONFIG),rows=output,stats=model_stats[name]))
                del model,scorer
                torch.cuda.empty_cache()
            matched = compare(all_rows['teacher'],all_rows['native10M'])
            t = model_stats['teacher']['summary']
            signal = (t['accuracy']['ci95'][0] > .5 and t['both_contexts_hard_correct']['ci95'][0] > .25
                and matched['paired_teacher_minus_student_accuracy']['ci95'][0] > 0)
            check()
        final_stat = checkpoint.stat()
        if (final_stat.st_size,final_stat.st_mtime_ns) != (original_stat.st_size,original_stat.st_mtime_ns):
            raise ValueError('Native checkpoint file changed during readonly inference')
        result = dict(status='all192_matched_teacher_native_semantic_diagnostic_complete',created_at=now(),
            config_sha256=sha256(CONFIG),actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
            source_sha256=config['source_sha256'],packet_sha256=config['packet_sha256'],selection=config['selection'],
            teacher_model=config['model'],teacher_revision=config['revision'],
            native_checkpoint_sha256=config['checkpoint_sha256'],native_parameters=10001152,
            rows=all_rows,models=model_stats,comparison=matched,teacher_context_signal_passed=signal,
            signal_gate=config['signal_gate'],GPU_seconds=time.monotonic()-start,
            optimizer_updates=0,scientific_teacher_tokens=0,new_prepared_training_tokens=0,
            model_files_unchanged=True,no_logits_or_representations_used_for_training=True,
            Base_complete=False,Chat_started=False,quantization_started=False,
            protected_test_records_JSON_decoded=False,Chat_roles_or_templates=False,EOS_scored=False,
            no_case_exclusions_or_truncation=True,all_codec_roundtrips_and_boundaries_verified=True,
            next_action='Teacher context signal supports defining a genuinely new finite contextual/relational knowledge-transfer comparison against matched CE; first probe useful teacher features on TRAIN-only contexts, no direct cross-tokenizer logit matching.' if signal else
                'Close this readonly teacher diagnostic; contextual knowledge-transfer evidence is insufficient under the predeclared gate. Do not rescue with prompts/model/threshold sweeps.',
            limitations=config['limitations']+' These are constructed dev cases, not independent human evaluation or global task capability. Pretraining contamination of the external teacher is unknown. Likelihood ability is not proof that hidden-state transfer works.')
        atomic_json(RUN/'result.json',result)
        job.update(status='complete',ended_at=now(),stage='complete',GPU_seconds=result['GPU_seconds'],
            completed_cases_in_stage=192,teacher_context_signal_passed=signal)
        atomic_json(job_path,job)
        print(dict(status=result['status'],teacher=t['accuracy'],native=model_stats['native10M']['summary']['accuracy'],
            teacher_both=t['both_contexts_hard_correct'],paired_difference=matched['paired_teacher_minus_student_accuracy'],
            signal_passed=signal,GPU_seconds=result['GPU_seconds']))
    except BaseException as error:
        job.update(status='failed',ended_at=now(),error_type=type(error).__name__)
        heartbeat('failed_preserved')
        raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
