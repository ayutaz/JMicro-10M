"""Create the fixed context-mixing runners from preserved baseline harnesses."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]


def convert(name):
    source = ROOT/name
    target = ROOT/name.replace('base_muon','base_context_mixing')
    if target.exists(): raise ValueError('Preserve existing context-mixing command: '+str(target))
    text = source.read_text()
    text = text.replace('MuonTrainer','ContextMixingTrainer').replace('finite_muon_state','finite_context_mixing_state')
    text = text.replace('base_muon','base_context_mixing').replace('base-muon','base-context-mixing')
    text = text.replace('muon','context_mixing').replace('Muon','ContextMixing').replace('4800','7200')
    text = text.replace('from base_context_mixing_trainer import ContextMixingTrainer, finite_context_mixing_state',
        'from base_context_mixing_trainer import ContextMixingTrainer\nfrom base_context_mixing_state import finite_context_mixing_state')
    text = text.replace('from base_context_mixing_trainer import KIND, finite_context_mixing_state',
        'from base_context_mixing_trainer import KIND\nfrom base_context_mixing_state import finite_context_mixing_state')
    return target,text


def function(text, name, body):
    begin=text.index('def '+name+'(')
    end=text.index('\n\ndef ',begin+1)
    return text[:begin]+body.rstrip()+'\n'+text[end:]


def main():
    files={}
    for name in ('scripts/probe_base_muon.py','scripts/probe_base_muon.ps1',
                 'scripts/run_base_muon.py','scripts/run_base_muon.ps1',
                 'scripts/review_base_muon.py','scripts/complete_base_muon_probe.py',
                 'scripts/complete_base_muon.py','tests/test_base_muon_run.py'):
        path,text=convert(name)
        if name=='scripts/probe_base_muon.py':
            text=text.replace('from base_context_mixing_state import finite_context_mixing_state',
                'from base_context_mixing_state import finite_context_mixing_state, CapacitySampler')
            text=text.replace("'tests/test_base_context_mixing_trainer.py',", "'tests/test_base_context_mixing_trainer.py', 'scripts/base_context_mixing_state.py',")
            text=function(text,'prepare', '''def prepare():
    if CONFIG.exists(): raise ValueError('Preserve one fixed context-mixing probe')
    proposal = read_json(PROPOSAL)
    for name,digest in proposal['source_sha256'].items():
        if sha256(ROOT/name) != digest: raise ValueError('Verified CPU prototype changed')
    tests = ROOT/'reports/phase6/base_context_mixing_trainer_tests.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites) != 9 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Nine actual CPU protocol checks required')
    if proposal['CPU_tests']['sha256'] != sha256(tests): raise ValueError('Verified CPU receipt changed')
    old = read_json(ROOT/'configs/phase6/base_muon_comparison.json')
    old_probe = read_json(ROOT/'configs/phase6/base_muon_probe.json')
    fields = ('parent','parent_size','parent_mtime_ns','source_binding','goals','tokenizer','tokenizer_sha256',
              'dev_shards','dev_manifest_sha256','suite_sha256','evaluation')
    plan = dict(**{k:old[k] for k in fields}, created_at=now(), proposal=ref(PROPOSAL), CPU_tests=ref(tests),
        source_sha256={s:sha256(ROOT/s) for s in SOURCES}, payload=old_probe['payload'],
        batch=48, seed=42, context_mixing_probability=.05, context_prediction_passes=1,
        probe_GPU_cap_seconds=180, total_GPU_cap_seconds=7200,
        warmup_updates=3, timed_updates=32, control_CE=old['control_CE'],
        control_result=ref(ROOT/'reports/phase6/natural-context-contrast-comparison-20261007/CE/train-result.json'),
        Base_complete=False, Chat_started=False, quantization_started=False)
    atomic_json(CONFIG, plan)
    print(json.dumps(dict(status='Context_mixing_protocol_frozen_GPU0',total_GPU_cap_seconds=7200,config_sha256=sha256(CONFIG))))
''')
            begin=text.index("            payload = read_json(p['payload']['path'])", text.index('def run('))
            end=text.index('            states, logs = [], []',begin)
            text=text[:begin]+'''            del t; clear()
            payload = read_json(p['payload']['path'])
            t = ContextMixingTrainer(parent,CapacitySampler(payload,tokenizer,48),binding,batch=48)
            torch.cuda.reset_peak_memory_stats()
            capacity_row = t.step(); histories['capacity'] = [capacity_row]
            torch.cuda.synchronize()
            capacity = dict(context=1024,target_stride=512,batch=48,
                original_target_positions=capacity_row['CE_targets_this_update'],
                peak_VRAM_bytes=torch.cuda.max_memory_allocated(),CE_loss=capacity_row['CE_loss'],
                gradient_norm=capacity_row['gradient_norm'],optimizer_updates=1,
                prediction_valid_inputs=capacity_row['prediction_valid_inputs_this_update'],
                prediction_physical_inputs=capacity_row['prediction_physical_inputs_this_update'],
                mixing_selected=capacity_row['mixing_selected_this_update'],
                mixing_changed=capacity_row['mixing_changed_this_update'],
                original_train_genre=payload['original_record']['source'])
            if (not finite_context_mixing_state(host(t.state_dict())) or
                not 0<capacity['gradient_norm']<float('inf') or not capacity['mixing_changed'] or
                capacity['peak_VRAM_bytes'] >= memory['allocator_allowance_bytes']):
                raise ValueError('Finite complete mixed-context worst-shape update required')
            del t; clear()
''' +text[end:]
            text=text.replace("optimizer_state=states[0]['optimizer']['names']", "context_mixing_state=states[0]['context_mixing']")
            text=text.replace("checks['full_sampler_matches_AdamW'] = equal_state(states[0]['sampler'],control.sampler.state_dict())",
                "checks['full_sampler_matches_AdamW'] = equal_state(states[0]['sampler'],control.sampler.state_dict())\n            checks['real_input_changes'] = states[0]['context_mixing']['changed_positions'] > 0\n            checks['prediction_forward_not_additional_supervision'] = states[0]['context_mixing']['prediction_valid_inputs'] == states[0]['counters']['CE_input_tokens']")
        if name=='scripts/run_base_muon.py':
            text=text.replace("'scripts/base_context_mixing_trainer.py', 'tests/test_base_context_mixing_run.py',",
                "'scripts/base_context_mixing_trainer.py', 'scripts/base_context_mixing_state.py', 'tests/test_base_context_mixing_run.py',")
            text=text.replace("optimizer='official_ContextMixing_hidden_matrix_match_rms_adamw_fresh_AdamW_tied_vocab_norms_lr1e-5_wd0.1_constant'",
                "optimizer='fresh_AdamW_lr1e-5_wd0.1_constant',context_mixing_probability=.05,context_prediction_passes=1")
            text=text.replace("scientific_CE_teacher_tokens=100000000,counters=state['counters'],sampler=state['sampler'],spec=state['spec'],lineage=state['lineage'])",
                "scientific_CE_teacher_tokens=100000000,counters=state['counters'],sampler=state['sampler'],spec=state['spec'],lineage=state['lineage'],context_mixing=state['context_mixing'])")
            text=text.replace("t.counters['update'] == t.optimizer.completed_steps", "finite_context_mixing_state(host(t.state_dict()))")
            text=text.replace('One fixed optimizer transition; no LR/momentum/NS/scaling/source/parent/batch/teacher/cap rescue',
                'One fixed history-mixing condition; no probability/passes/decoder/LR/source/parent/batch/teacher/cap rescue')
            text=text.replace('full native hybrid state','full native state and dedicated mixing RNG')
        if name=='scripts/review_base_muon.py':
            text=function(text,'audit_state', '''def audit_state(state, record, c):
    counters=state['counters']; steps=counters['update']; opt=state['optimizer']; mixed=state['context_mixing']
    if (not finite_context_mixing_state(state) or state['kind']!=KIND or state['binding']!=record['binding'] or
        state['spec']['optimizer_policy']!='fresh_equal_AdamW_both_arms' or
        state['spec']['batch']!=48 or state['spec']['seed']!=42 or state['spec']['contrast'] or
        state['spec']['context_mixing_probability']!=.05 or state['spec']['context_mixing_passes']!=1 or
        state['spec']['context_prediction']!='previous_position_greedy_body_only' or
        state['spec']['context_prediction_gradient'] or state['spec']['CE_labels']!='unaltered_original_gold' or
        state['model_config']['expected_parameter_count']!=10001152 or
        counters['supervised_tokens']!=100000000 or counters['source_teachers']!=c['goals'] or
        counters!=record['counters'] or not equal_state(state['sampler'],record['sampler']) or
        state['lineage']['parent']!=c['parent'] or counters['auxiliary_pairs'] or counters['auxiliary_input_tokens'] or steps<=0 or
        mixed!=record['context_mixing'] or not 0<mixed['changed_positions']<=mixed['selected_positions']<=mixed['eligible_positions'] or
        mixed['prediction_valid_inputs']!=counters['CE_input_tokens'] or
        mixed['prediction_physical_inputs']!=counters['physical_input_tokens'] or
        any(g['lr']!=1e-5 or g['weight_decay']!=.1 for g in opt['param_groups'])):
        raise ValueError('Exact native original100M/mixed-history committed state required')
''')
            text=text.replace('only optimizer transition differs','only CE conditioning inputs differ; extra prediction forwards accounted separately')
            needle="        raise ValueError('Final history/committed state counters differ')"
            text=text.replace(needle,needle+"\n    if history[steps]['context_mixing'] != state['context_mixing']:\n        raise ValueError('Final committed mixed-input history differs')")
            text=text.replace('Single seed and mature-parent optimizer transition; repeated nonblind DEV; heuristic update RMS and compute differ.',
                'Single seed and mature-parent history-mixing transition; repeated nonblind DEV; additional prediction compute. Fixed greedy variant is not full on-policy sampling or a likelihood-consistent objective.')
            text=text.replace("probe_GPU_seconds=c['probe_GPU_seconds'],all80_individually_read", "probe_GPU_seconds=c['probe_GPU_seconds'],context_mixing=state['context_mixing'],all80_individually_read")
        if name=='scripts/complete_base_muon_probe.py':
            text=text.replace('Same nominal LR/RMS heuristic does not make optimizer steps identical.',
                'Original gold teachers match CE, but inputs mix5percent predictions and prediction forwards add compute.')
            text=text.replace('single mature-parent transition','single fixed history-mixing transition')
            text=text.replace("'tests/test_base_context_mixing_trainer.py','tests/test_base_context_mixing_run.py')", "'tests/test_base_context_mixing_trainer.py','tests/test_base_context_mixing_run.py','scripts/base_context_mixing_state.py')")
        if name=='scripts/complete_base_muon.py':
            text=text.replace('no LR/momentum/NS/scaling/source/parent/batch/teacher/cap rescue',
                'no probability/passes/decoder/LR/source/parent/batch/teacher/cap rescue')
        if name=='tests/test_base_muon_run.py':
            text=text.replace("float('inf'),20000", "float('inf'),10000")
        # Retain old quality helpers verbatim; correct study descriptions only.
        text=text.replace('optimizer comparison','context-input comparison').replace('optimizer-only','context-input-only')
        text=text.replace('hybrid','native context-mixing')
        files[path]=text
    for path,text in files.items():
        path.write_text(text,encoding='utf-8',newline='\n')
    print('Created8 context-mixing commands/tests; old sources preserved')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
