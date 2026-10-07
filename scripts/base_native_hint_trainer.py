"""Original CE plus a frozen native teacher's normalized middle-layer hints.

Hints use only original textbook/story supervised positions. No predictive KL,
middle CE head, adapter, new gold labels, or change to the inference model.
"""
import copy
import hashlib
import json
from pathlib import Path
import time
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.model import JMicroModel
from jmicro.training import synchronize, rng_state, restore_rng
from natural_context_contrast_corpus import NaturalCorpusTrainer, GENRES
from natural_context_contrast_trainer import right_pad
from base_native_teacher_KD_trainer import finite_KD_state

KIND = 'native_original_gold_CE_frozen_same_depth_middle_feature_cosine_v1'
RECIPE = dict(layer='floor_native_depth_over_two_after_completed_block',
    coefficient=1., sources=['textbook','story'],
    loss='sum_one_minus_FP32_unit_feature_dot_over_all_original_gold_positions',
    epsilon=1e-12, teacher_frozen_eval=True,
    teacher_forward='original_embedding_and_first_middle_blocks_no_norm_or_head',
    student_forward='one_full_native_decoder_original_final_CE_plus_middle_hint',
    extra_student_parameters=0, optimizer='fresh_AdamW_lr1e-5_wd0.1_constant',
    inference='unchanged_full_native_10M_no_teacher',
    commit_boundary='original_and_hint_counters_after_single_Adam_scheduler_update_v1')


def hidden_with_hint(model, ids, teacher_only=False):
    """Native causal blocks; capture the same completed middle block in both nets."""
    depth = len(model.model.layers)
    if depth < 2 or ids.shape[1] > model.config['max_position_embeddings']:
        raise ValueError('Native depth and context required')
    middle = depth // 2
    positions = torch.arange(ids.shape[1],device=ids.device)[None].expand_as(ids)
    x = model.model.embed_tokens(ids)
    hint = None
    for number, layer in enumerate(model.model.layers,1):
        x,_ = layer(x,positions,None,None,causal=True)
        if number == middle:
            hint = x
            if teacher_only: return None,hint
    return x,hint


def hint_loss(student, teacher, total_gold):
    if (student.ndim != 2 or student.shape != teacher.shape or not len(student)
        or type(total_gold) is not int or total_gold < len(student)):
        raise ValueError('Matching nonempty native features and original gold denominator required')
    student,teacher = student.float(),teacher.detach().float()
    if not bool(torch.isfinite(student).all() and torch.isfinite(teacher).all()):
        raise ValueError('Finite native features required')
    a = F.normalize(student,p=2,dim=-1,eps=RECIPE['epsilon'])
    b = F.normalize(teacher,p=2,dim=-1,eps=RECIPE['epsilon'])
    penalties = (1-(a*b).sum(-1)).clamp(0,2)
    return penalties.sum()/total_gold


def committed_state(state):
    try:
        if state['kind'] != KIND or state['spec']['native_hint'] != RECIPE: return False
        c,h = state['counters'],state['native_hint']; steps = c['update']
        sources = {g:(c['source_teachers'][g] if g in RECIPE['sources'] else 0) for g in GENRES}
        if (h['updates'] != steps or h['source_positions'] != sources or h['positions'] != sum(sources.values())
            or h['EOS'] != sum(c['source_EOS'][g] for g in RECIPE['sources'])
            or not 0 <= h['positions'] <= h['teacher_valid_inputs'] <= h['teacher_physical_inputs']
            or not 0 <= h['angular_penalty_sum'] <= 2*h['positions']
            or c['source_teachers'] != state['sampler']['consumed']
            or c['supervised_tokens'] != sum(c['source_teachers'].values())
            or c['auxiliary_input_tokens'] or c['auxiliary_pairs'] or c['auxiliary_digest'] != '0'*64
            or state['scheduler']['last_epoch'] != steps
            or any(int(v['step']) != steps for v in state['optimizer']['state'].values())
            or (steps and len(state['optimizer']['state']) != sum(len(g['params']) for g in state['optimizer']['param_groups']))):
            return False
        return finite_KD_state(state)
    except (KeyError,TypeError,ValueError,OverflowError):
        return False


