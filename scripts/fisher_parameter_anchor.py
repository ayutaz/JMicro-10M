"""Fixed-context conditional Monte Carlo Fisher; no empirical-Fisher fallback.

Scores use independent model-sampled labels at unchanged TRAIN contexts. Squaring
each row's sum/sqrt(total supported tokens), then summing rows and averaging
replicates, estimates the token-weighted mean diagonal conditional Fisher. It
does not estimate a joint ancestral sequence Fisher or guarantee finite losses.
"""
import copy
import hashlib
import math
from pathlib import Path
from types import SimpleNamespace
import time

import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel

from jmicro.experiment import sha256
from jmicro.training import autocast, synchronize
from condition_positive_loss import positive_weighted_ce
from parameter_displacement_anchor_trainer import ParameterAnchorTrainer

KIND = 'fixed_context_conditional_MC_Fisher_parameter_anchor_v1'


def tensor_digest(values):
    digest = hashlib.sha256()
    for name, value in values.items():
        digest.update(name.encode())
        digest.update(str(value.dtype).encode())
        digest.update(str(tuple(value.shape)).encode())
        digest.update(value.detach().cpu().contiguous().numpy().tobytes())
    return digest.hexdigest()


def validate_field(named, field):
    if not named or len({id(p) for _, p in named}) != len(named):
        raise ValueError('Unique named parameters required')
    if [k for k, _ in named] != list(field):
        raise ValueError('Ordered field parameter identity differs')
    total = 0.
    for name, parameter in named:
        value = field[name]
        if (value.shape != parameter.shape or value.dtype != torch.float32
                or value.requires_grad or not bool(torch.isfinite(value).all())
                or bool(value.lt(0).any())):
            raise ValueError('Finite nonnegative aligned FP32 fixed field required')
        total += float(value.double().sum())
    if total <= 0 or not math.isfinite(total):
        raise ValueError('Nonzero finite field trace required; no uniform fallback')
    return total / sum(p.numel() for _, p in named)


def normalize_field(named, raw):
    if [k for k, _ in named] != list(raw):
        raise ValueError('Raw field parameter identity differs')
    if any(v.shape != p.shape or not bool(torch.isfinite(v).all())
           or bool(v.lt(0).any()) or v.requires_grad for (k, p), v in zip(named, raw.values(), strict=True)):
        raise ValueError('Finite nonnegative aligned raw field required')
    trace = sum(float(v.double().sum()) for v in raw.values())
    coordinates = sum(p.numel() for _, p in named)
    mean = trace / coordinates
    if not math.isfinite(mean) or mean <= 0:
        raise ValueError('Nonzero finite field trace required; no uniform fallback')
    field = {k: (v / mean).float() for k, v in raw.items()}
    actual = validate_field(named, field)
    if not math.isclose(actual, 1., rel_tol=2e-6):
        raise ValueError('Global unique-coordinate mean-one field required')
    return field, dict(raw_trace=trace, raw_coordinate_mean=mean,
                      unique_coordinates=coordinates, normalized_coordinate_mean=actual)


def sampled_score_loss(logits, labels, mask, total_body_tokens):
    if labels.shape != mask.shape or logits.shape[:-1] != labels.shape or mask.dtype != torch.bool:
        raise ValueError('Exact conditional score shapes required')
    if total_body_tokens <= 0 or not bool(mask.any()):
        raise ValueError('Positive body-token support required')
    return F.cross_entropy(logits[mask], labels[mask], reduction='sum') / math.sqrt(total_body_tokens)


