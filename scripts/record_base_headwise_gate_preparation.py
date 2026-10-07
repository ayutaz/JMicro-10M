"""Preserve initial evidence and record corrected, CPU-verified gate preparation."""
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
import argparse
import ast
import copy
import json
from pathlib import Path
import sys
import urllib.request
import xml.etree.ElementTree as ET

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json
from phase6_performance import alive
from base_headwise_gate_model import ARMS,POLICY

PHASE = ROOT/'reports/phase6'


def reference(path):
    return dict(path=str(path),sha256=sha256(path))


def forward_and_construction_AST(path):
    tree = ast.parse(path.read_text())
    # Only the static-state loader predicate changed. Check the complete module
    # AST after removing that method, not merely a claimed unchanged forward.
    for node in tree.body:
        if isinstance(node,ast.ClassDef) and node.name=='HeadwiseGateModel':
            node.body = [child for child in node.body if not (
                isinstance(child,ast.FunctionDef) and child.name=='load_state_dict')]
    return ast.dump(tree,include_attributes=False)


def main():
    destination = PHASE/'base_headwise_gate_preparation_v2.json'
    if destination.exists():raise ValueError('Preserve completed gate preparation record')
    proposal_path = PHASE/'base_headwise_gate_proposal.json'
    proposal,parity = read_json(proposal_path),read_json(PHASE/'base_headwise_gate_parent_CPU_parity.json')
    if (proposal['scientific_configuration_frozen'] or proposal['scientific_started']
            or proposal['GPU_seconds'] or proposal['total_GPU_ceiling_seconds']!=9000
            or proposal['probe_GPU_ceiling_seconds']!=180 or proposal['policy']!=POLICY
            or proposal['arms']!=list(ARMS)):
        raise ValueError('Original unstarted fixed gate contract required')
    snapshot = PHASE/'base-headwise-gate-preparation-v1/source/scripts/base_headwise_gate_model.py'
    current = ROOT/'scripts/base_headwise_gate_model.py'
    if sha256(snapshot)!=parity['source_sha256']['scripts/base_headwise_gate_model.py']:
        raise ValueError('Actual initial parity implementation must be preserved')
    if forward_and_construction_AST(snapshot)!=forward_and_construction_AST(current):
        raise ValueError('Initial actual-parent parity cannot be reused after forward/construction changes')
    if (not parity['original_model_unchanged'] or not parity['RNG_unchanged']
            or parity['CPU_seconds']>30 or parity['GPU_seconds'] or len(parity['observations'])!=2
            or any(not all(o['checks'].values()) or len(o['rows'])!=24 for o in parity['observations'])):
        raise ValueError('All48 original-parent exact finite CPU outputs required')
    tests = PHASE/'base_headwise_gate_CPU_tests_v2.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if (sum(int(s.get('tests',0)) for s in suites)!=33
            or any(int(s.get(k,0)) for s in suites for k in ('failures','errors','skipped'))):
        raise ValueError('Current33 actual CPU model/trainer/evaluator checks required')
    ui = read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:
        model = json.load(response)
    if not alive(ui) or model['checkpoint_sha256']!=proposal['parent']['sha256'] or model['busy']:
        raise ValueError('Original actual idle UI required')
    sources = ('scripts/base_headwise_gate_model.py','scripts/base_headwise_gate_trainer.py',
        'scripts/base_headwise_gate_evaluation.py','scripts/prepare_base_headwise_gate.py',
        'scripts/record_base_headwise_gate_preparation.py','tests/test_base_headwise_gate_model.py',
        'tests/test_base_headwise_gate_trainer.py','src/jmicro/model.py','scripts/natural_context_contrast_corpus.py',
        'scripts/natural_context_contrast_trainer.py','scripts/run_complete_text_comparison.py')
    record = dict(status='matched_headwise_gate_model_trainer_typed_evaluator_CPU_verified_GPU_unstarted',
        created_at=now(),prospective_contract=reference(proposal_path),
        preserved_original_parent_parity=reference(PHASE/'base_headwise_gate_parent_CPU_parity.json'),
        preserved_model_source=reference(snapshot),
        all_non_loader_model_AST_unchanged=True,current_CPU_tests=reference(tests),CPU_tests=33,
        model_checks=16,trainer_and_evaluation_checks=17,
        initial_failures=dict(model_fixture=reference(PHASE/'base_headwise_gate_model_tests_initial.xml'),
            trainer_static_validation=reference(PHASE/'base_headwise_gate_trainer_tests_initial_failure.xml'),
            preparation_input_assumption=reference(PHASE/'base_headwise_gate_parent_CPU_preparation_initial_failure.json')),
        repair='Static gate checkpoint validation incorrectly matched SwiGLU MLP gate_proj as well as the added attention gate. Restrict the predicate to .self_attn.gate_proj.weight. Keep static gates zero; add a successful static model/Adam roundtrip and both-arm full trainer resume checks. Model forward/conversion, optimizer, teachers, caps and quality policy unchanged. No scientific config had been frozen.',
        source_sha256={name:sha256(ROOT/name) for name in sources},policy=copy.deepcopy(POLICY),
        parent=proposal['parent'],goals=proposal['goals'],source_binding=proposal['source_binding'],
        native_parameters=10001152,study_parameters_each=10014464,
        added_parameters_each=13312,total_proposed_scientific_teachers=200000000,
        new_scientific_teacher_tokens=0,GPU_seconds=0,quality_generations=0,
        total_GPU_ceiling_seconds=9000,probe_GPU_ceiling_seconds=180,
        scientific_configuration_frozen=False,CUDA_verified=False,scientific_started=False,
        same_original_full_sampler_and_CE_verified=True,typed_likelihood_cache_generation_factory_verified=True,
        fullstate_CPU4_vs_2_save_2_both_arms_verified=True,partial_update_save_continue_refused=True,
        UI=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},actual_alive=True,model=model),
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,quality_criteria_unchanged=True,
        next_action='Implement durable paired CUDA probe/launcher and science runner/reviewer. Probe both actual arms4vs2+2 fullstate/history,48x1024 BF16 finite resident90percent, and all32 aggregate timings. Start paired100M only if both prospective forecasts plus measured probe fit9000; fixed science and quality conditions unchanged.')
    atomic_json(destination,record)
    print(json.dumps(dict(status=record['status'],CPU_tests=33,initial_CPU_forward_unchanged=True,
                          GPU_seconds=0,UI_pid=ui['pid'])))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    argparse.ArgumentParser(description=__doc__).parse_args();main()