class NativeHintTrainer(NaturalCorpusTrainer):
    def __init__(self,parent,sampler,binding,teacher_checkpoint,teacher_reference,batch=48,
                 contrast=False,device='cuda',seed=42):
        if contrast or parent['model_config'] != teacher_checkpoint['model_config']:
            raise ValueError('Same native architecture/codec and original CE source required')
        super().__init__(parent,sampler,binding,batch,False,device,seed)
        if self.model.config.get('dropout',0) != 0 or len(self.model.model.layers) < 2:
            raise ValueError('Deterministic native dropout0 depth required')
        self.spec.update(kind=KIND,native_hint=copy.deepcopy(RECIPE),teacher=copy.deepcopy(teacher_reference))
        self.lineage.update(kind=KIND,teacher=copy.deepcopy(teacher_reference),
            teacher_parent_update=teacher_checkpoint['update'],teacher_parent_tokens=teacher_checkpoint['tokens'])
        before = rng_state()
        self.teacher = JMicroModel(teacher_checkpoint['model_config']).to(self.device).eval()
        self.teacher.load_state_dict(teacher_checkpoint['model'],strict=True)
        self.teacher.requires_grad_(False)
        restore_rng(before)
        self.native_hint = dict(updates=0,positions=0,EOS=0,teacher_valid_inputs=0,
            teacher_physical_inputs=0,source_positions=dict.fromkeys(GENRES,0),
            angular_penalty_sum=0.,digest='0'*64)
        self._step_in_progress = False

    def state_dict(self):
        if self._step_in_progress: raise ValueError('Cannot serialize uncommitted native hint update')
        state = super().state_dict()
        state.update(kind=KIND,native_hint=copy.deepcopy(self.native_hint))
        return state

    def load(self,path):
        state = torch.load(Path(path),map_location=self.device,weights_only=False)
        if not committed_state(state): raise ValueError('Committed native hint state required')
        super().load(path)
        self.native_hint = copy.deepcopy(state['native_hint'])
        self._step_in_progress = False

    def step(self):
        if self._step_in_progress: raise ValueError('Interrupted update requires completed checkpoint resume')
        synchronize(self.device); started = time.monotonic(); self._step_in_progress = True
        rows = self.sampler.take(self.spec['batch']); wait = time.monotonic()-started
        ids,_ = right_pad([r['input_ids'] for r in rows],self.device)
        targets = torch.full_like(ids,-100)
        for i,r in enumerate(rows): targets[i,:len(r['target_ids'])] = torch.tensor(r['target_ids'],device=self.device)
        selected = targets.ne(-100); gold = sum(r['teacher_tokens'] for r in rows)
        if int(selected.sum()) != gold: raise ValueError('Exact original gold mask required')
        short = [i for i,r in enumerate(rows) if r['source'] in RECIPE['sources']]
        short_rows = torch.tensor([r['source'] in RECIPE['sources'] for r in rows],device=self.device)
        hint_selected = selected & short_rows[:,None]
        count = int(hint_selected.sum()); valid = physical = 0
        self.optimizer.zero_grad(set_to_none=True)
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        with sdpa_kernel(backend),torch.autocast(self.device.type,dtype=torch.bfloat16,enabled=self.device.type == 'cuda'):
            teacher_features = None
            if short:
                teacher_ids,_ = right_pad([rows[i]['input_ids'] for i in short],self.device)
                teacher_targets = torch.full_like(teacher_ids,-100)
                for j,i in enumerate(short):
                    teacher_targets[j,:len(rows[i]['target_ids'])] = torch.tensor(rows[i]['target_ids'],device=self.device)
                if not torch.equal(teacher_targets[teacher_targets.ne(-100)],targets[hint_selected]):
                    raise ValueError('Teacher and student original prediction positions differ')
                with torch.no_grad():
                    _,features = hidden_with_hint(self.teacher,teacher_ids,teacher_only=True)
                    teacher_features = features[teacher_targets.ne(-100)]
                valid = sum(len(rows[i]['input_ids']) for i in short); physical = teacher_ids.numel()
            final,middle = hidden_with_hint(self.model,ids)
            logits = self.model.lm_head(self.model.model.norm(final[selected])).float()
            ce = F.cross_entropy(logits,targets[selected]); auxiliary = ce.new_zeros(())
            if teacher_features is not None:
                auxiliary = hint_loss(middle[hint_selected],teacher_features,gold)
            combined = ce+RECIPE['coefficient']*auxiliary
        if not all(bool(torch.isfinite(v)) for v in (ce,auxiliary,combined)):
            raise ValueError('Finite original CE and native hint loss required')
        combined.backward()
        gradient = torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        self.optimizer.step(); self.scheduler.step(); self.counters['update'] += 1
        for k,v in dict(supervised_tokens=gold,CE_input_tokens=sum(len(r['input_ids']) for r in rows),
                        physical_input_tokens=ids.numel(),original_body_bytes=sum(r['teacher_body_bytes'] for r in rows)).items():
            self.counters[k] += v
        for r in rows:
            self.counters['source_teachers'][r['source']] += r['teacher_tokens']
            self.counters['source_EOS'][r['source']] += r['original_EOS_targets']
        if self.counters['source_teachers'] != self.sampler.consumed: raise ValueError('Completed original source cursor differs')
        stream = json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
        self.counters['token_digest'] = hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        h = self.native_hint; h['updates'] += 1; h['positions'] += count
        h['EOS'] += sum(rows[i]['original_EOS_targets'] for i in short)
        h['teacher_valid_inputs'] += valid; h['teacher_physical_inputs'] += physical
        h['angular_penalty_sum'] += float(auxiliary.detach())*gold
        for i in short: h['source_positions'][rows[i]['source']] += rows[i]['teacher_tokens']
        hint_stream = json.dumps([(rows[i]['index_byte_position'],rows[i]['index_record_sha256'],
                                  rows[i]['input_ids'],rows[i]['target_ids']) for i in short]).encode()
        h['digest'] = hashlib.sha256(bytes.fromhex(h['digest'])+hint_stream).hexdigest()
        self._step_in_progress = False; synchronize(self.device)
        return dict(**copy.deepcopy(self.counters),native_hint=copy.deepcopy(h),
            CE_loss=float(ce.detach()),hint_loss=float(auxiliary.detach()),combined_loss=float(combined.detach()),
            gradient_norm=float(gradient),lr=self.optimizer.param_groups[0]['lr'],committed_update=True,
            CE_targets_this_update=gold,hint_positions_this_update=count,teacher_valid_inputs_this_update=valid,
            teacher_physical_inputs_this_update=physical,total_physical_inputs_this_update=ids.numel()+physical,
            physical_inputs_this_update=ids.numel(),student_decoder_forwards_this_update=1,
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),original_windows_this_update=len(rows),
            seconds=time.monotonic()-started,data_wait_seconds=wait,
            draw_trace=[(r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],r['teacher_tokens']) for r in rows])