def estimate_field(model, memory, seed, replicates=2, check=lambda: None, progress=lambda **_: None):
    named = list(model.named_parameters())
    if not named or any(p.dtype != torch.float32 or not p.requires_grad for _, p in named):
        raise ValueError('Native FP32 trainable parameters required')
    if len({id(p) for _, p in named}) != len(named) or type(replicates) is not int or replicates <= 0:
        raise ValueError('Unique parameters and positive integer replicates required')
    device = named[0][1].device
    x, y = memory['x'], memory['y']
    if (x.ndim != 2 or y.shape != x.shape or x.dtype != torch.int64 or y.dtype != torch.int64
            or bool(x.eq(0).any())):
        raise ValueError('Exact unpadded int64 context and target matrices required')
    support = y.ge(8)
    total = int(support.sum())
    if not total or not bool(support.any(dim=1).all()):
        raise ValueError('Every fixed row requires body support')
    generator = torch.Generator(device=device).manual_seed(seed)
    accumulators = {k: torch.zeros_like(p, dtype=torch.float64) for k, p in named}
    scores, sampled = [], []
    training = model.training
    model.eval()
    try:
        with torch.enable_grad(), sdpa_kernel(SDPBackend.MATH), torch.autocast(device_type=device.type, enabled=False):
            for repeat in range(replicates):
                for row in range(len(x)):
                    check()
                    synchronize(device)
                    started = time.perf_counter()
                    logits = model(x[row:row+1].to(device), training_fast_path=True).logits
                    mask = support[row:row+1].to(device)
                    if not bool(torch.isfinite(logits).all()):
                        raise ValueError('Nonfinite native conditional distribution')
                    # Sample the full vocabulary, including special IDs; only
                    # context support is masked, never the sampled vocabulary.
                    probabilities = logits[mask].detach().softmax(-1)
                    draw = torch.multinomial(probabilities, 1, generator=generator).squeeze(-1)
                    labels = torch.zeros(mask.shape, dtype=torch.int64, device=device)
                    labels[mask] = draw
                    loss = sampled_score_loss(logits, labels, mask, total)
                    gradients = torch.autograd.grad(loss, [p for _, p in named])
                    if not bool(torch.isfinite(loss)) or any(not bool(torch.isfinite(g).all()) for g in gradients):
                        raise ValueError('Nonfinite model-sampled score gradient')
                    for (name, _), gradient in zip(named, gradients, strict=True):
                        accumulators[name].add_(gradient.detach().double().square())
                    sampled.append(labels.detach().cpu())
                    synchronize(device)
                    seconds = time.perf_counter() - started
                    scores.append(dict(replicate=repeat, row=row, body_tokens=int(mask.sum()),
                                       score_loss=float(loss.detach()), seconds=seconds))
                    del logits, loss, gradients, probabilities, draw
                    progress(completed_score_gradients=len(scores), total_score_gradients=len(x)*replicates)
        raw = {k: v / replicates for k, v in accumulators.items()}
        field, normalization = normalize_field(named, raw)
        return dict(field={k: v.cpu() for k, v in field.items()},
                    sampled_labels=torch.cat(sampled), support_mask=support.clone(),
                    scores=scores, normalization=normalization,
                    accounting=dict(score_gradient_calls=len(scores),
                        sampled_score_labels=total*replicates, physical_context_tokens=x.numel()*replicates,
                        ordinary_source_CE_teacher_tokens=0, optimizer_updates=0),
                    field_tensor_digest=tensor_digest(field), seed=seed, replicates=replicates)
    finally:
        model.train(training)


def weighted_parameter_penalty(named, anchor, field, coefficient):
    # Field values are validated once at construction and rehashed on save/load.
    if (not math.isfinite(coefficient) or coefficient < 0
            or [k for k, _ in named] != list(anchor) or list(anchor) != list(field)):
        raise ValueError('Fixed nonnegative coefficient and aligned unique field/anchor required')
    return coefficient/2 * torch.stack([
        ((p-anchor[k]).float().square()*field[k]).sum() for k, p in named]).sum()


