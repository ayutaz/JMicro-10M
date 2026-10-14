"""Prospective fresh FIM protocol on the unchanged original TRAIN stream.

Transform AFTER native draw/quota masking. Consequently original documents,
windows, update grouping, supervised identities and material RNG are matched.
Long units retain all native AR windows. No new structural vocabulary or role
IDs, no tokenizer retraining, no data selection and no generated targets.
"""
import copy
import hashlib
import json
import random

from base_kv_allocation_trainer import CEOnlyOriginalSampler
from jmicro.fim_compatibility import MARKERS, serialize_psm, utf8_token_boundaries

KIND = 'original_TRAIN_post_quota_FIM_PSM_single_window_v1'
POLICY = dict(kind=KIND, probability=.5, markers=list(MARKERS), marker_targets='ignore_-100',
    span='two_uniform_distinct_interior_codec_stable_original_token_boundaries',
    eligible='complete_original_document_body_plus_EOS_at_most512',
    long_units='unchanged_native_AR_all_windows', original_gold='identities_and_quota_mask_preserved',
    context=1024, data_rng='unchanged_native_seed', augmentation_rng='separate_seed_xor_0xF1A0',
    EOS_semantics='original_EOS_identity_ends_middle_reconstruction_in_augmented_rows')


def native_stream_payload(rows):
    return json.dumps([(r['index_byte_position'], r['index_record_sha256'],
                       r['input_ids'], r['target_ids']) for r in rows]).encode()


class FimOriginalSampler(CEOnlyOriginalSampler):
    def __init__(self, pool, manifest_sha256, tokenizer, goals, seed=42):
        super().__init__(pool, manifest_sha256, tokenizer, goals, seed)
        self.fim_rng = random.Random(seed ^ 0xF1A0)
        self.fim = dict(rows=0, eligible_rows=0, applied_rows=0, marker_inputs=0,
                        selected_original_teachers=0, native_stream_digest='0'*64)

    def take(self, size):
        rows = super().take(size)
        self.fim['native_stream_digest'] = hashlib.sha256(
            bytes.fromhex(self.fim['native_stream_digest']) + native_stream_payload(rows)).hexdigest()
        for row in rows:
            self.fim['rows'] += 1
            chosen = self.fim_rng.random() < POLICY['probability']
            row.update(FIM_applied=False, FIM_eligible=False, FIM_cuts=None, FIM_marker_inputs=0)
            if row['original_body_tokens'] + 1 > 512:
                continue
            if (not row['original_document_first_window'] or row['input_start'] != 0
                    or row['target_first'] != 1 or row['target_end'] != row['original_body_tokens'] + 2
                    or row['input_ids'][0] != 2
                    or len(row['input_ids']) != row['original_body_tokens'] + 1):
                raise ValueError('Eligible unit must be one complete original native window')
            body = row['input_ids'][1:]
            interior = utf8_token_boundaries(body, self.tokenizer)[1:-1]
            if len(interior) < 2:
                continue
            self.fim['eligible_rows'] += 1
            row['FIM_eligible'] = True
            if not chosen:
                continue
            cuts = tuple(sorted(self.fim_rng.sample(interior, 2)))
            form = serialize_psm(body, self.tokenizer, cuts, context=POLICY['context'])
            old_targets = row['target_ids']
            ids = list(form.ids[:-1])
            targets = [old_targets[p] if p is not None else -100
                       for p in form.original_positions[1:]]
            if len(ids) != len(targets) or sum(t != -100 for t in targets) != row['teacher_tokens']:
                raise ValueError('Quota-selected original teacher count changed')
            # Independently restore ALL native labels, including masked quota tails.
            restored = [t for p, t in sorted((p, t) for p, t in
                zip(form.original_positions[1:], targets) if p is not None)]
            if restored != old_targets or targets.count(3) != row['original_EOS_targets']:
                raise ValueError('Original gold identity, partial quota or EOS mask changed')
            if form.original_body_sha256 != row['full_original_body_sha256']:
                raise ValueError('Original full document bytes changed')
            row.update(input_ids=ids, target_ids=targets, FIM_applied=True,
                       FIM_cuts=list(cuts), FIM_marker_inputs=form.marker_tokens)
            self.fim['applied_rows'] += 1
            self.fim['marker_inputs'] += form.marker_tokens
            self.fim['selected_original_teachers'] += row['teacher_tokens']
        return rows

    def state_dict(self):
        state = super().state_dict()
        state.update(kind=KIND, FIM_policy=copy.deepcopy(POLICY),
                     FIM_RNG=self.fim_rng.getstate(), FIM_counters=copy.deepcopy(self.fim))
        return state

    def validate_state(self, state):
        current = self.state_dict()
        if any(state.get(k) != current[k] for k in ('kind', 'binding', 'seed', 'goals', 'FIM_policy')):
            raise ValueError('FIM sampler recipe/binding differs')
        f = state.get('FIM_counters', {})
        if (set(f) != set(self.fim) or any(type(f[k]) is not int or f[k] < 0
                for k in set(f) - {'native_stream_digest'})
                or f['rows'] != state['windows_emitted']
                or not 0 <= f['applied_rows'] <= f['eligible_rows'] <= f['rows']
                or f['marker_inputs'] != f['applied_rows'] * sum(len(self.tokenizer.encode(m)) for m in MARKERS)
                or f['selected_original_teachers'] > sum(state['consumed'].values())
                or not isinstance(f['native_stream_digest'], str)
                or len(f['native_stream_digest']) != 64):
            raise ValueError('FIM completed-row counters differ')
        try:
            bytes.fromhex(f['native_stream_digest'])
            random.Random().setstate(state['FIM_RNG'])
            random.Random().setstate(state['RNG'])
        except (ValueError, TypeError, KeyError) as e:
            raise ValueError('Actual saved augmentation/material RNG required') from e
        if (set(state['consumed']) != set(self.goals) or set(state['pending']) != set(self.goals)
                or any(type(n) is not int or not 0 <= n <= self.goals[g]
                       for g,n in state['consumed'].items())):
            raise ValueError('Original quota cursors differ')
        for genre, windows in state['pending'].items():
            for row in windows:
                if (row['source'] != genre or len(row['input_ids']) != len(row['target_ids'])
                        or not 0 < len(row['input_ids']) <= POLICY['context']
                        or any(type(i) is not int or not 0 <= i < self.tokenizer.vocab_size
                               for i in row['input_ids'])
                        or any(type(i) is not int or (i != -100 and i != 3
                               and not 8 <= i < self.tokenizer.vocab_size) for i in row['target_ids'])):
                    raise ValueError('Original pending window shape/source/IDs differ')
        if not f['rows'] and state['FIM_RNG'] != random.Random(self.seed ^ 0xF1A0).getstate():
            raise ValueError('Actual fresh augmentation seed required at zero rows')

    def load_state_dict(self, state):
        self.validate_state(state)
        super().load_state_dict(state)
        self.fim_rng.setstate(state['FIM_RNG'])
        self.fim = copy.deepcopy(state['FIM_counters'])