class FisherAnchorTrainer(ParameterAnchorTrainer):
    def __init__(self, parent, pool, original, positive, goals, binding, coefficient,
                 field, field_binding, device='cuda', context=1024, batch=32):
        if field_binding['parent'] != binding['parent']:
            raise ValueError('Field estimated at a different parent')
        super().__init__(parent, pool, original, positive, goals, binding, coefficient, device, context, batch)
        named = list(self.model.named_parameters())
        mean = validate_field(named, field)
        if not math.isclose(mean, 1., rel_tol=2e-6):
            raise ValueError('Frozen global mean-one field required')
        self.field = {k: v.detach().to(self.device).clone() for k, v in field.items()}
        self.field_initial_digest = tensor_digest(self.field)
        if self.field_initial_digest != field_binding['field_tensor_digest']:
            raise ValueError('Frozen field tensor digest differs')
        self.spec.update(research_kind=KIND, fisher_trainer_sha256=sha256(Path(__file__)),
                         field_binding=copy.deepcopy(field_binding), field_normalization='unique_global_coordinate_mean_one')
        self.lineage.update(kind=KIND, field_initial_digest=self.field_initial_digest,
                            field_binding=copy.deepcopy(field_binding))

    def step(self):
        synchronize(self.device)
        started = time.perf_counter()
        x, y, byte_count, focused = self.sampler.batch(self.spec['batch'])
        if x.eq(0).any():
            raise ValueError('Unpadded input required')
        digest = hashlib.sha256(bytes.fromhex(self.token_digest))
        digest.update(x.numpy().astype('<i8').tobytes())
        digest.update(y.numpy().astype('<i8').tobytes())
        focus_digest = hashlib.sha256(bytes.fromhex(self.focus_token_digest))
        focus_digest.update(focused.numpy().astype(np.uint8).tobytes())
        waited = time.perf_counter()-started
        self.optimizer.zero_grad(set_to_none=True)
        self.model.train()
        x, y, focused = x.to(self.device), y.to(self.device), focused.to(self.device)
        with sdpa_kernel(SDPBackend.FLASH_ATTENTION if self.spec['backend']=='flash' else SDPBackend.MATH), autocast(self.device, self.spec['dtype']):
            logits = self.forward(x, training_fast_path=True).logits
            ce, counts = positive_weighted_ce(logits, y, focused, 1)
        penalty = weighted_parameter_penalty(list(self.model.named_parameters()), self.anchor, self.field, self.coefficient)
        loss = ce+penalty
        loss.backward()
        norm = torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1., error_if_nonfinite=True)
        values = [float(v.detach()) for v in (loss, ce, penalty)]
        if not all(math.isfinite(v) for v in values):
            raise ValueError('Finite CE/Fisher parameter penalty required')
        lr = self.optimizer.param_groups[0]['lr']
        self.optimizer.step()
        self.scheduler.step()
        self.update += 1
        self.tokens += x.numel()
        self.supervised_tokens += counts['ordinary_teacher_tokens']
        self.body_bytes += byte_count
        self.focus_teacher_tokens += counts['outcome_focus_teacher_tokens']
        self.weighted_teacher_mass += counts['weighted_teacher_mass']
        self.token_digest, self.focus_token_digest = digest.hexdigest(), focus_digest.hexdigest()
        self.audit_counters()
        synchronize(self.device)
        seconds = time.perf_counter()-started
        return dict(update=self.update, loss=values[0], CE_loss=values[1], parameter_penalty=values[2],
            parameter_coefficient=self.coefficient, gradient_norm=float(norm), lr=lr, tokens_seen=self.tokens,
            supervised_tokens=self.supervised_tokens, body_bytes_seen=self.body_bytes,
            token_digest=self.token_digest, focus_token_digest=self.focus_token_digest,
            focus_teacher_tokens=self.focus_teacher_tokens, weighted_teacher_mass=self.weighted_teacher_mass, outcome_weight=1,
            source_teachers=self.sampler.source_teachers.copy(), source_eos=self.sampler.source_eos.copy(),
            source_input_tokens=self.sampler.source_tokens.copy(), source_body_bytes=self.sampler.source_body_bytes.copy(),
            source_focus_teachers=self.sampler.source_focus_teachers.copy(), seconds=seconds, data_wait_seconds=waited,
            tokens_per_second=x.numel()/seconds, valid_input_tokens=self.tokens-self.lineage['parent_tokens'],
            physical_input_tokens=self.tokens-self.lineage['parent_tokens'],
            additional_teacher_tokens=self.supervised_tokens-self.lineage['parent_supervised_tokens'],
            parameter_penalty_teacher_tokens=0)

    def save(self, path):
        if tensor_digest(self.field) != self.field_initial_digest:
            raise ValueError('Fixed Fisher field changed')
        return super().save(path)

    def load(self, path):
        if tensor_digest(self.field) != self.field_initial_digest:
            raise ValueError('Fixed Fisher field changed')
        super().load(path)
        if self.lineage['field_initial_digest'] != self.field_initial_digest:
            raise ValueError('Saved Fisher field differs')
